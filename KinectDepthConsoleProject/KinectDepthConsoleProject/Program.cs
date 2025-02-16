using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Kinect;

namespace KinectServer
{
    class Program
    {
        private static KinectSensor _sensor;
        private static DepthImageStream _depthStream;
        private static short[] _depthData;
        private static TcpListener server;
        private static bool isRunning = true;

        static void Main(string[] args)
        {
            Console.WriteLine("Starting Kinect Server...");
            StartKinect();
            StartServerAsync().Wait();
        }

        static void StartKinect()
        {
            _sensor = KinectSensor.KinectSensors[0];

            if (_sensor != null)
            {
                _depthStream = _sensor.DepthStream;
                _depthStream.Enable();
                _depthData = new short[_depthStream.FramePixelDataLength];

                _sensor.DepthFrameReady += Sensor_DepthFrameReady;
                _sensor.Start();
            }
            else
            {
                Console.WriteLine("No Kinect sensor detected.");
                Environment.Exit(1);
            }
        }

        static void Sensor_DepthFrameReady(object sender, DepthImageFrameReadyEventArgs e)
        {
            using (DepthImageFrame depthFrame = e.OpenDepthImageFrame())
            {
                if (depthFrame != null)
                {
                    depthFrame.CopyPixelDataTo(_depthData);
                }
            }
        }

        static async Task StartServerAsync()
        {
            int port = 5005;
            server = new TcpListener(IPAddress.Any, port);
            server.Start();

            Console.WriteLine($"Server started on port {port}. Waiting for Python client...");

            while (isRunning)
            {
                try
                {
                    TcpClient client = await server.AcceptTcpClientAsync();
                    Console.WriteLine("Python client connected!");
                    _ = HandleClientAsync(client); // Fire-and-forget handling of this client
                }
                catch (SocketException ex)
                {
                    Console.WriteLine($"Socket Exception: {ex.Message}");
                }
            }
        }

        static async Task HandleClientAsync(TcpClient client)
        {
            using (client)
            using (NetworkStream stream = client.GetStream())
            {
                while (client.Connected)
                {
                    try
                    {
                        string depthData = GetDepthData() + "|END"; // Append delimiter
                        byte[] data = Encoding.UTF8.GetBytes(depthData);
                        await stream.WriteAsync(data, 0, data.Length);
                        await Task.Delay(20); // Reduced delay for faster updates (tune as needed)
                    }
                    catch (IOException)
                    {
                        Console.WriteLine("Client disconnected.");
                        break;
                    }
                }
            }
        }

        static string GetDepthData()
        {
            int width = _depthStream.FrameWidth;
            int height = _depthStream.FrameHeight;
            int stepSize = 10; // Adjust for resolution vs. message size
            StringBuilder depthString = new StringBuilder();

            for (int y = 0; y < height; y += stepSize)
            {
                for (int x = 0; x < width; x += stepSize)
                {
                    int index = x + (y * width);
                    int depth = _depthData[index] >> DepthImageFrame.PlayerIndexBitmaskWidth;

                    // You can remove the lower bound (800) if you wish to see all values,
                    // but note Kinect v1 has a minimum working range around 800mm.
                    if (depth < 1600)
                        depthString.Append(depth).Append(",");
                    else
                        depthString.Append("0,");
                }
                // Optionally, you could add a newline between rows for readability:
                depthString.Append("\n");
            }

            return depthString.ToString().TrimEnd('\n', ','); // Remove extra newline and comma
        }
    }
}

import serial
import time


def write_to_serial(ser):
    """Pan the motor"""

    while True:
        i = 180
        while i > 60: 
            i -= 10

            data = ser.readline().decode('utf-8').strip()
            oldata = data
            while len(data) != 0:
                oldata = data
                data = ser.readline().decode('utf-8').strip()

            if len(oldata) == 0:
                data = 1000 
            else:
                data = float(oldata)
                print(data)
            # this data is the distance from the ultrasonic sensor

            if data < 30:
                motors = [i - 10, 150, 85, 180]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))
                # data = float(ser.readline().decode('utf-8').strip())


                time.sleep(2)

                motors = [i - 10, 150, 85, 0]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))
                # data = float(ser.readline().decode('utf-8').strip())

                time.sleep(2)

                motors = [180, 30, 140, 150]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))
                # data = float(ser.readline().decode('utf-8').strip())

                break

            motors = [i, 85, 85, 180]
            out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
            ser.write(( out + '\n').encode('utf-8'))
            time.sleep(1)

            
            # motors = [i, 85, 85, 180]
            # out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
            # ser.write(( out + '\n').encode('utf-8'))

if __name__ == "__main__":
    try:
        ser = serial.Serial('/dev/cu.usbserial-142130', baudrate=9600, timeout=1)
        print("Serial port opened.")

        # Write to serial in the main thread
        write_to_serial(ser)
    
    except serial.SerialException as e:
        print(f"Serial error: {e}")


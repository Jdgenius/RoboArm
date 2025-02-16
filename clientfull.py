import serial
import time


def write_to_serial(ser):
    """Pan the motor"""

    while True:
        i = 180
        while i > 60: 
            i -= 10

            time.sleep(1)


            data = float(ser.readline().decode('utf-8').strip())
            
            print(data)

            # this data is the distance from the ultrasonic sensor

            if data < 10:
                motors = [i, 127, 85, 180]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))

                time.sleep(5)

                motors = [i, 127, 85, 0]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))

                time.sleep(5)

                motors = [180, 0, 85, 150]
                out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
                ser.write(( out + '\n').encode('utf-8'))

                break

            
            motors = [i, 85, 85, 180]
            out = f"{motors[0]},{motors[1]},{motors[2]},{motors[3]}"
            ser.write(( out + '\n').encode('utf-8'))

if __name__ == "__main__":
    try:
        ser = serial.Serial('/dev/cu.usbserial-142130', baudrate=9600, timeout=1)
        print("Serial port opened.")

        # Write to serial in the main thread
        write_to_serial(ser)
    
    except serial.SerialException as e:
        print(f"Serial error: {e}")


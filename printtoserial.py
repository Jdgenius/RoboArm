import serial
import threading

def read_from_serial(ser):
    """Continuously read from the serial port and print received data."""
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received: '{data}' ")
        except Exception as e:
            print(f"Error reading from serial: {e}")
            break

def write_to_serial(ser):
    """Continuously write user input to the serial port."""
    while True:
        try:
            user_input = input("Enter message to send: ")
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            ser.write((user_input + '\n').encode('utf-8'))
        except Exception as e:
            print(f"Error writing to serial: {e}")
            break

if __name__ == "__main__":
    try:
        ser = serial.Serial('/dev/cu.usbserial-141130', baudrate=9600, timeout=1)
        print("Serial port opened.")

        # Start reading in a separate thread
        read_thread = threading.Thread(target=read_from_serial, args=(ser,), daemon=True)
        read_thread.start()

        # Write to serial in the main thread
        write_to_serial(ser)
    
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

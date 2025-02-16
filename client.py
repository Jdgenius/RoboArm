import asyncio

async def tcp_client():
    host = '127.0.0.1'
    port = 5005
    reader, writer = await asyncio.open_connection(host, port)
    print("[CONNECTED] Receiving Kinect depth data...")
    
    buffer = ""
    
    try:
        while True:
            data = await reader.read(4096)
            if not data:
                print("[WARNING] No data received, skipping...")
                continue
            buffer += data.decode('utf-8')
            # Process full messages (using |END as a delimiter)
            while "|END" in buffer:
                full_message, buffer = buffer.split("|END", 1)
                process_depth_data(full_message.strip(), writer)
    except asyncio.CancelledError:
        print("\n[DISCONNECTED] Closing connection.")
    finally:
        writer.close()
        await writer.wait_closed()

# def process_depth_data(raw_data, writer):
#     try:
#         # Convert the CSV string to a list of integers.
#         # If your C# server sends newlines between rows, you may need to adjust the parsing.
#         depth_values = [list(map(int, value.split(",")[:-1])) for value in raw_data.split("\n") if value] 
#        # Find the closest valid depth value (>800 mm)
#         # valid_depths = [d for d in depth_values if d > 800]
#         # closest_depth = min(valid_depths, default=0)

#         for value in depth_values:
#             print(" ".join(f"{v: <4}" for v in value))        
            
#         # # Determine movement command based on depth
#         # if closest_depth == 0:
#         #     command = "STOP"
#         # elif closest_depth < 1000:
#         #     command = "MOVE_LEFT"
#         # elif closest_depth > 2000:
#         #     command = "MOVE_RIGHT"
#         # else:
#         #     command = "STOP"
        
#         # print(f"[SENT] {command}")
#         # writer.write(command.encode('utf-8'))
#     except Exception as e:
#         print(f"[ERROR] Failed to parse depth values: {e}")

def process_depth_data(raw_data, writer):
    try:
        # Convert the CSV string to a 2D list of integers
        depth_values = [list(map(int, value.split(",")[:-1])) for value in raw_data.split("\n") if value]

        # object_detected = False
        valid_depths = []

        for row in depth_values:
            for depth in row:
                if depth >= 800:  # Object detection threshold
                    # object_detected = True
                    valid_depths.append(depth)

        # if object_detected:
        #     print("[INFO] Object detected at depth ≈ 400 mm")

        if len(valid_depths) > 10:
            avg_depth = sum(valid_depths) / len(valid_depths)
            print(f"[INFO] Average Depth in range (800-2000 mm): {avg_depth:.2f} mm")
        else:
            print("[INFO] No valid depth values found.")

        # # # Print depth values as before
        # for value in depth_values:
        #     print(" ".join(f"{v: <4}" for v in value))        

    except Exception as e:
        print(f"[ERROR] Failed to parse depth values: {e}")

if __name__ == '__main__':
    asyncio.run(tcp_client())

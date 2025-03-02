# Quicker Picker Upper
The Quicker Picker Upper is a robotic arm equipped with depth sensing that detects objects in a garbage collection area. It automatically identifies, sorts, and disposes of waste into the appropriate bins. The robotic arm has three degrees of rotation (X, Y, Z) that allow it to swivel and maneuver efficiently.

## Inspiration
Our inspiration for this project stemmed from the growing need for efficient waste sorting and automation. We wanted to create a fun, interactive, and intelligent solution that not only helps sort trash but also gamifies the process to encourage better waste disposal habits.

## How We Built It
We combined hardware, software, and mathematics to bring this project to life:

- Custom 3D-printed parts for the robotic arm
- Kinect Xbox 360 depth camera to detect object presence
- Python & C# integration for data parsing and Kinect control via a TCP server
- Raspberry Pi controlling servos for arm movement
- Linear algebra calculations to determine positioning and optimize arm rotation
## Challenges We Ran Into
One of the biggest challenges we faced was power management for the servo motors. Running four servo motors directly from the Raspberry Pi led to power instability, which required an external power supply for stable operation.

Integrating the Kinect sensor in C# was another significant challenge. As a team, we had little prior experience with C#, and dealing with library compatibility issues made the setup process difficult. Debugging and troubleshooting took a considerable amount of time, but ultimately, we were able to get the depth sensor working.

## Accomplishments That We're Proud Of
We are especially proud of the:

- 3D modeling and assembly of our robotic arm, which required careful design and iteration
- Successful integration of Kinect’s depth sensing with real-time data processing
- Implementation of a real-time TCP communication system between the Kinect and the robotic arm
- Overcoming technical challenges and learning a new programming language, C#
## What We Learned
- Dimensional analysis and linear algebra were essential for accurate positioning and movement calculations of the robotic arm
- Efficient real-time communication through TCP socket programming allowed us to stream data between the Kinect, Raspberry Pi, and Python
- Hardware-software integration was a key aspect of the project, ensuring that the servo motors, depth sensing, and data processing worked together seamlessly
### What's Next for The Quicker Picker Upper?
We plan to integrate machine learning to enhance the robot's ability to recognize waste items and categorize them into recycling, compost, or garbage.

In addition, we want to incorporate a gamification system, where users earn points for correctly disposing of waste and lose points for misplacing items. This would make the process more engaging while promoting better waste management habits.


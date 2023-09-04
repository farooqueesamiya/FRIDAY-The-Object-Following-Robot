# FRIDAY-The-Object-Following-Robot
This GitHub repository documents the design and development of an object-following robot using Raspberry Pi, showcasing the fusion of robotics and computer vision.

# Smart Color-Based Object Tracking Robot

## Table of Contents
1. Introduction
2. Acknowledgement
3. Objectives
4. Applications
5. Hardware Requirements
6. Software Requirements
7. Installation and Setup
8. Project Implementation
9. Conclusion

## 1. Introduction

The Smart Color-Based Object Tracking Robot is an innovative project designed as part of a computer science engineering final year endeavor. Leveraging the power of the Raspberry Pi, computer vision, and robotics, this project aims to create an autonomous robot capable of detecting and tracking objects based on their color in real-time. This documentation outlines the project's objectives, applications, hardware and software requirements, installation procedures, and the steps involved in creating the robot.

## 2. Acknowledgement

I would like to extend my heartfelt gratitude to the Integral University Robotics Lab (https://www.robotics.iul.ac.in/) for their invaluable support throughout the development of this project. Their generous provision of funds, tools, and a conducive environment for research and innovation has been instrumental in bringing this project to fruition. I am also deeply appreciative of their guidance and expertise, which have played a pivotal role in the successful design and implementation of the object-following robot using Raspberry Pi. This project would not have been possible without their unwavering support and mentorship.

## 3. Objectives

- Develop a color-based object tracking system using the Raspberry Pi.
- Implement computer vision techniques to detect and follow objects of specific colors.
- Create a user-friendly interface for color selection and adjustments.
- Enable the robot to autonomously make decisions based on the position and size of detected objects.
- Integrate remote operation and monitoring capabilities.

## 4. Applications

The Smart Color-Based Object Tracking Robot has a wide range of real-world applications, including:
- **Industrial Automation:** Sorting and material handling tasks in manufacturing and logistics.
- **Surveillance and Security:** Detecting and tracking suspicious objects in surveillance systems.
- **Autonomous Robotics:** Navigation and interaction with the environment in search and rescue missions or exploration.
- **Augmented Reality:** Interaction with virtual objects in augmented reality applications.
- **Human-Robot Interaction:** Communication through colored markers or objects.
- **Education and Research:** Teaching computer vision and robotics principles.
- **Entertainment and Gaming:** Incorporating the robot into interactive games and experiences.
- **Home Automation:** Assisting in household tasks and enhancing smart homes.
- **Accessibility:** Aiding individuals with specific needs.
- **Humanoid Robotics:** Enhancing interaction capabilities in humanoid robots.

## 5. Hardware Requirements

- Raspberry Pi 3 board 
- Raspberry Pi Camera (B) Rev 2.0 (Rpi Cam)
- Two DC motors
- Two wheels
- Motor Driver Shield (L298N)
- 7805 IC (Voltage Regulator)
- Li-Po battery
- DC switch

## 6. Software Requirements

- Raspberry Pi OS
- OpenCV (Computer Vision Library)
- RealVNC viewer (for remote operation)

## 7. Installation and Setup

### Raspberry Pi OS Installation:
1. Download Raspberry Pi OS from the official website raspberrypi.com.
2. Flash the OS onto an SD card using a tool like Etcher (https://etcher.balena.io/).
3. Insert the SD card into the Raspberry Pi and boot it up.
4. Follow the on-screen setup instructions to configure the OS.
5. Assign a static IP address during the setup process. If you have difficulty in assigning the static IP address, click here and follow the instructions: https://www.tomshardware.com/how-to/static-ip-raspberry-pi

### Installing OpenCV:
- Use the following commands to install OpenCV:
  
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install python3-opencv
  

### Installing VNC Viewer (Optional):
- Follow the documentation provided by RealVNC Viewer for installation and configuration: https://www.realvnc.com/en/connect/download/viewer/

## 8. Project Implementation

### Hardware Setup:

1. **Pi Camera Module**:
   - The Pi Camera Module connects directly to the dedicated camera port on the Raspberry Pi board. No additional wiring is needed.

2. **DC Motors and Wheels**:
   - Two DC motors are typically connected to a motor driver shield. The motor driver shield is not directly mentioned in the code, but it's assumed to be connected.
   - **Motor Driver Shield (L298N)**:
     - **Motor A (Left Motor)**:
       - Input 1: GPIO 22
       - Input 2: GPIO 27
     - **Motor B (Right Motor)**:
       - Input 3: GPIO 17
       - Input 4: GPIO 23

3. **7805 Voltage Regulator**:
   - The 7805 IC is used for voltage regulation but is not directly interfaced with the Raspberry Pi's GPIO pins. It's part of the power supply circuitry for the motors and other components.

4. **Li-Po Battery**:
   - The Li-Po battery is used as the power source for the motors and the Raspberry Pi. It connects to the appropriate input terminals on the motor driver shield and to the Raspberry Pi for power.

5. **DC Switch**:
   - The DC switch is used to turn the power supply on/off. It's part of the power circuitry and is not connected to the Raspberry Pi's GPIO pins.

### Software Setup:

- The software setup involves configuring the Raspberry Pi OS, installing OpenCV for computer vision, and optionally setting up OpenVPN for remote operation. 

### Running the Code:

- Once the hardware and software are set up, you can run the provided Python code on the Raspberry Pi.
- The code captures video from the Pi Camera Module and processes it to detect and track objects based on color.
- The robot's movement is controlled based on the position and size of the detected object.
- You can observe the robot's behavior and interaction with objects in real-time.

**Note:** Be sure to follow safety precautions when working with the hardware, especially when handling power components and motor connections.

## 9. Conclusion

The Smart Color-Based Object Tracking Robot is an exciting project that showcases the integration of computer vision, robotics, and remote control using the Raspberry Pi. Its potential applications are diverse, ranging from industrial automation to augmented reality. By following the outlined hardware and software requirements, installation steps, and implementation process, this project opens up a world of possibilities for innovation in the field of computer science engineering.

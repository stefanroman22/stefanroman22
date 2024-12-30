# Bionic Arm Controlled by Flex Sensors and Accelerometer

## Overview
This project presents a robotic arm that mimics the real-time movements of a human hand using three flex sensors and an accelerometer. The sensors are mounted on a wearable glove, translating user hand gestures into movements of the robotic arm. The arm is powered by servo motors controlled via a Raspberry Pi Pico.

## Features
- **Real-Time Motion Mimicry**: Replicates hand movements accurately using flex sensors and accelerometer data.
- **Servo Motor Control**: Provides smooth motion with PWM signals.
- **Modular and Extendable**: Designed for easy modification and enhancements.
- **Energy Efficiency**: Utilizes a power-efficient Raspberry Pi Pico board.
- **Safety Mechanisms**: Prevents overloading of motors with angle clamping.

## Table of Contents
1. [Hardware Requirements](#hardware-requirements)
2. [Software Setup](#software-setup)
3. [Usage Instructions](#usage-instructions)
4. [Project Architecture](#project-architecture)
5. [Design Details](#design-details)
6. [Future Improvements](#future-improvements)
7. [Acknowledgments](#acknowledgments)

## Hardware Requirements

### Components
- **Robotic Arm**: Pre-assembled arm structure with 5 servo motors:
  - Shoulder: YF6125-MG
  - Elbow: YF6125-MG
  - Wrist Rotation: MG996-R
  - Hand Grip: MG996-R
- **Sensors**:
  - 3 Flex Sensors
  - 1 MPU6050 Accelerometer
- **Controller**: Raspberry Pi Pico
- **Power Supply**: 5V DC
- **Intermediate Servo Controller Board**: For wiring organization and isolation.

### Robot Components
![image](https://github.com/user-attachments/assets/a28a1941-3ff4-42d1-b0aa-fa572033c736)


## Software Setup

### Prerequisites:
- Python 3.x installed on your PC.
- Libraries: `pio_servo`, `machine`, `MPU6050`, `math`, `time`.

### Installation:
Clone the repository:

```bash
git clone https://github.com/your-repo/bionic-arm.git
cd bionic-arm

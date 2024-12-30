# **Project Overview: Bionic Arm Controlled by Flex Sensors and Accelerometer**

## **Introduction**
The Bionic Arm project demonstrates a robotic arm that mimics real-time hand movements using three flex sensors and one accelerometer. By leveraging the power of a Raspberry Pi Pico, this system translates human hand gestures into precise robotic motions, enabling an intuitive interface for controlling the arm. 

The project combines mechanical engineering, electronics, and software development to provide a robust, scalable, and user-friendly solution.

---

## **System Highlights**
- **Real-Time Motion Tracking**: Mimics the user's hand movements with high precision.
- **Flexible Control System**: Combines flex sensors and accelerometer for comprehensive motion coverage.
- **Servo Motor Precision**: PWM-controlled servos ensure smooth and reliable movement.
- **Energy Efficient**: Powered by the highly efficient Raspberry Pi Pico.
- **Scalable Design**: Modular architecture for easy integration of new features.

---

## **Core Components**

### **Hardware**
1. **Robotic Arm**: Pre-assembled mechanical structure with 5 servo motors:
   - Shoulder: YF6125-MG (rotational movement and abduction/adduction)
   - Elbow: YF6125-MG (flexion/extension)
   - Wrist Rotation: MG996-R
   - Hand Grip: MG996-R

2. **Sensors**:
   - **Flex Sensors**: Detect bending angles for shoulder, elbow, and hand grip.
   - **MPU6050 Accelerometer**: Measures pitch and roll for hand elevation and rotation.

3. **Controller**:
   - Raspberry Pi Pico (chosen for its efficiency, support for Python, and available servo driver).

4. **Servo Driver Board**: Organizes connections and isolates power to prevent damage.

5. **Power Supply**:
   - 5V DC power supply to support servos and electronics.

### **Software**
- Developed in Python, leveraging libraries such as `pio_servo`, `machine`, and `math`.
- Modular codebase for flexibility and maintainability.
- Real-time data processing from sensors and control of servo motors via PWM signals.

---

## **System Mechanism**

### **Sensor Integration**
- **Flex Sensors**:
  - Connected to the Raspberry Pi Pico’s ADC pins via voltage divider circuits.
  - Map bending resistance to angle values.
- **MPU6050 Accelerometer**:
  - Provides digital output via I2C interface.
  - Measures pitch and roll for hand movement detection.

### **Angle Calculation**
Raw sensor data is converted into meaningful angles using specific formulas:
- Flex Sensor (e.g., Pin 28): Linear mapping based on resistance changes.
- Accelerometer: Radians converted to degrees for pitch and roll movements.

### **Servo Control**
- PWM signals are generated to control servo motors.
- Angle thresholds and delays (0.1s) ensure efficient and noise-free movements.

---

## **Data Flow**
1. **Sensor Input**: Flex sensors and accelerometer data are read.
2. **Angle Mapping**: Raw values are processed to derive corresponding joint angles.
3. **Servo Commands**: Mapped angles are converted to PWM signals and sent to servos.
4. **Real-Time Response**: The robotic arm mimics user hand gestures seamlessly.

---

## **Challenges and Solutions**
### Challenges:
1. **Servo Noise**: Sudden, unintended movements due to minor sensor fluctuations.
2. **Wireless Communication**: Initial attempts to use Bluetooth/Wi-Fi modules were unsuccessful.
3. **Component Alignment**: Initial misalignment of servo motors caused inaccuracies.

### Solutions:
1. **Noise Filtering**: Introduced thresholds to ignore minor sensor value changes (<8 degrees).
2. **Wired Communication**: Opted for wired connections for reliable data transfer.
3. **Mechanical Adjustments**: Realigned and recalibrated servo positions.

---

## **Future Improvements**
1. **Wireless Connectivity**: Implement Bluetooth or Wi-Fi for sensor-to-arm communication.
2. **Smoother Movements**: Optimize servo control for gradual transitions.
3. **Enhanced Design**: Use waterproof and durable components for wider applications.
4. **Additional Sensors**: Expand capabilities with more flex sensors or advanced motion trackers.

---

## **Conclusion**
The Bionic Arm project successfully integrates hardware and software to create a functional, real-time robotic hand mimicking system. With further refinements, this project has the potential for applications in prosthetics, robotics research, and human-machine interfaces.


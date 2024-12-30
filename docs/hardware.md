# **Hardware Documentation: Bionic Arm**

## **Introduction**
The hardware for the Bionic Arm project consists of a robotic arm controlled by sensors and servo motors, with a focus on modularity and ease of assembly. The system integrates flex sensors, an accelerometer, and servo motors through a servo driver board, powered by a Raspberry Pi Pico.

---

## **Hardware Components**

### **1. Robotic Arm**
A pre-assembled mechanical structure forms the foundation of the bionic arm. It comprises:

- **Metal Frame**: Provides durability and structural support.
- **5 Servo Motors**:
  - **Shoulder**: 2 motors (rotational movement and abduction/adduction).
  - **Elbow**: 1 motor (flexion/extension).
  - **Wrist**: 1 motor (rotation).
  - **Hand**: 1 motor (grip).

### **2. Sensors**
- **Flex Sensors**:
  - Detect bending in the user’s hand and translate it into motor movement.
  - Connected to the Raspberry Pi Pico via ADC pins.
  - Used for:
    - Shoulder movement (up/down).
    - Elbow movement (up/down).
    - Hand grip control.

- **MPU6050 Accelerometer**:
  - Mounted on the glove to detect pitch and roll.
  - Provides real-time motion data for hand elevation and rotation.
  - Connected via I2C interface.

### **3. Raspberry Pi Pico**
The microcontroller serves as the central processing unit:
- **Key Features**:
  - Supports Python, enabling easy programming.
  - Low power consumption (1.8–5.5V).
  - Programmable I/O (PIO) for concurrent tasks.
- **Functionality**:
  - Reads sensor values.
  - Processes data to calculate servo angles.
  - Sends PWM signals to the servo driver board.

### **4. Servo Driver Board**
An intermediate component for managing servo connections:
- **Features**:
  - Dedicated power input for servo motors (5V DC).
  - Organized pin layout for PWM, GND, and power connections.
- **Benefits**:
  - Prevents Raspberry Pi Pico from overloading.
  - Simplifies wiring and troubleshooting.

### **5. Power Supply**
- **Voltage**: 5V DC.
- **Role**: Supplies power to the servo motors and driver board.

---

## **Hardware Connections**

### **1. Servo Motor Pin Assignments**
Each servo motor is connected to specific GPIO pins on the Raspberry Pi Pico via the servo driver board:
- **Shoulder Up/Down**: GPIO17
- **Elbow Up/Down**: GPIO18
- **Hand Up/Down**: GPIO19
- **Hand Rotation**: GPIO20
- **Hand Grip**: GPIO21

### **2. Sensor Connections**
- **Flex Sensors**:
  - Connected to ADC pins:
    - **Shoulder Up/Down**: ADC2 (GPIO28)
    - **Elbow Up/Down**: ADC1 (GPIO27)
    - **Hand Grip**: ADC0 (GPIO26)
  - Voltage divider circuits used to convert resistance to measurable voltage.

- **MPU6050 Accelerometer**:
  - Connected via I2C:
    - **SDA**: GPIO0
    - **SCL**: GPIO1

### **3. Power Connections**
- Servo motors receive power directly from the servo driver board.
- Raspberry Pi Pico is powered via USB or a separate 5V source.

---

## **System Mechanism**
### **1. Sensor Integration**
- Flex sensors measure bending and generate variable resistance.
- The accelerometer provides digital pitch and roll values for rotational movements.

### **2. Signal Processing**
- Sensor data is read by the Raspberry Pi Pico and converted into angles for servo control.
- Each angle is mapped to a specific PWM value for precise motor movement.

### **3. Servo Motor Control**
- The servo driver board distributes PWM signals from the Raspberry Pi Pico to the servo motors.
- Delays between servo movements ensure smooth operation.

---

## **Hardware Challenges and Solutions**
### Challenges:
1. **Servo Motor Alignment**:
   - Initial misalignment caused inaccuracies.
2. **Sensor Noise**:
   - Flex sensors detected minor, unintended movements.
3. **Wiring Complexity**:
   - Multiple connections created clutter and potential for errors.

### Solutions:
1. **Recalibration**:
   - Reassembled the robotic arm to correct servo alignment.
2. **Noise Filtering**:
   - Software thresholding ignored angle changes below 8 degrees.
3. **Servo Driver Board**:
   - Streamlined wiring and reduced connection errors.

---

## **Future Enhancements**
1. **Wireless Communication**:
   - Integrate Bluetooth or Wi-Fi modules to eliminate cables.
2. **Improved Sensors**:
   - Use more precise sensors or expand sensor capacity with multiplexing.
3. **Durability Improvements**:
   - Use waterproof and dust-resistant components for wider applications.

---

## **Conclusion**
The hardware design of the Bionic Arm ensures efficient and reliable functionality. By integrating flex sensors, an accelerometer, and servo motors through a robust framework, this system replicates human hand movements with precision. The modular design also allows for future enhancements and scalability.

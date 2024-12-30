# **Software Documentation: Bionic Arm**

## **Introduction**
The software for the Bionic Arm project is designed to interface with flex sensors and an accelerometer, process the sensor data, and control servo motors to replicate hand movements in real time. This modular Python-based system emphasizes efficiency, scalability, and maintainability.

---

## **Core Functionalities**
The software provides the following core functionalities:
1. **Sensor Input**: Reads analog values from flex sensors and digital values from the accelerometer.
2. **Data Processing**: Converts raw sensor data into angles for servo control.
3. **Servo Control**: Generates PWM signals to move servo motors based on calculated angles.
4. **Noise Filtering**: Minimizes unintended movements by ignoring minor sensor fluctuations.

---

## **Software Architecture**
### **High-Level Workflow**
1. **Initialization**:
   - Set up I2C interface for the accelerometer.
   - Configure ADC pins for flex sensors.
   - Initialize servo motor parameters and global variables.

2. **Main Loop**:
   - Continuously read sensor values.
   - Process the sensor data to calculate angles.
   - Control servo motors based on the calculated angles.

3. **Delays**:
   - Introduce delays between servo movements to ensure smooth operation.

### **Key Components**
1. **Sensor Input**:
   - **Flex Sensors**: Connected via ADC pins (GP26, GP27, GP28) to measure bending resistance.
   - **MPU6050 Accelerometer**: Connected via I2C to read pitch and roll values.

2. **Angle Calculation**:
   - Custom functions (`calculate_angle_PIN28`, `calculate_angle_PIN_REST`, `calculate_angle_Hand_Accelerometer`) process raw sensor values into angles.

3. **Servo Motor Control**:
   - Functions (`move_specific_servo`, `move_HandGrip_servo`) generate PWM signals for precise servo movements.

---

## **Detailed Function Descriptions**

### **move_specific_servo**
- **Description**: Moves a specific servo motor to a given angle, considering the angle difference threshold.
- **Parameters**:
  - `motor`: PIN of the servo motor to move.
  - `angle`: Target angle in degrees.
  - `previous_angle`: Previous angle of the servo motor.
- **Outcome**: The specified servo motor moves to the given angle.

### **move_HandGrip_servo**
- **Description**: Moves the hand grip servo motor to a given angle.
- **Parameters**:
  - `motor`: PIN of the hand grip servo motor.
  - `angle`: Target angle in degrees.
  - `previous_angle`: Previous angle of the servo motor.
- **Outcome**: The hand grip servo motor moves to the desired angle.

### **angle_to_ms**
- **Description**: Converts an angle in degrees to the corresponding PWM value in milliseconds.
- **Parameters**:
  - `angle`: Input angle in degrees.
- **Output**: PWM value in milliseconds.

### **calculate_angle_PIN28**
- **Description**: Calculates the angle based on the sensor value from the flex sensor connected to ADC PIN 28.
- **Parameters**:
  - `sensor_value`: Raw sensor value.
  - `min_sensor_value`: Minimum expected sensor value.
  - `max_sensor_value`: Maximum expected sensor value.
  - `max_angle`: Maximum angle (in degrees).
- **Output**: Calculated angle in degrees.

### **calculate_angle_PIN_REST**
- **Description**: Calculates the angle based on the sensor value from flex sensors connected to ADC pins other than PIN 28.
- **Parameters**:
  - `sensor_value`: Raw sensor value.
- **Output**: Calculated angle in degrees.

### **calculate_angle_Hand_Accelerometer**
- **Description**: Calculates the angle based on the accelerometer's sensor value.
- **Parameters**:
  - `sensor_value`: Accelerometer sensor value.
- **Output**: Calculated angle in degrees.

### **read_pitch_roll**
- **Description**: Reads pitch and roll values from the MPU6050 accelerometer.
- **Parameters**:
  - `mpu`: MPU6050 object.
- **Output**: Tuple containing pitch and roll angles (in degrees).

---

## **Error Handling and Optimizations**
1. **Noise Filtering**:
   - Introduced a threshold to ignore minor angle changes (<8 degrees) to prevent unintended movements.
2. **Angle Clamping**:
   - Ensures calculated angles remain within the servo’s operational range (0-180 degrees).
3. **Sequential Movements**:
   - Added delays between servo movements to ensure smooth operation and prevent signal conflicts.

---

## **Execution Flow**
1. Initialize I2C and ADC configurations.
2. Enter the main loop:
   - Read sensor values.
   - Calculate angles for shoulder, elbow, hand, and hand grip movements.
   - Move corresponding servo motors.
3. Introduce delays to ensure proper signal processing.

---

## **Future Enhancements**
1. **Wireless Communication**:
   - Integrate Bluetooth or Wi-Fi modules for sensor-to-arm connectivity.
2. **Advanced Motion Control**:
   - Implement smoother transitions between servo positions.
3. **Error Correction**:
   - Introduce self-calibration for sensor and servo alignment.

---

This modular software framework enables precise control of the bionic arm and provides a foundation for future enhancements.

# **Troubleshooting: Bionic Arm**

## **Introduction**
This guide provides solutions to common issues encountered during the setup and operation of the Bionic Arm. By systematically addressing these challenges, you can ensure smoother operation and quicker debugging.

---

## **Common Issues and Solutions**

### **1. Servo Motors Not Moving**
**Symptoms**:
- Servo motors remain stationary even after running the script.
- No sound or movement is detected.

**Potential Causes**:
1. Servo driver board is not receiving power.
2. Incorrect GPIO pin assignments in the code.
3. PWM signal not generated correctly.

**Solutions**:
- Verify that the servo driver board is connected to a stable 5V power source.
- Double-check GPIO pin assignments in the script:
  - Ensure they match the pin connections for each motor.
- Confirm the PWM signal output using debugging tools (e.g., an oscilloscope).

### **2. Servo Motors Moving Erratically**
**Symptoms**:
- Sudden, unintended movements.
- Motors jitter or move when sensors are stationary.

**Potential Causes**:
1. Noise or minor fluctuations in sensor readings.
2. Power supply instability.

**Solutions**:
- Implement a noise filtering threshold in the software (e.g., ignore angle changes <8 degrees).
- Ensure the power supply is stable and meets the required specifications (5V, adequate current).
- Inspect connections for loose wires or bad solder joints.

### **3. Incorrect Servo Movements**
**Symptoms**:
- Motors move to unexpected positions.
- Movements are reversed or inconsistent with hand gestures.

**Potential Causes**:
1. Incorrect angle calculations in the software.
2. Flex sensor values not mapped correctly.

**Solutions**:
- Verify angle mapping formulas in the code:
  - For flex sensors, ensure the range of raw sensor values is accurately converted to angles.
  - For the accelerometer, confirm correct pitch and roll calculations.
- Check if any angle reversal logic (e.g., `180 - angle`) is misapplied.

### **4. Flex Sensors Not Responding**
**Symptoms**:
- No change in motor movement despite flexing the sensors.
- Sensor values remain constant or undefined.

**Potential Causes**:
1. Improper connection to ADC pins.
2. Faulty flex sensor.

**Solutions**:
- Verify the voltage divider circuit connections:
  - Ensure the flex sensor and resistors are properly soldered or connected.
- Test the flex sensor with a multimeter to check resistance changes when bent.
- Replace faulty flex sensors with spare ones.

### **5. Accelerometer Values Seem Incorrect**
**Symptoms**:
- Unexpected or nonsensical pitch and roll values.
- Motors do not respond to hand rotation or elevation.

**Potential Causes**:
1. Improper I2C connection.
2. Calibration issues.

**Solutions**:
- Ensure proper I2C connections:
  - **SDA** to GPIO0, **SCL** to GPIO1.
- Recalibrate the accelerometer by resetting its orientation.
- Use diagnostic scripts to read raw accelerometer values and verify their accuracy.

### **6. Overheating Servo Motors**
**Symptoms**:
- Servo motors become hot during operation.
- Motors fail to hold positions or behave erratically.

**Potential Causes**:
1. Servo motors are trying to move

# Import required libraries
from pio_servo import PIO_SERVO  # For controlling servo motors
import machine                   # For microcontroller-specific operations
import time                      # For delays and timing
import MPU6050                   # For accelerometer operations
import math                      # For mathematical calculations

# Global variables to track the previous angles for each servo motor
previous_angle_ShoulderRotation = 0
previous_angle_ShoulderUpDown = 0
previous_angle_ElbowUpDown = 0
previous_angle_HandUpDown = 0
previous_angle_HandRotation = 0
previous_angle_HandGrip = 0

# History lists and maximum size for debugging or optimization purposes (currently unused)
history_ShoulderUpDown = []
history_HandUpDown = []
history_HandRotation = []
history_size = 10

# Sensor value thresholds and range definitions
min_sensor_value = 2320
threshold_value = 2340  # Define a threshold value close to the minimum
max_sensor_value = 5000
max_angle = 180

# Servo pin assignments (corresponding to the hardware setup)
servo_pin_ShoulderUpDown = 17
servo_pin_ElbowUpDown = 18
servo_pin_HandUpDown = 19
servo_pin_HandRotation = 20
servo_pin_HandGrip = 21

# Function to move a specific servo motor
# This ensures smooth transitions and avoids unnecessary movements
def move_specific_servo(motor, angle, previous_angle):
    global previous_angle_ShoulderUpDown, previous_angle_ElbowUpDown
    global previous_angle_HandUpDown, previous_angle_HandRotation, previous_angle_HandGrip

    # Only move if the angle change is significant (to filter noise)
    if abs(angle - previous_angle) > 8 or angle == 0:
        servoChoice = PIO_SERVO(2, motor)

        # Special case for motor at pin 18
        if motor == 18:
            angle = 180 - angle

        servoChoice.set_ms(angle_to_ms(angle))

        # Update the corresponding previous angle variable
        if motor == 17:
            previous_angle_ShoulderUpDown = angle
        elif motor == 19:
            previous_angle_HandUpDown = angle
        elif motor == 20:
            previous_angle_HandRotation = angle
        elif motor == 21:
            previous_angle_HandGrip = angle

# Function to handle special cases for the hand grip servo
def move_HandGrip_servo(motor, angle, previous_angle):
    global previous_angle_HandGrip

    # Significant angle change check (specific to hand grip)
    if abs(angle - previous_angle):
        servoChoice = PIO_SERVO(0, motor)

        if motor == 18:
            angle = 180 - angle

        servoChoice.set_ms(angle_to_ms(angle))

        if motor == 21:
            previous_angle_HandGrip = angle

# Convert a given angle to the corresponding PWM value
def angle_to_ms(angle):
    angle = max(0, min(angle, 180))  # Clamp the angle to [0, 180]
    ms = 0.5 + (angle / 180.0) * 2.0
    return ms

# Calculate angle for flex sensor connected to ADC28 (requires specific adjustments)
def calculate_angle_PIN28(sensor_value, min_sensor_value, max_sensor_value, max_angle):
    zero_deg_min = 2384
    zero_deg_max = 2520

    # Return 0 if within 0-degree range
    if zero_deg_min <= sensor_value <= zero_deg_max:
        return 0

    # Normalize the sensor value to [0, max_angle]
    angle = (sensor_value - zero_deg_max) * (max_angle / (max_sensor_value - zero_deg_max))
    return max(0, min(angle, 180))

# Calculate angle for other flex sensors
def calculate_angle_PIN_REST(sensor_value):
    sensor_value_at_0_deg = 280
    sensor_value_at_180_deg = 4000

    angle = (sensor_value - sensor_value_at_0_deg) * (180.0 / (sensor_value_at_180_deg - sensor_value_at_0_deg))
    return max(0, min(angle, 180))

# Calculate angle adjustments for the accelerometer
def calculate_angle_Hand_Accelerometer(sensor_value):
    if 0 < sensor_value < 2:
        sensor_value = 0
    return sensor_value + 90

# Read pitch and roll angles from the accelerometer
def read_pitch_roll(mpu):
    accel = mpu.read_accel_data()
    x, y, z = accel

    # Calculate pitch and roll angles (in degrees)
    pitch = math.atan2(y, math.sqrt(x**2 + z**2)) * (180.0 / math.pi)
    roll = math.atan2(x, math.sqrt(y**2 + z**2)) * (180.0 / math.pi)

    return pitch, roll

# Initialize I2C interface and accelerometer
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
accelerometerHand = MPU6050.MPU6050(i2c)
accelerometerHand.wake()

# ADC setup for reading flex sensor values
readShoulderUpDown = machine.ADC(28)
readElbowUpDown = machine.ADC(27)
readHandGrip = machine.ADC(26)

# Main function to coordinate the sensor readings and servo movements
def main():
    global previous_angle_ShoulderRotation, previous_angle_ShoulderUpDown
    global previous_angle_ElbowUpDown, previous_angle_HandUpDown
    global previous_angle_HandRotation, previous_angle_HandGrip

    while True:
        # Read sensor values
        sensorValueShoulderUpDown = readShoulderUpDown.read_u16()
        sensorValueElbowUpDown = readElbowUpDown.read_u16()
        sensorValueHandGrip = readHandGrip.read_u16()
        sensorValueHandUpDown, sensorValueHandRotation = read_pitch_roll(accelerometerHand)

        # Compute angles for each servo
        servo_angle_ShoulderUpDown = calculate_angle_PIN28(sensorValueShoulderUpDown, min_sensor_value, max_sensor_value, max_angle)
        servo_angle_ElbowUpDown = calculate_angle_PIN_REST(sensorValueElbowUpDown)
        servo_angle_ElbowUpDown = max(90, servo_angle_ElbowUpDown)  # Clamp to 90 degrees minimum
        servo_angle_HandUpDown = calculate_angle_Hand_Accelerometer(sensorValueHandUpDown)
        servo_angle_HandRotation = 180 - calculate_angle_Hand_Accelerometer(sensorValueHandRotation)
        servo_angle_HandGrip = calculate_angle_PIN_REST(sensorValueHandGrip)

        # Print calculated angles for debugging
        print("Angle ShoulderUpDown:", servo_angle_ShoulderUpDown)
        print("Angle ElbowUpDown:", servo_angle_ElbowUpDown)
        print("Angle HandUpDown:", servo_angle_HandUpDown)
        print("Angle HandRotation:", servo_angle_HandRotation)
        print("Angle HandGrip:", servo_angle_HandGrip)

        # Move the servos with delays to ensure proper response
        move_specific_servo(servo_pin_ShoulderUpDown, servo_angle_ShoulderUpDown, previous_angle_ShoulderUpDown)
        time.sleep(0.1)
        move_specific_servo(servo_pin_ElbowUpDown, servo_angle_ElbowUpDown, previous_angle_ElbowUpDown)
        time.sleep(0.1)
        move_specific_servo(servo_pin_HandUpDown, servo_angle_HandUpDown, previous_angle_HandUpDown)
        time.sleep(0.1)
        move_specific_servo(servo_pin_HandRotation, servo_angle_HandRotation, previous_angle_HandRotation)
        time.sleep(0.1)
        move_HandGrip_servo(servo_pin_HandGrip, servo_angle_HandGrip, previous_angle_HandGrip)
        time.sleep(0.2)

# Entry point of the program
if __name__ == "__main__":
    main()

from machine import Pin, ADC
from time import sleep

soil_sensor = ADC(Pin(26))
# Configure the GPIO pin connected to MOSFET
PUMP_PIN = 15  # Change this to match your wiring
pump = Pin(PUMP_PIN, Pin.OUT)


# Replace these with your actual measured values (Adjust taking example from your own soil, may differ)
DRY_VALUE = 48000    # Value when completely dry
WET_VALUE = 20900        # Replace with your value when in water

# Make sure pump starts in OFF state
pump.value(0)

#Green LED
green_led = Pin(4, Pin.OUT)
green_led.value(0)
#Yellow LED
yellow_led = Pin(5, Pin.OUT)
yellow_led.value(0)
# Threshold value for soil moisture (vary as per your plant)
moisture_threshold = 80


def read_soil_moisture():
    sensor_value = soil_sensor.read_u16()
    
    # Convert to percentage (0% = dry, 100% = wet)
    moisture_percentage = (DRY_VALUE - sensor_value) / (DRY_VALUE - WET_VALUE) * 100
    
    # Constrain to 0-100%
    moisture_percentage = max(0, min(100, moisture_percentage))
    
    return sensor_value, moisture_percentage

def turn_pump_on():
    pump.value(1)
    print("Pump turned ON")

def turn_pump_off():
    pump.value(0)
    print("Pump turned OFF")

def run_pump_for_seconds(seconds):
    turn_pump_on()
    sleep(seconds) 
    turn_pump_off()

while True:
    value, percentage = read_soil_moisture()
    print("Sensor Value: {}, Moisture Percentage: {:.2f}%".format(value, percentage))
    
    if percentage > moisture_threshold:
        green_led.value(1)
        yellow_led.value(0)
    else:
        green_led.value(0)
        yellow_led.value(1)
        run_pump_for_seconds(2)

    sleep(2)
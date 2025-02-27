# Auto-Watering-System-Pico-Solar-Powered
Auto Watering System - Pico + Solar Powered

![Setup Image v2](https://github.com/user-attachments/assets/ea062719-2a01-42e9-81f4-9196138a8feb)

*in v2 of the setup diagram, i am powering pico now from the solar cell header instead of usb out due to pico not coming back to power when the battery is depleted. Since we are powering using vsys pin, remember, the soil sensor will not get power from vbus anymore, hence shifted it to the solar cell 5v pin.

Parts Used:
1. Raspberry Pi Pico
2. Gravity: MOSFET Power Controller ( https://www.dfrobot.com/product-1567.html )
3. Solar Power Manager 5V ( https://www.dfrobot.com/product-1712.html )
4. Solar Cell 6v 1amp ( https://saurally.com/product/5w-6v-saurally-solar-panel-poly/ )
5. 3v Pump (https://robu.in/product/dc-3-6-v-mini-micro-submersible-water-pump/ )
6. Capacitive Soil Moisture Sensor  ( https://thinkrobotics.com/products/capacitive-soil-moisture-sensor-corrosion-resistant )

![2](https://github.com/user-attachments/assets/8be8cff7-8e44-4c24-8e41-9c3a2fb5ded6)
![1](https://github.com/user-attachments/assets/35223ca8-c9d4-4962-bd20-6be63ec9cfe4)

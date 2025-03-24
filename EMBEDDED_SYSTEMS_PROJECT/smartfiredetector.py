import network
import urequests
import utime
import machine
from ahtx0 import AHT10  # AHT10 temperature & humidity sensor library
import config  # Import WiFi & Telegram credentials

# 🔥 GPIO Pin Assignments
FLAME_SENSOR = machine.Pin(16, machine.Pin.IN)  # Flame sensor (D0)
RED_LED = machine.Pin(14, machine.Pin.OUT)  # Red LED (Fire Alert)
GREEN_LED = machine.Pin(15, machine.Pin.OUT)  # Green LED (Normal Mode)
BUZZER = machine.Pin(13, machine.Pin.OUT)  # Buzzer

# 🌡 I2C for AHT10 Sensor
i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))
aht10 = AHT10(i2c)

# 🔄 System State Variables
fire_detected = False
alert_count = 0

# 📡 Function to connect WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(config.SSID, config.PASSWORD)  # Load credentials from config.py
    
    print("⏳ Connecting to WiFi...")
    timeout = 10  # 10 seconds timeout
    while not wlan.isconnected() and timeout > 0:
        utime.sleep(1)
        timeout -= 1
    
    if wlan.isconnected():
        print("✅ Connected to WiFi:", wlan.ifconfig())
        return True
    else:
        print("❌ WiFi Connection Failed")
        return False

# 📢 Function to send Telegram Alert
def send_telegram_message(message):
    encoded_message = message.replace(" ", "%20").replace("\n", "%0A").replace("🔥", "%F0%9F%94%A5").replace("✅", "%E2%9C%85")

    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={config.CHAT_ID}&text={encoded_message}"
    
    try:
        print("📤 Sending Telegram Alert...")
        response = urequests.get(url, timeout=10)  # 10-second timeout
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("❌ Error sending Telegram alert:", e)

# 🔥 Main Fire Detection System
def fire_detection_system():
    global fire_detected, alert_count
    
    if not connect_wifi():
        return  # Exit if WiFi fails

    while True:
        if FLAME_SENSOR.value() == 0:  # Fire Detected
            while FLAME_SENSOR.value() == 0:
                # 🔴 Keep Red LED and Buzzer cycling until fire is cleared
                # Keep looping while fire is detected
                # Turn off Buzzer
                RED_LED.on()  # Turn on RED LED
                utime.sleep(0.5)  # Keep LED on for 0.5 seconds
                
                RED_LED.off()  # Turn off RED LED
                
                BUZZER.on()  # Turn on Buzzer
                utime.sleep(1)  # Keep buzzer ON for 1 seconds
                
                BUZZER.off()
                    
            if not fire_detected:
                fire_detected = True
                alert_count = 0  # Reset alert counter
                
                # Read temperature & humidity
                temperature = aht10.temperature
                humidity = aht10.relative_humidity
                
                print("🔥 Fire detected! Activating alerts...")
                send_telegram_message(f"🔥 Fire detected! 🚨\n🌡 Temp: {temperature:.1f}°C\n💧 Humidity: {humidity:.1f}%")
            
            # 📩 Send alert every 1 minute, up to 3 times
            if alert_count < 3:
                utime.sleep(5)  # Wait 1 minute
                temperature = aht10.temperature
                humidity = aht10.relative_humidity
                send_telegram_message(f"🚨 Fire Alert (Repeat) 🚨\n🌡 Temp: {temperature:.1f}°C\n💧 Humidity: {humidity:.1f}%")
                alert_count += 1
        
        else:  # ✅ Normal Mode
            if fire_detected:  # Fire was previously detected and now cleared
                print("✅ Fire cleared. Resetting system...")
                send_telegram_message("✅ Fire has been cleared. System back to normal.")
                fire_detected = False  # Reset fire detection state

            # 🟢 Green LED stays ON but blinks every 1 second
            GREEN_LED.on()
            utime.sleep(0.5)
            GREEN_LED.off()
            utime.sleep(0.5)

# 🚀 Run the Fire Detection System
fire_detection_system()

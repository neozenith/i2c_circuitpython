import board
import adafruit_bme680
import time

if __name__ == "__main__":
    i2c = board.I2C()
    sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    temp_offset = -5
    sensor.sea_level_pressure = 1013.25

    while True:

        print("\nTemp: %0.1f C" % (sensor.temperature + temp_offset))
        print("\nHumidity: %0.1f %%" % (sensor.relative_humidity))
        print("\nPressure: %0.3f hPa" % (sensor.pressure))
        print("\nAltitude: %0.2f m" % (sensor.altitude))
        time.sleep(1)

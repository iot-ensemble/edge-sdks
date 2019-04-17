from iothub_client import IoTHubClient, IoTHubTransportProvider, IoTHubMessage
import time
import board
import digitalio
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

CONNECTION_STRING = "HostName=flw-rd-trevor.azure-devices.net;DeviceId=TrevorRasPiTestDevice;SharedAccessKey=vXopp724VsYWo/n0INXBKRdCkTtotZKuKENFYJgLyB4="
PROTOCOL = IoTHubTransportProvider.MQTT


def send_confirmation_callback(message, result, user_context):
    print("Confirmation received for message with result = %s" % (result))


if __name__ == '__main__':
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    message = IoTHubMessage("test message")
    client.send_event_async(message, send_confirmation_callback, None)
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Message transmitted to IoT Hub")

    while True:
        time.sleep(1)

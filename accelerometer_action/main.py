
from bleak import BleakScanner
import time
from accelerometer_action import handle_ble_data

def main():


    print("Scanning...")

    scanner = BleakScanner()

    try:
        while True:
            devices = scanner.discover(timeout=1.0)
            for device in devices:
                handle_ble_data(device, device.metadata)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping scanner...")

if __name__ == "__main__":
    main()

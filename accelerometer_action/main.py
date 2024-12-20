import asyncio
from bleak import BleakScanner
from accelerometer import process_data

async def scan_devices():
    print("Scanning...")
    scanner = BleakScanner(detection_callback=process_data)

    try:
        await scanner.start()
        while True:
            await asyncio.sleep(1.0)
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        await scanner.stop()

def main():
    asyncio.run(scan_devices())

if __name__ == "__main__":
    main()

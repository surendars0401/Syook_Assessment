import asyncio
from ui import App
from accelerometer import process_data

async def scan_devices(ui_callback):
    from bleak import BleakScanner
    print("Scanning...")
    scanner = BleakScanner(detection_callback=lambda d, a: process_data(d, a, ui_callback))
    try:
        await scanner.start()
        while True:
            await asyncio.sleep(1.0)
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        await scanner.stop()

def main():

    app = App()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.ensure_future(scan_devices(app.update_device_list))
    app.run()

if __name__ == "__main__":
    main()

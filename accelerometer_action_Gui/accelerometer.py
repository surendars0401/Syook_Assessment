THRESHOLD = 0.5

def parse_data(Baw):
    try:
        if not raw.startswith("0201060303E1FF"):
            return None
        x = int(raw[16:20], 16) / 1000
        y = int(raw[20:24], 16) / 1000
        z = int(raw[24:28], 16) / 1000
        return x, y, z
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

def process_data(device, advertisement, ui_callback):
    if (
        device.address
        and advertisement
    ):
        manufacturer_data = advertisement.manufacturer_data
        if manufacturer_data:
            raw = ''.join(
                format(b, '02x') for b in manufacturer_data.get(
                    next(iter(manufacturer_data), 0), b''
                )
            )
            data = parse_data(raw)
            if data:
                x, y, z = data
                magnitude = (x**2 + y**2 + z**2)**0.5
                status = (
                    "Moving"
                    if magnitude > THRESHOLD
                    else "Stationary"
                )

                ui_callback(device.address, x, y, z, status)

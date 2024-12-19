acc_readings = []
MOVEMENT_THRESHOLD = 0.5

def accelerometer_data(raw_data):

    try:
        if not raw_data.startswith("0201060303E1FF"):
            return None

        x = int(raw_data[16:20], 16) / 1000
        y = int(raw_data[20:24], 16) / 1000
        z = int(raw_data[24:28], 16) / 1000

        return (x, y, z)
    except:
        return None

def is_moving():

    if not acc_readings:
        return "Error"

    total_magnitude = 0
    for x, y, z in acc_readings:
        magnitude = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        total_magnitude += magnitude

    average_magnitude = total_magnitude / len(acc_readings)

    if average_magnitude > MOVEMENT_THRESHOLD:
        return "Moving"
    return "Stationary"

def add_reading(x, y, z):

    acc_readings.append([x, y, z])
    if len(acc_readings) > 50:
        acc_readings.pop(0)

def handle_ble_data(device, advertising_data):

    if device.address:
        raw_data = ''.join([format(b, '02x') for b in
                            advertising_data.manufacturer_data.get(
                                next(iter(advertising_data.manufacturer_data)), b'')])

        acc_data = accelerometer_data(raw_data)
        if acc_data:
            x, y, z = acc_data
            add_reading(x, y, z)
            movement_status = is_moving()

            print(f"\nDevice: {device.address}")
            print(f"\nX-axis: {x:.2f}")
            print(f"\nY-axis: {y:.2f}")
            print(f"\nZ-axis: {z:.2f}")
            print(f"\nStatus: {movement_status}")

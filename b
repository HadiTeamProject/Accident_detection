import serial
import re

def parse_gprmc(sentence):
    # Regular expression pattern to match GPRMC sentence
    pattern = r'^\$GPRMC,(\d{6}\.\d+),([AV]),(\d+\.\d+),(N|S),(\d+\.\d+),(E|W),\d+\.\d+,\d+\.\d+,(\d{6}),,,([AV]\*\w{2})$'
    match = re.match(pattern, sentence)
    if match:
        time_stamp = match.group(1)  # Time stamp
        status = match.group(2)  # Status (A: Valid, V: Void)
        latitude = float(match.group(3))  # Latitude
        latitude_dir = match.group(4)  # Latitude direction (N: North, S: South)
        longitude = float(match.group(5))  # Longitude
        longitude_dir = match.group(6)  # Longitude direction (E: East, W: West)
        date_stamp = match.group(7)  # Date stamp
        return {
            "time_stamp": time_stamp,
            "status": status,
            "latitude": latitude,
            "latitude_dir": latitude_dir,
            "longitude": longitude,
            "longitude_dir": longitude_dir,
            "date_stamp": date_stamp
        }
    else:
        return None

# Open serial port
ser = serial.Serial('/dev/ttyAMA0', 9600)  # Change '/dev/ttyAMA0' to your serial port

try:
    while True:
        # Read data from serial port
        data = ser.readline().decode('latin1').strip()  # Use latin1 encoding instead of utf-8
        
        # Check if the data starts with '$GPRMC' (a GPRMC sentence)
        if data.startswith("$GPRMC"):
            # Parse the GPRMC sentence
            parsed_data = parse_gprmc(data)
            if parsed_data:
                # Print latitude and longitude
                latitude=int (parsed_data["latitude"])
                longitude=int(parsed_data["longitude"])
                la_decimal_degrees = latitude // 100 + (degrees % 100) / 60
                lo_decimal_degrees = longitude // 100 + (degrees % 100) / 60
                print("Latitude:", la_decimal_degrees)
                print("Longitude:", lo_decimal_degrees)
except KeyboardInterrupt:
    # Close serial port on keyboard interrupt (Ctrl+C)
    ser.close()


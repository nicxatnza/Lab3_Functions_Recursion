# [EXERCISE 1] EQUIPMENT DIAGNOSTIC SYSTEM
LAST_NAME = "ATIENZA"
SEED_NUM = 2
FAVORITE_ARTIST = "IV OF SPADES"

def process_logger(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def generate_readings():
    return [len(LAST_NAME) * 10, SEED_NUM * 15, len(FAVORITE_ARTIST) * 5, "invalid_reading", 100]

@process_logger
def validate_reading(reading):
    try:
        return float(reading)
    except ValueError:
        return None

@process_logger
def calculate_average(valid_readings):
    return sum(valid_readings) / len(valid_readings) if valid_readings else 0

@process_logger
def classify_condition(average):
    if average > 50: return "CRITICAL"
    elif average > 20: return "WARNING"
    return "NORMAL"

readings = generate_readings()
valid_readings = [v for r in readings if (v := validate_reading(r)) is not None]
avg = calculate_average(valid_readings)
status = classify_condition(avg)

print(f"Generated Equipment Data: {readings}")
print(f"Validation Results: {valid_readings}")
print(f"Diagnostic Results: Average = {avg:.1f}, Status = {status}")
print(f"Final Output: {status}")
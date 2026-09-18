# Monitor for [Exercise 3] INTELLIGENT EQUIPMENT MONITORING PIPELINE
def monitor_logger(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

trace_path = []

def analyze_abnormal(value, depth=0):
    trace_path.append(f"{value:.2f}")
    if value <= 10:
        return depth
    return analyze_abnormal(value * 0.5, depth + 1)
# [EXERCISE 3] INTELLIGENT EQUIPMENT MONITORING PIPELINE
from monitor_utils import monitor_logger, analyze_abnormal, trace_path

LAST_NAME = "ATIENZA"
SEED_NUM = 2
FAVORITE_ARTIST = "IV OF SPADES"

def telemetry_generator():
    base_data = [len(LAST_NAME)*5, "drop", SEED_NUM*20, len(FAVORITE_ARTIST)*8, -10, 150]
    for data in base_data:
        yield data

filter_valid = lambda x: x > 0

@monitor_logger
def process_stream(stream):
    stats = {'processed': 0, 'valid_count': 0, 'invalid_count': 0, 'abnormal_count': 0}
    generated_data, valid_data, invalid_data = [], [], []
    
    for item in stream:
        generated_data.append(item)
        stats['processed'] += 1
        try:
            val = float(item)
            if not filter_valid(val):
                raise ValueError("Negative value")
            valid_data.append(val)
            stats['valid_count'] += 1
            
            if val > 100:
                stats['abnormal_count'] += 1
                analyze_abnormal(val)
                
        except ValueError:
            invalid_data.append(item)
            stats['invalid_count'] += 1
            
    return generated_data, valid_data, invalid_data, stats

generated, valid, invalid, summary_stats = process_stream(telemetry_generator())

print(f"Student-Specific Inputs: {LAST_NAME}, {SEED_NUM}, {FAVORITE_ARTIST}")
print(f"Generated Telemetry Data: {generated}")
print(f"Valid/Invalid Results: Valid: {valid} | Invalid: {invalid}")
print(f"Processed Results: Total: {summary_stats['processed']}, Valid: {summary_stats['valid_count']}, Invalid: {summary_stats['invalid_count']}, Abnormal: {summary_stats['abnormal_count']}")
print(f"Recursive Analysis: {' -> '.join(trace_path)}")
print(f"Final Diagnostic Summary: {summary_stats}")
print(f"Final Output: {'NEEDS MAINTENANCE' if summary_stats['abnormal_count'] > 0 else 'OPERATIONAL'}")
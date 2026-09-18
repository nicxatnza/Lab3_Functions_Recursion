# [EXERCISE 2] RECURSIVE FAULT TRACE
LAST_NAME = "ATIENZA"
SEED_NUM = 2
FAVORITE_ARTIST = "IV OF SPADES"

fault_code = len(LAST_NAME) + SEED_NUM + len(FAVORITE_ARTIST)
call_count = 0
trace_path = []

def trace_fault(code):
    global call_count
    call_count += 1
    trace_path.append(str(code))
    
    if code <= 1:
        return "Fault isolated."
    
    if code % 2 == 0:
        return trace_fault(code // 2)
    else:
        return trace_fault(code - 3)

result = trace_fault(fault_code)

print(f"Generated Fault Data: {fault_code}")
print(f"Recursive Trace: {' -> '.join(trace_path)}")
print(f"Number of Recursive Calls: {call_count}")
print(f"Final Output: {result}")
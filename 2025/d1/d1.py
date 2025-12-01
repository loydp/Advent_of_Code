example = "example.txt"
source = "data.txt"

def get_data(file_path):
    raw = None
    with open(file_path, "r") as file:
        raw = file.readlines()
    raw = [line.strip() for line in raw]
    data = [int(line[1:]) if line[0] == "R" else -1 * int(line[1:]) for line in raw]
    return data

def process(data, curr=50, dial_size=100):
    zero_count = 0
    for spin_val in data:
        curr = (curr + spin_val) % dial_size
        if curr == 0:
            zero_count += 1
    return zero_count

def get_zero_hits(start, spin_val, dial_size):
    distance = abs(spin_val)
    
    if distance == 0:
        return 0

    if spin_val > 0:
        clicks_to_first_zero = (dial_size - start) % dial_size
        if clicks_to_first_zero == 0:
            clicks_to_first_zero = dial_size
            
    else:
        clicks_to_first_zero = start % dial_size
        if clicks_to_first_zero == 0: # If starting at 0, first hit is after 100 clicks
            clicks_to_first_zero = dial_size

    if distance < clicks_to_first_zero:
        return 0

    # Hit 0 at least once
    zero_hits = 1
    remaining_clicks = distance - clicks_to_first_zero
    
    # Count subsequent hits every 100 clicks
    zero_hits += remaining_clicks // dial_size
    
    return zero_hits

def process2(data, curr=50, dial_size=100):
    zero_count = 0
    for spin_val in data:
        zero_hits = get_zero_hits(curr, spin_val, dial_size)
        zero_count += zero_hits
        curr = (curr + spin_val) % dial_size
        
    return zero_count

#data = get_data(example)
data = get_data(source)

result = process(data)
result2 = process2(data)

print(result)
print(result2)
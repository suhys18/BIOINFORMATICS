def frequency_table(text, k):
    freqmap = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i+k]
        if pattern not in freqmap:
            freqmap[pattern] = 1
        else:
            freqmap[pattern] += 1

    return freqmap

def find_clumps(text, k, l, t):
    patterns = []
    n = len(text)

    for i in range(n - l + 1):
        window = text[i:i+l]
        freqmap = frequency_table(window, k)
        
        for s in freqmap:
            if freqmap[s] >= t:
                patterns.append(s)
    
    # Remove duplicates by converting the list to a set, then back to a list
    patterns = list(set(patterns))
    
    return patterns

# Function to read the input file and parse the values
def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        text = lines[0].strip()
        k, l, t = map(int, lines[1].strip().split())
    return text, k, l, t

# Example usage
filename = 'input.txt'  # Replace with your file name
text, k, l, t = read_input_file(filename)
result = find_clumps(text, k, l, t)

# Print the result without commas and brackets
print(" ".join(result))


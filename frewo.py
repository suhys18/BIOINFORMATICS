def rfaex(filename):
    k = None
    text = ""

    with open(filename, 'r') as file:
        lines = file.readlines()


    for line in lines:
        stripped_line = line.strip()
        if stripped_line.isdigit():
            k = int(stripped_line)
        else:
            text += stripped_line + " "

    text = text.strip()
    return k, text


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


def most_frequent_kmers(text, k):
    freqmap = frequency_table(text, k)
    max_freq = max(freqmap.values())
    most_frequent = [pattern for pattern, freq in freqmap.items() if freq == max_freq]
    return " ".join(most_frequent)


filename = 'z.txt'
k, text = rfaex(filename)
most_frequent = most_frequent_kmers(text, k)


result = most_frequent

print(result)




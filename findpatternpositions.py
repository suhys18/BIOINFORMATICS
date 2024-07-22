def find_pattern_positions(pattern, genome):
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)
    
    return positions

def main():
    file_path = 'z.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
        pattern = lines[0].strip()
        genome = ''.join(line.strip() for line in lines[1:])

    positions = find_pattern_positions(pattern, genome)

    # Print positions as a space-separated string
    print(' '.join(map(str, positions)))

if __name__ == "__main__":
    main()


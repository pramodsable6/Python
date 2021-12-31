# Problem: There are 10 rods, idx = 0 ... 9 and each rod can have multiple rings with color R, G, B
# Find number of rods with all three color rings

def count_rods(rings):
    B = []
    G = []
    R = []
    for idx, value in enumerate(rings):
        if rings[idx] == 'B':
            B.append(rings[idx+1])
        elif rings[idx] == 'G':
            G.append(rings[idx+1])
        elif rings[idx] == 'R':
            R.append(rings[idx+1])
    return len(set(B).intersection(set(G)).intersection(set(R)))


print(count_rods('B0R0G0R9R0B0G0B1G1R1B2G2R2'))

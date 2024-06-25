def huffman_coding(counts):
    ln = sum([val for _, val in counts.items()])

    # tree node representation -> (val, left, right)
    sort_forest = lambda f : sorted(f, key=lambda x: x[0][1])
    forest = sort_forest([((key, val/ln), None, None) for key, val in counts.items()])
    print(forest[:10])

    print(len(forest))

    iter_count = 0
    while len(forest) > 1:
        # 1. get two lowest prob trees and merge them
        tree1, tree2 = forest[:2]

        new_prob = tree1[0][1] + tree2[0][1]
        new_tree = ((None, new_prob), tree1, tree2)

        forest = [new_tree] + forest[2:]
        forest = sort_forest(forest)
        print(forest[:10])
        print(len(forest))
        iter_count += 1
        if iter_count == 200: break

filename = "enwik6"

with open(filename, "rb") as f: data = f.read()

print("Data length:", len(data))
print("Data sample:", data[:100])
print("Binary sample:", " ".join(f"{b:08b}" for b in data[:100]))

# compression limit
symbols = set(data)
print("Symbols:", len(symbols))

from collections import defaultdict
from math import log2

counts = defaultdict(int)
for c in data: counts[c] += 1

counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

for i, (key, value) in enumerate(counts.items()):
    if i == 20: break
    print(f"{i+1:2}: s={key:3} chr={repr(chr(key)):3} count={value:7} p(s)={value/len(data):7.5f} -log2p(s)={-log2(value/len(data)):4.2f} bits")


entropy = -sum([log2(c/len(data))*(c/len(data)) for _, c in counts.items()])
print(f"entropy = {entropy:.3f} bits")
print(f"worst case entropy for {len(symbols)} symbols: {log2(len(symbols)):.3f} bits")
print(f"optimal compression ratio: 8 / {entropy:.3f} = {8 / entropy:.2f}x")

huffman_coding(counts)

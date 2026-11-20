"""Read alternate upper-triangle rows backward so every comparison has a witness."""
import csv
import json
from pathlib import Path


def chain(n):
    for i in range(n-1):
        js = range(i+1, n)
        for j in (reversed(js) if i % 2 else js):
            yield i, j


def restore(d, anchor, bit):
    out = [0]*(len(d)+1)
    out[anchor] = bit
    for i in range(anchor, len(d)):
        out[i+1] = out[i] ^ d[i]
    for i in reversed(range(anchor)):
        out[i] = out[i+1] ^ d[i]
    return out


def main():
    root = Path(__file__).parent
    with (root/'ramsey_balanced_order_20.csv').open(newline='') as f:
        header, *rows = csv.reader(f)
    labels = list(map(int, header[1:]))
    assert labels == [int(row[0]) for row in rows]
    pairs = list(chain(len(labels)))
    assert len(set(pairs)) == len(pairs) == 190
    assert all(len(set(p)&set(q)) == 1 for p,q in zip(pairs,pairs[1:]))
    bits = [int(rows[i][j+1]) for i,j in pairs]
    d = [a^b for a,b in zip(bits,bits[1:])]
    for i,b in enumerate(bits):
        assert restore(d,i,b) == bits
        assert restore(d,i,1-b) == [1-x for x in bits]
    (root/'ramsey_common_witness_chain_20.json').write_text(json.dumps(dict(address_order=labels, pair_order='upper triangle; reverse odd rows (zero-based)', different_from_next=''.join(map(str,d))),indent=2)+'\n')
    print('Verified 189 shared-address comparisons and 190 anchors.')
    print('First row boundary:',[(labels[i],labels[j],bit) for (i,j),bit in zip(pairs[18:20],bits[18:20])])

if __name__=='__main__':main()

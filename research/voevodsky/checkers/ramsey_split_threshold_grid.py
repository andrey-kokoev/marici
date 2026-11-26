"""Exact threshold grids for the 8-vertex path split and its cycle closure."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import csv

D = Path(__file__).resolve().parents[1] / 'results'
vertices = range(8)
bit = {e: 1 << j for j, e in enumerate(combinations(vertices, 2))}
full = sum(bit.values())
sub = [[sum(bit[e] for e in combinations(c, 2)) for c in combinations(vertices, n)] for n in range(9)]
base = sum(bit[e] for e in [(0,1),(0,2),(0,3),(4,5),(5,6),(6,7)])
cross = [bit[a,b] for a in (1,2,3) for b in (4,5,6,7)]

def threshold(forbidden):
    return 1 + next(n for n in range(8,0,-1) if any(not (s & forbidden) for s in sub[n]))

def main():
    transitions = Counter()
    for x in range(4096):
        p = base | sum(b for j,b in enumerate(cross) if x >> j & 1)
        c = p | bit[4,7]
        transitions[threshold(full^p),threshold(p),threshold(full^c),threshold(c)] += 1
    with (D/'ramsey_split_threshold_transitions.csv').open('w', newline='') as f:
        w=csv.writer(f);w.writerow(['path_l','path_k','cycle_l','cycle_k','gluings']);w.writerows((*t,n) for t,n in sorted(transitions.items()))
    with (D/'ramsey_split_threshold_2_13.csv').open('w', newline='') as f:
        w=csv.writer(f);w.writerow(['core','l','k','first_legal','total_legal'])
        for name,i in [('path',0),('cycle',2)]:
            h=Counter()
            for t,n in transitions.items():h[t[i:i+2]]+=n
            print(name,sorted(h.items()));assert sum(h.values())==4096
            for l in range(2,14):
                for k in range(2,14):w.writerow([name,l,k,h[l,k],sum(n for (a,b),n in h.items() if a<=l and b<=k)])
    print('former (3,4):',[(t,n) for t,n in transitions.items() if t[:2]==(3,4)])
if __name__=='__main__':main()

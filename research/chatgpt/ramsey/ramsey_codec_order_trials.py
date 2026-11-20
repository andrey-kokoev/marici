"""Hold the graph fixed. Preselect ten shared permutations; do not select the best."""
import csv
from pathlib import Path
from random import Random
from statistics import median
from ramsey_paired_interval_codec import run as paired
from ramsey_rolling_lookahead_codec import run as rolling

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:
        h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));base=[list(map(int,row[1:])) for row in data]; results=[]
    for seed in range(10):
        order=sorted(range(20),key=labels.__getitem__);Random(seed).shuffle(order)
        m=[[base[i][j] for j in order] for i in order];results.append((paired(m),rolling(m,False),rolling(m,True)))
    print('paired, prune, weighted:',results); print('ranges/medians',[(min(v),max(v),median(v)) for v in zip(*results)])

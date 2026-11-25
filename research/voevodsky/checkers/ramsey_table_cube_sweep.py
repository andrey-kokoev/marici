"""Extend ledger 4339 without replacing its width 6-13 receipt."""
import csv,sys
from math import comb
from collections import Counter
from pathlib import Path
from ramsey_table_cube_differences import analyze
end=int(sys.argv[1]) if len(sys.argv)>1 else 25
p=Path(__file__).resolve().parents[1]/f'results/ramsey_table_cube_sweep_5_{end}.csv'
with p.open('w',newline='') as f:
    w=csv.writer(f);w.writerow('width upper center cubes squares edges points uncovered display_rows compressed_records'.split())
    for k in range(5,end+1):
        r=analyze(k);h=Counter(len(c['new']) for c in r['pieces']);u=len(r['leftover']);z=len(r['center'])
        assert all(c['box'] for c in r['pieces']) and set(h)<={1,2,4,8} and sum(n*c for n,c in h.items())+u==r['upper']
        if k>=8:
            assert [h[v] for v in (8,4,2,1)]==[comb(3,j)*comb(k-8,j) for j in range(4)] and u==3*k-16
        row=[k,r['upper'],z,h[8],h[4],h[2],h[1],u,r['display_rows'],2*(r['cubes']+u)+z];w.writerow(row);print(*row)

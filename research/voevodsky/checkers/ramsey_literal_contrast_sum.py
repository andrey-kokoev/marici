"""Test the two-row column action on the six marked edge contrasts. No arbitrary rotors."""
from itertools import permutations,combinations,combinations_with_replacement
from pathlib import Path
import json

def run():
    rows=('BRNN','BNRN');U=set(range(4));s=[{j for j,c in enumerate(row) if c!='N'} for row in rows];Y,=[p for p in permutations(range(4)) if all({p[j] for j in v}==U-v for v in s)];r=(0,2,1,3);G=[tuple(range(4)),r,Y,tuple(r[j] for j in Y)];assert len(set(G))==4
    def score(edge,p):
        i,j=edge;return int(p[i]==i)+int(p[j]==j)-int(p[i]==j)-int(p[j]==i) # twice normalized signed projection
    edges=list(combinations(range(4),2));vals={''.join(str(i+1) for i in e):[score(e,p) for p in G] for e in edges}
    seen={};counts=0
    for seq in combinations_with_replacement(range(4),4):
        # Sum of literal permutation operators on four labeled columns.
        op=tuple(sum(G[h][j]==i for h in seq) for i in range(4) for j in range(4));signs=[]
        for e in edges:
            v=[score(e,G[h]) for h in seq];neg=min(v)<0;pos=max(v)>0
            if min(score(e,p) for p in G)>=0:assert not neg and pos==(sum(v)>0)
            else:assert set(v)<={-2,2} and neg==(sum(v)<8) and pos==(sum(v)>-8)
            signs.append((neg,pos))
        assert seen.setdefault(op,signs)==signs;counts+=1
    p=Path(__file__).resolve().parents[1]/'results/ramsey_literal_contrast_sum.json';out=dict(rows=rows,actions=G,twice_self_projection=vals,assignments_up_to_order=counts,distinct_sums=len(seen),scope='Conditional simultaneous BR/NN side exchange and literal row change; same-axis column contrast projection; four present routes.');p.write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=='__main__':run()

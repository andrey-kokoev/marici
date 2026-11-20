"""Cell-address lift of the three by seven nonzero-profile table. Search a two-orbit completion, no catalogue. Red=1."""
from itertools import combinations
from pathlib import Path
import json
X=[[p>>i&1 for p in range(1,8)] for i in range(3)]
# Order columns by their actual bit profiles, then cells by row: integer addresses 0..20.
cells=[(i,j) for j in sorted(range(7),key=lambda j:sum(X[i][j]<<i for i in range(3))) for i in range(3)]

def indep(rows):
    sets=[0]
    for j,r in enumerate(rows):sets += [s|1<<j for s in sets if not s&r]
    return sets

def main():
    n=(len(cells)+1)//2;assert 2*n==len(cells)+1;full=(1<<n)-1
    rot=lambda s,i:((s<<i)|(s>>(n-i)))&full
    blocks=[]
    for m in range(1<<(n//2)):
        d=sum((1<<i)|(1<<(n-i)) for i in range(1,n//2+1) if m>>(i-1)&1);a=[rot(d,i) for i in range(n)];ss=indep(a)
        if max(map(int.bit_count,ss))<=6 and all(r in ss for r in a):blocks.append((d,a,ss))
    for d,a,ss in blocks:
        for e,b,tt in blocks:
            # Score only the 21 old addresses: the right block lacks its final slot.
            right=full^(1<<(n-1))
            # right independent-set capacities on every allowed subset
            cap=[0]*(1<<n)
            for t in tt:cap[t]=t.bit_count()
            for m in range(1,1<<n):
                if cap[m]==0:cap[m]=max(cap[m^(1<<i)] for i in range(n) if m>>i&1)
            for cross in tt:
                rev=sum(1<<((-i)%n) for i in range(n) if cross>>i&1)
                if rev not in ss:continue
                cr=[rot(cross,i) for i in range(n)];blocked={0:0};ok=True
                for s in ss:
                    if s:blocked[s]=blocked[s&(s-1)]|cr[(s&-s).bit_length()-1]
                    if s.bit_count()+cap[right&~blocked[s]]>6:ok=False;break
                if not ok:continue
                rows=[a[i]|(cr[i]<<n) for i in range(n)]+[rot(rev,i)|(b[i]<<n) for i in range(n)];core=[r&((1<<len(cells))-1) for r in rows[:-1]];cs=indep(core);sixes=[s for s in cs if s.bit_count()==6];borders=[s for s in cs if all(s&t for t in sixes)]
                if not borders:continue
                selected=borders[0];matrix=[r|(((selected>>i)&1)<<len(cells)) for i,r in enumerate(core)]+[selected];final=indep(matrix);assert max(map(int.bit_count,final))==6 and all(r in final for r in matrix)
                tensor=[[[int(matrix[cells.index((i,j))]>>w&1) for w in range(len(matrix))] for j in range(7)] for i in range(3)]
                assert max(map(int.bit_count,cs))==6 and all(r in cs for r in core);print('found',d,e,cross,'borders',len(borders));obj=dict(table=X,cells=cells,core_rows=core,legal_border_masks=borders,selected=selected,tensor=tensor);Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2));return
    print('no two-orbit witness')
if __name__=='__main__':main()

"""Target-only displacement seeds. Same deterministic first-fit growth for both formulas.
No imports of witness data, known thresholds, or previous graphs. Standard library.
"""
from itertools import product, combinations

def blue(rows, stop=None):
    sets=[0]
    for i,r in enumerate(rows):
        new=[s|1<<i for s in sets if not s&r]
        if stop and any(s.bit_count()>=stop for s in new):return None
        sets+=new
    return sets

def check(rows,k):
    for i,r in enumerate(rows):
        assert not r>>i&1 and all(((r>>j)&1)==((t>>i)&1) for j,t in enumerate(rows))
        if any(r>>j&1 and r&t for j,t in enumerate(rows)):return False
    return blue(rows,k) is not None

def seed(k,form):
    if form not in ('double','array','full_array'):raise ValueError(form)
    h,w=(2,3+k) if form=='double' else (3,k)
    group=list(product(range(h),range(w)));V=group[1:] if form=='array' else group
    def rep(x,y):return min((x,y),((-x)%h,(-y)%w))
    reps=sorted({rep(*z) for z in group[1:]}); mats=[[0]*len(V) for _ in reps];tested=0
    for i,j in combinations(range(len(V)),2):
        x,y=V[i];u,v=V[j];m=mats[reps.index(rep((x-u)%h,(y-v)%w))];m[i]|=1<<j;m[j]|=1<<i
    # Increasing number of positive displacement classes, then lexicographic.
    for t in range(len(reps)+1):
        for choice in combinations(range(len(reps)),t):
            rows=[sum(mats[z][i] for z in choice) for i in range(len(V))];tested+=1
            if max(map(int.bit_count,rows))>=k:continue # triangle-free neighborhoods are blue
            if check(rows,k):return rows,[reps[z] for z in choice],tested
    return None,[],tested

def grow(rows,k):
    while True:
        sets=blue(rows);targets=[s for s in sets if s.bit_count()==k-1]
        p=next((p for p in sorted(sets) if all(p&s for s in targets)),None)
        if p is None:return
        n=len(rows);rows=[r|(((p>>i)&1)<<n) for i,r in enumerate(rows)]+[p];assert check(rows,k);yield n+1

if __name__=='__main__':
    for k,form in product((7,8),('double','array')):
        rows,offsets,tested=seed(k,form)
        print(k,form,'assignments visited',tested,'size',len(rows) if rows else None,'offsets',offsets,'growth',list(grow(rows,k)) if rows else None,flush=True)

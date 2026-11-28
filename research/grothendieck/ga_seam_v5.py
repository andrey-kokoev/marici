from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'voevodsky/checkers'))
from ramsey_repair_next_seam import graph,grow,check,D,json,combinations
mask=lambda xs:sum(1<<x for x in xs)
d=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(i-1 for i in s) for s in d['supports']),d['gap'])
fl=[mask(i for i in (g-1,g) if 0<=i<9) for g in range(10)]
def audit(s,c):
    a=graph(9,s,c)
    if not check(a,16383,3,7):return
    red=[mask((i,j)) for i,j in combinations(range(14),2) if a[i]>>j&1];blue={k:[b for t in combinations(range(14),k) for b in [mask(t)] if all(e&b!=e for e in red)] for k in (5,6)};C=set();sole=set()
    R={(b>>9,mask(i for i,f in enumerate(fl) if not b&f)) for b in blue[6]};nd=sum(not any((q,h)!=(p,g) and q&p==q and g&h==g for q,h in R) for p,g in R)
    for i,f in enumerate(fl):
        if 0<i<9 and any(not b&(f|a[i-1]|a[i]) for b in blue[5]):continue
        M={}
        for p in range(32):
            N=f|(p<<9)
            if any(e!=f and e&N==e for e in red):continue
            w=frozenset(b for b in blue[6] if not N&b);M[p]=w
            if w:C.add(w)
        for b in blue[6]:
            pp=[p for p,w in M.items() if b in w]; k=max((p.bit_count() for p in pp),default=-1)
            if any(len(M[p])==1 and p.bit_count()==k for p in pp):sole.add(b)
    pool=sorted(set().union(*C));C=sorted(C,key=len)
    for k in range(len(pool)+1):
        opt=[frozenset(t) for t in combinations(pool,k) if all(not w.isdisjoint(t) for w in C)]
        if opt:return nd,sole,opt
if __name__=='__main__':
    c=192;nd,sole,[O]=audit(S,c);print('nondominated',nd,'sole',sorted(sole),'unique optimum',sorted(O));count=0;failed=0
    for j in range(5):
        for i in range(9):
            T=list(S);T[j]=tuple(sorted(set(T[j])^{i}));res=audit(T,c)
            if res is None:continue
            count+=1;opts=res[2];local=(1<<i)|(1<<(9+j))
            if not any(all(b&local for b in t-O) for t in opts):
                failed+=1
                if failed==1:print('first failure: port,site,red before,minimum,number of optima',j+1,i+1,i in S[j],len(opts[0]),len(opts))
    print('legal neighbors',count,'local failures',failed)

"""Read the first actual movement between tetrahedral fan apexes on the alternating Hall path. Compare all boundary-compatible matchings and all four native bindings; do not look at cube colors to select a movement."""
from ramsey_seed_affine_witness import P,T,r,m,mate,p
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;X=list(combinations(range(1,5),2));rows=('BRNN','BNRN')
def apex(d):
    i,j=P[d];u=set(X[i])&set(X[j]);return next(iter(u)) if u else None

def paths(M):
    other={(r[i],r[j]) for i,j in M};return [[0,16,next(i for i,j in other if j==16)],[0,17,next(i for i,j in M if j==17)]]

def run():
    hist=Counter();cert=[]
    def enum(i,used,flags):
        if i==15:
            z=paths(flags);a,b=[apex(t[-1]) for t in z];hist[a,b]+=1;return
        for t,parts in enumerate(T,15):
            if t in used or P[i] not in parts or (i==0 and t!=16) or (i==7 and t!=29):continue
            enum(i+1,used|{t},flags+[(i,t)])
    enum(0,set(),[]);assert sum(hist.values())==36
    z=paths(m);assert z[0]==p[:3] and z[1]==[r[i] for i in p[:3]]
    for w,t in zip(rows,z):
        start,end=apex(t[0]),apex(t[-1]);a=1+w.index('R');pool=[(P.index(d),apex(P.index(d))) for d in T[t[1]-15] if d!=P[t[0]]];assert a not in {v for _,v in pool};cert.append(dict(row=w,visits=t,apex_step=[start,end],moving_R=a,entry_exits=pool))
    print(cert,hist);return dict(selected=cert,boundary_counts={str(k):v for k,v in hist.items()})
if __name__=='__main__':(D/'ramsey_first_fan_rim_probe.json').write_text(json.dumps(run())+'\n')

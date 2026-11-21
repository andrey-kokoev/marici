"""Extract the R triangle from flags, compare ordinary conjugation vs directed native admission (inverse conjugation); no output graph or pole used."""
from itertools import permutations,combinations
from pathlib import Path
import sys,json
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_carrier_probe_adapter import transition,group,edges
I=tuple(range(4));X=list(combinations(I,2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];J=(0,2,1,3);flags=[((0,16),(7,29)),((0,17),(4,29))];native={'AB','BC','CA','BA','AD','DB'}
def roles(pair):
    (a,t),(b,u)=pair;assert P[a] in T[t-15] and P[b] in T[u-15];e,f=[set(X[v]) for v in P[a]];B,=e&f;Q,=set(I)-(e|f);exit_edges=[set(X[v]) for v in P[b]];v,=next(h for h in exit_edges if B in h)-{B};R,=set(I)-{B,Q,v};return B,Q,R,v

def probe(triple):
    m={x:x for x in 'ABCD'};m.update(zip(triple,triple[1:]+triple[:1]));idx=group.index(tuple('ABCD'.index(m[x]) for x in 'ABCD'));return [int(transition[edges.index(e)].get(idx,0)) for e in ((0,1),(1,0))]

def run():
    F=list(map(roles,flags));assert [t[2] for t in F]==[1,2];out=[]
    for p in permutations('ABCD'):
        rho=dict(zip(p,[p[i] for i in J]));rev=lambda e:rho[e[1]]+rho[e[0]]
        if set(map(rev,['AB','BC','CA']))!={'AD','DB','BA'} or set(map(rev,native))!=native:continue
        tri=[''.join(p[i] for i in t[:3]) for t in F];admit=[]
        for t in tri:
            cand=[w for w in (t,t[0]+t[:0:-1]) if all(w[i]+w[(i+1)%3] in native for i in range(3))];assert len(cand)==1;admit+=cand
        assert admit[1]==''.join(rho[x] for x in (admit[0][0]+admit[0][:0:-1]));out.append(dict(binding=''.join(p),flag_order=tri,flag_readings=list(map(probe,tri)),native_order=admit,native_readings=list(map(probe,admit))))
    return {'roles_B_Q_R_other':F,'records':out}
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_flag_triangle_probe.json').write_text(json.dumps(out)+'\n')

"""Test a positive-duration lift of successive Hall duads to a full native receipt, with and without preserving every defined fan apex. Enumerate all clock assignments rather than declare a duration at exit."""
from itertools import combinations,permutations
from ramsey_first_fan_rim_probe import apex
from ramsey_oriented_overlap_reader import orient,cycle,m,r,X,D,json
from ramsey_handoff_distance_audit import run as native

def run():
    ds=cycle(m)[::2];out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        pair=[]
        for d in (ds,[r[i] for i in ds]):
            a,b=orient(d,X)[-1]['arrow'];i,=[i for i,x in enumerate(d) if apex(x)==a];d=d[i:]+d[:i];pins=[apex(x) for x in d];assert pins==[a,1,b,None,None];fits=[]
            for t in native():
                w=t['word'];k,=[i for i,e in enumerate(w) if e[0]==p[a-1]];w=w[k:]+w[:k];v=[e[0] for e in w];
                for ks in combinations(range(1,6),4):
                    times=(0,)+ks
                    if v[times[2]]!=p[b-1]:continue
                    fits.append(dict(seam=t['seam'],times=times,all_pins=v[times[1]]==p[0]))
            assert len(fits)==3 and len({f['seam'] for f in fits})==1 and all(f['times'][2]==2 for f in fits);pair.append(dict(fans=pins,fits=fits))
        assert sum(any(f['all_pins'] for f in row['fits']) for row in pair)==1;out.append(dict(binding=''.join(p),rows=pair))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_fan_clock_lift.json').write_text(json.dumps(out)+'\n')

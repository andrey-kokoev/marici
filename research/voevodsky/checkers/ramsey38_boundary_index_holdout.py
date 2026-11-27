"""Freeze on graph-only eligibility, prior to constructing any boundary or mesh."""
import sys
from ramsey38_boundary_ball_index import run,p
from ramsey38_disk_filter_trial import key
P=p.prev.out/'ramsey38_boundary_index_holdout_cases.json'

def freeze():
    prior={e['record']:e['root'] for e in p.json.loads(p.P.read_text())['entries']};seen=set();entries=[]
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in prior:seen.add(key(*p.setup(p.graph(line.strip()),prior[i])))
            if i<=260000:continue
            g=p.graph(line.strip())
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,r,m=p.setup(g,u)
                if max(map(int.bit_count,r.values()))>4 or sum(t.bit_count()==2 for t in r.values())<2 or not any(p.setup(p.add(g,a),u)[2] for a in m):continue
                k=key(L,r,m)
                if k in seen:continue
                seen.add(k);entries.append(dict(record=i,root=u));break
            if len(entries)==32:break
    assert len(entries)==32;p.prev.save(P,dict(protocol='First 32 catalogue records after 260000 admitting a new marked seven-column array with supports <=4, >=2 edge rows and an ordered pair of legal promotions. Exclude the eight calibration keys. First eligible novel root per record. No stage or mesh tests.',entries=entries));print(entries[-1])
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze()
    elif sys.argv[1]=='check':run(P,'ramsey38_boundary_index_holdout.json')

"""Exhaust candidate second tips of the buried triangle, not just the first certificate."""
import json
from collections import Counter
from ramsey38_named_gain_trial import P,R,inputs,templates,face,prev,screen,find
from ramsey38_release_census import first_ball
from ramsey38_compare_support_fillings import boundary
from ramsey38_polygon_endpoint_rule import compatible

def audit(e):
    b,a,x,rs,vbit=inputs(e);u=e['u'];labels=sorted(b[u]);S=rs[x];rs={**rs,x:S|vbit};short={j:s for j,s in rs.items() if s.bit_count()<4};ds=set(e['predicted']);base=set(rs.values());tips=[(w,1<<i) for i,w in enumerate(labels) if not (S|vbit)&(1<<i)];out={j:{w:{'shells':0,'screen':0,'oriented':0,'fill':0} for w,_ in tips} for j in ds};cert={}
    for bd,closure in templates():
        if S in closure:continue
        h=[j for j,s in short.items() if s not in closure]
        if len(h)!=1 or h[0] not in ds:continue
        j=h[0];fs=frozenset(map(face,bd))
        for w,m in tips:
            stat=out[j][w];stat['shells']+=1;req=base|{S|m};required=set(map(face,req));local=screen(frozenset(range(7)),required,fs)=='pass' and not find(required|fs,fs);stat['screen']+=int(local)
            named=lambda collection:frozenset(frozenset(labels[i] for i in f) for f in collection)
            oriented=local and compatible(named(fs),named(required));stat['oriented']+=int(oriented)
            o=first_ball(bd,req)
            if o:
                assert oriented and boundary(o)==fs and all(any(f<=t for t in o) for f in required);stat['fill']+=1
                cert.setdefault((j,w),[sorted(labels[i] for i in t) for t in o])
    return out,[{'row':j,'tip':w,'order':order} for (j,w),order in sorted(cert.items())]
if __name__=='__main__':
    es=json.loads(P.read_text())['cases'];truth=json.loads(R.read_text())['results'];entries=[];summary=Counter()
    for e,tr in zip(es,truth):
        out,cert=audit(e);assert {j for j,d in out.items() if any(v['fill'] for v in d.values())}==set(tr['actual'])
        for j,d in sorted(out.items()):
            ok=[w for w,v in d.items() if v['fill']];short=[w for w,v in d.items() if v['screen']];summary[len(ok)]+=1;print(e['record'],e['u'],j,'screen',short,'actual',ok,flush=True)
        entries.append(dict(record=e['record'],root=e['u'],rows=out,certificates=cert))
    prev.save(prev.out/'ramsey38_opposite_tip_orientation_audit.json',dict(counts=dict(sorted(summary.items())),entries=entries));print(summary)

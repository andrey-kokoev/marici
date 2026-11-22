"""Frozen fan-transfer protocol; inherit orientation and mark calibration, not corner-side target colors."""
from ramsey_sector_arrow_bridge import read,sides,point,cal,features,S,D,json,combinations,ws,Counter
from collections import defaultdict

def signature(x,e,m):
    return tuple(sorted((-1,0) if t&e else (sum(bool(k&e and k&t) for k in sides),int(read(t,e,m))) for t in sides if x in t))
rows=[]
for n,(i,j) in enumerate((e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])):
    a,b=sorted((features[i],features[j]),key=len)
    if len(a)!=1 or b not in sides:continue
    x,=a
    for s in range(8):
        m=point[''.join(map(str,cal[str(s)]))];sig=signature(x,b,m);k=sum(v for t,v in sig);d=sum(t>=0 for t,v in sig);rows.append((n,s,x,sorted(b),m,sig,(k,d),2*k>d))
assert len(rows)==576;tables=[defaultdict(list),defaultdict(list)];conf=Counter();by=Counter()
for n,s,x,b,m,sig,v,p in rows:
    y=bool(ws[s]>>n&1);ex=dict(point=x,side=b,mark=m,red=y,query_index=n);conf[int(p),int(y)]+=1;by[s]+=p!=y
    for table,key in zip(tables,(v,sig)):table[key].append(ex)
def audit(t):
    err=0;witness=None;same=None
    for k,rs in t.items():
        pos=[x for x in rs if x['red']];neg=[x for x in rs if not x['red']];err+=min(len(pos),len(neg))
        if pos and neg and witness is None:witness=[k,pos[0],neg[0]]
        if same is None:same=next(([k,a,b] for a in pos for b in neg if a['point']==b['point'] and a['side']==b['side']),None)
    return dict(keys=len(t),min_errors=err,collision=same or witness)
r=dict(rows=len(rows),confusion={str(k):v for k,v in conf.items()},errors_by_state=by,count_only=audit(tables[0]),typed_fan=audit(tables[1]));print(r);(D/'ramsey_sector_corner_side.json').write_text(json.dumps(r,indent=2)+'\n')

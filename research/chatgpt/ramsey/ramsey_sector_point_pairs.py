"""Point-pair holdout; use geometric readers for exterior inputs. Compare oracle only after inference."""
from ramsey_sector_arrow_bridge import features,ws,point,cal,S,read,D,json,Counter,combinations,op,sides
from ramsey_sector_square_rim import cycles
from ramsey_sector_rim_tick import allowed
from functools import lru_cache

def side_point(x,e,m):
    cs=[c for f,c in cycles.items() if x in f and e<=f];
    if not cs:return False
    c,=cs;i=c.index(x);forward={c[(i+1)%4],c[(i+2)%4]}==e;return (m in c)!=forward

def geometric(a,b,m):
    a,b=sorted((a,b),key=len)
    if a&b:return False
    if len(b)==4:return m in allowed(b,a,1)
    if len(a)==2:return read(a,b,m)
    return side_point(next(iter(a)),b,m)

def seven(g,m,k=7):
    if not k:return ()
    while m.bit_count()>=k:
        b=m&-m;m^=b;i=b.bit_length()-1;t=seven(g,m&g[i],k-1)
        if t is not None:return (i,)+t
    return None

def run(s):
    m=point[''.join(map(str,cal[str(s)]))];r=[0]*35;b=r.copy();pins=[];pending=[];pts=sorted(point.values());
    def setpair(i,j,y):
        g=r if y else b;g[i]|=1<<j;g[j]|=1<<i
    for i,j in combinations(range(35),2):
        if i==0:y=j<=8
        elif i<9:y=j>=9 and pts[i-1] in features[j-9]
        else:
            x,z=features[i-9],features[j-9]
            if len(x)==len(z)==1:pending.append((i,j));continue
            y=geometric(x,z,m)
        setpair(i,j,y)
    init=pending.copy();rounds=[];proof={};votes={}
    for i,j in init:
        x,z=(next(iter(features[k-9])) for k in (i,j));v=[]
        for rim,c in cycles.items():
            if {x,z}<=rim:
                v.append(any(m in allowed(rim,{a},1) for a in (x,z)))
        votes[i,j]=any(v)
    while pending:
        f=[]
        for i,j in pending:
            common=r[i]&r[j];w=seven(b,b[i]&b[j]);assert not(common and w is not None)
            if common or w is not None:f.append((i,j,not common));proof[f'{i},{j}']=dict(red=not common,witness=list(w) if w is not None else [(common&-common).bit_length()-1])
        if not f:break
        rounds.append([sum(c for _,_,c in f),sum(not c for _,_,c in f)]);
        for i,j,c in f:setpair(i,j,c);pending.remove((i,j))
    ix={p:k for k,p in enumerate(e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])};hist=Counter();oracle=[]
    for i,j in init:
        y=ws[s]>>ix[i-9,j-9]&1;hist[int(votes[i,j]),y]+=1;assert (i,j) in pending or bool(r[i]>>j&1)==bool(y);oracle.append((next(iter(features[i-9])),next(iter(features[j-9])),y))
    form=lambda x,z: frozenset((x,z)) in sides or {x,z}=={m,op[m]};assert all(form(x,z)==bool(y) for x,z,y in oracle)
    for (i,j),k in ix.items():
        a,z=features[i],features[j];calc=form(next(iter(a)),next(iter(z))) if len(a)==len(z)==1 else geometric(a,z,m);assert calc==bool(ws[s]>>k&1)
    return dict(mark=m,full_mask_checked=len(ix),rounds=rounds,open=pending,proof=proof,votes={str(k):v for k,v in hist.items()},point_truth=oracle)
if __name__=='__main__':
    out=[run(i) for i in range(8)];print([(o['mark'],o['rounds'],len(o['open']),o['votes']) for o in out]);(D/'ramsey_sector_point_pairs.json').write_text(json.dumps(out,indent=2)+'\n')

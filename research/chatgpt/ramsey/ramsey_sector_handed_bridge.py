"""Check the exploratory oriented-bridge formula against independent stored wirings, not just compiled pair rules."""
from ramsey_address_to_cube import S,D,json,combinations
from itertools import product
from collections import Counter
V=list(product(range(2),repeat=3));neg=lambda v:tuple(1-x for x in v);sub=lambda v,u:tuple(y-x for x,y in zip(u,v));dist=lambda a,b:sum(i!=j for i,j in zip(a,b));
def det(a,b,c):return sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3]) for i in range(3))
def predict(A,B):
    if tuple(map(abs,sub(*A)))==tuple(map(abs,sub(*B))):return ('parallel',set(V) if min(dist(a,b) for a in A for b in B)==1 else set())
    (u,v),=[(a,b) for a in A for b in B if dist(a,b)==1];i,=set(A)-{u};j,=set(B)-{v};h=det(sub(i,u),sub(j,v),sub(v,u));assert abs(h)==1;return h,({u,v} if h<0 else {neg(u),neg(v)})
co=json.loads((D/'ramsey_nine_opposite_faces.json').read_text())['label_coordinates'];coord=lambda x:tuple(x>>i&1 for i in range(3));addr=[[coord(co[j]) for j in range(8) if m>>j&1] for m in S];ws=json.loads((D/'ramsey_nine_frame_readout.json').read_text())['coordinate_ordered_wirings'];counts=Counter();wrong=Counter();flip=0;actual=Counter()
# Decode physical corner using ONLY three independent (non-side-pair) probe columns of the pre-existing cube chart.
from ramsey_cube_pair_rules import G
from ramsey_address_to_cube import probes
feat=lambda A:''.join(str(z[0]) if len(set(z))==1 else '*' for z in zip(*A));lookup={}
for key,cs in json.loads((D/'ramsey_cube_pair_rules.json').read_text()).items():
    for g in G:lookup[tuple(sorted(map(g,key.split()))) ]={g(c,state=True) for c in cs}
cal={};
for v in V:
    word=''.join(map(str,v));s=sum((word in lookup[tuple(sorted((feat(addr[i]),feat(addr[j]))))])<<k for k,(i,j) in enumerate(probes));cal[s]=v
assert len(cal)==8 and all(len(addr[i])!=2 or len(addr[j])!=2 for i,j in probes);naive=0
for n,(i,j) in enumerate((e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])):
    a,b=addr[i],addr[j];
    if len(a)!=2 or len(b)!=2:continue
    k,R=predict(a,b);assert (k,R)==predict(b,a);counts[str(k)]+=1
    for s,w in enumerate(ws):
        v=cal[s];y=w>>n&1;naive+=((coord(s) in R)!=y);wrong[str(k)]+=(v in R)!=y;actual[str(k)]+=y;flip+=((neg(v) in R)!=y)
r=dict(corner_by_probe_word=cal,naive_bit_order_errors=naive,pair_classes=counts,errors=wrong,red=actual,reversed_hand_errors=flip,decisions=sum(counts.values())*len(ws));print(r);(D/'ramsey_sector_handed_bridge.json').write_text(json.dumps(r,indent=2)+'\n')

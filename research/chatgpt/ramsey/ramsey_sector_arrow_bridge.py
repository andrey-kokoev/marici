"""Native arrow reader. No ray coordinates in the edge-color predicate. Recover physical ray names only for identifying chart data during scoring."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());T=load(D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json')['triangles_and_transports'];V=set('ABCD');F={r['triangle'][0] for r in T};inc={f:{x for x in V if x in f[2:]} for f in F};op={f:(V-z).pop() for f,z in inc.items()};op.update({v:f for f,v in list(op.items())});arrows={(f,a,b) for r in T for f,a,b in [r['triangle']]};sides={frozenset((f,v)) for f,z in inc.items() for v in z}

def read(e,h,m,reverse=False):
    bridges=[k for k in sides if k&e and k&h];assert e.isdisjoint(h)
    if len(bridges)!=1:return len(bridges)==2 # two common connectors span one square, zero = opposite parallel
    k,=bridges;f,=k&F;b,=k&V;left=e if f in e else h;a,=left&V;near=((f,b,a) in arrows)^reverse;return (m if near else op[m]) in k

# Evaluation adapter, not an input to read().
from ramsey_address_to_cube import S
co=load(D/'ramsey_nine_opposite_faces.json')['label_coordinates'];coords={'A':'111','B':'100','C':'010','D':'001'};coords.update({f:''.join(str(1-int(i)) for i in coords[op[f]]) for f in F});point={v:k for k,v in coords.items()};bits=lambda n:''.join(str(n>>i&1) for i in range(3));features=[frozenset(point[bits(co[j])] for j in range(8) if s>>j&1) for s in S];cal=load(D/'ramsey_sector_handed_bridge.json')['corner_by_probe_word'];ws=load(D/'ramsey_nine_frame_readout.json')['coordinate_ordered_wirings'];assert set(features)&sides==sides;err=Counter();classes=Counter();example=None
for n,(i,j) in enumerate((e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])):
    e,h=features[i],features[j]
    if e not in sides or h not in sides:continue
    ks=[k for k in sides if k&e and k&h];classes[len(ks)]+=1
    for t,w in enumerate(ws):
        m=point[''.join(map(str,cal[str(t)]))];y=bool(w>>n&1);p=read(e,h,m);assert p==read(h,e,m) and p==read(e,h,op[m],True);err['forward']+=p!=y;err['reverse']+=read(e,h,m,True)!=y
        if example is None and len(ks)==1 and m in ks[0] and y:example=dict(sides=[sorted(e),sorted(h)],bridge=sorted(ks[0]),mark=m)
out=dict(pair_counts_by_connector_count=classes,errors=err,comparisons=sum(classes.values())*8,example=example);print(out);(D/'ramsey_sector_arrow_bridge.json').write_text(json.dumps(out,indent=2)+'\n')

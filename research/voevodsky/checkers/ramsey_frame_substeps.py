"""Test both orders of the two disjoint swaps in each native frame move. Stage 1 must preserve the named address set, the list of allowed edge slots, then membership in the eight-wiring chart. Do not renumber a displaced chart to manufacture a stage."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];raw=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=raw['address_masks'];E=list(map(tuple,raw['edge_order']));W=set(raw['wirings'])
def test(swaps):
 p=list(range(7))
 for i,j in swaps:p[i],p[j]=p[j],p[i]
 T=[sum(1<<p[i] for i in range(7) if s>>i&1) for s in S];lost=len(set(T)-set(S));out={'missing_addresses':lost}
 if lost:return out
 m=list(map(S.index,T));edges=[tuple(sorted((m[i],m[j]))) for i,j in E];out['missing_slots']=len(set(edges)-set(E));
 if out['missing_slots']:return out
 perm=list(map(E.index,edges));image=lambda w:sum(((w>>i)&1)<<v for i,v in enumerate(perm));out['admitted_images']=sum(image(w) in W for w in W);out['unchanged']=sum(image(w)==w for w in W);return out
rows={}
for name,(s,t) in zip('ABC',[((0,1),(2,3)),((0,1),(4,5)),((2,4),(3,5))]):
 rows[name]={'first':test([s]),'other_first':test([t]),'whole':test([s,t])};assert rows[name]['whole']['admitted_images']==8
print(rows);(D/'results/ramsey_frame_substeps.json').write_text(json.dumps(rows,indent=2)+'\n')

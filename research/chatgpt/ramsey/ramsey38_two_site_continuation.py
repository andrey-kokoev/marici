"""Weaker core after one-deletion pilot: omit two frame-fixed label vertices, insert one fresh vertex; exclude restoration of either old row on either output. All input 0, all pairs of old label vertices fixed pointwise by (45)."""
from ramsey38_matching_continuations import data,C,J,D,ls,combinations,json
out=[];witness=None
for x,y in combinations([1,2,3,4,7],2):
 m=1<<x|1<<y;families=[];rest=set()
 for idx in [C[0],J[0]]:
  h,_,t=data[idx];ts=[q for q in t if not q&m];I=[0]
  for i,v in enumerate(h):
   if not m>>i&1:I.extend([s|1<<i for s in I if not s&v]);
  families.append({s for s in I if all(s&q for q in ts)});rest.update([h[x]&~m,h[y]&~m]);
 a,b=families;dif=(a^b)-rest;out.append(dict(deleted=[x,y],counts=[len(a),len(b)],nonrestoration_difference=len(dif)))
 if dif and not witness:
  s=min(dif);ok=s in a;h,_,t=data[J[0] if ok else C[0]];witness=dict(input_index=0,outputs=[C[0],J[0]],deleted=[x,y],support=ls(s),legal=[ok,not ok],red_conflict=next(([u,v] for u,v in combinations(ls(s),2) if h[u]>>v&1),None),missed_seven=next((ls(q) for q in t if not q&(m|s)),None))
r=dict(tests=out,witness=witness);print(r);(D/'ramsey38_two_site_continuation.json').write_text(json.dumps(r,indent=2)+'\n')

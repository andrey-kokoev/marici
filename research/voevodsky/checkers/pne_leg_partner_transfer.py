"""Holdout of same-leg-outside vs other-leg-inside on actual ordered sector triangles. No per-face reorientation or output fitting. Every corner supplies a middle anchor pair; demand two distinct neighbouring sectors. Compare the signed outer pattern, not mere existence of a four-record table."""
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1];tri=[s['triangle'] for s in json.loads((D.parent/'nima/results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']];edges=[[tuple(t[i:]+t[:i])[:2] for i in range(3)] for t in tri];out=[]
for k,t in enumerate(tri):
 for i,v in enumerate(t):
  a=(t[i-1],v);b=(v,t[(i+1)%3]);pairs=[]
  for e in (a,b):
   (l,q),=[(l,q) for l,es in enumerate(edges) if l!=k for q in es if set(q)==set(e)];pairs.append((l,q))
  assert pairs[0][0]!=pairs[1][0];rows=[(pairs[0][1],a),(a,b),(b,a),(b,pairs[1][1])];roles=[[('end' if e[1]==v else 'start') for e in row] for row in rows];sizes=[len(set(a)&set(b)) for a,b in rows];assert sizes==[2,1,1,2];out.append(dict(middle=t,pivot=v,rows=rows,roles=roles,outer_agreement=[pairs[0][1]==a,pairs[1][1]==b]))
r=dict(sector_corners=len(out),unique_partners=len(out),outer_patterns=dict(Counter(str(s['outer_agreement']) for s in out)),example=out[0]);print(r);(D/'results/pne_leg_partner_transfer.json').write_text(json.dumps(r,indent=2)+'\n')

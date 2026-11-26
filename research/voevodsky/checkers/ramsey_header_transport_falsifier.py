"""Hostile control: endpoint-color transports on the Shrikhande and 4x4 rook graphs. State I/R/B relative to start; propagate all three channels, including the neutral return to the start. Verify strong lumpability for every ordered pair."""
import json,itertools
from ramsey_retention_slice import D,check
V=list(itertools.product(range(4),repeat=2));out={}
for name in ['rook','Shrikhande']:
 def color(i,j):
  if i==j:return 'I'
  x,y=V[i];u,v=V[j];red=(x==u or y==v) if name=='rook' else ((u-x)%4,(v-y)%4) in {(0,1),(0,3),(1,0),(3,0),(1,1),(3,3)};return 'R' if red else 'B'
 a=[sum(1<<j for j in range(16) if color(i,j)=='R') for i in range(16)];T={}
 for i,j in itertools.product(range(16),repeat=2):
  h=[[sum(color(j,k)==c and color(i,k)==b for k in range(16)) for b in 'IRB'] for c in 'RB'];s=color(i,j);assert s not in T or T[s]==h;T[s]=h
 red4=[q for q in itertools.combinations(range(16),4) if all(color(i,j)=='R' for i,j in itertools.combinations(q,2))];out[name]=dict(table=T,red_four_count=len(red4),example=red4[:1],valid45=check(a,65535,4,5));
assert out['rook']['table']==out['Shrikhande']['table'] and not out['rook']['valid45'] and out['Shrikhande']['valid45'];print(out);(D.parent/'ramsey_header_transport_falsifier.json').write_text(json.dumps(out,indent=1)+'\n')

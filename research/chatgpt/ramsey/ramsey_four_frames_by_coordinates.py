"""Construct the four row-compatible C5 subgroups from two binary choices. Compare against the independent 36-group audit only after construction."""
I=tuple(range(6));r=(1,0,2,3,5,4);names=('12','13','14','23','24','34');built=set()
for hub in (2,3):
 zero=5-hub
 for sign in (1,-1):
  chart={zero:0,0:1,1:4,5:(2*sign)%5,4:(-2*sign)%5};back={v:k for k,v in chart.items()};g=list(I)
  for x,k in chart.items():g[x]=back[(k+1)%5]
  assert all(chart[r[x]]==(-k)%5 for x,k in chart.items())
  p=I;G=[]
  for _ in range(5):G.append(p);p=tuple(g[x] for x in p)
  built.add(frozenset(G));print('hub',names[hub],'zero',names[zero],'coordinates',{names[x]:k for x,k in chart.items()})
assert len(built)==4
from ramsey_row_quotient_constructor import compatible
assert built==set(compatible);print('two hub choices times two relative signs exhaust the compatible frames')

"""Pure-Python 35-vertex construction from cube cells only. No files, SAT solver, or graph catalogue needed. Bit complement fixes *. Cyclically rotate coordinates and optionally complement all bits."""
from itertools import product,combinations
from collections import Counter
cells=[''.join(x) for x in product('01*',repeat=3) if x!=('*','*','*')];corner=[c for c in cells if '*' not in c];G=[0]*35
def edge(i,j):G[i]|=1<<j;G[j]|=1<<i
def red(a,b):edge(cells.index(a),cells.index(b))
def orbit(a,b):
 for _ in range(3):
  red(a,b);red(a.translate(str.maketrans('01','10')),b.translate(str.maketrans('01','10')));a=a[1:]+a[:1];b=b[1:]+b[:1]
for a,b in combinations(cells,2):
 # Cube edges on corner vertices; opposite faces; opposite parallel edges of a square face.
 if [i for i in range(3) if a[i]=='*']==[i for i in range(3) if b[i]=='*'] and sum(x!=y for x,y in zip(a,b))==1:red(a,b)
red('000','111')
for a,b in [('**0','*11'),('**0','0*1'),('**0','011'),('*00','0*1'),('*00','001'),('*00','110'),('*01','100'),('*01','111')]:orbit(a,b)
assert sum(v.bit_count() for v in G)==152
for j,c in enumerate(corner,26):
 edge(34,j)
 for i,s in enumerate(cells):
  if all(x=='*' or x==y for x,y in zip(s,c)):edge(i,j)
assert all(v.bit_count()==8 for v in G);assert all(not G[i]&G[j] for i,j in combinations(range(35),2) if G[i]>>j&1);I=[0]
for i,v in enumerate(G):I.extend([s|1<<i for s in I if not s&v]);
h=Counter(s.bit_count() for s in I);assert max(h)==8;print('35 vertices, 140 red edges, triangle-free; independence number',max(h),'with',h[8],'blue eights.')

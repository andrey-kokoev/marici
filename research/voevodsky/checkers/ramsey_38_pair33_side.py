"""At e=33 the exclusive cross graph is K4,4 minus a matching. Its four rows per side are disjoint independent triples. Enumerate a side and search compatible opposite sides."""
import json,itertools
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_38_common49.json').read_text())['triples'];out={};E=[(i,j) for j in range(15) for i in range(j)]
for h in rows:
 m=int(h,16)
 if m.bit_count()!=33:continue
 a=[0]*15
 for k,(i,j) in enumerate(E):
  if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not v&s])
 S=[s for s in I if s.bit_count()==3 and all((a[i]&a[j]).bit_count()<3 for i,j in E if s>>i&1 and s>>j&1)];Q=[[q for q in I if q.bit_count()==n] for n in (3,4,5)];M=[[sum(1<<i for i,q in enumerate(qs) if not q&s) for s in S] for qs in Q];G=[{j for j in range(i+1,len(S)) if not s&S[j] and not M[2][i]&M[2][j]} for i,s in enumerate(S)];sides=[]
 for i,adj in enumerate(G):
  for j in adj:
   both=adj&G[j];four=M[1][i]&M[1][j]
   for k in both:
    if four&M[1][k]:continue
    block=four|((M[1][i]|M[1][j])&M[1][k]);three=M[0][i]&M[0][j]&M[0][k]
    for l in both&G[k]:
     if not block&M[1][l] and not three&M[0][l]:sides.append([S[t] for t in (i,j,k,l)])
 def compat(s,t):
  return all(sum(bool(x&y) for y in t)<=1 for x in s) and all(sum(bool(x&y) for x in s)<=1 for y in t)
 passes=any(compat(s,t) for i,s in enumerate(sides) for t in sides[i:]);out[h]=[len(sides),passes]
print(len(out),sum(bool(s) for s,t in out.values()),sum(t for s,t in out.values()));(P/'ramsey_38_pair33_side.json').write_text(json.dumps(out)+'\n')

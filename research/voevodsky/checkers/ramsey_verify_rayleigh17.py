"""Standalone integer replay: no SDP, numpy or catalogue libraries. Check square quartet against all blue demands and path Gram certificate against the support conflict pattern."""
from pathlib import Path
import json,itertools
p=Path(__file__).resolve().parents[1]/'results';rows=json.loads((p/'ramsey_support_rayleigh17.json').read_text());controls=json.loads((p/'ramsey_frozen_gain_control.json').read_text())[1]
for r in rows:
 a=r['core'];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];assert S==r['supports'];Q=[q for q in I if q.bit_count()==5];m=[sum(1<<i for i,q in enumerate(Q) if not q&s) for s in S];assert all(m)
 if 'dual' not in r:
  w=next(c['supports'] for c in controls if c['core']==a);assert len(w)==4 and all(s in I for s in w) and all(q.bit_count()+sum(not s&q for s in w)<=6 for q in I);continue
 z=r['dual'];T=r['T'];scale=r['scale'];n=len(S);assert len(z)==n and all(len(row)==n for row in z) and 0<T<4*scale
 for i in range(n):
  for j in range(n):assert z[i][j]==z[j][i] and (not z[i][j] or (i!=j and m[i]&m[j]))
 h=[[T*(i==j)+z[i][j]-scale for j in range(n)] for i in range(n)];prev=1
 for i in range(n):
  pivot=h[i][i];assert pivot>0
  for j in range(i+1,n):
   for k in range(i+1,n):h[j][k],rem=divmod(pivot*h[j][k]-h[j][i]*h[i][k],prev);assert not rem
  prev=pivot
 print('verified',n,'positive leading minors; bound',T,'/',scale)

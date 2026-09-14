#!/usr/bin/env python3
"""Extract exact rational countercycles at cutoff 960."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]; RESULT=ROOT/'research/voevodsky/results/coded_modulation_countercycles.json'; L=960
def primes_upto(n):
 out=[]
 for x in range(2,n+1):
  if all(x%p for p in out if p*p<=x): out.append(x)
 return out
ps=primes_upto(L//2+2); E=[]
for j,(p,q) in enumerate(zip(ps,ps[1:])):
 for k in range(1,L//(p*q)+1): E.append((k*p*q,j,k,p,q,k*p,k*q))
E.sort(); V=sorted({e[5] for e in E}|{e[6] for e in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
for col,e in enumerate(E): B[vi[e[5]],col]-=1; B[vi[e[6]],col]+=1
def witness(code):
 D=s.diag(*[code(e) for e in E]); M=s.Matrix.vstack(B,B*D); ns=M.nullspace(); z=ns[0]; support=[{'edge_index':i,'shell_index':E[i][1],'shell':[E[i][3],E[i][4]],'scale':E[i][2],'interval':[E[i][5],E[i][6]],'coefficient':str(z[i])} for i in range(len(E)) if z[i]!=0]
 return {'nullity':len(E)-M.rank(),'support_size':len(support),'support':support,'verified_boundary':B*z==s.zeros(B.rows,1),'verified_modulated_boundary':B*D*z==s.zeros(B.rows,1)}
result={'schema':'marici.voevodsky.coded-modulation-countercycles.v1','cutoff':L,'edge_count':len(E),'shell_code':witness(lambda e:e[1]+1),'scale_code':witness(lambda e:e[2])}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'shell':(result['shell_code']['nullity'],result['shell_code']['support_size']),'scale':(result['scale_code']['nullity'],result['scale_code']['support_size'])})); raise SystemExit(0 if all(result[k]['verified_boundary'] and result[k]['verified_modulated_boundary'] for k in ('shell_code','scale_code')) else 1)

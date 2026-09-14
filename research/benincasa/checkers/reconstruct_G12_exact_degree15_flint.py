#!/usr/bin/env python3
"""Exact degree-15 reconstruction using modular pivot scouting and FLINT rational solve."""
import gzip,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
import sympy as s
from flint import fmpq_mat
pres=json.loads((ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').read_text());ov=json.loads((ROOT/'research/benincasa/results/G12_coefficient_overlap_representatives.json').read_text());data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
lines=gzip.decompress((ROOT/pres['matrix_artifact']).read_bytes()).decode().splitlines();nr,nc,_=map(int,lines[1].split());columns=[];labels=[]
for _ in range(nc):columns.append({});labels.append(None)
for line in lines[2:]:r,j,x=line.split();p,q=x.split('/');assert q=='1';columns[int(j)-1][int(r)-1]=int(p)
for j in range(nc):labels[j]={'kind':'d0','column':j}
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};rows=[(i,j,d-i-j) for d in range(19) for i in range(d+1) for j in range(d-i+1)];ridx={e:i for i,e in enumerate(rows)}
base=[dict(s.Poly(s.sympify(col['formula'],locals=L),a,b,c).terms()) for col in ov['columns']]
for edge,coeff in zip([x['overlap'] for x in ov['columns']],base):
 for d in range(16):
  for i in range(d+1):
   for j in range(d-i+1):
    m=(i,j,d-i-j);columns.append({ridx[tuple(e[k]+m[k] for k in range(3))]:int(x) for e,x in coeff.items()});labels.append({'kind':'overlap','edge':edge,'monomial':m})
q=[b+c+1,a+c+1,b+c+2,a+c+2];N=s.Poly(s.expand(s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L)*q[3]**3-s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L)*q[2]**3),a,b,c);target={ridx[e]:int(x) for e,x in N.terms()}
def insert(v,B,p):
 while v:
  z=max(v);t=v[z]%p
  if not t:v.pop(z);continue
  if z not in B:
   inv=pow(t,-1,p);B[z]={e:x*inv%p for e,x in v.items() if x%p};return True
  for e,x in B[z].items():
   y=(v.get(e,0)-t*x)%p
   if y:v[e]=y
   else:v.pop(e,None)
 return False
start=time.time();prime=32003;B={};selected=[]
for j,col in enumerate(columns):
 if insert({r:x%prime for r,x in col.items()},B,prime):selected.append(j)
assert len(selected)==1223
# Select independent rows of the pivot-column matrix.
RB={};selected_rows=[]
for r in range(nr):
 v={j:columns[col].get(r,0)%prime for j,col in enumerate(selected) if columns[col].get(r,0)%prime}
 if insert(v,RB,prime):selected_rows.append(r)
assert len(selected_rows)==len(selected)
n=len(selected);A=fmpq_mat(n,n);rhs=fmpq_mat(n,1)
for i,r in enumerate(selected_rows):
 rhs[i,0]=target.get(r,0)
 for j,col in enumerate(selected):
  x=columns[col].get(r,0)
  if x:A[i,j]=x
sol=A.solve(rhs);coeff=[sol[i,0] for i in range(n)]
# Verify against every ambient row over Q.
for r in range(nr):
 assert sum(coeff[j]*columns[col].get(r,0) for j,col in enumerate(selected))==target.get(r,0),r
terms=[]
for col,x in zip(selected,coeff):
 if x:terms.append({**labels[col],'coefficient':str(x)})
height=max(max(abs(int(x.p)),int(x.q)) for x in coeff if x);out={'schema':'marici.benincasa.G12-exact-degree15-reconstruction.v1','prospective_action':'R_exact_degree15','ambient_shape':[nr,len(columns)],'modular_pivot_rank':n,'square_minor_rows':len(selected_rows),'nonzero_solution_terms':len(terms),'coefficient_height':height,'solution':terms,'resolution':'++','verification':'all 1330 coefficient rows agree exactly over Q','elapsed_seconds':round(time.time()-start,3),'passed':True};p=ROOT/'research/benincasa/results/G12_exact_degree15_reconstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('passed','resolution','nonzero_solution_terms','coefficient_height','elapsed_seconds')}))

"""Independently replay the polynomial contraction identities exported by ChatGPT."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];cp=ROOT/'research/chatgpt/full_q_support_relative_morse_certificate.json';x=json.loads(cp.read_text())
N=len(x['Q_base_states']);K=len(x['cellular_Q_labels']);vars=x['coefficients']['variables'];idx={v:i for i,v in enumerate(vars)}
plus={idx[v] for v in ('X13','X15','X35')};minus={idx[v] for v in ('X02','X04','X24')}
def addp(a,b):
 c=dict(a)
 for m,z in b.items():c[m]=c.get(m,0)+z
 return {m:z for m,z in c.items() if z}
def mulp(a,b):
 c={}
 for u,z in a.items():
  for v,w in b.items():
   m=tuple(i+j for i,j in zip(u,v))
   if any(m[i] for i in plus) and any(m[i] for i in minus):continue
   c[m]=c.get(m,0)+z*w
 return {m:z for m,z in c.items() if z}
def negp(a):return {m:-z for m,z in a.items()}
def mat(rows):
 M={}
 for e in rows:
  p={tuple(m):z for m,z in e['polynomial']}
  key=(e['target'],e['source']);M[key]=addp(M.get(key,{}),p)
 return M
D=mat(x['Q_base_differential']);P=mat(x['Q_to_cellular']);I=mat(x['cellular_to_Q']);H=mat(x['Q_contraction'])
def compose(A,B):
 # A after B
 C={};by={}
 for (r,k),p in A.items():by.setdefault(k,[]).append((r,p))
 for (k,c),q in B.items():
  for r,p in by.get(k,[]):C[(r,c)]=addp(C.get((r,c),{}),mulp(p,q))
 return {k:v for k,v in C.items() if v}
def madd(*xs):
 C={}
 for A in xs:
  for k,p in A.items():C[k]=addp(C.get(k,{}),p)
 return {k:v for k,v in C.items() if v}
zero=(0,)*len(vars)
def ident(n):return {(i,i):{zero:1} for i in range(n)}
PI=compose(P,I);IP=compose(I,P);DH=compose(D,H);HD=compose(H,D)
assert PI==ident(K),(len(PI),K)
assert madd(DH,HD)==madd(ident(N),{k:negp(v) for k,v in IP.items()})
# chain-map equations too
# Infer cellular differential from exported rows.
DC=mat(x['cellular_Q_differential'])
assert compose(P,D)==compose(DC,P)
assert compose(D,I)==compose(I,DC)
out={'schema':'nima.full_q_contraction_replay.v1','status':'passed','certificate':cp.relative_to(ROOT).as_posix(),'certificate_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'base_states':N,'cellular_states':K,'differential_entries':len(x['Q_base_differential']),'projection_entries':len(x['Q_to_cellular']),'inclusion_entries':len(x['cellular_to_Q']),'homotopy_entries':len(x['Q_contraction']),'identities':['p_i=id','d_h+h_d=id-i_p','p_d=d_p','d_i=i_d'],'mixed_sheet_products_reduced':True,'numeric_sampling':False}
op=ROOT/'research/nima/results/full-q-contraction-replay.json';op.write_text(json.dumps(out,indent=2)+'\n');print(out)

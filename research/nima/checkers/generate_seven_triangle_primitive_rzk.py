"""Generate the seven-triangle primitive and its three-term roof boundary."""
from pathlib import Path
import json,hashlib,importlib.util,sys,subprocess
ROOT=Path(__file__).resolve().parents[3];cert=ROOT/'research/chatgpt/full_q_support_relative_morse_certificate.json';x=json.loads(cert.read_text())
src=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py';saved=sys.argv;sys.argv=[str(src),'--cell-limit','1'];sp=importlib.util.spec_from_file_location('g7',src);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g);sys.argv=saved
tri=[(38,0,1),(246,0,1),(247,0,-1),(273,0,-1),(274,0,1),(307,1,-1),(309,1,1)]
S={i for i,_,_ in tri};es=[e for e in x['Q_base_differential'] if e['source'] in S];targets=sorted(set(e['target'] for e in es));states=[('t',i) for i,_,_ in tri]+[('r',i) for i in targets]
name=lambda k,i:f'nima-seven-{k}-{i}'
cols={s:[] for s in states}
for e in es:
 poly=e['polynomial'];assert len(poly)==1;exp=sum(poly[0][0]);coef=poly[0][1];assert exp in (0,1) and coef in (-1,1)
 cols[('t',e['source'])].append((('r',e['target']),exp,coef))
def nat(n):return 'marici-zero' if n==0 else f'(marici-succ {nat(n-1)})'
def atom(st,n):return g.app('nima-sum-atom','NimaSevenTriangleBasis',f'({name(*st)},{nat(n)})')
def sumterms(ts):
 out=g.app('nima-sum-zero','NimaSevenTriangleBasis')
 for st,n,c in reversed(ts):
  z=atom(st,n);z=g.app('nima-sum-neg','NimaSevenTriangleBasis',z) if c<0 else z;out=g.app('nima-sum-add','NimaSevenTriangleBasis',z,out)
 return out
L=['# Recovered seven-triangle Morse primitive','','```rzk','#lang rzk-1','#data NimaSevenTriangleState','  := '+name(*states[0])]+['  | '+name(*s) for s in states[1:]]
L += ['','#define NimaSevenTriangleBasis : U := Sigma (_ : NimaSevenTriangleState), MariciNat','#define NimaSevenTriangle : U := NimaZSum NimaSevenTriangleBasis','#define nima-seven-column : NimaSevenTriangleBasis -> NimaSevenTriangle','  := \\ (q,n) -> match q into (\\ _ -> MariciNat -> NimaSevenTriangle) (']
for j,s in enumerate(states):
 terms=[]
 for t,e,c in cols[s]:terms.append((t, f'(marici-succ n)' if e else 'n',c))
 # custom because exponent string
 out=g.app('nima-sum-zero','NimaSevenTriangleBasis')
 for t,en,c in reversed(terms):
  z=g.app('nima-sum-atom','NimaSevenTriangleBasis',f'({name(*t)},{en})');z=g.app('nima-sum-neg','NimaSevenTriangleBasis',z) if c<0 else z;out=g.app('nima-sum-add','NimaSevenTriangleBasis',z,out)
 L += [('    ' if j==0 else '  | ')+name(*s)+' => \\ n -> '+out]
L += ['  ) n','#define nima-seven-d : NimaSevenTriangle -> NimaSevenTriangle := nima-sum-bind NimaSevenTriangleBasis NimaSevenTriangleBasis nima-seven-column',
 '#define nima-seven-morse-primitive : NimaSevenTriangle := '+sumterms([(('t',i),n,c) for i,n,c in tri]),
 '#define nima-seven-corrected-roof : NimaSevenTriangle := '+sumterms([(('r',22),0,1),(('r',286),0,-1),(('r',319),1,1)])]
# Build exact evaluation syntax of d primitive and roof.
keys=[]
def A(st,n):
 k=(st,n)
 if k not in keys:keys.append(k)
 return ('a',keys.index(k))
def col_expr(st,n):
 o=('z',)
 for t,e,c in reversed(cols[st]):
  z=A(t,n+e);z=('n',z) if c<0 else z;o=('+',z,o)
 return o
lhs=('z',)
for i,n,c in reversed(tri):
 z=col_expr(('t',i),n);z=('n',z) if c<0 else z;lhs=('+',z,lhs)
rhs=('z',)
for st,n,c in reversed([(('r',22),0,1),(('r',286),0,-1),(('r',319),1,1)]):
 z=A(st,n);z=('n',z) if c<0 else z;rhs=('+',z,rhs)
nl,pl=g.normalize(lhs);nr,pr=g.normalize(rhs);assert nl==nr
proof=g.path(g.expr(lhs),g.total(nl),g.expr(rhs),pl,g.rev(g.expr(rhs),g.total(nr),pr))
vals=[g.app('probe',f'({name(*st)},{nat(n)})') for st,n in keys]
L += ['','#define nima-seven-morse-boundary : nima-sum-equal NimaSevenTriangleBasis (nima-seven-d nima-seven-morse-primitive) nima-seven-corrected-roof','  := \\ probe -> '+g.app('(\\ ('+' '.join('a'+str(i) for i in range(len(keys)))+' : MariciInt) -> '+proof+')',*vals),'```','']
out=ROOT/'research/nima/rzk/42-seven-triangle-morse-primitive.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),'primitive_terms':7,'local_differential_entries':len(es),'boundary_terms':3,'states':len(states),'requires_rzk_check':True};(ROOT/'research/nima/results/seven-triangle-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)

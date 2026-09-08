"""Generate the finite physical six-point source J and its conductor map."""
from pathlib import Path
import importlib.util,sys,subprocess,hashlib,json
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py'
saved=sys.argv;sys.argv=[str(src),'--cell-limit','1'];sp=importlib.util.spec_from_file_location('gphys',src);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g);sys.argv=saved
Z=g.Z;app=g.app;add=g.add;neg=g.neg
state=lambda i:f'nima-physical-j-state-{i}'
cols={i:[] for i in range(11)}
def edge(i,j,sgn=1):cols[i].append((j,sgn))
# J3 state0 -> J2 states1..4
for j in (2,3,4):edge(0,j)
# d2 columns
edge(1,5);edge(1,6)
edge(2,7);edge(2,8,-1)
edge(3,8);edge(3,9,-1)
edge(4,7,-1);edge(4,9)
# d1
edge(5,10);[edge(i,10,-1) for i in range(6,10)]
def sparse(items):
 out=app('nima-sum-zero','NimaPhysicalJBasis')
 for j,sgn in reversed(items):
  z=app('nima-sum-atom','NimaPhysicalJBasis',state(j));z=app('nima-sum-neg','NimaPhysicalJBasis',z) if sgn<0 else z
  out=app('nima-sum-add','NimaPhysicalJBasis',z,out)
 return out
L=['# Physical six-point source and conductor augmentation','','```rzk','#lang rzk-1','#data NimaPhysicalJState','  := '+state(0)]+['  | '+state(i) for i in range(1,11)]
L += ['','#define NimaPhysicalJBasis : U := NimaPhysicalJState','#define NimaPhysicalJ : U := NimaZSum NimaPhysicalJBasis','#define nima-physical-j-column : NimaPhysicalJBasis -> NimaPhysicalJ','  := \\ q -> match q']
for i in range(11):L += [('       (' if i==0 else '       | ')+state(i)+' => '+sparse(cols[i])]
L += ['       )','#define nima-physical-j-d : NimaPhysicalJ -> NimaPhysicalJ','  := nima-sum-bind NimaPhysicalJBasis NimaPhysicalJBasis nima-physical-j-column']
# square patterns
patterns={};per=[]
for i in range(11):
 keys=[];e=('z',)
 def atom(j):
  if j not in keys:keys.append(j)
  return ('a',keys.index(j))
 for j,sgn in reversed(cols[i]):
  inn=('z',)
  for k,s2 in reversed(cols[j]):
   z=atom(k);z=('n',z) if s2<0 else z;inn=('+',z,inn)
  if sgn<0:inn=('n',inn)
  e=('+',inn,e)
 if e not in patterns:
  normal,pf=g.normalize(e);assert not normal
  idx=len(patterns);patterns[e]=idx
  args=' (a'+ ' a'.join(map(str,range(len(keys))))+' : MariciInt)' if keys else ''
  L += ['',f'#define nima-physical-j-cancel-{idx}{args} : {g.expr(e)} = {Z} := {pf}']
 per.append((patterns[e],keys))
for i,(idx,keys) in enumerate(per):
 vals=[app('probe',state(j)) for j in keys]
 L += ['',f'#define nima-physical-j-cell-square-{i} : nima-sum-equal NimaPhysicalJBasis',f'  (nima-physical-j-d (nima-physical-j-column {state(i)})) (nima-sum-zero NimaPhysicalJBasis)',f'  := \\ probe -> '+app(f'nima-physical-j-cancel-{idx}',*vals)]
zexpr=('+',('+',('a',0),('z',)),('+',('n',('a',0)),('z',)))
znormal,zproof=g.normalize(zexpr);assert not znormal
L += ['',f'#define nima-physical-z-cancel (a0 : MariciInt) : {g.expr(zexpr)} = {Z} := {zproof}']
L += ['','#define nima-physical-j-column-square : (q : NimaPhysicalJBasis) ->','  nima-sum-equal NimaPhysicalJBasis (nima-physical-j-d (nima-physical-j-column q)) (nima-sum-zero NimaPhysicalJBasis)','  := \\ q -> match q']
L += [('       (' if i==0 else '       | ')+state(i)+f' => nima-physical-j-cell-square-{i}' for i in range(11)]
L += ['       )','#define nima-physical-j-square (p : NimaPhysicalJ)','  : nima-sum-equal NimaPhysicalJBasis (nima-physical-j-d (nima-physical-j-d p)) (nima-sum-zero NimaPhysicalJBasis)','  := nima-sum-column-square NimaPhysicalJBasis nima-physical-j-column nima-physical-j-column-square p',
 '#define nima-physical-z : NimaPhysicalJ := nima-sum-add NimaPhysicalJBasis (nima-sum-atom NimaPhysicalJBasis nima-physical-j-state-5) (nima-sum-atom NimaPhysicalJBasis nima-physical-j-state-7)',
 '#define nima-physical-z-cycle : nima-sum-equal NimaPhysicalJBasis (nima-physical-j-d nima-physical-z) (nima-sum-zero NimaPhysicalJBasis)',
 '  := \\ probe -> nima-physical-z-cancel (probe nima-physical-j-state-10)',
 '#define nima-physical-a-probe : NimaPhysicalJBasis -> MariciInt','  := \\ q -> match q',
 '       (nima-physical-j-state-0 => marici-int-zero','       | nima-physical-j-state-1 => marici-int-zero','       | nima-physical-j-state-2 => marici-int-zero','       | nima-physical-j-state-3 => marici-int-zero','       | nima-physical-j-state-4 => marici-int-zero','       | nima-physical-j-state-5 => marici-int-zero','       | nima-physical-j-state-6 => marici-int-zero','       | nima-physical-j-state-7 => marici-int-one','       | nima-physical-j-state-8 => marici-int-one','       | nima-physical-j-state-9 => marici-int-one','       | nima-physical-j-state-10 => marici-int-zero)','#define nima-physical-a-C (p : NimaPhysicalJ) : MariciInt := nima-sum-eval NimaPhysicalJBasis nima-physical-a-probe p',
 '#define nima-physical-a-column-zero (q : NimaPhysicalJBasis) : nima-physical-a-C (nima-physical-j-column q) = marici-int-zero','  := match q (nima-physical-j-state-0 => refl | nima-physical-j-state-1 => refl | nima-physical-j-state-2 => refl | nima-physical-j-state-3 => refl | nima-physical-j-state-4 => refl | nima-physical-j-state-5 => refl | nima-physical-j-state-6 => refl | nima-physical-j-state-7 => refl | nima-physical-j-state-8 => refl | nima-physical-j-state-9 => refl | nima-physical-j-state-10 => refl)',
 '#define nima-physical-eval-zero-atoms (probe : NimaPhysicalJBasis -> MariciInt) (zero-atoms : (q : NimaPhysicalJBasis) -> probe q = marici-int-zero) (p : NimaPhysicalJ) : nima-sum-eval NimaPhysicalJBasis probe p = marici-int-zero',
 '  := match p (nima-sum-zero => refl | nima-sum-atom q => zero-atoms q | nima-sum-add x ihx y ihy => nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add (nima-sum-eval NimaPhysicalJBasis probe x) marici-int-zero (nima-sum-eval NimaPhysicalJBasis probe y) marici-int-zero ihx ihy | nima-sum-neg x ih => nima-frame-ap MariciInt MariciInt marici-int-negate (nima-sum-eval NimaPhysicalJBasis probe x) marici-int-zero ih | nima-sum-scale c x ih => nima-frame-concat MariciInt (marici-int-mul c (nima-sum-eval NimaPhysicalJBasis probe x)) (marici-int-mul c marici-int-zero) marici-int-zero (nima-frame-ap MariciInt MariciInt (marici-int-mul c) (nima-sum-eval NimaPhysicalJBasis probe x) marici-int-zero ih) (marici-int-mul-zero-right c))',
 '#define nima-physical-a-chain (p : NimaPhysicalJ) : nima-physical-a-C (nima-physical-j-d p) = marici-int-zero','  := nima-frame-concat MariciInt (nima-physical-a-C (nima-physical-j-d p)) (nima-sum-eval NimaPhysicalJBasis (\\ q -> nima-physical-a-C (nima-physical-j-column q)) p) marici-int-zero (nima-sum-eval-bind NimaPhysicalJBasis NimaPhysicalJBasis nima-physical-j-column nima-physical-a-probe p) (nima-physical-eval-zero-atoms (\\ q -> nima-physical-a-C (nima-physical-j-column q)) nima-physical-a-column-zero p)',
 '#define nima-physical-a-z : nima-physical-a-C nima-physical-z = marici-int-one := refl',
 '#define nima-physical-a-endpoint-left : nima-physical-a-probe nima-physical-j-state-5 = marici-int-zero := refl',
 '#define nima-physical-a-endpoint-right : nima-physical-a-probe nima-physical-j-state-6 = marici-int-zero := refl',
 '#define nima-physical-road-uniqueness (r1 r2 r3 : MariciInt) (r12 : r1 = r2) (r23 : r2 = r3) (normalized : r1 = marici-int-one)','  : Sigma (_ : r1 = marici-int-one), Sigma (_ : r2 = marici-int-one), r3 = marici-int-one','  := (normalized,(nima-frame-concat MariciInt r2 r1 marici-int-one (nima-frame-rev MariciInt r1 r2 r12) normalized, nima-frame-concat MariciInt r3 r2 marici-int-one (nima-frame-rev MariciInt r2 r3 r23) (nima-frame-concat MariciInt r2 r1 marici-int-one (nima-frame-rev MariciInt r1 r2 r12) normalized)))','```','']
out=ROOT/'research/nima/rzk/30-physical-source-comparison.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'states':11,'arrows':sum(map(len,cols.values())),'cancellation_shapes':len(patterns),'requires_rzk_check':True};(ROOT/'research/nima/results/physical-source-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)

"""Generate the 12-state cone fibre of the physical road augmentation."""
from pathlib import Path
import importlib.util,sys,subprocess,hashlib,json
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py'
saved=sys.argv;sys.argv=[str(src),'--cell-limit','1'];sp=importlib.util.spec_from_file_location('gfibre',src);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g);sys.argv=saved
app=g.app;state=lambda i:f'nima-relative-f-state-{i}'
cols={i:[] for i in range(12)}
def edge(i,j,s=1):cols[i].append((j,s))
for j in (2,3,4):edge(0,j)
edge(1,5);edge(1,6);edge(2,7);edge(2,8,-1);edge(3,8);edge(3,9,-1);edge(4,7,-1);edge(4,9)
edge(5,10);edge(6,10,-1)
for i in (7,8,9):edge(i,10,-1);edge(i,11)
def sparse(xs):
 o=app('nima-sum-zero','NimaRelativeFBasis')
 for j,s in reversed(xs):
  z=app('nima-sum-atom','NimaRelativeFBasis',state(j));z=app('nima-sum-neg','NimaRelativeFBasis',z) if s<0 else z;o=app('nima-sum-add','NimaRelativeFBasis',z,o)
 return o
L=['# Relative fibre of the physical road augmentation','','The extra state 11 is the conductor summand in cone degree zero.','', '```rzk','#lang rzk-1','#data NimaRelativeFState','  := '+state(0)]+['  | '+state(i) for i in range(1,12)]
L += ['','#define NimaRelativeFBasis : U := NimaRelativeFState','#define NimaRelativeF : U := NimaZSum NimaRelativeFBasis','#define nima-relative-f-column : NimaRelativeFBasis -> NimaRelativeF','  := \\ q -> match q']
L += [('       (' if i==0 else '       | ')+state(i)+' => '+sparse(cols[i]) for i in range(12)]+['       )','#define nima-relative-f-d : NimaRelativeF -> NimaRelativeF','  := nima-sum-bind NimaRelativeFBasis NimaRelativeFBasis nima-relative-f-column']
patterns={};per=[]
for i in range(12):
 keys=[];e=('z',)
 def atom(j):
  if j not in keys:keys.append(j)
  return ('a',keys.index(j))
 for j,s in reversed(cols[i]):
  q=('z',)
  for k,t in reversed(cols[j]):
   z=atom(k);z=('n',z) if t<0 else z;q=('+',z,q)
  q=('n',q) if s<0 else q;e=('+',q,e)
 if e not in patterns:
  n,pf=g.normalize(e);assert not n;idx=len(patterns);patterns[e]=idx
  args=(' ('+' '.join('a'+str(k) for k in range(len(keys)))+' : MariciInt)') if keys else ''
  L += ['',f'#define nima-relative-f-cancel-{idx}{args} : {g.expr(e)} = {g.Z} := {pf}']
 per.append((patterns[e],keys))
for i,(idx,keys) in enumerate(per):
 L += ['',f'#define nima-relative-f-cell-square-{i} : nima-sum-equal NimaRelativeFBasis (nima-relative-f-d (nima-relative-f-column {state(i)})) (nima-sum-zero NimaRelativeFBasis)', '  := \\ probe -> '+app(f'nima-relative-f-cancel-{idx}',*[app('probe',state(j)) for j in keys])]
L += ['','#define nima-relative-f-column-square : (q : NimaRelativeFBasis) -> nima-sum-equal NimaRelativeFBasis (nima-relative-f-d (nima-relative-f-column q)) (nima-sum-zero NimaRelativeFBasis)','  := \\ q -> match q']
L += [('       (' if i==0 else '       | ')+state(i)+f' => nima-relative-f-cell-square-{i}' for i in range(12)]+['       )','#define nima-relative-f-square (p : NimaRelativeF) : nima-sum-equal NimaRelativeFBasis (nima-relative-f-d (nima-relative-f-d p)) (nima-sum-zero NimaRelativeFBasis)','  := nima-sum-column-square NimaRelativeFBasis nima-relative-f-column nima-relative-f-column-square p',
 '#define nima-relative-f-z : NimaRelativeF := nima-sum-add NimaRelativeFBasis (nima-sum-atom NimaRelativeFBasis nima-relative-f-state-5) (nima-sum-atom NimaRelativeFBasis nima-relative-f-state-7)',
 '#define nima-relative-f-conductor-probe : NimaRelativeFBasis -> MariciInt := \\ q -> match q (nima-relative-f-state-0 => marici-int-zero | nima-relative-f-state-1 => marici-int-zero | nima-relative-f-state-2 => marici-int-zero | nima-relative-f-state-3 => marici-int-zero | nima-relative-f-state-4 => marici-int-zero | nima-relative-f-state-5 => marici-int-zero | nima-relative-f-state-6 => marici-int-zero | nima-relative-f-state-7 => marici-int-zero | nima-relative-f-state-8 => marici-int-zero | nima-relative-f-state-9 => marici-int-zero | nima-relative-f-state-10 => marici-int-zero | nima-relative-f-state-11 => marici-int-one)',
 '#define nima-relative-f-conductor (p : NimaRelativeF) : MariciInt := nima-sum-eval NimaRelativeFBasis nima-relative-f-conductor-probe p',
 '#define nima-relative-f-z-boundary-conductor : nima-relative-f-conductor (nima-relative-f-d nima-relative-f-z) = marici-int-one := refl','```','']
out=ROOT/'research/nima/rzk/33-relative-physical-fibre.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'states':12,'arrows':sum(map(len,cols.values())),'cancellation_shapes':len(patterns),'requires_rzk_check':True};(ROOT/'research/nima/results/relative-fibre-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)

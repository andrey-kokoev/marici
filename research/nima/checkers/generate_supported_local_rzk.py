"""Generate the 16-state supported local (u,s,t) coefficient complex."""
from pathlib import Path
import importlib.util,sys,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
# Reuse only the proof-term normalizer. Importing the generator emits its bounded
# default checkpoint; callers regenerate the full loaded checkpoint separately.
saved=sys.argv;sys.argv=['build_loaded_polynomial_cech_rzk.py','--cell-limit','1']
p=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py'
spec=importlib.util.spec_from_file_location('loaded_builder_helpers',p);g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g);sys.argv=saved
Z=g.Z;app=g.app;add=g.add;neg=g.neg;tup=g.tup;tuple_type=g.tuple_type
# states 0..2 degree -2; 3..9 degree -1; 10..14 degree 0; 15 degree 1
cols={i:[] for i in range(16)}
def edge(i,j,var=None,sign=1): cols[i].append((j,var,sign))
# [ -M^T ; -u I3 ]
edge(0,4,'t');edge(0,5,'s',-1);edge(0,7,'u',-1)
edge(1,3,None,-1);edge(1,5,None);edge(1,8,'u',-1)
edge(2,4,None,-1);edge(2,6,None);edge(2,9,'u',-1)
# [w^T 0; uI4 -M^T]
for i,v in enumerate(('t','s','t','s'),3): edge(i,10,v)
for i in range(4): edge(3+i,11+i,'u')
edge(7,12,'t');edge(7,13,'s',-1)
edge(8,11,None,-1);edge(8,13,None)
edge(9,12,None,-1);edge(9,14,None)
# (-u,t,s,t,s)
edge(10,15,'u',-1);edge(11,15,'t');edge(12,15,'s');edge(13,15,'t');edge(14,15,'s')
state=lambda i:f'nima-local-state-{i}'
def shifted(v,var):
 u,s,t=v
 if var=='u':u=app('marici-succ',u)
 if var=='s':s=app('marici-succ',s)
 if var=='t':t=app('marici-succ',t)
 return (u,s,t)
def sparse(items,v):
 out=app('nima-sum-zero','NimaLocalBasis')
 for j,var,sgn in reversed(items):
  term=app('nima-sum-atom','NimaLocalBasis',tup([state(j),tup(shifted(v,var))]))
  if sgn<0:term=app('nima-sum-neg','NimaLocalBasis',term)
  out=app('nima-sum-add','NimaLocalBasis',term,out)
 return out
lines=['# Supported local coefficient complex','',
 'The three variables are u=u03, s=t04, and t=t35. Spectator coefficients',
 'act independently and are omitted from this minimal polynomial block.','',
 '```rzk','#lang rzk-1','#data NimaLocalState','  := '+state(0)]
lines += ['  | '+state(i) for i in range(1,16)]
lines += ['','#define NimaUSTMonomial : U := Sigma (_ : MariciNat), Sigma (_ : MariciNat), MariciNat',
 '#define NimaLocalBasis : U := Sigma (_ : NimaLocalState), NimaUSTMonomial',
 '#define NimaLocalCoefficients : U := NimaZSum NimaLocalBasis',
 '#define nima-local-column : NimaLocalBasis -> NimaLocalCoefficients',
 '  := \\ (q,m) -> (match q into (\\ _ -> NimaUSTMonomial -> NimaLocalCoefficients) (']
for i in range(16): lines += [('    ' if i==0 else '  | ')+state(i)+' => \\ (u,(s,t)) -> '+sparse(cols[i],('u','s','t'))]
lines += ['  )) m','#define nima-local-d : NimaLocalCoefficients -> NimaLocalCoefficients',
 '  := nima-sum-bind NimaLocalBasis NimaLocalBasis nima-local-column']
# square proofs
patterns={}; per=[]
for i in range(16):
 keys=[]
 def atom(j,v):
  key=(j,v)
  if key not in keys:keys.append(key)
  return ('a',keys.index(key))
 e=('z',)
 for j,var,sgn in reversed(cols[i]):
  v=shifted(('u','s','t'),var);inner=('z',)
  for k,var2,sgn2 in reversed(cols[j]):
   z=atom(k,shifted(v,var2))
   if sgn2<0:z=('n',z)
   inner=('+',z,inner)
  if sgn<0:inner=('n',inner)
  e=('+',inner,e)
 if e not in patterns:
  normal,pf=g.normalize(e)
  if normal:raise RuntimeError((i,normal))
  idx=len(patterns);patterns[e]=(idx,len(keys))
  args=' ('+tup([f'a{k}' for k in range(len(keys))])+' : '+tuple_type(['MariciInt']*len(keys))+')' if keys else ''
  lines += ['',f'#define nima-local-cancellation-{idx}{args}',f'  : {g.expr(e)} = {Z}',f'  := {pf}']
 per.append((patterns[e][0],keys))
for i,(idx,keys) in enumerate(per):
 vals=[app('probe',tup([state(j),tup(list(v))])) for j,v in keys]
 eq=f'nima-sum-equal NimaLocalBasis (nima-sum-bind NimaLocalBasis NimaLocalBasis nima-local-column (nima-local-column ({state(i)},m))) (nima-sum-zero NimaLocalBasis)'
 pf=app(f'nima-local-cancellation-{idx}',*([tup(vals)] if vals else []))
 lines += ['',f'#define nima-local-cell-square-{i} : (m : NimaUSTMonomial) -> {eq}',f'  := \\ (u,(s,t)) probe -> {pf}']
lines += ['', '#define nima-local-column-square : (v : NimaLocalBasis) ->',
 '  nima-sum-equal NimaLocalBasis (nima-sum-bind NimaLocalBasis NimaLocalBasis nima-local-column (nima-local-column v)) (nima-sum-zero NimaLocalBasis)',
 '  := \\ (q,m) -> (match q into (\\ k -> (m : NimaUSTMonomial) -> nima-sum-equal NimaLocalBasis',
 '       (nima-sum-bind NimaLocalBasis NimaLocalBasis nima-local-column (nima-local-column (k,m))) (nima-sum-zero NimaLocalBasis)) (']
lines += [('    ' if i==0 else '  | ')+state(i)+f' => nima-local-cell-square-{i}' for i in range(16)]
lines += ['  )) m', '#define nima-local-square (p : NimaLocalCoefficients)',
 '  : nima-sum-equal NimaLocalBasis (nima-local-d (nima-local-d p)) (nima-sum-zero NimaLocalBasis)',
 '  := nima-sum-column-square NimaLocalBasis nima-local-column nima-local-column-square p',
 '#define nima-local-alpha : NimaLocalCoefficients := nima-sum-neg NimaLocalBasis (nima-sum-atom NimaLocalBasis (nima-local-state-10,(marici-zero,(marici-zero,marici-zero))))',
 '#define nima-local-u-tau : NimaLocalCoefficients := nima-local-d nima-local-alpha',
 '#define nima-local-bockstein-chain : nima-local-d nima-local-alpha = nima-local-u-tau := refl','```','']
out=ROOT/'research/nima/rzk/26-supported-local-coefficient-complex.rzk.md';out.write_text('\n'.join(lines))
meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'states':16,'arrows':sum(map(len,cols.values())),'cancellation_shapes':len(patterns),'trusted_generator':False,'requires_rzk_check':True}
(ROOT/'research/nima/results/supported-local-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)

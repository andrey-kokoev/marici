"""Generate Q_cell tensor K_occ(X35) with the homological tensor sign."""
from pathlib import Path
import importlib.util,sys,subprocess,hashlib,json
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py'
saved=sys.argv;sys.argv=[str(src),'--cell-limit','1'];sp=importlib.util.spec_from_file_location('gqocc',src);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g);sys.argv=saved
app=g.app
# q=0 T,1 h03,2 h14,3 h25,4 p03,5 p14,6 p25; occ 0=p,1=h
S=lambda q,o:f'nima-q-occ-state-{q}-{o}'
cols={(q,o):[] for q in range(7) for o in range(2)}
def edge(src,tgt,var,sgn=1):cols[src].append((tgt,var,sgn))
qedges={0:[(4,'X03'),(5,'X14'),(6,'X25')],1:[(4,'u03')],2:[(5,'u14')],3:[(6,'u25')],4:[],5:[],6:[]}
for q in range(7):
 for o in range(2):
  for r,v in qedges[q]:edge((q,o),(r,o),v)
  if o==1:edge((q,o),(q,0),'X35',-1 if q<4 else 1)
def shift(v,var):
 names=['X03','X14','X25','u03','u14','u25','X35'];i=names.index(var);w=list(v);w[i]=app('marici-succ',w[i]);return tuple(w)
def tup(xs):
 o=xs[-1]
 for x in reversed(xs[:-1]):o=f'({x},{o})'
 return o
def mono(v):return f'({tup(list(v[:6]))},{v[6]})'
def sparse(es,v):
 out=app('nima-sum-zero','NimaQOccurrenceBasis')
 for (q,o),var,sgn in reversed(es):
  z=app('nima-sum-atom','NimaQOccurrenceBasis',f'({S(q,o)},{mono(shift(v,var))})');z=app('nima-sum-neg','NimaQOccurrenceBasis',z) if sgn<0 else z;out=app('nima-sum-add','NimaQOccurrenceBasis',z,out)
 return out
L=['# Fourteen-state occurrence-tensored Q complex','','```rzk','#lang rzk-1','#data NimaQOccurrenceState','  := '+S(0,0)]+['  | '+S(q,o) for q in range(7) for o in range(2) if (q,o)!=(0,0)]
L += ['','#define NimaQOccurrenceMonomial7 : U := Sigma (_ : NimaQLongMonomial6), MariciNat','#define NimaQOccurrenceBasis : U := Sigma (_ : NimaQOccurrenceState), NimaQOccurrenceMonomial7','#define NimaQOccurrence : U := NimaZSum NimaQOccurrenceBasis','#define nima-q-occ-column : NimaQOccurrenceBasis -> NimaQOccurrence','  := \\ (q,((X03,(X14,(X25,(u03,(u14,u25))))),x35)) -> match q into (\\ _ -> NimaQOccurrence) (']
v=('X03','X14','X25','u03','u14','u25','x35')
for n,(q,o) in enumerate(cols):L += [('    ' if n==0 else '  | ')+S(q,o)+' => '+sparse(cols[(q,o)],v)]
L += ['  )','#define nima-q-occ-d : NimaQOccurrence -> NimaQOccurrence := nima-sum-bind NimaQOccurrenceBasis NimaQOccurrenceBasis nima-q-occ-column']
patterns={};per=[]
for st in cols:
 keys=[];e=('z',)
 def atom(k,v):
  key=(k,v)
  if key not in keys:keys.append(key)
  return ('a',keys.index(key))
 for mid,var,s1 in reversed(cols[st]):
  vv=shift(v,var);inn=('z',)
  for end,var2,s2 in reversed(cols[mid]):
   z=atom(end,shift(vv,var2));z=('n',z) if s2<0 else z;inn=('+',z,inn)
  inn=('n',inn) if s1<0 else inn;e=('+',inn,e)
 if e not in patterns:
  normal,pf=g.normalize(e);assert not normal;idx=len(patterns);patterns[e]=idx
  args=(' ('+' '.join('a'+str(i) for i in range(len(keys)))+' : MariciInt)') if keys else ''
  L += ['',f'#define nima-q-occ-cancel-{idx}{args} : {g.expr(e)} = {g.Z} := {pf}']
 per.append((patterns[e],keys))
for st,(idx,keys) in zip(cols,per):
 vals=[app('probe',f'({S(k[0],k[1])},{mono(vv)})') for k,vv in keys]
 L += ['',f'#define nima-q-occ-cell-square-{st[0]}-{st[1]} : (m : NimaQOccurrenceMonomial7) -> nima-sum-equal NimaQOccurrenceBasis (nima-q-occ-d (nima-q-occ-column ({S(*st)},m))) (nima-sum-zero NimaQOccurrenceBasis)',f'  := \\ ((X03,(X14,(X25,(u03,(u14,u25))))),x35) probe -> '+app(f'nima-q-occ-cancel-{idx}',*vals)]
L += ['','#define nima-q-occ-column-square : (v : NimaQOccurrenceBasis) -> nima-sum-equal NimaQOccurrenceBasis (nima-q-occ-d (nima-q-occ-column v)) (nima-sum-zero NimaQOccurrenceBasis)','  := \\ (q,m) -> (match q into (\\ k -> (m0 : NimaQOccurrenceMonomial7) -> nima-sum-equal NimaQOccurrenceBasis (nima-q-occ-d (nima-q-occ-column (k,m0))) (nima-sum-zero NimaQOccurrenceBasis)) (']
for n,(q,o) in enumerate(cols):L += [('    ' if n==0 else '  | ')+S(q,o)+f' => nima-q-occ-cell-square-{q}-{o}']
L += ['  )) m','#define nima-q-occ-square (p : NimaQOccurrence) : nima-sum-equal NimaQOccurrenceBasis (nima-q-occ-d (nima-q-occ-d p)) (nima-sum-zero NimaQOccurrenceBasis) := nima-sum-column-square NimaQOccurrenceBasis nima-q-occ-column nima-q-occ-column-square p','```','']
out=ROOT/'research/nima/rzk/41-q-occurrence-tensor.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'states':14,'arrows':sum(map(len,cols.values())),'cancellation_shapes':len(patterns),'requires_rzk_check':True};(ROOT/'research/nima/results/q-occurrence-tensor-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)

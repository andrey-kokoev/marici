"""Generate typed finite/Cech coefficient presentations and kernel-checkable d² proofs.

The input checker is read-only. Python generates terms, not trusted assertions:
Rzk must check every emitted proof against the actual typed differential.
"""
from pathlib import Path
import argparse
import importlib.util
import hashlib
import json
import sys
sys.dont_write_bytecode = True
parser=argparse.ArgumentParser()
parser.add_argument('--cell-limit',type=int,default=1,help='Bounded square-proof prefix; full 215-state carriers are always generated')
args=parser.parse_args()
if not 1 <= args.cell_limit <= 215: raise SystemExit('cell-limit must be 1..215')
cell_limit=args.cell_limit
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/chatgpt/mixed-normal-chern-comparision/check_mixed_normal_chern_comparison.py'
spec = importlib.util.spec_from_file_location('nima_loaded_source', SOURCE)
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)

Z = 'marici-int-zero'
def app(f, *xs): return '(' + ' '.join((f, *xs)) + ')'
def add(a,b): return app('marici-int-add',a,b)
def neg(a): return app('marici-int-negate',a)
def path(a,b,c,p,q):
    if a == b and p == 'refl': return q
    if b == c and q == 'refl': return p
    return app('nima-frame-concat','MariciInt',a,b,c,p,q)
def rev(a,b,p): return app('nima-frame-rev','MariciInt',a,b,p)
def apadd(a,b,c,d,p,q):
    if a == b and c == d and p == q == 'refl': return 'refl'
    return app('nima-cochain-ap2','MariciInt','MariciInt','MariciInt','marici-int-add',a,b,c,d,p,q)
def apneg(a,b,p): return 'refl' if a == b and p == 'refl' else app('nima-frame-ap','MariciInt','MariciInt','marici-int-negate',a,b,p)
def literal(t):
    i, sign=t
    return 'a'+str(i) if sign == 1 else neg('a'+str(i))
def total(ts):
    out=Z
    for t in reversed(ts): out=add(literal(t),out)
    return out

def insert(a, ts):
    initial=add(literal(a),total(ts))
    if not ts or a[0] < ts[0][0] or a == ts[0]: return [a]+ts, 'refl'
    b, tail=ts[0],ts[1:]
    if a[0] == b[0]:
        law='nima-int-cancel-positive-prefix' if a[1] == 1 else 'nima-int-cancel-negative-prefix'
        return tail, app(law,'a'+str(a[0]),total(tail))
    new, proof=insert(a,tail)
    middle=add(literal(b),add(literal(a),total(tail)))
    final=add(literal(b),total(new))
    return [b]+new,path(initial,middle,final,
        app('nima-int-swap-prefix',literal(a),literal(b),total(tail)),
        apadd(literal(b),literal(b),add(literal(a),total(tail)),total(new),'refl',proof))

def merge(xs,ys):
    initial=add(total(xs),total(ys))
    if not xs: return ys,'refl'
    if not ys: return xs,app('marici-int-add-zero-right',total(xs))
    a,tail=xs[0],xs[1:]
    zs,p=merge(tail,ys)
    ws,q=insert(a,zs)
    m1=add(literal(a),add(total(tail),total(ys)))
    m2=add(literal(a),total(zs))
    return ws,path(initial,m1,total(ws),app('marici-int-add-assoc',literal(a),total(tail),total(ys)),
        path(m1,m2,total(ws),apadd(literal(a),literal(a),add(total(tail),total(ys)),total(zs),'refl',p),q))

def negate_list(xs):
    if not xs:return [],'refl'
    a,tail=xs[0],xs[1:]
    ys,p=negate_list(tail)
    b=(a[0],-a[1])
    q='refl' if a[1] == 1 else app('marici-int-negate-involutive','a'+str(a[0]))
    initial=neg(total(xs)); middle=add(neg(literal(a)),neg(total(tail)))
    return [b]+ys,path(initial,middle,total([b]+ys),app('marici-int-negate-add',literal(a),total(tail)),
        apadd(neg(literal(a)),literal(b),neg(total(tail)),total(ys),q,p))

def expr(e):
    if e[0]=='z':return Z
    if e[0]=='a':return 'a'+str(e[1])
    if e[0]=='n':return neg(expr(e[1]))
    return add(expr(e[1]),expr(e[2]))

def normalize(e):
    if e[0]=='z':return [],'refl'
    if e[0]=='a':
        a='a'+str(e[1]);return [(e[1],1)],rev(add(a,Z),a,app('marici-int-add-zero-right',a))
    if e[0]=='n':
        xs,p=normalize(e[1]);ys,q=negate_list(xs)
        return ys,path(expr(e),neg(total(xs)),total(ys),apneg(expr(e[1]),total(xs),p),q)
    xs,p=normalize(e[1]);ys,q=normalize(e[2]);zs,r=merge(xs,ys)
    return zs,path(expr(e),add(total(xs),total(ys)),total(zs),
        apadd(expr(e[1]),total(xs),expr(e[2]),total(ys),p,q),r)

def tup(xs):
    if len(xs)==1:return xs[0]
    return '('+xs[0]+','+tup(xs[1:])+')'
def tuple_type(types):
    out=types[-1]
    for ty in reversed(types[:-1]):out='Sigma (_ : '+ty+'), '+out
    return out
V=['x'+str(i) for i in range(9)]+['u'+str(i) for i in range(9)]
POLY='NimaPolynomialMonomial'
def cell(i):return 'nima-loaded-cell-'+str(i)
def basis(mode):return 'Nima'+mode+'LoadedBasis'
def mono(mode,i):return POLY if mode=='Finite' else app('NimaCechMonomial',cell(i))
def types(mode,i):
    f,h=s.CELLS[i]
    return ['MariciNat']*9 + ['MariciInt' if mode=='Cech' and d in f-h else 'MariciNat' for d in s.D]
def transition(mode, i, edge, values):
    j,d,kind,sign=edge
    out=list(values);k=s.DI[d]
    if kind=='radial':out[k]=app('marici-succ',out[k])
    if mode=='Finite':
        if kind=='normal':out[9+k]=app('marici-succ',out[9+k])
    else:
        # A radial arrow introduces a newly invertible coordinate.  Use the
        # canonical predecessor presentation directly; this is propositionally
        # equal to embed(n)-1 but makes the Lambda square definitionally visible.
        out[9+k]=app('nima-laurent-predecessor',out[9+k]) if kind=='radial' else app('marici-int-embed-nat',out[9+k])
    return j,out,sign

def summands(mode,i,values):
    return [transition(mode,i,e,values) for e in s.ADJ[i]]
def sparse_sum(mode,items):
    out=app('nima-sum-zero',basis(mode))
    for j,values,sign in reversed(items):
        term=app('nima-sum-atom',basis(mode),tup([cell(j),tup(values)]))
        if sign==-1:term=app('nima-sum-neg',basis(mode),term)
        out=app('nima-sum-add',basis(mode),term,out)
    return out

def square_sparse(mode,i):
    out=app('nima-sum-zero',basis(mode))
    for j,vs,sign in reversed(summands(mode,i,V)):
        inner=sparse_sum(mode,summands(mode,j,vs))
        if sign==-1:inner=app('nima-sum-neg',basis(mode),inner)
        out=app('nima-sum-add',basis(mode),inner,out)
    return out

def square_expr(mode,i):
    keys=[]
    def atom(j,vs):
        key=(j,tuple(vs))
        if key not in keys:keys.append(key)
        return ('a',keys.index(key))
    out=('z',)
    for j,vs,sgn in reversed(summands(mode,i,V)):
        inner=('z',)
        for k,ws,tgn in reversed(summands(mode,j,vs)):
            t=atom(k,ws)
            if tgn==-1:t=('n',t)
            inner=('+',t,inner)
        if sgn==-1:inner=('n',inner)
        out=('+',inner,out)
    return out,keys

lines=['# Loaded polynomial and legal Cech coefficient presentations','',
    'Generated by `research/nima/checkers/build_loaded_polynomial_cech_rzk.py`.',
    'All 215 cells and 522 signed arrows are retained. Each monomial has nine',
    'natural occurrence exponents; normal exponents are natural unless the',
    'specific target stalk permits inversion, when they are canonical integers.',
    'Coefficients are finite integral sums with the explicit equality of module 18.',
    'This is a setoid presentation, not a claimed quotient/identity-type bridge.','',
    '```rzk','#lang rzk-1','#data NimaLoadedCell','  := '+cell(0)]
lines += ['  | '+cell(i) for i in range(1,len(s.CELLS))]
lines += ['','#define '+POLY+' : U := '+tuple_type(['MariciNat']*18),
    '#define nima-laurent-predecessor (n : MariciNat) : MariciInt',
    '  := match n (marici-zero => marici-int-minus-one | marici-succ k ih => marici-int-embed-nat k)',
    '#define NimaCechMonomial (c : NimaLoadedCell) : U','  := match c (']
lines += [('    ' if i==0 else '  | ')+cell(i)+' => '+tuple_type(types('Cech',i)) for i in range(len(s.CELLS))]
lines += ['  )', '#define NimaFiniteLoadedBasis : U := Sigma (_ : NimaLoadedCell), NimaPolynomialMonomial',
    '#define NimaCechLoadedBasis : U := Sigma (c : NimaLoadedCell), NimaCechMonomial c',
    '#define NimaFiniteLoadedCoefficients : U := NimaZSum NimaFiniteLoadedBasis',
    '#define NimaCechLoadedCoefficients : U := NimaZSum NimaCechLoadedBasis',
    '#define NimaPolynomialCoefficients : U := NimaZSum NimaPolynomialMonomial']

for mode in ('Finite','Cech'):
    name='nima-'+mode.lower()+'-loaded-column'
    lines += ['',f'#define {name} : {basis(mode)} -> NimaZSum {basis(mode)}',
        '  := \\ (c,m) -> (match c into (\\ k -> '+(POLY if mode=='Finite' else 'NimaCechMonomial k')+' -> NimaZSum '+basis(mode)+') (']
    lines += [('    ' if i==0 else '  | ')+cell(i)+' => \\ '+tup(V)+' -> '+sparse_sum(mode,summands(mode,i,V)) for i in range(len(s.CELLS))]
    lines += ['  )) m',f'#define nima-{mode.lower()}-loaded-d : NimaZSum {basis(mode)} -> NimaZSum {basis(mode)}',
        f'  := nima-sum-bind {basis(mode)} {basis(mode)} {name}']

# Cochain grading and the actual diagonal finite-to-Cech coefficient map.
lines += ['', '#define nima-loaded-cochain-degree (c : NimaLoadedCell) : MariciInt', '  := match c (']
for i in range(len(s.CELLS)):
    n=s.degree(i)
    value=Z if n==0 else app('marici-int-neg', 'marici-zero' if n==1 else app('marici-succ','marici-zero') if n==2 else app('marici-succ',app('marici-succ','marici-zero')))
    lines += [('    ' if i==0 else '  | ')+cell(i)+' => '+value]
lines += ['  )', '#define NimaFiniteCoefficientDegree (k : MariciInt) : U',
    '  := NimaZSum (Sigma (a : NimaFiniteLoadedBasis), nima-loaded-cochain-degree (first a) = k)',
    '#define NimaCechCoefficientDegree (k : MariciInt) : U',
    '  := NimaZSum (Sigma (a : NimaCechLoadedBasis), nima-loaded-cochain-degree (first a) = k)',
    '#define nima-finite-cech-monomial : NimaFiniteLoadedBasis -> NimaCechLoadedBasis',
    '  := \\ (c,m) -> (match c into (\\ _ -> NimaPolynomialMonomial -> NimaCechLoadedBasis) (']
for i in range(len(s.CELLS)):
    f,h=s.CELLS[i]
    vs=V[:9]+[app('nima-laurent-predecessor',V[9+j]) if d in f-h else V[9+j] for j,d in enumerate(s.D)]
    lines += [('    ' if i==0 else '  | ')+cell(i)+' => \\ '+tup(V)+' -> '+tup([cell(i),tup(vs)])]
lines += ['  )) m', '#define nima-finite-cech-comparison : NimaFiniteLoadedCoefficients -> NimaCechLoadedCoefficients',
    '  := nima-sum-map NimaFiniteLoadedBasis NimaCechLoadedBasis nima-finite-cech-monomial']

# Scalar monomial action: natural scalar powers can act at every legal stalk.
for mode in ('Finite','Cech'):
    name='nima-'+mode.lower()+'-monomial-action'
    a=['a'+str(i) for i in range(18)]
    lines += ['',f'#define {name} : {POLY} -> {basis(mode)} -> {basis(mode)}',
        '  := \\ '+tup(a)+' (c,m) -> (match c into (\\ k -> '+(POLY if mode=='Finite' else 'NimaCechMonomial k')+' -> '+basis(mode)+') (']
    for i in range(len(s.CELLS)):
        out=[app('marici-int-add',app('marici-int-embed-nat',av),v) if ty=='MariciInt' else app('marici-add',av,v)
             for av,v,ty in zip(a,V,types(mode,i))]
        lines += [('    ' if i==0 else '  | ')+cell(i)+' => \\ '+tup(V)+' -> '+tup([cell(i),tup(out)])]
    lines += ['  )) m',f'#define nima-{mode.lower()}-polynomial-action (p : NimaPolynomialCoefficients) (v : NimaZSum {basis(mode)}) : NimaZSum {basis(mode)}',
        f'  := nima-sum-bind {POLY} {basis(mode)} (\\ a -> nima-sum-map {basis(mode)} {basis(mode)} ({name} a) v) p']

carrier_lines=lines+['```','','These are full 215-state coefficient presentations and typed operations.',
    'Square-zero proofs are generated separately in module 20; their verification',
    'status must be consulted. The complete R0-module axiom package and the',
    'identity-type/quotient realization are not supplied by these carrier types.','']
lines=['# Loaded coefficient square-zero proof checkpoint','',
    f'Generated cell prefix: {cell_limit} of 215 in each model. This is not a full proof when the prefix is shorter.',
    '', '```rzk','#lang rzk-1']
# Deduplicate integer cancellation shapes; no matrix result is assumed in Rzk.
patterns={}; per_mode={}
for mode in ('Finite','Cech'):
    per_mode[mode]=[]
    for i in range(cell_limit):
        e,keys=square_expr(mode,i)
        if e not in patterns:
            normal,proof=normalize(e)
            if normal:raise RuntimeError(f'Nonzero column square at {mode} {i}: {normal}')
            idx=len(patterns);patterns[e]=(idx,len(keys))
            args=' ('+tup(['a'+str(k) for k in range(len(keys))])+' : '+tuple_type(['MariciInt']*len(keys))+')' if keys else ''
            lines += ['',f'#define nima-loaded-cancellation-{idx}{args}',f'  : {expr(e)} = {Z}',f'  := {proof}']
        per_mode[mode].append((patterns[e][0],keys))
for mode in ('Finite','Cech'):
    b=basis(mode);col='nima-'+mode.lower()+'-loaded-column'
    sq='nima-'+mode.lower()+'-loaded-column-square'
    eq=lambda c,m: f'nima-sum-equal {b} (nima-sum-bind {b} {b} {col} ({col} ({c},{m}))) (nima-sum-zero {b})'
    for i,(idx,keys) in enumerate(per_mode[mode]):
        args=[app('probe',tup([cell(j),tup(list(vs))])) for j,vs in keys]
        # Keep the proof at the evaluation boundary.  Reducing bind twice already
        # exposes exactly the signed incidence expression; an intermediate path
        # between two four-megabyte syntax trees made Rzk normalize that tree
        # repeatedly and caused the old monolithic checkpoint to time out.
        proof=app('nima-loaded-cancellation-'+str(idx),*([tup(args)] if args else []))
        lines += ['',f'#define nima-{mode.lower()}-loaded-cell-square-{i} : (v : {mono(mode,i)}) -> '+eq(cell(i),'v'),
            '  := \\ '+tup(V)+' probe -> '+proof]
    if cell_limit != len(s.CELLS): continue
    lines += ['',f'#define {sq} : (v : {b}) -> nima-sum-equal {b} (nima-sum-bind {b} {b} {col} ({col} v)) (nima-sum-zero {b})',
        '  := \\ (c,m) -> (match c into (\\ k -> (v : '+(POLY if mode=='Finite' else 'NimaCechMonomial k')+') -> '+eq('k','v')+') (']
    for i,(idx,keys) in enumerate(per_mode[mode]):
        lines += [('    ' if i==0 else '  | ')+cell(i)+f' => nima-{mode.lower()}-loaded-cell-square-{i}']
    lines += ['  )) m',f'#define nima-{mode.lower()}-loaded-square (v : NimaZSum {b})',
        f'  : nima-sum-equal {b} (nima-{mode.lower()}-loaded-d (nima-{mode.lower()}-loaded-d v)) (nima-sum-zero {b})',
        f'  := nima-sum-column-square {b} {col} {sq} v']
lines += ['```','',
    'When all 215 rows are included, the assembled square-zero theorems quantify over every finite coefficient expression,',
    'including arbitrary signed integer coefficients and every legal Laurent',
    'monomial. The exponent types forbid inverses on disallowed stalks.',
    'Scalar-action operations are defined, but the complete R0-module axiom',
    'package and its identity-type realization remain explicit obligations.','']
out=ROOT/'research/nima/rzk/19-loaded-polynomial-cech-modules.rzk.md'
out.write_text('\n'.join(carrier_lines))
proofout=ROOT/'research/nima/rzk/20-loaded-coefficient-square.rzk.md'
proofout.write_text('\n'.join(lines))

# The finite-to-Cech comparison is checked generatorwise against the actual
# two loaded columns.  Keep this separate from square-zero so either large
# certificate can be checked headlessly without loading the other.
lam=['# Loaded finite-to-Cech chain comparison','',
    'All 215 generator squares are present.  The final theorem extends them to',
    'every finite integral coefficient expression by structural recursion.','',
    '```rzk','#lang rzk-1',
    '#define nima-loaded-lambda-column-square : (v : NimaFiniteLoadedBasis) ->',
    '  nima-sum-equal NimaCechLoadedBasis',
    '    (nima-finite-cech-comparison (nima-finite-loaded-column v))',
    '    (nima-cech-loaded-column (nima-finite-cech-monomial v))',
    '  := \\ (c,m) -> (match c into (\\ k -> (v : NimaPolynomialMonomial) ->',
    '       nima-sum-equal NimaCechLoadedBasis',
    '         (nima-finite-cech-comparison (nima-finite-loaded-column (k,v)))',
    '         (nima-cech-loaded-column (nima-finite-cech-monomial (k,v)))) (']
for i in range(len(s.CELLS)):
    lam += [('    ' if i==0 else '  | ')+cell(i)+' => \\ '+tup(V)+' probe -> refl']
lam += ['  )) m','',
    '#define nima-loaded-lambda-chain (p : NimaFiniteLoadedCoefficients)',
    '  : nima-sum-equal NimaCechLoadedBasis',
    '      (nima-finite-cech-comparison (nima-finite-loaded-d p))',
    '      (nima-cech-loaded-d (nima-finite-cech-comparison p))',
    '  := match p',
    '       (nima-sum-zero => \\ probe -> refl',
    '       | nima-sum-atom a => nima-loaded-lambda-column-square a',
    '       | nima-sum-add x ihx y ihy => \\ probe -> nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x)))',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d y)))',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison y))) (ihx probe) (ihy probe)',
    '       | nima-sum-neg x ih => \\ probe -> nima-frame-ap MariciInt MariciInt marici-int-negate',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x))) (ih probe)',
    '       | nima-sum-scale c x ih => \\ probe -> nima-frame-ap MariciInt MariciInt (marici-int-mul c)',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))',
    '           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x))) (ih probe))',
    '```','']
lamout=ROOT/'research/nima/rzk/21-loaded-finite-cech-chain.rzk.md'
lamout.write_text('\n'.join(lam))

# Concrete endpoint quotient: use the 199 nonendpoint cells as a fresh datatype,
# rather than pretending that setoid equality is an identity quotient.
kept=[i for i in range(len(s.CELLS)) if i not in s.VERTICES]
rindex={i:k for k,i in enumerate(kept)}
def rcell(k): return 'nima-relative-cell-'+str(k)
def rbasis(): return 'NimaRelativeCechBasis'
def rsummands(i,values):
    return [(rindex[j],vs,sgn) for j,vs,sgn in summands('Cech',i,values) if j in rindex]
def rsparse(items):
    out=app('nima-sum-zero',rbasis())
    for j,values,sign in reversed(items):
        term=app('nima-sum-atom',rbasis(),tup([rcell(j),tup(values)]))
        if sign==-1: term=app('nima-sum-neg',rbasis(),term)
        out=app('nima-sum-add',rbasis(),term,out)
    return out
rel=['# Concrete endpoint-relative Cech coefficient complex','',
    'The sixteen complete endpoint-packet cells are absent from this datatype.',
    'All remaining 199 cells retain their exact legal Laurent stalk types.','',
    '```rzk','#lang rzk-1','#data NimaRelativeCell','  := '+rcell(0)]
rel += ['  | '+rcell(k) for k in range(1,len(kept))]
rel += ['', '#define nima-relative-loaded-cell (c : NimaRelativeCell) : NimaLoadedCell','  := match c (']
rel += [('    ' if k==0 else '  | ')+rcell(k)+' => '+cell(i) for k,i in enumerate(kept)]
rel += ['  )','#define NimaRelativeCechBasis : U := Sigma (c : NimaRelativeCell), NimaCechMonomial (nima-relative-loaded-cell c)',
    '#define NimaRelativeCechCoefficients : U := NimaZSum NimaRelativeCechBasis',
    '#define nima-relative-cech-column : NimaRelativeCechBasis -> NimaZSum NimaRelativeCechBasis',
    '  := \\ (c,m) -> (match c into (\\ k -> NimaCechMonomial (nima-relative-loaded-cell k) -> NimaZSum NimaRelativeCechBasis) (']
for k,i in enumerate(kept):
    rel += [('    ' if k==0 else '  | ')+rcell(k)+' => \\ '+tup(V)+' -> '+rsparse(rsummands(i,V))]
rel += ['  )) m','#define nima-relative-cech-d : NimaRelativeCechCoefficients -> NimaRelativeCechCoefficients',
    '  := nima-sum-bind NimaRelativeCechBasis NimaRelativeCechBasis nima-relative-cech-column','```','']
relout=ROOT/'research/nima/rzk/22-endpoint-relative-cech-complex.rzk.md'; relout.write_text('\n'.join(rel))

# Endpoint-relative square-zero certificate, generated independently from the
# filtered 199-column differential.
rproof=['# Endpoint-relative Cech square-zero certificate','',
    'All 199 generator columns and the arbitrary finite-sum theorem are checked.','',
    '```rzk','#lang rzk-1']
rpatterns={}; rper=[]
for k,i in enumerate(kept):
    keys=[]
    def ratom(j,vs):
        key=(j,tuple(vs))
        if key not in keys: keys.append(key)
        return ('a',keys.index(key))
    e=('z',)
    for j,vs,sgn in reversed(rsummands(i,V)):
        inner=('z',)
        gj=kept[j]
        for q,ws,tgn in reversed(rsummands(gj,vs)):
            z=ratom(q,ws)
            if tgn==-1:z=('n',z)
            inner=('+',z,inner)
        if sgn==-1:inner=('n',inner)
        e=('+',inner,e)
    if e not in rpatterns:
        normal,pf=normalize(e)
        if normal: raise RuntimeError(f'Nonzero relative square at {i}: {normal}')
        idx=len(rpatterns);rpatterns[e]=(idx,len(keys))
        aa=' ('+tup(['a'+str(n) for n in range(len(keys))])+' : '+tuple_type(['MariciInt']*len(keys))+')' if keys else ''
        rproof += ['',f'#define nima-relative-cancellation-{idx}{aa}',f'  : {expr(e)} = {Z}',f'  := {pf}']
    rper.append((rpatterns[e][0],keys,i))
for k,(idx,keys,i) in enumerate(rper):
    vals=[app('probe',tup([rcell(j),tup(list(vs))])) for j,vs in keys]
    eqr=f'nima-sum-equal NimaRelativeCechBasis (nima-sum-bind NimaRelativeCechBasis NimaRelativeCechBasis nima-relative-cech-column (nima-relative-cech-column ({rcell(k)},v))) (nima-sum-zero NimaRelativeCechBasis)'
    pf=app('nima-relative-cancellation-'+str(idx),*([tup(vals)] if vals else []))
    rproof += ['',f'#define nima-relative-cell-square-{k} : (v : NimaCechMonomial {cell(i)}) -> {eqr}',
        '  := \\ '+tup(V)+' probe -> '+pf]
rproof += ['', '#define nima-relative-column-square : (v : NimaRelativeCechBasis) ->',
    '  nima-sum-equal NimaRelativeCechBasis',
    '      (nima-sum-bind NimaRelativeCechBasis NimaRelativeCechBasis nima-relative-cech-column (nima-relative-cech-column v))',
    '      (nima-sum-zero NimaRelativeCechBasis)',
    '  := \\ (c,m) -> (match c into (\\ k -> (v : NimaCechMonomial (nima-relative-loaded-cell k)) ->',
    '       nima-sum-equal NimaRelativeCechBasis',
    '         (nima-sum-bind NimaRelativeCechBasis NimaRelativeCechBasis nima-relative-cech-column (nima-relative-cech-column (k,v)))',
    '         (nima-sum-zero NimaRelativeCechBasis)) (']
rproof += [('    ' if k==0 else '  | ')+rcell(k)+f' => nima-relative-cell-square-{k}' for k in range(len(kept))]
rproof += ['  )) m', '#define nima-relative-cech-square (p : NimaRelativeCechCoefficients)',
    '  : nima-sum-equal NimaRelativeCechBasis (nima-relative-cech-d (nima-relative-cech-d p)) (nima-sum-zero NimaRelativeCechBasis)',
    '  := nima-sum-column-square NimaRelativeCechBasis nima-relative-cech-column nima-relative-column-square p','```','']
rproofout=ROOT/'research/nima/rzk/23-endpoint-relative-cech-square.rzk.md';rproofout.write_text('\n'.join(rproof))

# Explicit quotient projection and its chain law. Endpoint atoms go to zero;
# retained atoms keep the same dependent Laurent monomial.
quot=['# Endpoint quotient projection','',
    'This is the concrete setoid quotient map from 215 loaded Cech cells to the',
    '199-cell endpoint-relative complex.  It does not postulate a quotient HIT.','',
    '```rzk','#lang rzk-1',
    '#define nima-cech-relative-basis-column : NimaCechLoadedBasis -> NimaZSum NimaRelativeCechBasis',
    '  := \\ (c,m) -> (match c into (\\ k -> NimaCechMonomial k -> NimaZSum NimaRelativeCechBasis) (']
for i in range(len(s.CELLS)):
    if i in rindex: body=app('nima-sum-atom',rbasis(),tup([rcell(rindex[i]),'m']))
    else: body=app('nima-sum-zero',rbasis())
    quot += [('    ' if i==0 else '  | ')+cell(i)+' => \\ m -> '+body]
quot += ['  )) m',
    '#define nima-cech-relative-projection : NimaCechLoadedCoefficients -> NimaRelativeCechCoefficients',
    '  := nima-sum-bind NimaCechLoadedBasis NimaRelativeCechBasis nima-cech-relative-basis-column',
    '#define nima-cech-relative-column-chain : (v : NimaCechLoadedBasis) ->',
    '  nima-sum-equal NimaRelativeCechBasis',
    '    (nima-cech-relative-projection (nima-cech-loaded-column v))',
    '    (nima-relative-cech-d (nima-cech-relative-basis-column v))',
    '  := \\ (c,m) -> (match c into (\\ k -> (v : NimaCechMonomial k) ->',
    '       nima-sum-equal NimaRelativeCechBasis',
    '         (nima-cech-relative-projection (nima-cech-loaded-column (k,v)))',
    '         (nima-relative-cech-d (nima-cech-relative-basis-column (k,v)))) (']
quot += [('    ' if i==0 else '  | ')+cell(i)+' => \\ '+tup(V)+' probe -> refl' for i in range(len(s.CELLS))]
quot += ['  )) m',
    '#define nima-cech-relative-projection-chain (p : NimaCechLoadedCoefficients)',
    '  : nima-sum-equal NimaRelativeCechBasis',
    '      (nima-cech-relative-projection (nima-cech-loaded-d p))',
    '      (nima-relative-cech-d (nima-cech-relative-projection p))',
    '  := match p',
    '       (nima-sum-zero => \\ probe -> refl',
    '       | nima-sum-atom a => nima-cech-relative-column-chain a',
    '       | nima-sum-add x ihx y ihy => \\ probe -> nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-cech-relative-projection (nima-cech-loaded-d x)))',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-relative-cech-d (nima-cech-relative-projection x)))',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-cech-relative-projection (nima-cech-loaded-d y)))',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-relative-cech-d (nima-cech-relative-projection y))) (ihx probe) (ihy probe)',
    '       | nima-sum-neg x ih => \\ probe -> nima-frame-ap MariciInt MariciInt marici-int-negate',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-cech-relative-projection (nima-cech-loaded-d x)))',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-relative-cech-d (nima-cech-relative-projection x))) (ih probe)',
    '       | nima-sum-scale c x ih => \\ probe -> nima-frame-ap MariciInt MariciInt (marici-int-mul c)',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-cech-relative-projection (nima-cech-loaded-d x)))',
    '           (nima-sum-eval NimaRelativeCechBasis probe (nima-relative-cech-d (nima-cech-relative-projection x))) (ih probe))',
    '```','']
quotout=ROOT/'research/nima/rzk/24-endpoint-quotient-projection.rzk.md';quotout.write_text('\n'.join(quot))
metadata={'source':SOURCE.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'output':out.relative_to(ROOT).as_posix(),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'cells':len(s.CELLS),'arrows':sum(map(len,s.ADJ.values())),'cancellation_shapes':len(patterns),'bytes':out.stat().st_size,
    'proof_output':proofout.relative_to(ROOT).as_posix(),'proof_sha256':hashlib.sha256(proofout.read_bytes()).hexdigest(),
    'square_cells_per_model':cell_limit,'proof_bytes':proofout.stat().st_size,
    'lambda_output':lamout.relative_to(ROOT).as_posix(),'lambda_sha256':hashlib.sha256(lamout.read_bytes()).hexdigest(),
    'relative_output':relout.relative_to(ROOT).as_posix(),'relative_sha256':hashlib.sha256(relout.read_bytes()).hexdigest(),
    'relative_cells':len(kept),'relative_square_output':rproofout.relative_to(ROOT).as_posix(),
    'relative_square_sha256':hashlib.sha256(rproofout.read_bytes()).hexdigest(),
    'quotient_output':quotout.relative_to(ROOT).as_posix(),'quotient_sha256':hashlib.sha256(quotout.read_bytes()).hexdigest(),
    'cell_table':[s.encode_cell(i) for i in range(len(s.CELLS))],
    'trusted_generator':False,'requires_rzk_check':True}
(ROOT/'research/nima/results/loaded-polynomial-cech-generation.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps({k:metadata[k] for k in ('cells','arrows','cancellation_shapes','bytes')}))

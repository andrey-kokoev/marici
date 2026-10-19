# /// script
# dependencies = ["sympy"]
# ///
"""Bounded finite-packet access and lineage-preserving channel updates."""
import importlib.util
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/retained-history-source-access.v1.json'
NOTE='research/voevodsky/retained-history-source-access-v1.md'
OUT='research/voevodsky/results/retained-history-source-access-v1.json'
# Reuse the independently replayed exact bilinear Gaussian transpose rules.
spec=importlib.util.spec_from_file_location('observer',ROOT/'research/voevodsky/checkers/check_context_indexed_observer.py')
observer=importlib.util.module_from_spec(spec);spec.loader.exec_module(observer)

def require(ok,msg):
    if not ok: raise ValueError(msg)
def equal(a,b): return S.simplify(a-b)==0

def state():
    # Pentagon: five diagonal coordinates; a triangulation has two entries.
    # The axis seed is an explicitly added lattice packet, not a triangulation.
    return dict(h=S.Rational(1,3),j=0,D=5,history=[],mode='packet',
                seeds={'tri0':(1,1,0,0,0),'axis0':(1,0,0,0,0)},
                terms=[((1,1,0,0,0),S.Integer(2),'tri0',()),
                       ((1,0,0,0,0),S.Integer(3),'axis0',())])
def update(s,op,param):
    require(s['mode']=='packet','materialized updates require packet representation')
    h=s['h'];j=s['j']; out=[]; serial=len(s['history'])
    if op=='shift': require(isinstance(param,int),'axis shift must be integral')
    if op=='heat': require(param>=0,'negative heat')
    if op=='conv': require(all(isinstance(k,int) for k,w in param),'finite axis kernel required')
    if op=='perm': require(sorted(param)==list(range(s['D'])),'invalid permutation')
    for n,w,seed,line in s['terms']:
        variants=[(n,w)]
        if op=='shift':
            m=list(n);m[j]+=param;variants=[(tuple(m),w)]
        elif op=='heat': variants=[(n,w*S.exp(-S.pi*param*h*h*sum(x*x for x in n)))]
        elif op=='mod':
            require(len(param)==s['D'],'character dimension')
            variants=[(n,w*S.exp(2*S.pi*S.I*sum(a*b for a,b in zip(n,param))))]
        elif op=='bond': variants=[(tuple(2*x for x in n),w)]
        elif op=='perm':
            m=[0]*s['D']
            for i,v in enumerate(n): m[param[i]]=v
            variants=[(tuple(m),w)]
        elif op=='conv':
            variants=[]
            for k,v in param:
                m=list(n);m[j]+=k;variants.append((tuple(m),w*v))
        else: raise ValueError('unsupported packet operation')
        for branch,(m,v) in enumerate(variants):out.append((m,S.simplify(v),seed,line+((serial,op,branch),)))
    return dict(s,terms=out,h=h/2 if op=='bond' else h,
                j=param[j] if op=='perm' else j,history=s['history']+[(op,param)])
def partition(s):
    axis=[];off=[]
    for term in s['terms']:
        (axis if all(v==0 for i,v in enumerate(term[0]) if i!=s['j']) else off).append(term)
    return axis,off
# Tensor Gaussian query; tests have one (A,B,L,c) tuple per coordinate.
def query(s,tests):
    require(len(tests)==s['D'],'query dimension')
    require(all(A>0 for A,B,L,c in tests),'positive Gaussian widths required')
    value=0
    for n,w,seed,line in s['terms']:
        v=w
        for k,(A,B,L,c) in zip(n,tests):
            x=s['h']*k;v*=c*S.exp(S.pi*(L-A*x*x+2*B*x))
        value+=v
    return S.simplify(value)
def transported_query(s,tests,word):
    # History operations ('F','H','T','M',coordinate) use fixed exact parameters
    # from the observer checker. Stored snapshot stays fully accessible.
    pulled=list(tests)
    for op,i in reversed(word):
        require(0<=i<s['D'],'history coordinate')
        pulled[i]=observer.step(pulled[i],op,True)
    return query(s,pulled)

def main():
    contract=json.loads((ROOT/DEF).read_text());require(not contract['common_source_node_closed'],'scope promotion')
    s=state();original=dict(s['seeds']);g=[(S.Integer(1),S.Integer(0),S.Integer(0),S.Integer(1))]*5
    checks=[]
    def check(name,ok):require(ok,name);checks.append(name)
    a,o=partition(s);check('pentagon geometry retained off-axis',len(o)==1 and o[0][2]=='tri0' and len(a)==1)
    cur=s
    for op,p in [('shift',2),('mod',(S.Rational(1,3),0,0,0,0)),('heat',S.Rational(1,2)),('conv',[(1,S.Integer(2)),(-1,S.Integer(1))]),('bond',None),('perm',[1,0,2,3,4])]:
        cur=update(cur,op,p);a,o=partition(cur)
        check(op+'/archive',cur['seeds']==original and len(a)+len(o)==len(cur['terms']) and all(len(t[3])==len(cur['history']) for t in cur['terms']))
    bonded=update(s,'bond',None)
    check('bond physical query',equal(query(s,g),query(bonded,g)))
    heat=update(s,'heat',S.Rational(1,2));pulled=[observer.step(t,'H',True) for t in g]
    check('full heat source/query square',equal(query(heat,g),query(s,pulled)))
    shifted=update(s,'shift',2);pulled=list(g)
    # Physical shift is integer axis shift times the mesh, here 2/3.
    pulled[0]=observer.step(g[0],'T',True)
    check('shift source/query square',equal(query(shifted,g),query(s,pulled)))
    perm=[1,0,2,3,4];rel=update(s,'perm',perm);q=list(g);q[0]=(S.Integer(2),S.Rational(1,3),S.Integer(0),S.Integer(1))
    transported=[None]*5
    for i in range(5): transported[perm[i]]=q[i]
    check('relabel query and mark',rel['j']==1 and equal(query(s,q),query(rel,transported)))
    conv=update(s,'conv',[(1,S.Integer(2)),(-1,S.Integer(1))]);value=0
    for k,w in [(1,S.Integer(2)),(-1,S.Integer(1))]:
        q=list(g);A,B,L,c=q[0];b=-s['h']*k
        q[0]=(A,B+A*b,S.simplify(L-A*b*b-2*B*b),c)
        value+=w*query(s,q)
    check('convolution branched query',equal(query(conv,g),value))
    # Full Fourier followed by full heat; direct Fourier atom Gaussian integral.
    word=[('F',i) for i in range(5)]+[('H',i) for i in range(5)]
    direct=sum(w*S.prod(S.exp(-S.pi*(s['h']*k)**2/S.Rational(3,2))/S.sqrt(S.Rational(3,2)) for k in n) for n,w,seed,line in s['terms'])
    check('full Fourier then heat history',equal(transported_query(s,g,word),direct))
    bad=dict(s,mode='history')
    try:update(bad,'heat',S.Integer(1))
    except ValueError:checks.append('history packet-update rejected')
    else:raise AssertionError('history silently materialized')
    for op,param in [('heat',-1),('off-axis-shift',1)]:
        try:update(s,op,param)
        except ValueError:checks.append(op+'/unsupported rejected')
        else:raise AssertionError(op)
    paths=[DEF,NOTE,'research/voevodsky/checkers/check_context_indexed_observer.py',
           'research/conjecture_net/contracts/marked-channel-selection.v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.retained-history-source-access-validation.v1',passed=True,checks=checks,
                query_access='finite packet evaluation of explicitly transported tensor Gaussian tests and their finite linear combinations',
                geometry='immutable seed provenance; current terms not asserted to be triangulations',
                twelve_arrow_geometric_seed_binding=False,common_source_node_closed=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()

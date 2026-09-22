"""Standalone rational verifier for one explicitly supported structural model.

No producer, discovery checker, or optional package is imported. The model is
an S-bimodule fixture for S=Q[t]/(t^2); its depth ideal is J=(t_left,t_right).
It is not an identification with the actual 270-row observer.
"""
from fractions import Fraction as F
import json,sys,hashlib

def need(ok,msg):
    if not ok:raise ValueError(msg)
def keys(x,ks):need(type(x) is dict and set(x)==set(ks),'unexpected fields')
def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):
    need(len(a[0])==len(b),'matrix type mismatch')
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def join(a,b):need(len(a)==len(b),'row mismatch');return [x+y for x,y in zip(a,b)]
def block(a,b):return [r+[F(0)]*len(b[0]) for r in a]+[[F(0)]*len(a[0])+r for r in b]
def neg(a):return [[-x for x in r] for r in a]
def rank(a):
    a=[r[:] for r in a];p=0
    for j in range(len(a[0])):
        k=next((k for k in range(p,len(a)) if a[k][j]),None)
        if k is None:continue
        a[p],a[k]=a[k],a[p];v=a[p][j];a[p]=[x/v for x in a[p]]
        for k in range(len(a)):
            if k!=p:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[p])]
        p+=1
        if p==len(a):break
    return p
def same_span(a,b):return rank(a)==rank(b)==rank(join(a,b))
def matrix(raw,n,m):
    need(type(raw) is list and len(raw)==n,'matrix row count')
    out=[]
    for row in raw:
        need(type(row) is list and len(row)==m,'matrix column count')
        need(all(type(x) is str and len(x)<256 for x in row),'rational strings required')
        out.append([F(x) for x in row])
    return out
def diagonal(a):
    need(len(a)==len(a[0]) and all(a[i][i]>0 for i in range(len(a))) and
         all(a[i][j]==0 for i in range(len(a)) for j in range(len(a)) if i!=j),'positive diagonal map required')
def columns(a,js):return [[r[j] for j in js] for r in a]
def model():
    return {'name':'commuting-dual-number-fixture-v1','field':'Q',
     'algebra':'Q[t]/(t^2), commuting left and right actions',
     'depth_ideal':'J=(t_left,t_right) in the enveloping algebra',
     'dimensions':{'E':5,'O':2,'A':3,'B':1,'G':2},
     'source_maps':'fixed i:B->A, q:A->G; identity source comparisons',
     'scope':'finite structural fixture, not a physical observer identification'}
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def base():
    l=zero(5,5);r=zero(5,5);l[1][0]=l[3][2]=F(1)
    r[2][0]=r[3][1]=r[3][4]=F(1)
    p=eye(5)[:2];ol=[[F(0),F(0)],[F(1),F(0)]];orr=zero(2,2)
    al=zero(3,3);ar=zero(3,3);al[2][1]=ar[2][0]=F(1)
    i=[[F(0)],[F(0)],[F(1)]];q=eye(3)[:2]
    return l,r,p,ol,orr,al,ar,i,q
EDGES={'00-10':('00','10'),'00-01':('00','01'),'10-11':('10','11'),'01-11':('01','11')}
def verify(bundle):
    keys(bundle,('schema','problem','problem_sha256','nodes','edges'))
    need(bundle['schema']=='structural-gain-square-v1','schema')
    need(bundle['problem']==model() and bundle['problem_sha256']==digest(bundle['problem'])==digest(model()),'unsupported model/digest')
    keys(bundle['nodes'],('00','10','01','11'));keys(bundle['edges'],EDGES)
    l0,r0,p0,ol0,or0,al,ar,i,q=base();unit=eye(5)
    need(mul(q,i)==zero(2,1) and rank(i)==1 and rank(q)==2,'source exactness')
    need(mul(al,i)==mul(ar,i)==zero(3,1),'source inclusion equivariance')
    need(mul(q,al)==mul(q,ar)==zero(2,3),'source quotient equivariance')
    nodes={}
    shapes={'D':(5,5),'C':(2,2),'left':(5,5),'right':(5,5),
      'lower_left':(2,2),'lower_right':(2,2),'pi':(2,5),
      'K':(5,3),'M':(5,3),'N':(5,2),'L':(5,1),
      'f':(5,1),'H':(5,3),'private':(1,5),'graph':(8,1)}
    for name,raw in bundle['nodes'].items():
        keys(raw,shapes);n={k:matrix(raw[k],*shape) for k,shape in shapes.items()}
        D,C=n['D'],n['C'];diagonal(D);diagonal(C)
        l,r,p=n['left'],n['right'],n['pi']
        need(mul(D,l0)==mul(l,D) and mul(D,r0)==mul(r,D),'upper evaluation does not intertwine')
        need(mul(C,ol0)==mul(n['lower_left'],C) and mul(C,or0)==mul(n['lower_right'],C),'lower evaluation does not intertwine')
        need(mul(p,D)==mul(C,p0),'evaluation transition compatibility')
        need(mul(l,l)==mul(r,r)==zero(5,5) and mul(l,r)==mul(r,l),'algebra relations')
        for action,lower in ((l,n['lower_left']),(r,n['lower_right'])):
            need(mul(p,action)==mul(lower,p),'transition not equivariant')
        K,M,N,L=n['K'],n['M'],n['N'],n['L']
        need(rank(p)==2 and rank(K)==3 and mul(p,K)==zero(2,3),'K not the whole kernel')
        need(rank(M)==3 and same_span(M,join(l,r)),'M not J E')
        need(rank(L)==1 and same_span(L,join(mul(l,M),mul(r,M))),'L not J^2 E')
        need(rank(N)==2 and rank(join(K,N))==3 and rank(join(M,N))==3 and
             rank(K)+rank(M)-rank(join(K,M))==2,'N not K intersect M')
        need(rank(join(N,L))==2 and mul(l,L)==mul(r,L)==zero(5,1),'depth flag')
        need(mul(p,n['H'])==zero(2,3) and mul(n['H'],i)==n['f'],'unfiltered homotopy')
        need(mul(l,n['H'])==mul(n['H'],al) and mul(r,n['H'])==mul(n['H'],ar),'homotopy not equivariant')
        need(n['f']==mul(D,columns(unit,[3])),'wrong source coefficient map')
        need(mul(n['private'],D)==[[F(0),F(0),F(0),F(1),F(0)]],'normalized private row')
        need(mul(r,N)==zero(5,2) and mul(n['private'],n['f'])==[[F(1)]],'level-two obstruction')
        # AR sends the first source basis vector to i(B). Any extension A->N
        # must therefore kill f(B), contradicting the certified private value.
        need(columns(ar,[0])==i,'obstruction source action')
        graph=n['f']+neg(i);need(n['graph']==graph,'wrong pushout relation')
        flags=[block(K,eye(3)),block(N,eye(3)),block(L,i)]
        for flag,dim in zip(flags,(5,4,1)):
            need(rank(join(flag,graph))==rank(flag) and rank(flag)-rank(graph)==dim,'pushout filtration dimensions')
            need(same_span(flag,join(flag,mul(block(l,al),flag))) and
                 same_span(flag,join(flag,mul(block(r,ar),flag))),'unstable pushout flag')
        n['flags']=flags;nodes[name]=n
    edges={}
    for key,(a,b) in EDGES.items():
        raw=bundle['edges'][key];keys(raw,('upper','lower','pushout'))
        U=matrix(raw['upper'],5,5);V=matrix(raw['lower'],2,2);T=matrix(raw['pushout'],8,8)
        diagonal(U);diagonal(V);x,y=nodes[a],nodes[b]
        need(mul(U,x['D'])==y['D'] and mul(V,x['C'])==y['C'],'edge source evaluation')
        for k in ('left','right'):need(mul(U,x[k])==mul(y[k],U),'edge upper action')
        for k in ('lower_left','lower_right'):need(mul(V,x[k])==mul(y[k],V),'edge lower action')
        need(mul(y['pi'],U)==mul(V,x['pi']),'edge transition square')
        for k in ('K','M','N','L'):need(same_span(mul(U,x[k]),y[k]),'edge flag transport')
        need(mul(U,x['f'])==y['f'] and mul(y['private'],U)==x['private'],'edge coefficient transport')
        need(T==block(U,eye(3)) and mul(T,x['graph'])==y['graph'],'pushout relation transport')
        for f,g in zip(x['flags'],y['flags']):need(same_span(mul(T,f),g),'pushout flag transport')
        edges[key]=(U,V,T)
    for j in range(3):
        need(mul(edges['10-11'][j],edges['00-10'][j])==mul(edges['01-11'][j],edges['00-01'][j]),'square routes disagree')
    return {'verified':True,'nodes':4,'edges':4,'coherent_routes':['upper','lower','filtered pushout'],
      'filtered_class':'nonzero at every node by the level-two right-action obstruction',
      'underlying_class':'zero at every node by the supplied equivariant homotopy',
      'scope':model()['scope']}
def pairs(items):
    d={}
    for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
    return d
def reject_number(s):raise ValueError('floating/nonfinite JSON number forbidden')
def load(path):
    with open(path,encoding='utf-8') as f:return json.load(f,object_pairs_hook=pairs,parse_float=reject_number,parse_constant=reject_number)
if __name__=='__main__':
    try:
        need(len(sys.argv)==2,'usage: verify_structural_gain_square.py BUNDLE.json')
        print(json.dumps(verify(load(sys.argv[1])),indent=2))
    except (ValueError,TypeError,KeyError,ZeroDivisionError,IndexError) as e:
        print('REJECTED: '+str(e),file=sys.stderr);sys.exit(1)

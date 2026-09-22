"""Four distinct coherence roles on the finite forgotten-diamond packets.

Exact rational identities, not a claim of four independent tetrahedral faces.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,runpy
ROOT=Path(__file__).resolve().parents[3]
f=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
PRIMES=[2,3,5,7,11,13]


def wire(x):return json.loads(json.dumps(x))
def dot(x,y):return sum((a*b for a,b in zip(x,y)),Q(0))
def basis(n):return [[Q(i==j) for i in range(n)] for j in range(n)]
def moments(a):return [sum((v for b,v in enumerate(a) if b&t==t),Q(0)) for t in range(len(a))]
def inverse(m):return [sum(((-1)**((t^b).bit_count())*v for t,v in enumerate(m) if t&b==b),Q(0)) for b in range(len(m))]


def paths(a,offset,n):
    out={}
    for bits,c in enumerate(a):
        if not c:continue
        word=tuple(e for j in range(n) for e in ((2*(offset+j)+1,2*(offset+j)) if bits&(1<<j) else (2*(offset+j),2*(offset+j)+1)))
        out[word,(0,)*(2*n)]=c
    return out


def encode_m(m,offset,n,level):
    if not (0<=offset<=offset+n<=3 and 0<=level<=n and len(m)==1<<n):raise ValueError('packet')
    return wire({'schema':'typed-forgotten-residual-v1','offset':offset,'blocks':n,
        'primes':PRIMES[2*offset:2*(offset+n)],'level':level,
        'visible':{str(t):str(v) for t,v in enumerate(m) if t.bit_count()<=level},
        'residuals':[{'order':r,'values':{str(t):str(v) for t,v in enumerate(m) if t.bit_count()==r}}
                     for r in range(n,level,-1)]})


def coordinates(e):
    if e['schema']!='typed-forgotten-residual-v1':raise ValueError('schema')
    offset,n,r=e['offset'],e['blocks'],e['level']
    if any(type(v) is not int for v in (offset,n,r)) or not 0<=offset<=offset+n<=3 or not 0<=r<=n:raise ValueError('packet')
    if e['primes']!=PRIMES[2*offset:2*(offset+n)]:raise ValueError('labels')
    if set(e['visible'])!={str(t) for t in range(1<<n) if t.bit_count()<=r}:raise ValueError('visible')
    if [b['order'] for b in e['residuals']]!=list(range(n,r,-1)):raise ValueError('residual orders')
    values=dict(e['visible'])
    for b in e['residuals']:
        if set(b['values'])!={str(t) for t in range(1<<n) if t.bit_count()==b['order']}:raise ValueError('residual labels')
        values.update(b['values'])
    return [Q(values[str(t)]) for t in range(1<<n)]


def lower(e,r):
    if not 0<=r<=e['level']:raise ValueError('not a reduction')
    return encode_m(coordinates(e),e['offset'],e['blocks'],r)


def decode(e):return paths(inverse(coordinates(e)),e['offset'],e['blocks'])


def tensor(a,b):return [x*y for y in b for x in a]


def propagate(e,d,level):
    if e['offset']+e['blocks']!=d['offset']:raise ValueError('incompatible endpoints')
    # Work in interaction coordinates directly, not through decoded source paths.
    return encode_m(tensor(coordinates(e),coordinates(d)),e['offset'],e['blocks']+d['blocks'],level)


def rref(rows,width):
    a=[[Q(v) for v in row] for row in rows];pivots=[];i=0
    for j in range(width):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        pivots.append(j);i+=1
        if i==len(a):break
    return a,pivots


def solve(A,b,n):
    rows,pivots=rref([list(row)+[v] for row,v in zip(A,b)],n)
    if any(not any(row[:n]) and row[n] for row in rows):return None
    x=[Q(0)]*n
    for row,j in zip(rows,pivots):x[j]=row[n]
    kernel=[]
    for j in range(n):
        if j in pivots:continue
        v=[Q(0)]*n;v[j]=1
        for row,k in zip(rows,pivots):v[k]=-row[j]
        kernel.append(v)
    return x,kernel


def canonical(space,n):
    if space is None:return None
    point,directions=space
    normals=solve(directions,[0]*len(directions),n)[1]
    rows,_=rref([row+[dot(row,point)] for row in normals],n)
    return tuple(tuple(row) for row in rows if any(row))


def apply(T,x):return [dot(row,x) for row in T]
def image(T,space):return None if space is None else (apply(T,space[0]),[apply(T,v) for v in space[1]])


def restrict(space,E,z):
    if space is None:return None
    point,directions=space
    params=solve([[dot(row,v) for v in directions] for row in E],
                 [v-dot(row,point) for row,v in zip(E,z)],len(directions))
    if params is None:return None
    def combine(c):return [sum((c[j]*v[i] for j,v in enumerate(directions)),Q(0)) for i in range(len(point))]
    shift=combine(params[0])
    return [x+y for x,y in zip(point,shift)],[combine(v) for v in params[1]]


def pull(E,T):return [[sum((row[i]*T[i][j] for i in range(len(T))),Q(0)) for j in range(len(T[0]))] for row in E]
def action(tail,n):return [list(row) for row in zip(*(tensor(x,tail) for x in basis(1<<n)))]


def main():
    counts={'reconstruction':0,'action':0,'higher_composition':0,'prediction_evidence':0}
    fox_checks=0
    for n in range(1,4):
        for offset in range(4-n):
            start=(1<<(2*offset))-1;end=(1<<(2*(offset+n)))-1
            for a in basis(1<<n):
                for t,value in enumerate(moments(a)):
                    seams=tuple(('e',(1<<(2*(offset+i)))-1,
                                 ((1<<(2*(offset+i)))-1)|(1<<(2*(offset+i)+1)),0)
                                for i in range(n) if t&(1<<i))
                    assert f['vacuum_rows'](start,end,paths(a,offset,n),t.bit_count()).get(seams,0)==value
                    fox_checks+=1
    for n in range(1,4):
        for offset in range(4-n):
            samples=basis(1<<n)+[inverse(v) for v in basis(1<<n)]+[[Q(i-2,i+1) for i in range(1<<n)]]
            for a in samples:
                top=encode_m(moments(a),offset,n,n)
                for r in range(n+1):
                    e=lower(top,r);assert decode(e)==paths(a,offset,n)
                    for q in range(r+1):assert lower(e,q)==lower(top,q)
                    counts['reconstruction']+=1
    for n,m in ((1,1),(1,2),(2,1)):
        for a,b in product(basis(1<<n)+[inverse(v) for v in basis(1<<n)],basis(1<<m)+[inverse(v) for v in basis(1<<m)]):
            for r,t in product(range(n+1),range(m+1)):
                e=encode_m(moments(a),0,n,r);d=encode_m(moments(b),n,m,t)
                for level in range(n+m+1):
                    result=propagate(e,d,level)
                    assert decode(result)==f['multiply'](decode(e),decode(d))
                    assert result==propagate(lower(e,0),lower(d,0),level)
                    assert lower(result,0)==propagate(e,d,0)
                    counts['action']+=1
    one=basis(2)+[inverse(v) for v in basis(2)]+[[Q(2,3),Q(-3,5)]]
    for a,b,c in product(one,repeat=3):
        for r,t,u in product(range(2),repeat=3):
            e,d,h=[encode_m(moments(v),i,1,level) for i,(v,level) in enumerate(zip((a,b,c),(r,t,u)))]
            for intermediate,final in product(range(3),range(4)):
                left=propagate(propagate(e,d,intermediate),h,final)
                right=propagate(e,propagate(d,h,intermediate),final)
                assert left==right
                assert decode(left)==f['multiply'](f['multiply'](decode(e),decode(d)),decode(h))
                counts['higher_composition']+=1
    # Entire rational affine histories, not an enumeration of a few possible states.
    for n,m in ((1,1),(1,2),(2,1)):
        for tail in basis(1<<m)+[inverse(v) for v in basis(1<<m)]+[[Q(0)]*(1<<m)]:
            T=action(tail,n);outdim=1<<(n+m)
            for y in (Q(0),Q(1)):
                histories=solve([[1]*(1<<n)],[y],1<<n)
                evidence_rows=[basis(outdim)[0],[Q(1)]*outdim,
                               [Q(bool(b&1)) for b in range(outdim)]]
                for E in ([evidence_rows[0]],evidence_rows[:2],evidence_rows):
                    for z in product((Q(0),Q(1)),repeat=len(E)):
                        forward=restrict(image(T,histories),E,z)
                        backward=image(T,restrict(histories,pull(E,T),z))
                        assert canonical(forward,outdim)==canonical(backward,outdim)
                        # Refinements accumulate constraints without rewriting y.
                        sequential=histories
                        for row,value in zip(E,z):sequential=restrict(sequential,pull([row],T),[value])
                        assert canonical(sequential,1<<n)==canonical(restrict(histories,pull(E,T),z),1<<n)
                        counts['prediction_evidence']+=1
    # Backward refinement is itself compatible with composing actual actions.
    H=[Q(1),Q(-1)];A=action(H,1);B=action(H,2);BA=pull(B,A)
    E=[basis(8)[0]]
    assert pull(E,BA)==pull(pull(E,B),A)==[[Q(1),Q(0)]]
    histories=solve([[1,1]],[1],2)
    past_fiber=canonical(histories,2)
    refined=restrict(histories,pull(E,BA),[1])
    assert refined==([Q(1),Q(0)],[])
    assert canonical(histories,2)==past_fiber # Original terminal evidence is unchanged.
    assert apply(BA,[Q(1),Q(0)])[0]==1 and apply(BA,[Q(0),Q(1)])[0]==0
    # Lossy propagation has no deterministic terminal-state predictor.
    assert moments([Q(1),Q(0)])[0]==moments([Q(0),Q(1)])[0]
    bad=encode_m(moments([Q(1),Q(0)]),0,1,0);bad['residuals']=[]
    try:decode(bad)
    except ValueError:pass
    else:raise AssertionError('missing residual accepted')
    # Marginally compatible facts can be jointly impossible: retain correlations.
    P=[Q(1),Q(0)];T=action(P,1);same=[basis(4)[0],basis(4)[0]]
    assert all(restrict(image(T,histories),[row],[value]) is not None for row,value in zip(same,[0,1]))
    assert restrict(image(T,histories),same,[0,1]) is None
    report={'passed':True,'schema':'four-finite-residual-coherence-roles-v1','checks':counts,
        'actual_ordered_fox_coordinate_checks':fox_checks,
        'roles':{'reconstruction':'decode(reduce_with_residuals(encode(s)))=s',
                 'action':'decode(propagate(e,d))=decode(e)*decode(d)',
                 'higher_composition':'residual reductions and both associative action routes agree as serialized envelopes',
                 'prediction_evidence':'T(C intersect T^-1(B))=T(C) intersect B, for retained affine histories C'},
        'composition_of_evidence_pullback_checked':True,
        'negative_controls':{'missing_residual_rejected':True,'terminal_only_prediction_impossible':True,
                             'separate_marginal_compatibility_does_not_imply_joint_compatibility':True},
        'prediction_example':{'historical_fact':'a_P+a_Q=1','future_vacuum':'a_P',
                              'new_evidence':'future_vacuum=1','refined_history':'a_P=1, a_Q=0',
                              'historical_reading_rewritten':False},
        'interpretation':'Four coherence roles, with strict witnesses in this finite model. The third follows from the associative product and reconstructive coordinate transport; not four independent tetrahedral faces.',
        'scope':'Finite rational forgotten-block packets and compatible concatenations, exact affine evidence. Not arbitrary marked-source actions, the selected O2, noisy physical acquisition, a source-bimodule splitting, or the full observer-tower tetrahedron.'}
    out=ROOT/'research/nima/results/four-residual-coherence-roles.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()

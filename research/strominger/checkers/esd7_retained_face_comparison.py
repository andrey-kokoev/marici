"""Exact finite linear residual comparison gate, not an analytical homotopy solver.
A passing finite input compares retained presentations; it does not install H.
"""
from fractions import Fraction as Q


def matrix(a):
    if not isinstance(a,list) or not a or not all(isinstance(row,list) and len(row)==len(a[0]) for row in a) or not a[0]:
        raise ValueError('nonempty rectangular matrix required')
    if any(type(x) not in (int,str) for row in a for x in row):
        raise ValueError('exact integer or rational-string entries required')
    return [[Q(x) for x in row] for row in a]


def mul(a,b):
    if len(a[0]) != len(b):
        raise ValueError('matrix type mismatch')
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def sub(a,b):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        raise ValueError('residual type mismatch')
    return [[x-y for x,y in zip(row,col)] for row,col in zip(a,b)]


def rank(a):
    a=[row[:] for row in a]; pivot=0
    for col in range(len(a[0])):
        i=next((i for i in range(pivot,len(a)) if a[i][col]),None)
        if i is None:continue
        a[pivot],a[i]=a[i],a[pivot]; scale=a[pivot][col]
        a[pivot]=[x/scale for x in a[pivot]]
        for j in range(len(a)):
            if j!=pivot:
                scale=a[j][col]; a[j]=[x-scale*y for x,y in zip(a[j],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot


def encode(a):return [[str(x) for x in row] for row in a]


def compare(payload):
    """Three vertices, three edges, full frames and two retained endpoint rows.
    C_v maps the left vertex presentation into the right presentation.
    E_right C_v = B_v E_left retains the two labelled endpoint coordinates.
    All matrices are finite exact input data, never inferred from prototype names.
    """
    vertices=('u','v','w'); edges={'uv':('u','v'),'vw':('v','w'),'uw':('u','w')}
    C={v:matrix(payload['frames'][v]) for v in vertices}
    left={e:matrix(payload['left'][e]) for e in edges}
    right={e:matrix(payload['right'][e]) for e in edges}
    EL={v:matrix(payload['endpointLeft'][v]) for v in vertices}
    ER={v:matrix(payload['endpointRight'][v]) for v in vertices}
    B={v:matrix(payload['endpointFrames'][v]) for v in vertices}
    conditions={}
    for v in vertices:
        n=len(C[v]);conditions['invertibleFrame:'+v]=len(C[v][0])==n and rank(C[v])==n
        conditions['twoEndpoints:'+v]=len(EL[v])==len(ER[v])==2 and rank(EL[v])==rank(ER[v])==2
        conditions['endpointFrame:'+v]=len(B[v])==len(B[v][0])==2 and rank(B[v])==2
        conditions['endpointSquare:'+v]=mul(ER[v],C[v])==mul(B[v],EL[v])
    for e,(s,t) in edges.items():
        conditions['edgeSquare:'+e]=mul(C[t],left[e])==mul(right[e],C[s])
    residual_left=sub(mul(left['vw'],left['uv']),left['uw'])
    residual_right=sub(mul(right['vw'],right['uv']),right['uw'])
    conditions['residualSquare']=mul(C['w'],residual_left)==mul(residual_right,C['u'])
    return {'passed':all(conditions.values()),'conditions':conditions,
            'leftResidual':encode(residual_left),'rightResidual':encode(residual_right),
            'residualErased':False,'analyticalHomotopyEstablished':False,
            'scope':'Finite linear presentation comparison only; neither a supplied analytical homotopy nor a full-complex field binding.'}

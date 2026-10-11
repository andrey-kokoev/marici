"""Third whole-composite comparison and exact record-transport coherence.

Four affine comparison coordinates, not an asserted three-electron atom.
The retained Euclidean projection law is supplied from the existing model.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def dot(a,b):return sum(x*y for x,y in zip(a,b))

def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)

def transpose(a):return tuple(zip(*a))

def mv(a,x):return tuple(dot(r,x) for r in a)

I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
D=tuple(tuple(F((2,6,12)[i] if i==j else 0) for j in range(3)) for i in range(3))


def normals(order):
    prefix=[0];rows=[]
    for new in order:
        row=[F(0)]*4
        for i in prefix:row[i]=1
        row[new]=-len(prefix)
        rows.append(tuple(row));prefix.append(new)
    return tuple(rows)


def transport(source,target):
    return tuple(tuple(F(dot(r,s),dot(r,r)) for s in source) for r in target)


def execute(q,rows):
    original=q;records=[];middles=[]
    for r in rows:
        a=dot(r,q)/dot(r,r)
        q=tuple(x-a*y for x,y in zip(q,r))
        records.append(a);middles.append(q)
    assert q==(sum(original)/4,)*4
    assert dot(original,original)==dot(q,q)+dot(records,mv(D,records))
    recovered=q
    for r,a in reversed(list(zip(rows,records))):
        assert dot(r,recovered)==0
        recovered=tuple(x+a*y for x,y in zip(recovered,r))
    assert recovered==original
    return q,tuple(records),middles


def main():
    orders=list(permutations((1,2,3)))
    frames={o:normals(o) for o in orders}
    for rows in frames.values():
        assert [dot(r,r) for r in rows]==[2,6,12]
        assert all(dot(rows[i],rows[j])==0 for i in range(3) for j in range(i))
        assert all(sum(r)==0 for r in rows)
    transitions={(a,b):transport(frames[a],frames[b]) for a,b in product(orders,repeat=2)}
    for (a,b),t in transitions.items():
        assert mm(transitions[b,a],t)==I
        assert mm(mm(transpose(t),D),t)==D
    for a,b,c in product(orders,repeat=3):
        assert mm(transitions[b,c],transitions[a,b])==transitions[a,c]
    # The adjacent position swaps act by these fixed record-coordinate maps.
    A=transitions[(1,2,3),(2,1,3)]
    B=transitions[(1,2,3),(1,3,2)]
    for o in orders:
        assert transitions[o,(o[1],o[0],o[2])]==A
        assert transitions[o,(o[0],o[2],o[1])]==B
    assert mm(A,A)==mm(B,B)==I
    assert mm(mm(A,B),A)==mm(mm(B,A),B)
    assert mm(A,B)!=mm(B,A)
    # Check the final-state and record maps on a linear basis: identities
    # hold for every real input, not just the illustrative data below.
    for i in range(4):
        q=tuple(F(i==j) for j in range(4))
        outputs={o:execute(q,frames[o]) for o in orders}
        for a,b in product(orders,repeat=2):
            assert mv(transitions[a,b],outputs[a][1])==outputs[b][1]
    q=tuple(map(F,(1,2,4,8)))
    rows=[]
    for o in orders:
        end,records,middles=execute(q,frames[o])
        assert dot(records,mv(D,records))==F(115,4)
        rows.append(dict(order=o,final=end,records=records,intermediate_states=middles,
                         transferred_budget=tuple(F(n)*a*a for n,a in zip((2,6,12),records))))
    # Mistaking order changes for commuting operations fails, despite the
    # verified braid coherence. This is the deliberate incorrect-closure test.
    noncommuting=tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(mm(A,B),mm(B,A)))
    assert any(x for r in noncommuting for x in r)
    result=dict(schema='marici.nima.nested-four-part-coherence.v1',status='pass',
                obligation='whole-composite attachment plus comparisons between order-change paths',
                input_type='four affine comparison coordinates; no particle assignment',
                canonical_normals=frames[(1,2,3)],record_metric=D,
                orders=6,transport_maps=36,composition_triangles=216,
                adjacent_swap_A=A,adjacent_swap_B=B,braid_left=mm(mm(A,B),A),braid_right=mm(mm(B,A),B),
                false_commutation_residual=noncommuting,fixture=rows,
                disposition='Third witness adds a third independent recorded mismatch. Six orders share the barycenter and total budget; record transports compose exactly and obey the braid relation without erasing histories.',
                residual='Supplied affine/Euclidean comparison law. Three record directions are not spatial volume, mass or a third electron. No uniquely selected native physical growth rule has been proved.')
    def enc(x):
        if isinstance(x,F):return str(x)
        if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [enc(v) for v in x]
        return x
    result=enc(result)
    (ROOT/'results/nested-four-part-coherence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='fixture'},indent=2))


if __name__=='__main__':main()

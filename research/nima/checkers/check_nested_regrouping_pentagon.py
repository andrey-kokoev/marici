"""Weighted barycenter regrouping and exact retained-record pentagon.

Four ordered leaves, five binary bracketings. No new physical interaction or
particle is added. Equal-weight averaging of unequal-size groups is a separate
history-weighted readout, not automatically a representation of the same mean.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from check_nested_four_part_coherence import dot, mm, mv, transpose, I, transport

ROOT=Path(__file__).resolve().parents[1]
TREES={
    '(((ab)c)d)':(((0,1),2),3),
    '((a(bc))d)':((0,(1,2)),3),
    '(a((bc)d))':(0,((1,2),3)),
    '(a(b(cd)))':(0,(1,(2,3))),
    '((ab)(cd))':((0,1),(2,3)),
}


def leaves(tree):
    return [tree] if isinstance(tree,int) else leaves(tree[0])+leaves(tree[1])


def frame(tree):
    if isinstance(tree,int):return []
    l,r=tree;left=leaves(l);right=leaves(r)
    row=[F(0)]*4
    for i in left:row[i]=F(len(right))
    for i in right:row[i]=-F(len(left))
    return frame(l)+frame(r)+[tuple(row)]


def center(tree,q,weighted=True):
    if isinstance(tree,int):return q[tree]
    l,r=tree
    a,b=center(l,q,weighted),center(r,q,weighted)
    if not weighted:return (a+b)/2
    p,n=len(leaves(l)),len(leaves(r))
    return (p*a+n*b)/(p+n)


def metric(rows):
    return tuple(tuple(dot(rows[i],rows[i]) if i==j else F(0) for j in range(3)) for i in range(3))


def execute(q,rows):
    original=q;records=[]
    for r in rows:
        a=dot(q,r)/dot(r,r)
        records.append(a)
        q=tuple(x-a*v for x,v in zip(q,r))
    assert q==(sum(original)/4,)*4
    recovered=q
    for a,r in reversed(list(zip(records,rows))):
        assert dot(recovered,r)==0
        recovered=tuple(x+a*v for x,v in zip(recovered,r))
    assert recovered==original
    assert dot(original,original)==dot(q,q)+dot(records,mv(metric(rows),records))
    return tuple(records),q


def main():
    names=list(TREES)
    frames={name:frame(t) for name,t in TREES.items()}
    for rows in frames.values():
        assert len(rows)==3
        assert all(dot(rows[i],rows[j])==0 for i in range(3) for j in range(i))
        assert all(sum(r)==0 for r in rows)
    maps={(a,b):transport(frames[a],frames[b]) for a,b in product(names,repeat=2)}
    for a,b in product(names,repeat=2):
        T=maps[a,b]
        assert mm(maps[b,a],T)==I
        assert mm(mm(transpose(T),metric(frames[b])),T)==metric(frames[a])
    for a,b,c in product(names,repeat=3):
        assert mm(maps[b,c],maps[a,b])==maps[a,c]
    A,B,C,D,E=names
    long=mm(maps[C,D],mm(maps[B,C],maps[A,B]))
    short=mm(maps[E,D],maps[A,E])
    assert long==short==maps[A,D]
    # Basis checks establish every linear active/readout map, not only example.
    for i in range(4):
        q=tuple(F(i==j) for j in range(4))
        for name,t in TREES.items():
            records,end=execute(q,frames[name])
            assert center(t,q)==F(1,4) and end==(F(1,4),)*4
        for a,b in product(names,repeat=2):
            assert mv(maps[a,b],execute(q,frames[a])[0])==execute(q,frames[b])[0]
    q=tuple(map(F,(1,2,4,8)))
    rows=[]
    for name,t in TREES.items():
        records,end=execute(q,frames[name])
        rows.append(dict(bracketing=name,weighted_center=center(t,q),
                         unweighted_group_midpoints=center(t,q,False),
                         records=records,record_metric=metric(frames[name]),
                         budget=dot(records,mv(metric(frames[name]),records))))
    assert all(r['weighted_center']==F(15,4) and r['budget']==F(115,4) for r in rows)
    assert len({r['unweighted_group_midpoints'] for r in rows})==5
    assert rows[0]['unweighted_group_midpoints']==F(43,8)
    assert rows[3]['unweighted_group_midpoints']==F(5,2)
    result=dict(schema='marici.nima.nested-regrouping-pentagon.v1',status='pass',
                obligation='regrouping coherence and representative/readout descent with retained constituent weights',
                merge_rule='(wL,cL),(wR,cR) -> (wL+wR,(wL*cL+wR*cR)/(wL+wR)); retain comparison record',
                bracketings=5,record_maps=25,composition_checks=125,
                long_path=[A,B,C,D],short_path=[A,E,D],long_map=long,short_map=short,
                fixture=rows,
                disposition='Weighted representatives and retained-record maps satisfy the regrouping pentagon. Forgetting subtree weights changes the readout under reassociation.',
                residual='This is the supplied affine comparison realization. Pentagon matrix equality does not identify or erase path histories, derive a native physical law, or turn record rank into spatial volume.')
    def enc(x):
        if isinstance(x,F):return str(x)
        if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [enc(v) for v in x]
        return x
    result=enc(result)
    (ROOT/'results/nested-regrouping-pentagon.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='pass',bracketings=5,record_maps=25,composition_checks=125,
                         pentagon='pass',centers=[{k:r[k] for k in ('bracketing','weighted_center','unweighted_group_midpoints')} for r in result['fixture']]),indent=2))


if __name__=='__main__':main()

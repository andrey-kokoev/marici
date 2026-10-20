#!/usr/bin/env python3
"""Exact finite certificate for Marici's inspected fourQ comparison sector.

The fourQ carrier, swap, independent product lifts and table re-fibration
are transcribed from pinned Agda definitions. This is not Agda execution.
Optional --marici PATH verifies the complete source files by Git blob SHA.
No claim of classification of all native WG histories or pushout attachments.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Callable

Perm = tuple[int, ...]
REF = '37e41e86b558157a496627d9fe9686f3ae97c23f'
SOURCES = {
 'research/nima/agda/BoundaryGeneratedQuestions.agda':'1e27e1350380d39efe58273f81abd77fd576e67a',
 'research/nima/agda/ObserverCoherenceCube.agda':'4abce32028ec145f469fc9acd422a2e76ee496ab',
 'research/nima/agda/NativeTableRegression.agda':'ed8cbc563822fc8434ff622cb482217887f90738',
 'research/nima/agda/TableFibrationCycle.agda':'0138756c0602021e1138190023f79298f23c0adb',
}


def compose(f: Perm, g: Perm) -> Perm:
    """f after g; Boundary.compose f g instead means g after f."""
    return tuple(f[g[i]] for i in range(len(f)))


def inv(f: Perm) -> Perm:
    out = [0]*len(f)
    for i, j in enumerate(f): out[j] = i
    return tuple(out)


def comm(f: Perm, g: Perm) -> Perm:
    return compose(compose(compose(f, g), inv(f)), inv(g))


def order(f: Perm) -> int:
    p, identity = tuple(range(len(f))), tuple(range(len(f)))
    for n in range(1, 100000):
        p = compose(f,p)
        if p == identity: return n
    raise ValueError('Unexpectedly large permutation order')


def sign(f: Perm) -> int:
    return (-1)**sum(f[i]>f[j] for i in range(len(f)) for j in range(i+1,len(f)))


def swap(n: int, i: int, j: int) -> Perm:
    x = list(range(n)); x[i],x[j]=x[j],x[i]; return tuple(x)


def generated(gens: list[Perm]) -> set[Perm]:
    identity=tuple(range(len(gens[0])))
    seen, queue = {identity}, deque([identity])
    while queue:
        x=queue.popleft()
        for g in gens:
            y=compose(g,x)
            if y not in seen: seen.add(y); queue.append(y)
    return seen


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('native_relation_certificate_results.json'))
    parser.add_argument('--marici', type=Path)
    args=parser.parse_args()
    source_hashes = {}
    if args.marici:
        for path, wanted in SOURCES.items():
            data=(args.marici/path).read_bytes()
            got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            if got != wanted: raise ValueError(f'Source version mismatch: {path}: {got} != {wanted}')
            source_hashes[path]=got

    # Exact source definition: fourQ has values Bool x Bool and selected 00;
    # BoundaryGeneratedQuestions.swap-iso sends (x,y) to (y,x).
    points=list(itertools.product((False,True),repeat=2))
    index={p:i for i,p in enumerate(points)}
    a=tuple(index[(y,x)] for x,y in points)
    identity=tuple(range(4))
    assert a==(0,2,1,3) and a[0]==0 and order(a)==2
    S4=set(itertools.permutations(range(4)))
    H={g for g in S4 if g[0]==0}
    assert len(H)==6
    r=(0,2,3,1)
    b=compose(compose(r,a),inv(r))
    assert b==swap(4,2,3)
    assert generated([a,b])==H
    assert compose(a,a)==compose(b,b)==identity
    assert order(compose(a,b))==3
    assert compose(compose(a,b),a)==compose(compose(b,a),b)
    c=comm(a,b)
    assert c!=identity and order(c)==3
    normal_forms={'1':identity,'a':a,'b':b,'ab':compose(a,b),
                  'ba':compose(b,a),'aba':compose(compose(a,b),a)}
    assert set(normal_forms.values())==H

    # Maps (not raw derivation histories) have exact finite extensional equality.
    for f,g in itertools.product(H,repeat=2):
        assert compose(f,g) in H
        assert compose(inv(f),f)==identity
        assert (f==g)==all(f[x]==g[x] for x in range(4))
    # The full function-space pullback distinguishes all six maps.
    signatures={g:tuple(tuple(int(g[x]==j) for x in range(4)) for j in range(4)) for g in H}
    assert len(set(signatures.values()))==6
    assert {g for g in H if sign(g)==1}=={identity,r,compose(r,r)}
    assert all(sign(compose(f,g))==sign(f)*sign(g) for f,g in itertools.product(H,repeat=2))

    # Actual independent-slot recipe extends to m factors.
    product_reports=[]
    for m in range(1,5):
        values=list(itertools.product(range(4),repeat=m))
        def slot(x: tuple[int,...], i: int, g: Perm) -> tuple[int,...]:
            return x[:i]+(g[x[i]],)+x[i+1:]
        for i in range(m):
            for f,g,x in itertools.product(H,H,values):
                assert slot(slot(x,i,g),i,f)==slot(x,i,compose(f,g))
        for i in range(m):
            for j in range(i+1,m):
                for f,g,x in itertools.product(H,H,values):
                    assert slot(slot(x,j,g),i,f)==slot(slot(x,i,f),j,g)
        # Faithfulness can be checked on the separate coordinates; no full 6^(2m) product table is required.
        action_signatures={tuple(g) for g in H}
        assert len(action_signatures)==6
        product_reports.append({'slots':m,'states':4**m,'factorwise_group_order':6**m,
                                'swap_only_group_order':2**m,'cross_slot_interchange':True})
    vals2=list(itertools.product(range(4),repeat=2)); ix2={x:i for i,x in enumerate(vals2)}
    left=tuple(ix2[(a[x],y)] for x,y in vals2)
    right=tuple(ix2[(x,a[y])] for x,y in vals2)
    assert comm(left,right)==tuple(range(16))
    assert len(generated([left,right]))==4

    # Contextual source arrows are actual endofillers evaluated at an unmarked value.
    # This does not replace fourQ's distinguished point 0.
    U=(1,2,3)
    rows=tuple((i,g[i],g) for i in U for g in sorted(H))
    assert len(rows)==18
    rowset=set(rows)
    def compose_rows(first, second):
        i,j,g=first; j2,k,h=second
        if j!=j2: raise ValueError('Not composable')
        return (i,k,compose(h,g))
    for first,second in itertools.product(rows,repeat=2):
        if first[1]==second[0]: assert compose_rows(first,second) in rowset
    for f,g,h in itertools.product(rows,repeat=3):
        if f[1]==g[0] and g[1]==h[0]:
            assert compose_rows(compose_rows(f,g),h)==compose_rows(f,compose_rows(g,h))
    triangles=[]
    for i,j,k in itertools.permutations(U):
        hol=compose(swap(4,k,i),compose(swap(4,j,k),swap(4,i,j)))
        assert hol[0]==0 and hol[i]==i and hol!=identity and order(hol)==2
        triangles.append({'route':[i,j,k,i],'holonomy':hol})

    # Eight field-fibration transitions, retaining keys AND the entire old row.
    nested=tuple((x,x) for x in rows) # (original row, nested witness record)
    field_names=['label','source','target']
    stages=[]
    for step in range(8):
        name=field_names[step%3]
        selected={'label':lambda r:r,'source':lambda r:r[0],'target':lambda r:r[1]}[name]
        grouped=defaultdict(list)
        for original,payload in nested:
            key=selected(original)
            grouped[key].append((original,(key,payload)))
        next_rows=tuple(item for key in sorted(grouped,key=repr) for item in grouped[key])
        assert {original for original,_ in next_rows}==rowset
        assert len(next_rows)==18
        for original,payload in next_rows: assert payload[0]==selected(original)
        nested=next_rows
        stages.append({'rung':11-step,'selected_field':name,'groups':len(grouped),'retained_rows':18})
    for original,payload in nested:
        for _ in range(8): payload=payload[1]
        assert payload==original
    # No horizontal T9 has been manufactured by this generic table instance.

    # Derived pointed/oriented comparison. Orientation is an explicit decoration,
    # not asserted to be selected by the native swap rule.
    A4={g for g in S4 if sign(g)==1}
    C3=A4&H
    assert len(A4)==12 and len(C3)==3
    V4={g for g in A4 if g==identity or (order(g)==2 and all(g[i]!=i for i in range(4)))}
    assert len(V4)==4
    assert {compose(v,t) for v,t in itertools.product(V4,C3)}==A4
    assert V4&C3=={identity}
    assert all(compose(compose(g,v),inv(g)) in V4 for g,v in itertools.product(A4,V4))
    orientation_values=(-1,1)
    decorations=list(itertools.product(range(4),orientation_values))
    orbit={(g[0],sign(g)) for g in S4}
    assert orbit==set(decorations)
    assert {g for g in S4 if (g[0],sign(g))==(0,1)}==C3
    for g,h in itertools.product(S4,repeat=2):
        for i,o in decorations:
            assert (compose(g,h)[i],sign(compose(g,h))*o)==(g[h[i]],sign(g)*sign(h)*o)

    # Degree-respecting benchmark map: F[S1]_0=1; d0(t)=1.
    # In the constant simplicial group H, d0 is the identity. Only t->1 is legal.
    target_d0 = lambda g: g  # faces of a constant simplicial group
    source_d0_t = identity   # d0(t)=1 in F[S1]
    admitted=[g for g in H if target_d0(g)==source_d0_t]
    assert admitted==[identity]
    assert a not in admitted and b not in admitted and c not in admitted

    report={
      'status':'passed',
      'source_ref':REF,
      'source_blob_manifest':SOURCES,
      'source_files_locally_hash_verified':bool(args.marici),
      'checked_source_hashes':source_hashes,
      'source_definition_method':'faithful finite transcription of inspected Agda bodies; no proof-assistant run',
      'fourQ':{'values':points,'selected':0,'actual_swap':a,'all_endofillers':sorted(H)},
      'single_factor':{'group':'S3','normal_forms':normal_forms,'same_slot_commutator':c,'commutator_order':3},
      'independent_slots':product_reports,
      'independent_swap_square':{'commutator_identity':True,'group_order':4,'raw_schedules_not_identified':True},
      'unmarked_context':{'objects':3,'arrows':18,'isotropy_orders':[2,2,2],
                         'classifying_type':'B(C2)','triangle_holonomies':triangles},
      'retained_table_stages':stages,
      'rung_scope':'generic exact label/from/to re-fibration instance; no assertion about horizontal T9',
      'decoration_comparison':{'unpointed_group':'S4','pointed_group':'S3','oriented_group':'A4',
        'pointed_oriented_group':'C3','pointing_cover_degree':4,'orientation_cover_degree':2,
        'normal_translation_subgroup':sorted(V4),'orientation_selection':'additional explicit decoration'},
      'benchmark_comparison':{'nontrivial_simplicial_maps_to_constant_S3':False,
        'reason':'degree-one face condition forces the source generator to identity'},
      'scope':'Finite comparison semantics and its canonical groupoids; not raw-history adequacy or topology-changing WG classification',
      'proof_assistant_executed':False,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['source_blob_manifest','fourQ','retained_table_stages']},indent=2))

if __name__=='__main__': main()

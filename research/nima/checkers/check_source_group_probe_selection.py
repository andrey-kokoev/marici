"""Does the existing seed-generated body group select a probe geometry?

Reuses both prior probe dictionaries. The full-seed group is the existing
Machian construction. Regenerating it after deletions is an explicitly
labelled extension of that construction, not a selected physical response.
"""
from contextlib import redirect_stdout
from pathlib import Path
from fractions import Fraction as F
import hashlib
import io
import json
import runpy
import sympy as S

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(HERE/'check_seed_probe_exchange_bridge.py'))
    body = runpy.run_path(str(HERE/'check_machian_thing_eigenline_cycle.py'))
probe = prior['prior']
packets = prior['PACKETS']
registry = {label:(s,t) for label,s,t in packets}
labels = tuple(registry)
triangles = (('AB','BC','CA'), ('AD','DB','BA'))
identity = (0,1,2,3)
compose = body['compose']
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def generator(word):
    result = list(identity)
    for label in word:
        a,b = registry[label]
        result['ABCD'.index(a)] = 'ABCD'.index(b)
    assert sorted(result) == list(identity)
    return tuple(result)


def group_for(retained):
    # Only the two original marked triangle cycles generate this body group;
    # no extra seam transposition is inserted to recover S4.
    generators = [generator(w) for w in triangles if set(w) <= retained]
    group, todo = {identity}, [identity]
    while todo:
        p = todo.pop()
        for g in generators:
            q = compose(g,p)
            if q not in group:
                group.add(q); todo.append(q)
    return sorted(group)


check('original-body-generators-recovered', tuple(map(generator,triangles)) == ((1,2,0,3),(3,0,2,1)))
full = group_for(set(labels))
check('original-twelve-element-group', len(full) == 12 and all(body['parity'](p)==1 for p in full))


def restrict_probes(group, retained, family):
    dictionary = probe.fixed if family == 'endpoint-fixing' else probe.transition
    positions = [probe.group.index(p) for p in group]
    values = {}
    for label in retained:
        a,b = registry[label]
        edge = probe.edges.index(('ABCD'.index(a),'ABCD'.index(b)))
        values[label] = S.Matrix([dictionary[edge].get(k,F(0)) for k in positions])
    return values


rows = []
for removed in ((), ('AD',), ('BC',), ('AD','BC')):
    retained = set(labels)-set(removed)
    group = group_for(retained)
    for family in ('endpoint-fixing','directed-transition'):
        values = restrict_probes(group, [p for p in labels if p in retained], family)
        norms = {p:(v.T*v)[0] for p,v in values.items()}
        # Same named AB-BA two-event experiment. Never normalize a zero probe.
        if norms['AB'] == 0 or norms['BA'] == 0:
            overlap = None
        else:
            overlap = S.simplify((values['AB'].T*values['BA'])[0]/S.sqrt(norms['AB']*norms['BA']))
        rank = S.Matrix.hstack(*values.values()).rank()
        rows.append({'removed':list(removed),'family':family,'group_size':len(group),
                     'feature_rank':rank,'zero_ports':[p for p,n in norms.items() if n==0],
                     'AB_BA_amplitude':None if overlap is None else str(overlap),
                     'available':overlap is not None})
        if not removed:
            check('full-seed-no-zero-probes/'+family, all(n>0 for n in norms.values()))
            check('full-seed-rank/'+family, rank == (1 if family=='endpoint-fixing' else 6))
            check('full-seed-two-pulse/'+family, overlap == (1 if family=='endpoint-fixing' else S.Rational(1,3)))
        if removed and family == 'directed-transition':
            if len(removed)==1:
                check('one-triangle-overlap-zero/'+str(removed), overlap == 0)
            else:
                check('no-triangles-protocol-unavailable', overlap is None)
        if family == 'endpoint-fixing':
            check('reciprocal-fixed-probes-identical/'+str(removed), values['AB']==values['BA'])

# The actual full source group is already 2-transitive: the directed pair
# overlaps agree with the previous S4 counting kernel. Hence changing that
# group carrier need not change the observed normalized kernel at all.
values = restrict_probes(full, labels, 'directed-transition')
for a in labels:
    for b in labels:
        va,vb = values[a],values[b]
        overlap = S.simplify((va.T*vb)[0]/S.sqrt((va.T*va)[0]*(vb.T*vb)[0]))
        ia = probe.edges.index(tuple('ABCD'.index(v) for v in registry[a]))
        ib = probe.edges.index(tuple('ABCD'.index(v) for v in registry[b]))
        old_overlap = probe.dot(probe.transition[ia],probe.transition[ib])/F(6)
        check('directed-S4-kernel-preserved/'+a+'/'+b, overlap == old_overlap)

result = {
    'schema':'marici.nima.source-group-probe-selection.v1','status':'pass','checks':checks,
    'full_source':'original two triangle permutations generate A4 with 12 elements',
    'full_source_result':'endpoint-fixing and directed-transition probes both remain available but yield ranks 1 and 6; AB-BA transfer 1 and 1/3',
    'selection':'not achieved: group selection does not choose the query/probe or physical measure, preparation, and exchange semantics',
    'environment_extension':'rebuild group from surviving original triangle generators; new deletion policy explicitly declared',
    'rows':rows,
    'mixed_environment_response':'undefined for directed-transition model after both triangle generators disappear; never replace unavailable port by zero',
    'native_constructor_audit':'WholePackageResolution compare-rule consumes an equivalence and marked-value path; higher-rule consumes its higher equality. No probe/metric/preparation selector found in those inspected signatures.',
    'input_sha256':{str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
      [HERE/'check_seed_probe_exchange_bridge.py', HERE/'check_machian_thing_eigenline_cycle.py',
       HERE.parent/'agda/WholePackageResolution.agda', HERE/'check_source_group_probe_selection.py']},
}
(HERE.parent/'results/source-group-probe-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact source-group selection tests')
print('Existing source-generated group does not select between prior probes.')
for row in rows:
    print(row)

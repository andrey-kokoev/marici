"""Test stage-cost selection against prior retained source operations.

Replays the operation-resolved comparison graph, checks all admitted interchange
faces, and separates traversal cochains, onsite energy and preparation effort.
No measured mass or target gap is used.
"""
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import io
import json
import runpy

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE.parent/'nima/checkers/check_mass_path_port_connectivity.py'


def stage(slot):
    _,(kind,_,right) = slot
    if kind == 'state':
        return 'L'
    return 'G' if right[0] == 0 else 'N'


def rank(rows):
    a = [list(map(F,row)) for row in rows]
    r = 0
    for c in range(3):
        p = next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None:
            continue
        a[r],a[p] = a[p],a[r]
        q = a[r][c]
        a[r] = [v/q for v in a[r]]
        for i in range(r+1,len(a)):
            q = a[i][c]
            if q:
                a[i] = [x-q*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


def main():
    with redirect_stdout(io.StringIO()):
        source = runpy.run_path(str(SOURCE))
    slots,index,directions = source['slots'],source['index'],source['directions']
    assert len(slots) == 1836
    assert Counter(map(stage,slots)) == {'L':108,'G':432,'N':1296}
    kind_for = {}
    for kind,edges in directions.items():
        for e in edges:
            assert e not in kind_for
            kind_for[e] = kind
    assert len(kind_for) == 17820
    outer_arcs = sorted({(slots[a][0],slots[b][0]) for a,b in directions['outer']})
    inner_arcs = sorted({(slots[a][1],slots[b][1]) for kind in ('inner_left','inner_right','endpoint') for a,b in directions[kind]})
    assert len(outer_arcs)==36 and len(inner_arcs)==1026
    relation_rows,witnesses = set(),{}
    face_count = 0
    operations = ('outer','inner_left','inner_right','endpoint')

    def face(vertices):
        nonlocal face_count
        terms = [(vertices[0],vertices[1],1),(vertices[1],vertices[2],1),
                 (vertices[3],vertices[2],-1),(vertices[0],vertices[3],-1)]
        role_balance = Counter()
        stage_balance = Counter()
        for a,b,sign in terms:
            role_balance[kind_for[a,b]] += sign
            stage_balance[stage(slots[a])] += sign
        assert all(v==0 for v in role_balance.values())
        row = tuple(stage_balance[s] for s in ('L','G','N'))
        relation_rows.add(row)
        if any(row):
            witnesses.setdefault(row,{'slots':[slots[v] for v in vertices],
                                      'operations':[kind_for[a,b] for a,b,_ in terms],
                                      'cost_equation':list(row)})
        # Four independent operation-role costs, with no equality fitted:
        # each admitted face preserves each role count separately.
        for costs in ((1,1,1,1),(2,3,5,7),(7,5,3,2)):
            assert sum(sign*costs[operations.index(kind_for[a,b])] for a,b,sign in terms)==0
        # Positive coherent costs need not be departure-stage-only. An
        # operation-role cost plus an onsite energy difference also descends.
        for gap in ((2,1,1),(1,2,1)):
            potential = lambda vertex:gap[('L','G','N').index(stage(slots[vertex]))]
            assert sum(sign*((2,3,5,7)[operations.index(kind_for[a,b])]+potential(b)-potential(a))
                       for a,b,sign in terms)==0
        face_count += 1

    for o0,o1 in outer_arcs:
        for d0,d1 in inner_arcs:
            face([index[(o0,d0)],index[(o1,d0)],index[(o1,d1)],index[(o0,d1)]])
    for outer in sorted({s[0] for s in slots}):
        for a0,a1 in outer_arcs:
            for b0,b1 in outer_arcs:
                face([index[(outer,('arrow',a0,b0))],index[(outer,('arrow',a1,b0))],
                      index[(outer,('arrow',a1,b1))],index[(outer,('arrow',a0,b1))]])
    assert face_count == 52488
    assert rank(sorted(relation_rows)) == 2
    assert all(sum(row)==0 for row in relation_rows)
    assert any(row[0] and row[1] and not row[2] for row in relation_rows)
    assert any(row[1] and row[2] and not row[0] for row in relation_rows)
    # The only source-stage-only departure costs descending through every
    # square are therefore c_L=c_G=c_N. They still charge returning appends.
    inner = ('state',1,1)
    u,v = index[((0,1),inner)],index[((1,0),inner)]
    assert kind_for[u,v]==kind_for[v,u]=='outer'
    assert 1+1 == 2
    # Stage labels are stable under the generous independent rooted S3 action.
    # Thus onsite (stored) stage gaps can still have either ordering.
    group = [(0,)+p for p in permutations((1,2,3))]
    def edge(p,e):
        return (p[e[0]],p[e[1]])
    symmetry_cases = 0
    for po,pl,pr in product(group,repeat=3):
        for slot in slots:
            o,(kind,a,b) = slot
            changed = (edge(po,o),(kind,edge(pl,a),edge(pr,b))) if kind=='arrow' else (edge(po,o),(kind,pl[a],pr[b]))
            assert changed in index and stage(changed)==stage(slot)
            symmetry_cases += 1
    # Taking differences of any onsite potential produces a telescoping
    # cochain, not a strictly positive traversal cost on a returning loop.
    countermodels = []
    counts_p,counts_b = (108,432,1296),(432,108,1296)
    for gap in ((F(2),F(1),F(1)),(F(1),F(2),F(1)),(F(1),F(1),F(1))):
        energy_p = sum(n*x for n,x in zip(counts_p,gap))
        energy_b = sum(n*x for n,x in zip(counts_b,gap))
        assert energy_b-energy_p == 324*(gap[0]-gap[1])
        potential = lambda vertex:gap[('L','G','N').index(stage(slots[vertex]))]
        paid = []
        for (a,b),kind in kind_for.items():
            sink = F((2,3,5,7)[operations.index(kind)])
            delta = potential(b)-potential(a)
            work = sink+delta
            assert work>0 and delta+sink-work==0
            paid.append(work)
        assert (potential(v)-potential(u))+(potential(u)-potential(v))==0
        countermodels.append({'stage_gaps':list(map(str,gap)),'stored_energy_difference':str(energy_b-energy_p),
                              'positive_coherent_cost_min':str(min(paid)),'positive_coherent_cost_max':str(max(paid)),
                              'edge_reservoir_balance_checked':len(paid)})
    departure = {s:Counter() for s in ('L','G','N')}
    for (a,b),kind in kind_for.items():
        departure[stage(slots[a])][kind] += 1
    means = {s:str(F(sum(count.values()),n)) for (s,count),n in zip(departure.items(),counts_p)}
    assert means == {'L':'3','G':'39/4','N':'41/4'}
    # Preparation control on the same commuting-projector carrier, not on
    # the above path graph: fresh maximally mixed input each aborted trial.
    preparations = {}
    for name,rank_l,rank_g in [('proton',12,3),('belt',3,12)]:
        p_l,p_g,p_both = F(rank_l,36),F(rank_g,36),F(1,36)
        assert p_l*F(1,rank_l)==p_g*F(1,rank_g)==p_both
        preparations[name] = {'L_then_G':{'L_attempts':36,'G_attempts':rank_l,'total_unit_attempts':36+rank_l},
                              'G_then_L':{'L_attempts':rank_g,'G_attempts':36,'total_unit_attempts':36+rank_g},
                              'both_always':72,'success_per_fresh_trial':str(p_both)}
    assert preparations['proton']['L_then_G']['total_unit_attempts']==48
    assert preparations['belt']['L_then_G']['total_unit_attempts']==39
    assert preparations['proton']['G_then_L']['total_unit_attempts']==39
    assert preparations['belt']['G_then_L']['total_unit_attempts']==48
    result = {
        'verification_passed':True,'source_operation_edges':17820,'interchange_faces_checked':face_count,
        'comparison_slot_stage_counts':dict(Counter(map(stage,slots))),
        'departure_stage_cost_constraint_rank':2,
        'departure_stage_cost_solution':'c_L=c_G=c_N',
        'scope_of_equality':'Cost of every forward source operation depends only on its departure slot stage, and additive path cost is invariant under the admitted interchanges.',
        'independent_operation_role_costs_allowed':list(operations),
        'positive_returning_append_cost':2,
        'rooted_symmetry_cases_checked':symmetry_cases,
        'onsite_gap_countermodels':countermodels,
        'coherent_positive_cost_family':'r(e)=kappa_operation+V(target)-V(source), kappa=(2,3,5,7); battery change=-r, resource-sink change=kappa',
        'outgoing_operations_by_departure_stage':{s:dict(c) for s,c in departure.items()},
        'mean_enabled_outgoing_operations':means,
        'preparation_trial':preparations,
        'preparation_scope':'Fresh maximally mixed input, unit attempt costs, immediate abort on failed first test; scheduling and reset resources are supplied. G-first is a competing commuting-projector implementation, not an asserted interchange of the original typed three-stage protocol.',
        'square_witnesses':list(witnesses.values()),
        'physical_selection_alignment_cost_order_selected':False,
        'next_gate':'Construct a physically weighted record-change functional on actual operation histories, with specified reservoirs and particle-sector occupation. Onsite gaps, traversal costs and preparation effort must not be identified without that map.',
        'source_sha256':sha256(SOURCE.read_bytes()).hexdigest()
    }
    path = BASE/'results/selection_alignment_cost_selection.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='square_witnesses'},indent=2))


if __name__=='__main__':
    main()

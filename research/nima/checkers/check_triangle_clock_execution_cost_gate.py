"""Conditional primitive-event cost audit, not a physical scheduler.

If every newly constructed continuation word is executed once, count its
new final primitive. Do not charge retained prefix words again. The source
constructor itself has not declared these constructions to be events.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    clock=runpy.run_path(str(HERE/'check_triangle_source_contrast_clock.py'))
c=clock['c']; ledger=c['ledger']; labels=ledger.labels
whole=ledger.retain_payload(ledger.root,(1,)*6)
left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)


def edge_counts(payloads):
    return tuple(sum(value for payload in payloads for path,value in zip(payload.paths,payload.values)
                     if path[-1][2]==label) for label in labels)


def target_counts(payloads):
    return {v:sum(value for payload in payloads for path,value in zip(payload.paths,payload.values)
                  if path[-1][1]==v) for v in 'ABCD'}

layers=[]
for tick in range(9):
    before=target_counts((left,right))
    left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
    actual=edge_counts((left,right))
    expected=tuple(before[c['registry'][label][0]] for label in labels)
    check('primitive-event-multiplicity/'+str(tick),actual==expected)
    check('unit-occurrence-not-weighted-amplitude/'+str(tick),all(v==1 for p in (left,right) for v in p.values))
    layers.append(actual)
cycles=[tuple(sum(layers[i][j] for i in range(k,k+3)) for j in range(6)) for k in (0,3,6)]
check('first-cycle',cycles[0]==(6,6,4,6,6,4))
check('second-cycle',cycles[1]==(26,26,16,26,26,16))
check('third-cycle',cycles[2]==(110,110,68,110,110,68))
differences=[tuple(b-a for a,b in zip(x,y)) for x,y in zip(cycles,cycles[1:])]
check('strict-componentwise-cost-growth',all(v>0 for d in differences for v in d))
# Every nonnegative fixed cost vector with at least one positive entry gives
# a strictly positive dot product with these positive differences. This is
# a coefficientwise certificate, not a finite sampling of cost assignments.
check('calibration-independent-positive-gap',differences[0]==(20,20,12,20,20,12))

# The combined endpoint count stays (a,a,b,b), with (a,b)->(a+b,a).
# From positive initial (1,1), a increases and b catches up. Hence primitive
# counts and cycle workloads are unbounded, independent of clock phase return.
S=clock['S']
a,b=S.symbols('a b')
check('source-total-invariant-sector',clock['M']*S.Matrix([a,a,b,b])==S.Matrix([a+b,a+b,a,a]))
result={
    'schema':'marici.nima.triangle-clock-execution-cost-gate.v1','status':'pass','checks':checks,
    'primitive_order':labels,
    'per_layer_counts':[[int(v) for v in row] for row in layers],
    'three_phase_cycle_counts':[[int(v) for v in row] for row in cycles],
    'unit_cost_cycle_work':[int(sum(row)) for row in cycles],
    'cost_gap_coefficients':[int(v) for v in differences[0]],
    'conditional_theorem':'under one executed attempt per new branch and fixed nonnegative primitive costs not all zero, cycle 2 costs strictly more than cycle 1 for EVERY such cost calibration',
    'duration_scope':'cost means time only if identified with sequential event duration; the source positive-resource proposal alone does not make that identification',
    'bounded_capacity_scope':'unbounded cycle work obstructs bounded uniform period if a fixed finite work-per-time capacity and actual execution of every branch are additionally required',
    'not_selected':['physical execution of all branches','sequential versus parallel scheduling','time per primitive','physical work-to-time conversion','compressed phase-only execution'],
}
(ROOT/'results/triangle-clock-execution-cost-gate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact execution-cost gate checks')
print('Three-cycle workloads at unit primitive cost: 32, 136, 576.')
print('The increase holds for every fixed positive primitive-cost assignment, not only equal costs.')
print('No source-selected physical scheduler or duration is inferred.')

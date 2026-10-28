"""Bounded candidate: counter-traversals of the labelled twelve-sector square.
No P/E species binding, coefficient action, spatial turn or global 28-stage law
is presumed. Each step translates endpoint labels and re-fibrates the whole table.
"""
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = tuple((4*i+j, i, j) for i in range(4) for j in range(4) if i != j)


def transport(rows, g):
    return tuple(sorted((label, s ^ g, t ^ g) for label, s, t in rows))


def fibrate(rows):
    # Source-column instance of the marked TableFibrationCycle finite formulas.
    return tuple((s, tuple(sorted((label, t) for label, a, t in rows if a == s))) for s in range(4))


def restore(fibers):
    return tuple(sorted((label, s, t) for s, children in fibers for label, t in children))


def trace(start, axes, steps=30):
    g = start
    history = []
    states = []
    for k in range(steps+1):
        rows = transport(BASE, g)
        states.append({'stage': k, 'source_corner': g, 'rows': rows,
                       'source_fibers': fibrate(rows), 'history': tuple(history),
                       'active_sectors': tuple((s,t) for _,s,t in rows if s == g)})
        if k < steps:
            move = axes[k % 2]
            history.append(move)
            g ^= move
    return states


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    check('twelve retained occurrences and three sectors per source', len(BASE) == 12 and all(len(c) == 3 for _,c in fibrate(BASE)))
    check('source fibration reconstructs all marked rows', all(restore(fibrate(transport(BASE,g))) == transport(BASE,g) for g in range(4)))
    check('two factor flips are independent commuting involutions', transport(transport(BASE,1),1) == BASE and transport(transport(BASE,2),2) == BASE and transport(transport(BASE,1),2) == transport(transport(BASE,2),1) and transport(BASE,1) != transport(BASE,2))
    check('sector differences are conserved channel labels', all((s ^ t) == ((s ^ g) ^ (t ^ g)) for _,s,t in BASE for g in range(4)))
    check('all chart comparisons compose coherently', all(transport(transport(transport(BASE,g),g ^ h),h ^ j) == transport(BASE,j) for g,h,j in product(range(4),repeat=3)))
    forward, backward = trace(0,(1,2)), trace(3,(2,1))
    for name, states in [('forward',forward),('backward',backward)]:
        check(name+' preserves full fibration at every stage', all(restore(s['source_fibers']) == s['rows'] for s in states))
        check(name+' retains ordered transition history', all(len(s['history']) == s['stage'] for s in states))
    coincident = [k for k in range(29) if forward[k]['rows'] == backward[k]['rows']]
    check('same-stage full tables coincide exactly at odd stages', coincident == list(range(1,29,2)))
    check('crossing does not identify histories', all(forward[k]['history'] != backward[k]['history'] for k in coincident))
    check('four-stage endpoint return preserves nonempty history', forward[4]['rows'] == forward[0]['rows'] and forward[4]['history'] != forward[0]['history'])
    check('stage 28 returns each to its own endpoint table', forward[28]['rows'] == forward[0]['rows'] and backward[28]['rows'] == backward[0]['rows'])
    check('stage 28 does not exchange distinct endpoint tables', forward[28]['rows'] != backward[0]['rows'] and backward[28]['rows'] != forward[0]['rows'])
    exchanged = [k for k in range(1,31) if forward[k]['rows'] == backward[0]['rows'] and backward[k]['rows'] == forward[0]['rows']]
    check('endpoint exchanges occur at 2 mod 4, not 28', exchanged == list(range(2,31,4)))
    check('complementary-stage comparison at 28 is not literal matching', all(forward[k]['rows'] != backward[28-k]['rows'] for k in range(29)))
    check('complementary-stage comparison at exchange time 30 does match tables', all(forward[k]['rows'] == backward[30-k]['rows'] for k in range(31)))
    # Coordinate changes applied to every endpoint, not an altered phase law.
    frame_cases = 0
    for p in permutations(range(4)):
        relabel = lambda rows: tuple(sorted((label,p[s],p[t]) for label,s,t in rows))
        for axes in [(1,2),(2,1)]:
            a,b = trace(0,axes,28), trace(3,axes[::-1],28)
            assert relabel(a[28]['rows']) == relabel(a[0]['rows'])
            assert relabel(a[28]['rows']) != relabel(b[0]['rows'])
            assert [k for k in range(29) if relabel(a[k]['rows']) == relabel(b[k]['rows'])] == coincident
            frame_cases += 1
    check('24 endpoint relabelings times two traversal senses preserve findings', frame_cases == 48)
    sources = ['research/nima/table-fibration.md', 'research/nima/checkers/check_table_fibration.py',
               'research/nima/arrow-history-window.md', 'research/realization-tower/definition.md',
               'research/strominger/checkers/check_two_ended_sector_trace.py']
    report = {'status':'passed', 'check_count':len(checks), 'checks':checks,
              'candidate':{'endpoint_labels':['A=00','B=10','C=01','D=11'],
                           'forward_seed':0,'backward_seed':3,'forward_axes':[1,2],'backward_axes':[2,1],
                           'phase_definition':'one endpoint-label translation followed by source-column fibration; not one stage of the four-stage group/reversed-unpack cycle',
                           'endpoint_role_binding':'P/E identification is hypothetical, not derived'},
              'forward':forward, 'backward':backward, 'same_stage_crossings_through_28':coincident,
              'endpoint_exchange_stages_through_30':exchanged,'discrete_frame_cases':frame_cases,
              'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
              'disposition':'Passing with coherent label transport is constructed; opposite-endpoint arrival at 28 is rejected for this periodic candidate only.',
              'scope':'Exact labelled incidence and source-fibration recovery. No C3 coefficient transport, higher physical coherence, esd7 assembly, continuous rotation covariance, or Pb-208 interpretation is constructed.'}
    dest = ROOT/'research/strominger/results/two-ended-sector-trace.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'frame_cases':frame_cases,'crossings':coincident,'exchange_stages':exchanged,'result':str(dest)}))


if __name__ == '__main__':
    main()

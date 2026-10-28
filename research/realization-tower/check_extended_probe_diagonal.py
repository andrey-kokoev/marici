"""Point-probe 12x12 continuation audit on the extended FCC octahedral axis.

This extends the point-pole experiment, NOT the six tetrahedral-carrier pool.
Every comparison keeps first-channel labels and exact walk witnesses.
"""
from itertools import product
from collections import defaultdict, Counter
from pathlib import Path
import json
from check_six_step_octahedron import interval, distance, add

DIRECTIONS=tuple(sorted(d for d in product((-1,0,1),repeat=3) if sum(abs(x) for x in d)==2))


def paths_by_channel(origin,depth):
    result=[]
    for d in DIRECTIONS:
        paths=[(origin,add(origin,d))]
        for _ in range(1,depth):
            paths=[p+(add(p[-1],step),) for p in paths for step in DIRECTIONS]
        endpoints=defaultdict(list)
        for p in paths:endpoints[p[-1]].append(p)
        result.append(endpoints)
    return result


def audit(start,end,depth):
    left=paths_by_channel(start,depth);right=paths_by_channel(end,depth)
    table=[];meetings=set();walk_count=0;shortest=set();walks=[]
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            common=sorted(a.keys()&b.keys());meetings.update(common)
            count=sum(len(a[p])*len(b[p]) for p in common);walk_count+=count
            table.append({'entry_channel':i,'exit_channel':j,'meeting_vertices':common,'joined_walks':count})
            # At the first meeting depth every joined walk is shortest. Retain
            # all of them, not only one selected branch or scalar count.
            if depth*2==distance(start,end):
                for p in common:
                    for pa in a[p]:
                        for pb in b[p]:
                            joined=pa+tuple(reversed(pb[:-1]))
                            assert len(joined)==distance(start,end)+1
                            assert all(distance(x,y)==1 for x,y in zip(joined,joined[1:]))
                            shortest.update(joined);walks.append(joined)
    assert len(table)==144
    return {'depth_each_side':depth,'comparison_slots':len(table),'matching_slots':sum(bool(r['meeting_vertices']) for r in table),
            'distinct_meeting_vertices':len(meetings),'joined_walk_witnesses':walk_count,
            'table':table,'shortest_walks':walks,'shortest_walk_union':sorted(shortest)}


def main():
    start=(0,0,0);old_end=(2,0,0);end=(4,0,0)
    old=audit(start,old_end,1)
    reports=[audit(start,end,d) for d in (1,2,3)]
    assert old['distinct_meeting_vertices']==4
    assert reports[0]['matching_slots']==0
    first=reports[1]
    assert first['distinct_meeting_vertices']==9
    assert first['joined_walk_witnesses']==36
    assert len(set(first['shortest_walks']))==36
    expected=interval(start,end)
    assert set(first['shortest_walk_union'])==expected
    assert Counter(distance(start,p) for p in expected)=={0:1,1:4,2:9,3:4,4:1}
    assert len(expected)==19
    # Two extra levels allow detours as well. Do not call all longer walk
    # matches part of the minimal completion.
    assert reports[2]['joined_walk_witnesses']>first['joined_walk_witnesses']
    bad_endpoint=(3,0,0)
    assert sum(bad_endpoint)%2!=0
    report={'status':'pass','source':'FCC even-sum integer chart; point probes',
      'entry':start,'old_exit':old_end,'new_exit':end,
      'one_axis_unit':[2,0,0],'nearest_neighbour_distance_before':2,'nearest_neighbour_distance_after':4,
      'match_rule':'Coincidence of continuation endpoints in the common lattice codomain; retain first-channel and complete path provenance',
      'baseline':old,'extended':reports,
      'recovered_interval':{'grades':[1,4,9,4,1],'vertices':19,'tetrahedra':8,'octahedra':6,
                            'cell_count_source':'small-octahedra-v1.json, four-step case'},
      'limits':['First-channel comparisons remain 144 but each slot can contain many continuation witnesses.',
                'Lattice vertices here are codomain match cells; no tetrahedral-particle correspondence is supplied.',
                'The shortest-path union recovers a geometric interval, not a full higher-coherence certificate.',
                'Two extra levels were allowed; only one extra level per side was needed to first meet.']}
    # Cross-check existing independently enumerated cell count receipt.
    prior=json.loads((Path(__file__).with_name('results')/'small-octahedra-v1.json').read_text())
    middle=next(c for c in prior['cases'] if c['steps']==4)
    assert (middle['vertices'],middle['tetrahedra'],middle['octahedra'])==(19,8,6)
    out=Path(__file__).with_name('results')/'extended-probe-diagonal-v1.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','levels':[{k:r[k] for k in ('depth_each_side','comparison_slots','matching_slots','distinct_meeting_vertices','joined_walk_witnesses')} for r in reports],
                      'interval':report['recovered_interval']}))


if __name__=='__main__':main()

"""Feed growing packet tables through the existing retained-total rung schedule.

Reuses the existing finite fibration kernel and fresh graph-geometry calculation.
This verifies transport to rung4; it does not invent a physical metric or clock.
"""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
from contextlib import redirect_stdout
import io
import json
import runpy

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    kernel = runpy.run_path(str(HERE/'check_label_from_to_fibration_tower.py'))
    runpy.run_path(str(HERE/'check_line_graph_geometry.py'))
original = kernel['original']
geometry = json.loads((HERE.parent/'results/line-graph-geometry.json').read_text())
assert geometry['status'] == 'passed'

edges = {(0,1),(0,2),(1,2),(0,3)}
reports = []
for cycle in range(8):
    directed = sorted([pair for edge in edges for pair in (edge,edge[::-1])])
    initial = [(i,a,b) for i,(a,b) in enumerate(directed)]
    initial_set = set(initial)
    current = initial
    stages = [{'rung':12,'rows':len(current),'selected_field':None}]
    for depth in range(8):
        column = depth % 3
        family = defaultdict(list)
        for row in current:
            family[original(row,depth)[column]].append(row)
        current = [(key,row) for key,fiber in family.items() for row in fiber]
        assert len(current) == len(initial)
        # Retained keys witness the inherited field; full leaves remain intact.
        assert all(original(row,depth)[column] == key for key,row in current)
        assert {original(row,depth+1) for row in current} == initial_set
        stages.append({'rung':11-depth,'rows':len(current),
                       'selected_field':('label','from','to')[column],
                       'occupied_fibers':len(family)})
    restored = [original(row,8) for row in current]
    rung4_directed = {(a,b) for label,a,b in restored}
    assert rung4_directed == set(directed)
    rung4_edges = {tuple(sorted((a,b))) for a,b in rung4_directed}
    assert rung4_edges == edges
    vertices = {v for edge in edges for v in edge}
    observed = geometry['cycles'][cycle]
    assert observed['vertices'] == len(vertices) and observed['edges'] == len(edges)
    # Therefore the freshly computed unit-hop metric transports exactly to
    # rung4 via reconstruction; no rescaling follows from grouping itself.
    reports.append({'cycle':cycle,'stages':stages,
                    'rung4_total_rows':len(current),
                    'rung4_occupied_source_fibers':len(vertices),
                    'recovered_graph_identical':True,
                    'transported_unit_hop_diameter':observed['diameter'],
                    'transported_unit_hop_mean_distance':observed['mean_distance'],
                    'physical_length':None,'proper_time_increment':None,
                    'physical_readout_status':'metric and clock maps unspecified'})
    print(cycle,'rung4 rows',len(current),'source fibers',len(vertices),
          'unit-hop diameter',observed['diameter'],flush=True)
    # Release retained tuples before building the next graph.
    del current, family, restored, initial, initial_set, directed
    if cycle < 7:
        incidence = defaultdict(list)
        for i,(a,b) in enumerate(sorted(edges)):
            incidence[a].append(i); incidence[b].append(i)
        edges = {tuple(sorted(pair)) for ids in incidence.values() for pair in combinations(ids,2)}

result = {'status':'passed','source_kernel':'check_label_from_to_fibration_tower.py',
          'schedule':['label','from','to','label','from','to','label','from'],
          'cycles':reports,
          'conclusion':'Descent transports the full packet graph faithfully to rung4. It does not select a physical spatial metric or cycle duration, nor reduce all rows to four.',
          'unfixed_readout_freedom':'Multiplying any candidate spatial metric by a positive cycle-dependent factor leaves the table/fibration transport unchanged; cycle duration is likewise not fixed by these operators.'}
(HERE.parent/'results/growth-rung4-readout.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: all8 descents preserve packet labels, endpoints and reconstructed graphs.')

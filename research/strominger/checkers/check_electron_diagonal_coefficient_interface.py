"""Test existing coefficient interfaces on all five admitted diagonal seeds.

No projection, fixed-fixture substitution or new coefficient law is inserted.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from assemble_triangle_arrow_source import assemble as coefficient_assemble
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import apply


def main():
    path=ROOT/'research/strominger/results/electron_diagonal_seeds.json'
    original=path.read_bytes()
    data=json.loads(original)
    assert data['status']=='passed'
    # Ensure the already generated source records still bind current code.
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['source_hashes'].items())
    points={'A':(0,0,0,0)}
    points.update({label:tuple(int(i==j) for i in range(4)) for j,label in enumerate('BCDE')})
    cell=frozenset('BCDE') # facet opposite the retained A pole
    rows=[]
    for name in ('plus_DB','plus_AD','plus_CA','plus_EC','plus_BE'):
        case=data['cases'][name]
        assert case['status']=='assembled'
        source={'vertices':{k:list(v) for k,v in points.items()},'arrows':case['arrows']}
        try:
            coefficient_assemble(source)
        except ValueError as error:
            rejection=str(error)
        else:
            raise AssertionError('4D source unexpectedly accepted: inspect new interface')
        permutations=[]
        for g in case['source']['generators']:
            action=(tuple(tuple(map(Q,row)) for row in g['matrix']),tuple(map(Q,g['translation'])))
            by_point={v:k for k,v in points.items()}
            permutations.append({k:by_point[apply(action,v)] for k,v in points.items()})
        frontier=[cell];orbit={cell}
        while frontier:
            c=frontier.pop()
            for p in permutations:
                image=frozenset(p[v] for v in c)
                if image not in orbit:orbit.add(image);frontier.append(image)
        # Raw endpoint continuation is a different, currently available measure.
        arrows=case['arrows']
        composable=sum(a[1]==b[0] for a in arrows for b in arrows)
        rows.append({'case':name,'coefficient_frontend':'assemble_triangle_arrow_source',
                     'rejection':rejection,'added_generator_preserves_attachment':frozenset(permutations[1][v] for v in cell)==cell,
                     'full_generator_attachment_orbit':sorted(''.join(sorted(c)) for c in orbit),
                     'attachment_orbit_size':len(orbit),
                     'primitive_occurrences':len(arrows),'raw_composable_pairs':composable,
                     'new_coefficient_transfers':None})
    checks={'all_five_4D_inputs_rejected':all(r['rejection']=='Vertices must supply rational three-dimensional coordinates' for r in rows),
            'all_attachment_orbits_have_five_cells':all(r['attachment_orbit_size']==5 for r in rows),
            'only_DB_EC_new_generators_preserve_marked_cell':{r['case'] for r in rows if r['added_generator_preserves_attachment']}=={'plus_DB','plus_EC'},
            'raw_continuation_counts_agree':len({r['raw_composable_pairs'] for r in rows})==1,
            'source_receipt_unchanged':path.read_bytes()==original}
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,'cases':rows,
            'disposition':'New coefficient-network counts unavailable from inspected constructors. Triangle frontend requires 3D; fixed electron spinor producer does not accept these inputs. All full actions move the attachment through five cells; missing spinor transport cannot be replaced with the old 144-transfer fixture.',
            'existing_missing_map_source':'research/voevodsky/checkers/check_geometric_phase_energy_bridge.py: electron_gate',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,Path(__file__).resolve(),ROOT/'research/nima/checkers/assemble_triangle_arrow_source.py',ROOT/'research/voevodsky/checkers/check_electron_tetrahedral_spinor.py']}}
    dest=ROOT/'research/strominger/results/electron_diagonal_coefficient_interface.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()

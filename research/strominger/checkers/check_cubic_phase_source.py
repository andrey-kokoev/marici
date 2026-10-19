"""Regression and rejection controls for the phase-input adapter."""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from assemble_cubic_phase_source import run, decode_source, assemble, evolve, ROOT


def main():
    phase_path = ROOT/'research/strominger/inputs/neutron-phase-source.json'
    legacy_path = ROOT/'research/voevodsky/inputs/mode-neutron.json'
    source = json.loads(phase_path.read_text())
    legacy = json.loads(legacy_path.read_text())
    result = run(source)
    checks = {'same_unselected_geometry': result['unselected_geometry'] == assemble(legacy),
              'same_complete_cycle': result['cycle'] == evolve(legacy),
              'input_has_no_spatial_coordinates': all(set(s)=={'phase','role'} for s in source['seeds']),
              'primitive_phase_source_retained': result['phase_source'] == source}
    h = Q(source['height_scale'])
    decoded = lambda row: [str(Q(row['phase'][1])), str(h*Q(row['height_moment'])), str(Q(row['phase'][0]))]
    checks['all_vertices_recover'] = [decoded(r) for r in result['phase_cells']['vertices']] == result['unselected_geometry']['vertices']
    checks['center_recovers'] = decoded(result['phase_cells']['center']) == result['unselected_geometry']['center']
    caps = [r for r in result['phase_cells']['facet_centroids'] if r['phase']==['0','0']]
    checks['cap_moments_remain_distinct'] = len(caps)==2 and {r['height_moment'] for r in caps}=={'-1','1'}
    changed = deepcopy(source); changed['height_scale']='1/2'
    other = run(changed)
    checks['height_not_erased'] = other['unselected_geometry']['squared_distances'] != result['unselected_geometry']['squared_distances']
    changed = deepcopy(source); changed['seeds'].reverse()
    reordered = run(changed)
    checks['seed_order_not_upper_lower_semantics'] = all(reordered['cycle'][k]==result['cycle'][k] for k in ('facet_states','centroid_motion_trace'))
    reversed_action = deepcopy(source); reversed_action['phase_multiplier']=['-1/2','1/2']
    back = run(reversed_action)
    checks['reversed_action_preserves_geometry_changes_trace'] = back['unselected_geometry']==result['unselected_geometry'] and back['cycle']['centroid_motion_trace']!=result['cycle']['centroid_motion_trace']
    def reject(label, modified, message):
        try: run(modified)
        except ValueError as error: checks[label]=message in str(error)
        else: checks[label]=False
    bad=deepcopy(source); bad['height_scale']='0'; reject('zero_height_rejected',bad,'positive')
    bad=deepcopy(source); bad['phase_multiplier']=['1','0']; reject('identity_multiplier_rejected',bad,'order three')
    bad=deepcopy(source); bad['seeds'][0]['phase']=['1','2']; reject('nonreal_cubic_seed_rejected',bad,'must be real')
    bad=deepcopy(source); bad['seeds']=bad['seeds'][:1]; reject('one_rim_does_not_silently_fill',bad,'do not span')
    bad=deepcopy(source); bad['upper_lower']=[1,-1]; reject('undeclared_coordinates_rejected',bad,'fields only')
    paths=[phase_path,legacy_path,Path(__file__).resolve(),ROOT/'research/strominger/checkers/assemble_cubic_phase_source.py']
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'research/strominger/results/cubic_phase_source_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    if not all(checks.values()): raise SystemExit(1)


if __name__=='__main__': main()

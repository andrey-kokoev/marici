#!/usr/bin/env python3
"""Exact cut/composition equivalence test for retained two-output records."""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_neutrino_arrow_seed_science import rank
from check_half_electron_positron_seeds import matmul

def rename(label,r):return 'ABCDE'[('ABCDE'.index(label)+r)%5]
def signature(occ,r=0,reverse=False):
    path=[rename(label,r) for label in occ['retained_path']]
    owner=occ['source_owner']
    if reverse:path.reverse();owner='positron' if owner=='electron' else 'electron'
    return owner,occ['operation'],tuple(path)

def find_equivalence(base,target):
    for reverse in (False,True):
        for rotation in range(5):
            for output_map in permutations(range(2)):
                maps=[]
                for i,j in enumerate(output_map):
                    source=base['outputs'][i]['compound_occurrences'];dest=target['outputs'][j]['compound_occurrences']
                    transformed=[signature(o,rotation,reverse) for o in source]
                    actual=[signature(o) for o in dest]
                    if Counter(transformed)!=Counter(actual):break
                    maps.append([actual.index(s) for s in transformed])
                else:return {'rotation':rotation,'reverse_all_arrows_and_exchange_owners':reverse,'output_permutation':list(output_map),'occurrence_permutations':maps}
    return None

def transfer_checks(base,target,witness):
    # The native photon plane g=u+i sqrt(3) w in each shared-seam registry.
    U=[[Q(1),Q(0)],[-Q(1),Q(0)],[Q(1,2),Q(1,2)],[-Q(1),Q(0)],[Q(1),Q(0)],[-Q(1,2),-Q(1,2)]]
    reports=[]
    for i,j in enumerate(witness['output_permutation']):
        p=witness['occurrence_permutations'][i]
        J=[[Q(p[col]==row) for col in range(6)] for row in range(6)]
        K=[[Q(x) for x in row] for row in base['outputs'][i]['continuation_matrix']]
        L=[[Q(x) for x in row] for row in target['outputs'][j]['continuation_matrix']]
        shifted=matmul(J,U)
        # Compare plane membership, allowing an internal basis change.
        joined=[a+b for a,b in zip(U,shifted)]
        plane_preserved=rank(joined)==2
        expected=matmul(J,matmul(matmul(K,K),U)) if witness['reverse_all_arrows_and_exchange_owners'] else matmul(J,matmul(K,U))
        actual=matmul(L,shifted)
        defect=[[a-b for a,b in zip(row_a,row_b)] for row_a,row_b in zip(actual,expected)]
        transposed=[[K[col][row] for col in range(6)] for row in range(6)]
        expected_full=matmul(matmul(J,transposed if witness['reverse_all_arrows_and_exchange_owners'] else K),[[J[col][row] for col in range(6)] for row in range(6)])
        reports.append({'source_output':i,'target_output':j,'full_incidence_reversal_or_isomorphism':L==expected_full,'native_right_mode_plane_preserved_by_occurrence_map':plane_preserved,'expected_phase_transport':'inverse phase' if witness['reverse_all_arrows_and_exchange_owners'] else 'same phase','phase_transport_defect_rank':rank(defect),'phase_transport_defect':[[str(x) for x in row] for row in defect]})
    return reports

def main():
    source_path=ROOT/'research/strominger/results/two_output_comparison_promotion.json'
    source=json.loads(source_path.read_text());base=source['example'];results=[]
    for attempt in source['attempts']:
        witness=find_equivalence(base,attempt)
        assert witness is not None
        reports=transfer_checks(base,attempt,witness)
        results.append({'meeting_labels':attempt['meeting_labels'],'rule':attempt['rule'],'equivalence':witness,'mode_transport':reports})
    forward=[row for row in results if not row['equivalence']['reverse_all_arrows_and_exchange_owners']]
    reversed_rows=[row for row in results if row['equivalence']['reverse_all_arrows_and_exchange_owners']]
    checks={
        'all_ten_attempts_equivalent_as_retained_paired_histories':len(results)==10,
        'all_occurrence_maps_bijective':all(sorted(p)==list(range(6)) for row in results for p in row['equivalence']['occurrence_permutations']),
        'all_continuation_matrices_match_isomorphism_or_transpose':all(report['full_incidence_reversal_or_isomorphism'] for row in results for report in row['mode_transport']),
        'five_rotated_same_composition_attempts':len(forward)==5,
        'five_opposite_composition_attempts_use_pair_reversal':len(reversed_rows)==5,
        'rotations_preserve_native_phase_plane':all(report['native_right_mode_plane_preserved_by_occurrence_map'] and report['phase_transport_defect_rank']==0 for row in forward for report in row['mode_transport']),
        'pair_reversal_exposes_right_mode_transport_defect':all(not report['native_right_mode_plane_preserved_by_occurrence_map'] and report['phase_transport_defect_rank']>0 for row in reversed_rows for report in row['mode_transport']),
    }
    residual=next(report for row in reversed_rows for report in row['mode_transport'])
    out={'schema':'marici.strominger.two-output-cut-independence.v1','status':'passed' if all(checks.values()) else 'failed','checks':checks,'results':results,'scientific_disposition':'cut-independent retained seed shapes/history pairs modulo rotations and whole-pair reversal; native right-mode transport not yet composition-choice independent','equivalence_operations':['rotate all original five-cycle labels','reverse every retained path and exchange electron/positron ownership','exchange the two outputs','reindex compound occurrences without dropping history'],'positive':'All ten paired constructions are explicitly equivalent at the arrow/history level. Rotating the cut preserves the native photon mode plane and phase update.','residual':'Switching first-two versus last-two composition requires global path reversal and source/output exchange. Incidence becomes the transpose under the occurrence correspondence. Its right photon mode plane is not carried into the target right plane by that raw correspondence.','first_phase_residual':residual,'next_exact_test':'Construct and test the induced left/right mode identification under the retained positive metric; do not substitute a fresh target eigenvector for transported data.','source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),source_path,ROOT/'research/strominger/checkers/check_neutrino_arrow_seed_science.py',ROOT/'research/strominger/checkers/check_half_electron_positron_seeds.py']}}
    (ROOT/'research/strominger/results/two_output_cut_independence.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'first_phase_residual':residual},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()

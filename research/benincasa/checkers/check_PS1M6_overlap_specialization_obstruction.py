#!/usr/bin/env python3
"""Test extension of the endpoint nearby lift across marked-cut overlaps."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
loc=json.loads((R/'cyclic-leray-naturality-certificate.json').read_text())
cross=json.loads((R/'cross-sector-overlap-certificate.json').read_text())
cous=json.loads((R/'three-cut-cousin-cocycle-certificate.json').read_text())
ep=json.loads((R/'results/PS1M5_endpoint_collar_specialization.json').read_text())
assert loc['leray_residue_matrix']=='identity_6'
assert loc['leray_residue_commutes_with_cyclic_permutation']
assert loc['all_pairwise_iterated_marked_cut_residues']==0
assert cross['source_double_pole_G12_G23'] is False
assert cous['pairwise_cut_residues']==[0,0,0] and cous['triple_cut_residue']==0
assert cous['exact_in_full_source_cousin_complex'] and cous['nonzero_in_degree_positive_truncation']
out={'schema':'marici.benincasa.PS1M6-overlap-specialization-obstruction.v1','prospective_action':'PS1M6_extend_endpoint_specialization_across_overlaps','resolution':'-+','local_result':{'six_occurrence_Leray_map':'identity','cyclic_naturality':True,'endpoint_lift_from_PS1M5':ep['nearby_occurrence_lift']},'overlap_test':{'pairwise_iterated_residues':[0,0,0],'triple_residue':0,'joint_marked_cut_pole':False,'koszul_intersection_exists':True},'conclusion':'The source canonically supplies all six local occurrence maps, but supplies no pair-overlap coefficient arrow. The nearby occurrence vector is exact from the frozen meromorphic pre-residue form in the full Cousin complex and survives only in the degree-positive support truncation. Therefore the endpoint lift does not extend to the requested degree-15-to-nearby natural transformation on overlap columns.','moduli_consequence':'PS1A and the nearby packet still cannot be compared as global realizations. Their equal normalized e6/H0 signature is a filtered common-line coincidence, not a chain-level equivalence.','reopening_interface':['a source term with a genuine joint marked-cut pole','or an independently authorized correspondence whose boundary supplies the missing overlap map'],'passed':True}
(R/'results/PS1M6_overlap_specialization_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

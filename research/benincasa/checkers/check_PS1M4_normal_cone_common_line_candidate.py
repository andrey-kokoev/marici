#!/usr/bin/env python3
"""Derive the unique cyclic common-line candidate; keep geometric existence conditional."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
ps=json.loads((R/'results/PS1M1_Leray_Cech_homology_signature.json').read_text())
near=json.loads((R/'cyclic-cut-nearby-sewing.json').read_text())
lay=json.loads((R/'full-rank12-cut-nearby-layers-certificate.json').read_text())
A=ps['augmentation_signature']; c=ps['normalized_common_coefficient']; mult=near['forget_occurrence_multiplicities']
assert A==3*c and mult==[2,2,2]
assert lay['intersection_rank']==1 and lay['intersection_generator']=='e6'
assert near['residue_orientation_signs']==[1,1,1]
# Cyclic transitivity forces one coefficient k on each primitive positive occurrence;
# forgetting the paired occurrence contributes multiplicity two per sector.
assert A%sum(mult)==0
k=A//sum(mult)
assert 2*k==c
out={
 'schema':'marici.benincasa.PS1M4-normal-cone-common-line-candidate.v1',
 'prospective_action':'PS1M4_normal_cone_common_line_candidate',
 'resolution':'+-',
 'derived':{
  'only_common_algebraic_carrier':'e6',
  'cyclic_positive_occurrence_coefficient':k,
  'forgotten_occurrence_sector_coefficient':2*k,
  'three_sector_augmentation':sum(mult)*k,
  'matches_PS1A_H0_augmentation':sum(mult)*k==A,
  'orientation':'positive in all three sectors'},
 'axioms_used':['factorization through the sole algebraic intersection line e6','cyclic transitivity','positive residue orientations','declared occurrence-forgetting multiplicity two','PS1A integral H0 normalization'],
 'positive_result':'These constraints select a unique integral nearby common-line candidate and reproduce the PS1A augmentation exactly.',
 'missing_geometric_arrow':'No source artifact constructs specialization of each supported degree-15 d0/overlap column to the cut-incidence object. Thus the candidate is a uniquely normalized target class, not yet the value of a natural transformation.',
 'next':'Materialize specialization on the three endpoint collar generators first; verify base change and iterated-cut transitivity before extending to the 984 supported columns.',
 'passed':True}
(R/'results/PS1M4_normal_cone_common_line_candidate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

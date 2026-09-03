#!/usr/bin/env python3
"""Audit the source-labelled twisted-de-Rham deletion cube and its Möbius grades."""
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
one=json.loads((P/'generic-q-pole-twisted-derham-rank.json').read_text());cube=json.loads((P/'generic-multi-q-pole-twisted-derham-rank.json').read_text())
r=cube['complete_closed_cube'];grades=[]
for mask in range(8):
 s=0
 for sub in range(8):
  if sub&~mask==0:s+=(-1)**(bin(mask^sub).count('1'))*r[sub]
 grades.append(s)
out={'schema':'marici.benincasa.cosmology-twisted-derham-compatibility-audit.v1','single_deletion_stable_ranks':one['depth_two']['ambient_10'],'published_single_deletion_targets':one['published_targets'],'single_deletion_match':one['depth_two']['ambient_10']==one['published_targets'],'closed_cube':r,'recomputed_mobius_support_grades':grades,'recorded_mobius_support_grades':cube['proper_support_grades'],'mobius_match':grades==cube['proper_support_grades'],'kinematic_replication':cube['point_A']['ambient_9']==cube['point_B_ambient_9'],'compatible':one['depth_two']['ambient_10']==one['published_targets'] and grades==cube['proper_support_grades'] and cube['point_A']['ambient_9']==cube['point_B_ambient_9'],'scope':'generic Cayley-Menger weight 5 over F_32003 at the two recorded kinematic points and tested pole/degree filtration; no physical exponent, characteristic-zero, closure, or canonical comparison promotion'}
(P/'results'/'cosmology_twisted_derham_compatibility_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

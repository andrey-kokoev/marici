"""Weak-row ancestor selection depends on explicit surplus and catalogue scope."""
from fractions import Fraction as Q
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
weak=((1,1),3)
def image(m,c=Q(0)):
 rows=old+(weak,)
 return tuple(sum(Q(rows[i][0][j])*m[i] for i in range(len(m))) for j in (0,1)),sum(Q(rows[i][1])*m[i] for i in range(len(m)))+c
primitive=(Q(0),Q(1),Q(0),Q(1));lift=(primitive+(Q(0),),Q(1))
new=((Q(0),)*4+(Q(1),),Q(0))
old_zero=((Q(1),Q(2),Q(0),Q(1),Q(0)),Q(0))
assert image(*lift)==image(*new)==image(*old_zero)==((1,1),Q(3))
assert image(primitive,Q(0))==((1,1),Q(2))
relative=lambda packet:(packet[0][4],packet[1],packet[0][:4])
assert min((lift,new),key=relative)==lift
assert min((new,),key=relative)==new
assert min((old_zero,new),key=relative)==old_zero
assert image(new[0],new[1])==image(lift[0],lift[1])
report={'passed':True,'frozen_primitive_packet_bound':'2 without surplus','lifted_ancestor_packet_bound':'3 with surplus 1','new_row_packet_bound':'3 with surplus 0','base_anchored_choice_if_lift_present':'lift','restricted_zero_surplus_catalogue_with_only_new_row':'new row','alternative_old_zero_surplus_proof_exists':'x-low+x-high cycle added to old uppers','scope':'Fixed finite catalogue and unit square. Never infer intrinsic absence of old proofs from absence in catalogue. Ancestor priority requires explicit surplus closure and provenance; not owner admission.'}
out=Path(__file__).resolve().parents[1]/'results/ancestor-surplus-catalogue.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))

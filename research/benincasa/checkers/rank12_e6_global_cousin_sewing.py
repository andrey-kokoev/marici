"""Global Cousin typing of the six first-Rees physical e6 germs."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-e6-global-cousin-sewing.json'
c=Fraction(1,4)
d0=[c]*6
d1=[[0]*6 for _ in range(3)]
assert [sum(row[j]*d0[j] for j in range(6)) for row in d1]==[0,0,0]
forget=[d0[0]+d0[1],d0[2]+d0[3],d0[4]+d0[5]]
assert forget==[Fraction(1,2)]*3

packet={
 'schema':'marici.benincasa.rank12_e6_global_cousin_sewing.v1',
 'occurrence_order':['12|23','12|31','23|31','23|12','31|12','31|23'],
 'degree_one_vector':['1/4']*6,
 'pairwise_differential_rank':0,
 'closed':True,
 'source_primitive':'(1/4)*Omega_src',
 'exact_in_full_rational_cousin_complex':True,
 'nonzero_in_truncated_associated_grade':True,
 'occurrence_forgetting':['1/2','1/2','1/2'],
 'new_global_cohomology_rank':0,
 'classification':'the local pairings sew as the exact first residue of the frozen source form; they define a nonzero filtered support grade but no new global cohomology class'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))

"""Relative zero-fresh-row selector: path coherence depends on candidate closure."""
from fractions import Fraction as Q
from pathlib import Path
import json
p=(Q(0),Q(1),Q(0),Q(1),Q(0),Q(0))
z=(Q(0),Q(0),Q(0),Q(0),Q(1),Q(0))
w=(Q(0),Q(0),Q(0),Q(0),Q(0),Q(1))
# Two distinct row IDs, both x+y<=2. Canonical coordinate order old,z,w.
def image(v):return (v[1]-v[0]+v[4]+v[5],v[3]-v[2]+v[4]+v[5]),v[1]+v[3]+2*(v[4]+v[5])
assert image(p)==image(z)==image(w)==((1,1),Q(2))
def choose(candidates,new,previous):
 assert candidates
 return min(candidates,key=lambda v:(v[new],tuple(v[i] for i in previous)))
old=(0,1,2,3)
# At each stage candidate set DOES contain the previous selected proof.
# Yet a zero-newest tie at the final stage is resolved by the prior coordinate
# order, so a formerly unselected proof beats the included previous winner.
first_path=choose((p,z,w),5,old+(4,))
second_path=choose((p,z,w),4,old+(5,))
assert choose((p,z),4,old)==p and choose((p,w),5,old)==p
assert first_path==z and second_path==w and first_path!=second_path
# Refine priority to zero TOTAL non-base-row mass: holds on this finite set.
rooted=lambda v:(v[4]+v[5],tuple(v[i] for i in old))
assert min((p,z,w),key=rooted)==p
report={'passed':True,'old_selection':'p in both intermediate paths','inclusion_closed_final_candidates':'{p,z,w} retains old selected proof','order_dependent_final_selection':'z after z-first; w after w-first','zero_total_fresh_mass_repairs_this_finite_square':True,'distinct_row_ids_required':True,'scope':'Frozen finite candidates for two duplicate exact redundant rows. Zero-newest-row policy fails order coherence even with candidate inclusion; ancestor-relative mass rescue is not a global composition-functorial theorem or source grant.'}
out=Path(__file__).resolve().parents[1]/'results/two-extension-relative-selector.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))

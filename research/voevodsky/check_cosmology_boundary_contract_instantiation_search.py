"""Test materialized programme candidates against the nine-field physical contract."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_boundary_contract_instantiation_search.json'
FIELDS=('physical_source','kinematic_map','cycle_map','avoidance_certificate','orientation_authority','boundary_prescription','normalization','state_effect_pairing','record_map')
def complete(row):return all(row[f] for f in FIELDS)
def main():
 no={f:False for f in FIELDS}
 candidates={
  'rank26_DNC_source':dict(no),
  'exceptional_split_torus':dict(no,kinematic_map=True),
  'chosen_Betti_torus':dict(no,cycle_map=True,avoidance_certificate=True),
  'Parshin_orientation':dict(no,orientation_authority=True),
  'normalized_K2_period':dict(no,normalization=True),
 }
 assert not any(complete(r) for r in candidates.values())
 aggregate={f:any(r[f] for r in candidates.values()) for f in FIELDS}
 assert [f for f,v in aggregate.items() if not v]==['physical_source','boundary_prescription','state_effect_pairing','record_map']
 out={'schema':'marici.voevodsky.cosmology-boundary-contract-instantiation-search.v1','status':'no_materialized_candidate_instantiates_physical_contract','candidate_matrix':candidates,'aggregate_mathematical_fields':['kinematic_map','cycle_map','avoidance_certificate','orientation_authority','normalization'],'missing_physical_fields':['physical_source','boundary_prescription','state_effect_pairing','record_map'],'compatibility_warning':'The aggregate list combines separate mathematical artifacts. It is not itself one source object and does not authorize composition across them.','candidate_dispositions':{'rank26_DNC_source':'relation presentation with absorbed p-normal image; not a physical configuration or record source','exceptional_split_torus':'algebraic coordinate target only; no physical domain map','chosen_Betti_torus':'closed mathematical cycle with no boundary-condition selection','Parshin_orientation':'residue orientation, not physical contour authority','normalized_K2_period':'dimensionless mathematical normalization, not units or amplitude normalization'},'decision':'No candidate, and not even their unauthorised aggregate, supplies the physical-source, boundary-prescription, pairing, and record arrows. The physical-period branch is blocked pending external source data.','next_gate':'K2-integral-lattice: continue the admissible mathematical branch by identifying the integral/Tate lattice class detected simultaneously by period and Parshin residue','limitations':['bounded to materialized programme candidates','does not test unspecified external cosmological models','state-effect pairing may be inapplicable to a nonprobabilistic amplitude but a physical source and record interface remain required'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

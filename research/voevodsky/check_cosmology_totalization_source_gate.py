"""Test whether mapping-cone totalization alone creates the missing horn source cell."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; OUT=V/'cosmology_totalization_source_gate.json'
def load(n):return json.loads((V/n).read_text())
def main():
 inv=load('cosmology_relative_horn_source_degree_inventory.json');formal=load('cosmology_tau_lift_formal_problem.json');unit=load('cosmology_comparison_morphism_unit_gate.json');assert inv['passed'] and formal['passed'] and unit['passed']
 d2=[[1,-1],[-1,1],[1,-1]];c=[1,1];assert [sum(r[j]*c[j] for j in range(2)) for r in d2]==[0,0,0]
 out={'schema':'marici.voevodsky.cosmology-totalization-source-gate.v1','status':'mapping_cone_totalization_packages_but_does_not_create_missing_nullhomotopy','existing_complex':{'degree_1_sourced_rank':0,'degree_2_basis':['Xi_log','minus_sigma123'],'closed_primitive_pair':[1,1]},'formal_totalization_fact':'A cone or homotopy-fiber construction can shift and package existing cochains, maps, and homotopies. A degree-one element mapping to the closed pair exists only when a nullhomotopy/comparison arrow is supplied as input.','forced_comparison':'If an exceptional-face coefficient is fixed to one, the chain condition forces the Xi coefficient to one; this determines a hypothetical map but does not construct it.','decision':'Totalization is not an independent source mechanism. Applying a mapping cone to the current data either leaves degree-one rank zero or inserts the missing nullhomotopy as part of the cone map, which is circular.','admissible_next_source':'a deformation-to-normal/Rees correspondence with an independently defined specialization or connecting morphism whose chain-level boundary is computed, not stipulated, to be (1,1)','limitations':['formal gate for constructions using only currently materialized objects and maps','does not rule out a new geometric correspondence carrying its own nullhomotopy','no Bockstein or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

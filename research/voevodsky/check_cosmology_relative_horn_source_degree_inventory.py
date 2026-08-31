"""Inventory currently sourced cells at the exact degree required by the relative horn."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; OUT=V/'cosmology_relative_horn_source_degree_inventory.json'
def load(n):return json.loads((V/n).read_text())
def main():
 horn=load('cosmology_tau_lift_formal_problem.json'); face=load('cosmology_blowup_exceptional_cell_gate.json'); gysin=load('cosmology_corner_blowup_global_gysin_map.json'); cm=load('cosmology_CM_relative_face_source_gate.json'); assert all(x['passed'] for x in [horn,face,gysin,cm])
 inventory=[
 {'object':'ordered exceptional/Cech face sigma123','source_derived':True,'cochain_degree':2,'map':'boundary to pair-face edges','eligible_incoming_horn_cell':False,'reason':'it is already the second coordinate of the degree-two closed pair, not a degree-one preimage'},
 {'object':'exceptional hyperplane Gysin class H','source_derived':True,'cochain_degree':2,'map':'ordinary restriction to Xi is zero','eligible_incoming_horn_cell':False,'reason':'no chain map H to Xi and wrong role in the total complex'},
 {'object':'abstract tau_p','source_derived':False,'cochain_degree':1,'map':'column (1,1)','eligible_incoming_horn_cell':False,'reason':'formal classifier only'},
 {'object':'Cayley-Menger face','source_derived':False,'cochain_degree':None,'map':None,'eligible_incoming_horn_cell':False,'reason':'no CM boundary generator at the marked-wall collision'}]
 eligible=[x for x in inventory if x['source_derived'] and x['eligible_incoming_horn_cell']];assert eligible==[]
 out={'schema':'marici.voevodsky.cosmology-relative-horn-source-degree-inventory.v1','status':'no_current_source_cell_occupies_required_incoming_horn_degree','required_cell':{'cochain_degree':1,'differential_column_rows_Xi_minusSigma':[1,1]},'inventory':inventory,'eligible_sourced_cells':eligible,'typing_correction':'The preceding face-attachment/Bezout gates classify cells filling the boundary triangle. That job is already performed at residue level by sigma123. They do not construct the one-degree-lower preimage of the closed pair (Xi_log,-sigma123).','decision':'The present sourced degree-one domain is empty. No attachment-degree gcd can be formed for the actual horn until degree-one source cells with full carrier maps are constructed.','next_gate':'derive a degree-one source cell from a totalization mechanism (mapping cone, deformation-to-normal cone, or relative correspondence), not another boundary face','limitations':['inventory of currently materialized candidates','does not rule out a new totalization source cell','no Bockstein or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

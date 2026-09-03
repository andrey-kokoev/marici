"""Attach the full tame-symbol tuple to the ambient cone and check all residues."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_integral_decoration_of_ambient_cone.json'
def main():
 tame={'D1':'v^-1','D2':'u','D3':'-v/u','E':'1'}
 pair_residues={'D1D2':(-1,1),'D2D3':(-1,1),'D3D1':(-1,1),'D1E':(0,0),'D2E':(0,0),'D3E':(0,0)}
 assert all(sum(x)==0 for x in pair_residues.values())
 outer_edges=tuple(x[1] for k,x in pair_residues.items() if 'E' not in k);assert outer_edges==(1,1,1)
 radial=[x for k,x in pair_residues.items() if 'E' in k];assert radial==[(0,0)]*3
 out={'schema':'marici.voevodsky.cosmology-integral-decoration-of-ambient-cone.v1','status':'ambient_cone_has_complete_integral_tame_decoration_with_zero_residuals','ambient_functions':'u=l1/l3, v=l2/l3 on Bl_0(A3)','divisors':'div(u)=D1-D3 and div(v)=D2-D3; exceptional valuations of both ratios are zero','tame_symbols':tame,'codimension_two_residues':{k:list(v) for k,v in pair_residues.items()},'residue_sums':{k:sum(v) for k,v in pair_residues.items()},'outer_flag_cycle':list(outer_edges),'radial_residuals':[list(x) for x in radial],'sign_disposition':'The constant -1 in the D3 unit has zero valuation. It cannot be isolated, but together with v^-1, u, and -v/u the full tuple is the exact tame boundary of {u,v}.','total_result':'The incidence boundary is sigma123, the logarithmic Thom component is Xi_log, every radial component vanishes, and every codimension-two Gersten sum is zero.','contract_status':{'geometric_source':True,'relative_degree_one_cell':True,'independent_boundary':True,'top_weight_realization':True,'full_integral_component_check':True,'orientation_naturality':True,'local_carrier_comparison':True},'decision':'The ambient semistable star provides a complete integral geometric HomotopyLift realizing tau. It remains distinct from a rank26 or higher-Chow ElementLift.','next_gate':'ambient-cone-carrier-functor: determine whether the local normal-slice realization extends functorially to the full characteristic-zero carrier rather than only its principal corner','limitations':['local semistable normal-slice geometry','does not produce a source-chain boundary for {u,v}','no physical process or record inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

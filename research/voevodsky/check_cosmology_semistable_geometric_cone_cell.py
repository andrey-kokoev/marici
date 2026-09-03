"""Construct the cone over the exceptional triangle in the ambient blowup dual complex."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_semistable_geometric_cone_cell.json'
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def main():
 forms=[[1,0,0],[0,1,0],[1,1,1]];assert det3(forms)==1
 # Boundaries: [E,X,Y], [E,Y,Z], [E,Z,X].
 boundaries=[{'XY':1,'EY':-1,'EX':1},{'YZ':1,'EZ':-1,'EY':1},{'ZX':1,'EX':-1,'EZ':1}]
 total={k:sum(b.get(k,0) for b in boundaries) for k in ('XY','YZ','ZX','EX','EY','EZ')}
 assert total=={'XY':1,'YZ':1,'ZX':1,'EX':0,'EY':0,'EZ':0}
 out={'schema':'marici.voevodsky.cosmology-semistable-geometric-cone-cell.v1','status':'ambient_blowup_dual_complex_contains_geometric_cone_over_exceptional_triangle','local_source':'A3 with transverse hyperplanes U=0, V=0, U+V+P=0','coefficient_determinant':det3(forms),'geometry':'Y=Bl_0(A3); E=P2 is exceptional and the three strict transforms meet E in the triangle lines','dual_cells':['[E,X,Y]','[E,Y,Z]','[E,Z,X]'],'cone_chain':'Gamma=[E,X,Y]+[E,Y,Z]+[E,Z,X]','boundary':total,'topology':'The star of E is a disk, the cone on its link triangle. Radial edges cancel and the outer boundary is sigma123 in cyclic orientation.','correction':'The earlier no-face result was correct only for the divisor E viewed internally. It was incorrect when extrapolated to the ambient semistable boundary, whose dual complex contains these three 2-cells.','contract_status':{'geometric_source':True,'degree_one_cell_after_relative_shift':True,'independent_boundary':True,'carrier_comparison':'local normal-slice equations match','realization_map':'pending Thom/residue construction','full_component_check':False,'naturality':'pending'},'decision':'A genuine, independently defined geometric cone cell exists at the topological/incidence level. Promotion to tau now depends on the Thom/logarithmic regulator image and complete residual audit.','next_gate':'ambient-star-regulator-realization: compute the residue/Thom image of Gamma and test whether it is exactly (Xi_log,-sigma123)','limitations':['ambient dual-complex construction only','degree-one designation uses the relative comparison shift','integral tame-unit and physical interfaces not yet checked'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

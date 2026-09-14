#!/usr/bin/env python3
"""Exact hostile: signed-exchange symmetry permits indefinite Hermitian forms."""
import json
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(A):return [list(x) for x in zip(*A)]
def q(G,v):return sum(v[i]*G[i][j]*v[j] for i in range(2) for j in range(2))
def main():
 J=[[0,-1],[-1,0]];G=[[1,2],[2,1]]
 assert mm(mm(tr(J),G),J)==G
 fixed=[1,-1];mobius=[1,1]
 assert q(G,fixed)==-2 and q(G,mobius)==6
 # Reversing the cross sign moves the negative direction to the Mobius eigenline.
 H=[[1,-2],[-2,1]]
 assert mm(mm(tr(J),H),J)==H
 assert q(H,fixed)==6 and q(H,mobius)==-2
 result={'schema':'marici.voevodsky.mobius-symmetry-does-not-force-weil-positivity.v1','signed_exchange':J,'fixed_channel_vector':fixed,'mobius_channel_vector':mobius,'hostile_forms':[G,H],'both_forms_J_invariant':True,'first_negative_sector':'fixed line','second_negative_sector':'Mobius line','conclusion':'Orientation-reversing channel monodromy constrains transport but does not force positivity on either eigenchannel.','typing_warning':'Channel basis indices and Gaussian translate packet indices are different sorts; a rank-two numerical coincidence does not identify them.','rh_consequence':'No Weil Gram minor follows from the Mobius theorem without a source-derived intertwiner carrying the Weil form.'}
 out=Path(__file__).parents[1]/'results'/'mobius_symmetry_does_not_force_weil_positivity.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

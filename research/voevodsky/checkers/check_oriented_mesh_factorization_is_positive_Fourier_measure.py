#!/usr/bin/env python3
"""Exact finite audit: coherent phase-labelled cells are a positive Fourier factorization."""
import json,cmath,math
from pathlib import Path

def gram(weights,angles,n):return [[sum(w*cmath.exp(1j*(i-j)*t) for w,t in zip(weights,angles)) for j in range(n)] for i in range(n)]
def q(G,c):return sum(c[i].conjugate()*G[i][j]*c[j] for i in range(len(c)) for j in range(len(c))).real
def main():
 weights=[1.0,2.0,0.5];angles=[0,2*math.pi/3,math.pi];G=gram(weights,angles,5)
 probes=[[1,0,2,-1,3],[1,-1,1,-1,1],[0,1,1j,2,0]];vals=[q(G,[complex(x) for x in c]) for c in probes];assert all(v>=-1e-12 for v in vals)
 bad=gram([1.0,-2.0],[0,math.pi],2);badval=q(bad,[1, -1]);assert badval<0
 result={'schema':'marici.voevodsky.oriented-mesh-positive-Fourier-factorization.v1','phase_law':'s_a(alpha)=exp(i a theta_alpha), so s_(a+b)=s_a s_b and s_(-a)=conj(s_a)','kernel':'K(a-b)=sum_alpha c_alpha exp(i(a-b)theta_alpha)','positive_weights_fixture_quadratic_values':vals,'signed_weight_hostile_value':badval,'theorem':'A translation-coherent oriented cell factorization with positive weights is exactly a positive Fourier/Bochner factorization and therefore gives every Gram rank at once. Conversely, circle positivity supplies such a factorization by Herglotz.','rh_boundary':'For the source circle pushforward, constructing positive weights is the original positivity gate; orientation phases solve sign-changing cross-pairings but do not prove weight positivity.'}
 out=Path(__file__).parents[1]/'results'/'oriented_mesh_positive_Fourier_factorization.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'positive_values':vals,'signed_hostile':badval},indent=2))
if __name__=='__main__':main()

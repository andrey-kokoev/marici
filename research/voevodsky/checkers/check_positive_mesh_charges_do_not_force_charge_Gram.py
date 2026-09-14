#!/usr/bin/env python3
"""Exact hostile: individually positive mesh sources need not form a positive Gram matrix."""
import json
from fractions import Fraction
from pathlib import Path

def q(A,x):return sum(x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def main():
 C=[[Fraction(1),Fraction(2)],[Fraction(2),Fraction(1)]]
 assert all(x>0 for row in C for x in row)
 witness=[1,-1];val=q(C,witness);det=C[0][0]*C[1][1]-C[0][1]**2
 assert val<0 and det<0
 result={'schema':'marici.voevodsky.positive-mesh-charges-not-charge-Gram.v1','charge_matrix':[[str(x) for x in row] for row in C],'every_mesh_charge_positive':True,'determinant':str(det),'negative_witness':witness,'negative_value':str(val),'charge_matrix_psd':False,'theorem':'Entrywise positivity C_ij>0 of discrete-wave sources does not imply positive semidefiniteness of the matrix [C_ij].','implication_for_RH':'The associahedral positive-source condition does not by itself establish positivity of the zero-sum Weil block. A common-carrier or Schwarz inequality |C_ij|^2<=C_ii C_jj is still required.'}
 out=Path(__file__).parents[1]/'results'/'positive_mesh_charges_do_not_force_charge_Gram.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

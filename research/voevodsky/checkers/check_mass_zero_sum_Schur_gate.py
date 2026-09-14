#!/usr/bin/env python3
"""Exact audit of the mass/zero-sum Schur complement gate."""
import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def inv2(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0];return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def main():
 r=Fraction(-3,5);G=[[Fraction(1) if i==j else r for j in range(3)] for i in range(3)]
 # Columns: anchor e0, zero-sum increments e1-e0,e2-e0.
 B=[[1,-1,-1],[0,1,0],[0,0,1]];H=mm(mm(tr(B),G),B);a=H[0][0];b=H[0][1:];C=[row[1:] for row in H[1:]]
 Ci=inv2(C);correction=sum(b[i]*Ci[i][j]*b[j] for i in range(2) for j in range(2));schur=a-correction
 assert C[0][0]>0 and C[0][0]*C[1][1]-C[0][1]**2>0 and schur<0
 result={'schema':'marici.voevodsky.mass-zero-sum-Schur-gate.v1','basis':['anchor mass e0','e1-e0','e2-e0'],'transformed_Gram':[[str(x) for x in row] for row in H],'mass_scalar':str(a),'mass_zero_sum_cross':[str(x) for x in b],'zero_sum_block':[[str(x) for x in row] for row in C],'Schur_correction':str(correction),'Schur_margin':str(schur),'zero_sum_block_positive':True,'full_packet_positive':False,'general_gate':'C>=0, b in ran(C), and a-b*C^dagger*b>=0','interpretation':'Mesh-charge positivity supplies C. Endpoint/archimedean mass positivity supplies a. Rung-four incidence must control b by the Schur inequality.'}
 out=Path(__file__).parents[1]/'results'/'mass_zero_sum_Schur_gate.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact visible/hidden block test for first-order metric tomography."""
import json
from fractions import Fraction
from pathlib import Path
import check_constrained_green_anomaly_lift as lin

def outer(a,b):return [[x*y for y in b] for x in a]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def leakage(K,A,P,G,u):
 raw=lin.mv(lin.inv(K),lin.mv(G,u));pr=lin.mv(P,raw);return [-(x-y) for x,y in zip(raw,pr)]
def main():
 n=7;rho=Fraction(1,2);K=[[rho**abs(i-j) for j in range(n)] for i in range(n)];A=[K[-1],K[0]];X=lin.inv(K);R=lin.mm(X,lin.tr(A));H=lin.mm(A,R);Hi=lin.inv(H);P=lin.mm(R,lin.mm(Hi,A));visible=[lin.mv(R,lin.mv(Hi,d)) for d in ([Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)])]
 cols=(0,3,6);C=[[A[q][i] for i in cols] for q in range(2)];z=[C[0][1]*C[1][2]-C[0][2]*C[1][1],C[0][2]*C[1][0]-C[0][0]*C[1][2],C[0][0]*C[1][1]-C[0][1]*C[1][0]];h=[Fraction(0)]*n
 for i,x in zip(cols,z):h[i]=x
 assert lin.mv(A,h)==[0,0]
 v=visible[0];Kh=lin.mv(K,h);Kv=lin.mv(K,v);Ghh=outer(Kh,Kh);Gvv=outer(Kv,Kv);Ghv=add(outer(Kh,Kv),outer(Kv,Kh))
 assert all(all(x==0 for x in leakage(K,A,P,Ghh,u)) for u in visible)
 assert all(all(x==0 for x in leakage(K,A,P,Gvv,u)) for u in visible)
 observed=[leakage(K,A,P,Ghv,u) for u in visible];assert any(any(x for x in row) for row in observed)
 result={'schema':'marici.coherence.first-order-metric-tomography-limit.v1','state_dimension':n,'visible_dimension':2,'hidden_dimension':n-2,'maximum_cross_block_parameters':2*(n-2),'hidden_hidden_perturbation_invisible':True,'visible_visible_perturbation_invisible':True,'visible_hidden_cross_perturbation_detected':True,'conclusion':'first-order boundary-target tomography identifies only the metric cross block coupling the two-dimensional visible sector to the boundary-invisible kernel'}
 Path(__file__).with_name('first-order-metric-tomography-limit.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

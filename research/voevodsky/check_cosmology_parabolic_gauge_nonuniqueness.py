"""Exhibit two distinct coherent parabolic stationary gauges."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_parabolic_gauge_nonuniqueness.json'
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def make_p(v,w,shift):
 u=v[1:];z=w[1:];rr=[-u[1],u[0]];ss=[-z[1]+shift*z[0],z[0]+shift*z[1]];U=[[u[0],rr[0]],[u[1],rr[1]]];W=[[z[0],ss[0]],[z[1],ss[1]]];du=U[0][0]*U[1][1]-U[0][1]*U[1][0];Ui=[[U[1][1]/du,-U[0][1]/du],[-U[1][0]/du,U[0][0]/du]];B=[[sum(W[i][k]*Ui[k][j] for k in range(2)) for j in range(2)] for i in range(2)];r1=(w[0]-v[0])/v[1] if v[1] else 0;r2=0 if v[1] else (w[0]-v[0])/v[2];return [[Fraction(1),Fraction(r1),Fraction(r2)],[0,B[0][0],B[0][1]],[0,B[1][0],B[1][1]]]
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());C1=[[t.q(x) for x in r] for r in a['change_matrix']];C2=[[t.q(x) for x in r] for r in b['transition_matrix']];e=[Fraction(1),0,0];v=mv(t.inv(C2),e);w=mv(t.inv(C1),e);solutions=[]
 for shift in (0,1):
  p=make_p(v,w,shift);assert mv(p,v)==w;S=t.mm(p,C1);G2=t.mm(t.mm(S,p),t.inv(C2));assert G2[1][0]==G2[2][0]==0 and t.mm(t.mm(G2,C2),t.inv(p))==S;solutions.append((p,S,G2))
 assert solutions[0][0]!=solutions[1][0] and solutions[0][1]!=solutions[1][1]
 out={'schema':'marici.voevodsky.cosmology-parabolic-gauge-nonuniqueness.v1','status':'distinct_coherent_gauges_exhibited','gauge_count':2,'stationary_matrices_distinct':True,'decision':'Two exact coherent parabolic gauge sequences, produced by different rational complement choices, yield distinct stationary matrices.','claim_boundary':'Nonuniqueness does not prove that no additional source datum could select one; none is present in the current construction.','next_gate':'record-detector-stationarity-as-gauge-only-equivalence','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

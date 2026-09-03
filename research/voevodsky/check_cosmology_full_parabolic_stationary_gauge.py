"""Construct a coherent two-step stationary gauge in the full constant-line parabolic."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_full_parabolic_stationary_gauge.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());C1=[[t.q(x) for x in r] for r in a['change_matrix']];C2=[[t.q(x) for x in r] for r in b['transition_matrix']];e=[Fraction(1),Fraction(0),Fraction(0)];v=mv(t.inv(C2),e);w=mv(t.inv(C1),e);assert any(v[1:]) and any(w[1:])
 u=v[1:];z=w[1:];U=[[u[0],-u[1]],[u[1],u[0]]];W=[[z[0],-z[1]],[z[1],z[0]]];du=U[0][0]*U[1][1]-U[0][1]*U[1][0];Ui=[[U[1][1]/du,-U[0][1]/du],[-U[1][0]/du,U[0][0]/du]];B=[[sum(W[i][k]*Ui[k][j] for k in range(2)) for j in range(2)] for i in range(2)];r1=(w[0]-v[0])/v[1] if v[1] else Fraction(0);r2=Fraction(0) if v[1] else (w[0]-v[0])/v[2];p=[[Fraction(1),r1,r2],[0,B[0][0],B[0][1]],[0,B[1][0],B[1][1]]];assert mv(p,v)==w and t.det(p);S=t.mm(p,C1);G2=t.mm(t.mm(S,p),t.inv(C2));assert G2[1][0]==G2[2][0]==0 and t.det(G2);left=t.mm(p,C1);right=t.mm(t.mm(G2,C2),t.inv(p));assert left==right==S
 out={'schema':'marici.voevodsky.cosmology-full-parabolic-stationary-gauge.v1','status':'coherent_two_step_stationary_gauge_constructed','middle_gauge':[[enc(x) for x in r] for r in p],'terminal_gauge':[[enc(x) for x in r] for r in G2],'stationary_matrix':[[enc(x) for x in r] for r in S],'decision':'An exact rational ambient-indexed parabolic gauge makes both detector transitions equal to one shared flag-moving matrix.','claim_boundary':'The construction is nonunique and algebraically chosen; no source-derived normalization or all-step recurrence follows.','next_gate':'seek-source-derived-parabolic-gauge-or-record-gauge-only-equivalence','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('middle_gauge','terminal_gauge','stationary_matrix')},indent=2))
if __name__=='__main__':main()

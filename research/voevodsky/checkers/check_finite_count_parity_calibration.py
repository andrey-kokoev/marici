#!/usr/bin/env python3
"""Verify exact finite-count inversion and parity recovery under calibrated loss/dark response."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
from sympy import kronecker_product
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/finite_count_calibration_recovers_the_two_parity_syndromes.md';COUNT=ROOT/'research/aspect/calibrated-photon-counting-intensity-statistics.md';PARITY=ROOT/'research/voevodsky/results/pairwise_photon_parity_probe.json';RESULT=ROOT/'research/voevodsky/results/finite_count_parity_calibration.json';eta=s.Rational(9,25);d=s.Rational(1,10);N=2
def response(eta,d):
 R=s.zeros(N+2,N+1)
 for m in range(N+2):
  for n in range(N+1):
   b=lambda k:s.binomial(n,k)*eta**k*(1-eta)**(n-k) if 0<=k<=n else 0
   R[m,n]=s.simplify((1-d)*b(m)+d*b(m-1))
 return R
R=response(eta,d);A=R[:3,:];L=A.inv().row_join(s.zeros(3,1));R3=kronecker_product(R,R,R);L3=kronecker_product(L,L,L);threshold=s.Matrix([[1,1,1],[0,0,0]])
# Actual threshold no-click probabilities after loss/dark; click is complement.
no=s.Matrix([[(1-d)*(1-eta)**n for n in range(3)]]);Thr=no.col_join(s.ones(1,3)-no);Rzero=response(s.Rational(0),d);text=PACKET.read_text(encoding='utf-8');count=COUNT.read_text(encoding='utf-8');parity=json.loads(PARITY.read_text(encoding='utf-8'));checks={'source_parameters':'n=2' in count and 'eta=9/25' in count and 'd=1/10' in count,'response_exact':R==s.Matrix([[s.Rational(9,10),s.Rational(72,125),s.Rational(1152,3125)],[s.Rational(1,10),s.Rational(97,250),s.Rational(1424,3125)],[0,s.Rational(9,250),s.Rational(1017,6250)],[0,0,s.Rational(81,6250)]]),'top_minor_nonzero':s.factor(A.det())==s.Rational(531441,15625000),'left_inverse_exact':L*R==s.eye(3),'joint_rank_27':R3.rank()==27,'joint_left_inverse':L3*R3==s.eye(27),'parity_observables_prior':parity['checks']['kernel_equals_J_image'],'threshold_rank_defect':Thr.rank()<3,'zero_efficiency_rank_one':Rzero.rank()==1,'scope_gate':'does not cover afterpulsing, dead time, correlated backgrounds, or actual data' in text,'remaining_encoder':'encoder from conductor coordinates to source occupations' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.finite-count-parity-calibration.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'counting_source_sha256':sha256(COUNT.read_bytes()).hexdigest(),'parity_result_sha256':sha256(PARITY.read_bytes()).hexdigest(),'single_response':[[str(x) for x in R.row(i)] for i in range(4)],'single_left_inverse':[[str(x) for x in L.row(i)] for i in range(3)],'joint_response_shape':[64,27],'joint_rank':R3.rank(),'checks':checks,'passed':all(checks.values()),'disposition':{'finite_calibration':'invertible exactly','threshold_only':'insufficient','zero_efficiency':'insufficient','raw_data':'missing','conductor_encoder':'missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

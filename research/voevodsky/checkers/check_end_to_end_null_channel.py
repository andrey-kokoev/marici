#!/usr/bin/env python3
"""Exact end-to-end synthetic test of encoder, response, inverse, and parity decoder."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy import kronecker_product as kron
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/end_to_end_synthetic_null_channel_acceptance_test.md';ENC=ROOT/'research/voevodsky/results/single_rail_conductor_encoder.json';CAL=ROOT/'research/voevodsky/results/finite_count_parity_calibration.json';RESULT=ROOT/'research/voevodsky/results/end_to_end_null_channel.json';N=2;d=s.Rational(1,10)
def response(eta):
 R=s.zeros(4,3)
 for m in range(4):
  for n in range(3):
   bn=lambda k:s.binomial(n,k)*eta**k*(1-eta)**(n-k) if 0<=k<=n else 0
   R[m,n]=s.simplify((1-d)*bn(m)+d*bn(m-1))
 return R
def inverse(R):return R[:3,:].inv().row_join(s.zeros(3,1))
R=response(s.Rational(9,25));L=inverse(R);R3=kron(R,R,R);L3=kron(L,L,L);Lwrong3=kron(inverse(response(s.Rational(2,5))),inverse(response(s.Rational(2,5))),inverse(response(s.Rational(2,5))));occup=list(product(range(3),repeat=3));idx={n:i for i,n in enumerate(occup)};records=[]
for a,b in product((0,1),repeat=2):
 p=s.zeros(27,1);p[idx[(a,b,0)]]=1;q=R3*p;rec=s.simplify(L3*q);wrong=s.simplify(Lwrong3*q);o1=sum(((-1)**(n[0]+n[2]))*rec[i] for i,n in enumerate(occup));o2=sum(((-1)**(n[1]+n[2]))*rec[i] for i,n in enumerate(occup));records.append({'class':[a,b],'exact_residual_zero':rec==p,'decoded_signs':[int(o1),int(o2)],'decoded_bits':[int((1-o1)/2),int((1-o2)/2)],'wrong_calibration_residual_zero':wrong==p})
enc=json.loads(ENC.read_text(encoding='utf-8'));cal=json.loads(CAL.read_text(encoding='utf-8'));text=PACKET.read_text(encoding='utf-8');checks={'prior_encoder':enc['passed'],'prior_calibration':cal['passed'],'all_exact_recoveries':all(x['exact_residual_zero'] for x in records),'all_classes_decoded':all(x['decoded_bits']==x['class'] for x in records),'vacuum_trivial':records[0]['decoded_bits']==[0,0],'nontrivial_distinct':len({tuple(x['decoded_bits']) for x in records})==4,'wrong_efficiency_fails_nontrivial':all(not x['wrong_calibration_residual_zero'] for x in records if x['class']!=[0,0]),'synthetic_scope':'not experimental evidence' in text,'acquisition_criterion':'held-out prepared codewords reconstruct within a preregistered error bound' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.end-to-end-null-channel.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'encoder_result_sha256':sha256(ENC.read_bytes()).hexdigest(),'calibration_result_sha256':sha256(CAL.read_bytes()).hexdigest(),'class_tests':records,'checks':checks,'passed':all(checks.values()),'disposition':{'synthetic_channel':'passes all four classes','mismatched_calibration':'nonzero residual on every nontrivial class','physical_preparation_and_acquisition':'missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'class_tests':records,'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

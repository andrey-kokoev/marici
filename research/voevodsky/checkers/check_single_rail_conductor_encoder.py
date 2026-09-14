#!/usr/bin/env python3
"""Verify the site-equivariant single-rail encoder and pair-parity readout."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/a_single_rail_fock_encoder_realizes_the_conductor_syndrome_quotient.md';PARITY=ROOT/'research/voevodsky/results/pairwise_photon_parity_probe.json';CAL=ROOT/'research/voevodsky/results/finite_count_parity_calibration.json';RESULT=ROOT/'research/voevodsky/results/single_rail_conductor_encoder.json';basis=list(product((0,1),repeat=3));logical=list(product((0,1),repeat=2));idx={v:i for i,v in enumerate(basis)};E=s.zeros(8,4)
for j,(a,b) in enumerate(logical):E[idx[(a,b,0)],j]=1
O1=s.diag(*[(-1)**(n[0]+n[2]) for n in basis]);O2=s.diag(*[(-1)**(n[1]+n[2]) for n in basis]);Z1=s.diag(*[(-1)**a for a,b in logical]);Z2=s.diag(*[(-1)**b for a,b in logical]);Uf=s.zeros(8);Ul=s.zeros(4)
for n in basis:Uf[idx[(n[1],n[0],n[2])],idx[n]]=1
for j,(a,b) in enumerate(logical):Ul[logical.index((b,a)),j]=1
text=PACKET.read_text(encoding='utf-8');parity=json.loads(PARITY.read_text(encoding='utf-8'));cal=json.loads(CAL.read_text(encoding='utf-8'));checks={'encoder_isometry':E.T*E==s.eye(4),'parity_one_intertwining':O1*E==E*Z1,'parity_two_intertwining':O2*E==E*Z2,'site_exchange_intertwining':Uf*E==E*Ul,'vacuum_is_state':E[:,0].dot(E[:,0])==1 and E[idx[(0,0,0)],0]==1,'four_distinct_codewords':E.rank()==4,'prior_parity_probe':parity['passed'],'prior_calibration':cal['passed'],'gauge_disclaimer':'is a section of the syndrome map, not a source-derived necessity' in text,'preparation_gate':'remaining physical gate is an authorized preparation mechanism' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.single-rail-conductor-encoder.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'parity_result_sha256':sha256(PARITY.read_bytes()).hexdigest(),'calibration_result_sha256':sha256(CAL.read_bytes()).hexdigest(),'logical_basis':[list(v) for v in logical],'fock_codewords':{str(v):list((v[0],v[1],0)) for v in logical},'checks':checks,'passed':all(checks.values()),'disposition':{'finite_encoder':'constructed','exchange_equivariance':'verified','null_syndrome':'normalized vacuum state','physical_preparation':'missing','raw_data':'missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

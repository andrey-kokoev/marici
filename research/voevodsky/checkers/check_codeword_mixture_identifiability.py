#!/usr/bin/env python3
"""Verify exact recovery of four codeword mixture weights from conclusive events."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/conclusive_two_count_events_identify_codeword_mixtures.md';LIKE=ROOT/'research/voevodsky/results/direct_codeword_likelihood_bound.json';RESULT=ROOT/'research/voevodsky/results/codeword_mixture_identifiability.json';c=s.Rational(9,250);tests=[[s.Rational(1),0,0,0],[0,s.Rational(1),0,0],[0,0,s.Rational(1),0],[0,0,0,s.Rational(1)],[s.Rational(1,10),s.Rational(2,10),s.Rational(3,10),s.Rational(4,10)],[s.Rational(1,4)]*4]
def events(w):
 w00,w01,w10,w11=w;return c*(w10+w11),c*(w01+w11),c*c*w11
def recover(r):
 r1,r2,r12=r;w11=r12/c**2;w10=r1/c-w11;w01=r2/c-w11;w00=1-w10-w01-w11;return [s.factor(x) for x in [w00,w01,w10,w11]]
records=[{'input':[str(x) for x in w],'events':[str(x) for x in events(w)],'recovered':[str(x) for x in recover(events(w))],'exact':recover(events(w))==w} for w in tests];like=json.loads(LIKE.read_text(encoding='utf-8'));text=PACKET.read_text(encoding='utf-8');# Exchange permutation in order 00,01,10,11.
def swapw(w):return [w[0],w[2],w[1],w[3]]
def swapr(r):return (r[1],r[0],r[2])
checks={'prior_likelihood_model':like['passed'],'conclusive_probability':c==s.Rational(9,250),'all_test_mixtures_recovered':all(x['exact'] for x in records),'vertex_recognition':all(sum(x!=0 for x in w)==1 for w in tests[:4]) and all(sum(x!=0 for x in w)>1 for w in tests[4:]),'exchange_equivariance':all(recover(swapr(events(w)))==swapw(w) for w in tests),'rare_joint_event':c*c==s.Rational(81,62500),'classical_scope':'arbitrary classical mixtures' in text,'coherence_gate':'cannot distinguish a coherent superposition' in text,'finite_sample_missing':'does not provide a finite-sample confidence region' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.codeword-mixture-identifiability.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'likelihood_result_sha256':sha256(LIKE.read_bytes()).hexdigest(),'conclusive_single_probability':str(c),'conclusive_joint_probability':str(c*c),'mixture_tests':records,'checks':checks,'passed':all(checks.values()),'disposition':{'classical_mixture_weights':'exactly identifiable','fixed_codeword_test':'simplex vertex criterion','coherent_superposition':'not identifiable by count POVM','finite_sample_confidence':'missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

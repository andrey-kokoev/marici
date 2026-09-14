#!/usr/bin/env python3
"""Verify the local Bunch-Davies germ cannot order the exchanged paired thimbles."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/bunch_davies_boundary_germ_does_not_order_the_paired_thimbles.md'
PAIRED=ROOT/'research/nima/results/total-energy-paired-picard-lefschetz.json'
SCALED=ROOT/'research/nima/results/cosmology_triple_incidence_scaled_monodromy.json'
AUTH=ROOT/'research/nima/results/cosmology_post_candidate_authority_status.json'
MOD2=ROOT/'research/voevodsky/results/paired_thimble_mod2_collapse.json'
RESULT=ROOT/'research/voevodsky/results/bunch_davies_thimble_ordering_no_go.json'
x,y,E,t=s.symbols('x y E t',nonzero=True);z=E-x-y
F=s.expand(x**2*t**4-(x**2+y**2-z**2)*t**2+y**2)
nodejet=s.factor(s.diff(F,E).subs(E,0).subs(t**2,-y/x))
paired=json.loads(PAIRED.read_text(encoding='utf-8'));scaled=json.loads(SCALED.read_text(encoding='utf-8'));auth=json.loads(AUTH.read_text(encoding='utf-8'));mod2=json.loads(MOD2.read_text(encoding='utf-8'));text=PACKET.read_text(encoding='utf-8')
checks={'boundary_square':s.factor(F.subs(E,0))==(x*t**2+y)**2,'node_exchange_even':s.expand(F.subs(t,-t)-F)==0,'equal_node_jet':nodejet==2*y*(x+y)/x,'paired_source_two_nodes':paired['identities']['node_count']==2,'punctured_monodromy_trivial':scaled['local_picard_lefschetz_variation_rank']==0 and scaled['local_betti_monodromy']=='identity','no_mu2_odd_thimble':scaled['primitive_mu2_odd_thimble_generated_by_p_loop'] is False,'local_authority_only':auth['source_authorized_local_boundary_germ'] is True and auth['candidate_certifies_global_contour_authority'] is False,'mod2_local_direction_one':mod2['disposition']['local_exchange_data']=='one mod-two direction','ordering_refused':'cannot turn the unordered pair' in text,'global_marking_gate':'global ordered Picard marking remains' in text};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.bunch-davies-thimble-ordering-no-go.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'paired_sha256':sha256(PAIRED.read_bytes()).hexdigest(),'scaled_sha256':sha256(SCALED.read_bytes()).hexdigest(),'authority_sha256':sha256(AUTH.read_bytes()).hexdigest(),'mod2_sha256':sha256(MOD2.read_bytes()).hexdigest(),'common_node_jet':str(nodejet),'checks':checks,'passed':all(checks.values()),'disposition':{'local_boundary_germ':'source-authorized','paired_thimble_ordering':'not supplied','second_mod2_direction':'not supplied','remaining':'global based paths and integral Picard marking'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

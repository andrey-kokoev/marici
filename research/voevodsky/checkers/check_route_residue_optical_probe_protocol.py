#!/usr/bin/env python3
"""Deliberate pass/fail controls for the optical probe acceptance protocol."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/route_residue_optical_probe_acceptance_protocol_20260912.md'
RESULT=ROOT/'research/voevodsky/results/route_residue_optical_probe_protocol.json'
checks={}; t=s.Rational(2,3); D=s.diag(t,t**2,t**3); iota=s.eye(3); M=D; C=s.Matrix([[1,0,1],[0,1,1]]); Ctilde=C
checks['transfer_intertwining_pass']=M*iota-iota*D==s.zeros(3)
checks['detector_pullback_pass']=Ctilde*iota-C==s.zeros(2,3)
Edet=D.T*D; Eloss=s.eye(3)-Edet
checks['loss_normalization_pass']=Edet+Eloss==s.eye(3) and Eloss.is_positive_definite is True
checks['removed_loss_control_fails']=Edet!=s.eye(3)
Rhat=s.diag(2,1); eta=s.Rational(1,2); blind=s.diag(2,0)
checks['robust_singular_margin_pass']=min(Rhat.singular_values())>eta
checks['blind_direction_rejected']=not (min(blind.singular_values())>eta)
N=s.Matrix([[2,s.Rational(1,2)],[s.Rational(1,2),1]]); Q=Rhat.T*N.inv()*Rhat
checks['correlated_noise_positive']=N.is_positive_definite is True
checks['fisher_positive_on_response']=Q.is_positive_definite is True
# Perturbation larger than the certified margin invalidates robust admission.
checks['uncertainty_margin_control']=not (min(Rhat.singular_values())>s.Rational(3,2))
text=PACKET.read_text()
checks['preregistration_required']='before collecting the discriminating data' in text
checks['no_fitted_threshold']='no fitted detection threshold' in text
checks['all_gates_independent']='no other passing item repairs it' in text
checks['loss_conditioning_prohibited']='Do not renormalize detected events' in text
checks['missing_data_named']='calibrated transfer matrices, detector pullback data, loss counts, and joint noise samples' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.route-residue-optical-probe-protocol-check.v1','input_digest':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'disposition':{'protocol':'executable once calibrated apparatus data are supplied','controls':['exact intertwiner pass','detector pullback pass','loss omission fail','blind response fail','uncertainty margin fail'],'missing':'apparatus dataset'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)

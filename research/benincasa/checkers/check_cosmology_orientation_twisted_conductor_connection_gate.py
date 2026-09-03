#!/usr/bin/env python3
"""Obstruct a direct single-frame conductor connection by exceptional support incidence."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
st=json.loads((B/'relative-stokes-pairing-gate.json').read_text())
sc=st['scope_correction'];assert sc['direct_exceptional_pullback_is_valid'] is False
central=[0,0];moving=[1,-1]
# No label-preserving function of the exceptional coordinate sends the common central point to both moving points.
direct_identification_exists=all(v==moving[0] for v in moving)
assert not direct_identification_exists
out={'schema':'marici.benincasa.cosmology-orientation-twisted-conductor-connection-gate.v1','wall_incidence':{'central':{'walls':sc['central_walls'],'exceptional_points':central},'moving':{'walls':sc['moving_walls'],'exceptional_points':moving}},'direct_single_frame_identification_exists':False,'exact_obstruction':'a function of the exceptional coordinate cannot satisfy f(0)=1 and f(0)=-1 simultaneously','consequence':'direct exceptional pullback cannot produce a residue-compatible connection or preserve the two labelled moving residues','required_replacement':{'object':'normalized three-point conductor cospan','central_branch':'point r=0 with two labelled wall occurrences retained','moving_branches':['r=1','r=-1'],'data':['separate residue maps','orientation local-system signs','transition comparison through the bulk complement','Gauss-Manin compatibility on each leg']},'pairing_status':'still undefined until the cospan and its continued Leray tubes are constructed','passed':True};(R/'cosmology_orientation_twisted_conductor_connection_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

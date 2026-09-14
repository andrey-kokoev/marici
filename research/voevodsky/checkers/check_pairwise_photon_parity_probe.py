#!/usr/bin/env python3
"""Verify pairwise photon-count parities realize the two conductor syndromes."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/two_pairwise_photon_parities_realize_the_complementary_syndrome_probe.md'
COUNT=ROOT/'research/aspect/calibrated-photon-counting-intensity-statistics.md'
PROBE=ROOT/'research/voevodsky/results/minimal_cut_null_complementary_probe.json'
SOURCE=ROOT/'research/benincasa/primitive-conductor-top-connection.json'
RESULT=ROOT/'research/voevodsky/results/pairwise_photon_parity_probe.json'
J=s.Matrix(json.loads(SOURCE.read_text(encoding='utf-8'))['enhanced_intertwiner_J']);L=s.Matrix([[1,0,1],[0,1,1]])
syndrome=lambda n:tuple(int(x)%2 for x in L*s.Matrix(n))
records=list(product(range(5),repeat=3));classes={a:[n for n in records if syndrome(n)==a] for a in product((0,1),repeat=2)}
image_mod2={tuple(int(x)%2 for x in J*s.Matrix(v)) for v in product((0,1),repeat=3)}
kernel={v for v in product((0,1),repeat=3) if syndrome(v)==(0,0)}
swap=lambda n:(n[1],n[0],n[2]);count=COUNT.read_text(encoding='utf-8');text=PACKET.read_text(encoding='utf-8')
checks={
 'number_resolving_source':'ideal number-resolving detector uses' in count and 'effects `Pi_n=|n><n|`' in count,
 'four_nonempty_effect_classes':len(classes)==4 and all(classes.values()),
 'finite_partition':sum(len(v) for v in classes.values())==len(records) and len(set().union(*(set(v) for v in classes.values())))==len(records),
 'syndrome_surjective':set(syndrome(v) for v in product((0,1),repeat=3))==set(product((0,1),repeat=2)),
 'kernel_equals_J_image':kernel==image_mod2,
 'site_swap':all(syndrome(swap(n))==tuple(reversed(syndrome(n))) for n in records),
 'elementary_records_distinguished':syndrome((1,0,0))==(1,0) and syndrome((0,1,0))==(0,1),
 'no_raw_parity_constraint':'No same-parity constraint is imposed on raw records' in text,
 'noise_gate':'response must be calibrated and shown invertible' in text,
 'encoder_gate':'remaining missing arrow is an encoder' in text,
}
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.pairwise-photon-parity-probe.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'counting_source_sha256':sha256(COUNT.read_bytes()).hexdigest(),'probe_result_sha256':sha256(PROBE.read_bytes()).hexdigest(),'conductor_source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'observables':['(-1)^(n1+n3)','(-1)^(n2+n3)'],'finite_cutoff_test':{'counts_per_channel':'0..4','record_count':len(records),'class_sizes':{str(k):len(v) for k,v in classes.items()}},'checks':checks,'passed':all(checks.values()),'disposition':{'binary_POVM_coarse_graining':'constructed','site_exchange':'verified','conductor_to_optical_encoder':'missing','physical_calibration_data':'missing'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)

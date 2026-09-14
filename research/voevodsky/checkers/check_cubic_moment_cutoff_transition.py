#!/usr/bin/env python3
"""Checks the recorded depth transition and its rational/modular boundary."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/cubic_moment_channel_is_first_modularly_full_at_cutoff_15360_20260912.md'
CENSUS=ROOT/'research/voevodsky/results/modulation_moment_channel_growth.json'
RESULT=ROOT/'research/voevodsky/results/cubic_moment_cutoff_transition.json'
d=json.loads(CENSUS.read_text()); checks={}
for L,expected in ((960,2),(1920,2),(3840,2),(7680,2),(15360,3),(30720,3)):
 records=d['census'][str(L)]['records']
 checks[f'depth_{L}']=all(r['shell_max_power']==expected and r['scale_max_power']==expected for r in records)
 checks[f'moduli_agree_{L}']=len({(tuple(r['shell_ranks']),tuple(r['scale_ranks'])) for r in records})==1
for L,deficiency in ((15360,2),(30720,7)):
 entry=d['census'][str(L)]; checks[f'quadratic_modular_deficiency_{L}']=all(entry['edges']-r['shell_ranks'][2]==deficiency and entry['edges']-r['scale_ranks'][2]==deficiency for r in entry['records'])
 checks[f'cubic_modular_full_rank_{L}']=all(r['shell_ranks'][3]==entry['edges'] and r['scale_ranks'][3]==entry['edges'] for r in entry['records'])
text=PACKET.read_text(); checks['rational_boundary_stated']='Modular deficiency alone is not an exact rational countercycle' in text
checks['full_mod_rank_force_correct']='modular full rank does prove rational full rank' in text
checks['prior_stability_withdrawn']='Withdraw the reported stability of maximum power two' in text
checks['countable_family_not_completed']='plausible completed probe family' in text and 'completed continuity and lower-frame problem is separate' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cubic-moment-cutoff-transition-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'census':hashlib.sha256(CENSUS.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'certified':'cubic stacks rationally full rank at cutoffs 15360 and 30720','modular_only':'quadratic deficiencies 2 and 7','supersedes':'cutoff-independent depth-two conjecture'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)

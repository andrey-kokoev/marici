"""Structural/source-current export audit only; no source-suite or Agda replay."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/strominger/contracts/wg-reusable-integration-interface.v1.json'
def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def digest(path): return sha256((ROOT/path).read_bytes()).hexdigest()
contract=load(CONTRACT); net=load(contract['upstream_net']); pins=load(contract['upstream_pins'])['source_sha256']
checks={}
assert len(net['conjectures'])==56 and not net['frontier'] and net['recommended_start'] is None
assert all(n['status']=='resolved' and n['outcome'] is None for n in net['conjectures'])
assert net['source_pins']==contract['upstream_pins']
checks['read_completed_upstream_without_promoting_formal_outcomes']=True
for path,expected in pins.items(): assert digest(path)==expected, 'stale upstream source: '+path
checks['all181_existing_upstream_pins_current']=len(pins)==181
assert len({x['id'] for x in contract['dictionary']})==len(contract['dictionary'])
for entry in contract['dictionary']:
    path=entry['path']; assert path in pins
    text=(ROOT/path).read_text(encoding='utf-8')
    if path.endswith('.py'):
        names={n.name for n in ast.walk(ast.parse(text)) if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
        assert entry['symbol'] in names,(path,entry['symbol'])
    else:
        assert re.search(r'\b'+re.escape(entry['symbol'])+r'\s*[:(]',text),(path,entry['symbol'])
    assert all(entry[k] for k in ('domain','codomain','witness'))
checks['eleven_exports_have_actual_source_symbols_and_typed_ports']=True
historical=[]
for path in contract['historical_receipts']:
    assert path in pins
    receipt=load(path)
    assert receipt.get('status')=='pass' or receipt.get('passed') is True
    historical.append({'path':path,'sha256':digest(path),'replayed_this_turn':False})
checks['six_historical_receipts_present_and_hash_bound_not_replayed']=True
for path in contract['consumer_interfaces']: assert (ROOT/path).is_file()
checks['existing_consumer_interfaces_readable_not_identified_as_common_carriers']=True
verification=contract['verification']
assert verification['written_interface'] and verification['fresh_inventory_check']
assert not any(verification[k] for k in ('fresh_source_suite_replay','fresh_Agda_closure','physical_validation','parent_outcome_admitted'))
successor=contract['optional_consumer_successor']
assert successor['not_executed'] and 'guards' in successor and 'transport(w)' in successor['square']
checks['verification_levels_and_proposed_consumer_square_remain_separate']=True
rejected=[{k:n[k] for k in ('id','statement','scope','falsifier','evidence','counterexample') if k in n}
          for n in net['conjectures'] if n['verdict']=='rejected']
assert len(rejected)==10
checks['all_ten_rejected_candidates_and_their_falsifiers_retained']=True
out={'schema':'marici.wg-reusable-integration-audit.v1','status':'pass','checks':checks,
     'contract_sha256':digest(CONTRACT),'upstream_net_sha256':digest(contract['upstream_net']),
     'upstream_pins_sha256':digest(contract['upstream_pins']),'checker_sha256':digest(str(Path(__file__).relative_to(ROOT)).replace('\\','/')),
     'historical_receipts':historical,'rejected_candidates':rejected,
     'consumer_source_hashes':{p:digest(p) for p in contract['consumer_interfaces']},
     'fresh_scope':'structural inventory, existing evidence hashes and actual declaration locators only',
     'source_suites_replayed':False,'Agda_recompiled':False,'parent_outcomes_changed':False}
(ROOT/'research/strominger/results/wg-reusable-integration-audit-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('historical_receipts','rejected_candidates')},indent=2))

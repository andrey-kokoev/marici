"""Validate existing fresh receipt, with fail-closed controls; no compiler run."""
import copy
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
RECEIPT=ROOT/'research/sontag/results/agda-RetainedHistoryTransport.json'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def validate(r):
    if r.get('passed') is not True or r.get('exit_code')!=0 or r.get('inputs_stable') is not True:
        raise ValueError('unsuccessful or unstable compiler receipt')
    if r.get('ignore_interfaces') is not True or '--ignore-interfaces' not in r['args']:
        raise ValueError('incremental receipt')
    for flag in ('--safe','--cubical','--guardedness'):
        if flag not in r['args']: raise ValueError('missing safe flag')
    if r['compiler_sha256']!=sha(r['args'][0]): raise ValueError('compiler drift')
    if r['source_sha256']!=sha(ROOT/'research/sontag/agda/RetainedHistoryTransport.agda'): raise ValueError('source drift')
    if r['checker_sha256']!=sha(ROOT/'research/sontag/checkers/check_retained_history_transport_agda.py'): raise ValueError('checker drift')
    dirs=[ROOT/'research/sontag/agda',ROOT/'research/nima/agda',ROOT/'research/voevodsky/agda',ROOT/'research/nima/adapters',Path(r['args'][-2])]
    expected={str(p) for d in dirs for p in d.rglob('*.agda')}
    if set(r['source_inventory_sha256'])!=expected: raise ValueError('inventory coverage')
    for p,h in r['source_inventory_sha256'].items():
        if sha(p)!=h: raise ValueError('inventory source drift')

r=json.loads(RECEIPT.read_text(encoding='utf-8'))
validate(r)
rejected=[]
for name in ('incremental','unsafe','failed','unstable','stale-source','missing-inventory','stale-checker'):
    bad=copy.deepcopy(r)
    if name=='incremental': bad['ignore_interfaces']=False
    elif name=='unsafe': bad['args'].remove('--safe')
    elif name=='failed': bad['exit_code']=42
    elif name=='unstable': bad['inputs_stable']=False
    elif name=='stale-source': bad['source_sha256']='0'*64
    elif name=='missing-inventory': bad['source_inventory_sha256'].pop(next(iter(bad['source_inventory_sha256'])))
    else: bad['checker_sha256']='0'*64
    try: validate(bad)
    except ValueError: rejected.append(name)
    else: raise AssertionError('accepted corrupt receipt '+name)
out={'schema':'marici.sontag.retained-history-receipt-validation.v1','passed':True,
     'compiler_rerun':False,'receipt_sha256':sha(RECEIPT),'rejected_controls':rejected,
     'inventory_count':len(r['source_inventory_sha256'])}
p=ROOT/'research/sontag/results/retained-history-receipt-validation-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

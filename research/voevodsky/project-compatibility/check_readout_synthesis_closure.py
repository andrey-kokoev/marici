"""Rerun source-scoped controls; keep refutations and conditional claims distinct."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
claims_path=HERE/'readout-comparison-claims.json'
checks=[('check_readout_relative_contract.py','readout-relative-comparison-contract.json'),('check_readout_contract_tate.py','readout-contract-tate-instance.json'),('check_readout_realized_pullback.py','readout-contract-realized-pullback.json'),('check_readout_orientation.py','readout-orientation-obstruction.json'),('check_spectral_observer_completion.py','spectral-observer-compatible-completion.json')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
watched=[claims_path,HERE/'readout-comparison-synthesis.md']+[HERE/n for n,_ in checks]
before={str(p.relative_to(ROOT)):sha(p) for p in watched}
exe=ROOT/'temp/readout-weighted-three-road-star.exe'
subprocess.run(['rustc',str(ROOT/'research/voevodsky/check_weighted_three_road_star.rs'),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
run=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=60)
(ROOT/'temp/readout-weighted-three-road-star.json').write_text(run.stdout,encoding='utf-8')
results=[];packets={}
for checker,receipt in checks:
 subprocess.run([sys.executable,str(HERE/checker)],check=True,capture_output=True,text=True,timeout=120)
 packet=json.loads((HERE/receipt).read_text(encoding='utf-8'))
 assert packet['passed'] and packet['source_unchanged']
 packets[checker]=packet
 results.append({'checker':checker,'receipt_sha256':sha(HERE/receipt),'passed':True})
registry=json.loads(claims_path.read_text(encoding='utf-8'));claims={c['id']:c for c in registry['claims']}
assert len(claims)==len(registry['claims'])==12
allowed={'proved_scoped','source_recorded','refuted','source_conditional','not_posed'}
for claim in claims.values():
 assert claim['status'] in allowed and (ROOT/claim['evidence']).is_file()
 assert claim['model'] and claim['boundary']
assert claims['later_fs_kato_realization']['status']=='source_recorded'
assert claims['twisted_source_bridge']['status']=='source_conditional'
assert claims['direct_spectral_to_kato_physical_readout']['status']=='not_posed'
assert packets['check_readout_contract_tate.py']['fresh_weighted_star_status']=='inconclusive'
assert packets['check_spectral_observer_completion.py']['ordinary_stacked_cone_cokernel_rank']==3
assert packets['check_readout_realized_pullback.py']['arbitrary_ambient_triples_realized'] is False
assert packets['check_readout_orientation.py']['untwisted_equivariant_map_values']==[0]
assert packets['check_readout_orientation.py']['nonzero_twisted_choices']==2
assert before=={str(p.relative_to(ROOT)):sha(p) for p in watched}
report={'passed':True,'source_unchanged':True,'comparison_checker_count':5,'fresh_weighted_road_status':'inconclusive','claim_count':12,'results':results,'source_sha256':before,'scope':'Finite source-indexed claim-consistency audit; neither registry labels nor graph admission certify physical truth or re-prove the fs/Kato geometric construction.'}
(HERE/'readout-synthesis-closure.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))

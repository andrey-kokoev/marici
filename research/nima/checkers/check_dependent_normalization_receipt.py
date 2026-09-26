"""Audit the fresh dependent-normalization Agda receipt; does not compile."""
import copy
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
RESULTS=ROOT/'research/nima/results'
NAMES=('DependentPackageNormalizationRegression.agda','DependentPackageNormalization.agda',
       'DependentNormalizationCoherence.agda','DependentArbitraryIndexRoutes.agda',
       'DependentSigmaPiCoherence.agda','WholePackageSigmaPi.agda',
       'ProofRelevantCoherenceClosure.agda','IndexIdentityCoherence.agda',
       'IndexIdentityCoherenceRegression.agda','SigmaPiComparisonDecomposition.agda')
def errors(receipt):
    found=[]
    if receipt.get('schema')!='marici.nima.agda-check.v1':found.append('wrong schema')
    if receipt.get('module')!='DependentPackageNormalizationRegression':found.append('wrong module')
    if receipt.get('passed') is not True or receipt.get('exit_code')!=0:found.append('compiler failed')
    if receipt.get('ignore_interfaces') is not True:found.append('not fresh')
    for name in NAMES:
        actual=hashlib.sha256((ROOT/'research/nima/agda'/name).read_bytes()).hexdigest()
        if receipt.get('owner_source_inventory_sha256',{}).get(name)!=actual:found.append('stale: '+name)
    return found
receipt=json.loads((RESULTS/'agda-DependentPackageNormalizationRegression.json').read_text(encoding='utf-8-sig'))
found=errors(receipt)
for mutation in ('stale-source','failed-compiler','not-fresh'):
    bad=copy.deepcopy(receipt)
    if mutation=='stale-source':bad['owner_source_inventory_sha256'][NAMES[1]]='0'*64
    elif mutation=='failed-compiler':bad['passed']=False
    else:bad['ignore_interfaces']=False
    assert errors(bad),'bad receipt accepted: '+mutation
report={'schema':'marici.nima.dependent-normalization-receipt.v1','passed':not found,
        'classification':'checked_arbitrary_dependent_index_normalization_and_common_coordinate_coherence',
        'errors':found,'source_files_audited':len(NAMES),'negative_receipt_checks':3,
        'full_generated_comparison_basis_complete':False,
        'scope':'Receipt/digest audit; mathematical evidence is the fresh Agda closure check.'}
(RESULTS/'dependent-normalization-receipt.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(0 if not found else 1)

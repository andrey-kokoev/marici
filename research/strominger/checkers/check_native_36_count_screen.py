"""Fresh exact baryon-grid replay, typed counts and source fingerprint checks."""
from pathlib import Path
import hashlib,json
import check_baryon_tensor_grid as grid_check  # Replays every operator coefficient.
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger/results'
receipt=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())
for name,digest in receipt['sourceHashes'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
assert receipt['checkerSha256']==hashlib.sha256(Path(grid_check.__file__).read_bytes()).hexdigest()
dimensions={};sources=[]
for species in ['proton','neutron','electron']:
    source=BASE/'common-three-carrier-protocol'/f'{species}.json'
    data=json.loads(source.read_text());dimensions[species]=len(data['source']['metric'])
    assert len(data['source']['coordinates'])==dimensions[species]
    sources.append(source)
assert dimensions=={'proton':36,'neutron':36,'electron':8}
for species in ['proton','neutron']:
    c=receipt['carriers'][species]
    assert c['allOperatorCoefficientsMatch'] and c['weightFactorizationExact']
    assert len(c['grid'])==12 and all(len(row)==3 for row in c['grid'])
    assert sorted(sum(c['grid'],[]))==list(range(36))
    assert sorted(sum(c['columnBlocks'],[]))==list(range(36))
    assert [len(b) for b in c['columnBlocks']]==[12,12,12]
    assert all(len(set(r)&set(b))==1 for r in c['rowBlocks'] for b in c['columnBlocks'])
assert sum(dimensions.values())==80
assert dimensions['neutron']+dimensions['electron']==44
result={'status':'native-baryon-36-grid-confirmed-not-three-PNE-sectors',
        'rawDimensions':dimensions,'baryonGrid':[12,3],
        'columnBlockSizes':[12,12,12],
        'independentPNEDirectSumDimension':80,
        'sharedBaryonChartPlusIndependentElectronDimension':44,
        'freshFullBaryonCoefficientReplay':True,
        'geometricEdgeToFieldMapConstructed':False,
        'PNESolidConstructed':False,'fieldSewingVerified':False,
        'interpretationSelected':False,
        'scope':'Exact field-coordinate accounting. The three support blocks lie within each baryon chart; they are not P,N,E species. No geometric closure, source regeneration, physical or global coverage claim.'}
sources += [Path(__file__),Path(grid_check.__file__),BASE/'baryon-tensor-grid/verification.json',ROOT/'research/strominger/native-36-count-screen-v1.md']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'native-36-count-screen';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['sourceHashes','scope']}))

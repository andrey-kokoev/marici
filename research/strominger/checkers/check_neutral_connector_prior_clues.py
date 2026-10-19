"""Read-only prior-source audit plus small exact arithmetic replays.
Does not rerun or overwrite other owners' checkers/results.
"""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
import hashlib
import json
from check_symplectic_neutral_connector import mul,transpose,rank
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
hashes={}
def read(path):
    b=(ROOT/path).read_bytes();hashes[path]=hashlib.sha256(b).hexdigest();return json.loads(b)
def inverse(a):
    n=len(a);r=[row[:]+[Q(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if r[i][j]);r[j],r[p]=r[p],r[j]
        v=r[j][j];r[j]=[x/v for x in r[j]]
        for i in range(n):
            if i!=j:
                v=r[i][j];r[i]=[x-v*y for x,y in zip(r[i],r[j])]
    return [row[n:] for row in r]
def extract(a,rows,cols):return [[a[i][j] for j in cols] for i in rows]
def minus(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def encoded(a):return [[str(x) for x in row] for row in a]

def main():
    audited=[];checked=0
    for path in [
        'research/strominger/results/canonical-source-energy.json',
        'research/strominger/results/neutron-canonical-record-binding.json',
        'research/strominger/results/neutron-canonical-rotation-frame.json',
        'research/strominger/results/neutron-canonical-occupied-closure.json',
        'research/strominger/results/polarization_reversal_transport.json',
        'research/strominger/results/neutron-autonomous-rim-scattering-audit.json',
        'research/strominger/results/neutron-source-action-rest-gap.json']:
        data=read(path);assert data.get('status')=='passed',path
        sources=data.get('source_hashes',{});assert sources,path
        for source,digest in sources.items():
            assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==digest,('stale receipt',path,source);checked+=1
        audited.append({'receipt':path,'directHashesChecked':len(sources)})
    flux=read('research/voevodsky/results/mode_flux_charge.json');assert flux['verification_passed']
    checker='research/voevodsky/checkers/check_mode_flux_charge.py'
    assert hashlib.sha256((ROOT/checker).read_bytes()).hexdigest()==flux['checker_sha256'];checked+=1
    ambient=read('research/voevodsky/results/coupled_six_piece_belt_store.json')
    assert flux['source_roots']['ambient']==ambient['root']
    edges=flux['adjacency_comparison']['belt_shared_face_edges']
    patterns=[list(signs) for signs in product((-1,1),repeat=6) if all(signs[i]==-signs[j] for i,j in edges)]
    assert len(patterns)==2 and sorted(patterns)==sorted(flux['adjacency_comparison']['belt_patterns'])
    assert not [signs for signs in product((-1,1),repeat=4) if all(signs[i]==-signs[j] for i,j in combinations(range(4),2))]
    response=read('research/voevodsky/results/belt_interface_response.json');assert response['verification_passed']
    spectrum_path='research/voevodsky/results/collective_carrier_spectrum.json'
    b=(ROOT/spectrum_path).read_bytes();assert hashlib.sha256(b).hexdigest()==response['source_sha256'];hashes[spectrum_path]=hashlib.sha256(b).hexdigest();checked+=1
    spectrum=json.loads(b);assert spectrum['verification_passed']
    K=[[Q(x) for x in row] for row in spectrum['belt_reduced_matrix']]
    weights=list(map(Q,spectrum['belt_modal_norms']));assert len(K)==len(weights)==6
    odd=[[K[i][j]-K[i][j+3] for j in range(3)] for i in range(3)]
    assert encoded(odd)==response['odd_sector_matrix']
    inv=inverse(odd);assert inv[0][0]==1 and mul(inv,inv)[0][0]==Q(4485,1193)
    e=[[Q(i==0)] for i in range(3)];ke=mul(odd,e);kke=mul(odd,ke)
    control=[e[i]+ke[i]+kke[i] for i in range(3)]
    observe=[transpose(e)[0],mul(transpose(e),odd)[0],mul(mul(transpose(e),odd),odd)[0]]
    assert rank(control)==rank(observe)==3
    assert odd[0][1]==Q(-2099,3292)
    stiffness=[[weights[i]*K[i][j] for j in range(6)] for i in range(6)]
    assert stiffness==transpose(stiffness)
    B=[0,3];I=[1,2,4,5]
    schur=minus(extract(stiffness,B,B),mul(extract(stiffness,B,I),mul(inverse(extract(stiffness,I,I)),extract(stiffness,I,B))))
    c=Q(1193,675);assert schur==[[c,-c],[-c,c]]
    typed=read('research/voevodsky/results/deuterium_typed_rim_binding.json');assert typed['verification_passed']
    assert typed['opposite_charge_fixed_neutral_linear_matching_rejected']
    assert Q(typed['same_total_exterior_charge_pair_minus_separate'])==0
    assert all(Q(row['pair_minus_separate_exact'])>0 for row in typed['nuclear_breakup_controls'])
    for path in [Path(__file__),BASE/'checkers/check_symplectic_neutral_connector.py']:
        hashes[str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
    result={'schema':'marici.neutral-connector-prior-clues.v1','status':'pass','sourceHashes':hashes,
        'receiptAudits':audited,'directHashComparisons':checked,
        'freshSmallReplays':{'beltAlternatingPatterns':patterns,'protonK4AlternationImpossible':True,
         'actualBridgeStiffness':encoded(schur),'responseAtZero':'1','responseDerivativeAtZero':'4485/1193',
         'minimalResponseDimension':3,'scalarClosureCounterexample':'-2099/3292'},
        'scope':'Fresh direct receipt/hash audit and graph/Schur/response arithmetic. Not a rerun of full flux, autonomous scattering, gap, polarization or other-owner suites; no bridge to the new opposite-circulation branch is inferred.'}
    out=BASE/'results/neutral-connector-prior-clues';out.mkdir(parents=True,exist_ok=True)
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','directHashComparisons':checked,'freshSmallReplays':result['freshSmallReplays']}))

if __name__=='__main__':main()

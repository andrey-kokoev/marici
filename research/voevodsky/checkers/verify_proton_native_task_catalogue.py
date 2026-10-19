"""Independent rational-realification audit of the saved task certificate.
Does not import the producer or its field/matrix functions. Shared inputs are
read only. Exact C-linear rank r is checked as rational rank 2r on Q(sqrt(-3)).
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/'research/voevodsky/results/proton-native-task-catalogue-v1.json'

def zero(n,m):return [[F(0)]*m for _ in range(n)]
def identity(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def multiply(a,b):
    c=zero(len(a),len(b[0]));rows=[[(j,v) for j,v in enumerate(r) if v] for r in b]
    for i,r in enumerate(a):
        for k,v in enumerate(r):
            if v:
                for j,w in rows[k]:c[i][j]+=v*w
    return c

def subtract(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def rank(a):
    if not a:return 0
    a=[list(r) for r in a];i=0
    for j in range(len(a[0])):
        p=next((k for k in range(i,len(a)) if a[k][j]),None)
        if p is None:continue
        a[i],a[p]=a[p],a[i];v=a[i][j]
        # Forward echelon only: distinct from the producer's reduced algorithm.
        a[i]=[x/v for x in a[i]]
        for k in range(i+1,len(a)):
            if a[k][j]:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def realify(packet):
    n,m=packet['shape'];out=zero(2*n,2*m)
    for i,j,aa,bb in packet['entries']:
        a,b=F(aa),F(bb)
        out[i][j]=a;out[i][j+m]=-3*b;out[i+n][j]=b;out[i+n][j+m]=a
    return out

def vector(v):return [[F(x[0])] for x in v]+[[F(x[1])] for x in v]
def native(records,ports):
    index={tuple(p):i for i,p in enumerate(ports)};stages={'raw':0,'local':1,'aligned':2};packets=[{'shape':[36,36],'entries':[]} for _ in range(3)]
    for r in records:
        packets[stages[r['source'][0]]]['entries'].append([index[tuple(r['target'][1:])],index[tuple(r['source'][1:])],r['weight_real'],r['weight_imag_sqrt3']])
    return list(map(realify,packets))

def main():
    p=json.loads(RESULT.read_text());assert p['verification_passed']
    for name,h in p['source_hashes'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==h,name
    records=json.loads((ROOT/'research/nima/results/twelve-triangle-1836-arrows.json').read_text())
    L,G,N=native(records,p['coordinate_addresses']);I=identity(72)
    assert multiply(G,L)==N and multiply(N,N)==N
    assert [rank(a)//2 for a in (L,G,N)]==[12,3,1]
    assert [rank(a)//2 for a in (subtract(I,L),subtract(L,N),N)]==[24,11,1]
    B=realify(p['local_mode_encoder']);C=realify(p['local_mode_decoder'])
    assert multiply(B,C)==L and multiply(C,B)==identity(24)
    comparisons=realify(p['independent_compatibility_comparisons']);assert rank(comparisons)==22
    measurement=realify(p['reconstruction']['measurement']);decoder=realify(p['reconstruction']['decoder'])
    assert multiply(decoder,measurement)==I
    # Receipt rows must be genuine native readings, not a fabricated invertible map.
    rr=p['reconstruction']['raw_addresses'];ll=p['reconstruction']['local_addresses']
    expected=[I[j] for j in rr]+[L[j] for j in ll]+[I[j+36] for j in rr]+[L[j+36] for j in ll]
    assert measurement==expected
    for case in p['all_mask_theorem']['global_regressions']:
        anchors=case['anchors'];rows=[A[j] for A in (I,L,N) for j in anchors]+[A[j+36] for A in (I,L,N) for j in anchors]
        assert rank(rows)==2*case['rank']
    seed=p['seed_face_counterexample'];anchors=seed['observed_addresses']
    O=[A[j] for A in (I,L,N) for j in anchors]+[A[j+36] for A in (I,L,N) for j in anchors]
    assert rank(O)==38 and rank(multiply(O,B))==14
    x,y,b=map(vector,(seed['input_x'],seed['input_y'],seed['collective_vector']))
    assert x!=y and multiply(O,x)==multiply(O,y)
    assert multiply(L,x)==x and multiply(L,y)==y and multiply(N,x)==multiply(N,y)==b
    energy=lambda v:sum(v[i][0]**2+3*v[i+36][0]**2 for i in range(36))
    assert energy(x)==energy(y)>0
    for deletion in p['reconstruction']['one_address_deletion_witnesses']:
        aa=[j for j in rr if j!=deletion['removed_address']]
        rows=[A[j] for A in (I,L,N) for j in aa]+[A[j+36] for A in (I,L,N) for j in aa]
        v=vector(deletion['kernel_witness'])
        assert any(z[0] for z in v) and multiply(rows,v)==zero(len(rows),1)
    # A corrupted decoder fails the exact identity, even with unchanged counts.
    wrong=[row[:] for row in decoder];wrong[0][0]+=1
    assert multiply(wrong,measurement)!=I
    out={'schema':'marici.voevodsky.native-task-independent-audit.v1','status':'passed','verification_passed':True,
         'method':'independent rational realification, forward Gaussian rank and sparse matrix products; no producer import',
         'checked_global_mask_profiles':len(p['all_mask_theorem']['global_regressions']),
         'checked_deletion_witnesses':len(p['reconstruction']['one_address_deletion_witnesses']),
         'decoder_checked_on_all_72_rational_basis_vectors':True,'equal_norm_seed_blind_pair_verified':True,
         'result_sha256':sha256(RESULT.read_bytes()).hexdigest(),'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    dest=RESULT.with_name('proton-native-task-catalogue-v1-independent-audit.json');dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

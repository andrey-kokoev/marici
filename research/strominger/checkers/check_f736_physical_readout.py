"""Source physical packet bounds and native covariance on the actual F736 pair."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from exact_multiradical import Radical as R,mm,adj,identity,serialize
from check_finite_observer_encoder import restore,perm,rational_inverse
ROOT=Path(__file__).resolve().parents[3];BASE='research/strominger/'
CONTRACT=BASE+'contracts/f736-physical-readout-attempt.v1.json'
SNAPSHOT=BASE+'contracts/persistent-seam-pe-conjecture-net.snapshot.rev40.json'
OUT=BASE+'results/f736-physical-readout/'
def load(p):return json.loads((ROOT/p).read_text())
def encode_intervals(a):return [[[str(x) for x in v] for v in row] for row in a]
def outer(a,b):return [[x*y for y in b] for x in a]
def transpose(a):return [list(row) for row in zip(*a)]
def hermitian_intervals(m):
    return [[tuple((m[i][j][k]+m[j][i][k])/2 for k in range(2)) for j in range(len(m))] for i in range(len(m))]
def skew_interval(m,i,j):return ((m[i][j][0]-m[j][i][1])/2,(m[i][j][1]-m[j][i][0])/2)
def pairing(m,a,b):return sum(b[i].conjugate()*m[i][j]*a[j] for i in range(len(a)) for j in range(len(a)))
def main():
    spec=load(CONTRACT);pre=load(SNAPSHOT);checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    inputs={CONTRACT,SNAPSHOT,BASE+'checkers/check_f736_physical_readout.py',BASE+'checkers/check_finite_observer_encoder.py',BASE+'checkers/exact_multiradical.py',BASE+'f736-physical-readout-result-v1.md'}
    receipt_names=['archimedean-cutoff-entry-verification','archimedean-diagonal-limit-verification','finite-observer-encoder-verification','screw-field-sewing','native-ne-fine-face/verification','external-c0-finite-trace/verification']
    for name in receipt_names:
        p=BASE+'results/'+name+'.json';r=load(p);inputs.add(p)
        check('live source receipt: '+name,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==sha for q,sha in r['sourceHashes'].items()));inputs.update(r['sourceHashes'])
    n=next(n for n in pre['conjectures'] if n['id']=='f736-physical-readout-attempt')
    check('physical readout attempt registered before execution',n['status']=='open' and n['registration_before_execution'])
    face=load(BASE+'results/native-ne-fine-face/binding.json')
    check('actual F736 H134 pair and native crossing retained',face['face']['face']==spec['face'] and [p['packet'] for p in face['incidentPackets']]==[5,15] and all(c['role']=='H134' for c in face['face']['localContexts']))
    physical,diagonal=map(load,spec['inputBounds']);inputs.update(spec['inputBounds'])
    diagonal_rows={r['Lambda']:r for r in diagonal['cutoffBounds']};cutoff_results=[]
    for row in physical['cutoffResults']:
        cutoff=row['Lambda']
        if cutoff not in spec['cutoffs']:continue
        d=tuple(map(F,diagonal_rows[cutoff]['centeredDiagonalCoarseEnclosure']))
        entries={(r['i'],r['j']):r for r in row['entries']}
        T=[[d if i==j else tuple(map(F,entries[i,j]['traceEnclosure'])) for j in range(5)] for i in range(5)]
        # Source T_ij multiplies a_i conjugate(b_j), hence M_ji=T_ij in b* M a.
        M=transpose(T)
        H=hermitian_intervals(M)
        S=[]
        for i in range(5):
            r=[]
            for j in range(5):
                if i==j:r.append((F(0),F(0)));continue
                lo,hi=skew_interval(M,i,j)
                # Opposite ordered entries have the same source limit, not equal finite values.
                radius=(F(entries[i,j]['errorFromLimitAtMost'])+F(entries[j,i]['errorFromLimitAtMost']))/2
                r.append((max(lo,-radius),min(hi,radius)))
            S.append(r)
        check('all25 centered physical entries retained at cutoff '+str(cutoff),len(entries)==20 and all(lo<=hi for matrix in [T,M,H,S] for r in matrix for lo,hi in r))
        check('Hermitian and skew orientations retained at cutoff '+str(cutoff),all(H[i][j]==H[j][i] and S[i][j]==(-S[j][i][1],-S[j][i][0]) for i in range(5) for j in range(5)))
        check('finite skew is bounded but not silently erased at cutoff '+str(cutoff),all(S[i][i]==(0,0) for i in range(5)) and all(S[i][j][0]<0<S[i][j][1] for i in range(5) for j in range(5) if i!=j))
        cutoff_results.append({'Lambda':cutoff,'sourceOrderedTraceIntervals':encode_intervals(T),'sesquilinearMatrixIntervals':encode_intervals(M),'HermitianIntervals':encode_intervals(H),'realSkewNumeratorIntervals':encode_intervals(S),'skewConvention':'K=-i*S, S=(M-M*)/2; these are bounds, not point values.'})
    check('exactly the registered physical cutoffs used',[r['Lambda'] for r in cutoff_results]==spec['cutoffs'])
    encoder=load(BASE+'results/finite-observer-encoder.json');sewing=load(BASE+'results/screw-field-sewing.json')
    _,inverse=rational_inverse([[F(x) for x in row] for row in encoder['analyticReadoutMatrix']]);Ti=[[R(x) for x in row] for row in inverse];Hframe=restore(encoder['nativeFiveFrame'])
    p={r['packet']:r for r in sewing['packetBindings']};D={i:mm(mm(mm(Ti,Hframe),adj(perm(p[i]['nativePermutation']))),restore(p[i]['readout'])) for i in [5,15]}
    U=restore(sewing['generatorMatrices']['NE']);transported=mm(D[15],U)
    check('decoder covariance on all44 field inputs',transported==D[5])
    for i in range(5):
        for j in range(5):
            check('native pullback square for physical matrix unit '+str((i,j)),outer(transported[i],transported[j])==outer(D[5][i],D[5][j]))
    control=[[F(0),F(1)],[F(0),F(0)]];a=[F(1),F(0)];b=[F(0),F(1)]
    check('linear-first trace requires transpose, detected by ordered matrix-unit control',pairing(transpose(control),a,b)==1 and pairing(control,a,b)==0)
    T=[[R(F(x)) for x in row] for row in encoder['analyticReadoutMatrix']]
    check('physical volume metric is not replaced by observation Gram',mm(adj(T),T)!=identity(5) and any(mm(adj(T),T)[i][j]!=0 for i in range(5) for j in range(5) if i!=j))
    # M=e01: H and iK are both nonzero; retaining H alone changes its ordered pairing.
    ci=[[(x,x) for x in row] for row in transpose(control)]
    h=hermitian_intervals(ci)[1][0][0];s=skew_interval(ci,1,0)[0]
    check('discarding skew loses an ordered cross-observer readout',h+s==pairing(transpose(control),a,b) and h!=1 and h-s==0)
    artifact={'contract':CONTRACT,'face':face['face'],'nativeInterface':spec['nativeInterface'],'domain':spec['domain'],'physicalOperators':spec['physicalOperators'],
        'cutoffResults':cutoff_results,'decoderPullbacks':{str(i):serialize(d) for i,d in D.items()},
        'nativeForms':'G_a(M)=D_a* M D_a; U_NE* G_15(M) U_NE=G_5(M), separately for Hermitian and skew channels.',
        'volumeCounterterm':'2 log(Lambda) d I5 in packet coefficients; pull back I5 with D_a, not T*T.',
        'physicalReadoutComparisonEstablished':True,'analyticalFaceFillerEstablished':False,'fineEdgeOperatorsSupplied':False,'hardyReferenceIdentificationEstablished':False,'allSemilocalSectorsEstablished':False,'fullPbConstructionEstablished':False,
        'remainingObligation':'Bind source operators on E514,E539,E515 and the H134 homotopy or witness recovery on admitted fine-vertex presentations. Native covariance of this physical readout is not that filler.',
        'scope':spec['scope']}
    (ROOT/OUT).mkdir(parents=True,exist_ok=True);dest=OUT+'readout.json';(ROOT/dest).write_text(json.dumps(artifact,indent=2)+'\n');inputs.add(dest)
    report={'status':'passed','check_count':len(checks),'checks':checks,'face':'F736','cutoffs':spec['cutoffs'],'enclosedPhysicalEntries':75,'nativeMatrixUnitSquares':25,'nativeFieldDimension':44,
        'physicalReadoutComparisonEstablished':True,'analyticalFaceFillerEstablished':False,'fineEdgeOperatorsSupplied':False,'hardyReferenceIdentificationEstablished':False,'allSemilocalSectorsEstablished':False,'fullPbConstructionEstablished':False,
        'sourceHashes':{q:hashlib.sha256((ROOT/q).read_bytes()).hexdigest() for q in sorted(inputs)}}
    (ROOT/OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['checks','sourceHashes']}))
if __name__=='__main__':main()

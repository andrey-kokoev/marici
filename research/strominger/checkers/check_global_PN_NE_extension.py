"""Necessary exact conditions for extending the local PN face connection."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,product,sharp
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
def trace(op):return sum((v for (i,j),v in op.items() if i==j),ZERO)
def rank(op,n):
    a=[[op.get((i,j),ZERO) for j in range(n)] for i in range(n)];r=0
    for j in range(n):
        k=next((i for i in range(r,n) if a[i][j]!=ZERO),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k];factor=a[r][j].inverse();a[r]=[v*factor for v in a[r]]
        for i in range(r+1,n):
            x=a[i][j]
            if x!=ZERO:a[i]=[v-x*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r
sources={s:json.loads((BASE/f'common-three-carrier-protocol/{s}.json').read_text()) for s in ['proton','neutron','electron']};ops={s:{k:read_operator(d['operators'][k],len(d['source']['metric'])) for k in ['L','G','N']} for s,d in sources.items()}
labels=sources['proton']['source']['coordinates'];patches=json.loads((BASE/'tetrahedral-field-attachment/verification.json').read_text())['gridGeometry'];pEdges=[p['outerArrow'] for p in patches if p['surfaceTriangle'][0]=='F_BCD'];assert len(pEdges)==3
# Marking A=a,B=b,C=u,D=v: incoming face is BCD. Its ambient normal is
# proportional to (1,1,1); each of its three patches has the same tangent plane.
FP={}
for edge in pEdges:
    for i in range(3):
        for j in range(3):FP[labels.index(edge+':'+'xyz'[i]),labels.index(edge+':'+'xyz'[j])]=A(F(int(i==j))-F(1,3))
face=json.loads((BASE/'native-patch-mode-transport/verification.json').read_text());store=json.loads((ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json').read_text());incoming=face['incomingReaderFaceTriangleIndices'];nSlots=[2*store['triangle_order'].index(t)+axis for t in incoming for axis in range(2)];FN={(i,i):ONE for i in nSlots}
for s,proj in [('proton',FP),('neutron',FN)]:
    assert product(proj,proj)==proj;assert sharp(proj,list(map(F,sources[s]['source']['metric'])))==proj;assert rank(proj,36)==6
faceWeights={s:trace(product(proj,ops[s]['N'])) for s,proj in [('proton',FP),('neutron',FN)]};assert faceWeights['proton']==A(F(1,4));assert faceWeights['neutron']==A(F(1,6))
compressionRanks={s:{k:rank(product(product(proj,op),proj),36) for k,op in ops[s].items()} for s,proj in [('proton',FP),('neutron',FN)]}
assert compressionRanks['proton']['L']==3;assert compressionRanks['neutron']['G']==6
assert compressionRanks['proton']['G']!=compressionRanks['neutron']['L']
# Even preservation of the rank-one return alone would imply equal face
# weights if a metric-unitary S sent the six-dimensional face onto the face.
assert faceWeights['proton']!=faceWeights['neutron']
# NE rank bound: a map intertwining returns decomposes into image and kernel
# blocks. It can reach at most min(1,2)+min(35,6)=7 electron directions.
rN=int(trace(ops['neutron']['N']).record()['0']);rE=int(trace(ops['electron']['N']).record()['0']);assert (rN,rE)==(1,2)
rankBound=min(rN,rE)+min(36-rN,8-rE);assert rankBound==7
result={'status':'strict-local-PN-extension-and-surjective-NE-intertwining-obstructed','PN':{'sourceTangentialFaceDimension':6,'targetTangentialFaceDimension':6,'sourceFaceOuterArrows':pEdges,'targetFaceCoordinates':nSlots,'returnNormFractions':{s:v.record() for s,v in faceWeights.items()},'compressedOperatorRanks':compressionRanks,'faceSupportedMetricUnitaryGlobalReturnExtensionExists':False,'returnWeightMismatch':'1/4 - 1/6 = 1/12 of normalized full return norm','proof':'If S is metric-unitary, S FP S^-1=FN and S NP S^-1=NN imply tr(FP NP)=tr(FN NN). Exact native values differ. Exchanging L/G also fails compressed-rank preservation.','consequence':'A globally return-preserving unitary connection must couple the selected face to other field components; the six-dimensional conditional face map cannot remain a closed face-supported block.'},'NE':{'sourceDimension':36,'targetDimension':8,'sourceReturnRank':rN,'targetReturnRank':rE,'maximumRankOfAnyReturnIntertwiner':rankBound,'minimumKernelDimension':36-rankBound,'surjectiveReturnIntertwinerExists':False,'proof':'For S NN=NE S, im(NN) maps into im(NE), and ker(NN) into ker(NE). Rank(S)<=min(1,2)+min(35,6)=7.','consequence':'At least one electron return direction is inaccessible under this exact linear intertwining hypothesis. Need another independent incoming return channel, or an interaction not preserving these projectors. No such extension is silently supplied.'},'scope':'Conditional exact extension tests, not claims that actual physical PN/NE transfers must be unitary, face-supported, surjective or return-intertwining. The earlier normalized six-component face transport remains valid; it is not extendible with all the extra stated properties. No global field connection derived, no source/production/viewer changes.'}
paths=[Path(__file__).resolve(),*[BASE/f'common-three-carrier-protocol/{s}.json' for s in sources],BASE/'tetrahedral-field-attachment/verification.json',BASE/'native-patch-mode-transport/verification.json',ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths};out=BASE/'global-PN-NE-extension';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'PNfaceReturnWeights':{'proton':'1/4','neutron':'1/6'},'compressedRanks':compressionRanks,'NEmaximumIntertwinerRank':rankBound}))

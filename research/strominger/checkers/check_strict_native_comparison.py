"""Exact native comparison functor and conditional analytical-to-native square.
The native matrices are source artifacts, not synthetic stand-ins for observers.
No observer encoder L is supplied or silently inferred.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from exact_multiradical import Radical as R,mm,identity,serialize

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
SEWING=BASE+'channel-assembled-field-sewing.json'
FIXTURE=BASE+'channel-assembled-native-fixture.json'
STRICT=BASE+'esd7-strict-parent-evaluation-verification.json'


def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def perm(p):return [[R(int(j==p[i])) for j in range(5)] for i in range(5)]
def inverse(p):return [p.index(i) for i in range(5)]
def compose(p,q):return [q[i] for i in p] # matrices P(p)P(q)
def relative(p,q):return compose(q,inverse(p))
INV={'PN':'inverse-PN','inverse-PN':'PN','P-reader':'P-reader','NE':'NE'}
def normalize(word):
    out=[]
    for x in word:
        if out and INV[x]==out[-1]:out.pop()
        else:out.append(x)
    return out


def joint_normal(program,start):
    """Typed execution-order square with an UNSPECIFIED L:D->Z44."""
    current=start;stack=[]
    for token in program:
        kind,label=token.split(':') if ':' in token else (token,'')
        if kind=='R':source,target='V'+label,'D'
        elif kind=='S':source,target='D','V'+label
        elif kind=='U':source,target='Z44','N'+label
        elif kind=='Ui':source,target='N'+label,'Z44'
        elif kind=='L':source,target='D','Z44'
        else:raise ValueError('unknown symbol')
        if current!=source:raise ValueError('comparison domain mismatch')
        current=target
        if stack:
            old=stack[-1];k,l=old.split(':') if ':' in old else (old,'')
            if label==l and (k,kind) in [('S','R'),('R','S'),('U','Ui'),('Ui','U')]:
                stack.pop();continue
        stack.append(token)
    return current,stack


def main():
    data=json.loads((ROOT/SEWING).read_text());fixture=json.loads((ROOT/FIXTURE).read_text());strict=json.loads((ROOT/STRICT).read_text())
    checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    for label,receipt in [('native',data),('strict-parent',strict)]:
        check(label+' direct receipt inputs are current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in receipt['sourceHashes'].items()))
    check('native source reports the complete14-packet18-interface44-field fixture',data['status']=='passed' and data['counts']['packets']==14 and data['counts']['interfaces']==18 and data['counts']['rootFieldDimension']==44)
    generators={name:restore(a) for name,a in data['generatorMatrices'].items()}
    packets={p['packet']:p for p in data['packetBindings']}; ids=sorted(packets);root=fixture['rootPacket']
    U={i:data['frameTypes'][p['species']+str(p['frameParity'])]['forwardFactorWord'] for i,p in packets.items()}
    Ui={i:data['frameTypes'][p['species']+str(p['frameParity'])]['inverseFactorWord'] for i,p in packets.items()}
    P={i:p['nativePermutation'] for i,p in packets.items()}
    B={i:restore(p['binding']) for i,p in packets.items()}; RR={i:restore(p['readout']) for i,p in packets.items()}
    normalized_readouts={};normalized_bindings={}
    for i in ids:
        # R_i U_i as an actual5x44 matrix; no restriction to prepared states.
        row=RR[i]
        for factor in reversed(U[i]):row=mm(row,generators[factor])
        normalized_readouts[i]=row
        # U_i^-1 B_i as an actual44x5 matrix.
        column=B[i]
        for factor in Ui[i]:column=mm(generators[factor],column)
        normalized_bindings[i]=column
        if row!=mm(perm(P[i]),RR[root]):raise AssertionError('full readout root comparison')
        if column!=mm(B[root],perm(inverse(P[i]))):raise AssertionError('coefficient binding root comparison')
    check('all14 normalized readouts agree on the entire44-coordinate root field',True)
    check('all14 normalized embeddings preserve the actual five-slot permutations',True)
    pairs=[]
    for a,b in product(ids,repeat=2):
        pi=relative(P[a],P[b]); field=normalize(Ui[a]+U[b])
        assert normalized_readouts[b]==mm(perm(pi),normalized_readouts[a])
        assert mm(normalized_bindings[b],perm(pi))==normalized_bindings[a]
        pairs.append({'source':a,'target':b,'fieldFactorWord':field,'coefficientPermutation':pi,
                      'full44ReadoutSquare':True,'fiveBindingSquare':True})
    check('all196 pairwise field/readout and coefficient-binding squares hold',len(pairs)==196)
    for a,b,c in product(ids,repeat=3):
        assert normalize(Ui[a]+U[b]+Ui[b]+U[c])==normalize(Ui[a]+U[c])
        assert compose(relative(P[b],P[c]),relative(P[a],P[b]))==relative(P[a],P[c])
    check('all2744 comparison triangles retain both cocycles',True)
    for op in fixture['operations']:
        assert op['permutation']==relative(P[op['source']],P[op['target']])
    check('comparison coefficients restrict to all18 native interface laws',True)
    a,b=fixture['comparisonPackets']; pi=relative(P[a],P[b]);power=list(range(5));order=0
    while True:
        power=compose(pi,power);order+=1
        if power==list(range(5)):break
        assert order<=120
    check('actual retained-history comparison has identity field map and order-five coefficient map',normalize(Ui[a]+U[b])==[] and order==5 and pi!=list(range(5)))
    check('dropping its coefficient witness breaks a full44 readout square',RR[a]!=RR[b] and normalized_readouts[a]!=normalized_readouts[b])
    check('discarding local binding frames is observably wrong',B[a]!=B[b])
    # K_(i,a)=U_a L R_i. Check the conditional square for every pair of
    # analytical charts and every pair of native packet presentations.
    conditional_count=0
    for i,j,a,b in product(range(1,5),range(1,5),ids,ids):
        left=[f'R:{i}',f'S:{j}',f'R:{j}','L',f'U:{b}']
        right=[f'R:{i}','L',f'U:{a}',f'Ui:{a}',f'U:{b}']
        assert joint_normal(left,'V'+str(i))==joint_normal(right,'V'+str(i))==('N'+str(b),[f'R:{i}','L',f'U:{b}'])
        conditional_count+=1
    check('all3136 mixed presentation squares commute conditional on one typed encoder L',conditional_count==3136)
    try:joint_normal(['R:1','U:0'],'V1');rejected=False
    except ValueError:rejected=True
    check('missing observer-to-native encoder cannot be replaced by identity',rejected)
    try:joint_normal(['R:1','L','U:0','Ui:999','U:1'],'V1');rejected=False
    except ValueError:rejected=True
    check('mismatched native comparison frame is rejected',rejected)
    a,b=fixture['comparisonPackets']
    witness={'sourcePacket':a,'targetPacket':b,'fieldFactorWord':normalize(Ui[a]+U[b]),
             'coefficientPermutation':relative(P[a],P[b]),'coefficientOrder':order,
             'readoutsDifferent':RR[a]!=RR[b],'bindingsDifferent':B[a]!=B[b]}
    artifact=BASE+'strict-native-comparison.json'
    result={'pairs':pairs,'retainedOrderFiveWitness':witness,
            'normalizedReadouts':{str(i):serialize(r) for i,r in normalized_readouts.items()},
            'conditionalComparison':'K_(i,a)=U_a L R_i, with L:D->C44 not supplied',
            'coefficientReadout':'R_native,a K_(i,a)=P_a R_native,root L R_i',
            'encoderSupplied':False,'intendedAnalyticalWitnessBindingEstablished':False,
            'fullEsd7NativeTransportEstablished':False,'full114ChannelEstablished':False}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[SEWING,FIXTURE,STRICT,artifact,'research/strominger/checkers/exact_multiradical.py',
            'research/strominger/checkers/check_strict_native_comparison.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'pairwiseComparisons':196,
            'nativeCocycleTriangles':2744,'conditionalMixedSquares':conditional_count,
            'retainedOrderFiveWitness':witness,'encoderSupplied':False,
            'intendedAnalyticalWitnessBindingEstablished':False,'fullEsd7NativeTransportEstablished':False,'full114ChannelEstablished':False,
            'remainingGate':'Supply a source-defined observer encoder L and its endpoint/residual/readout identities on an admitted domain or finite packet. Arbitrary L satisfies the formal field square but does not bind the intended observables or higher witnesses.',
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Exact existing native fixture comparisons plus a symbolic conditional family. No analytical observer is encoded by these checks; native coefficient witnesses are not erased by field-frame equality.'}
    (ROOT/BASE/'strict-native-comparison-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','pairwiseComparisons','nativeCocycleTriangles','conditionalMixedSquares','retainedOrderFiveWitness']}))


if __name__=='__main__':main()

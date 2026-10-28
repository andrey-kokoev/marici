#!/usr/bin/env python3
"""Bounded exact native transport and source-integral residual enclosure."""
import json, hashlib, sys
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from check_finite_observer_encoder import restore, perm, rational_inverse
from exact_multiradical import Radical as R, mm, adj, identity, serialize
BASE='research/strominger/results/'
inputs={}
def load(path):
    inputs[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    return json.loads((ROOT/path).read_text())
def main():
    profile=load('research/aspect/contracts/analytical-two-route-pilot.v1.json')
    enc=load(BASE+'finite-observer-encoder.json')
    sewing=load(BASE+'channel-assembled-field-sewing.json')
    fixture=load(profile['fixture'])
    diag=load(BASE+'archimedean-diagonal-limit.json')
    off=load(BASE+'archimedean-cutoff-entry.json')
    checks=[]
    def check(name,v):
        if not v: raise AssertionError(name)
        checks.append(name)
    for name in ['finite-observer-encoder-verification.json','archimedean-cutoff-entry-verification.json','archimedean-diagonal-limit-verification.json']:
        receipt=load(BASE+name)
        check(name+' live direct hashes',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in receipt['sourceHashes'].items()))
    check('sewing live hashes',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in sewing['sourceHashes'].items()))
    T=[[R(F(v)) for v in row] for row in enc['analyticReadoutMatrix']]
    _,ti=rational_inverse(enc['analyticReadoutMatrix']);Ti=[[R(v) for v in row] for row in ti]
    L=restore(enc['rootEncoder']);D={int(k):restore(v) for k,v in enc['packetDecoders'].items()}
    packets={p['packet']:p for p in sewing['packetBindings']}
    generators={k:restore(v) for k,v in sewing['generatorMatrices'].items()}
    ops={o['id']:o for o in fixture['operations']}
    check('root reconstruction',mm(D[fixture['rootPacket']],L)==identity(5))
    results=[];ends=[]
    for history in fixture['histories']:
        x=L;current=fixture['rootPacket'];steps=[];transported=[]
        for n,oid in enumerate(history['operations']):
            op=ops[oid];check(history['id']+' boundary '+str(n),op['source']==current and op['target']==history['packets'][n+1])
            kind=op['kind']
            if kind=='reader-phase-advance':kind='P-reader' if packets[current]['species']=='proton' else 'identity'
            if kind=='NN-phase-advance':kind='identity'
            if kind!='identity':x=mm(generators[kind],x)
            current=op['target'];transported.append(kind)
            check(history['id']+' decode '+str(n),mm(D[current],x)==identity(5))
            steps.append({'operation':oid,'occurrence':history['occurrences'][n],'decodedBasisIdentity':True})
        # Reverse on the transported image using actual metric inverse generators.
        back=x
        inv={'PN':'inverse-PN','inverse-PN':'PN','P-reader':'P-reader','NE':'NE'}
        for kind in reversed(transported):
            if kind!='identity':back=mm(generators[inv[kind]],back)
        check(history['id']+' roundtrip',back==L)
        ends.append(x)
        results.append({'history':history,'steps':steps,'roundtripDefect':'exact zero on all five packet basis vectors','exit':current})
    check('endpoint decoded agreement',mm(D[9],ends[0])==mm(D[25],ends[1])==identity(5))
    a,b=fixture['comparisonPackets'];pa=perm(packets[a]['nativePermutation']);pb=perm(packets[b]['nativePermutation'])
    comparison=mm(pb,adj(pa));power=identity(5)
    for _ in range(5):power=mm(comparison,power)
    check('nontrivial order five coefficient witness',comparison!=identity(5) and power==identity(5))
    check('histories not erased',fixture['histories'][0]['operations']!=fixture['histories'][1]['operations'])
    v=[[R(i)] for i in [2,-5,2,0,0]]
    check('endpoint invisible control',mm(T[:2],v)==[[R(0)],[R(0)]] and mm(T[2:],v)!=[[R(0)]]*3)
    check('full decode retains invisible control',mm(D[9],mm(ends[0],v))==v)
    truncated=T[:2]+[[R(0)]*5 for _ in range(3)]
    check('drop complement rejected',mm(Ti,truncated)!=identity(5))
    check('swapped endpoints rejected',T[0]!=T[1])
    G=[[R(F(2)**(i-j)+F(2)**(j-i)) for j in range(5)] for i in range(5)]
    negative=[[R(i)] for i in [3,-2,0,0,0]]
    check('signed endpoint value minus four',mm(adj(negative),mm(G,negative))==[[R(-4)]])
    check('reversed endpoint form detected',mm(adj(negative),mm([[-v for v in row] for row in G],negative))==[[R(4)]])
    check('wrong volume Gram rejected',mm(adj(T),T)!=identity(5) and mm(adj(T),T)[0][1]!=0)
    cutoff=profile['Lambda'];bound=next(x for x in diag['cutoffBounds'] if x['Lambda']==cutoff)
    dist=off['distanceBounds']['1'];err=F(dist['forwardErrorConstant'])/cutoff**2
    lo,hi=map(F,dist['limit']);residual=[lo-err-F(5,2),hi+err-F(5,2)]
    check('declared equation refuted beyond cutoff error',residual[1]<0)
    ordered=[]
    for i in range(5):
        for j in range(5):
            if i==j:
                entry={'finitePart':diag['finitePartExpression'],'error':bound['diagonalCenteredErrorAtMost']}
            else:
                db=off['distanceBounds'][str(abs(i-j))]
                entry={'limitIntegral':off['packetIntegral'].replace('K_Lambda','K_infinity'),'limitEnclosure':db['limit'],'error':str(F(db['forwardErrorConstant' if i<j else 'reverseErrorConstant'])/cutoff**2)}
            ordered.append({'i':i,'j':j,'centeredEntry':entry,'subtractEndpoint':str(F(2)**(i-j)+F(2)**(j-i))})
    result={'checksPassed':len(checks),'checks':checks,'routes':results,
      'analyticalForm':{'kernel':off['kernel'],'centeredVolume':'2*d*log(Lambda)*I5','orderedEntries':ordered,'pullback':'D_a^* (C_Lambda-G) D_a; on transported basis X_a, D_a X_a=I5 checked exactly, hence all 25 entries recovered without approximating integrals'},
      'inputEquationResidual':{'equation':profile['equation_under_test'],'enclosure':list(map(str,residual)),'cutoffErrorAtMost':str(err),'verdict':'nonzero negative; chosen equality rejected, not a refutation of a source theorem'},
      'interRouteDecodedDiscrepancy':'exact zero on packet; coefficient/history witness remains nontrivial',
      'retainedCoefficientComparison':serialize(comparison),
      'observationLoss':{'vector':[2,-5,2,0,0],'endpointValues':[0,0],'retainedFlux':[2,-5,2]},
      'cutoffUncertainty':bound,'witnessMatch':{'verdict':'blocked by missing source data','H':None,'boundaryMap':None,'missing':'Intended analytical face/tetrahedral witness and typed boundary identifying it with these retained routes. Native permutation is not silently that analytical filler.'},
      'overallVerdict':'Detected endpoint observation loss; exact finite-packet transport and nonzero chosen analytical defect bounded. Intended analytical coherencer comparison blocked. No quotient obstruction certified.',
      'scope':'No positivity, physical implementation, arbitrary equation solving, uniform regulator exhaustion or full 4x28/114-record claim. Continuum bounds imported from cited analytic derivations, not independently kernel-proved or quadrature-evaluated.',
      'sourceHashes':inputs}
    dest=ROOT/'research/aspect/results/analytical-two-route-pilot.json';dest.parent.mkdir(parents=True,exist_ok=True)
    result['sourceHashes']['research/aspect/checkers/check_analytical_two_route_pilot.py']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checksPassed':len(checks),'residualEnclosure':list(map(str,residual)),'verdict':result['overallVerdict']},indent=2))
if __name__=='__main__':main()

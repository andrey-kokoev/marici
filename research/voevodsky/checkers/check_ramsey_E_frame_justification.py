"""Full44 passive frame comparison versus actual native E-transition authority."""
from pathlib import Path
import hashlib,json,subprocess,sys
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3]
for path in ['research/strominger/checkers','research/voevodsky/checkers']:sys.path.insert(0,str(ROOT/path))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
from check_ramsey_E_joint44_comparison import restore,add,sharp,gram,perm
pins={}
def load(path):
    raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def block(a,b):
    return [row+[R() for _ in b] for row in a]+[[R() for _ in a]+row for row in b]
def main():
    comparison=load('research/voevodsky/results/ramsey-E-joint44-comparison-v1.json')
    for path,digest in comparison['source_sha256'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
        pins[path]=digest
    five=load('research/strominger/results/full-five-channel-candidate/verification.json')
    ne=load('research/strominger/results/neutron-contrast-electron-transport/verification.json')
    native=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    B=restore(five['neutronFiveEmbedding']);Bout=restore(five['postNEJointEmbedding'])
    EF=restore(ne['electronFrame']);rot=restore(comparison['electronContrastFrameDifference'])
    m=list(map(F,native['source']['metric']));metric=m+[F(1)]*8
    # Swap only the two already retained orthonormal context lines.
    contexts=[[row[0],row[4]] for row in B]
    assert gram(contexts,m)==identity(2)
    Pc=mm(contexts,sharp(contexts,m))
    FN=add(add(identity(36),Pc,-1),mm(mm(contexts,perm([1,0])),sharp(contexts,m)))
    # Complete the known native action by identity off the E return image.
    PE=mm(EF,adj(EF))
    FE=add(add(identity(8),PE,-1),mm(mm(EF,rot),adj(EF)))
    FNinv=[[FN[j][i].conj()*(m[j]/m[i]) for j in range(36)] for i in range(36)]
    assert mm(FNinv,FN)==identity(36) and mm(FN,FN)==identity(36)
    assert mm(adj(FE),FE)==identity(8) and mm(mm(FE,FE),FE)==identity(8)
    F44=block(FN,FE);back=block(FNinv,adj(FE))
    assert mm(back,F44)==identity(44)
    Pi=perm(ne['fiveCoefficientTest']['nativePermutation'])
    H=perm(comparison['provisionalOutgoingToNativeOutputIndices'])
    actual=mm(Bout,Pi);target=mm(Bout,H)
    assert mm(F44,actual)==target and actual!=target
    Ra,Rt=sharp(actual,metric),sharp(target,metric)
    assert mm(Rt,F44)==Ra # on ALL44 coordinates, not only prepared fields
    assert mm(Ra,actual)==mm(Rt,target)==identity(5)
    assert mm(Ra,F44)!=Ra,'unchanged reader wrongly accepted'
    sixth=identity(44)
    for _ in range(6):sixth=mm(F44,sixth)
    assert sixth==identity(44) and mm(F44,F44)!=identity(44)
    # Minimal actual-native audit: all24 marked source P->N->E chains,
    # complete geometry aliases and the unchanged outgoing generator.
    js="""
import assert from 'node:assert/strict';
import {GenerativeAssemblyRules} from './research/nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from './research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from './research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from './research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const perms=a=>a.length?a.flatMap((v,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]), names=['C0','M0','C1','M1'],rows=[];
for(const marking of perms([0,1,2,3])){
 const r=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(names.map((n,i)=>[n,seed.vertices[marking[i]].join(',')]))});
 const op=(id,k)=>r.outgoing(id).map(i=>r.operations[i]).find(o=>o.kind===k);
 const pn=op(r.root,'PN'),ne=op(pn.target,'NE');assert(r.validateTransfer(pn)&&r.validateTransfer(ne));
 const p=r.packets[ne.target],c=r.charts[p.chart],f=phaseFrame(c,0);
 assert.equal(auditPhaseFrame(f).status,'native-template-compatible');
 const cyclic={...f,window:[f.window[1],f.window[2],f.window[0]]};
 const cyclicStatus=auditPhaseFrame(cyclic).status;
 assert.notEqual(cyclicStatus,'native-template-compatible');
 assert.notEqual(c.aliases.C0,c.aliases.M2);
 rows.push({marking,C0:c.aliases.C0,M2:c.aliases.M2,orderedWindow:f.window,context:f.context,
   electronOutgoingCount:r.outgoing(ne.target).length,cyclicRelabellingStatus:cyclicStatus});
}
assert(rows.every(r=>r.electronOutgoingCount===0));console.log(JSON.stringify(rows));
"""
    run=subprocess.run(['node','--input-type=module','-e',js],cwd=ROOT,capture_output=True,text=True,check=True)
    rows=json.loads(run.stdout);assert len(rows)==24
    for path in ['research/nima/generative-phase-assembly.mjs',
      'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
      'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
      'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs']:
        pins[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    # Typed target basis of the comparison is H^-1 acting on native labels.
    # Its first four names agree with the outgoing reference, its last is
    # the retained OLD C0, not the distinct native geometric M2.
    nativeLabels=['C0','M0','C1','M1','C2']
    h=comparison['provisionalOutgoingToNativeOutputIndices']
    targetLabels=[nativeLabels[h.index(i)] for i in range(5)]
    assert targetLabels==['M0','C1','M1','C2','C0']
    outgoingLabels=['M0','C1','M1','C2','M2']
    assert targetLabels[:4]==outgoingLabels[:4] and targetLabels[-1]!=outgoingLabels[-1]
    occurrenceJ={'C0':'M2','M0':'C2','C1':'M1','M1':'C1','C2':'M0','M2':'C0'}
    fullJLabels=[occurrenceJ[label] for label in targetLabels]
    assert fullJLabels==['C2','M1','C1','M0','M2']
    assert fullJLabels!=outgoingLabels # J is not a context-only rename
    for module in list(sys.modules.values()):
        filename=getattr(module,'__file__',None)
        if filename:
            path=Path(filename).resolve()
            if path.is_file() and path.is_relative_to(ROOT/'research'):
                pins[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    result={'schema':'marici.ramsey-E-frame-justification.v1','node':'T-seam-based-port-readout-binding',
      'checkerStatus':'passed','scientificStatus':'full44_passive_comparison_passes_native_transition_not_supplied',
      'full44MetricUnitary':True,'full44ReadoutSquare':True,'fiveCoefficientRecovery':True,
      'contextSwapOrder':2,'electronActionOrder':3,'combinedOrder':6,
      'forwardFrame':serialize(F44),'backwardFrame':serialize(back),
      'actualNativeOutputLabelsAfterReindexing':targetLabels,'requestedOutgoingLabels':outgoingLabels,
      'unmatchedComplementSlot':4,'fullOccurrenceJOnReindexedLabels':fullJLabels,
      'directionalProvenanceNote':'J sends old C0 to dual M2 at the old C0 vertex, not to the old native M2 vertex. It also transforms every other occurrence; applying only the last rename is not J.',
      'freshNativeMarkings':24,'nativeAudit':rows,
      'negativeControls':['Frozen reader fails despite unitary frame','Cyclic geometric-window relabelling fails native phase frame','Native C0 and M2 are geometrically distinct in every tested chain','No generated outgoing E operation in any tested chain'],
      'disposition':'The frame adjustment is justified as a constructed passive comparison with a transported reader. It is not justified as an active native E transition or same-chart C0=M2 identification. The latter would require a direction-indexed occurrence/boundary witness; preserving the labels instead leaves that interface open.',
      'netOutcomeChanged':False,'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-E-frame-justification-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','full44MetricUnitary','full44ReadoutSquare','fiveCoefficientRecovery','combinedOrder','freshNativeMarkings','actualNativeOutputLabelsAfterReindexing','requestedOutgoingLabels']}))
if __name__=='__main__':main()

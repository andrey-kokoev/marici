"""Shared common-port selection: covariance versus pair-reversal invariance."""
from pathlib import Path
import json,hashlib,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-common-selection'
V=['c0','m0','c1','m1'];S=[1,0,3,2];EDGES=list(itertools.combinations(range(4),2));EN=['e'+str(a)+str(b) for a,b in EDGES]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-endpoint-policy-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale endpoint policy '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyCommonSelection where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (Bool; false; true)',
      'open import Cubical.Data.Unit.Base using (tt)','open import Cubical.Data.Empty.Base using (⊥)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)',
      'open import RamseyEndpointPolicy using (Frame; base; complement; swap; choose; side-map; not-fixed)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyEdgeNaturality as N','import RamseyPermitEquivalence as M',
      'chart : Frame → C.Chart','chart base = C.q0','chart complement = C.q7',
      'reverse : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.S.Common (chart b) (chart a)',
      'reverse a b (e , (p , q)) = e , (q , p)',
      'edge-move : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.S.Common (chart (swap a)) (chart (swap b))']
    frames=[('base',0),('complement',7)]
    for a,c in frames:
        for b,d in frames:
            for i,e in enumerate(EN):
                j=EDGES.index(tuple(sorted(S[v] for v in EDGES[i])))
                lines += [f'edge-move {a} {b} ({e} , (p , q)) = {EN[j]} , (N.move-{c}-{i} p , N.move-{d}-{i} q)']
    lines += ['vertex-move : (a b : Frame) → E.A.V.Common (chart a) (chart b) → E.A.V.Common (chart (swap a)) (chart (swap b))']
    for a,c in frames:
        for b,d in frames:
            for v in range(4):lines += [f'vertex-move {a} {b} ({V[v]} , (p , q)) = {V[S[v]]} , (M.move-{c}-{v} p , M.move-{d}-{v} q)']
    lines += ['FullSelector : Type','FullSelector = (a b : Frame) → E.A.S.Common (chart a) (chart b) → Bool',
      'ordered : FullSelector','ordered a b (e , ports) = choose a e',
      'Covariant : FullSelector → Type',
      'Covariant s = (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → s (swap a) (swap b) (edge-move a b x) ≡ side-map (fst x) (s a b x)',
      'ReversalInvariant : FullSelector → Type',
      'ReversalInvariant s = (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → s b a (reverse a b x) ≡ s a b x',
      'ordered-covariant : Covariant ordered']
    for a,c in frames:
        for b,d in frames:
            for e in EN:lines += [f'ordered-covariant {a} {b} ({e} , (p , q)) = refl']
    lines += ['select : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.V.Common (chart a) (chart b)',
      'select a b x = E.A.restrict-common (ordered a b x) {a = chart a} {b = chart b} x',
      'select-natural : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → vertex-move a b (select a b x) ≡ select (swap a) (swap b) (edge-move a b x)']
    for a,c in frames:
        for b,d in frames:
            for i,e in enumerate(EN):
                side=1 if c==7 and i in [0,5] else 0;v=EDGES[i][side]
                lines += [f'select-natural {a} {b} ({e} , (p , q)) i = {V[S[v]]} , (N.restrict-{c}-{i}-{side} p i , N.restrict-{d}-{i}-{side} q i)']
    lines += ['witness : E.A.S.Common C.q0 C.q7','witness = e01 , (E.att-0-2-0 , E.att-7-3-0)',
      'witness-move-reverses : edge-move base complement witness ≡ reverse base complement witness','witness-move-reverses = refl',
      'no-covariant-reversal : (s : FullSelector) → Covariant s → ReversalInvariant s → ⊥',
      'no-covariant-reversal s covariance reversal = not-fixed (s base complement witness) (sym (covariance base complement witness) ∙ reversal base complement witness)',
      'ordered-not-reversal : ReversalInvariant ordered → ⊥','ordered-not-reversal = no-covariant-reversal ordered ordered-covariant',
      'left : FullSelector','left a b x = false',
      'left-reversal : ReversalInvariant left','left-reversal a b x = refl',
      'left-not-covariant : Covariant left → ⊥','left-not-covariant covariance = no-covariant-reversal left covariance left-reversal',
      'different-selected-vertices : fst (select base complement witness) ≡ fst (select complement base (reverse base complement witness)) → ⊥',
      'different-selected-vertices p = transport (cong (M.Is m0) (sym p)) tt']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyCommonSelection.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyCommonSelectionBadReversal.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCommonSelectionBadReversal where
open import Cubical.Foundations.Prelude
open import RamseyCommonSelection
open import RamseyEndpointPolicy using (base; complement)
bad : ordered complement base (reverse base complement witness) ≡ ordered base complement witness
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyCommonSelection',True),('RamseyCommonSelectionBadReversal',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-common-selection-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-common-selection.verification.v1','status':'passed','scope_id':'common-port-selection-covariance-versus-reversal-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'orderedSharedSelectionCovariant':True,'arbitraryCommonRestrictionNaturality':True,
      'nonemptyMixedChartWitness':True,'witnessInvolutionEqualsReversal':True,
      'fullWitnessDependentCovariantReversalInvariantSelectorRefuted':True,
      'orderedSelectionReversalInvariant':False,'constantLeftReversalInvariant':True,
      'selectedVertexDifferenceProved':True,'reversalPromotionHostileRejected':True,
      'retainedBothEndpointComparisonRefuted':False,'nativeOperationAdded':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-common-selection-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

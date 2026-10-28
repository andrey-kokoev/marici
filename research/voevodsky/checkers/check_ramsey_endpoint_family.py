"""Retained endpoint family and covariance/reversal interchange."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-endpoint-family'
ED=list(itertools.combinations(range(4),2));EN=['e'+str(a)+str(b) for a,b in ED];V=['c0','m0','c1','m1'];S=[1,0,3,2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-common-selection-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale common selection '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyEndpointFamily where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.HLevels',
      'open import Cubical.Data.Bool.Base using (Bool; false; true)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)',
      'open import RamseyEndpointPolicy using (Frame; base; complement; swap; side-map)',
      'open import RamseyCommonSelection using (chart; reverse; edge-move; vertex-move; witness)',
      'open import RamseyPermitFibers using (vertex-set; facet-fiber-prop)',
      'import RamseyEdgeNaturality as N','import RamseyEdgeAttachmentsExamples as E',
      'family : (a b : Frame) → E.A.S.Common (chart a) (chart b) → Bool → E.A.V.Common (chart a) (chart b)',
      'family a b x side = E.A.restrict-common side {a = chart a} {b = chart b} x',
      'reverse-vertex : (a b : Frame) → E.A.V.Common (chart a) (chart b) → E.A.V.Common (chart b) (chart a)',
      'reverse-vertex a b (v , (p , q)) = v , (q , p)',
      'family-native : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → E.A.V.R.Resolve (E.A.V.selected-package (chart a) (chart b) (family a b x side))',
      'family-native a b x side = E.A.restricted-selection side (chart a) (chart b) x',
      'covariance : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → vertex-move a b (family a b x side) ≡ family (swap a) (swap b) (edge-move a b x) (side-map (fst x) side)']
    frames=[('base',0),('complement',7)]
    for a,c in frames:
        for b,d in frames:
            for e,en in enumerate(EN):
                for side in range(2):
                    v=ED[e][side];s=['false','true'][side]
                    lines += [f'covariance {a} {b} ({en} , (p , q)) {s} i = {V[S[v]]} , (N.restrict-{c}-{e}-{side} p i , N.restrict-{d}-{e}-{side} q i)']
    lines += ['reversal : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → reverse-vertex a b (family a b x side) ≡ family b a (reverse a b x) side',
      'reversal a b (e , (p , q)) false = refl','reversal a b (e , (p , q)) true = refl',
      'edge-interchange : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → edge-move b a (reverse a b x) ≡ reverse (swap a) (swap b) (edge-move a b x)']
    for a,c in frames:
        for b,d in frames:
            for en in EN:lines += [f'edge-interchange {a} {b} ({en} , (p , q)) = refl']
    lines += ['vertex-interchange : (a b : Frame) (x : E.A.V.Common (chart a) (chart b)) → vertex-move b a (reverse-vertex a b x) ≡ reverse-vertex (swap a) (swap b) (vertex-move a b x)']
    for a,c in frames:
        for b,d in frames:
            for v in V:lines += [f'vertex-interchange {a} {b} ({v} , (p , q)) = refl']
    lines += ['common-set : (a b : Frame) → isSet (E.A.V.Common (chart a) (chart b))',
      'common-set a b = isSetΣ vertex-set (λ v → isSetΣ (isSetΣ vertex-set (λ f → isProp→isSet (facet-fiber-prop (chart a) v f))) (λ _ → isSetΣ vertex-set (λ f → isProp→isSet (facet-fiber-prop (chart b) v f))))']
    signature='(a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → vertex-move b a (reverse-vertex a b (family a b x side)) ≡ family (swap b) (swap a) (edge-move b a (reverse a b x)) (side-map (fst x) side)'
    lines += ['reverse-then-move : '+signature,
      'reverse-then-move a b (e , (p , q)) side = cong (vertex-move b a) (reversal a b (e , (p , q)) side) ∙ covariance b a (reverse a b (e , (p , q))) side',
      'move-then-reverse : '+signature,
      'move-then-reverse a b x side = vertex-interchange a b (family a b x side) ∙ cong (reverse-vertex (swap a) (swap b)) (covariance a b x side) ∙ reversal (swap a) (swap b) (edge-move a b x) (side-map (fst x) side) ∙ cong (λ y → family (swap b) (swap a) y (side-map (fst x) side)) (sym (edge-interchange a b x))',
      'interchange : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → reverse-then-move a b x side ≡ move-then-reverse a b x side',
      'interchange a b x side = common-set (swap b) (swap a) _ _ _ _']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyEndpointFamily.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyEndpointFamilyBadCollapse.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointFamilyBadCollapse where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyEndpointPolicy using (base; complement)
open import RamseyCommonSelection using (witness)
open import RamseyEndpointFamily
bad : family base complement witness false ≡ family base complement witness true
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-common-selection','ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyEndpointFamily',True),('RamseyEndpointFamilyBadCollapse',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-endpoint-family-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-endpoint-family.verification.v1','status':'passed','scope_id':'retained-two-endpoint-restriction-and-interchange-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'bothEndpointsRetained':True,'arbitraryCommonCovariance':True,'arbitraryPairReversalCompatibility':True,
      'covarianceReversalPathInterchange':True,'bothEndpointNativeSelections':True,
      'commonIndexIsSet':True,'endpointCollapseHostileRejected':True,
      'nativeDerivationProofEqualityClaimed':False,'invariantSingleEndpointSelectionClaimed':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-endpoint-family-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

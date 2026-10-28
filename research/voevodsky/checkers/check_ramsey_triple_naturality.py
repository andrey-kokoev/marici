"""Common-edge triple transport with projections and retained middle data."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-triple-naturality'
ED=list(itertools.combinations(range(4),2));EN=['e'+str(a)+str(b) for a,b in ED];V=['c0','m0','c1','m1'];S=[1,0,3,2]
FR=[('base',0),('complement',7)]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-endpoint-family-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale endpoint family '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyTripleNaturality where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (Bool; false; true)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)',
      'open import RamseyEndpointPolicy using (Frame; base; complement; swap; side-map)',
      'open import RamseyCommonSelection using (chart; edge-move; vertex-move)',
      'import RamseyEdgeNaturality as N','import RamseyPermitEquivalence as M',
      'import RamseyEdgeAttachmentsExamples as E','import RamseyEndpointFamily as H',
      'ET VT : Frame → Frame → Frame → Type',
      'ET a b c = E.A.S.Triple (chart a) (chart b) (chart c)',
      'VT a b c = E.A.V.Triple (chart a) (chart b) (chart c)',
      'edge-triple : (a b c : Frame) → ET a b c → ET (swap a) (swap b) (swap c)']
    for frames in itertools.product(FR,repeat=3):
        fs=' '.join(x[0] for x in frames);cs=[x[1] for x in frames]
        for e,en in enumerate(EN):
            j=ED.index(tuple(sorted(S[v] for v in ED[e])))
            lines += [f'edge-triple {fs} ({en} , (p , (q , r))) = {EN[j]} , (N.move-{cs[0]}-{e} p , (N.move-{cs[1]}-{e} q , N.move-{cs[2]}-{e} r))']
    lines += ['vertex-triple : (a b c : Frame) → VT a b c → VT (swap a) (swap b) (swap c)']
    for frames in itertools.product(FR,repeat=3):
        fs=' '.join(x[0] for x in frames);cs=[x[1] for x in frames]
        for v,vn in enumerate(V):lines += [f'vertex-triple {fs} ({vn} , (p , (q , r))) = {V[S[v]]} , (M.move-{cs[0]}-{v} p , (M.move-{cs[1]}-{v} q , M.move-{cs[2]}-{v} r))']
    # Explicit chart arguments avoid inference through dependent projection domains.
    for kind,mod,typ in [('edge','S','ET'),('vertex','V','VT')]:
        for piece,pair in [('ab','a b'),('bc','b c'),('ac','a c')]:
            lines += [f'{kind}-{piece} : (a b c : Frame) → {typ} a b c → E.A.{mod}.Common '+ ' '.join('(chart '+x+')' for x in pair.split()),
              f'{kind}-{piece} a b c t = E.A.{mod}.{piece}-index {{a = chart a}} {{b = chart b}} {{c = chart c}} t',
              f'{kind}-projection-{piece} : (a b c : Frame) (t : {typ} a b c) → {kind}-move {pair} ({kind}-{piece} a b c t) ≡ {kind}-{piece} (swap a) (swap b) (swap c) ({kind}-triple a b c t)']
            for frames in itertools.product(FR,repeat=3):
                fs=' '.join(x[0] for x in frames)
                for name in EN if kind=='edge' else V:lines += [f'{kind}-projection-{piece} {fs} ({name} , (p , (q , r))) = refl']
    lines += ['restrict : (a b c : Frame) → ET a b c → Bool → VT a b c',
      'restrict a b c t side = E.A.restrict-triple side {a = chart a} {b = chart b} {c = chart c} t',
      'naturality : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-triple a b c (restrict a b c t side) ≡ restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side)']
    for frames in itertools.product(FR,repeat=3):
        fs=' '.join(x[0] for x in frames);cs=[x[1] for x in frames]
        for e,en in enumerate(EN):
            for side in range(2):
                v=ED[e][side];bit=['false','true'][side]
                lines += [f'naturality {fs} ({en} , (p , (q , r))) {bit} i = {V[S[v]]} , (N.restrict-{cs[0]}-{e}-{side} p i , (N.restrict-{cs[1]}-{e}-{side} q i , N.restrict-{cs[2]}-{e}-{side} r i))']
    for piece,pair in [('ab','a b'),('bc','b c'),('ac','a c')]:
        lines += [f'restriction-{piece} : (a b c : Frame) (t : ET a b c) (side : Bool) → H.family {pair} (edge-{piece} a b c t) side ≡ vertex-{piece} a b c (restrict a b c t side)',
          f'restriction-{piece} a b c t side = E.A.{piece}-restriction-cell side (chart a) (chart b) (chart c) t']
        targetpair=' '.join('(swap '+x+')' for x in pair.split())
        sig=f'(a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move {pair} (H.family {pair} (edge-{piece} a b c t) side) ≡ vertex-{piece} (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))'
        lines += [f'pair-route-{piece} : {sig}',
          f'pair-route-{piece} a b c (e , (p , (q , r))) side = H.covariance {pair} (edge-{piece} a b c (e , (p , (q , r)))) side ∙ cong (λ x → H.family {targetpair} x (side-map e side)) (edge-projection-{piece} a b c (e , (p , (q , r)))) ∙ restriction-{piece} (swap a) (swap b) (swap c) (edge-triple a b c (e , (p , (q , r)))) (side-map e side)',
          f'triple-route-{piece} : {sig}',
          f'triple-route-{piece} a b c t side = cong (vertex-move {pair}) (restriction-{piece} a b c t side) ∙ vertex-projection-{piece} a b c (restrict a b c t side) ∙ cong (vertex-{piece} (swap a) (swap b) (swap c)) (naturality a b c t side)',
          f'interchange-{piece} : (a b c : Frame) (t : ET a b c) (side : Bool) → pair-route-{piece} a b c t side ≡ triple-route-{piece} a b c t side',
          f'interchange-{piece} a b c t side = H.common-set {targetpair} _ _ _ _']
    lines += ['native : (a b c : Frame) (t : ET a b c) (side : Bool) → E.A.V.R.Resolve (E.A.V.composition-package (chart a) (chart b) (chart c) (restrict a b c t side))',
      'native a b c t side = E.A.V.composition-proof (chart a) (chart b) (chart c) (restrict a b c t side)',
      'middle-witness : ET base base base',
      'middle-witness = e13 , (E.att-0-0-4 , (E.att-0-2-4 , E.att-0-0-4))',
      'middle-retained : fst (fst (snd (snd (edge-triple base base base middle-witness)))) ≡ m1',
      'middle-retained = refl']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyTripleNaturality.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyTripleNaturalityBadMiddle.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyTripleNaturalityBadMiddle where
open import Cubical.Foundations.Prelude
open import RamseyNativeEdgeAttachments using (e02)
open import RamseyEndpointPolicy using (base)
import RamseyEdgeAttachmentsExamples as E
open import RamseyTripleNaturality
bad : edge-triple base base base middle-witness ≡ (e02 , (E.att-7-1-1 , (E.att-7-1-1 , E.att-7-1-1)))
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-endpoint-family','ramsey-common-selection','ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyTripleNaturality',True),('RamseyTripleNaturalityBadMiddle',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-triple-naturality-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-triple-naturality.verification.v1','status':'passed','scope_id':'common-edge-triple-projection-and-endpoint-naturality-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'arbitraryCommonEdgeTripleTransport':True,'edgeProjectionLaws':3,'vertexProjectionLaws':3,
      'bothEndpointTripleNaturality':True,'projectionPathInterchangeLaws':3,
      'retainedMiddleWitnessChecked':True,'middleCollapseHostileRejected':True,
      'restrictedTripleNativeRealization':True,'differentEdgeFourFacetSeamsCovered':False,
      'nativeDerivationProofEqualityClaimed':False,'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-triple-naturality-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

"""Compare constructor-induced occurrence transport with the established involution."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-constructor-occurrence-agreement'
S=[1,0,3,2];V=['c0','m0','c1','m1']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tag(t):return '-'.join(map(str,t))
def patterns():
    return [f'(P.S.{piece} , (({v} , (p , q)) , (P.S.{side} , tt)))' for piece in ['AB','BC','AC'] for v in V for side in ['source-leg','target-leg']]+[f'(P.S.full-source , (P.S.{port} , tt))' for port in ['first-port','middle-port','final-port']]
def prepare():
    prior=BASE/'results/ramsey-four-facet-constructor-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale constructor comparison '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyConstructorOccurrenceAgreement where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.Equiv using (_≃_)',
      'open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)','open import Cubical.Data.Unit.Base using (tt)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyExternalPEExamples','import RamseyOccurrenceEquivalence as O',
      'import RamseyFourFacetConstructor as F','open import RamseyPEComparisonOccurrences',
      'module L = OccurrenceLift P.S.InputIndex F.payload O.Transports']
    triples=list(itertools.permutations(range(4),3))
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t))
        lines += [f'agree-{n} : (o : P.T.Occurrence tree-{n}) → L.map-occurrence F.comparison-{n} o ≡ O.move-{n} o']
        for p in patterns():lines += [f'agree-{n} {p} = refl']
        lines += [f'function-agree-{n} : L.map-occurrence F.comparison-{n} ≡ O.move-{n}',f'function-agree-{n} = funExt agree-{n}',
          f'witness-agree-{n} : (o : P.T.Occurrence tree-{n}) → PathP (λ i → O.Transports (P.T.origin tree-{n} o) (P.T.origin tree-{u} (agree-{n} o i))) (L.origin-law F.comparison-{n} o) (O.origin-{n} o)']
        for p in patterns():lines += [f'witness-agree-{n} {p} = refl']
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t))
        lines += [f'square-{n} : (o : P.T.Occurrence tree-{n}) → L.map-occurrence F.comparison-{u} (L.map-occurrence F.comparison-{n} o) ≡ o',
          f'square-{n} o = cong (L.map-occurrence F.comparison-{u}) (agree-{n} o) ∙ agree-{u} (O.move-{n} o) ∙ O.square-{n} o']
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t))
        lines += [f'equiv-{n} : P.T.Occurrence tree-{n} ≃ P.T.Occurrence tree-{u}',
          f'equiv-{n} = isoToEquiv (iso (L.map-occurrence F.comparison-{n}) (L.map-occurrence F.comparison-{u}) square-{u} square-{n})']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyConstructorOccurrenceAgreement.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyConstructorOccurrenceBadSelectedOnly.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyConstructorOccurrenceBadSelectedOnly where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (m0; c1)
open import RamseyExternalPEExamples
import RamseyFourFacetVertexCells as Ports
import RamseyFourFacetConstructor as F
open import RamseyConstructorOccurrenceAgreement
bad : L.map-occurrence F.comparison-0-1-2 (P.S.AB , ((m0 , (Ports.vp-0-1 , Ports.vp-3-1)) , (P.S.source-leg , tt)))
  ≡ (P.S.AB , ((c1 , (Ports.vp-1-2 , Ports.vp-0-2)) , (P.S.source-leg , tt)))
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-four-facet-constructor','ramsey-occurrence-equivalence','ramsey-external-pe','ramsey-common-selection','ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyPEComparisonOccurrences',BASE/'agda',True),('RamseyConstructorOccurrenceAgreement',FIX,True),('RamseyConstructorOccurrenceBadSelectedOnly',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'agda/RamseyPEComparisonOccurrences.agda',BASE/'contracts/ramsey-constructor-occurrence-agreement-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-constructor-occurrence-agreement.verification.v1','status':'passed','scope_id':'constructor-induced-full-occurrence-and-source-witness-agreement-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'genericConstructorOccurrenceMap':True,'genericSourceRelationWitness':True,
      'arbitraryOccurrenceAgreementLaws':24,'functionEqualityCells':24,'dependentSourceWitnessAgreementLaws':24,
      'inducedOccurrenceEquivalences':24,'unselectedBranchCollapseHostileRejected':True,
      'constructorCorrespondenceRoundTripEqualityClaimed':False,'wholeNativeDerivationEqualityClaimed':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-constructor-occurrence-agreement-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

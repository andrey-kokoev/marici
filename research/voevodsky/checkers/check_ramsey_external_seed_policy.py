"""Policy necessity for the explicit external compiler, not arbitrary native paths."""
from pathlib import Path
import hashlib,json,subprocess,sys,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-external-seed-policy'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-external-pe-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale external construction '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyExternalSeedPolicyExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Unit.Base using (Unit; tt)',
      'open import Cubical.Data.Empty.Base using (⊥)',
      'import RamseyRequestedPortExamples as C','open import RamseyExternalPEExamples',
      'open import RamseyExternalPEPolicy',
      'BaseChart PairChart : C.Chart → Type']
    for c in range(24):
        lines.append(f'BaseChart C.q{c} = '+('Unit' if c==0 else '⊥'))
    for c in range(24):
        lines.append(f'PairChart C.q{c} = '+('Unit' if c in [0,7] else '⊥'))
    lines += ['payload = λ { (c , (v , p)) → P.S.port-package c v p }',
      'module Base = Policy P.S.InputIndex (λ { (c , (v , p)) → E.A.vertex-packet c v p }) (λ i → BaseChart (fst i))',
      'module Pair = Policy P.S.InputIndex (λ { (c , (v , p)) → E.A.vertex-packet c v p }) (λ i → PairChart (fst i))']
    # E is used explicitly rather than relying on re-exports from the imported example.
    lines.insert(lines.index('open import RamseyExternalPEExamples'),'import RamseyEdgeAttachmentsExamples as E')
    lines.remove('payload = λ { (c , (v , p)) → P.S.port-package c v p }')
    branch='λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } }'
    for a,b,c in itertools.permutations(range(4),3):
        tag=f'{a}-{b}-{c}';tree='tree-'+tag
        lines += [f'pair-good-{tag} : Pair.Good {tree}',
          f'pair-good-{tag} = λ {{ P.S.AB → {branch} ; P.S.BC → {branch} ; P.S.AC → {branch} ; P.S.full-source → λ {{ P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt }} }}',
          f'pair-native-{tag} : Pair.R.Resolve (P.T.encode {tree})',
          f'pair-native-{tag} = Pair.realize {tree} pair-good-{tag}']
        position=next(i for i,f in enumerate([a,b,c]) if f in [1,3]);leg=['first-port','middle-port','final-port'][position]
        lines += [f'not-base-{tag} : Base.Good {tree} → ⊥',
          f'not-base-{tag} good = Base.all-leaves {tree} good (P.S.full-source , (P.S.{leg} , tt))']
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyExternalSeedPolicyExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyExternalSeedPolicyBadPromotion.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalSeedPolicyBadPromotion where
open import RamseyExternalPEExamples
open import RamseyExternalSeedPolicyExamples
bad : Base.Good tree-0-1-2
bad = pair-good-0-1-2
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,FIX,BASE/'fixtures/ramsey-external-pe',BASE/'fixtures/ramsey-four-facet-vertex-cells',
      BASE/'fixtures/ramsey-native-edge-attachments',BASE/'fixtures/ramsey-requested-port',ROOT/'research/nima/agda',
      tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyExternalPEPolicy',owner,True),('RamseyExternalSeedPolicyExamples',FIX,True),('RamseyExternalSeedPolicyBadPromotion',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),owner/'RamseyExternalPEPolicy.agda',owner/'RamseyExternalPE.agda',
      BASE/'contracts/ramsey-external-seed-policy-attempt.v1.json',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-external-seed-policy.verification.v1','status':'passed',
      'scope_id':'external-four-facet-PE-tree-seed-policy-necessity-v1','freshSafeCubical':True,
      'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'goodIffAllExternalLeavesAllowed':True,'restrictedPolicyNativeRealization':True,
      'twoChartPolicyActualTreesAdmitted':24,'baseOnlyActualTreesRefuted':24,
      'complementarySourceOccurrenceWitnesses':24,'policyPromotionHostileRejected':True,
      'unselectedEPrerequisitesOmitted':False,'arbitraryNativeResolveImpossibilityClaimed':False,
      'allOperationalComplementGenerationRefuted':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-external-seed-policy-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

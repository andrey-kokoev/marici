"""Admission transport on full occurrences; never singleton-source generation."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-policy-transport'
S=[1,0,3,2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tag(t):return '-'.join(map(str,t))
def prepare():
    priors=[BASE/'results'/f'{n}-v1.json' for n in ['ramsey-occurrence-equivalence','ramsey-external-seed-policy']]
    for path in priors:
        d=json.loads(path.read_text());assert d['status']=='passed'
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale policy input '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyPolicyTransportExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Unit.Base using (Unit; tt)',
      'open import Cubical.Data.Empty.Base using (⊥)','open import Agda.Builtin.String using (String)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyFourFacetVertexCells as F','open import RamseySingleFrameFaces using (m0; c0)',
      'open import RamseyExternalPEExamples','import RamseyExternalSeedPolicyExamples as Policy',
      'import RamseyOccurrenceEquivalence as O','import RamseyExternalPEPolicy as GP',
      'open import RamseyExternalPolicyTransport',
      'ComplementChart : C.Chart → Type']
    for c in range(24):lines += [f'ComplementChart C.q{c} = '+('Unit' if c==7 else '⊥')]
    lines += ['PairAllowed BaseAllowed ComplementAllowed : P.S.InputIndex → Type',
      'PairAllowed s = Policy.PairChart (fst s)','BaseAllowed s = Policy.BaseChart (fst s)',
      'ComplementAllowed s = ComplementChart (fst s)',
      'payload : P.S.InputIndex → String','payload = λ { (c , (v , p)) → E.A.vertex-packet c v p }',
      'module Complement = GP.Policy P.S.InputIndex payload ComplementAllowed',
      'module PairTransfer = Transfer P.S.InputIndex payload PairAllowed PairAllowed',
      'module BaseTransfer = Transfer P.S.InputIndex payload BaseAllowed ComplementAllowed',
      'module ComplementTransfer = Transfer P.S.InputIndex payload ComplementAllowed BaseAllowed',
      'pair-back : {x y : P.S.InputIndex} → O.Transports x y → PairAllowed y → PairAllowed x']
    for c in [0,7]:
        for v in range(4):lines += [f'pair-back (O.input-{c}-{v} p) allowed = tt']
    lines += ['base-back : {x y : P.S.InputIndex} → O.Transports x y → BaseAllowed y → ComplementAllowed x']
    for c in [0,7]:
        for v in range(4):lines += [f'base-back (O.input-{c}-{v} p) '+('allowed = tt' if c==7 else '()')]
    lines += ['complement-back : {x y : P.S.InputIndex} → O.Transports x y → ComplementAllowed y → BaseAllowed x']
    for c in [0,7]:
        for v in range(4):lines += [f'complement-back (O.input-{c}-{v} p) '+('allowed = tt' if c==0 else '()')]
    for t in itertools.permutations(range(4),3):
        n=tag(t);u=tag(tuple(S[i] for i in t))
        for stem,module,src,dst,law in [('pair','PairTransfer','Policy.Pair','Policy.Pair','pair-back'),('base','BaseTransfer','Policy.Base','Complement','base-back'),('complement','ComplementTransfer','Complement','Policy.Base','complement-back')]:
            lines += [f'{stem}-{n} : {src}.Good tree-{n} → {dst}.Good tree-{u}',
              f'{stem}-{n} = {module}.transfer tree-{n} tree-{u} O.move-{u} (λ o → {law} (O.origin-{u} o))']
        lines += [f'transported-good-{n} : Policy.Pair.Good tree-{u}',f'transported-good-{n} = pair-{n} Policy.pair-good-{n}',
          f'transported-native-{n} : Policy.Pair.R.Resolve (P.T.encode tree-{u})',
          f'transported-native-{n} = Policy.Pair.realize tree-{u} transported-good-{n}']
    lines += ['source-leaf : P.T.Tree','source-leaf = P.port C.q0 m0 F.vp-0-1',
      'target-leaf : P.T.Tree','target-leaf = P.port C.q7 c0 F.vp-1-0',
      'source-leaf-good : Policy.Base.Good source-leaf','source-leaf-good = tt',
      'target-leaf-good : Complement.Good target-leaf',
      'target-leaf-good = BaseTransfer.transfer source-leaf target-leaf (λ _ → tt) (λ _ → base-back (O.input-7-0 F.vp-1-0)) source-leaf-good',
      'not-base-target : Policy.Base.Good target-leaf → ⊥','not-base-target allowed = allowed']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyPolicyTransportExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyPolicyTransportBadPromotion.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPolicyTransportBadPromotion where
import RamseyExternalSeedPolicyExamples as Policy
open import RamseyPolicyTransportExamples
bad : Policy.Base.Good target-leaf
bad = target-leaf-good
''',encoding='utf-8')
    return priors

def main():
    priors=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-occurrence-equivalence','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-external-seed-policy','ramsey-external-pe','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyExternalPolicyTransport',BASE/'agda',True),('RamseyPolicyTransportExamples',FIX,True),('RamseyPolicyTransportBadPromotion',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins={}
    for path in priors:
        for p,h in json.loads(path.read_text())['source_sha256'].items():
            assert p not in pins or pins[p]==h
            pins[p]=h
    for p in [*priors,Path(__file__),BASE/'contracts/ramsey-policy-transport-attempt.v1.json',BASE/'agda/RamseyExternalPolicyTransport.agda',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-policy-transport.verification.v1','status':'passed','scope_id':'full-occurrence-admission-policy-transport-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'genericAllPrerequisitePolicyTransfer':True,'twoChartGoodTransfers':24,'singletonExchangeTransfers':48,
      'transportedRestrictedNativeRealizations':24,'nonvacuousSingletonLeafExchange':True,
      'baseOnlyTargetLeafRefuted':True,'policyPromotionHostileRejected':True,
      'unselectedEPrerequisitesOmitted':False,'arbitraryNativeResolveTransportClaimed':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-policy-transport-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

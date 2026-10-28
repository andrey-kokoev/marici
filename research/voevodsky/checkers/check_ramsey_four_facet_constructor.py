"""Actual four-facet constructor comparisons and compiled middle-premise seams."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-four-facet-constructor'
S=[1,0,3,2];V=['c0','m0','c1','m1'];CH=[0,7,0,7];FR={0:'base',7:'complement'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tag(t):return '-'.join(map(str,t))
def cs(t):return ' '.join('C.q'+str(CH[f]) for f in t)
def index(piece,t):return 'P.S.'+piece+'-index '+' '.join('{'+n+' = C.q'+str(CH[f])+'}' for n,f in zip(['a','b','c'],t))+' F.triple-'+tag(t)
def prepare():
    priors=[BASE/'results'/f'{n}-v1.json' for n in ['ramsey-pe-constructor-comparison','ramsey-occurrence-equivalence','ramsey-different-edge-transport']]
    for path in priors:
        d=json.loads(path.read_text());assert d['status']=='passed'
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale constructor input '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyFourFacetConstructor where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.Equiv using (_≃_; idEquiv)',
      'open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)',
      'open import Agda.Builtin.String using (String)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyEndpointPolicy using (base; complement)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E','import RamseyFourFacetVertexCells as F',
      'import RamseyPermitEquivalence as M','import RamseyCommonSelection as K','import RamseyOccurrenceEquivalence as O',
      'open import RamseyExternalPEExamples','open import RamseyPEConstructorComparison',
      'payload : P.S.InputIndex → String','payload = λ { (c , (v , p)) → E.A.vertex-packet c v p }',
      'module D = Compare P.S.InputIndex payload O.Transports']
    pairs=list(itertools.product([0,7],repeat=2))
    for c,d in pairs:
        name=f'{c}-{d}';forward=f'K.vertex-move {FR[c]} {FR[d]}';back=f'K.vertex-move {FR[7-c]} {FR[7-d]}'
        lines += [f'square-{name} : (x : P.S.Common C.q{c} C.q{d}) → {back} ({forward} x) ≡ x']
        for v,vn in enumerate(V):lines += [f'square-{name} ({vn} , (p , q)) i = {vn} , (M.square-{c}-{v} p i , M.square-{d}-{v} q i)']
    for c,d in pairs:
        name=f'{c}-{d}';forward=f'K.vertex-move {FR[c]} {FR[d]}';back=f'K.vertex-move {FR[7-c]} {FR[7-d]}'
        src=f'C.q{c} C.q{d}';dst=f'C.q{7-c} C.q{7-d}'
        lines += [f'common-{name} : P.S.Common {src} ≃ P.S.Common {dst}',f'common-{name} = isoToEquiv (iso ({forward}) ({back}) square-{7-c}-{7-d} square-{name})',
          f'leg-{name} : (x : P.S.Common {src}) (side : P.S.Side) → D.Correspondence (P.leg {src} x side) (P.leg {dst} ({forward} x) side)']
        for v,vn in enumerate(V):
            for side,k,p in [('source-leg',c,'p'),('target-leg',d,'q')]:
                lines += [f'leg-{name} ({vn} , (p , q)) P.S.{side} = D.leaf (C.q{k} , ({vn} , {p})) (C.q{7-k} , ({V[S[v]]} , M.move-{k}-{v} {p})) (O.input-{k}-{v} {p})']
        lines += [f'pair-{name} : (x : P.S.Common {src}) → D.Correspondence (P.pair {src} x) (P.pair {dst} ({forward} x))',
          f'pair-{name} x = D.product P.S.Side P.S.Side (idEquiv P.S.Side) (P.leg {src} x) (P.leg {dst} ({forward} x)) (leg-{name} x)',
          f'selected-{name} : (x : P.S.Common {src}) → D.Correspondence (P.selected {src} x) (P.selected {dst} ({forward} x))',
          f'selected-{name} x = D.selection (P.S.Common {src}) (P.S.Common {dst}) common-{name} (P.pair {src}) (P.pair {dst}) x ({forward} x) refl pair-{name}']
    triples=list(itertools.permutations(range(4),3))
    for t in triples:
        a,b,c=t;n=tag(t);target=tuple(S[i] for i in t);u=tag(target);v=next(i for i in range(4) if i not in t)
        f=f'P.piece {cs(t)} F.triple-{n}';g=f'P.piece {cs(target)} F.triple-{u}'
        lines += [f'piece-{n} : (part : P.S.Piece) → D.Correspondence ({f} part) ({g} part)']
        for piece,(x,y) in [('ab',(a,b)),('bc',(b,c)),('ac',(a,c))]:lines += [f'piece-{n} P.S.{piece.upper()} = selected-{CH[x]}-{CH[y]} ({index(piece,t)})']
        branch='λ { '+' ; '.join(f'P.S.{port} → D.leaf _ _ (O.input-{CH[x]}-{v} F.vp-{x}-{v})' for x,port in zip(t,['first-port','middle-port','final-port']))+' }'
        lines += [f'piece-{n} P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole {cs(t)} F.triple-{n}) (P.whole {cs(target)} F.triple-{u}) ({branch})',
          f'comparison-{n} : D.Correspondence tree-{n} tree-{u}',
          f'comparison-{n} = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) ({f}) ({g}) piece-{n}',
          f'compiled-{n} : D.NativeComparison (D.closed tree-{n}) (D.closed tree-{u})',f'compiled-{n} = D.compile comparison-{n}',
          f'outer-premises-{n} : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-{n}) (lift part)) (D.T.R.premise (D.closed tree-{u}) (lift part))',
          f'outer-premises-{n} = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) ({f}) ({g}) piece-{n}']
    for t in triples:
        n=tag(t)
        for piece,side in [('ab','target-leg'),('bc','source-leg')]:
            lines += [f'middle-{piece}-{n} : D.T.R.Closed',
              f'middle-{piece}-{n} = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-{n}) (lift P.S.{piece.upper()})) (lift ({index(piece,t)}))) (lift P.S.{side})']
        lines += [f'compiled-middle-seam-{n} : middle-ab-{n} ≡ middle-bc-{n}',f'compiled-middle-seam-{n} = refl']
    for t in triples:
        a,b,c=t;n=tag(t);u=tag(tuple(S[i] for i in t))
        for piece,x,y,side in [('ab',a,b,'target-leg'),('bc',b,c,'source-leg')]:
            lines += [f'middle-comparison-{piece}-{n} : D.NativeComparison middle-{piece}-{n} middle-{piece}-{u}',
              f'middle-comparison-{piece}-{n} = D.compile (leg-{CH[x]}-{CH[y]} ({index(piece,t)}) P.S.{side})']
        lines += [f'middle-comparison-agreement-{n} : middle-comparison-ab-{n} ≡ middle-comparison-bc-{n}',f'middle-comparison-agreement-{n} = refl']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyFourFacetConstructor.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyFourFacetConstructorBadIdentity.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFourFacetConstructorBadIdentity where
open import RamseyExternalPEExamples
open import RamseyFourFacetConstructor
bad : D.Correspondence tree-0-1-2 tree-0-1-2
bad = comparison-0-1-2
''',encoding='utf-8')
    return priors

def main():
    priors=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-occurrence-equivalence','ramsey-external-pe','ramsey-common-selection','ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyFourFacetConstructor',True),('RamseyFourFacetConstructorBadIdentity',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins={}
    for path in priors:
        for p,h in json.loads(path.read_text())['source_sha256'].items():
            assert p not in pins or pins[p]==h
            pins[p]=h
    for p in [*priors,Path(__file__),BASE/'contracts/ramsey-four-facet-constructor-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-four-facet-constructor.verification.v1','status':'passed','scope_id':'actual-four-facet-PE-constructor-comparisons-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'fullCommonIndexEquivalences':4,'actualConstructorComparisons':24,'actualCompiledNativeComparisons':24,
      'allEPrerequisitesCompared':True,'compiledMiddleDerivationSeams':24,'middlePremiseComparisons':48,'middleComparisonAgreementCells':24,
      'transportAsIdentityHostileRejected':True,'nativeComparisonIsOwnerLocalRelation':True,
      'wholeNativeDerivationEqualityClaimed':False,'arbitraryNativeResolveTransportClaimed':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-four-facet-constructor-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

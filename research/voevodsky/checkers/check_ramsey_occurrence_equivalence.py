"""Full dependent P/E occurrence equivalences, not just canonical support."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-occurrence-equivalence'
V=['c0','m0','c1','m1'];S=[1,0,3,2];CH=[0,7,0,7]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tag(t):return '-'.join(map(str,t))
def occurrence(piece,v,p='p',q='q',side='side'):
    return f'(P.S.{piece} , (({V[v]} , ({p} , {q})) , ({side} , tt)))'
def full(port):return f'(P.S.full-source , ({port} , tt))'
def pieces(t):return [('AB',(t[0],t[1])),('BC',(t[1],t[2])),('AC',(t[0],t[2]))]
def prepare():
    priors=[BASE/'results'/f'{n}-v1.json' for n in ['ramsey-permit-equivalence','ramsey-diagram-involution']]
    for path in priors:
        d=json.loads(path.read_text());assert d['status']=='passed'
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale input '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyOccurrenceEquivalence where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.Equiv using (_≃_)',
      'open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)','open import Cubical.Data.Unit.Base using (tt)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyFourFacetVertexCells as F','import RamseyPermitEquivalence as M','open import RamseyExternalPEExamples',
      'data Transports : P.S.InputIndex → P.S.InputIndex → Type where']
    for c in [0,7]:
        for v in range(4):lines += [f'  input-{c}-{v} : (p : E.A.VertexPermit C.q{c} {V[v]}) → Transports (C.q{c} , ({V[v]} , p)) (C.q{7-c} , ({V[S[v]]} , M.move-{c}-{v} p))']
    triples=list(itertools.permutations(range(4),3))
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t))
        lines += [f'move-{n} : P.T.Occurrence tree-{n} → P.T.Occurrence tree-{u}']
        for piece,(a,b) in pieces(t):
            for v in range(4):
                for side in ['P.S.source-leg','P.S.target-leg']:
                    lines += [f'move-{n} {occurrence(piece,v,side=side)} = {occurrence(piece,S[v],f"M.move-{CH[a]}-{v} p",f"M.move-{CH[b]}-{v} q",side)}']
        for port in ['P.S.first-port','P.S.middle-port','P.S.final-port']:lines += [f'move-{n} {full(port)} = {full(port)}']
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t))
        lines += [f'square-{n} : (o : P.T.Occurrence tree-{n}) → move-{u} (move-{n} o) ≡ o']
        for piece,(a,b) in pieces(t):
            for v in range(4):
                for side in ['P.S.source-leg','P.S.target-leg']:
                    lines += [f'square-{n} {occurrence(piece,v,side=side)} i = {occurrence(piece,v,f"M.square-{CH[a]}-{v} p i",f"M.square-{CH[b]}-{v} q i",side)}']
        for port in ['P.S.first-port','P.S.middle-port','P.S.final-port']:lines += [f'square-{n} {full(port)} = refl']
    for t in triples:
        n=tag(t);u=tag(tuple(S[i] for i in t));remaining=next(v for v in range(4) if v not in t)
        lines += [f'equiv-{n} : P.T.Occurrence tree-{n} ≃ P.T.Occurrence tree-{u}',f'equiv-{n} = isoToEquiv (iso move-{n} move-{u} square-{u} square-{n})',
          f'origin-{n} : (o : P.T.Occurrence tree-{n}) → Transports (P.T.origin tree-{n} o) (P.T.origin tree-{u} (move-{n} o))']
        for piece,(a,b) in pieces(t):
            for v in range(4):
                for side,c,p in [('source-leg',CH[a],'p'),('target-leg',CH[b],'q')]:
                    lines += [f'origin-{n} {occurrence(piece,v,side="P.S."+side)} = input-{c}-{v} {p}']
        for a,port in zip(t,['first-port','middle-port','final-port']):
            lines += [f'origin-{n} {full("P.S."+port)} = input-{CH[a]}-{remaining} F.vp-{a}-{remaining}']
        for piece,(a,b) in pieces(t):
            for side in ['source-leg','target-leg']:
                source=occurrence(piece,remaining,f'F.vp-{a}-{remaining}',f'F.vp-{b}-{remaining}','P.S.'+side)
                target=occurrence(piece,S[remaining],f'F.vp-{S[a]}-{S[remaining]}',f'F.vp-{S[b]}-{S[remaining]}','P.S.'+side)
                name=f'selected-{n}-{piece}-{side}'
                lines += [f'{name} : move-{n} {source} ≡ {target}',f'{name} = refl']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyOccurrenceEquivalence.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyOccurrenceEquivalenceBadSelection.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOccurrenceEquivalenceBadSelection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (m0; c1)
import RamseyFourFacetVertexCells as F
open import RamseyExternalPEExamples
open import RamseyOccurrenceEquivalence
bad : move-0-1-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
  ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
bad = refl
''',encoding='utf-8')
    return priors

def main():
    priors=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-external-pe','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyOccurrenceEquivalence',True),('RamseyOccurrenceEquivalenceBadSelection',False)]:
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
    for p in [*priors,Path(__file__),BASE/'contracts/ramsey-occurrence-equivalence-attempt.v1.json',BASE/'agda/RamseyExternalPE.agda',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-occurrence-equivalence.verification.v1','status':'passed','scope_id':'full-dependent-four-facet-occurrence-involution-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'fullOccurrenceEquivalences':24,'arbitraryOccurrenceRoundTrips':24,'arbitrarySourceOriginTransportLaws':24,
      'selectedOccurrenceAgreementCells':144,'unselectedEPrerequisitesRetained':True,
      'unselectedBranchCollapseHostileRejected':True,'rawPackageEqualityProved':False,
      'nativeOperationAdded':False,'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-occurrence-equivalence-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

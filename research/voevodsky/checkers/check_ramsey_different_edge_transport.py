"""Actual different-edge four-facet transport, not a common-edge surrogate."""
from pathlib import Path
import json,hashlib,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-different-edge-transport'
S=[1,0,3,2];CH=[0,7,0,7];V=['c0','m0','c1','m1'];FR=['base','complement','base','complement']
def tag(t):return '-'.join(map(str,t))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-triple-naturality-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale triple input '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyDifferentEdgeTransport where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (false; true)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyEndpointPolicy using (base; complement; side-map)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyFourFacetVertexCells as F','import RamseyCommonSelection as K',
      'import RamseyEndpointFamily as H','import RamseyTripleNaturality as T','import RamseyPermitEquivalence as M']
    for a,b in itertools.permutations(range(4),2):
        lines += [f'edge-{a}-{b} : K.edge-move {FR[a]} {FR[b]} F.edge-{a}-{b} ≡ F.edge-{S[a]}-{S[b]}',f'edge-{a}-{b} = refl']
    rows=[]
    for t in itertools.permutations(range(4),3):
        a,b,c=t;n=tag(t);u=tag(tuple(S[i] for i in t));v=next(i for i in range(4) if i not in t)
        lines += [f'triple-{n} : T.vertex-triple {FR[a]} {FR[b]} {FR[c]} F.triple-{n} ≡ F.triple-{u}',f'triple-{n} = refl']
        routeRows=[]
        for piece,(x,y) in [('ab',(a,b)),('bc',(b,c)),('ac',(a,c))]:
            ends=[i for i in range(4) if i not in [x,y]];bit=ends.index(v)
            targetEnds=[i for i in range(4) if i not in [S[x],S[y]]];targetBit=targetEnds.index(S[v])
            side=['false','true'][bit];toSide=['false','true'][targetBit];name=f'{piece}-{n}'
            source=f'F.route-{piece}-{n}';target=f'F.route-{piece}-{u}'
            lines += [f'bind-{name} : {source} ≡ H.family {FR[x]} {FR[y]} F.edge-{x}-{y} {side}',f'bind-{name} = refl',
              f'side-{name} : side-map (fst F.edge-{x}-{y}) {side} ≡ {toSide}',f'side-{name} = refl',
              f'route-{name} : K.vertex-move {FR[x]} {FR[y]} {source} ≡ {target}',f'route-{name} = refl',
              f'natural-{name} : K.vertex-move {FR[x]} {FR[y]} {source} ≡ {target}',
              f'natural-{name} = H.covariance {FR[x]} {FR[y]} F.edge-{x}-{y} {side}',
              f'coherence-{name} : route-{name} ≡ natural-{name}',
              f'coherence-{name} = H.common-set {FR[S[x]]} {FR[S[y]]} _ _ _ _']
            routeRows.append({'piece':piece,'edge':ends,'sourceSide':bit,'targetEdge':targetEnds,'targetSide':targetBit})
        midAB=f'snd (snd F.route-ab-{n})';midBC=f'fst (snd F.route-bc-{n})'
        movedAB=f'(C.q{CH[S[b]]} , ({V[S[v]]} , M.move-{CH[b]}-{v} ({midAB})))'
        movedBC=f'(C.q{CH[S[b]]} , ({V[S[v]]} , M.move-{CH[b]}-{v} ({midBC})))'
        targetAB=f'(C.q{CH[S[b]]} , (fst F.route-ab-{u} , snd (snd F.route-ab-{u})))'
        targetBC=f'(C.q{CH[S[b]]} , (fst F.route-bc-{u} , fst (snd F.route-bc-{u})))'
        # A type annotation on each source-index term pins the external observation type.
        for label,term in [('moved-ab',movedAB),('moved-bc',movedBC),('target-ab',targetAB),('target-bc',targetBC)]:
            lines += [f'{label}-{n} : E.A.V.InputIndex',f'{label}-{n} = {term}']
        lines += [f'middle-{n} : moved-ab-{n} ≡ moved-bc-{n}',f'middle-{n} = refl',
          f'middle-ab-{n} : moved-ab-{n} ≡ target-ab-{n}',f'middle-ab-{n} = refl',
          f'middle-bc-{n} : moved-bc-{n} ≡ target-bc-{n}',f'middle-bc-{n} = refl']
        def premise(x,y,route,leg):
            args=f'C.q{CH[x]} C.q{CH[y]} {route}'
            return f'E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package {args} , E.A.V.selected-proof {args}) (lift {route})) (lift E.A.V.{leg})'
        lhs=premise(S[a],S[b],f'F.route-ab-{u}','target-leg');rhs=premise(S[b],S[c],f'F.route-bc-{u}','source-leg')
        lines += [f'target-native-seam-{n} : {lhs} ≡ {rhs}',f'target-native-seam-{n} = F.middle-{u}']
        rows.append({'triple':t,'targetTriple':[S[i] for i in t],'vertex':v,'targetVertex':S[v],'routes':routeRows})
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyDifferentEdgeTransport.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyDifferentEdgeBadSide.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDifferentEdgeBadSide where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import RamseyEndpointPolicy using (base; complement)
import RamseyFourFacetVertexCells as F
import RamseyCommonSelection as K
import RamseyEndpointFamily as H
bad : K.vertex-move base complement F.route-ab-0-1-2 ≡ H.family complement base F.edge-1-0 true
bad = refl
''',encoding='utf-8')
    (FIX/'RamseyDifferentEdgeBadMiddle.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDifferentEdgeBadMiddle where
open import Cubical.Foundations.Prelude
import RamseyPermitEquivalence as M
import RamseyFourFacetVertexCells as F
bad : M.move-0-1 F.vp-2-1 ≡ M.move-0-1 F.vp-0-1
bad = refl
''',encoding='utf-8')
    return prior,rows

def main():
    prior,rows=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-triple-naturality','ramsey-endpoint-family','ramsey-common-selection','ramsey-endpoint-policy','ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyDifferentEdgeTransport',True),('RamseyDifferentEdgeBadSide',False),('RamseyDifferentEdgeBadMiddle',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-different-edge-transport-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-different-edge-transport.verification.v1','status':'passed','scope_id':'actual-different-edge-four-facet-transport-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'actualEdgeTransportCells':12,'actualVertexTripleCells':24,'actualDifferentEdgeRouteCells':72,
      'endpointSideTransportCells':72,'routeNaturalityCoherenceCells':72,
      'transportedMiddleIndexSeams':24,'middleTargetBindings':48,'existingTargetNativeMiddleSeamsChecked':24,
      'wrongEndpointSideHostileRejected':True,'middleFacetCollapseHostileRejected':True,
      'nativeDerivationTransportProved':False,'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'routes':rows,'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-different-edge-transport-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory','routes']},indent=2))
if __name__=='__main__':main()

"""Edge-only selector obstruction and a chart-aware positive control."""
from pathlib import Path
import json,hashlib,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-endpoint-policy'
EDGES=list(itertools.combinations(range(4),2));EN=['e'+str(a)+str(b) for a,b in EDGES];V=['c0','m0','c1','m1'];S=[1,0,3,2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-edge-naturality-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale edge naturality '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyEndpointPolicy where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (Bool; false; true; not)',
      'open import Cubical.Data.Bool.Properties using (false≢true)','open import Cubical.Data.Unit.Base using (tt)',
      'open import Cubical.Data.Empty.Base using (⊥)',
      'open import RamseySingleFrameFaces using (Vertex; c0; m0)',
      'open import RamseyNativeEdgeAttachments using (Edge; e01; e02; e03; e12; e13; e23; endpoint)',
      'import RamseyEdgeNaturality as N','import RamseyPermitEquivalence as M',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'edge-map : Edge → Edge']
    targets=[EDGES.index(tuple(sorted(S[v] for v in e))) for e in EDGES]
    for i,e in enumerate(EN):lines += [f'edge-map {e} = {EN[targets[i]]}']
    lines += ['side-map : Edge → Bool → Bool']
    for i,e in enumerate(EN):lines += [f'side-map {e} b = '+('not b' if i in [0,5] else 'b')]
    lines += ['Selector : Type','Selector = Edge → Bool','turn : Selector → Selector','turn s e = side-map e (s (edge-map e))',
      'not-square : (b : Bool) → not (not b) ≡ b','not-square false = refl','not-square true = refl',
      'turn-square-at : (s : Selector) (e : Edge) → turn (turn s) e ≡ s e']
    for i,e in enumerate(EN):lines += [f'turn-square-at s {e} = '+(f'not-square (s {e})' if i in [0,5] else 'refl')]
    lines += ['turn-square : (s : Selector) → turn (turn s) ≡ s','turn-square s = funExt (turn-square-at s)',
      'covariant : (s : Selector) (e : Edge) → N.vertex-map (endpoint (s e) e) ≡ endpoint (turn s (edge-map e)) (edge-map e)']
    for e in EN:lines += [f'covariant s {e} with s {e}','... | false = refl','... | true = refl']
    lines += ['not-fixed : (b : Bool) → not b ≡ b → ⊥','not-fixed false p = false≢true (sym p)','not-fixed true p = false≢true p',
      'no-fixed-selector : (s : Selector) → turn s ≡ s → ⊥','no-fixed-selector s p = not-fixed (s e01) (cong (λ f → f e01) p)',
      'fixed-endpoint-obstruction : (b : Bool) → N.vertex-map (endpoint b e01) ≡ endpoint b e01 → ⊥',
      'fixed-endpoint-obstruction false p = transport (cong (M.Is c0) (sym p)) tt',
      'fixed-endpoint-obstruction true p = transport (cong (M.Is m0) (sym p)) tt',
      'no-geometric-selector : (s : Selector) → ((e : Edge) → N.vertex-map (endpoint (s e) e) ≡ endpoint (s (edge-map e)) (edge-map e)) → ⊥',
      'no-geometric-selector s law = fixed-endpoint-obstruction (s e01) (law e01)',
      'data Frame : Type where','  base complement : Frame','swap : Frame → Frame','swap base = complement','swap complement = base',
      'choose : Frame → Selector','choose base e = false','choose complement e = side-map e false',
      'context-covariant : (f : Frame) (e : Edge) → N.vertex-map (endpoint (choose f e) e) ≡ endpoint (choose (swap f) (edge-map e)) (edge-map e)']
    for f in ['base','complement']:
        for e in EN:lines += [f'context-covariant {f} {e} = refl']
    for c in [0,7]:
        for i,e in enumerate(EN):
            side=1 if c==7 and i in [0,5] else 0;v=EDGES[i][side];j=targets[i];ts=EDGES[j].index(S[v]);name=f'context-restrict-{c}-{i}'
            lines += [f'{name} : (p : E.A.EdgePermit C.q{c} {e}) → M.move-{c}-{v} (E.A.restrict {["false","true"][side]} C.q{c} {e} p) ≡ E.A.restrict {["false","true"][ts]} C.q{7-c} {EN[j]} (N.move-{c}-{i} p)',f'{name} = N.restrict-{c}-{i}-{side}']
    lines += ['left-selector : Selector','left-selector e = false']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyEndpointPolicy.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyEndpointPolicyBadFixed.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointPolicyBadFixed where
open import Cubical.Foundations.Prelude
open import RamseyEndpointPolicy
bad : turn left-selector ≡ left-selector
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-edge-naturality','ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyEndpointPolicy',True),('RamseyEndpointPolicyBadFixed',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-endpoint-policy-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-endpoint-policy.verification.v1','status':'passed','scope_id':'edge-only-selector-obstruction-and-chart-aware-transport-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'selectorTransportInvolutive':True,'arbitrarySelectorCovariance':True,'invariantEdgeOnlySelectorRefuted':True,
      'geometricEdgeOnlySelectorRefuted':True,'chartAwareCovarianceCells':12,'actualPermitRestrictionLaws':12,
      'fixedSelectorHostileRejected':True,'chartAwareSelectionRefuted':False,
      'nativeOperationAdded':False,'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-endpoint-policy-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

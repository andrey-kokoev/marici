"""Full edge-permit equivalence and endpoint-order-sensitive restriction naturality."""
from pathlib import Path
import json,hashlib,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-edge-naturality'
V=['c0','m0','c1','m1'];S=[1,0,3,2];CH=[0,7,0,7];EDGES=list(itertools.combinations(range(4),2));EN=['e'+str(a)+str(b) for a,b in EDGES]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-permit-equivalence-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale permit evidence '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyEdgeNaturality where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.HLevels',
      'open import Cubical.Foundations.Equiv using (_≃_)','open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)',
      'open import Cubical.Data.Nat.Properties using (isSetℕ)','open import Cubical.Data.Sigma.Properties using (Σ≡Prop)',
      'open import Cubical.Data.Bool.Base using (false; true)','import Cubical.Data.Empty as Empty',
      'open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)',
      'open import RamseyNativeEdgeAttachments using (Edge; e01; e02; e03; e12; e13; e23; InFace; endpoint)',
      'open import RamseyPermitFibers using (membership-prop)',
      'import RamseyPermitEquivalence as M','import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'edge-fiber-prop : (c : C.Chart) (e : Edge) (f : Vertex) → isProp (Σ (C.Permit c f) (λ _ → Σ (InFace (endpoint false e) f) (λ _ → InFace (endpoint true e) f)))',
      'edge-fiber-prop c e f = isPropΣ (isSetℕ _ _) (λ _ → isPropΣ (membership-prop (endpoint false e) f) (λ _ → membership-prop (endpoint true e) f))',
      'same-edge-facet : (c : C.Chart) (e : Edge) (p q : E.A.EdgePermit c e) → fst p ≡ fst q → p ≡ q',
      'same-edge-facet c e p q = Σ≡Prop (edge-fiber-prop c e)',
      'vertex-map : Vertex → Vertex']
    for v in range(4):lines += [f'vertex-map {V[v]} = {V[S[v]]}']
    ids=[(c,e) for c in [0,7] for e in range(6)]
    def valid(c,e):return [f for f in range(4) if CH[f]==c and f not in EDGES[e]]
    def invalid(c,e,f):
        if CH[f]!=c:return 'Empty.rec (M.wrong-count permit)'
        a,b=EDGES[e];return f'Empty.rec (M.self-free {V[f]} '+('left)' if f==a else 'right)')
    for c,e in ids:
        t=f'{c}-{e}';fs=valid(c,e);ptype=f'E.A.EdgePermit C.q{c} {EN[e]}'
        lines += [f'data Code-{t} : Type where']
        if fs:lines += ['  '+' '.join(f'k{t}-{f}' for f in fs)+f' : Code-{t}']
        lines += [f'decode-{t} : Code-{t} → {ptype}']
        for f in fs:lines += [f'decode-{t} k{t}-{f} = E.att-{c}-{f}-{e}']
        if not fs:lines += [f'decode-{t} ()']
        lines += [f'encode-{t} : {ptype} → Code-{t}']
        for f in range(4):lines += [f'encode-{t} ({V[f]} , (permit , (left , right))) = '+(f'k{t}-{f}' if f in fs else invalid(c,e,f))]
        lines += [f'encode-decode-{t} : (k : Code-{t}) → encode-{t} (decode-{t} k) ≡ k']
        for f in fs:lines += [f'encode-decode-{t} k{t}-{f} = refl']
        if not fs:lines += [f'encode-decode-{t} ()']
        lines += [f'decode-encode-{t} : (p : {ptype}) → decode-{t} (encode-{t} p) ≡ p']
        for f in range(4):
            p=f'({V[f]} , (permit , (left , right)))'
            rhs=f'sym (same-edge-facet C.q{c} {EN[e]} {p} E.att-{c}-{f}-{e} refl)' if f in fs else invalid(c,e,f)
            lines += [f'decode-encode-{t} {p} = {rhs}']
    for c,e in ids:
        target=EDGES.index(tuple(sorted(S[v] for v in EDGES[e])));t=f'{c}-{e}';u=f'{7-c}-{target}';fs=valid(c,e)
        lines += [f'code-move-{t} : Code-{t} → Code-{u}']
        for f in fs:lines += [f'code-move-{t} k{t}-{f} = k{u}-{S[f]}']
        if not fs:lines += [f'code-move-{t} ()']
        lines += [f'move-{t} : E.A.EdgePermit C.q{c} {EN[e]} → E.A.EdgePermit C.q{7-c} {EN[target]}',f'move-{t} p = decode-{u} (code-move-{t} (encode-{t} p))']
    for c,e in ids:
        target=EDGES.index(tuple(sorted(S[v] for v in EDGES[e])));t=f'{c}-{e}';u=f'{7-c}-{target}';fs=valid(c,e)
        lines += [f'code-square-{t} : (k : Code-{t}) → code-move-{u} (code-move-{t} k) ≡ k']
        for f in fs:lines += [f'code-square-{t} k{t}-{f} = refl']
        if not fs:lines += [f'code-square-{t} ()']
        lines += [f'square-{t} : (p : E.A.EdgePermit C.q{c} {EN[e]}) → move-{u} (move-{t} p) ≡ p',
          f'square-{t} p = cong (λ k → decode-{t} (code-move-{u} k)) (encode-decode-{u} (code-move-{t} (encode-{t} p))) ∙ cong decode-{t} (code-square-{t} (encode-{t} p)) ∙ decode-encode-{t} p']
    for c,e in ids:
        target=EDGES.index(tuple(sorted(S[v] for v in EDGES[e])));t=f'{c}-{e}';u=f'{7-c}-{target}';fs=valid(c,e)
        lines += [f'equiv-{t} : E.A.EdgePermit C.q{c} {EN[e]} ≃ E.A.EdgePermit C.q{7-c} {EN[target]}',f'equiv-{t} = isoToEquiv (iso move-{t} move-{u} square-{u} square-{t})']
        for f in fs:lines += [f'canonical-{c}-{f}-{e} : move-{t} E.att-{c}-{f}-{e} ≡ E.att-{7-c}-{S[f]}-{target}',f'canonical-{c}-{f}-{e} = refl']
        for side in [0,1]:
            v=EDGES[e][side];toSide=EDGES[target].index(S[v]);s=['false','true'][side];ts=['false','true'][toSide];name=f'restrict-{t}-{side}'
            lines += [f'{name} : (p : E.A.EdgePermit C.q{c} {EN[e]}) → M.move-{c}-{v} (E.A.restrict {s} C.q{c} {EN[e]} p) ≡ E.A.restrict {ts} C.q{7-c} {EN[target]} (move-{t} p)']
            for f in range(4):lines += [f'{name} ({V[f]} , (permit , (left , right))) = '+('refl' if f in fs else invalid(c,e,f))]
    for e,(a,b) in enumerate(EDGES):
        target=EDGES.index(tuple(sorted([S[a],S[b]])))
        for side,v in enumerate([a,b]):
            ts=EDGES[target].index(S[v]);name=f'endpoint-{e}-{side}'
            lines += [f'{name} : vertex-map (endpoint {["false","true"][side]} {EN[e]}) ≡ endpoint {["false","true"][ts]} {EN[target]}',f'{name} = refl']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyEdgeNaturality.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyEdgeNaturalityBadOrder.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeNaturalityBadOrder where
open import Cubical.Data.Bool.Base using (false)
open import RamseySingleFrameFaces using (m0)
open import RamseyNativeEdgeAttachments using (e01)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
open import RamseyEdgeNaturality
bad : E.A.VertexPermit C.q7 m0
bad = E.A.restrict false C.q7 e01 (move-0-0 E.att-0-2-0)
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-permit-equivalence','ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyEdgeNaturality',True),('RamseyEdgeNaturalityBadOrder',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-edge-naturality-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-edge-naturality.verification.v1','status':'passed','scope_id':'full-edge-permit-restriction-naturality-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'fullEdgePermitEquivalences':12,'emptyEdgePermitTypes':2,'arbitraryEdgeRoundTrips':12,
      'canonicalAgreementCells':12,'arbitraryRestrictionNaturalityLaws':24,'emptyDomainNaturalityLaws':4,
      'endpointTransportCells':12,'endpointReversingEdges':['e01','e23'],'omittedEndpointFlipHostileRejected':True,
      'nativeOperationAdded':False,'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-edge-naturality-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

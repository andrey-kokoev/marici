"""Full permit classification and complementary transport, preserving facet choices."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-permit-equivalence'
V=['c0','m0','c1','m1'];S=[1,0,3,2];CH=[0,7,0,7]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-permit-fibers-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale permit fibers '+p
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyPermitEquivalence where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.Equiv using (_≃_)','open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)',
      'open import Cubical.Data.Nat.Base using (ℕ; zero; suc)',
      'open import Cubical.Data.Unit.Base using (Unit; tt)','open import Cubical.Data.Empty.Base using (⊥)',
      'import Cubical.Data.Empty as Empty','open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)',
      'open import RamseyUniformRelative using (first; next)','open import RamseyNativeEdgeAttachments using (InFace)',
      'open import RamseyPermitFibers using (same-facet)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E','import RamseyFourFacetVertexCells as F',
      'Tag : ℕ → Type','Tag zero = Unit','Tag (suc zero) = Unit','Tag (suc (suc n)) = ⊥',
      'wrong-count : 1 ≡ 2 → ⊥','wrong-count p = transport (cong Tag p) tt',
      'Is : Vertex → Vertex → Type']
    for a in V:
        for b in V:lines += [f'Is {a} {b} = '+('Unit' if a==b else '⊥')]
    lines += ['self-free : (v : Vertex) → InFace v v → ⊥']
    for v in V:
        for slot in ['first','(next first)','(next (next first))']:
            lines += [f'self-free {v} ({slot} , p) = transport (cong (Is {v}) (sym p)) tt']
        lines += [f'self-free {v} (next (next (next ())) , p)']
    ids=[(c,v) for c in [0,7] for v in range(4)]
    for c,v in ids:
        t=f'{c}-{v}';valid=[f for f in range(4) if CH[f]==c and f!=v];ptype=f'E.A.VertexPermit C.q{c} {V[v]}'
        lines += [f'data Code-{t} : Type where','  '+' '.join(f'k{t}-{f}' for f in valid)+f' : Code-{t}',f'decode-{t} : Code-{t} → {ptype}']
        for f in valid:lines += [f'decode-{t} k{t}-{f} = F.vp-{f}-{v}']
        lines += [f'encode-{t} : {ptype} → Code-{t}']
        for f in range(4):
            rhs=f'k{t}-{f}' if f in valid else ('Empty.rec (wrong-count permit)' if CH[f]!=c else f'Empty.rec (self-free {V[v]} member)')
            lines += [f'encode-{t} ({V[f]} , (permit , member)) = {rhs}']
        lines += [f'encode-decode-{t} : (k : Code-{t}) → encode-{t} (decode-{t} k) ≡ k']
        for f in valid:lines += [f'encode-decode-{t} k{t}-{f} = refl']
        lines += [f'decode-encode-{t} : (p : {ptype}) → decode-{t} (encode-{t} p) ≡ p']
        for f in range(4):
            p=f'({V[f]} , (permit , member))'
            rhs=f'sym (same-facet C.q{c} {V[v]} {p} F.vp-{f}-{v} refl)' if f in valid else ('Empty.rec (wrong-count permit)' if CH[f]!=c else f'Empty.rec (self-free {V[v]} member)')
            lines += [f'decode-encode-{t} {p} = {rhs}']
        lines += [f'classification-{t} : {ptype} ≃ Code-{t}',f'classification-{t} = isoToEquiv (iso encode-{t} decode-{t} encode-decode-{t} decode-encode-{t})']
    for c,v in ids:
        t=f'{c}-{v}';u=f'{7-c}-{S[v]}';valid=[f for f in range(4) if CH[f]==c and f!=v]
        lines += [f'code-move-{t} : Code-{t} → Code-{u}']
        for f in valid:lines += [f'code-move-{t} k{t}-{f} = k{u}-{S[f]}']
        lines += [f'move-{t} : E.A.VertexPermit C.q{c} {V[v]} → E.A.VertexPermit C.q{7-c} {V[S[v]]}',f'move-{t} p = decode-{u} (code-move-{t} (encode-{t} p))']
    for c,v in ids:
        t=f'{c}-{v}';u=f'{7-c}-{S[v]}';valid=[f for f in range(4) if CH[f]==c and f!=v]
        lines += [f'code-square-{t} : (k : Code-{t}) → code-move-{u} (code-move-{t} k) ≡ k']
        for f in valid:lines += [f'code-square-{t} k{t}-{f} = refl']
        lines += [f'square-{t} : (p : E.A.VertexPermit C.q{c} {V[v]}) → move-{u} (move-{t} p) ≡ p',
          f'square-{t} p = cong (λ k → decode-{t} (code-move-{u} k)) (encode-decode-{u} (code-move-{t} (encode-{t} p))) ∙ cong decode-{t} (code-square-{t} (encode-{t} p)) ∙ decode-encode-{t} p']
    for c,v in ids:
        t=f'{c}-{v}';u=f'{7-c}-{S[v]}'
        lines += [f'equiv-{t} : E.A.VertexPermit C.q{c} {V[v]} ≃ E.A.VertexPermit C.q{7-c} {V[S[v]]}',f'equiv-{t} = isoToEquiv (iso move-{t} move-{u} square-{u} square-{t})']
        for f in range(4):
            if CH[f]==c and f!=v:lines += [f'canonical-{f}-{v} : move-{t} F.vp-{f}-{v} ≡ F.vp-{S[f]}-{S[v]}',f'canonical-{f}-{v} = refl']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyPermitEquivalence.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyPermitEquivalenceBadFacet.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitEquivalenceBadFacet where
open import Cubical.Foundations.Prelude
import RamseyFourFacetVertexCells as F
open import RamseyPermitEquivalence
bad : move-0-1 F.vp-2-1 ≡ F.vp-1-0
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-permit-fibers','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyPermitEquivalence',True),('RamseyPermitEquivalenceBadFacet',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    pins=dict(json.loads(prior.read_text())['source_sha256'])
    for p in [prior,Path(__file__),BASE/'contracts/ramsey-permit-equivalence-attempt.v1.json',*FIX.glob('*.agda')]:pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-permit-equivalence.verification.v1','status':'passed','scope_id':'full-two-chart-permit-classification-and-involution-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'fullPermitClassifications':8,'fullPermitEquivalences':8,'arbitraryPermitRoundTrips':8,'canonicalAgreementCells':12,
      'wrongFacetTransportHostileRejected':True,'wholeOccurrenceEquivalenceProved':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-permit-equivalence-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

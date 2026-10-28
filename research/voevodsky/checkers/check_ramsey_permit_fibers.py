"""Fixed-facet proof uniqueness without collapsing distinct retained facets."""
from pathlib import Path
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-permit-fibers'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-diagram-involution-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale involution '+p
    vertices=['c0','m0','c1','m1'];slots=['first','(next first)','(next (next first))']
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyPermitFibers where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.HLevels',
      'open import Cubical.Data.Nat.Base using (ℕ; zero; suc)',
      'open import Cubical.Data.Nat.Properties using (isSetℕ)',
      'open import Cubical.Data.Sigma.Properties using (Σ≡Prop)',
      'open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1; face)',
      'open import RamseyUniformRelative using (Slot; first; next)',
      'open import RamseyNativeEdgeAttachments using (InFace)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyFourFacetVertexCells as F',
      'number : Vertex → ℕ']
    for i,v in enumerate(vertices):lines += [f'number {v} = {i}']
    lines += ['vertex : ℕ → Vertex','vertex zero = c0','vertex (suc zero) = m0','vertex (suc (suc zero)) = c1','vertex (suc (suc (suc n))) = m1',
      'retract : (v : Vertex) → vertex (number v) ≡ v']
    for v in vertices:lines += [f'retract {v} = refl']
    lines += ['vertex-set : isSet Vertex','vertex-set = isSetRetract number vertex retract isSetℕ',
      'position : Vertex → Vertex → Slot 3']
    for f in vertices:
        others=[v for v in vertices if v!=f]
        for v in vertices:lines += [f'position {f} {v} = '+(slots[others.index(v)] if v!=f else 'first')]
    lines += ['position-face : (f : Vertex) (i : Slot 3) → position f (face f i) ≡ i']
    for f in vertices:
        for slot in slots:lines += [f'position-face {f} {slot} = refl']
        lines += [f'position-face {f} (next (next (next ())))']
    lines += ['face-injective : (f : Vertex) {i j : Slot 3} → face f i ≡ face f j → i ≡ j',
      'face-injective f {i} {j} p = sym (position-face f i) ∙ cong (position f) p ∙ position-face f j',
      'membership-prop : (v f : Vertex) → isProp (InFace v f)',
      'membership-prop v f (i , p) (j , q) = Σ≡Prop (λ k → vertex-set (face f k) v) (face-injective f (p ∙ sym q))',
      'facet-fiber-prop : (c : C.Chart) (v f : Vertex) → isProp (Σ (C.Permit c f) (λ _ → InFace v f))',
      'facet-fiber-prop c v f = isPropΣ (isSetℕ _ _) (λ _ → membership-prop v f)',
      'same-facet : (c : C.Chart) (v : Vertex) (p q : E.A.VertexPermit c v) → fst p ≡ fst q → p ≡ q',
      'same-facet c v p q = Σ≡Prop (facet-fiber-prop c v)',
      'facet-projection : (c : C.Chart) (v : Vertex) (p q : E.A.VertexPermit c v) → p ≡ q → fst p ≡ fst q',
      'facet-projection c v p q = cong fst']
    for f in range(4):
        for v in range(4):
            if f==v:continue
            c=[0,7,0,7][f];name=f'canonical-{f}-{v}'
            lines += [f'{name} : (p : E.A.VertexPermit C.q{c} {vertices[v]}) → fst p ≡ {vertices[f]} → p ≡ F.vp-{f}-{v}',
             f'{name} p = same-facet C.q{c} {vertices[v]} p F.vp-{f}-{v}']
    FIX.mkdir(parents=True,exist_ok=True);(FIX/'RamseyPermitFibers.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyPermitFibersBadCollapse.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitFibersBadCollapse where
open import Cubical.Foundations.Prelude
import RamseyFourFacetVertexCells as F
open import RamseyPermitFibers
bad : F.vp-0-3 ≡ F.vp-2-3
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyPermitFibers',True),('RamseyPermitFibersBadCollapse',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),BASE/'contracts/ramsey-permit-fibers-attempt.v1.json',*FIX.glob('*.agda'),
      *[BASE/'agda'/n for n in ['RamseyNativeEdgeAttachments.agda','RamseySingleFrameFaces.agda','RamseyUniformRelative.agda']],
      BASE/'fixtures/ramsey-requested-port/RamseyRequestedPortExamples.agda',
      BASE/'fixtures/ramsey-native-edge-attachments/RamseyEdgeAttachmentsExamples.agda',
      BASE/'fixtures/ramsey-four-facet-vertex-cells/RamseyFourFacetVertexCells.agda']
    out={'schema':'marici.ramsey-permit-fibers.verification.v1','status':'passed','scope_id':'fixed-facet-permit-witness-uniqueness-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'faceMembershipPropositional':True,'fixedFacetPermitFiberPropositional':True,
      'permitEqualityDeterminedByFacet':True,'canonicalNormalizationCells':12,
      'distinctFacetCollapseHostileRejected':True,'wholeOccurrenceEquivalenceProved':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-permit-fibers-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

"""Generate source-bound examples and check actual native P/E admission fresh."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
FIX=BASE/'fixtures/ramsey-native-incidence'
SOURCE=BASE/'results/ramsey-lifted-facet-incidence-v1.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def generate():
    d=json.loads(SOURCE.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale source incidence: '+p
    FIX.mkdir(parents=True,exist_ok=True)
    vs=['c0','m0','c1','m1'];world=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1']
    code='''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeIncidenceExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1; face; count)
open import RamseyNativeRetainedIncidence
role : Vertex → Vertex → ℕ
'''
    for p in d['facetPorts']:
        for i,v in enumerate(world):code+=f"role {vs[p['facet']]} {vs[i]} = {int(p['roles'][v]=='M')}\n"
    code+='''Permit : Vertex → Type
Permit p = count (λ i → role p (face p i)) ≡ 2
cert : (p : Vertex) → Permit p
'''
    for v in vs:code+=f'cert {v} = refl\n'
    code+='Inside : Vertex → Vertex → Type\n'
    for a in vs:
        for b in vs:code+=f'Inside {a} {b} = '+('⊥' if a==b else 'Unit')+'\n'
    code+='packet : (p : Vertex) → Permit p → String\n'
    for p in d['facetPorts']:
        quoted=json.dumps(json.dumps(p,sort_keys=True,separators=(',',':')))
        code+=f"packet {vs[p['facet']]} _ = {quoted}\n"
    code+='''module S = Incidence Vertex Vertex Permit Inside packet
edge : Vertex → Vertex → Bool → Vertex
edge a b false = a
edge a b true = b
data Three : Type where
  x y z : Three
triple : Vertex → Vertex → Vertex → Three → Vertex
triple a b c x = a
triple a b c y = b
triple a b c z = c
'''
    selections=0
    from itertools import combinations
    for a,b in combinations(range(4),2):
        for v in range(4):
            if v in [a,b]:continue
            name=f'e{a}{b}v{v}';parent=f'(edge {vs[a]} {vs[b]})'
            code+=f'{name} : S.Common Bool {parent}\n{name} = {vs[v]} , (λ {{ false → tt ; true → tt }})\n'
            code+=f'{name}-native : S.R.Resolve (S.selected Bool {parent} (λ i → cert ({parent} i)) {name})\n'
            code+=f'{name}-native = S.selected-proof Bool {parent} (λ i → cert ({parent} i)) {name}\n'
            selections+=1
    for a,b,c in combinations(range(4),3):
        v=next(i for i in range(4) if i not in [a,b,c]);name=f't{a}{b}{c}';parent=f'(triple {vs[a]} {vs[b]} {vs[c]})'
        code+=f'{name} : S.Common Three {parent}\n{name} = {vs[v]} , (λ {{ x → tt ; y → tt ; z → tt }})\n'
        code+=f'{name}-native : S.R.Resolve (S.selected Three {parent} (λ i → cert ({parent} i)) {name})\n'
        code+=f'{name}-native = S.selected-proof Three {parent} (λ i → cert ({parent} i)) {name}\n'
    code+='''no-fourfold : S.Common Vertex (λ p → p) → ⊥
no-fourfold (c0 , w) = w c0
no-fourfold (m0 , w) = w m0
no-fourfold (c1 , w) = w c1
no-fourfold (m1 , w) = w m1
all-parents : S.R.Resolve (S.family Vertex (λ p → p) cert)
all-parents = S.family-proof Vertex (λ p → p) cert
'''
    assert selections==12
    (FIX/'RamseyNativeIncidenceExamples.agda').write_text(code,encoding='utf-8')
    bad='''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeIncidenceBadFourfold where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
open import RamseyNativeIncidenceExamples
bad : S.Common Vertex (λ p → p)
bad = c0 , (λ { c0 → tt ; m0 → tt ; c1 → tt ; m1 → tt })
'''
    (FIX/'RamseyNativeIncidenceBadFourfold.agda').write_text(bad,encoding='utf-8')

def main():
    generate()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';library=tools/'cubical-0.9'
    owner=BASE/'agda';native=ROOT/'research/nima/agda'
    dirs=[owner,native,FIX,library,ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda)
    args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    results={}
    for name,path,positive in [('RamseyNativeRetainedIncidence',owner/'RamseyNativeRetainedIncidence.agda',True),
        ('RamseyNativeIncidenceExamples',FIX/'RamseyNativeIncidenceExamples.agda',True),
        ('RamseyNativeIncidenceBadFourfold',FIX/'RamseyNativeIncidenceBadFourfold.agda',False)]:
        run=subprocess.run(args+[str(path)],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr
        (BASE/f'results/agda-{name}.log').write_text(text,encoding='utf-8')
        results[name]=run.returncode
        if positive:
            assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda),'source changed during check'
    inputs=[SOURCE,Path(__file__),BASE/'contracts/ramsey-native-incidence-attempt.v1.json',owner/'RamseyNativeRetainedIncidence.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-native-incidence.verification.v1','status':'passed',
      'scope_id':'native-retained-parent-incidence-restriction-v1','freshSafeCubical':True,
      'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':results,
      'nativeParentFamilies':True,'typedCommonVertexSelections':True,'parentValuesAndDerivationsRetained':True,
      'reindexingCompositionProved':True,'edgeVertexSelections':12,'tripleVertexSelections':4,
      'emptyFourfoldProved':True,'falseFourfoldRejected':True,
      'sourceGeometryInterpretedInKernel':False,'fieldMatricesInterpretedInKernel':False,
      'sourceDefinedEdgeFieldObservable':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in inputs},
      'formalSourceInventory':before}
    (BASE/'results/ramsey-native-incidence-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['formalSourceInventory','source_sha256']},indent=2))
if __name__=='__main__':main()

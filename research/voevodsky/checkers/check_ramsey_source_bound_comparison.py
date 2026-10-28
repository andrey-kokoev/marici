"""Bind all four source ports to actual native derived-view constructors."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
FIX=BASE/'fixtures/ramsey-source-bound-comparison'
V='research/voevodsky/'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text())
PATHS=[V+'results/ramsey-lifted-facet-incidence-v1.json',V+'results/ramsey-trace-channel-transport-v1.json',
       V+'results/ramsey-native-incidence-v1.json',V+'results/ramsey-native-derived-comparison-v1.json']
def generate():
    incidence,transport,native,comparison=map(load,PATHS)
    for receipt in [incidence,transport,native,comparison]:
        for p,h in receipt['source_sha256'].items():assert sha(ROOT/p)==h,'stale source binding '+p
    payload={k:incidence[k] for k in ['PNTargetFieldBindings','directedEdgeRecords','orderedTripleVertexRecords']}
    payload['observationSupportContexts']=transport['observationSupports']
    payload['scope']='Retained comparison data; neither simultaneous occupancy nor kernel matrix interpretation.'
    raw=json.dumps(payload,sort_keys=True,separators=(',',':'));quoted=json.dumps(raw)
    code='''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySourceBoundComparison where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
import RamseyNativeIncidenceExamples as C
open import RamseyNativeDerivedComparison
Ports : Type
Ports = (p : Vertex) → Σ (C.Permit p) (λ _ → String)
Root : Type
Root = Σ Ports (λ _ → String)
payload : String
payload = '''+quoted+'''
actual : Root
actual = (λ p → C.cert p , C.packet p (C.cert p)) , payload
Valid : Root → Type
Valid a = a ≡ actual
View : Type
View = Σ Vertex (λ p → Σ (C.Permit p) (λ _ → String))
view : Vertex → Root → View
view p a = p , fst a p
module P = Presentations Root Vertex View Valid view
all-pairs : (f g : Vertex) → P.R.Resolve (P.comparison actual refl f g)
all-pairs f g = P.comparison-proof actual refl f g
all-compositions : (f g h : Vertex) → P.R.Resolve (P.composed actual refl f g h)
all-compositions f g h = P.composed-proof actual refl f g h
retained-context : (f g : Vertex) (x : N.Ty (P.display actual refl f))
  → snd (equivFun (P.equivalence actual refl f g) x) ≡ snd x
retained-context f g x = P.retains-parent actual refl f g x
'''
    # equivFun is not re-exported by the generic module.
    code=code.replace('open import Cubical.Foundations.Prelude\n','open import Cubical.Foundations.Prelude\nopen import Cubical.Foundations.Equiv\n',1)
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseySourceBoundComparison.agda').write_text(code,encoding='utf-8')
    (FIX/'RamseySourceBoundComparisonBadPayload.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySourceBoundComparisonBadPayload where
open import Cubical.Foundations.Prelude
open import RamseySourceBoundComparison
bad : Valid (fst actual , "")
bad = refl
''',encoding='utf-8')
    # Independent literal roundtrip ensures this is the full data, not just a digest.
    literal=next(line[len('payload = '):] for line in code.splitlines() if line.startswith('payload = '))
    assert json.loads(json.loads(literal))==payload
    return payload

def main():
    payload=generate()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';library=tools/'cubical-0.9'
    dirs=[owner,ROOT/'research/nima/agda',FIX,BASE/'fixtures/ramsey-native-incidence',library,
          ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,positive in [('RamseySourceBoundComparison',True),('RamseySourceBoundComparisonBadPayload',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if positive:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[ROOT/p for p in PATHS]+[Path(__file__),BASE/'contracts/ramsey-source-bound-comparison-attempt.v1.json',
      owner/'RamseyNativeDerivedComparison.agda',BASE/'fixtures/ramsey-native-incidence/RamseyNativeIncidenceExamples.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-source-bound-comparison.verification.v1','status':'passed',
      'scope_id':'source-bound-four-port-derived-comparison-parent-v1','freshSafeCubical':True,
      'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'retainedTypedPorts':4,'nativeComparisons':16,'nativeCompositions':64,
      'retainedDirectedEdgeRecords':len(payload['directedEdgeRecords']),
      'retainedTripleVertexRecords':len(payload['orderedTripleVertexRecords']),
      'retainedObservationContexts':len(payload['observationSupportContexts']),
      'literalSourceBindingChecked':True,'payloadOmissionRejected':True,
      'parentIsComparisonInputNotOccupiedAssembly':True,
      'kernelMatrixInterpretation':False,'differentRootPermitTransport':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-source-bound-comparison-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

"""Fresh safe Cubical closure verification of WG continuation/admission results.
Positive obstructions and universal theorems are kernel checked. Negative
fixtures must fail with a type mismatch, not merely a missing dependency.
"""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/voevodsky'
TOOLS=Path.home()/'tools/cubical-agda'
AGDA=TOOLS/'agda-2.8.0/agda.exe'
LIB=TOOLS/'cubical-0.9'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    fixtures=BASE/'fixtures/witness-generator-coherence';fixtures.mkdir(parents=True,exist_ok=True)
    header='{-# OPTIONS --safe --cubical --guardedness #-}\n'
    files={
      'WitnessGeneratorExamples':'''open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Vertex; A; Seeds)
open import InternalSourceComparisons using (package; act; exchange)
open import WitnessContinuationHistories
open import WitnessHigherControls
open import WitnessHigherAdmissionObstruction
import WitnessNativeEnvelope
import WholePackageResolution as R
open R.Generators ℓ-zero
-- Quantified checks, not a finite list of instances.
allHistories : {v : Vertex} (h : History A v)
  → Resolve Seeds (package (witness (squareState h chosen)))
allHistories = chosen-universal
reuse : {v t : Vertex} (h : History A v) (k : History (act exchange v) t)
  → Resolve Seeds (package (witness (squareState k (squareState h chosen))))
reuse h k = recursively-reusable h chosen k
higher = chosen-direct-staged
nativeHigherPath = chosen-direct-staged-native
obstruction = no-higher-package-admission
''',
      'WitnessGeneratorBadAdmissionBridge':'''open import Cubical.Foundations.Prelude
import WholePackageSigmaPi as W
import WholePackageResolution as R
open W.Universe ℓ-zero
open R.Generators ℓ-zero
open import NativeExtensionFamilyAudit using (Seeds)
open import InternalSourceComparisons using (derivation)
open import RepeatedInterchangeCoherence
-- A comparison derivation cannot be relabelled as admission of its filler atom.
bad : Resolve Seeds (pack (atom CompleteFiller) sequentialFiller)
bad = derivation (asBody sequentialFiller)
''',
      'WitnessGeneratorBadHiddenEquality':'''open import Cubical.Foundations.Prelude
open import WitnessContinuationHistories
open State
open import WitnessHigherControls
bad : selected nativeId ≡ selected nativeSwap
bad = refl
''',
      'WitnessGeneratorBadReverseDynamics':'''open import NativeExtensionFamilyAudit using (Edge; D; A; AD)
-- Reverse presentation does not supply the absent reverse execution edge.
bad : Edge D A
bad = AD
'''}
    for name,body in files.items():
        (fixtures/(name+'.agda')).write_text(header+'module '+name+' where\n'+body,encoding='utf-8')
    dirs=[BASE/'agda',ROOT/'research/strominger/agda',ROOT/'research/nima/agda',fixtures,LIB]
    def inventory():return {str(p.resolve()):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(AGDA)
    args=[str(AGDA),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    # The positive entry imports every result; ignored interfaces force a
    # fresh closure check of all of them, without four redundant replays.
    cases = [(name,fixtures,'Bad' not in name) for name in files]
    rows=[]
    for name,folder,positive in cases:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        log=run.stdout+'\n'+run.stderr;dest=BASE/('results/agda-'+name+'.log');dest.write_text(log,encoding='utf-8')
        assert 'UnsupportedIndexedMatch' not in log,log[-6000:]
        if positive:
            assert run.returncode==0,log[-6000:]
            for module in ['WitnessHigherAdmissionObstruction','WitnessContinuationHistories','WitnessHigherControls','WitnessNativeEnvelope']:
                assert 'Checking '+module+' ' in log,module+' not freshly checked'
        else:
            assert run.returncode!=0, name+' unexpectedly accepted'
            assert name+'.agda' in log and any(tag in log for tag in ['[UnequalTerms]','[UnequalTypes]','[MismatchedProjectionsError]']),log[-6000:]
        rows.append({'module':name,'expected':'pass' if positive else 'type-mismatch','exitCode':run.returncode,
          'log':dest.relative_to(ROOT).as_posix(),'log_sha256':sha(dest)})
    assert before==inventory(),'Agda input sources changed during verification'
    assert compiler==sha(AGDA),'Compiler changed during verification'
    project={Path(p).relative_to(ROOT).as_posix():h for p,h in before.items() if Path(p).is_relative_to(ROOT)}
    project[Path(__file__).relative_to(ROOT).as_posix()]=sha(Path(__file__))
    result={'status':'passed','freshSafeCubical':True,'ignoreInterfaces':True,'sourceStable':True,
      'compiler_sha256':compiler,'cases':rows,
      'priority1':'Formal impossibility of Resolve Seeds of the exact existing higher-package-formed, by an invariant covering every unchanged native rule.',
      'priority2':'Quantified elementary and finite-history interchange; same selected witness; native reuse; direct/staged whole-filler coherence for the selected source witness; higher pasting; opposite presentation without reverse dynamics.',
      'priority3':'Original hidden-fiber obstruction reused; strengthened control has independent Boolean fields built by actual native E/reflexivity rules from existing seeds. Canonical continuation survives; arbitrary filler equality fails.',
      'domain':'All Out histories; all requests of the actual source-indexed adapter; every presentation of the declared certified policy family. Not all twelve raw rule schemas, not all conceivable continuation policies.',
      'admissionLimit':'The exact higher atom is not admitted. Existing HigherWitnessAdmission proves this and admits a recovering E-envelope. Its mechanism is reused for the quantified higher witnesses, with exact path recovery and subsequent native continuation. No new primitive or seed is needed for the retained representation.',
      'source_sha256':project,'formalSourceInventory':before}
    out=BASE/'results/witness-generator-coherence-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

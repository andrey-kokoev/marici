"""Fresh generic kernel refutation, bound separately to live native reader ports."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    subprocess.run(['node',str(BASE/'checkers/check_ramsey_EP_reader_obstruction.mjs')],cwd=ROOT,check=True)
    inputPath=BASE/'results/ramsey-EP-reader-obstruction-input-v1.json';data=json.loads(inputPath.read_text())
    for p,h in data['source_sha256'].items():assert sha(ROOT/p)==h,p
    fix=BASE/'fixtures/ramsey-EP-reader-obstruction';fix.mkdir(parents=True,exist_ok=True)
    header='''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEPReaderObstructionExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseyEPReaderObstruction
module O = Obstruction Bool false true false≢true
context : O.Context
context x = x s0 , x s1
actual-failure : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1) → ⊥
actual-failure eq = false≢true (cong (λ x → x s0) eq)
actual-PN-failure : O.pn (O.readerP (O.adapter context O.unit1)) ≡ O.pn (O.adapter context (O.readerE O.unit1)) → ⊥
actual-PN-failure eq = false≢true (cong (λ x → x s3) eq)
'''
    (fix/'RamseyEPReaderObstructionExamples.agda').write_text(header,encoding='utf-8')
    (fix/'RamseyEPReaderObstructionBadSquare.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEPReaderObstructionBadSquare where
open import Cubical.Foundations.Prelude
open import RamseyEPReaderObstructionExamples
bad : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1)
bad = refl
''',encoding='utf-8')
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,fix,tools/'cubical-0.9']
    inventory=lambda:{str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyEPReaderObstruction',owner,True),('RamseyEPReaderObstructionExamples',fix,True),('RamseyEPReaderObstructionBadSquare',fix,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    for p,h in data['source_sha256'].items():assert sha(ROOT/p)==h,p
    files=[Path(__file__),inputPath,owner/'RamseyEPReaderObstruction.agda',*fix.glob('*.agda')]
    out={'status':'passed','scientificOutcome':'specified_U2_semantic_extension_refuted',
      'node':'face-chart-transition-descent','freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,
      'moduleExitCodes':codes,'compiler_sha256':compiler,'actualMarkings':24,'actualValidatedTransfers':data['validatedTransfers'],
      'contextChoiceIndependent':True,'evenArbitraryTargetRetainingC2CannotRepair':True,
      'necessarySourceThirdValue':'x1, whereas the locally native-operator-compatible family requires x2',
      'verificationBoundary':'Generic coefficient obstruction is kernel-proved. Native JS permutations and same-occurrence/full-reference bindings are independently runtime checked, not interpreted by Agda.',
      'broaderParentRefuted':False,'allSemanticAdaptersRefuted':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-EP-reader-obstruction-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

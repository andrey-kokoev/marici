"""All finite requests computed in the kernel; existing native span rules reused."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-requested-port'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def generate():
    prior=BASE/'results/ramsey-native-PN-overlap-span-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale port binding '+p
    w=d['witness'];ports={(p['chart'],p['face']):p for p in w['ports']}
    assert len(ports)==48 and len(w['frames'])==24
    verts=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'];faces=['c0','m0','c1','m1']
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyRequestedPortExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Nat.Base using (ℕ)',
      'open import Cubical.Data.Bool.Base using (false; true)',
      'open import Cubical.Relation.Nullary using (Dec; yes; no)',
      'import Cubical.Data.Empty as Empty','open import Agda.Builtin.String using (String)',
      'open import RamseySingleFrameFaces','open import RamseyRequestedPort',
      'data Chart : Type where','  '+' '.join('q'+str(i) for i in range(24))+' : Chart',
      'role : Chart → Vertex → ℕ']
    for frame in w['frames']:
        for vertex,name in zip(verts,faces):lines.append(f'role q{frame["chart"]} {name} = {int(frame["roles"][vertex]=="M")}')
    lines+=['Permit : Chart → Vertex → Type','Permit c f = count (λ i → role c (face f i)) ≡ 2',
      'packet : (c : Chart) (f : Vertex) → Permit c f → String']
    for c in range(24):
        for f,name in enumerate(faces):
            rhs=json.dumps(json.dumps(ports[c,f],sort_keys=True,separators=(',',':'))) if (c,f) in ports else 'Empty.rec (one-not-two p)'
            lines.append(f'packet q{c} {name} p = {rhs}')
    lines+=['decide : (c : Chart) (f : Vertex) → Dec (Permit c f)']
    for c in range(24):
        for f,name in enumerate(faces):lines.append(f'decide q{c} {name} = '+('yes refl' if (c,f) in ports else 'no one-not-two'))
    lines+=['module R = Request Chart Vertex Permit packet decide']
    accepted=refused=0;bad=None
    for (a,f),port in sorted(ports.items()):
        for b in range(24):
            ok=(b,f) in ports;tag=f'case-{a}-{f}-{b}';term=f'R.isAccepted (R.run q{a} q{b} {faces[f]} refl)'
            lines += [f'{tag} : {term} ≡ '+('true' if ok else 'false'),f'{tag} = refl']
            accepted+=int(ok);refused+=int(not ok)
            if not ok and bad is None:bad=term
    assert (accepted,refused)==(576,576)
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyRequestedPortExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyRequestedPortBadTotal.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRequestedPortBadTotal where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import RamseySingleFrameFaces
open import RamseyRequestedPortExamples
bad : '''+bad+''' ≡ true
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=generate()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,ROOT/'research/nima/agda',FIX,tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyRequestedPort',owner,True),('RamseyRequestedPortExamples',FIX,True),('RamseyRequestedPortBadTotal',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),BASE/'contracts/ramsey-requested-port-attempt.v1.json',owner/'RamseyRequestedPort.agda',owner/'RamseyNativePNOverlapSpan.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-requested-port.verification.v1','status':'passed','scope_id':'finite-chart-requested-native-port-selection-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,
      'moduleExitCodes':codes,'sourceBoundPorts':48,'kernelComputedRequests':1152,
      'kernelAccepted':576,'kernelRefused':576,'nativeSpanSelectorReused':True,
      'acceptedBranchRetainsTargetPermit':True,'rejectionCarriesPermitNegation':True,
      'newNativeComparisonRuleInvented':False,'sourceOnlyTargetConstruction':False,
      'totalPNTransport':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-requested-port-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

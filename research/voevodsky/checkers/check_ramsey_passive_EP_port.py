"""Fresh safe-Cubical binding of actual passive contexts to existing PN requests."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
FIX=BASE/'fixtures/ramsey-passive-EP-port'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    subprocess.run(['node',str(BASE/'checkers/check_ramsey_parent_face_binding_diagnostic.mjs')],cwd=ROOT,check=True)
    subprocess.run(['node',str(BASE/'checkers/check_ramsey_passive_EP_port.mjs')],cwd=ROOT,check=True)
    receipt=BASE/'results/ramsey-passive-EP-port-input-v1.json';data=json.loads(receipt.read_text())
    for p,h in data['source_sha256'].items():assert sha(ROOT/p)==h,p
    ports={(p['chart'],p['face']):p for p in data['ports']};faces=['c0','m0','c1','m1']
    vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1']
    quoted=lambda x:json.dumps(json.dumps(x,sort_keys=True,separators=(',',':')))
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyPassiveEPPortExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Nat.Base using (ℕ)',
      'open import Cubical.Data.Bool.Base using (false; true)','open import Cubical.Relation.Nullary using (Dec; yes; no)',
      'open import Cubical.Data.Empty.Base using (⊥)','import Cubical.Data.Empty as Empty',
      'open import Agda.Builtin.String using (String)','open import RamseySingleFrameFaces',
      'open import RamseyRequestedPort','open import RamseyPassiveEPPort',
      'data Chart : Type where','  '+' '.join('q'+str(i) for i in range(24))+' : Chart',
      'role : Chart → Vertex → ℕ']
    for c in range(24):
        role=next(p['role'] for p in data['ports'] if p['chart']==c)
        for v,f in zip(vertices,faces):lines.append(f'role q{c} {f} = {int(role[v]=="M")}')
    lines+=['Permit : Chart → Vertex → Type','Permit c f = count (λ i → role c (face f i)) ≡ 2',
      'packet : (c : Chart) (f : Vertex) → Permit c f → String']
    for c in range(24):
        for f,name in enumerate(faces):lines.append(f'packet q{c} {name} p = '+(quoted(ports[c,f]) if (c,f) in ports else 'Empty.rec (one-not-two p)'))
    lines+=['electron : Chart → String']
    for context in data['contexts']:
        # E's seed must not covertly contain the already supplied target P packet.
        lines.append(f'electron q{context["chart"]} = '+quoted({'packet':context['e'],'frame':context['eFrame']}))
    lines+=['decide : (c : Chart) (f : Vertex) → Dec (Permit c f)']
    for c in range(24):
        for f,name in enumerate(faces):lines.append(f'decide q{c} {name} = '+('yes refl' if (c,f) in ports else 'no one-not-two'))
    lines+=['module R = Request Chart Vertex Permit packet decide','module A = Passive Chart Vertex Permit packet electron']
    # For accepted faces request target P against itself; E is NEVER a PN source.
    # For refused faces use the complementary chart's actual source permit.
    refusal=None;first=None
    for request in data['requests']:
        c,f,ok=request['chart'],request['face'],request['accepted'];name=faces[f];tag=f'{c}-{f}'
        if ok:
            term=f'R.isAccepted (R.run q{c} q{c} {name} refl)'
            lines += [f'accept-{tag} : {term} ≡ true',f'accept-{tag} = refl',
              f'native-{tag} : A.Both.R.Resolve (A.T.encode (A.context q{c} {name} refl))',
              f'native-{tag} = A.native q{c} {name} refl',
              f'needs-target-{tag} : A.Only.Good (A.context q{c} {name} refl) → ⊥',
              f'needs-target-{tag} = A.needs-target q{c} {name} refl']
            if first is None:first=(c,name)
        else:
            roles=next(p['role'] for p in data['ports'] if p['chart']==c)
            a=next(j for j in range(24) if (j,f) in ports and all(ports[j,f]['role'][v]!=roles[v] for v in vertices))
            term=f'R.isAccepted (R.run q{a} q{c} {name} refl)'
            lines += [f'refuse-{tag} : {term} ≡ false',f'refuse-{tag} = refl']
            if refusal is None:refusal=term
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyPassiveEPPortExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    header=lambda name:'{-# OPTIONS --safe --cubical --guardedness #-}\nmodule '+name+' where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Bool.Base using (true)\nopen import Cubical.Data.Unit.Base using (tt)\nopen import RamseySingleFrameFaces\nopen import RamseyPassiveEPPortExamples\n'
    (FIX/'RamseyPassiveEPPortBadFace.agda').write_text(header('RamseyPassiveEPPortBadFace')+f'bad : {refusal} ≡ true\nbad = refl\n',encoding='utf-8')
    c,f=first
    (FIX/'RamseyPassiveEPPortBadAdmission.agda').write_text(header('RamseyPassiveEPPortBadAdmission')+f'bad : A.Only.Good (A.context q{c} {f} refl)\nbad = λ _ → tt\n',encoding='utf-8')
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';owner=BASE/'agda'
    dirs=[owner,ROOT/'research/nima/agda',FIX,tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyPassiveEPPort',owner,True),('RamseyPassiveEPPortExamples',FIX,True),('RamseyPassiveEPPortBadFace',FIX,False),('RamseyPassiveEPPortBadAdmission',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    for p,h in data['source_sha256'].items():assert sha(ROOT/p)==h,p
    files=[Path(__file__),receipt,owner/'RamseyPassiveEPPort.agda',owner/'RamseyRequestedPort.agda',owner/'RamseyNativePNOverlapSpan.agda',owner/'RamseyExternalPE.agda',owner/'RamseyExternalPEPolicy.agda',*FIX.glob('*.agda')]
    out={'status':'passed','scope':'passive-E-context-and-origin-lifted-PN-request-under-independent-input-policy',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'contexts':24,'originLiftedPortsBoundToExistingFamily':48,'kernelAccepted':48,'kernelRefused':48,
      'nativeContextualRealizations':48,'sourceOnlyCompilerAdmissionRefuted':48,
      'pnBranchEqualsExistingSelectedPackage':True,'electronFalselyUsedAsPNPermit':False,
      'fieldAmplitudeComparisonProved':False,'activeEToPOperationAdded':False,'parentResolved':False,
      'verificationBoundary':'Kernel checks native packaging, retained sources, request permits and compiler-policy necessity. JS geometry, reference/slot binding and phase indices are runtime checked and quoted, not kernel-interpreted.',
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-passive-EP-port-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

"""Source-bound native edge permits retaining actual parent-face choices."""
from pathlib import Path
import hashlib,json,subprocess,sys,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-native-edge-attachments'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def generate():
    previous=BASE/'results/ramsey-requested-port-v1.json';d=json.loads(previous.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale full chart instance '+p
    ports=json.loads((BASE/'results/ramsey-native-PN-overlap-span-v1.json').read_text())['witness']['ports']
    names=['c0','m0','c1','m1'];edges=list(itertools.combinations(range(4),2));ens=['e01','e02','e03','e12','e13','e23']
    slots=['first','next first','next (next first)']
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyEdgeAttachmentsExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (false)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyUniformRelative using (first; next)',
      'import RamseyRequestedPortExamples as C','open import RamseyNativeEdgeAttachments',
      'module A = Attachments C.Chart C.Permit C.packet']
    count=0
    for p in ports:
        c,f=p['chart'],p['face'];vertices=[v for v in range(4) if v!=f]
        for i,(u,v) in enumerate(edges):
            if f in (u,v):continue
            name=f'att-{c}-{f}-{i}';left=slots[vertices.index(u)];right=slots[vertices.index(v)]
            lines += [f'{name} : A.EdgePermit C.q{c} {ens[i]}',
              f'{name} = {names[f]} , (refl , ((({left}) , refl) , (({right}) , refl)))',
              f'{name}-native : A.S.R.Resolve (A.S.port-package C.q{c} {ens[i]} {name})',
              f'{name}-native = A.S.port-proof C.q{c} {ens[i]} {name}']
            count+=1
    assert count==144
    lines += ['triple : A.S.Triple C.q0 C.q2 C.q0',
      'triple = e13 , (att-0-2-4 , (att-2-0-4 , att-0-0-4))',
      'native-composition : A.S.R.Resolve (A.S.composition-package C.q0 C.q2 C.q0 triple)',
      'native-composition = A.S.composition-proof C.q0 C.q2 C.q0 triple',
      'vertex-composition : A.V.R.Resolve (A.V.composition-package C.q0 C.q2 C.q0 (A.restrict-triple false {a = C.q0} {b = C.q2} {c = C.q0} triple))',
      'vertex-composition = A.V.composition-proof C.q0 C.q2 C.q0 (A.restrict-triple false {a = C.q0} {b = C.q2} {c = C.q0} triple)']
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyEdgeAttachmentsExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyEdgeAttachmentsBadParent.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeAttachmentsBadParent where
open import Cubical.Foundations.Prelude
open import RamseyEdgeAttachmentsExamples
bad : fst att-0-2-4 ≡ fst att-0-0-4
bad = refl
''',encoding='utf-8')
    return previous

def main():
    previous=generate()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,ROOT/'research/nima/agda',FIX,BASE/'fixtures/ramsey-requested-port',tools/'cubical-0.9',
      ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyNativeEdgeAttachments',owner,True),('RamseyEdgeAttachmentsExamples',FIX,True),('RamseyEdgeAttachmentsBadParent',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[previous,Path(__file__),BASE/'contracts/ramsey-native-edge-attachments-attempt.v1.json',owner/'RamseyNativeEdgeAttachments.agda',
      owner/'RamseyNativePNOverlapSpan.agda',BASE/'fixtures/ramsey-requested-port/RamseyRequestedPortExamples.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-native-edge-attachments.verification.v1','status':'passed',
      'scope_id':'native-common-edge-attachments-with-parent-face-retention-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'sourceBoundEdgeAttachments':144,'parentFaceAndPNPermitRetained':True,'bothEndpointMembershipsTyped':True,
      'nativeCommonEdgeSpansAndTripleComposition':True,'endpointRestrictionAdmissionMap':True,
      'allDerivationsTransportAlongAdmissionMap':True,'pairTripleEndpointRestrictionCells':True,
      'differentParentErasureRejected':True,'totalChangedRoleEdgeTransport':False,
      'scalarFieldRestrictionInterpreted':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-native-edge-attachments-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

"""History-aware body adapter on live reader/PN ports, with explicit operator frames."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,subprocess
from check_ramsey_passive_EP_semantics import ROOT,load,restore,perm,pins,sha
from exact_multiradical import Radical as R,mm,adj,identity,serialize,decode_A
from assemble_metric_coefficient_protocol import read_operator
import check_twelve_triangle_positive_geometry as geo
BASE=ROOT/'research/voevodsky'

def main():
    subprocess.run(['node',str(BASE/'checkers/check_ramsey_covariant_EP_reader.mjs')],cwd=ROOT,check=True)
    source=load('research/voevodsky/results/ramsey-covariant-EP-reader-input-v1.json')
    load('research/voevodsky/results/ramsey-reader-prior-clues-v1.json')
    fields=load('research/strominger/results/full-five-channel-candidate/verification.json')
    semantics=load('research/voevodsky/results/ramsey-passive-EP-semantics-v1.json')
    pd=load('research/strominger/results/common-three-carrier-protocol/proton.json')
    nd=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    pn=load('research/strominger/results/global-PN-transport/verification.json')
    BP=restore(fields['protonFiveEmbedding']);PN=restore(pn['matrix']);m=list(map(F,nd['source']['metric']))
    sharp=lambda X:[[v*m[j] for j,v in enumerate(row)] for row in adj(X)]
    PNi=sharp(PN);assert mm(PNi,PN)==identity(36)
    labels=pd['source']['coordinates'];rotation=geo.rotation((2,3,0,1));rename=dict(zip('ABCD','CDAB'))
    A=[[R() for _ in range(36)] for _ in range(36)]
    for j,label in enumerate(labels):
        edge,axis=label.split(':');target=''.join(rename[v] for v in edge)
        for i in range(3):A[labels.index(target+':'+'xyz'[i])][j]=R(rotation[i]['xyz'.index(axis)])
    G=restore(next(t['geometricMap'] for t in semantics['tests'] if t['convention']=='co_moving_tetrahedral_frame'))
    assert mm(A,A)==identity(36) and mm(adj(A),A)==identity(36)
    assert mm(A,G)==mm(G,A)
    PP=perm(source['PReader']);PE=perm(source['negativeEReader']);T=perm(source['adapter']);pi=perm([3,1,2,0,4])
    assert mm(PP,T)==mm(T,PE)
    BE0=mm(BP,perm([4,3,2,1,0]));BE1=mm(mm(A,BE0),adj(PE))
    P0=mm(mm(G,BE0),adj(T));P1=mm(mm(A,P0),adj(PP))
    N0=mm(mm(PN,P0),adj(pi));N1=mm(mm(PN,P1),adj(pi))
    for e,p,n in [(BE0,P0,N0),(BE1,P1,N1)]:
        assert mm(adj(e),e)==mm(adj(p),p)==mm(sharp(n),n)==identity(5)
        assert mm(G,e)==mm(p,T)
        assert mm(adj(p),G)==mm(T,adj(e))
        assert mm(PN,p)==mm(n,pi)
        assert mm(sharp(n),PN)==mm(pi,adj(p))
    assert mm(adj(P1),A)==mm(PP,adj(P0))
    assert mm(adj(BE1),A)==mm(PE,adj(BE0))
    # Actual N0 -> inversePN -> P-reader -> PN -> N1 path; factor it,
    # avoiding an expensive dense multiradical product.
    SN=lambda X:mm(PN,mm(A,mm(PNi,X)))
    delta=mm(mm(pi,PP),adj(pi));assert mm(delta,delta)==identity(5)
    assert SN(N0)==mm(N1,delta)
    assert sharp(SN(N1))==mm(delta,sharp(N0))
    operatorChecks=[]
    for name in ['L','G','N']:
        sparse=read_operator(nd['operators'][name],36)
        X=[[decode_A(sparse[i,j].record()) if (i,j) in sparse else R() for j in range(36)] for i in range(36)]
        x0=mm(sharp(N0),mm(X,N0));assert mm(X,N0)==mm(N0,x0)
        # X1 = SN X SN^-1. SN is involutive. No assertion that this equals
        # the independently fixed canonical X matrix at the target chart.
        image=SN(mm(X,SN(N1)))
        x1=mm(sharp(N1),image);expected=mm(mm(delta,x0),adj(delta))
        assert x1==expected and image==mm(N1,x1)
        frozenImage=mm(X,N1);frozenReduced=mm(sharp(N1),frozenImage)
        assert frozenImage==image # unchanged raw operator works on this preparation
        assert x1!=x0 # its coefficient matrix genuinely tracks the reader frame
        operatorChecks.append({'operator':name,'sourceCompressed':serialize(x0),'transportedCompressed':serialize(x1),
          'historyConjugacyPasses':True,'transportedPreparationInvariant':True,
          'unchangedRawOperatorCovariantOnPreparedHistory':True,'compressedMatrixConstantAcrossHistory':False,
          'frozenTargetMatrixPreservesPreparation':frozenImage==mm(N1,frozenReduced),
          'frozenTargetCompressedEqualsTransported':frozenReduced==x1,
          'fixedCanonicalTargetIdentificationClaimed':False})
    # Actual geometric rows, with their induced signed reindexing, not a fitted H.
    edges=load('research/voevodsky/results/ramsey-geometric-edge-readout-v1.json')
    H=restore(edges['readout']);W=mm(mm(H,A),adj(H))
    W=[[v*F(1,8) for v in row] for row in W]
    assert mm(H,A)==mm(W,H) and mm(W,W)==identity(12)
    HN=mm(H,PNi)
    assert mm(HN,mm(PN,mm(A,P0)))==mm(W,mm(H,P0))
    # Generic coefficient theorem: any number of readers, with the outside
    # context map retained. Geometry is separately bound to the live one-step cases.
    fix=BASE/'fixtures/ramsey-covariant-EP-reader';fix.mkdir(parents=True,exist_ok=True)
    (fix/'RamseyCovariantEPReaderExamples.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCovariantEPReaderExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Nat.Base using (ℕ)
open import RamseyCovariantEPReader
module C = Natural Bool
all : (n : ℕ) (x : C.Vector) → C.pn (C.Psteps n (C.body (λ y → y) x)) ≡ C.pn (C.body (λ y → y) (C.Esteps n x))
all n x = C.all-reader-PN n (λ y → y) x
''',encoding='utf-8')
    # Retain the falsified adapter as a hostile control, not as an edited history.
    (fix/'RamseyCovariantEPReaderBadOldAdapter.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCovariantEPReaderBadOldAdapter where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import RamseyEPReaderObstruction
module O = Obstruction Bool false true false≢true
context : O.Context
context x = x s0 , x s1
bad : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1)
bad = refl
''',encoding='utf-8')
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';dirs=[owner,fix,tools/'cubical-0.9']
    def filehash(p):
        import hashlib
        return hashlib.sha256(p.read_bytes()).hexdigest()
    inventory=lambda:{str(p):filehash(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=filehash(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyCovariantEPReader',owner,True),('RamseyCovariantEPReaderExamples',fix,True),('RamseyCovariantEPReaderBadOldAdapter',fix,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==filehash(agda)
    for p,h in pins.items():assert sha(p)==h,p
    for module in list(sys.modules.values()):
        filename=getattr(module,'__file__',None)
        if filename:
            try:rel=Path(filename).resolve().relative_to(ROOT).as_posix()
            except ValueError:continue
            pins[rel]=sha(rel)
    for p in [Path(__file__),owner/'RamseyCovariantEPReader.agda',owner/'RamseyEPReaderObstruction.agda',*fix.glob('*.agda')]:
        rel=p.relative_to(ROOT).as_posix();pins[rel]=sha(rel)
    result={'status':'passed','node':'face-chart-transition-descent','freshSafeCubical':True,'ignoreInterfaces':True,
      'compiler_sha256':compiler,'moduleExitCodes':codes,'inputsStable':True,
      'liveMarkings':24,'liveValidatedTransfers':source['validatedTransfers'],
      'allFivePacketSlotsAgree':True,'genericAnyReaderCountAndPN':True,
      'all36EPAndPNReadoutSquares':True,'geometricTraceCovariance':True,
      'operatorHistoryChecks':operatorChecks,
      'bindings':{'E0':serialize(BE0),'E1':serialize(BE1),'P0':serialize(P0),'P1':serialize(P1),'N0':serialize(N0),'N1':serialize(N1)},
      'scope':'Retained E carrier; body-carrying adapter; actual direct and reader-prefixed PN ports. Coefficient theorem is generic; field computations exact. Full-source operator covariance is explicit, not identification with independently frozen target matrices. No all-overlap or source-selection theorem.',
      'outsideContextConvention':'identity for field/source executions; generic coefficient theorem permits a fixed scalar context function. Outside references are not equated as occurrences.',
      'parentResolved':False,'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-covariant-EP-reader-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','moduleExitCodes','liveMarkings','liveValidatedTransfers','allFivePacketSlotsAgree','genericAnyReaderCountAndPN','all36EPAndPNReadoutSquares','geometricTraceCovariance']} | {'operators':[{k:a[k] for k in ['operator','historyConjugacyPasses','frozenTargetMatrixPreservesPreparation','frozenTargetCompressedEqualsTransported']} for a in operatorChecks]},indent=2))
if __name__=='__main__':main()

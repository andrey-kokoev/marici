"""External provenance compiler for the actual retained four-facet P/E diagram."""
from pathlib import Path
import json,hashlib,subprocess,sys,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-external-pe'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prepare():
    prior=BASE/'results/ramsey-four-facet-vertex-cells-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale four-facet input '+p
    assert d['facetCharts']==[0,7,0,7]
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyExternalPEExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Unit.Base using (tt)',
      'open import Cubical.Data.Bool.Base using (Bool; false; true)',
      'open import Cubical.Data.Bool.Properties using (false≢true)',
      'open import Cubical.Data.Empty.Base using (⊥)',
      'open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)',
      'import RamseyRequestedPortExamples as C','import RamseyEdgeAttachmentsExamples as E',
      'import RamseyFourFacetVertexCells as F','open import RamseyExternalPE',
      'module P = TracedSpans C.Chart Vertex E.A.VertexPermit E.A.vertex-packet']
    names=['c0','m0','c1','m1'];charts=[0,7,0,7]
    for a,b,c in itertools.permutations(range(4),3):
        tag=f'{a}-{b}-{c}';cs=' '.join('C.q'+str(charts[i]) for i in [a,b,c]);t='F.triple-'+tag;tree='tree-'+tag
        v=next(i for i in range(4) if i not in [a,b,c])
        lines += [f'{tree} : P.T.Tree',f'{tree} = P.composition {cs} {t}',
          f'native-{tag} : P.T.R.Resolve (P.T.encode {tree})',f'native-{tag} = P.T.realize {tree}',
          f'cell-{tag} : P.T.encode {tree} ≡ E.A.V.composition-package {cs} {t}',
          f'cell-{tag} = P.composition-cell {cs} {t}',
          f'middle-{tag} : P.T.origin {tree} (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q{charts[b]} , ({names[v]} , F.vp-{b}-{v}))',
          f'middle-{tag} = refl']
    lines += ['module B = Trees Bool (λ _ → "same literal payload")',
      'left right : B.Located','left = B.leaf false , tt','right = B.leaf true , tt',
      'raw-equal : B.encode (fst left) ≡ B.encode (fst right)','raw-equal = refl',
      'no-external-erasure : left ≡ right → ⊥',
      'no-external-erasure path = false≢true (cong B.source-of path)']
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyExternalPEExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyExternalPEBadErasure.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPEBadErasure where
open import Cubical.Foundations.Prelude
open import RamseyExternalPEExamples
bad : left ≡ right
bad = refl
''',encoding='utf-8')
    return prior

def main():
    prior=prepare()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,FIX,BASE/'fixtures/ramsey-four-facet-vertex-cells',BASE/'fixtures/ramsey-native-edge-attachments',
      BASE/'fixtures/ramsey-requested-port',ROOT/'research/nima/agda',tools/'cubical-0.9',
      ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyExternalPE',owner,True),('RamseyExternalPEExamples',FIX,True),('RamseyExternalPEBadErasure',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),owner/'RamseyExternalPE.agda',owner/'RamseyNativePNOverlapSpan.agda',
      BASE/'contracts/ramsey-external-pe-attempt.v1.json',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-external-pe.verification.v1','status':'passed',
      'scope_id':'externally-indexed-PE-realization-of-four-facet-diagram-v1','freshSafeCubical':True,
      'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'genericNativePERealization':True,'allEPrerequisiteOccurrencesRetained':True,
      'locatedExternalSourceObservation':True,'selectedSpanAndCompositionCompilerCells':True,
      'sourceBoundVertexCompositions':24,'actualMiddleSourceIndexCells':24,
      'equalRawPayloadDistinctExternalLabelsControlled':True,'externalErasureRejected':True,
      'arbitraryNativeDerivationsLifted':False,'independentTargetInputsEliminated':False,
      'owningNativeSignatureChanged':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-external-pe-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()

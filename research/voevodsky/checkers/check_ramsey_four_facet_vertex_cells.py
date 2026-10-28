"""Four-facet vertex cells reached through different pairwise edges."""
from pathlib import Path
import hashlib,json,subprocess,sys,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-four-facet-vertex-cells'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def generate():
    previous=BASE/'results/ramsey-native-edge-attachments-v1.json';receipt=json.loads(previous.read_text())
    for p,h in receipt['source_sha256'].items():assert sha(ROOT/p)==h,'stale edge attachment '+p
    raw=json.loads((BASE/'results/ramsey-native-PN-overlap-span-v1.json').read_text())['witness']
    charts=[0,7,0,7];frames={f['chart']:f for f in raw['frames']}
    assert all(frames[0]['roles'][v]!=frames[7]['roles'][v] for v in frames[0]['roles'])
    ports=[next(p for p in raw['ports'] if p['chart']==charts[f] and p['face']==f) for f in range(4)]
    names=['c0','m0','c1','m1'];edges=list(itertools.combinations(range(4),2));ens=['e01','e02','e03','e12','e13','e23']
    slots=['first','next first','next (next first)'];chart=lambda a:'C.q'+str(charts[a])
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyFourFacetVertexCells where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Bool.Base using (false; true)',
      'open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'open import RamseyUniformRelative using (first; next)',
      'import RamseyRequestedPortExamples as C','open import RamseyNativeEdgeAttachments',
      'open import RamseyEdgeAttachmentsExamples']
    for f in range(4):
        vertices=[v for v in range(4) if v!=f]
        for v in vertices:
            slot=slots[vertices.index(v)];name=f'vp-{f}-{v}'
            lines += [f'{name} : A.VertexPermit {chart(f)} {names[v]}',f'{name} = {names[f]} , (refl , (({slot}) , refl))']
    for a,b in itertools.permutations(range(4),2):
        e=tuple(i for i in range(4) if i not in [a,b]);ei=edges.index(e);name=f'edge-{a}-{b}'
        lines += [f'{name} : A.S.Common {chart(a)} {chart(b)}',
          f'{name} = {ens[ei]} , (att-{charts[a]}-{a}-{ei} , att-{charts[b]}-{b}-{ei})',
          f'{name}-native : A.S.R.Resolve (A.S.selected-package {chart(a)} {chart(b)} {name})',
          f'{name}-native = A.S.selected-proof {chart(a)} {chart(b)} {name}']
    for a,b,c in itertools.permutations(range(4),3):
        v=next(i for i in range(4) if i not in [a,b,c]);tag=f'{a}-{b}-{c}';t='triple-'+tag
        args=f'{{a = {chart(a)}}} {{b = {chart(b)}}} {{c = {chart(c)}}}'
        lines += [f'{t} : A.V.Triple {chart(a)} {chart(b)} {chart(c)}',
          f'{t} = {names[v]} , (vp-{a}-{v} , (vp-{b}-{v} , vp-{c}-{v}))',
          f'{t}-native : A.V.R.Resolve (A.V.composition-package {chart(a)} {chart(b)} {chart(c)} {t})',
          f'{t}-native = A.V.composition-proof {chart(a)} {chart(b)} {chart(c)} {t}']
        routes={}
        for label,i,j in [('ab',a,b),('bc',b,c),('ac',a,c)]:
            e=tuple(k for k in range(4) if k not in [i,j]);side='false' if e[0]==v else 'true';route=f'route-{label}-{tag}';routes[label]=route
            lines += [f'{route} : A.V.Common {chart(i)} {chart(j)}',
              f'{route} = A.restrict-common {side} {{a = {chart(i)}}} {{b = {chart(j)}}} edge-{i}-{j}',
              f'cell-{label}-{tag} : {route} ≡ A.V.{label}-index {args} {t}',f'cell-{label}-{tag} = refl']
        def middle(i,j,route,leg):
            return f'A.V.R.premise (A.V.R.premise (A.V.selected-package {chart(i)} {chart(j)} {route} , A.V.selected-proof {chart(i)} {chart(j)} {route}) (lift {route})) (lift A.V.{leg}-leg)'
        lines += [f'middle-{tag} : {middle(a,b,routes["ab"],"target")} ≡ {middle(b,c,routes["bc"],"source")}',f'middle-{tag} = refl']
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyFourFacetVertexCells.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyFourFacetBadMiddle.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFourFacetBadMiddle where
open import Cubical.Foundations.Prelude
open import RamseyFourFacetVertexCells
-- Same chart and vertex, but different retained parent faces.
bad : fst vp-1-2 ≡ fst vp-3-2
bad = refl
''',encoding='utf-8')
    return previous,ports

def main():
    previous,ports=generate()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,ROOT/'research/nima/agda',FIX,BASE/'fixtures/ramsey-native-edge-attachments',
      BASE/'fixtures/ramsey-requested-port',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyFourFacetVertexCells',True),('RamseyFourFacetBadMiddle',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[previous,Path(__file__),BASE/'contracts/ramsey-four-facet-vertex-cells-attempt.v1.json',owner/'RamseyNativeEdgeAttachments.agda',
      BASE/'fixtures/ramsey-native-edge-attachments/RamseyEdgeAttachmentsExamples.agda',
      BASE/'fixtures/ramsey-requested-port/RamseyRequestedPortExamples.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-four-facet-vertex-cells.verification.v1','status':'passed',
      'scope_id':'native-four-facet-different-edge-vertex-restriction-cells-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'facetCharts':[0,7,0,7],'retainedFacetPorts':ports,'directedNativeEdgeSelections':12,
      'nativeVertexTripleCompositions':24,'differentEdgeRestrictionCells':72,'fullMiddleDerivationSeams':24,
      'differentMiddleParentErasureRejected':True,'globallyOccupiedSingleRoleFrame':False,
      'totalRoleDomainEquivalence':False,'scalarFieldGluing':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-four-facet-vertex-cells-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory','retainedFacetPorts']},indent=2))
if __name__=='__main__':main()

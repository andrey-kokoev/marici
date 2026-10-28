"""Classify full attachment-choice fibers, separately from selected spans."""
from pathlib import Path
import json,hashlib,subprocess,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';V='research/voevodsky/'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    paths=[BASE/'results/ramsey-edge-law-domain-v1.json',BASE/'results/ramsey-four-facet-vertex-cells-v1.json']
    law,cover=[json.loads(p.read_text()) for p in paths]
    for d in [law,cover]:
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale attachment input '+p
    charts=law['charts'];equal=unequal=0;witness=None
    for a in charts:
        for b in charts:
            for x,y in zip(a['edges'],b['edges']):
                na,nb=x['parentMultiplicity'],y['parentMultiplicity']
                if not na or not nb:continue
                if na==nb:equal+=1
                else:
                    unequal+=1
                    if witness is None:witness={'sourceChart':a['chart'],'targetChart':b['chart'],'sourceAttachment':x,'targetAttachment':y}
    assert (equal,unequal)==(1632,768)
    vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'];assignment=cover['facetCharts'];assert assignment==[0,7,0,7]
    edge_tests=[]
    for a,b in itertools.permutations(range(4),2):
        edge={vertices[i] for i in range(4) if i not in [a,b]}
        sa=next(x for x in charts[assignment[a]]['edges'] if set(x['edge'])==edge)
        sb=next(x for x in charts[assignment[b]]['edges'] if set(x['edge'])==edge)
        assert sa['parentMultiplicity']==sb['parentMultiplicity']>0
        edge_tests.append({'facets':[a,b],'charts':[assignment[a],assignment[b]],'edge':sorted(edge),
          'sourceChoices':sa['parentPorts'],'targetChoices':sb['parentPorts'],'cardinality':sa['parentMultiplicity']})
    vertex_tests=[]
    for a,b,c in itertools.permutations(range(4),3):
        v=next(vertices[i] for i in range(4) if i not in [a,b,c])
        records=[next(x for x in charts[assignment[f]]['vertices'] if x['vertex']==v) for f in [a,b,c]]
        sizes=[len(x['parentFaces']) for x in records];assert set(sizes)=={1,2}
        vertex_tests.append({'facets':[a,b,c],'charts':[assignment[f] for f in [a,b,c]],'vertex':v,
          'completeParentFaceChoices':[x['parentFaces'] for x in records],'cardinalities':sizes})
    owner=BASE/'agda';fix=BASE/'fixtures/ramsey-attachment-choice';tools=Path.home()/'tools/cubical-agda'
    agda=tools/'agda-2.8.0/agda.exe';dirs=[owner,fix,tools/'cubical-0.9']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyAttachmentChoiceObstruction',owner,True),('RamseyAttachmentChoiceBadInverse',fix,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=paths+[Path(__file__),BASE/'contracts/ramsey-attachment-fiber-equivalence-attempt.v1.json',
      owner/'RamseyAttachmentChoiceObstruction.agda',*fix.glob('*.agda')]
    out={'schema':'marici.ramsey-attachment-fiber-equivalence.verification.v1','status':'passed',
      'scope_id':'complete-parent-choice-fibers-versus-selected-facet-spans-v1',
      'verification_level':'exact finite parent-choice cardinalities plus fresh safe Cubical Unit/Bool non-equivalence; no kernel normalization of all attachment types',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'commonSupportedEdgeFibers':equal+unequal,'equalCardinalityEdgeFibers':equal,'unequalCardinalityEdgeFibers':unequal,
      'commonEdgeMultiplicityWitness':witness,'selectedCoverEdgeFibers':edge_tests,'selectedCoverVertexTriples':vertex_tests,
      'selectedCoverEdgeCardinalitiesAgree':True,'selectedCoverVertexTriplesWithMixedCardinalities':24,
      'completeChoiceFiberEquivalenceAcrossEverySelectedVertex':False,
      'chosenParentNativeSpansRefuted':False,'parentRequiresCompleteFiberEquivalenceAsserted':False,
      'kernelNormalizationOfActualAttachmentTypes':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-attachment-fiber-equivalence-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory','commonEdgeMultiplicityWitness','selectedCoverEdgeFibers','selectedCoverVertexTriples']},indent=2))
if __name__=='__main__':main()

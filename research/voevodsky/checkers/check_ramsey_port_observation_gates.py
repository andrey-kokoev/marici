"""Bind the observed-equivalence gate to declared components of real ports."""
from pathlib import Path
import json,hashlib,subprocess,sys,itertools
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-port-observation-gates'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def key(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def prepare():
    paths=[BASE/'results/ramsey-native-PN-overlap-span-v1.json',BASE/'results/ramsey-observed-comparisons-v1.json',BASE/'results/ramsey-four-facet-vertex-cells-v1.json']
    raw,guard,cover=[json.loads(p.read_text()) for p in paths]
    for d in [raw,guard,cover]:
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale observation input '+p
    ports=raw['witness']['ports'];frames={x['chart']:x for x in raw['witness']['frames']}
    def observe(p):return {
      'geometricFacet':sorted(p['faceVertices']),
      'namedReferences':p['source']['chart']['aliases'],
      'roleAssignment':p['role'],'eligibleFaceDomain':sorted(frames[p['chart']]['eligible']),
      'readerContext':{k:p['sourceFrame'][k] for k in ['species','window','context']},
      'provenance':{k:p[k] for k in ['chart','base','baseFrame','prefix','source','operation','target','targetFrame']}}
    pairs=[(a,b) for a in ports for b in ports if a['face']==b['face']];assert len(pairs)==576
    equality={k:sum(observe(a)[k]==observe(b)[k] for a,b in pairs) for k in observe(ports[0])}
    assert equality['geometricFacet']==576 and equality['namedReferences']==96
    a,b=next((a,b) for a,b in pairs if a['role']!=b['role'] and observe(a)['namedReferences']!=observe(b)['namedReferences'])
    obs=[observe(a),observe(b)]
    fixed=cover['retainedFacetPorts'];edges=[]
    for i,j in itertools.permutations(range(4),2):
        x,y=fixed[i],fixed[j];shared=sorted(set(x['faceVertices'])&set(y['faceVertices']));assert len(shared)==2
        assert x['face']==i and y['face']==j and i in frames[x['chart']]['eligible'] and j in frames[y['chart']]['eligible']
        edges.append({'facets':[i,j],'sharedGeometricEdge':shared,'differentParentFaces':True,
          'roleAssignmentEqual':x['role']==y['role'],'eligibleDomainsEqual':frames[x['chart']]['eligible']==frames[y['chart']]['eligible'],
          'namedReferencesEqual':observe(x)['namedReferences']==observe(y)['namedReferences'],
          'sourceParentPermit':{'chart':x['chart'],'face':i},'targetParentPermit':{'chart':y['chart'],'face':j}})
    assert sum(e['roleAssignmentEqual'] for e in edges)==4
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyPortObservationGates where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Foundations.Isomorphism',
      'open import Cubical.Data.Bool.Base using (Bool; false; true)','open import Agda.Builtin.String using (String)',
      'import RamseyAtomicSeedPaths as Atom','open import RamseyObservedComparisons']
    fields={'packet':[a,b],'geometry':[o['geometricFacet'] for o in obs],
      'references':[o['namedReferences'] for o in obs],'roles':[o['roleAssignment'] for o in obs],
      'lawDomain':[o['eligibleFaceDomain'] for o in obs],'provenance':[o['provenance'] for o in obs]}
    for name,values in fields.items():
        lines+=[name+' : Bool → String']
        for tag,value in zip(['false','true'],values):lines.append(f'{name} {tag} = '+json.dumps(key(value)))
    lines+=['geometry-swap : ObservedEquiv Bool Bool String geometry geometry',
      'geometry-swap = isoToEquiv Atom.flip , (λ { false → refl ; true → refl })',
      'geometry-tagged-path : tagged-atom geometry false ≡ tagged-atom geometry true',
      'geometry-tagged-path = guarded-package-path {a = geometry} {b = geometry} geometry-swap false true refl']
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyPortObservationGates.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyPortObservationBadReferences.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPortObservationBadReferences where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyPortObservationGates
bad : references false ≡ references true
bad = refl
''',encoding='utf-8')
    return paths,equality,edges,{'source':a,'target':b,'observations':obs}

def main():
    paths,equality,edges,witness=prepare()
    if '--generate' in sys.argv:return
    owner=BASE/'agda';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,FIX,ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyPortObservationGates',True),('RamseyPortObservationBadReferences',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=paths+[Path(__file__),BASE/'contracts/ramsey-port-observation-gates-attempt.v1.json',owner/'RamseyObservedComparisons.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-port-observation-gates.verification.v1','status':'passed',
      'scope_id':'source-bound-port-observation-components-and-guard-strength-v1','freshSafeCubical':True,
      'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'sameFacePairs':576,'componentEqualityCounts':equality,'selectedCoverEdgeComponents':edges,
      'actualRecordIndexWitness':witness,'geometryOnlyRecordIndexSwapAccepted':True,
      'namedReferenceEqualityHostileRejected':True,'geometryGuardImpliesRoleLawTransport':False,
      'recordIndexSwapIsOperationalTransition':False,'allNativeRulesObservationGuarded':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-port-observation-gates-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory','actualRecordIndexWitness','selectedCoverEdgeComponents']},indent=2))
if __name__=='__main__':main()

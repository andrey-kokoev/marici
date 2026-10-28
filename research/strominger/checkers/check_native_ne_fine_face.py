"""Registered coordinate bridge and native NE shared-face identification."""
from pathlib import Path
import hashlib,json,subprocess
from esd7_attachment_channel import produce,decode
from esd7_analytical_binding import bind
ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/'
CONTRACT=BASE+'contracts/native-ne-fine-face-attempt.v1.json'
SNAPSHOT=BASE+'contracts/persistent-seam-pe-conjecture-net.snapshot.rev38.json'
REGISTRY='research/voevodsky/results/esd7_tetrahedron_prototype_registry.json'
OUT=BASE+'results/native-ne-fine-face/'
def load(p):return json.loads((ROOT/p).read_text())
def point(v):return tuple(map(int,v.split(','))) if isinstance(v,str) else tuple(v)
def forward(x):
    b=[2-y for y in point(x)]
    assert sum(b)==7
    return (b[0],b[0]+b[1],b[0]+b[1]+b[2])
def inverse(v):return tuple(2-b for b in (v[0],v[1]-v[0],v[2]-v[1],7-v[2]))
def key(vs):return tuple(sorted(tuple(v) for v in vs))
def main():
    spec=load(CONTRACT);pre=load(SNAPSHOT);attachment=load(spec['sourceAttachment'])
    checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    inputs={CONTRACT,SNAPSHOT,REGISTRY,spec['sourceAttachment'],BASE+'checkers/check_native_ne_fine_face.py',BASE+'checkers/esd7_attachment_channel.py',BASE+'checkers/esd7_analytical_binding.py',BASE+'demos/particle-overlap-tetrahedron/simplex-components.mjs',BASE+'native-ne-fine-face-result-v1.md'}
    for p in [BASE+'results/screw-esd7-relative-attachment/verification.json',BASE+'results/external-c0-finite-trace/verification.json']:
        r=load(p);inputs.add(p)
        check('live source receipt closure: '+p,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==sha for q,sha in r['sourceHashes'].items()));inputs.update(r['sourceHashes'])
    n=next(n for n in pre['conjectures'] if n['id']=='native-ne-fine-face-attempt')
    check('coordinate bridge registered before face lookup',n['status']=='open' and n['registration_before_execution'])
    js="import {assembleComponents} from './research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';console.log(JSON.stringify(assembleComponents(7).components));"
    components=json.loads(subprocess.run(['node','--input-type=module','-e',js],cwd=ROOT,capture_output=True,text=True,check=True).stdout)
    assembly=decode(produce(7));binding=bind(assembly,load(REGISTRY))
    prior_binding_path=BASE+'results/esd7-analytical-prototype-binding.json';inputs.add(prior_binding_path)
    prior_binding=load(prior_binding_path)
    check('recomputed registry roles equal the authoritative retained binding',all(binding[k]==prior_binding[k] for k in ['assignments','faceBindings']))
    vertices={v['id']:tuple(v['cumulative']) for v in assembly['vertices']};vertex_ids={v:k for k,v in vertices.items()}
    tetra={key(vertices[v] for v in t['vertices']):t for t in assembly['tetrahedra']}
    transformed={key(forward(x) for x in c['addresses']):c for c in components}
    check('all343 actual primitives match, not merely their total counts',len(transformed)==len(tetra)==343 and set(transformed)==set(tetra))
    check('coordinate bridge inverts every native target vertex exactly',all(inverse(forward(x))==tuple(x) for c in components for x in c['addresses']))
    cells={c['sourceCell']:c for c in attachment['cells']};packets={p['id']:p for p in attachment['packets']};charts={c['nativeChart']:c for c in attachment['chartBindings']}
    operation=next(o for o in attachment['operations'] if o['id']==spec['nativeInterface']['operation'])
    check('actual retained native interface identity matches the registration',all(operation[k]==spec['nativeInterface'][k] for k in ['source','target','kind']))
    selected=[]
    for p in [operation['source'],operation['target']]:
        chart=charts[packets[p]['chart']];cell=cells[chart['sourceCell']];t=tetra[key(forward(x) for x in cell['vertices'])]
        selected.append({'packet':p,'species':chart['species'],'sourceCell':chart['sourceCell'],'targetComponent':cell['targetComponent'],'tetrahedron':t['id'],'vertices':t['vertices']})
    face_ids=sorted(vertex_ids[forward(x)] for x in operation['face'])
    face=next(f for f in binding['faceBindings'] if f['vertices']==face_ids)
    check('native shared face equals the exact intersection of its incident tetrahedra',set(face_ids)==set(selected[0]['vertices'])&set(selected[1]['vertices']))
    check('both incident tetrahedral roles are bound, not assigned by position',len(face['localContexts'])==2 and {c['tetrahedron'] for c in face['localContexts']}=={t['tetrahedron'] for t in selected})
    for row in selected:row['analyticalContext']=next(c for c in face['localContexts'] if c['tetrahedron']==row['tetrahedron'])
    edges={e['id']:e for e in assembly['edges']}
    check('shared triangle route and direct edge retain their actual endpoints',[edges[e]['vertices'] for e in face['sharedEdgeRoute']]==[face_ids[:2],face_ids[1:]] and edges[face['directEdge']]['vertices']==[face_ids[0],face_ids[2]])
    outside=[{'source':v['target'],'cumulative':forward(v['target'])} for v in attachment['externalReferences']]
    check('external C0 stays outside the ordered chamber and has no fabricated vertex ID',all(not (0<=v['cumulative'][0]<=v['cumulative'][1]<=v['cumulative'][2]<=7) and v['cumulative'] not in vertex_ids for v in outside))
    check('unrelated face label cannot replace the coordinate-bound face',all(set(f['vertices'])!=set(face_ids) for f in binding['faceBindings'] if f['face']!=face['face']))
    check('geometric lookup does not discharge retained analytical obligations',not face['comparisonDischarged'] and not face['homotopyInstalled'] and not binding['analyticalCoherenceDischarged'])
    missing=[{'edge':e,'obligation':'source-bound operator in both incident presentations on admitted common domains'} for e in [*face['sharedEdgeRoute'],face['directEdge']]]
    artifact={'contract':CONTRACT,'coordinateBridge':spec['coordinateBridge'],'nativeOperation':operation,'incidentPackets':selected,'face':face,'externalReferences':outside,
        'missingAnalyticalBindings':missing+[
            {'obligation':'three vertex comparison frames and endpoint/flux readout naturality for these actual fine-vertex presentations'},
            {'obligation':'intended triangular face residual and source homotopy or admitted faithful-whiskering recovery; native NE is transport across the shared face, not that filler'}],
        'nativeFineFaceIdentityEstablished':True,'analyticalFaceComparisonEstablished':False,'analyticalHomotopyEstablished':False,'fullPbConstructionEstablished':False,'scope':spec['scope']}
    (ROOT/OUT).mkdir(parents=True,exist_ok=True);artifact_path=OUT+'binding.json';(ROOT/artifact_path).write_text(json.dumps(artifact,indent=2)+'\n');inputs.add(artifact_path)
    report={'status':'passed','check_count':len(checks),'checks':checks,'primitiveMatches':len(transformed),'face':face['face'],'vertices':face_ids,'incidentPackets':selected,'sharedEdgeRoute':face['sharedEdgeRoute'],'directEdge':face['directEdge'],
        'nativeFineFaceIdentityEstablished':True,'analyticalFaceComparisonEstablished':False,'analyticalHomotopyEstablished':False,'fullPbConstructionEstablished':False,
        'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(inputs)}}
    (ROOT/OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['sourceHashes','checks']}))
if __name__=='__main__':main()

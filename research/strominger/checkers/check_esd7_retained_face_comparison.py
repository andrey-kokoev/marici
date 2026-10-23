"""Exercise the finite gate; report real F006 as awaiting source-bound payload."""
from pathlib import Path
import copy
import hashlib
import json
from esd7_retained_face_comparison import matrix,mul,encode,compare

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
BINDING=BASE+'esd7-analytical-prototype-binding.json'
SOURCES=[
 'research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md',
 'research/voevodsky/face-234-is-uniquely-recovered-on-the-observer-generated-geometric-subcategory-by-faithful-whiskering-along-the-integrated-representation.md',
 'research/voevodsky/checkers/check_asymptotic_face_234_propagation.py']


def main():
    binding=json.loads((ROOT/BINDING).read_text())
    face=next(f for f in binding['faceBindings'] if f['face']=='F006')
    checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    check('selected actual mixed-role face',face['vertices']==['V001','V008','V036'] and
          {(c['tetrahedron'],c['role']) for c in face['localContexts']}=={('T000','H234'),('T003','H123')})
    check('source shared edge route retained',face['sharedEdgeRoute']==['E004','E037'] and face['directEdge']=='E006')
    # These exact finite matrices are explicitly synthetic controls, not native
    # analytical operators inferred from the attached prototype names.
    C=[[2,0,0],[0,0,1],[0,1,0]]; Ci=[['1/2',0,0],[0,0,1],[0,1,0]]
    E=[[0,1,0],[0,0,1]]; B=[[0,1],[1,0]]
    left={'uv':[[1,1,0],[0,1,1],[0,0,1]],'vw':[[1,0,0],[1,1,0],[0,1,1]],'uw':[[1,0,0],[0,1,0],[0,0,1]]}
    right={e:encode(mul(mul(matrix(C),matrix(a)),matrix(Ci))) for e,a in left.items()}
    payload={'frames':{v:C for v in 'uvw'},'left':left,'right':right,
             'endpointLeft':{v:E for v in 'uvw'},'endpointRight':{v:E for v in 'uvw'},'endpointFrames':{v:B for v in 'uvw'}}
    positive=compare(payload)
    check('synthetic exact retained comparison passes',positive['passed'])
    check('nonzero residual is retained rather than silently set to zero',any(x!='0' for row in positive['leftResidual'] for x in row))
    check('passing comparison is not promoted to analytical homotopy',not positive['analyticalHomotopyEstablished'])
    bad=copy.deepcopy(payload);bad['right']['uw'][2][2]='2'
    negative=compare(bad)
    check('endpoint-only mutation rejected by full edge and residual squares',not negative['passed'] and
          not negative['conditions']['edgeSquare:uw'] and not negative['conditions']['residualSquare'])
    check('regular-row-only test would miss the endpoint mutation',
          mul(matrix(C),matrix(left['uw']))[0]==mul(matrix(bad['right']['uw']),matrix(C))[0])
    bad=copy.deepcopy(payload);bad['endpointRight']['w']=[[0,1,0],[0,0,0]]
    check('dropped endpoint rejected',not compare(bad)['passed'])
    bad=copy.deepcopy(payload);bad['frames']['w']=[[2,0,0],[0,0,1],[0,0,0]]
    check('singular comparison frame rejected',not compare(bad)['passed'])
    bad=copy.deepcopy(payload);bad['left']['uv'],bad['left']['vw']=bad['left']['vw'],bad['left']['uv']
    check('swapped noncommuting dependent edge maps rejected',not compare(bad)['passed'])
    bad=copy.deepcopy(payload);bad['left']['uv'][0][0]=1.0
    try:compare(bad); rejected=False
    except ValueError:rejected=True
    check('inexact float input rejected',rejected)
    missing=['source-bound edge operators in both local presentations',
             'three invertible comparison frames on admitted carriers/domains',
             'two retained endpoint readouts and their transported frames',
             'analytical face homotopies or faithful-whiskering recovery data']
    check('actual registry assignment does not supply finite comparison payload',
          not any(k in face for k in payload))
    report={'status':'passed','check_count':len(checks),'checks':checks,'face':face,
            'actualFaceStatus':'blocked_missing_source_bound_payload','actualFaceComparisonEstablished':False,
            'implementationControl':{'origin':'synthetic exact finite matrices; not source analytical data',
                                     'payload':payload,'positive':positive,'endpointMutation':negative},
            'missingSourceBindings':missing,'analyticalCoherenceDischarged':False,
            'globalFieldTransportEstablished':False,'full114ChannelEstablished':False,
            'scope':'Executed gate and negative controls. F006 remains unverified. Faithful whiskering in the source requires an admitted observer-generated carrier and recovery map; cutoff exponent bookkeeping alone supplies neither.',
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [BINDING,*SOURCES,
             'research/strominger/checkers/esd7_retained_face_comparison.py',
             'research/strominger/checkers/check_esd7_retained_face_comparison.py']}}
    dest=ROOT/BASE/'esd7-retained-face-comparison.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','actualFaceStatus','actualFaceComparisonEstablished']}))


if __name__=='__main__':main()

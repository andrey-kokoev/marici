"""Exact neutron geometric carrier gate, not a guessed36-coordinate operator."""
from fractions import Fraction as F
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_operator_inputs import frame,action,mode,qa,qm,qs
V='research/voevodsky/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def encode(v):return [[str(a),str(b)] for a,b in v]
def dot(a,b):
    z=(F(0),F(0))
    for x,y in zip(a,b):z=qa(z,qm(x,y))
    return z

def main():
    gp=V+'results/four_six_center_cones.json';ap=V+'results/coupled_six_piece_belt_store.json'
    geo,ambient=load(gp),load(ap)
    assert geo['verification_passed']
    assert sha(gp)==ambient['record']['geometry_sha256']
    assert hashlib.sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    points={k:tuple(map(F,v)) for k,v in geo['belt_scaled_coordinates'].items()}
    for face in geo['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum(points[v][i] for v in face)/3 for i in range(3))
    triangles=[tuple(t) for t in ambient['record']['triangles']]
    assert len(triangles)==18
    q=((F(1),F(0),F(0)),(F(0),F(-1),F(0)),(F(0),F(0),F(-1)))
    original={k:frame(v) for k,v in points.items()}
    moved={k:action(q,v) for k,v in original.items()}
    inverse={v:k for k,v in original.items()}
    missing=[k for k,v in moved.items() if v not in inverse]
    rename={k:inverse[v] for k,v in moved.items() if v in inverse}
    closed=not missing and {tuple(rename[k] for k in t) for t in triangles}==set(triangles)
    # Independently evaluate the same ordered-mode formula in the target frame.
    mode_checks=0;vectors=[]
    for t in triangles:
        re,im=mode(t,points)
        c,a,b=[moved[k] for k in t]
        target_re=tuple(qa(x,qs(-F(1,2),qa(y,z))) for x,y,z in zip(c,a,b))
        target_im=tuple(qs(F(1,2),qa(y,qs(-1,z))) for y,z in zip(a,b))
        assert target_re==action(q,re) and target_im==action(q,im)
        vectors.extend([(re,target_re),(im,target_im)]);mode_checks+=1
    for a,ta in vectors:
        for b,tb in vectors:assert dot(a,b)==dot(ta,tb)
    assert all(action(q,moved[k])==v for k,v in original.items())
    # The selected twofold rotation must not be reported as the source C3.
    assert missing and not closed
    first=missing[0]
    paths=[gp,ap,V+'checkers/check_belt_operator_inputs.py',
           V+'checkers/check_ramsey_neutron_world_action.py',V+'contracts/ramsey-neutron-world-action-attempt.v1.json']
    out={'schema':'marici.ramsey-neutron-world-action.verification.v1',
         'status':'fixed-belt-not-closed-moving-belt-mode-covariance-checked',
         'scope_id':'complementary-world-action-on-native-neutron-belt-v1',
         'fixedCarrierClosed':closed,'pointsOutsideFixedCarrier':missing,
         'firstPointFailure':{'label':first,'source':encode(original[first]),'rotated':encode(moved[first])},
         'orderedModeCovarianceChecks':mode_checks,'realImagGramChecks':len(vectors)**2,
         'rotatedPoints':{k:encode(v) for k,v in moved.items()},'triangles':triangles,
         'fixedTriangleAxisPermutationConstructed':False,
         'rotatedCarrierPNBindingEstablished':False,'crossContextPNIntertwiningVerified':False,
         'electronActionEstablished':False,'parentDescentResolved':False,
         'source_sha256':{p:sha(p) for p in paths}}
    (ROOT/(V+'results/ramsey-neutron-world-action-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['rotatedPoints','triangles','source_sha256']},indent=2))
if __name__=='__main__':main()

"""Geometric proton action; typed boundary before neutron/E extensions."""
from pathlib import Path
import sys,json,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
from check_twelve_triangle_positive_geometry import rotation
V='research/voevodsky/';S='research/strominger/results/'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text())
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def action(labels,p):
    rot=rotation(p);rename=dict(zip('ABCD',('ABCD'[i] for i in p)))
    q=[[R() for _ in labels] for _ in labels]
    for j,label in enumerate(labels):
        edge,axis=label.split(':');target=''.join(rename[v] for v in edge)
        for i in range(3):q[labels.index(target+':'+'xyz'[i])][j]=R(rot[i]['xyz'.index(axis)])
    return q

def main():
    paths=[S+'common-three-carrier-protocol/proton.json',S+'common-three-carrier-protocol/neutron.json',S+'full-five-channel-candidate/verification.json']
    p,n,five=map(load,paths)
    for path,h in five['sourceHashes'].items():assert sha(path)==h,'stale five-channel input: '+path
    labels=p['source']['coordinates'];q=action(labels,(1,0,3,2));reader=action(labels,(2,3,0,1))
    assert len(q)==36 and mm(adj(q),q)==identity(36) and mm(q,q)==identity(36)
    assert mm(q,reader)==mm(reader,q)
    b=restore(five['protonFiveEmbedding']);assert mm(adj(b),b)==identity(5)
    qb=mm(q,b);induced=mm(adj(b),qb);projected=mm(b,induced)
    residual=[[x-y for x,y in zip(a,c)] for a,c in zip(qb,projected)]
    entries=[{'row':i,'coordinate':labels[i],'column':j,'value':serialize([[x]])[0][0]}
             for i,row in enumerate(residual) for j,x in enumerate(row) if x!=R()]
    invariant=not entries
    if invariant:assert mm(adj(induced),induced)==identity(5)
    # Different carrier labels are a type gate, not a failed commutator.
    assert n['source']['coordinates']!=labels
    assert all(x.startswith('triangle-') for x in n['source']['coordinates'])
    inputs=paths+[V+'contracts/ramsey-world-frame-action-attempt.v1.json',V+'checkers/check_ramsey_world_frame_action.py',
        'research/strominger/checkers/exact_multiradical.py','research/nima/checkers/check_twelve_triangle_positive_geometry.py']
    out={'schema':'marici.ramsey-world-frame-action.verification.v1','status':'proton-action-checked-neutron-geometric-binding-open',
         'scope_id':'complementary-marking-proton-world-action-v1','marking':[1,0,3,2],
         'rotation':[[str(x) for x in row] for row in rotation((1,0,3,2))],
         'protonAction':serialize(q),'isometry':True,'involution':True,'commutesWithPReader':True,
         'fixedFiveImageInvariant':invariant,'compressedFiveAction':serialize(induced),
         'fixedImageResidualNonzeroEntries':len(entries),'firstResidual':entries[0] if entries else None,
         'rotatedTargetEmbedding':serialize(qb),
         'neutronGeometricActionSupplied':False,'electronGeometricActionSupplied':False,
         'crossContextPNIntertwiningVerified':False,'parentDescentResolved':False,
         'source_sha256':{path:sha(path) for path in inputs}}
    (ROOT/(V+'results/ramsey-world-frame-action-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['protonAction','compressedFiveAction','rotatedTargetEmbedding','source_sha256']},indent=2))
if __name__=='__main__':main()

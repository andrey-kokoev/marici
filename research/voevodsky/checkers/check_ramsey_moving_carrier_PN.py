"""Reconstruct moving neutron planes and PN under a declared transported grid."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from exact_multiradical import Radical as A,sqrt,decode_A,rational,serialize,mm
from check_coupled_six_piece_belt import R,encoded
from check_belt_operator_inputs import mode
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[A({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R())
def rat(x):assert x.b==0;return x.a
def plane(r,s):
    a,b=rat(dot(s,s)),rat(dot(r,s));assert a>0
    v=tuple(x-(b/a)*y for x,y in zip(r,s));beta=rat(dot(v,v));assert beta>0 and dot(v,s)==0
    return {'columns':(s,v),'d':(a,beta),'z':((R(b),R(a)),(R(beta),R()))}

def main():
    paths={'geo':V+'results/four_six_center_cones.json','ambient':V+'results/coupled_six_piece_belt_store.json',
           'native':V+'results/belt_three_by_twelve_store.json','q':V+'results/ramsey-world-frame-action-v1.json',
           'grid':S+'baryon-tensor-grid/verification.json','pn':S+'global-PN-transport/verification.json',
           'p':S+'common-three-carrier-protocol/proton.json','n':S+'common-three-carrier-protocol/neutron.json'}
    d={k:load(p) for k,p in paths.items()}
    for k in ['pn']:
        for p,h in d[k]['sourceHashes'].items():assert sha(p)==h,'stale PN input '+p
    for p,h in d['q']['source_sha256'].items():assert sha(p)==h,'stale world action input '+p
    assert sha(paths['geo'])==d['ambient']['record']['geometry_sha256']
    assert d['native']['source_root']==d['ambient']['root']
    assert hashlib.sha256(json.dumps(d['ambient']['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==d['ambient']['root']
    points={k:tuple(map(F,v)) for k,v in d['geo']['belt_scaled_coordinates'].items()}
    for face in d['geo']['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum(points[k][i] for k in face)/3 for i in range(3))
    targets=[];source_planes=[]
    for t in d['ambient']['record']['triangles']:
        re,im=mode(t,points);r,s=[tuple(R(*x) for x in vec) for vec in (re,im)]
        source=plane(r,s)
        # Re-evaluate the frame constructor on rotated modes, not copied columns.
        target=plane((r[0],-r[1],-r[2]),(s[0],-s[1],-s[2]))
        assert target['d']==source['d'] and target['z']==source['z']
        for c,tc in zip(source['columns'],target['columns']):assert tc==(c[0],-c[1],-c[2])
        source_planes.append(source);targets.append(target)
    coordinates=d['native']['coordinates'];target_coordinates=[]
    for c in coordinates:
        t,axis=c['triangle'],c['axis'];target=targets[t]
        assert str(target['d'][axis])==c['d'] and encoded(target['z'][axis])==c['selected_numerator']
        target_coordinates.append({'triangle':t,'axis':axis,'d':str(target['d'][axis]),
            'selected_numerator':encoded(target['z'][axis]),
            'ambient_column':[[str(x.a),str(x.b)] for x in target['columns'][axis]]})
    assert len(target_coordinates)==36
    # Hence the geometric Q_N has identity coefficients between the old and
    # newly derived moving intrinsic frames; this is not a fixed-belt symmetry.
    q=restore(d['q']['protonAction']);oldT=restore(d['pn']['matrix'])
    rows=[];signs=[]
    for j in range(36):
        nonzero=[(i,q[i][j]) for i in range(36) if q[i][j]!=A()]
        assert len(nonzero)==1
        i,x=nonzero[0];s=rational(x);assert s in (-1,1);rows.append(i);signs.append(s)
    frames={}
    for species,key in [('proton','p'),('neutron','n')]:
        g=d['grid']['carriers'][species];metric=list(map(F,d[key]['source']['metric']))
        z=[decode_A(x) for x in g['sourceReturnColumn']]
        frames[species]={'metric':metric,'z':z,'grid':sum(g['grid'],[])}
    p,n=frames['proton'],frames['neutron']
    znew=[A() for _ in range(36)];mnew=[F(0)]*36
    for j,i in enumerate(rows):znew[i]=signs[j]*p['z'][j];mnew[i]=p['metric'][j]
    gridnew=[rows[j] for j in p['grid']]
    pphase=[z*sqrt(1/rational(z.conj()*z)) for z in znew]
    nphase=[z*sqrt(1/rational(z.conj()*z)) for z in n['z']]
    # Normalized return probabilities at each transported grid occurrence agree,
    # so the existing ordered factor rotations receive the same inputs.
    for j in p['grid']:
        assert mnew[rows[j]]*rational(znew[rows[j]].conj()*znew[rows[j]])==p['metric'][j]*rational(p['z'][j].conj()*p['z'][j])
    o=[restore(x) for x in d['pn']['factorRotations']]
    newT=[[A() for _ in range(36)] for _ in range(36)]
    for a,i in enumerate(n['grid']):
        for b,j in enumerate(gridnew):
            newT[i][j]=nphase[i]*sqrt(mnew[j]/n['metric'][i])*o[0][a//3][b//3]*o[1][a%3][b%3]*pphase[j].conj()
    assert mm(newT,q)==oldT
    wrong=mm(oldT,q)
    failures=[(i,j) for i in range(36) for j in range(36) if wrong[i][j]!=oldT[i][j]]
    assert failures,'unchanged target map unexpectedly satisfies world square'
    inputs=list(paths.values())+[V+'contracts/ramsey-moving-carrier-PN-attempt.v1.json',
        V+'checkers/check_ramsey_moving_carrier_PN.py',V+'checkers/check_belt_operator_inputs.py',
        V+'checkers/check_coupled_six_piece_belt.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-moving-carrier-PN.verification.v1','status':'passed',
         'scope_id':'moving-neutron-planes-transported-grid-PN-covariance-v1',
         'reconstructedPlaneFrames':18,'intrinsicCoordinates':target_coordinates,
         'targetPN':serialize(newT),'targetProtonGrid':gridnew,
         'PNWorldSquareEntries':1296,'PNWorldSquare':'I_moving_N T_A = T_B Q_P',
         'unchangedTargetPNFailingEntries':len(failures),'firstUnchangedTargetFailure':list(failures[0]),
         'transportedGridPolicy':True,'independentGridSelectionProved':False,
         'fixedBeltSymmetryClaimed':False,'NEWorldSquareProved':False,
         'nativeWGRestrictionProved':False,'parentDescentResolved':False,
         'source_sha256':{p:sha(p) for p in inputs}}
    (ROOT/(V+'results/ramsey-moving-carrier-PN-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['intrinsicCoordinates','targetPN','targetProtonGrid','source_sha256']},indent=2))
if __name__=='__main__':main()

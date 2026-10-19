"""Independent degree-five Bose cut from the crossed local photon Born tensors."""
import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_local_ward_basis_v1 as w
import check_mixed_photon_ir_logs as archived
CONTRACT=HOME/'contracts/photon-degree5-cut-v1.json'
PROOF=HOME/'photon-degree5-cut-v1.md'
TEST=HOME/'checkers/test_photon_degree5_cut_v1.py'
MANIFEST=HOME/'scc-models/photon-degree5-cut-v1.json'
RESULT=HOME/'results/photon-degree5-cut-v1.json'


def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return tuple(p)
def add(a,b):return trim(tuple((a[i] if i<len(a) else Q())+(b[i] if i<len(b) else Q()) for i in range(max(len(a),len(b)))))
def scale(c,p):return trim(tuple(c*x for x in p))
def mul(a,b):
    r=[Q()]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return trim(r)
def integral(p):return sum((x/Q(i+1) for i,x in enumerate(p)),Q())
def evaluate(p,x):return sum((c*x**i for i,c in enumerate(p)),Q())
def interpolate(points):
    out=(Q(),)
    for i,(x,y) in enumerate(points):
        p=(Q(1),);d=Q(1)
        for j,(z,_) in enumerate(points):
            if i!=j:p=mul(p,(-z,Q(1)));d*=x-z
        out=add(out,scale(y/d,p))
    return out


def born_polynomials(drop_f3=False):
    data=[[[] for _ in w.PHI] for _ in range(2)]
    for c,s in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        rows=w.amplitude_rows(c,s)
        for i,v in enumerate(rows):
            data[0][i].append((s*s,(v[0]-v[1])/4))
            data[1][i].append((s*s,(v[2]-(0 if drop_f3 else 3*v[3]))/4))
    return tuple(tuple(interpolate(points) for points in order) for order in data)


LEGENDRE=((Q(1),),(Q(1),Q(-2)),(Q(1),Q(-6),Q(6)),(Q(1),Q(-12),Q(30),Q(-20)))
D22=((Q(1),Q(-2),Q(1)),(Q(1),Q(-8),Q(13),Q(-6)))


def project(born):
    out=[]
    for phis in born:
        equal={name:tuple(integral(mul(add(phis[0],scale(sign,phis[1])),P))/16 for P in LEGENDRE)
               for name,sign in (('plus',1),('minus',-1))}
        mixed=tuple(integral(mul(d,phis[2]))/8 for d in D22)
        # Completeness is checked by exact polynomial reconstruction, not samples.
        for name,sign in (('plus',1),('minus',-1)):
            recon=(Q(),)
            for J,P in enumerate(LEGENDRE):recon=add(recon,scale(16*(2*J+1)*equal[name][J],P))
            assert recon==add(phis[0],scale(sign,phis[1]))
            assert equal[name][1]==equal[name][3]==0
        recon=(Q(),)
        for J,d,m in zip((2,3),D22,mixed):recon=add(recon,scale(8*(2*J+1)*m,d))
        assert recon==phis[2]
        out.append({**equal,'mixed':mixed})
    return tuple(out)


def reconstruct(waves,interference_factor=1):
    a,b=waves;D=O=M=(Q(),)
    for J,P in enumerate(LEGENDRE):
        plus=a['plus'][J]*b['plus'][J];minus=a['minus'][J]*b['minus'][J]
        D=add(D,scale(8*(2*J+1)*(plus+minus)*interference_factor,P))
        O=add(O,scale(8*(2*J+1)*(plus-minus)*interference_factor,P))
    for j,(J,d) in enumerate(zip((2,3),D22)):
        M=add(M,scale(8*(2*J+1)*a['mixed'][j]*b['mixed'][j]*interference_factor,d))
    return D,O,M


def archived_target():
    # Call only the comparison endpoint AFTER deriving the new Born/cut data.
    Dz,o,Mx,_=archived.cut_polynomials();z=(Q(1),Q(-2));x=(Q(1),Q(-1))
    def substitute(p,q):
        out=(Q(),);power=(Q(1),)
        for c in p:out=add(out,scale(c,power));power=mul(power,q)
        return out
    return scale(Q(1,16),substitute(Dz,z)),(o/16,),scale(Q(1,16),substitute(Mx,x))


def validate(c):
    assert c['schema']=='marici.photon-degree5-cut.v1' and c['owner']=='marici.Nima'
    assert c['Born_family']=='R=r0*s^2+r1*s^3; Phi1=lambda_gamma*R(s)/4; Phi2=-lambda_gamma*sum R/4; Phi5=0'
    for k in ('cut_independently_reconstructed_from_covariant_Born','archived_degree5_interference_matches',
              'both_interference_orderings_retained','forward_invisible_f3_Born_effect_retained'):
        assert c[k] is True,k
    for k in ('general_degree5_photon_EFT_cut_classified','physical_matching_selected','native_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=w.build()
    born=born_polynomials();waves=project(born);derived=reconstruct(waves);target=archived_target()
    assert derived==target,(derived,target)
    # Fifth, unused angle confirms the tensor-to-polynomial interface independently.
    for order in range(2):
        c0,s0=Q(7,25),Q(24,25);rows=w.amplitude_rows(c0,s0)
        for i,v in enumerate(rows):
            value=(v[0]-v[1])/4 if order==0 else (v[2]-3*v[3])/4
            assert evaluate(born[order][i],s0*s0)==value
    assert waves[0]['mixed'][1]==0 and waves[1]['mixed'][1]!=0
    assert all(p==0 for p in born[0][4]+born[1][4])
    # A missing forward-invisible Born term changes a FORWARD loop cut.
    badborn=born_polynomials(True);badwaves=project(badborn);bad=reconstruct(badwaves)
    assert all(evaluate(born[n][i],Q())==evaluate(badborn[n][i],Q()) for n in range(2) for i in range(5))
    deltaD=add(bad[0],scale(-1,derived[0]));deltaO=add(bad[1],scale(-1,derived[1]))
    assert evaluate(deltaD,Q())==-Q(1,320) and deltaO==(Q(1,512),)
    assert reconstruct(waves,Q(1,2))!=target
    # The full two-term wave square is nonnegative even when its interference is negative.
    assert waves[0]['plus'][0]*waves[1]['plus'][0]<0
    assert 3*waves[0]['plus'][0]+4*waves[1]['plus'][0]==0
    for r0,r1 in product((Q(-2),Q(),Q(1),Q(3)),repeat=2):
        for name in ('plus','minus','mixed'):
            for a,b in zip(waves[0][name],waves[1][name]):
                assert (r0*a+r1*b)**2==r0*r0*a*a+2*r0*r1*a*b+r1*r1*b*b>=0
    refused=[]
    for key in ('general_degree5_photon_EFT_cut_classified','physical_matching_selected','native_dynamics_derived','C12_budget_renewed'):
        badc={**c,key:True}
        try:validate(badc)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported degree-five promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']}
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve(),archived.CONTRACT,archived.PROOF))
    paths.update(Path(m.__file__).resolve() for m in (archived,archived.ct,archived.logs,archived.cut,archived.crossed))
    encode=lambda p:list(map(str,p))
    return {'schema':'marici.photon-degree5-cut-receipt.v1','status':'pass',
        'scope':'independent_cut_compatibility_for_declared_R2_R3_family_not_general_degree5_EFT',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'angular_variable':'alpha=(1-z)/2; x=1-alpha',
        'Born_Phi_polynomials':[[encode(p) for p in order] for order in born],
        'pi_times_Bose_partial_waves':[{k:encode(v) for k,v in ws.items()} for ws in waves],
        'pi_times_invariant_degree5_cut_D_O_M':[encode(p) for p in derived],
        'drop_f3_forward_Born_unchanged':True,'drop_f3_forward_loop_D_defect':'-1/320','drop_f3_forward_loop_O_defect':'1/512',
        'r0_r1_J3_interference':'0','r1_J3_Born_wave':str(waves[1]['mixed'][1]),
        **{k:v for k,v in c.items() if isinstance(v,bool)},'general_partial_wave_proof_machine_formalized':False,
        'hostile_controls_refused':['drop_forward_invisible_f3','omit_one_interference_ordering','require_signed_interference_positive']+refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale degree-five cut receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','pi_times_invariant_degree5_cut_D_O_M','drop_f3_forward_loop_D_defect','drop_f3_forward_loop_O_defect','general_degree5_photon_EFT_cut_classified')}))

if __name__=='__main__':main()

"""Complete quadratic photon degree-six cut: Born2 x Born4 plus Born3 squared."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree5_cut_v1 as prev
import check_degree6_photon_ir_logs as archived
base=prev.base;p=prev.family
CONTRACT=HOME/'contracts/photon-general-degree6-cut-v1.json';PROOF=HOME/'photon-general-degree6-cut-v1.md'
TEST=HOME/'checkers/test_photon_general_degree6_cut_v1.py';MANIFEST=HOME/'scc-models/photon-general-degree6-cut-v1.json'
RESULT=HOME/'results/photon-general-degree6-cut-v1.json'
NAMES=base.NAMES
DEGREES=(2,2,3,3,3,4,4,4)
PAIRS=((0,5),(0,6),(0,7),(1,5),(1,6),(1,7),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4))
MONOMIALS=tuple(NAMES[i]+'*'+NAMES[j] for i,j in PAIRS)
LEGENDRE=p.LEGENDRE+((Q(1),Q(-20),Q(90),Q(-140),Q(70)),)
D22=p.D22+((Q(1),Q(-16),Q(57),Q(-70),Q(28)),)


def unit_born():
    data=[[[] for _ in base.PHI] for _ in NAMES]
    angles=((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(7,25),Q(24,25)))
    for c,s in angles:
        rows=base.amplitude_rows(c,s)
        for n in range(8):
            for i,row in enumerate(rows):data[n][i].append((s*s,row[n]))
    return tuple(tuple(p.interpolate(points) for points in column) for column in data)


def project(phi):
    equal={name:tuple(p.integral(p.mul(p.add(phi[0],p.scale(sign,phi[1])),P))/16 for P in LEGENDRE)
           for name,sign in (('plus',1),('minus',-1))}
    mixed=tuple(p.integral(p.mul(d,phi[2]))/8 for d in D22)
    off=p.integral(p.mul(prev.K,phi[4]))/8
    for name,sign in (('plus',1),('minus',-1)):
        value=(Q(),)
        for J,P in enumerate(LEGENDRE):value=p.add(value,p.scale(16*(2*J+1)*equal[name][J],P))
        assert value==p.add(phi[0],p.scale(sign,phi[1]))
        assert equal[name][1]==equal[name][3]==0
    value=(Q(),)
    for J,d,m in zip((2,3,4),D22,mixed):value=p.add(value,p.scale(8*(2*J+1)*m,d))
    assert value==phi[2] and p.scale(240*off,prev.K)==phi[4]
    return {**equal,'mixed':mixed,'off':off}


def project_cut(positive,negative,mixed_odd):
    D=O=M=(Q(),)
    for J in (0,2,4):
        a,b,d=positive[J];minus=negative[J]
        D=p.add(D,p.scale(8*(2*J+1)*(a+minus),LEGENDRE[J]))
        O=p.add(O,p.scale(8*(2*J+1)*(a-minus),LEGENDRE[J]))
        if J:M=p.add(M,p.scale(8*(2*J+1)*d,D22[J-2]))
    M=p.add(M,p.scale(56*mixed_odd,D22[1]))
    H=p.scale(240*positive[2][1],prev.K)
    return D,O,M,H


def bilinear(A,B):
    positive={0:(A['plus'][0]*B['plus'][0],Q(),Q())};negative={0:A['minus'][0]*B['minus'][0]}
    for J in (2,4):
        positive[J]=prev.sym_product((A['plus'][J],A['off'] if J==2 else Q(),A['mixed'][J-2]),
                                     (B['plus'][J],B['off'] if J==2 else Q(),B['mixed'][J-2]))
        negative[J]=A['minus'][J]*B['minus'][J]
    return project_cut(positive,negative,A['mixed'][1]*B['mixed'][1])


def inventory():
    born=unit_born();waves=tuple(project(phi) for phi in born)
    cases=tuple(tuple(p.scale(Q(1,2) if i==j else Q(1),v) for v in bilinear(waves[i],waves[j])) for i,j in PAIRS)
    return born,waves,cases


def direct_coefficient6(values,waves):
    # Independently form each graded physical Born block, square it, then extract degree six.
    def total(name,J,d):return sum((x*w[name][J] for x,w,n in zip(values,waves,DEGREES) if n==d),Q())
    def off(d):return sum((x*w['off'] for x,w,n in zip(values,waves,DEGREES) if n==d),Q())
    prod=lambda A,B:sum((A[d]*B[6-d] for d in (2,3,4)),Q())/2
    positive={};negative={}
    for J in (0,2,4):
        a={d:total('plus',J,d) for d in (2,3,4)}
        b={d:off(d) if J==2 else Q() for d in (2,3,4)}
        dd={d:total('mixed',J-2,d) if J else Q() for d in (2,3,4)}
        m={d:total('minus',J,d) for d in (2,3,4)}
        positive[J]=(prod(a,a)+6*prod(b,b),prod(b,{d:a[d]+dd[d] for d in (2,3,4)}),prod(dd,dd)+6*prod(b,b))
        negative[J]=prod(m,m)
    odd={d:total('mixed',1,d) for d in (2,3,4)}
    return project_cut(positive,negative,prod(odd,odd))


def combine(cases,values):return prev.combine(cases,tuple(values[i]*values[j] for i,j in PAIRS))


def archived_target(sector):
    Dz,o,Mx,_=archived.sector_polynomials(sector)
    def substitute(poly,q):
        value=(Q(),);power=(Q(1),)
        for c in poly:value=p.add(value,p.scale(c,power));power=p.mul(power,q)
        return value
    return p.scale(Q(1,16),substitute(Dz,(Q(1),Q(-2)))),(o/16,),p.scale(Q(1,16),substitute(Mx,(Q(1),Q(-1)))),(Q(),)


def validate(c):
    assert c['schema']=='marici.photon-general-degree6-cut.v1' and c['owner']=='marici.Nima'
    assert c['coupling_order']==list(NAMES) and c['monomial_order']==list(MONOMIALS)
    for k in ('full_degree6_quadratic_two_photon_cut_constructed','Born2_Born4_and_Born3_square_retained',
              'higher_Born_waves_retained','independent_quartic_Born_contacts_retained'):
        assert c[k] is True,k
    for k in ('all_h3_fibres_resolved_by_degree6','degree6_log_window_tensor_constructed',
              'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=prev.build()
    born,waves,cases=inventory()
    for sector,source in (('c1_squared',(0,0,Q(1,4),-Q(3,4),0,0,0,0)),
                          ('c0_r4',(Q(1,4),-Q(1,4),0,0,0,Q(1,4),0,-Q(1,8)))):
        got=combine(cases,source)
        if sector=='c0_r4': # contains only 2-by-4 at degree six
            assert all(source[i]==0 for i in (2,3,4))
        assert got==archived_target(sector),(sector,got,archived_target(sector))
    checks=0
    for values in product((Q(-1),Q(1)),repeat=8):
        assert combine(cases,values)==direct_coefficient6(values,waves);checks+=1
    for n in range(8):
        values=tuple(Q(int(i==n)) for i in range(8))
        assert combine(cases,values)==direct_coefficient6(values,waves);checks+=1
    # Higher source waves exist although their current 2-by-4 products vanish.
    assert waves[7]['plus'][4]==Q(1,2520) and waves[5]['mixed'][2]==Q(1,2016)
    assert all(waves[i]['plus'][4]==waves[i]['mixed'][2]==0 for i in (0,1,2,3,4))
    # h3 squared is a positive physical block; individual angular coefficients need not be positive.
    h2=cases[11]
    assert h2==(p.scale(Q(1,480),LEGENDRE[2]),p.scale(Q(1,480),LEGENDRE[2]),
                p.scale(Q(1,480),D22[0]),(Q(),))
    assert cases[8][3]==(Q(),-Q(1,96),Q(1,96))
    assert cases[10][3]==(Q(),-Q(1,960),Q(1,960))
    # Fixed nonzero quartic nuisance inputs: h3 sign can still be invisible through degree six.
    x=(Q(1),Q(-6),Q(2),Q(-20),Q(1),Q(1),Q(-2),Q(3));y=x[:4]+(-x[4],)+x[5:]
    import check_photon_joint_cut_fibres_v1 as fibres
    assert fibres.observe(x[:5])==fibres.observe(y[:5])
    assert combine(cases,x)==combine(cases,y) and x!=y and x!=tuple(-v for v in y)
    born_defect=2*base.amplitude_rows(Q(3,5),Q(4,5))[4][4];assert born_defect==Q(288,625)
    # Complete square PSD retained; the isolated degree-six coefficient can be negative.
    negative=combine(cases,(Q(1),Q(),Q(),Q(),Q(),Q(-1),Q(),Q()))
    assert p.evaluate(negative[0],Q())<0
    psd=0
    for values in product((Q(-1),Q(1)),repeat=8):
        s=Q(1,2);a=b=d=Q()
        for value,w,n in zip(values,waves,DEGREES):
            a+=value*s**n*w['plus'][2];b+=value*s**n*w['off'];d+=value*s**n*w['mixed'][0]
        assert prev.square_psd(a,b,d);psd+=1
    # Distinguish h3^2 from three quartic nuisance directions at the h3-cancellation leading pair.
    mapcols=tuple(tuple(cases[i][r][n] if n<len(cases[i][r]) else Q() for i in range(12))
                  for r in range(4) for n in range(max(len(case[r]) for case in cases)))
    nuisance=tuple((row[0]-6*row[3],row[1]-6*row[4],row[2]-6*row[5]) for row in mapcols)
    augmented=tuple(row+(full[11],) for row,full in zip(nuisance,mapcols))
    ranks=(len(base.reduced_rows(nuisance)[1]),len(base.reduced_rows(augmented)[1]))
    assert ranks==(3,4)
    # Sixth unused angle for the source-polynomial interface.
    cc,ss=Q(20,29),Q(21,29);rows=base.amplitude_rows(cc,ss)
    for j,phis in enumerate(born):
        for i,poly in enumerate(phis):assert p.evaluate(poly,ss*ss)==rows[i][j]
    refused=['omit_Born2_Born4_interference','drop_h3_square','erase_inactive_higher_Born_waves','infer_positive_homogeneous_coefficient_from_full_square']
    for key in ('all_h3_fibres_resolved_by_degree6','degree6_log_window_tensor_constructed',
                'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported degree-six promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']}
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve(),Path(fibres.__file__).resolve(),fibres.PROOF,fibres.CONTRACT,archived.CONTRACT,archived.PROOF))
    paths.update(Path(m.__file__).resolve() for m in (archived,archived.mixed,archived.ct,archived.logs,archived.cut,archived.crossed))
    enc=lambda poly:list(map(str,poly))
    return {'schema':'marici.photon-general-degree6-cut-receipt.v1','status':'pass',
        'scope':'full_degree6_quadratic_two_photon_cut_of_independent_Born_jet_through_degree4_not_log_window_or_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'coupling_order':list(NAMES),'monomial_order':list(MONOMIALS),
        'unit_Born_Bose_waves':[{k:str(v) if isinstance(v,Q) else enc(v) for k,v in w.items()} for w in waves],
        'cut_D_O_M_Phi5_by_monomial':[[enc(v) for v in case] for case in cases],
        'cut_response_rank':len(base.reduced_rows(mapcols)[1]),'source_monomial_dimension':12,
        'independent_complete_square_coefficient_checks':checks,'complete_Born_block_PSD_controls':psd,
        'R_family_sector_matches':['c1_squared','c0_r4'],
        'Phi5_cut':'-h3*(10*g3+f3)*s^4*t*u/960',
        'h3_square_forward_D_O_M':['1/480','1/480','1/480'],
        'remaining_sign_witness':{'source1':enc(x),'source2':enc(y),'Born_Phi5_difference':str(born_defect)},
        'quartic_nuisance_vs_h3_square_ranks':list(ranks),
        'general_partial_wave_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale general degree-six cut receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','cut_response_rank','source_monomial_dimension','Phi5_cut','quartic_nuisance_vs_h3_square_ranks','all_h3_fibres_resolved_by_degree6')}))

if __name__=='__main__':main()

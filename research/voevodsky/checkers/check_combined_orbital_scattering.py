"""Combined scalar-record/vector triple channels: exact optical matrix controls
and certified flux intervals at E=6. Declared core and vertices, not native rates.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_multiobject_onband import Interval
from check_pentachoron_spin_interfaces import A,CI,S2,S3,mm,adj,scale,add
from check_typed_spin_channels import eye,kron,decode

BASE=Path(__file__).resolve().parents[1]

def load(name):
    path=BASE/'results'/name;r=json.loads(path.read_text(encoding='utf-8'));assert r['verification_passed']
    for source,digest in r['source_hashes'].items():assert sha256((BASE/source).read_bytes()).hexdigest()==digest
    return path,r

def decode_interval(record):return Interval(Q(record['lower']),Q(record['upper']))
def intersection(a,b):return Interval(max(a.low,b.low),min(a.high,b.high))
def outward_grid(v,grid=10**10):
    lower=v.low.numerator*grid//v.low.denominator
    upper=-((-v.high.numerator*grid)//v.high.denominator)
    return Interval(Q(lower,grid),Q(upper,grid))
def sqrt_interval(v):
    from math import isqrt
    scale_=10**12
    lower=isqrt(v.low.numerator*scale_**2//v.low.denominator)
    upper=isqrt(v.high.numerator*scale_**2//v.high.denominator)+1
    return Interval(Q(lower,scale_),Q(upper,scale_))

def direct_sum(*matrices):
    n=sum(len(M) for M in matrices);out=[[A() for _ in range(n)] for _ in range(n)];offset=0
    for M in matrices:
        for i,row in enumerate(M):
            for j,value in enumerate(row):out[offset+i][offset+j]=value
        offset+=len(M)
    return tuple(tuple(row) for row in out)

def scattering_control(detuning,roots):
    width=sum((r*r for r in roots),A());G=(A(detuning)+CI*width/2).inverse()
    S=tuple(tuple(A(i==j)-CI*ri*rj*G for j,rj in enumerate(roots)) for i,ri in enumerate(roots))
    return S,G,width

def norm(x):return x.flip(8)*x

def fixture(u,a,b,c,v):
    # Scalar input and two-output widths 2b, scalar triple width 2u*c.
    den=4*a.square()+(2*b+u*c).square()
    Ts=4*b.square()/den;Ta=4*u*b*c/den;Rs=(4*a.square()+(u*c).square())/den
    denv=a.square()+(b+v).square()
    Tv=4*b*v/denv;Rv=(a.square()+(b-v).square())/denv
    # Physical identities improve intervals, without assuming independent
    # extremes can occur simultaneously or silently replacing error bounds.
    Ts=intersection(Ts,1-Rs-Ta);Ta=intersection(Ta,1-Rs-Ts);Rs=intersection(Rs,1-Ts-Ta)
    Tv=intersection(Tv,1-Rv);Rv=intersection(Rv,1-Tv)
    P2=Ts/4;Pa=Ta/4;Pv=Q(3,4)*Tv;P3=Pa+Pv
    survival=intersection(Rs/4+Q(3,4)*Rv,1-P2-P3)
    return {'scalar_R':Rs,'scalar_two_T':Ts,'scalar_three_T':Ta,'vector_R':Rv,'vector_three_T':Tv,
        'two_output':P2,'scalar_three_output':Pa,'vector_three_output':Pv,'three_output':P3,'survival':survival}

def main():
    on_path,on=load('multiobject_onband.json');orb_path,orb=load('orbital_record_selfenergy.json');typed_path,typed=load('typed_spin_channels.json')
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    response=on['retarded_selfenergy_at_unit_coupling']
    a=decode_interval(response['a2']);b=decode_interval(response['b2']);v=decode_interval(response['b3'])
    c=decode_interval(orb['center_unit_coupling_Gamma'])/2
    original=(a,b,c,v);a,b,c,v=map(outward_grid,original)
    check('rational_grid_rounding_is_outward',all(y.low<=x.low<=x.high<=y.high for x,y in zip(original,(a,b,c,v))))
    # Exact algebraic arithmetic, not floating tolerances, for optical matrices.
    Ss,Gs,gs=scattering_control(Q(-4,5),(A(1),S2,S3))
    Sv,Gv,gv=scattering_control(Q(-2,7),(A(1),S3))
    check('scalar_three_channel_matrix_unitary',mm(adj(Ss),Ss)==eye(3) and mm(Ss,adj(Ss))==eye(3))
    check('vector_two_channel_matrix_unitary',mm(adj(Sv),Sv)==eye(2) and mm(Sv,adj(Sv))==eye(2))
    check('scalar_core_optical_identity',Gs-Gs.flip(8)==-CI*gs*Gs*Gs.flip(8))
    check('vector_core_optical_identity',Gv-Gv.flip(8)==-CI*gv*Gv*Gv.flip(8))
    full=direct_sum(Ss,kron(Sv,eye(3)))
    check('nine_fiber_full_bright_matrix_unitary',len(full)==9 and mm(adj(full),full)==eye(9))
    check('no_scalar_vector_coherence_added',all(full[i][j]==0 and full[j][i]==0 for i in range(3) for j in range(3,9)))
    for index,cycle in enumerate(typed['native_cycle_reports']):
        R=tuple(tuple(decode(x) for x in row) for row in cycle['vector_action'])
        action=direct_sum(eye(3),kron(eye(2),R))
        check('full_native_cycle_covariance_'+str(index),mm(full,action)==mm(action,full))
    check('scalar_column_probability_one',sum((norm(full[i][0]) for i in range(9)),A())==1)
    check('vector_column_probability_one',all(sum((norm(full[i][j]) for i in range(9)),A())==1 for j in range(3,6)))
    # Symbolic probability identity reduced to exact rational controls for
    # unequal scalar couplings: d^2+(B-2b0)^2+4b0(b1+bA)=d^2+B^2.
    for index,(d,b0,b1,ba) in enumerate(((Q(2,5),Q(3,7),Q(1,4),Q(5,6)),(Q(-3,4),Q(1,2),Q(2,3),Q(1,8)))):
        B=b0+b1+ba
        check('unequal_three_channel_flux_identity_'+str(index),d*d+(B-2*b0)**2+4*b0*(b1+ba)==d*d+B*B)
    sweep=[];models={}
    for u in map(Q,('0','1/4','1','4','16','64')):
        p=fixture(u,a,b,c,v);models[u]=p
        check('scalar_flux_enclosure_'+str(u),(p['scalar_R']+p['scalar_two_T']+p['scalar_three_T']).contains(1))
        check('vector_flux_enclosure_'+str(u),(p['vector_R']+p['vector_three_T']).contains(1))
        check('unpolarized_flux_enclosure_'+str(u),(p['survival']+p['two_output']+p['three_output']).contains(1))
        check('probabilities_in_unit_interval_'+str(u),all(0<=x.low<=x.high<=1 for x in p.values()))
        sweep.append({'lambda_A_squared':str(u),'probability_enclosures':{name:value.record() for name,value in p.items()},
            'two_to_all_three_ratio':(p['two_output']/p['three_output']).record()})
    check('zero_new_coupling_recovers_previous_fixture',models[Q(0)]['scalar_three_T'].low==models[Q(0)]['scalar_three_T'].high==0 and all(models[Q(0)][name].low<=Q(on['typed_scattering_fixture']['unpolarized_probabilities'][name]['upper']) and Q(on['typed_scattering_fixture']['unpolarized_probabilities'][name]['lower'])<=models[Q(0)][name].high for name in ('two_output','three_output','survival')))
    check('scalar_record_channel_is_open_at_unit_coupling',models[Q(1)]['scalar_three_output'].low>0)
    check('unit_coupling_suppresses_two_output_relative_to_zero',models[Q(1)]['two_output'].high<models[Q(0)]['two_output'].low)
    check('strong_coupling_reduces_scalar_triple_conversion',models[Q(64)]['scalar_three_output'].high<models[Q(1)]['scalar_three_output'].low)
    check('orthogonal_vector_flux_unchanged',all(models[u]['vector_three_output'].low==models[Q(0)]['vector_three_output'].low and models[u]['vector_three_output'].high==models[Q(0)]['vector_three_output'].high for u in models))
    optimum=2*sqrt_interval(a.square()+b.square())/c
    check('finite_positive_conversion_optimum',optimum.low>0 and optimum.high<4)
    result={'verification_passed':all(checks.values()),'checks':checks,'energy':'6','core':'H_core=6 I4',
        'couplings':'lambda_in=lambda_2=lambda_vector3=1; lambda_A^2 varied',
        'response_inputs_outward_rounded_to_1e_minus_10':{name:value.record() for name,value in zip(('a2','b2','bA','b_vector3'),(a,b,c,v))},
        'selfenergy_scalar':'[2(a2-i b2)-i u bA] P_scalar, u=lambda_A^2',
        'selfenergy_vector':'[a2-i(b2+b_vector3)] P_vector',
        'bright_channel_order':['incoming scalar','two-output scalar','orbital-record three-output scalar','incoming vector x3','three-output vector x3'],
        'scalar_scattering':'S_ij=delta_ij-i sqrt(2b_i) sqrt(2b_j)/(-2a2+i(2b2+u bA)), b=(b2,b2,u bA)',
        'vector_scattering':'S_ij=delta_ij-i sqrt(2b_i) sqrt(2b_j)/(-a2+i(b2+b_vector3))',
        'scalar_flux':'T2=4b2^2/D, TA=4u b2 bA/D, R=(4a2^2+u^2 bA^2)/D, D=4a2^2+(2b2+u bA)^2',
        'scalar_three_conversion_optimum_u':optimum.record(),
        'exact_matrix_control':{'detunings':['-4/5','-2/7'],'scalar_widths':['1','2','3'],'vector_widths':['1','3'],
            'S':[[x.record() for x in row] for row in full]},
        'sweep':sweep,'unit_coupling_fixture':sweep[2],
        'qualifications':['All orbital self-energy bounds are inherited from infinite-volume certified continuum integrals.',
            'Exact matrix controls test optical algebra with declared rational detunings/widths; the E=6 physical fixture parameters remain interval-enclosed.',
            'Energy-fiber bright-channel probabilities are not initial internal retention or incident-wave capture probabilities.',
            'The scalar-record and vector triple outputs are orthogonal internal sectors; total multiplicity probability is their incoherent sum.',
            'No native core attachment, physical particle/channel identification or ratio calibration is supplied.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (on_path,orb_path,typed_path,Path(__file__),BASE/'checkers/check_multiobject_onband.py',BASE/'checkers/check_typed_spin_channels.py')}}
    (BASE/'results/combined_orbital_scattering.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'unit_coupling_probabilities':{name:value.record()['decimal_view'] for name,value in models[Q(1)].items() if name in ('two_output','scalar_three_output','vector_three_output','three_output','survival')},
        'conversion_optimum_lambda_A_squared':optimum.record()['decimal_view']},indent=2))

if __name__=='__main__':main()

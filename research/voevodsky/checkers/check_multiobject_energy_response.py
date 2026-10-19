"""Off-center infinite-volume responses and certified channel threshold widths.
Real-axis density certificates are separate from complex-energy resolvents.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_multiobject_orbital_selfenergy import moments
from check_orbital_record_selfenergy import exterior_moments,square_range
from check_multiobject_onband import Interval,pi_bounds,radius_bounds,root_bounds,SCALE,density_two,density_three
from check_pentachoron_spin_interfaces import A,CI

BASE=Path(__file__).resolve().parents[1]

def scalar_record_density(E,n,pl,ph):
    if E<=0 or E>=12:return Q(),Q()
    shift=Q(E*n,4);assert shift.denominator==1;shift=int(shift)
    radii=[radius_bounds(i,i+1,n) for i in range(n)];low=high=0
    for i,(a,b) in enumerate(radii):
        for j,(c,d) in enumerate(radii):
            f,g=radius_bounds(shift-i-j-2,shift-i-j,n)
            if not g:continue
            dl=dh=1
            for u,v in ((i-j-1,i-j+1),(2*i+j-shift,2*i+j+3-shift),(i+2*j-shift,i+2*j+3-shift)):
                l,h=square_range(u,v);dl*=l;dh*=h
            low+=root_bounds(a*c*f)[0]*dl;high+=root_bounds(b*d*g)[1]*dh
    factor=Q(128*4096,6*n**11*SCALE)
    return factor*low/ph**3,factor*high/pl**3

def complex_response(k,E,eta,raw,N):
    center=2*k
    centered=[sum(comb(n,j)*(-center)**(n-j)*raw[j] for j in range(n+1)) for n in range(N+1)]
    d=A(E-center)+CI*eta;inverse=d.inverse();term=inverse;value=A()
    for m in centered:
        value+=m*term;term*=inverse
    # |d|>=eta>2k makes the operator Neumann tail absolutely convergent.
    error=Q(2*k,eta)**(N+1)/(eta-2*k)
    assert all(x==0 for i,x in enumerate(value.c) if i not in (0,8))
    return Interval(value.c[0]-error,value.c[0]+error),Interval(value.c[8]-error,value.c[8]+error),error

def load(name):
    path=BASE/'results'/name;r=json.loads(path.read_text(encoding='utf-8'));assert r['verification_passed']
    for source,digest in r['source_hashes'].items():assert sha256((BASE/source).read_bytes()).hexdigest()==digest
    return path,r

def main():
    base_path,base=load('multiobject_orbital_selfenergy.json');orb_path,orb=load('orbital_record_selfenergy.json');combined_path,combined=load('combined_orbital_scattering.json')
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    pl,ph=pi_bounds();P=Interval(pl,ph)
    density_reports=[]
    for E in (2,4):
        reports=[]
        for n in (128,256,512):
            pair=Interval(*density_two(E,n,pl,ph));vector=Interval(*density_three(E,n,pl,ph));scalar=Interval(*scalar_record_density(E,n,pl,ph))
            check('positive_open_widths_'+str(E)+'_'+str(n),pair.low>0 and vector.low>0 and scalar.low>0)
            check('scalar_record_reflection_'+str(E)+'_'+str(n),scalar_record_density(12-E,n,pl,ph)==(scalar.low,scalar.high))
            check('vector_record_reflection_'+str(E)+'_'+str(n),density_three(12-E,n,pl,ph)==(vector.low,vector.high))
            reports.append({'mesh':n,'rho_pair':pair.record(),'rho_vector3':vector.record(),'rho_scalar3':scalar.record()})
        check('offcenter_widths_refine_'+str(E),all(Q(b[key]['upper'])-Q(b[key]['lower'])<Q(a[key]['upper'])-Q(a[key]['lower']) for a,b in zip(reports,reports[1:]) for key in ('rho_pair','rho_vector3','rho_scalar3')))
        density_reports.append({'energy':str(E),'refinements':reports,
            'unit_coupling_widths':{'pair':(2*P*pair).record(),'vector3':(2*P*vector).record(),'scalar3':(2*P*scalar).record()},
            'triple_reflected_energy':str(12-E),'pair_reflected_energy':str(8-E)})
    # At E=8 the pair fiber has zero spectral weight, while triple E=8 widths
    # equal E=4 widths. At E=10 triples reflect E=2; pair is outside its band.
    check('pair_upper_threshold_width_zero',density_two(8,128,pl,ph)==(0,0))
    check('pair_above_threshold_width_zero',density_two(10,128,pl,ph)==(0,0))
    check('triple_upper_threshold_width_zero',density_three(12,128,pl,ph)==(0,0) and scalar_record_density(12,128,pl,ph)==(0,0))
    check('triple_above_threshold_width_zero',density_three(14,128,pl,ph)==(0,0) and scalar_record_density(14,128,pl,ph)==(0,0))
    N=128;raws={'pair':(2,moments(2,N)),'vector3':(3,moments(3,N)),'scalar3':(3,exterior_moments(N))}
    complex_reports=[];evaluated={}
    for name,(k,raw) in raws.items():
        for E in (2,4,6,8,10):
            re,im,error=complex_response(k,E,8,raw,N);evaluated[name,E]=(re,im)
            check('complex_tail_control_'+name+'_'+str(E),error<Q(1,10**15))
            check('causal_sign_'+name+'_'+str(E),im.high<0)
            maxdistance=max(abs(E),abs(E-4*k))
            check('causal_measure_bound_'+name+'_'+str(E),im.high<=-Q(8,maxdistance**2+64))
            max_re=max(abs(re.low),abs(re.high));max_im=max(abs(im.low),abs(im.high))
            check('complex_resolvent_norm_'+name+'_'+str(E),max_re**2+max_im**2<Q(1,64))
            complex_reports.append({'channel':name,'z':{'Re':str(E),'Im':'8'},'Re_g':re.record(),'Im_g':im.record(),'tail_bound':str(error),'terms':N+1})
        for E in (2,4,6,8,10):
            reflected=4*k-E
            if (name,reflected) in evaluated:
                r,i=evaluated[name,E];rr,ii=evaluated[name,reflected]
                check('complex_reflection_'+name+'_'+str(E),r.low==-rr.high and r.high==-rr.low and i.low==ii.low and i.high==ii.high)
    check('orbital_vertex_changes_offcenter_complex_response',evaluated['scalar3',4][1].high<evaluated['vector3',4][1].low)
    # On-shell incoming pair ends at E=8. Open output fibers above eight do not
    # by themselves authorize an incident-pair flux probability there.
    threshold_table=[{'energy':E,'pair_density':state_pair,'triple_densities':state_three,'pair_incidence':'open' if 0<E<8 else 'not finite-flux pair incidence'} for E,state_pair,state_three in
        ((0,'zero','zero'),(2,'positive','positive'),(4,'positive','positive'),(6,'positive','positive'),(8,'zero','positive'),(10,'zero','positive'),(12,'zero','zero'),(14,'zero','zero'))]
    result={'verification_passed':all(checks.values()),'checks':checks,
        'real_axis_density_reports':density_reports,'threshold_table':threshold_table,
        'complex_energy_reports':complex_reports,
        'complex_tail_certificate':'Expand around spectral midpoint 2k: g(z)=sum_n <(H-2k)^n>/(z-2k)^(n+1). For Im z=eta>2k the tail is <=(2k/eta)^(N+1)/(eta-2k).',
        'selfenergy_matrices':'Multiply g_pair by lambda_in^2 I4 or lambda_2^2 Ps; g_vector3 by lambda_vector3^2 Pv; g_scalar3 by lambda_A^2 Ps.',
        'qualifications':['Real-axis density/width bounds are infinite-volume continuum certificates, not finite boxes.',
            'Complex responses use eta=8 and are NOT on-shell self-energies or a computed eta->0 limit.',
            'Real-axis triple principal-value parts away from E=6 remain uncomputed; no off-center scattering probabilities are assigned.',
            'At E>=8 the chosen incoming pair channel has no finite-flux incidence, despite open triple outputs for E<12.',
            'Free orbital models and vertices are constructive choices, not physical photon/positron dynamics or a native coupling theorem.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (base_path,orb_path,combined_path,Path(__file__),BASE/'checkers/check_multiobject_orbital_selfenergy.py',BASE/'checkers/check_orbital_record_selfenergy.py',BASE/'checkers/check_multiobject_onband.py')}}
    (BASE/'results/multiobject_energy_response.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'offcenter_scalar3_density':[
        {'energy':r['energy'],'rho':r['refinements'][-1]['rho_scalar3']['decimal_view']} for r in density_reports],
        'complex_response_count':len(complex_reports),'threshold_table':threshold_table},indent=2))

if __name__=='__main__':main()

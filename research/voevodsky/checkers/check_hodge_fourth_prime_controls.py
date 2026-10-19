"""Bounded F41 tests of the two previously certified CRT representatives.

Forward arithmetic realization and one-way faithful-Hom specialization only.
No positive finite-field factor is a complex-axis construction.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse
import json
import subprocess
import tempfile
import os
from datetime import datetime,timezone
import check_hodge_scalar_37_census as previous
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,zd,bar,ints,require

ROOT=previous.ROOT
P=41
I=9
CONTROLS={-1554:4,3087:12}
COUNTER=ROOT/'research/voevodsky/checkers/count_hodge_fourth_prime_controls.rs'
COUNTS=ROOT/'research/voevodsky/inputs/hodge-fourth-prime-controls-v1/counts.json'
NOTE=ROOT/'research/voevodsky/hodge-fourth-prime-controls-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-fourth-prime-controls-v1.json'


def prime_divisors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out


def quotient_power(poly,exponent):
    n=len(poly)-1
    def mul(a,b):
        c=[0]*(2*n-1)
        for j,x in enumerate(a):
            for k,y in enumerate(b):c[j+k]=(c[j+k]+x*y)%P
        for j in range(2*n-2,n-1,-1):
            for k in range(n):c[j-n+k]=(c[j-n+k]-c[j]*poly[k])%P
        return tuple(c[:n])
    x=((-poly[0]%P,) if n==1 else (0,1)+(0,)*(n-2));v=(1,)+(0,)*(n-1)
    while exponent:
        if exponent%2:v=mul(v,x)
        x=mul(x,x);exponent//=2
    return v


def primitive_modulus(poly):
    n=len(poly)-1;q=P**n;one=(1,)+(0,)*(n-1)
    return quotient_power(poly,q-1)==one and all(quotient_power(poly,(q-1)//r)!=one for r in prime_divisors(q-1))


@lru_cache(maxsize=1)
def find_moduli():
    out=[]
    for n in range(1,6):
        choices=((c,1) for c in range(1,P)) if n==1 else ((c,k)+(0,)*(n-2)+(1,) for k in range(1,P) for c in range(1,P))
        out.append(next(poly for poly in choices if primitive_modulus(poly)))
    return tuple(out)


def elliptic_beta():
    count=1+sum(1+(0 if (h:=(x*x*x-x)%P)==0 else (1 if pow(h,(P-1)//2,P)==1 else -1)) for x in range(P))
    r=Q(P+1-count,2);require(r.denominator==1,'integral oriented Ei trace');r=int(r)
    choices=[(r,s) for s in range(-P,P+1) if r*r+s*s==P and (r+I*s)%P==0]
    require(len(choices)==1 and I*I%P==P-1,'unique oriented Ei Frobenius')
    return choices[0]


def orbit_counts(n):
    sizes=[0]*6
    for d in range(1,n+1):
        if n%d==0:sizes[d]=(P**d-sum(e*sizes[e] for e in range(1,d) if d%e==0))//d
    return sizes


@lru_cache(maxsize=1)
def run_counter():
    manifest=ROOT/'.ai/tmp/hodge-fourth-prime-controls-run.json';manifest.parent.mkdir(parents=True,exist_ok=True)
    now=lambda:datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory(prefix='hodge-fourth41-') as d:
        exe=Path(d)/'count.exe';build=['rustc','-O',str(COUNTER),'-o',str(exe)]
        subprocess.run(build,check=True,capture_output=True,text=True,timeout=120)
        paths=[COUNTER,COUNTER.with_name('count_hodge_minimal_axis_second_prime.rs'),Path(__file__)]
        state={'schema':'marici.hodge.counter-run.v1','build_command':build,'command':[str(exe)],
            'source_sha256':{str(p):sha256(p.read_bytes()).hexdigest() for p in paths},
            'executable_sha256':sha256(exe.read_bytes()).hexdigest(),'inputs':{'p':P,'a':[4,12],'lambda':2,'b':2,'i_mod_p':I},
            'parent_pid':os.getpid(),'started_at':now(),'output_path':str(COUNTS),'expected_rows':10,'status':'running'}
        child=subprocess.Popen([str(exe)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        state['child_pid']=child.pid;manifest.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
        try:
            stdout,stderr=child.communicate(timeout=900)
            state.update(exit_code=child.returncode,status='completed' if child.returncode==0 else 'failed')
            require(child.returncode==0,'fresh F41 counter failed: '+stderr[-2000:])
            data=json.loads(stdout);state['output_sha256']=sha256(stdout.encode()).hexdigest()
            return data
        except BaseException:
            if child.poll() is None:child.kill();child.communicate()
            state.update(exit_code=child.returncode,status='failed');raise
        finally:
            state['ended_at']=now();manifest.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')


def reconstruct(rows,a):
    beta=elliptic_beta();require(len(rows)==5 and [r['n'] for r in rows]==list(range(1,6)),'five F41 rows')
    moments=[]
    for n,r in enumerate(rows,1):
        q=P**n
        require(r['a']==a and r['q']==q and tuple(r['modulus'])==find_moduli()[n-1] and r['full_primitive_generator_cycle_verified'] is True,'F41 field coverage')
        require(r['Frobenius_x_orbit_counts_by_length']==orbit_counts(n),'F41 full orbit coverage')
        require(r['direct_ordinary_crosscheck'] is (n<5),'F41 direct crosscheck coverage')
        require(r['rational_poles']==(4 if n%2==0 else previous.joint.prime_poles(a,P)),'F41 a-dependent pole normalization')
        require(r['W']==r['E']==q+1-2*zp(beta,n)[0] and (r['V']-q-1)**2<=324*q,'F41 elliptic moments and Weil bound')
        if n<5:
            require(r['twisted_base']==r['W'] and r['twist_power_crosscheck'] is (n<=2) and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'F41 twisted coverage and power audits')
            moments.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(beta,n),-1)))
    ac=[(1,0)]
    for n in range(1,5):
        z=(0,0)
        for j in range(1,n+1):z=za(z,zm(ac[n-j],moments[j-1]))
        ac.append(zs(z,Q(-1,n)))
    require(ac[3]!=(0,0),'F41 nonzero a3')
    det=zd(zs(ac[4],P**3),bar(ac[3]));ac += [zs(zm(det,bar(ac[2])),Q(1,P**2)),zs(zm(det,bar(ac[1])),Q(1,P)),det]
    for j in range(8):require(ac[7-j]==zs(zm(ac[7],bar(ac[j])),Q(1,P**j)),'F41 Gaussian reciprocity')
    gauss=[ints(z) for z in ac]
    c=ints([sum(ac[j][0]*ac[k-j][0]+ac[j][1]*ac[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
    require(c[-1]==P**7 and all(c[14-j]==P**(7-j)*c[j] for j in range(8)),'F41 rational reciprocity')
    traces=[14]
    for n in range(1,6):traces.append(-sum(c[j]*traces[n-j] for j in range(1,n))-n*c[n])
    for n,r in enumerate(rows,1):require(traces[n]==r['W']+r['E']-r['V']-r['q']-1,'F41 unused fifth trace')
    return {'Gaussian_power_traces':[ints(z) for z in moments],'Gaussian_characteristic_coefficients_descending':gauss,
        'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':traces[1:]}


@lru_cache(maxsize=1)
def independent_counts():
    out={a:[] for a in CONTROLS.values()}
    for poly in find_moduli()[:2]:
        f=previous.arithmetic.Field(P,poly);points=[(x,y) for x in range(f.q) for y in range(f.q) if f.mul(y,y)==f.wp(x)]
        for a in out:
            v=len(f.roots(6))
            for x,y in points:
                g=previous.previous.base.ga(f,x,y,a);v+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
            out[a].append(v)
    f=previous.arithmetic.Field(P,find_moduli()[3]);points=[]
    for x in range(1,f.q):
        if f.pow(x,P)!=f.mul(2,f.inv(x)):continue
        for y in f.roots(f.wp(x)):
            if f.pow(y,P)==f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):points.append((x,y))
    require(len(points)==P+1-2*elliptic_beta()[0],'F41 independent torsor base')
    for a in out:
        fixed=0
        for x,y in points:
            g=previous.previous.base.ga(f,x,y,a)
            if g is None:fixed+=1;continue
            fixed+=sum(f.mul(I,f.pow(w,P))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
        out[a].append(fixed)
    return out


FALSE_CLAIMS=['finite_positive_factor_lifted_to_complex_axis','all41_residues_counted','old_CRT_classes_exhaust_complex_sources',
    'remaining_algebraic_or_dependent_parameters_excluded','primitive_theta6_axis_constructed','joint_axis_kernel_computed',
    'fixed_X6_identified','nonzero_target_cycle_constructed','Hodge_proved','Hodge_refuted','global_search_complete']


def verify_frozen_base():
    pins=json.loads((ROOT/'research/voevodsky/inputs/hodge-net-source-pins.v54.json').read_text(encoding='utf-8'))
    for name,digest in pins['source_sha256'].items():
        require(sha256((ROOT/name).read_bytes()).hexdigest()==digest,'frozen base source changed: '+name)
    return True


def report(data=None):
    verify_frozen_base()
    data=json.loads(COUNTS.read_text(encoding='utf-8')) if data is None else data
    require(data==run_counter(),'stale F41 counts')
    require((data['p'],data['lambda'],data['b'],data['i_mod_p'])==(P,2,2,I) and len(data['rows'])==10,'F41 bounded input identity')
    base=previous.report();require(base==json.loads(previous.OUT.read_text(encoding='utf-8')),'stale F37 predecessor')
    require(base['CRT_partition']['joint_survivors']==[3087,6623],'prior two necessary classes')
    small=independent_counts();results=[];negative=[]
    for lift,a in CONTROLS.items():
        require(lift%P==a and previous.joint.good_model(lift,P) and previous.joint.good_model(a,P,P-2),'F41 good source and negative-b charts')
        rows=[r for r in data['rows'] if r['a']==a];result=reconstruct(rows,a)
        require(small[a]==[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']],'F41 independent ordinary and direct twisted controls')
        cert=previous.arithmetic.cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']),elliptic_beta())
        m=cert['geometric_reduction_Ei_multiplicity_in_complement']
        if m==0:negative.append(a)
        results.append({'a_lift':lift,'a_mod41':a,**result,**cert,'screen_verdict':'CM_absent' if m==0 else 'necessary_CM_screen_survives'})
    paths=[Path(__file__),COUNTER,COUNTER.with_name('count_hodge_minimal_axis_second_prime.rs'),COUNTS,NOTE,previous.OUT,
        ROOT/'research/voevodsky/inputs/hodge-net-source-pins.v54.json']
    return {'schema':'marici.hodge-fourth-prime-controls-result.v1','passed':True,'base_net_iteration':51,'base_net_pins':'v54',
        'p':P,'i_mod_p':I,'beta':list(elliptic_beta()),'finite_field_cases':results,'negative_a_mod41':negative,
        'literal_controls_excluded':[r['a_lift'] for r in results if r['screen_verdict']=='CM_absent'],
        'algebraic_residue_boxes_excluded':[[2,a,b] for a in negative for b in (2,P-2)],
        'prediction_both_controls_CM_absent_survived':len(negative)==2,
        'checks':dict.fromkeys(['good_models','fresh_10_ordinary_8_twisted_rows','complete_primitive_field_cycles',
            'orbit_direct_and_twist_power_audits','independent_small_and_direct_twisted_counts','full_Gaussian_and_rational_polynomials',
            'unused_fifth_traces','complete55_order_CM_certificates','one_way_Hom_specialization_only'],True),
        **dict.fromkeys(FALSE_CLAIMS,False),'main_net_or_pins_modified':False,
        'verification_level':'Exhaustive bounded F41 counts and exact CM certificates; written injective good-specialization argument. Not proof-assistant certification.',
        'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--capture',action='store_true');parser.add_argument('--preflight',action='store_true');args=parser.parse_args()
    if args.preflight:
        print(json.dumps({'moduli':find_moduli(),'beta':elliptic_beta(),'good_models':{a:previous.joint.good_model(a,P) for a in CONTROLS}},indent=2))
    else:
        if args.capture:
            data=run_counter();COUNTS.parent.mkdir(parents=True,exist_ok=True);COUNTS.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
        r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))

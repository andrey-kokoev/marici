"""Finite-horizon, continuous piecewise-linear norming filters.

Bounded hat integrals replace point samples. Calibration uses exact Euler-line
moments and an L2 projection-residual bound, not a 10^-540 waveform approximation.
"""
from pathlib import Path
import runpy,json,math,hashlib
from fractions import Fraction
from flint import arb,acb,acb_series,arb_mat,ctx

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/grothendieck/results'
DEN=2**40;NDEN=10**12

def rat(pair):return arb(pair[0])/arb(pair[1])
def upper(x):return arb(x.upper())
def symmetric(radius):return arb(0).union(upper(radius)).union(-upper(radius))
def rational_upper(value):
    n=math.ceil(float(value.upper())*NDEN)+2
    assert arb(n)/NDEN>value
    return [str(n),str(NDEN)]
def signed_dyadic(value):return round(float(value.mid())*DEN)

def nodes_for(subdivisions):
    edges=[Fraction(0),Fraction(1,4096)]+[Fraction(2)**p for p in range(-11,7)]
    nodes=[edges[0]]
    for lo,hi in zip(edges,edges[1:]):
        nodes.extend(lo+(hi-lo)*Fraction(j,subdivisions) for j in range(1,subdivisions+1))
    assert nodes[-1]==64
    return nodes

def exp_integrals(rate,a,b):
    d=b-a;z=rate*d;e=(-z).exp();left=(-rate*a).exp()
    return left*(1-e)/rate,left*(1-(1+z)*e)/(d*rate*rate)

def fit_filters(bulk_squared_upper,subdivisions=4):
    ctx.prec=384;ctx.cap=2
    s=arb(7)/2;beta=arb(3)/2
    rates=[arb(2)**k for k in range(-3,11) if k!=1]
    def L(q):
        z=acb_series([acb(q),1],2).zeta()
        return (1/q+1/(q-1)-arb.pi().log()/2+(acb(q)/2).digamma()/2+z[1]/z[0]).real
    ls=L(s)
    gram=arb_mat([[1/(a+b) for b in rates] for a in rates])
    nodes=nodes_for(subdivisions)
    times=[arb(n.numerator)/n.denominator for n in nodes]
    filters=[];responses=[];diagnostics=[]
    for side in (0,1):
        moments=[]
        for rate in rates:
            q=beta+rate;lq=L(q)
            h=(-(ls+lq)/(s+q-1)+1/(s*(q-1))+1/((s-1)*q)) if side==0 else ((lq-ls)/(q-s)+1/((s-1)*(q-1))+1/(s*q))
            moments.append(-h)
        solution=gram.solve(arb_mat([[x] for x in moments]))
        coeffs=[arb(signed_dyadic(solution[j,0]))/DEN for j in range(len(rates))]
        avec=arb_mat([[a] for a in coeffs])
        square=(avec.transpose()*gram*avec)[0,0]
        correlation=sum(a*m for a,m in zip(coeffs,moments))
        values=[signed_dyadic(sum(a*(-r*t).exp() for a,r in zip(coeffs,rates))) for t in times]
        values[-1]=0
        norm=arb(0);cross=arb(0)
        for k,(lo,hi) in enumerate(zip(times,times[1:])):
            p=arb(values[k])/DEN;q=arb(values[k+1])/DEN
            norm+=(hi-lo)*(p*p+p*q+q*q)/3
            for a,r in zip(coeffs,rates):
                i0,i1=exp_integrals(r,lo,hi)
                cross+=a*(p*i0+(q-p)*i1)
        error_sq=square-2*cross+norm
        assert error_sq>0
        residual_sq_upper=upper(bulk_squared_upper[side]-2*correlation+square)
        assert residual_sq_upper>0
        uncertainty=(residual_sq_upper*upper(error_sq)).sqrt()
        # <g,b> = <g,k> + <k,b-k> + <g-k,b-k>.
        response=correlation+cross-square+symmetric(uncertainty)
        normalizer=rational_upper(norm.sqrt())
        assert norm/rat(normalizer)**2<1
        responses.append(response/rat(normalizer))
        filters.append({'nodal_numerators':values,'normalizer':normalizer})
        diagnostics.append({'projection_response':str(correlation/square.sqrt()),
                            'interpolation_L2_error':str(error_sq.sqrt()),
                            'source_response':str(responses[-1])})
    # Weak-coordinate filter. Its correlation is available exactly by elementary integrals.
    values=[signed_dyadic((-4*t).exp()) for t in times];values[-1]=0
    norm=arb(0);correlation=arb(0)
    for j,(lo,hi) in enumerate(zip(times,times[1:])):
        p=arb(values[j])/DEN;q=arb(values[j+1])/DEN
        norm+=(hi-lo)*(p*p+p*q+q*q)/3
        i0,i1=exp_integrals(arb(4),lo,hi)
        correlation+=p*i0+(q-p)*i1
    normalizer=rational_upper(norm.sqrt())
    assert norm/rat(normalizer)**2<1
    weak={'nodal_numerators':values,'normalizer':normalizer}
    weak_response=correlation/rat(normalizer)
    endpoint_square=arb(4)/25+arb(4)/49
    endpoint_normalizer=rational_upper(endpoint_square.sqrt())
    C=sum(responses)+endpoint_square/rat(endpoint_normalizer)+weak_response
    assert C>0 and weak_response>0
    return {'nodes':[[str(n.numerator),str(n.denominator)] for n in nodes],
            'nodal_denominator':DEN,'bulk':filters,'weak':weak,
            'endpoint_direction':[['2','5'],['2','7']],'endpoint_normalizer':endpoint_normalizer},C,weak_response,diagnostics

if __name__=='__main__':
    exact=runpy.run_path(str(Path(__file__).with_name('certify_exact_full_cubic_observer_norm.py')))
    # Obtain the actual bulk norm enclosures from the same fresh norm run.
    sq=[upper(exact['normcheck']['plus_sq']),upper(exact['normcheck']['minus_sq'])]
    filters,C,h,diagnostics=fit_filters(sq)
    ctx.prec=384
    def response(w):return arb(2).sqrt()*w['X']*(C+h*(w['mu']-exact['L']))
    Nx=64*response(exact['whole_first'])*response(exact['whole_second'])
    N0=response(exact['A1'])*response(exact['B1'])
    assert Nx>0 and N0>0
    gains=[exact['Sx']/Nx,exact['S0']/N0]
    rational_gains=[];balls=[]
    for value in gains:
        exponent=math.floor(float(abs(value).log()/arb(10).log()))-8
        numerator=round(float(value/(arb(10)**exponent)))*10**max(exponent,0)
        denominator=10**max(-exponent,0)
        rational_gains.append([str(numerator),str(denominator)])
        balls.append(arb(numerator)/denominator)
    kx,k0=balls
    assert abs(gains[0])>abs(gains[1]) and abs(kx)>abs(k0)
    dx=abs(kx*Nx-exact['Sx']);d0=abs(k0*N0-exact['S0'])
    exact_ratio=abs(gains[0])/exact['optimal']
    rational_ratio=abs(kx)/exact['optimal']
    assert exact_ratio<arb('1.04') and rational_ratio<arb('1.03')
    assert d0<arb('0.00036') and dx<arb('0.00076')
    margin=exact['S0']-d0-abs(kx)*arb('1e-540')
    assert margin>arb('0.05')
    rows=[{'shape':shape,'sign':sign,'coefficient':'crossed'} for shape,sign in exact['J'].items()]
    shape,sign,_=exact['reserve'];rows.append({'shape':shape,'sign':sign,'coefficient':'positive'})
    assert len(rows)==449
    manifest={'schema':'marici.grothendieck.time-bin-cubic-observer.v1',
              'filters':filters,'coefficients_per_w_squared':dict(zip(('crossed','positive'),rational_gains)),
              'rows':rows,'horizon':64,'bins':len(filters['nodes'])-1,
              'input_contract':'Bounded integrals of exp(-u)*f(u) against continuous nodal hat functions. Last nodal coefficient is zero and need not be acquired. Two weak fields use the same weak filter. Negative fields are reflected to u>=0. Ordered tensor blocks require joint filters or certified finite-rank decompositions, not products of marginal readings.',
              'precision_bits':2048}
    path=OUT/'time-bin-cubic-observer.json'
    path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    certificate={'schema':'marici.grothendieck.time-bin-cubic-observer-certificate.v1','passed':True,
                 'manifest_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                 'horizon':64,'bins':manifest['bins'],'shape_blocks':449,
                 'certified_claims':{'exact_recalibration_within_factor_1_04_of_optimum':True,
                                     'rational_gain_norm_upper_within_factor_1_03':True,
                                     'positive_calibration_error_below_0_00036':True,
                                     'crossed_calibration_error_below_0_00076':True,
                                     'source_columns_audited':len(exact['columns'])},
                 'bulk_fit_diagnostics':diagnostics,
                 'rigorous_balls':{k:str(v) for k,v in {
                     'C_bin':C,'weak_response':h,'exact_recalibrated_norm_upper_to_optimum':exact_ratio,
                     'rational_norm_upper_to_optimum':rational_ratio,'operator_norm_upper_per_w_squared':abs(kx),
                     'positive_calibration_error':d0,'crossed_calibration_error':dx,
                     'margin_at_total_response_noise_1e_minus540':margin}.items()},
                 'scope':'Finite-horizon graph-test implementation with bounded hat-integral acquisition. Exact recalibration is feasible on all 270 columns; rational gains have the stated two-coordinate defects. Physical measurement accuracy is an external requirement, not fabricated data.'}
    (OUT/'time-bin-cubic-observer-certificate.json').write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(certificate,indent=2))

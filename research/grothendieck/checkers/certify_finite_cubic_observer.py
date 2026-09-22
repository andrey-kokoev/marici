"""Build dyadic finite-frequency filters and certify the 449-block observer."""
from pathlib import Path
import runpy,json,gzip,math,hashlib
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[3]
DEN=2**40
cells=[];squared=[arb(0),arb(0)];correlation=[arb(0),arb(0)]
def visit(j,rate,pp,mp):
    row=[j,rate]
    for k,target in enumerate((-pp,-mp)):
        # Both actual bulk labels are minus the unsubtracted Tate response.
        nr=round(float(target.real.mid())*DEN)
        ni=round(float(target.imag.mid())*DEN)
        r=acb(arb(nr)/DEN,arb(ni)/DEN)
        squared[k]+=(r.real**2+r.imag**2)/(rate*arb.pi())
        correlation[k]+=(r.conjugate()*target).real/(rate*arb.pi())
        row.extend([nr,ni])
    cells.append(row)

exact=runpy.run_path(str(Path(__file__).with_name('certify_exact_full_cubic_observer_norm.py')),
                    init_globals={'CELL_VISITOR':visit})
ctx.prec=192
NDEN=10**12
normalizers=[]
for square in squared:
    n=math.ceil(float(square.sqrt().upper())*NDEN)+2
    normalizers.append(n)
    assert arb(n)/NDEN>square.sqrt()
S=arb(7)/2
endpoint_square=1/S**2+1/(S-1)**2
endpoint_n=math.ceil(float(endpoint_square.sqrt().upper())*NDEN)+2
assert arb(endpoint_n)/NDEN>endpoint_square.sqrt()
weak_n=2828427;weak_den=1000000
weak=arb(weak_n)/weak_den
assert weak/(arb(8).sqrt())<1
h_effective=weak/8
C_effective=sum(correlation[k]/(arb(normalizers[k])/NDEN) for k in range(2))
C_effective+=endpoint_square/(arb(endpoint_n)/NDEN)+h_effective
assert C_effective>0
L=exact['L']
def measured(w):
    return arb(2).sqrt()*w['X']*(C_effective+h_effective*(w['mu']-L))
Nx=64*measured(exact['whole_first'])*measured(exact['whole_second'])
N0=measured(exact['A1'])*measured(exact['B1'])

def calibrate(value):
    exponent=math.floor(float(abs(value).log()/arb(10).log()))-8
    mantissa=round(float(value/(arb(10)**exponent)))
    numerator=mantissa*10**max(exponent,0)
    denominator=10**max(-exponent,0)
    return arb(numerator)/denominator,[str(numerator),str(denominator)]

kx,rx=calibrate(exact['Sx']/Nx)
k0,r0=calibrate(exact['S0']/N0)
assert abs(kx)>abs(k0)
dx=abs(kx*Nx-exact['Sx']);d0=abs(k0*N0-exact['S0'])
assert dx<arb('0.00147') and d0<arb('0.000702')
ratio=abs(kx)/exact['optimal']
exact_filter_ratio=(abs(exact['Sx'])/Nx)/exact['optimal']
assert ratio<arb('1.03')
assert exact_filter_ratio<arb('1.05')
noise=arb('1e-540')
margin=exact['S0']-d0-abs(kx)*noise
assert margin>arb('0.05')

outdir=ROOT/'research/grothendieck/results'
filter_path=outdir/'finite-cubic-filter-cells.json.gz'
payload=json.dumps({'dyadic_denominator':DEN,'cells':cells},separators=(',',':')).encode()
filter_path.write_bytes(gzip.compress(payload,mtime=0))
rows=[]
for shape,sign in exact['J'].items():
    rows.append({'shape':shape,'sign':sign,'coefficient':'crossed'})
shape,sign,_=exact['reserve']
rows.append({'shape':shape,'sign':sign,'coefficient':'positive'})
assert len(rows)==449
manifest={'schema':'marici.grothendieck.finite-cubic-observer.v1',
          'coefficients_per_w_squared':{'crossed':rx,'positive':r0},
          'bulk_normalizers':[[str(n),str(NDEN)] for n in normalizers],
          'endpoint_normalizer':[str(endpoint_n),str(NDEN)],
          'endpoint_direction':[['2','5'],['2','7']],
          'weak_multiplier':[str(weak_n),str(weak_den)],
          'cell_file':filter_path.name,'cell_file_sha256':hashlib.sha256(filter_path.read_bytes()).hexdigest(),
          'positive_frequency_cells':len(cells),'rows':rows,
          'input_contract':'Bulk entries are integrals of the Fourier transform of exp(-u)*f(u) over EACH positive and negative cell, independently, with no 2pi normalization. Negative-side fields are reflected to u>0. Weak entries are integrals exp(-5u)*f(u)du. Ordered tensor records require joint theta_tensor_theta measurements or finite-rank decompositions, not products of marginals.',
          'variance':'linear; conjugate final value for original conjugate-linear convention'}
(outdir/'finite-cubic-observer.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
result={'schema':'marici.grothendieck.finite-cubic-observer-certificate.v1','passed':True,
        'positive_frequency_cells':len(cells),'measured_shape_blocks':len(rows),
        'rigorous_balls':{k:str(v) for k,v in {
            'finite_test_even_response':C_effective,'finite_test_residual_response':h_effective,
            'operator_norm_upper_per_w_squared':abs(kx),'upper_to_optimal_norm_ratio':ratio,
            'exactly_recalibrated_filter_to_optimal_norm_ratio':exact_filter_ratio,
            'positive_basis_calibration_error':d0,'crossed_basis_calibration_error':dx,
            'noise_budget':noise,'positive_margin_after_calibration_and_noise':margin}.items()},
        'claims':{'one_feature_test_norm_at_most_one':True,
                  'all_268_zero_source_values_exactly_preserved':True,
                  'operator_norm_upper_below_1_03_times_optimum':True,
                  'exactly_recalibrated_finite_filter_below_1_05_times_optimum':True,
                  'positive_margin_exceeds_0_05_w_squared_at_noise_1e_minus540':True},
        'scope':'Finite rational filter and calibration. Acquisition must supply the declared bounded integral measurements with its error budget; no point-sampling or physical acquisition certificate is inferred.'}
(outdir/'finite-cubic-observer-certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

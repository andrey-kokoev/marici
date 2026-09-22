"""Eight private rows per visible basis: exact support and Arb norm gain.

This optimizes the fixed residual test on these sixteen rows, NOT all tests
on the entire response carrier.
"""
from pathlib import Path
from collections import defaultdict
from math import floor
import runpy,json
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
f=g['f'];columns=[];formal_rows=defaultdict(dict)
for pairs in g['pairings'](tuple(range(6))):
    for kinds in ((1,1,0),(1,0,1),(0,1,1)):
        start=0;ds=[]
        for pair,kind in zip(pairs,kinds):
            ds.append(g['one'](f['derivative'](start,f['relation'](pair,kind))))
            start|=sum(1<<j for j in pair)
        image=g['join'](g['join'](ds[0],ds[1]),ds[2])
        j=len(columns);columns.append((pairs,kinds))
        for row,c in image.items():formal_rows[row][j]=c
assert len(columns)==270
# A private residual-test pivot for EVERY source basis column: choose the
# first seam of each two-event block, and retain each mixed block's feature.
for j,(pairs,kinds) in enumerate(columns):
    start=0;seams=[]
    for pair,kind in zip(pairs,kinds):
        seams.append(('e',start,start|(1<<pair[0]),kind))
        start|=sum(1<<p for p in pair)
    pivot=(tuple(seams),((),(),(),()))
    assert formal_rows[pivot]=={j:1}
families=[]
for target,first_pair,second_pair in [(0,(0,1),(2,3)),(18,(0,2),(1,3))]:
    start2=sum(1<<p for p in first_pair)
    family=[]
    for p in first_pair:
        for q in second_pair:
            for last in (4,5):
                row=((('e',0,1<<p,1),('e',start2,start2|(1<<q),1),
                      ('e',15,15|(1<<last),0)),((),(),(),()))
                entries=formal_rows[row]
                assert set(entries)=={target} and abs(entries[target])==1
                family.append({'record':row,'source_sign':entries[target],
                               'first_prime_index':p,'second_prime_index':q})
    assert len(family)==8
    families.append(family)
# These are actual vacuum-buffer rows; no interpretation of potential-buffer
# keys as independent analytic measurement channels is made.

b=runpy.run_path(str(Path(__file__).with_name('certify_private_sector_cubic_noise.py')))
ctx.prec=192
old=b['b'];y=b['y'];gamma=b['gamma'];L=b['L'];h2=b['h2']
A1,A2,B1,B2=old['windows'];D=b['D'];window=old['window']
extra={(2,3):window(2,3,'early_A_prime3'),
       (2,5):window(2,5,'early_A_prime5'),
       (12,7):window(12,7,'early_B_prime7'),
       (20,7):window(20,7,'early_cross_prime7')}

def response(w):
    value=(2*h2).sqrt()*w['X']*(w['mu']-L)
    assert value>0
    return value

# Two forgotten-first seams for each of four retained-window pairs.
N0=2*(response(A1)+response(extra[2,3]))*(response(B1)+response(extra[12,7]))
Nx=2*(response(A1)+response(extra[2,5]))*(response(D)+response(extra[20,7]))
S0=b['S0'];Sx=b['Sx']
assert abs(Sx/Nx)>abs(S0/N0)
ideal_norm=abs(Sx/Nx)
old_ideal_norm=abs(Sx/b['Ex'])
gain=old_ideal_norm/ideal_norm
assert gain>arb('7.8')

def rational(value):
    sign=1 if value>0 else -1
    exponent=floor(float(abs(value).log()/arb(10).log()))
    numerator=round(float(abs(value)/(arb(10)**exponent))*1000000)
    result=sign*arb(numerator)/1000000*(arb(10)**exponent)
    return result,{'sign':sign,'mantissa_numerator':numerator,
                   'mantissa_denominator':1000000,'decimal_exponent':exponent}

k0,cal0=rational(S0/N0);kx,calx=rational(Sx/Nx)
assert abs(kx)>abs(k0)
norm=abs(kx)
assert b['operator_bound']/norm>arb('7.8')
d0=abs(k0*N0-S0);dx=abs(kx*Nx-Sx)
assert d0<arb('0.002') and dx<arb('0.002')
noise=arb('1e-542')
rho=b['rho']
cal_template=abs(k0*N0*rho-S0)
margin=k0*N0*rho-norm*noise-cal_template
assert margin>arb('0.05')

result={'schema':'marici.grothendieck.redundant-private-cubic-observer.v1','passed':True,
        'parameters':{'background_A':2,'spectral_y':3,'receiver_gamma':1,
                      'private_rows_per_visible_basis':8,'total_selected_rows':16,
                      'residual_test':'sqrt(8)*exp(-5*u)',
                      'independent_total_response_noise':'1e-542'},
        'source_audit':{'basis_products':270,'verified_private_correction_pivots':270,
                        'formal_record_keys':len(formal_rows),
                        'record_key_degrees':{str(d):sum(len(v)==d for v in formal_rows.values()) for d in (1,2)},
                        'private_row_families':families},
        'rational_coefficients_per_w_squared':{'positive_family':cal0,'crossed_family':calx},
        'rigorous_balls':{name:str(value) for name,value in {
            'positive_family_response_sum':N0,'crossed_family_response_sum':Nx,
            'ideal_restricted_observer_norm':ideal_norm,
            'gain_over_one_row_per_basis_ideal_test':gain,
            'rational_observer_norm':norm,
            'gain_over_previous_rational_test':b['operator_bound']/norm,
            'positive_calibration_error':d0,'crossed_calibration_error':dx,
            'noise_error_per_w_squared':norm*noise,
            'remaining_margin_after_template_calibration_and_noise':margin}.items()},
        'certified_claims':{'same_functional_on_all_270_basis_products_for_ideal_coefficients':True,
                            'norm_improvement_exceeds_7_8_in_same_response_norm':True,
                            'remaining_margin_exceeds_0_05_w_seam_squared':True},
        'scope':'Exact optimum within the fixed residual-coordinate test family on sixteen proved-private rows. This is a feasible upper bound for full-output optimization, not a certified full-output optimum. Formal potential-buffer record counts are not treated as independent analytic measurement coordinates.'}
out=ROOT/'research/grothendieck/results/redundant-private-cubic-observer.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

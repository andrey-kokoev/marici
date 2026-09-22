"""Exact all-column norming certificate, with an Arb enclosure of its norm.

The numerical LP is discovery only. Feasibility is proved by matching identical
actual feature windows in true analytical shape blocks.
"""
from pathlib import Path
from collections import defaultdict,Counter,deque
import runpy,json
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
audit=runpy.run_path(str(Path(__file__).with_name('audit_cubic_analytical_shapes.py')))
columns=audit['columns'];rows=audit['shape_rows'];target=18
support={shape for shape,sign,windows in columns[target]['entries']}
J={shape:sign for shape,sign,windows in columns[target]['entries']}
# Reserve a genuinely private A1,B1 row for the small positive source value.
reserve=None
for shape,sign,windows in columns[0]['entries']:
    if len(rows[shape])==1 and windows==((0,1),(3,7)):
        reserve=(shape,sign,windows);break
assert reserve is not None and reserve[0] not in support
matches=[]
for j,column in enumerate(columns):
    if j==target:continue
    private=defaultdict(deque)
    for shape,sign,windows in column['entries']:
        if len(rows[shape])==1 and shape!=reserve[0]:
            private[windows].append((shape,sign))
    for shape,sign,windows in column['entries']:
        if shape not in support:continue
        assert private[windows],(j,windows)
        replacement,replacement_sign=private[windows].popleft()
        assert replacement not in J
        J[replacement]=-J[shape]*sign*replacement_sign
        matches.append({'column':j,'shared_shape':shape,'private_shape':replacement,
                        'ordered_windows':windows,'correction_sign':J[replacement]})
# Exact polynomial verification: each variable is an ordered actual window pair.
for j,column in enumerate(columns):
    value=Counter()
    for shape,sign,windows in column['entries']:
        value[windows]+=J.get(shape,0)*sign
    value={w:c for w,c in value.items() if c}
    if j==target:
        assert len(value)==16 and set(value.values())=={16}
    else:assert not value,(j,value)
assert set(J.values())=={-1,1} and reserve[0] not in J

normcheck=runpy.run_path(str(Path(__file__).with_name('certify_even_response_norm.py')),
                       init_globals={'CELL_VISITOR':globals().get('CELL_VISITOR')})
C=normcheck['C'];assert C>arb('1.96') and C<arb('2.04')
b=runpy.run_path(str(Path(__file__).with_name('certify_private_sector_cubic_noise.py')))
ctx.prec=192
old=b['b'];y=b['y'];gamma=b['gamma'];L=b['L'];h=(1/(2*(y+gamma))).sqrt()
A1,A2,B1,B2=old['windows']
# These are unions of existing consecutive windows, not new event generators.
whole_first=old['window'](2,10,'union_2_to_20')
whole_second=old['window'](20,21,'union_20_to_420')
assert arb(2).log()*(y*arb(2).log()).tanh()>L

def response_norm(w):
    assert w['mu']-L>0
    return arb(2).sqrt()*w['X']*(C+h*(w['mu']-L))

# Exact norm: 256 distinct shape terms and positivity of the common norming test.
N=64*response_norm(whole_first)*response_norm(whole_second)
reserve_norm=response_norm(A1)*response_norm(B1)
S0=b['S0'];Sx=b['Sx']
optimal=abs(Sx)/N
small=S0/reserve_norm
assert small<optimal
assert small/optimal<arb('1e-340')
lo=arb(optimal.lower());hi=arb(optimal.upper())
assert lo>0 and hi/lo<arb('1.033')
assert optimal>arb('3.369e537') and optimal<arb('3.480e537')
old_gain=b['operator_bound']/optimal
assert old_gain>arb(1900)

structure={'schema':'marici.grothendieck.exact-cubic-norming-rows.v1',
           'crossed_source_column':target,'base_shape_count':len(support),
           'correcting_private_rows':matches,'reserved_positive_shape':reserve,
           'interpretation':'On each listed analytical shape apply the SAME unit simultaneous norming test theta tensor theta, with the listed sign. The exact observer is (Sx/N)*J+(S0/reserve_norm)*R0. Physical w_seam^2 multiplies it.'}
structure_path=ROOT/'research/grothendieck/results/exact-cubic-norming-rows.json'
structure_path.write_text(json.dumps(structure,indent=2)+'\n',encoding='utf-8')
result={'schema':'marici.grothendieck.exact-full-cubic-observer-norm.v1','passed':True,
        'parameters':{'background_A':2,'y':3,'gamma':1,
                      'carrier':'same unscaled l1 sum of actual analytical seam/memory shape blocks'},
        'exact_source_checks':{'columns':270,'analytical_shapes':len(rows),
                               'normed_crossed_shapes':len(support),'private_corrections':len(matches),
                               'observer_support_before_reserved_row':len(J),
                               'same_window_cancellation_on_every_other_column':True},
        'exact_formula_per_w_squared':'abs(Sx)/(64*N([2,20])*N([20,420]))',
        'rigorous_balls':{name:str(value) for name,value in {
            'C_even':C,'crossed_source_full_response_norm':N,
            'reserved_positive_row_norm':reserve_norm,
            'full_optimal_observer_norm_per_w_squared':optimal,
            'certified_lower_endpoint':lo,'certified_upper_endpoint':hi,
            'enclosure_ratio':hi/lo,'positive_row_coefficient':small,
            'positive_row_to_optimum_ratio':small/optimal,
            'gain_over_previous_two_private_row_rational_observer':old_gain}.items()},
        'certified_claims':{'exact_full_carrier_optimum_attained_by_continuous_tests':True,
                            'optimal_norm_between_3_369e537_and_3_480e537_per_w_squared':True,
                            'upper_lower_enclosure_ratio_below_1_033':True,
                            'same_source_functional_on_all_270_basis_products':True},
        'source_norming_artifact':str(structure_path.relative_to(ROOT)).replace('\\','/'),
        'scope':'Exact optimization in the stated continuous-response dual at this fixed background and spectral point. Simultaneous norming tests are defined analytically; no finite numerical implementation or noise experiment for those tests is certified.'}
out=ROOT/'research/grothendieck/results/exact-full-cubic-observer-norm.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

"""Audit supplied amplitudes and a finite same-mean/same-cost hostile.

This does not derive a physical kinetic cost: Frobenius cost is only a declared
control showing that one scalar constraint need not select the response.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/response-amplitude-source-gate.json'
out.unlink(missing_ok=True)
fixture=Path(__file__).with_name('check_shared_leg_dg_realization.py')
with redirect_stdout(io.StringIO()): m=runpy.run_path(str(fixture))
I,H,K,Z=(m[k] for k in ('I','H','K','Z'))
add,scale,mul=(m[k] for k in ('add','scale','mul'))
d=m['values']['d']
source=fixture.read_text(encoding='utf-8')
assert "F(i,3),H" in source and "F(j,5),K" in source
series=(ROOT/'research/nima/agda/RetainedComparisonSeries.agda').read_text(encoding='utf-8')
assert 'coefficient f zero v = v' in series
assert 'coefficient f (suc n) v = pull f (coefficient f n v)' in series
assert 'pull f v x = v (equivFun (fst f) x)' in series

def sub(a,b): return add(a,scale(-1,b))
def total(xs):
    out=Z
    for x in xs: out=add(out,x)
    return out

def determinant(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def rectangular(values,i,j):
    return sub(add(values[11*i+j],values[0]),add(values[11*i],values[j]))

def data(alpha,beta):
    # Actual shared-leg topology; centered nonzero shears, state sector held fixed.
    x=[add(I,scale(alpha*(i-5),H)) for i in range(11)]
    y=[add(I,scale(beta*(j-5),K)) for j in range(11)]
    assert all(determinant(a)==1 for a in x+y)
    values=[mul(b,a) for a in x for b in y]+[I]*16
    residuals=[sub(a,d) for a in values]
    assert all(determinant(a)==1 for a in values)
    for i in range(11):
        for j in range(11):
            assert rectangular(residuals,i,j)==scale(alpha*beta*i*j,mul(K,H))
    return values,residuals

positive,rp=data(F(1,3),F(1,5))
negative,rn=data(F(-1,3),F(1,5))
rescaled,rs=data(F(2,3),F(1,5))
for values,residuals in ((positive,rp),(negative,rn),(rescaled,rs)):
    assert len(values)==137
    assert scale(F(1,137),total(values))==I
    assert scale(F(1,137),total(residuals))==sub(I,d)
assert positive!=negative!=rescaled
assert rectangular(rp,1,1)==scale(-1,rectangular(rn,1,1))!=Z
assert rectangular(rs,1,1)==scale(2,rectangular(rp,1,1))

def cost(values): return sum((v*v for a in values for row in a for v in row),F(0))
assert cost(rp)==cost(rn)
assert cost(rs)!=cost(rp)
# This is not merely a common passive frame change: normalized loop traces
# are conjugacy invariants when the reference is transported with the maps.
r=scale(F(1,2),I)
trace=lambda a:a[0][0]+a[1][1]
assert trace(mul(r,positive[0]))==F(11,6)
assert trace(mul(r,negative[0]))==F(1,6)
# Source witnesses and typed path relations are unchanged by evaluation choices.
_,delta,_,rectangles,routes=m['build']({'a':(0,0),'s':(0,0)})
assert len(rectangles)==109
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        for j in range(size):
            first,second,filler=routes(tag,i,j)
            assert delta(first)==delta(second)
            assert delta(filler)==m['plus'](second,m['minus'](first))

# The source swap transports a supplied field; it does not prepare it.
swap=(0,2,1,3)
pull=lambda v:tuple(v[swap[i]] for i in range(4))
v=(F(1),F(2),F(3),F(4))
assert pull((F(0),)*4)==(F(0),)*4
assert pull(tuple(2*x for x in v))==tuple(2*x for x in pull(v))
assert pull(pull(v))==v

result={
 'status':'passed',
 'classification':'response_amplitudes_are_supplied_and_not_selected_by_reference_witness_or_mean',
 'obligation':'source amplitude preparation before physical scalar readout',
 'stratum':'Actual shared-leg topology and reference, centered rational shear evaluations with determinant-one legs; unchanged formal witnesses',
 'checks':{'fixture_coefficients_explicitly_assigned':True,
           'comparison_series_seed_explicit':True,'slots':137,'mixed_relations':109,
           'same_reference_and_mean':True,'same_scalar_cost_opposite_mixed_response':True,
           'nonzero_mixed_response_rescaling':True,'all_leg_determinants_one':True,
           'normalized_trace_separates_passive_frame_orbits':True},
 'control_cost':str(cost(rp)),
 'verdict':'Transport and retained comparison data do not determine the supplied amplitude preparation. Equal mean and a declared scalar cost do not select even the sign of a mixed response.',
 'unsupported':['derivation of the fixture coefficients from source physics',
                'physical status of the Frobenius cost',
                'identification with the separate scalar scattering benchmark'],
 'next_constructor':'Supply an amplitude preparation/evolution law and its witness-dependent action, or keep the matrix assignments explicitly as test fixtures.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

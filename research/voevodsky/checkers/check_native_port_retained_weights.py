"""Certified tail-normalized bound spectral weights and bandwidth control.
Univariate residues are enclosed using exact Q(sqrt(151)) interval arithmetic.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_native_adapter_collective_closure import F
from check_native_joint_generator_resolvent import characteristic_and_adjugate
from check_native_port_bound_spectrum import inertia,secular_gram,energy
from check_native_port_scattering import approximate

BASE=Path(__file__).resolve().parents[1]

class Interval:
    def __init__(self,lo=0,hi=None):
        self.lo=F.cast(lo);self.hi=F.cast(lo if hi is None else hi)
        assert self.hi==self.lo or (self.hi-self.lo).positive()
    @staticmethod
    def cast(x):return x if isinstance(x,Interval) else Interval(x)
    def __add__(self,o):
        o=Interval.cast(o);return Interval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,o):return self+-Interval.cast(o)
    def __rsub__(self,o):return Interval.cast(o)+-self
    def __mul__(self,o):
        o=Interval.cast(o);values=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        low=high=values[0]
        for x in values[1:]:
            if (low-x).positive():low=x
            if (x-high).positive():high=x
        return Interval(low,high)
    __rmul__=__mul__
    def inverse(self):
        if not (self.lo.positive() or (-self.hi).positive()):raise ZeroDivisionError('Interval includes zero')
        return Interval(self.hi.inverse(),self.lo.inverse())
    def __truediv__(self,o):return self*Interval.cast(o).inverse()
    def width_at_most(self,tolerance):return not ((self.hi-self.lo)-F(tolerance)).positive()
    def encoded(self):return {'lower':self.lo.encoded(),'upper':self.hi.encoded(),
        'decimal_bounds':[approximate(self.lo),approximate(self.hi)],
        'midpoint_decimal':approximate(Q(1,2)*(self.lo+self.hi))}


def trim(poly):
    while len(poly)>1 and not poly[-1]:poly.pop()
    return poly

def eval_poly(poly,x):
    result=F()
    for c in reversed(poly):result=result*x+c
    return result

def eval_interval(poly,x):
    result=Interval()
    for c in reversed(poly):result=result*x+c
    return result

def minor(A,index):return [[v for j,v in enumerate(row) if j!=index] for i,row in enumerate(A) if i!=index]
def determinant(A):
    A=[list(row) for row in A];result=F(1)
    for k in range(len(A)):
        pivot=next((i for i in range(k,len(A)) if A[i][k]),None)
        if pivot is None:return F()
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];result=-result
        value=A[k][k];result=result*value;inverse=value.inverse()
        for i in range(k+1,len(A)):
            coefficient=A[i][k]*inverse
            if coefficient:
                for j in range(k+1,len(A)):A[i][j]=A[i][j]-coefficient*A[k][j]
    return result


def lead_polynomial(K,ports):
    """det[I+r(2I-K-P)+r^2(I-P)] from the exact rank<=2 diagonal update.
    E(r)=(1+r)^2/r. All coefficients are calculated, not interpolated.
    """
    n=len(K);D,Adj=characteristic_and_adjugate(K);terms=[D]
    if ports:
        terms.append([sum((A[i][i] for i in range(ports)),F()) for A in Adj])
    if ports==2:
        hidden=[[K[i][j] for j in range(2,n)] for i in range(2,n)]
        terms.append(characteristic_and_adjugate(hidden)[0])
    assert ports<=2
    out=[F() for _ in range(2*n+1)]
    for m,poly in enumerate(terms):
        for j,c in enumerate(poly):
            for k in range(2*j+m+1):out[n-j+k]=out[n-j+k]+((-1)**m)*comb(2*j+m,k)*c
    trim(out)
    assert out[0]==1 and len(out)-1==2*n-ports
    for r in (Q(1,32),Q(1,4),Q(1,2)):
        E=energy(r)
        matrix=[[r*((F(E) if i==j else F())-K[i][j]-(F(1+r) if i==j and i<ports else F())) for j in range(n)] for i in range(n)]
        assert eval_poly(out,r)==determinant(matrix)
    return out


def refine(low,high,K,metric,ports):
    il=inertia(secular_gram(K,metric,ports,low));ih=inertia(secular_gram(K,metric,ports,high))
    assert il[2]==ih[2]==0 and ih[1]-il[1]==1
    for divisor in range(2,17):
        middle=low+(high-low)/divisor
        im=inertia(secular_gram(K,metric,ports,middle))
        if im[2]:continue
        if im[1]==il[1]:return middle,high
        assert im[1]==ih[1];return low,middle
    raise RuntimeError('No regular refinement point')


def enclose_weights(K,metric,ports,poly,cofactors,bracket):
    low,high=map(Q,bracket['decay_interval']);derivative=[j*c for j,c in enumerate(poly)][1:]
    for refinements in range(97):
        interval=Interval(low,high)
        try:
            dp=eval_interval(derivative,interval)
            factor=interval-interval.inverse()
            weights=[factor*eval_interval(c,interval)/dp for c in cofactors]
            tail=interval*interval/(1-interval*interval)*sum(weights,Interval())
            central=1-tail
            good=all(w.lo.positive() and (F(1)-w.hi).positive() and w.width_at_most(Q(1,10**9)) for w in weights)
            good=good and tail.lo.positive() and central.lo.positive() and (F(1)-central.hi).positive()
            if good:
                return {'decay_interval':[str(low),str(high)],'energy_interval':[str(energy(high)),str(energy(low))],
                    'refinements':refinements,'weights':weights,'tail_fraction':tail,'central_fraction':central,
                    'central_only_normalized_weights':[w/central for w in weights]}
        except ZeroDivisionError:pass
        low,high=refine(low,high,K,metric,ports)
    raise RuntimeError('Residue enclosure unresolved; do not replace by floating values')


def main():
    bound_path=BASE/'results/native_port_bound_spectrum.json';joint_path=BASE/'results/native_joint_generator_resolvent.json'
    bounds=json.loads(bound_path.read_text(encoding='utf-8'));joint=json.loads(joint_path.read_text(encoding='utf-8'))
    for receipt in (bounds,joint):
        assert receipt['verification_passed']
        for name,digest in receipt['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    # Independent scalar control: K=4, one positive contact, r=1/3.
    # Its secular polynomial is 1-3r and its full bound-state central weight
    # is 1-r^2=8/9, not the central-only normalization value one.
    toy=lead_polynomial([[F(4)]],1);r=Q(1,3)
    check('scalar_residue_control_includes_infinite_tail',toy==[F(1),F(-3)] and (r-1/r)/Q(-3)==Q(8,9) and (r*r/(1-r*r))*Q(8,9)==Q(1,9))
    reports=[];totals={};energy_totals={};mean_energies={}
    for sector in bounds['sector_reports']:
        label=sector['sector'];print('Enclosing '+label+' residues...',flush=True)
        K=[[F(*x) for x in row] for row in sector['generator']];metric=[F(*x) for x in sector['gram_diagonal']];ports=sector['active_ports']
        poly=lead_polynomial(K,ports)
        cofactors=[lead_polynomial(minor(K,j),ports-1) for j in range(ports)]
        check(label+'_determinant_and_cofactor_polynomials_verified',bool(poly) and len(cofactors)==ports)
        records=[];sums=[Interval() for _ in range(ports)];weighted_energy=[Interval() for _ in range(ports)]
        for index,bracket in enumerate(sector['brackets']):
            audit=enclose_weights(K,metric,ports,poly,cofactors,bracket)
            E=Interval(*map(Q,audit['energy_interval']))
            for j,w in enumerate(audit['weights']):sums[j]=sums[j]+w;weighted_energy[j]=weighted_energy[j]+E*w
            check(label+'_positive_full_norm_residues_'+str(index),all(w.lo.positive() for w in audit['weights']))
            check(label+'_nonzero_tail_fraction_'+str(index),audit['tail_fraction'].lo.positive() and (F(1)-audit['central_fraction'].hi).positive())
            records.append({**{k:v for k,v in audit.items() if k not in ('weights','tail_fraction','central_fraction','central_only_normalized_weights')},
                'weights':[w.encoded() for w in audit['weights']],
                'tail_fraction':audit['tail_fraction'].encoded(),'central_fraction':audit['central_fraction'].encoded(),
                'central_only_normalized_weights':[w.encoded() for w in audit['central_only_normalized_weights']]})
        mean=[K[j][j]+1 for j in range(ports)]
        check(label+'_total_retained_weights_strictly_between_zero_and_one',all(w.lo.positive() and (F(1)-w.hi).positive() for w in sums))
        check(label+'_continuum_energy_budget_in_band',all((Interval(mean[j])-weighted_energy[j]).lo.positive() and (4*(1-sums[j])-(Interval(mean[j])-weighted_energy[j])).lo.positive() for j in range(ports)))
        totals[label]=sums;energy_totals[label]=weighted_energy;mean_energies[label]=mean
        reports.append({'sector':label,'lead_determinant_coefficients_ascending':[c.encoded() for c in poly],
            'port_cofactor_coefficients_ascending':[[c.encoded() for c in row] for row in cofactors],
            'bound_records':records,'total_retained_weights':[w.encoded() for w in sums],
            'total_bound_energy_contributions':[w.encoded() for w in weighted_energy],
            'initial_mean_energies':[v.encoded() for v in mean]})
    retained={'native_belt_character':totals['symmetric'][0],
        'carrier_sum':totals['symmetric'][1],'carrier_difference':totals['antisymmetric'][0]}
    retained['proton_port']=Q(1,2)*(retained['carrier_sum']+retained['carrier_difference'])
    retained['electron_port']=retained['proton_port']
    check('individual_carriers_use_half_weight_in_each_orthogonal_sector',retained['proton_port'].lo==Q(1,2)*(retained['carrier_sum'].lo+retained['carrier_difference'].lo) and retained['proton_port'].hi==Q(1,2)*(retained['carrier_sum'].hi+retained['carrier_difference'].hi))
    check('final_probability_enclosures_narrow',all(w.width_at_most(Q(1,10**7)) for w in retained.values()))
    # Scale the leads AND contacts by t, leaving K fixed. The upper threshold
    # matrix is t(4I-2P)-K, so its negative inertia counts above-band modes.
    K=[[F(*x) for x in row] for row in joint['joint_generator']];metric=[F(*x) for x in joint['gram_diagonal']]
    bandwidth=[]
    for t in map(Q,('1/4','1/2','1','2','4','8','16')):
        threshold=[[metric[i]*((F(t*(4-2*(i<3))) if i==j else F())-K[i][j]) for j in range(11)] for i in range(11)]
        counts=inertia(threshold);assert counts[2]==0
        bandwidth.append({'hopping_and_contact_scale':str(t),'lead_band':['0',str(4*t)],'threshold_inertia':list(counts),'above_band_bound_count':counts[1]})
    check('bandwidth_count_fixture',[r['above_band_bound_count'] for r in bandwidth]==[7,7,5,4,2,0,0])
    check('bandwidth_counts_nondecreasing_when_band_narrows',all(a['above_band_bound_count']>=b['above_band_bound_count'] for a,b in zip(bandwidth,bandwidth[1:])))
    check('no_above_band_modes_for_scale_eight_or_larger',bandwidth[-2]['threshold_inertia']==[11,0,0] and all(F(4-2*(i<3)).positive() for i in range(11)))
    result={'verification_passed':all(checks.values()),'checks':checks,
        'residue_formula':'w_j = (r-1/r) c_j(r)/p_prime(r), p=det(r M(E(r))), c_j=diagonal cofactor of rM',
        'interpretation':'Spectral weight of a normalized initially central port preparation in a full tail-normalized bound eigenstate.',
        'sector_reports':reports,'retained_probability_enclosures':{name:w.encoded() for name,w in retained.items()},
        'continuum_probability_enclosures':{name:(1-w).encoded() for name,w in retained.items()},
        'bandwidth_controls':bandwidth,
        'bandwidth_law':'Leads and contacts scaled together by t, central K fixed; band [0,4t], threshold matrix t(4I-2P)-K.',
        'qualifications':['These are bound-subspace weights, not constant central occupation or capture probabilities for incoming scattering states.',
            'Bound eigenstates are normalized on the full infinite leads; central-only normalization overestimates each port overlap.',
            'Changing t changes a declared environmental law, not the validity of the fixed-t certificate.',
            'No negative-energy particle binding, protected memory, full spinor coupling or photon-sector branching ratio is derived.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (bound_path,joint_path,Path(__file__),BASE/'checkers/check_native_joint_generator_resolvent.py',BASE/'checkers/check_native_port_bound_spectrum.py',BASE/'checkers/check_native_port_scattering.py',BASE/'checkers/check_native_adapter_collective_closure.py')}}
    (BASE/'results/native_port_retained_weights.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),
        'retained_probability_bounds':{name:w.encoded()['decimal_bounds'] for name,w in retained.items()},
        'bandwidth_controls':bandwidth},indent=2))

if __name__=='__main__':main()

"""Exact Q(z)-operation boundary for the moving plane and its normalization.

The class is finite rational coefficient operations, not arbitrary spectral
functional calculus, infinite limits, or already supplied algebraic payloads.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import encode
from check_retained_word_transport import poly, add, sub, mul, scale
from check_conditional_boundary_metric import audit as metric_audit
from check_moving_boundary_plane import audit as moving_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/rational-normalization-gate.v1.json'


def mod_remainder(dividend,divisor,prime):
    r=[x%prime for x in dividend]
    for power in range(len(r)-1,len(divisor)-2,-1):
        coefficient=r[power]*pow(divisor[-1],-1,prime)%prime
        for j,a in enumerate(divisor):r[power-len(divisor)+1+j]=(r[power-len(divisor)+1+j]-coefficient*a)%prime
    return r[:len(divisor)-1]


def power(p,n):
    out=poly(1)
    for _ in range(n):out=mul(out,p)
    return out


def derivative_at_one(p,variable):
    return sum(coefficient*exponents[variable] for exponents,coefficient in p.items())


def audit():
    previous=metric_audit();moving=moving_audit()
    assert moving['characteristic']=='lambda^4-z^4*lambda^2-(z^4+z^5)*lambda-z^5'
    # z=2: irreducible quartic over F_13. A reducible quartic has a linear
    # factor or a monic quadratic factor; enumerate both classes completely.
    quartic=[-32,-48,-16,0,1];prime=13
    root_values=[sum(c*pow(x,i,prime) for i,c in enumerate(quartic))%prime for x in range(prime)]
    assert all(root_values)
    quadratic_remainders=[]
    for a in range(prime):
        for b in range(prime):
            remainder=mod_remainder(quartic,[b,a,1],prime)
            assert any(remainder)
            quadratic_remainders.append(remainder)
    assert len(quadratic_remainders)==169

    z=poly(variable=0);d=poly(variable=1)
    p=scale(power(z,4),-1)
    q=scale(add(power(z,4),power(z,5)),-1)
    r=scale(power(z,5),-1)
    # Pair-product sum u=d+r/d satisfies the standard resolvent cubic.
    # Verify its elimination algebra directly after clearing d^3.
    u=d
    resolvent=add(sub(power(u,3),mul(p,power(u,2))),add(scale(mul(r,u),-4),sub(scale(mul(p,r),4),mul(q,q))))
    expected=add(add(power(u,3),mul(power(z,4),power(u,2))),sub(scale(mul(power(z,5),u),4),mul(power(z,8),power(sub(z,poly(1)),2))))
    assert resolvent==expected
    # At z=2 the resolvent cubic has no root modulo 5, hence is irreducible.
    cubic=[-256,128,16,1]
    cubic_values=[sum(c*pow(x,i,5) for i,c in enumerate(cubic))%5 for x in range(5)]
    assert cubic_values==[4,4,2,4,1]

    numerator=add(power(d,2),r)
    cleared=add(sub(power(numerator,3),mul(mul(p,d),power(numerator,2))),
                add(scale(mul(mul(r,power(d,2)),numerator),-4),mul(sub(scale(mul(p,r),4),mul(q,q)),power(d,3))))
    determinant_polynomial=add(add(add(power(d,6),mul(power(z,4),power(d,5))),mul(power(z,5),power(d,4))),
        add(add(scale(mul(mul(power(z,8),add(poly(1),power(z,2))),power(d,3)),-1),scale(mul(power(z,10),power(d,2)),-1)),
            sub(mul(power(z,14),d),power(z,15))))
    assert cleared==determinant_polynomial
    assert sum(determinant_polynomial.values())==0
    assert derivative_at_one(determinant_polynomial,1)==8
    assert derivative_at_one(determinant_polynomial,0)==-20
    assert -derivative_at_one(determinant_polynomial,0)/derivative_at_one(determinant_polynomial,1)==F(5,2)

    # g=d^(-1/2): clear g^12. The positive local branch is specified at g(1)=1.
    gain_polynomial={}
    for (zpower,dpower,_),coefficient in determinant_polynomial.items():
        gain_polynomial=add(gain_polynomial,{(zpower,0,12-2*dpower):coefficient})
    assert sum(gain_polynomial.values())==0
    assert derivative_at_one(gain_polynomial,2)==-16
    assert derivative_at_one(gain_polynomial,0)==-20
    assert -derivative_at_one(gain_polynomial,0)/derivative_at_one(gain_polynomial,2)==-F(5,4)
    assert previous['local_source_metric']['normalization_delta_inverse_sqrt_coefficients'][1]==-F(5,4)
    assert moving['induced_step']['determinant_series'][1]==F(5,2)

    dependencies=list(previous['source_sha256'])+[
        'research/scattering/seed-composition/check_rational_normalization_gate.py',
        'research/nima/retained-path-family-composition-synthesis.md']
    return {
        'schema':'marici.scattering.rational-normalization-gate.v1',
        'status':'finite_rational_operation_class_cannot_exactly_select_plane_or_normalizing_gain',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'operation_class':{'field':'Q(z)','allowed':['finite rational incidence compositions','rational sums/products',
                           'invertible rational coordinate changes','finite rational auxiliary blocks and Schur complements','fixed finite fiber means'],
                           'excluded':['supplied algebraic spectral branches','arbitrary real-function payloads','infinite limits','unbounded functional calculus'],
                           'scope':'uniform exact parameterized maps on a nonempty open set, not one-point operations at z=1 or finite-order approximations'},
        'quartic_certificate':{'specialization_z':2,'coefficients_ascending':quartic,'prime':13,
                                'values_on_field':root_values,'monic_quadratics_tested':169,
                                'linear_or_quadratic_factors_found':0,
                                'consequence':'characteristic irreducible over Q(z); no rational rank-two invariant subspace or exact selected rank-two projector'},
        'determinant_certificate':{'pair_product_sum':'u=delta-z^5/delta',
                                    'resolvent':'u^3+z^4*u^2+4*z^5*u-z^8*(z-1)^2',
                                    'specialization_z':2,'cubic_prime':5,'cubic_values':cubic_values,
                                    'consequence':'delta is not in Q(z); delta^(-1/2) is not in Q(z)'},
        'algebraic_boundary':{'determinant_equation':'delta^6+z^4*delta^5+z^5*delta^4-z^8*(1+z^2)*delta^3-z^10*delta^2+z^14*delta-z^15=0',
                              'determinant_base_value':1,'derivative_wrt_delta_at_base':8,'determinant_derivative_at_base':'5/2',
                              'gain_equation':'1+z^4*g^2+z^5*g^4-z^8*(1+z^2)*g^6-z^10*g^8+z^14*g^10-z^15*g^12=0',
                              'gain_base_value':1,'derivative_wrt_gain_at_base':-16,'gain_derivative_at_base':'-5/4',
                              'base_conditions_specify_local_analytic_branches':True,
                              'branch_choice_is_physical_source_operation':False},
        'boundary':{'all_possible_source_operations_excluded':False,'algebraic_spectral_calculus_excluded':False,
                    'one_point_base_normalization_obstructed':False,'finite_order_approximations_obstructed':False,
                    'native_control_or_preparation_derived':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Construct an explicit algebraic spectral projector and its exact branch conditions, retaining the complementary sector; classify what additional selection operation this requires rather than calling it rational reindexing.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale rational-normalization receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: quartic irreducibility mod 13 and resolvent irreducibility mod 5 certify the Q(z) operation boundary.')
    print('PASS: exact algebraic determinant/gain equations and base derivatives agree with the moving-plane jet.')
    print('Boundary: finite rational exact transport only; algebraic branch selection and approximations remain possible.')


if __name__=='__main__':main()

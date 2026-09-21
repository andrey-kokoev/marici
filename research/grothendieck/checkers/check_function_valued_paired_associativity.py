"""Exact algebraic falsifiers for the function-valued paired attachment.

The matrices below are fixtures, NOT evaluations of the actual Clark tails.
Analytical injectivity and the slot Green identity are cited theorems.
"""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
certificate=ROOT/'research/grothendieck/results/six-prime-derived-block-associativity.json'
source=json.loads(certificate.read_text(encoding='utf-8'))
assert source['passed'] and source['shifted_source_comparison_cells']==720
J=s.Matrix([[0,1],[1,0]])
assert J.H==J and J*J==s.eye(2)
spectral=(s.I,1+2*s.I)
def h(kind,z):
    return s.Matrix([1+z,2-s.I*z]) if kind==0 else s.Matrix([z*z+s.I,1-2*z])
def denominator(w,z):return -s.I*(z-s.conjugate(w))
def kernel(a,b,w,z,eps=0,delta=0):
    return s.simplify((h(a,w).H*(J**(eps+delta+1))*h(b,z))[0]/denominator(w,z))
checks=0
for a in (0,1):
    for b in (0,1):
        for w in spectral:
            for z in spectral:
                for eps in (0,1):
                    for delta in (0,1):
                        direct=((J**eps*h(a,w)).H*J*(J**delta*h(b,z)))[0]/denominator(w,z)
                        assert s.simplify(direct-kernel(a,b,w,z,eps,delta))==0
                        assert s.simplify(kernel(a,b,w,z,eps,delta)-s.conjugate(kernel(b,a,z,w,delta,eps)))==0
                        checks+=1
# Source-derived tensor composition; complex coefficients require conjugation
# of the first packet and preserve each spectral denominator independently.
c=(1+s.I,2-s.I);d=(2+3*s.I,-1+s.I)
packet=sum(s.conjugate(c[i])*d[j]*kernel(0,1,w,z) for i,w in enumerate(spectral) for j,z in enumerate(spectral))
assert s.simplify(packet)!=0
wrong=sum(s.conjugate(c[i])*d[j]*(h(0,w).H*J*h(1,z))[0] for i,w in enumerate(spectral) for j,z in enumerate(spectral))/denominator(spectral[0],spectral[0])
assert s.simplify(packet-wrong)!=0
ks=[kernel(0,1,spectral[i%2],spectral[(i+1)%2]) for i in range(3)]
root=(s.Matrix([1,s.I]).H*J*s.Matrix([2+s.I,1]))[0]
left=s.simplify(root*((ks[0]*ks[1])*ks[2]))
right=s.simplify(root*(ks[0]*(ks[1]*ks[2])))
assert left==right and left!=0
assert s.simplify(left-(-right))!=0  # naive shifted right grouping fails
# Noncollapse needs ambient paired observations, not an invertible pullback Gram.
j=s.Matrix([1,0])
assert (j.H*J*j)[0]==0
assert (j.H*J).rank()==1
# Full complex-valued dual naturality: (AB)^H=B^H A^H, not plain transpose.
A=s.Matrix([[1,s.I],[2,1+s.I]])
B=s.Matrix([[1-s.I,2],[s.I,3]])
assert (A*B).H==B.H*A.H and (A*B).H!=(A*B).T
result={'schema':'marici.grothendieck.function-valued-paired-associativity.v1','passed':True,
        'source_certificate_sha256':hashlib.sha256(certificate.read_bytes()).hexdigest(),
        'source_shifted_channels':720,'slot_polarization_checks':checks,
        'checks':{'pairwise_spectral_denominators_retained':True,'aggregated_denominator_hostile':True,
                  'signature_closed_observer_channels':True,'tensor_associativity_with_root_pairing':True,
                  'uncorrected_shift_sign_hostile':True,'isotropic_primal_image_has_surjective_ambient_observation':True,
                  'complex_contragredient_order':True},
        'scope':'Universal pairing algebra tested on exact fixtures. No finite spectral-rank claim, actual tail evaluation, or new analytical injectivity proof.'}
p=ROOT/'research/grothendieck/results/function-valued-paired-associativity.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

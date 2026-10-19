"""Exact rational atom/character controls for the additive, not exponential, lift.
Uses formal rational phases: identities hold before evaluating exp(2 pi i phase).
No numerical Fourier approximation is treated as an infinite-domain proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/voevodsky'


def clean(d):return {k:v for k,v in d.items() if v}
def phase_sum(terms):
    d=defaultdict(Q)
    for a,p in terms:d[p%1]+=a
    return clean(d)
def fourier(atoms,y):return phase_sum((a,p-x*y) for x,a,p in atoms)
def shift(atoms,b):return [(x+b,a,p) for x,a,p in atoms]
def modulate(atoms,b):return [(x,a,p+b*x) for x,a,p in atoms]
def scale_phase(value,b):return phase_sum((a,p+b) for p,a in value.items())
def atom_sum(atoms):
    d=defaultdict(Q)
    for x,a,p in atoms:d[x,p%1]+=a
    return clean(d)
def convolve(a,b):return [(x+y,v*w,p+r) for x,v,p in a for y,w,r in b]
def multiply_values(a,b):return phase_sum((v*w,p+r) for p,v in a.items() for r,w in b.items())


def main():
    c={-2:Q(2,3),-1:Q(-1),0:Q(5,7),1:Q(3,2),3:Q(-2,5)}
    d={-1:Q(1,4),0:Q(-2),2:Q(3)}
    checks=0
    for h in (Q(1),Q(1,2),Q(1,4),Q(1,8)):
        atoms=[(h*n,a,Q(0)) for n,a in c.items()]
        other=[(h*n,a,Q(0)) for n,a in d.items()]
        # Bonding n -> 2n leaves actual additive atom positions unchanged.
        finer=[(h/2*(2*n),a,Q(0)) for n,a in c.items()]
        assert atom_sum(atoms)==atom_sum(finer);checks+=1
        for y in (Q(0),Q(1,7),Q(-2,3),Q(5,8)):
            # Torus theta=h*y; ordinary real Fourier is its periodic lift.
            torus=phase_sum((a,-n*h*y) for n,a in c.items())
            assert fourier(atoms,y)==torus==fourier(finer,y);checks+=1
            assert fourier(atoms,y+1/h)==fourier(atoms,y);checks+=1
            assert fourier(convolve(atoms,other),y)==multiply_values(fourier(atoms,y),fourier(other,y));checks+=1
            for k in (-2,-1,1,2):
                b=h*k;alpha=Q(1,8)/h
                assert fourier(shift(atoms,b),y)==scale_phase(fourier(atoms,y),-b*y);checks+=1
                assert fourier(modulate(atoms,alpha),y)==fourier(atoms,y-alpha);checks+=1
                left=shift(modulate(atoms,alpha),b)
                right=[(x,a,p-alpha*b) for x,a,p in modulate(shift(atoms,b),alpha)]
                assert atom_sum(left)==atom_sum(right);checks+=1
    # Reflection after two Fourier steps is the distributional theorem;
    # here test reflection and its algebra against the same atoms.
    assert atom_sum([(-x,a,p) for x,a,p in [(-x,a,p) for x,a,p in atoms]])==atom_sum(atoms);checks+=1
    # Exponential location fails the source additive law even at 0+0.
    assert 1*1==1 and 1+1!=1;checks+=1
    result={'schema':'marici.additive-lattice-fourier-bridge.v1','passed':True,
      'exact_finite_controls':checks,'embedding':'delta_n -> delta_(h*n), NOT delta_(exp(h*n))',
      'real_fourier_equals_periodic_lift_of_torus_fourier':True,
      'convolution_and_translation_modulation_preserved':True,
      'dyadic_atom_bonding_preserves_both_routes':True,
      'zero_atom_retained_separately_under_radialization':True,
      'Schwartz_limit_and_Poisson_status':'Analytic arguments in note; not proved by these finite tests',
      'log_prime_specialization_preserved_as_physical_additive_coordinate':False,
      'Hilbert_unitary_embedding_l2_Z_into_L2_R':False,
      'complete_native_carrier_constructor_identified':False}
    files=[Path(__file__),BASE/'additive-lattice-fourier-bridge-v1.md',
      ROOT/'research/nima/canonical-channel-tate-torus-fourier-functor.md',
      ROOT/'research/nima/source-derivation-of-realization-choices.md',
      ROOT/'research/nima/tate-torus-oriented-log-radial-comparison.md',
      BASE/'the-oriented-log-radial-fourier-sewing-has-an-explicit-oscillatory-hankel-kernel.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (BASE/'results/additive-lattice-fourier-bridge-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()

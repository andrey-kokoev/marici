# Generic six-modulus proof: all terms built, two quartics proved

Fresh execution reached the full generic chart, rather than another restricted family: first five twistors fixed to moment-curve frame values, Z6=(1,a,b,c), Z7=(1,d,e,f). The chart's six independent moduli were already certified by a nonzero invariant Jacobian.

`check_seven_point_generic_reduced_parity.py` constructed all six direct NNMHV and all six Fourier-transformed parity NMHV terms over Q(a,b,c,d,e,f). For every term it proved the two anti-supercharge row constraints symbolically. Direct matrices include the Q rows; dual matrices include the swapped Q rows and their Hodge complements obey the original Ward constraints. Thus generic membership in the universal three-dimensional Ward space is now established, not just sampled.

All12 signed rational weights and three pivot components are checkpointed in results/seven-point-generic-reduced-parity.json. Construction took about101 seconds. The180-second command then timed out simplifying the FIRST quartic with SymPy. Its passed=false status intentionally remains; this is a partial construction artifact, not a completed proof.

A separate exact rational backend in `check_seven_point_generic_quartics.py` uses FLINT multivariate polynomials, polynomial gcd reduction, and exact rational arithmetic (no floating point or interpolation). It proved quartics(0,0,0,0) and(0,0,0,1) identically zero in the full six-variable field. These are retained in results/seven-point-generic-quartics.json. That180-second run then timed out on subsequent work; passed=false remains correct.

Status: generic Ward membership and TWO of15 generic quartic parity identities are proved by these calculations. THIRTEEN remain unverified. Earlier complete one/two-parameter identities and exact rational full-tensor certificates are unaffected. Do not call this a generic full amplitude proof yet.

Next optimize denominator handling: cross-multiplying and gcd-reducing after every individual addition introduces avoidable huge intermediate polynomials. Retain factored denominators, form their least common multiple once per quartic, and sum polynomial numerators; cache repeated powers/monomials. Add source-digest-bound resumability so completed identities are not recomputed. This is an executable algebraic bottleneck, not an absence of mathematical continuation.

Commands: generic builder uses uv run --with sympy python; generic quartics additionally requires --with python-flint. Both checkpoints are intentionally partial after bounded timeouts.

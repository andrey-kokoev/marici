# Prime support is intrinsic to the output but inherited from the degree

Epistemic-graph event: 1374.

## Audit question

Does the norm complex derive prime loci from correspondence structure, or
does it merely restate the prime factorization of an integer degree already
present in the input?

For a regular fiber of cardinality `d>1`, Ledger 1348 gives

`H_d congruent (Z/d)^(d-2)`.

For `d>2`, its annihilator and support are

`Ann_Z(H_d)=dZ`,

`Supp_Z(H_d)=V(d)={ (p) : p divides d }`.

Thus the bad-prime set is intrinsic once `H_d` has been constructed: it can
be recovered without retaining a chosen factorization of `d`.  The primary
components also recover the exact valuations `v_p(d)`.

## Negative emergence result

This intrinsic recoverability is not yet an explanation of primes.  The
integer `d` already enters as the fiber cardinality and as the scalar in

`T^2=dT`.

Over `Z`, `T` is nonzero on a torsion-free module, so that scalar is unique.
The Smith reduction then deterministically repackages the already-present
`d`.  Moreover, after forgetting the induced group action, every two groups
of the same order give the same module `(Z/d)^(d-2)`.  The construction
factors through the cardinality map

`finite regular correspondence -> d in N -> H_d`.

Therefore the current norm homology recovers prime support intrinsically
from its output, but inherits the arithmetic source of that support from the
input degree.  It does not yet derive prime numbers from a prime-free
calculus.

The order-two exception is sharper: `H_2=0`, so the homology alone cannot
even recover its degree or the prime 2.  One must retain the operator relation
`T^2=2T` or the correspondence cardinality.

## Falsifier and next gate

The negative result would be overturned by a construction in which:

1. no integer degree or cardinality is supplied as arithmetic data;
2. indecomposable failure loci arise canonically from composition alone; and
3. those loci reproduce the prime ideals of `Z` presentation-independently.

Until such a construction exists, calling the present support an emergence
of primes overstates the evidence.  The next admissible target is narrower:
seek prime-power operations internal to composition and test whether they
contain information not determined by `d` alone.

## Scope

This audit concerns explanatory strength, not the validity of the Smith-form
theorem.  The algebraic support calculation remains exact.  No physical
relative-chain realization is asserted.

# Intrinsic prime formation and norm support are different mechanisms

Epistemic-graph event: 1378.

## Two typed constructions

The current program contains two distinct appearances of primes.

### Conditional pointed pi_0

Under the explicit monoidal-disjoint-union relaxation, the connected
generator `U` makes

`M=pi_0(Surf_U^sqcup)`

the free commutative monoid on one generator.  Its classifier by additive
endomorphisms gives a canonical multiplication, making `M` the initial
commutative semiring.  Irreducibility, divisibility, Euclid's lemma, and
unique factorization are then internal.  No degree map or external prime list
is used to define the prime elements.

This is a conditional but genuine prime-emergence theorem at decategorified
`pi_0`.  It does not lift to the full `D4`-resolved Carrier groupoid.

### Regular-fiber norm homology

For a correspondence whose regular fiber already has degree `d`, norm
homology is

`H_d=(Z/d)^(d-2)`.

Its support detects exactly the prime divisors of `d`, but the scalar `d` was
already present as fiber cardinality.  This mechanism is a prime detector,
not a prime generator.

## Conditional bridge

If a source-derived degree functor identifies a degree-`d` regular
correspondence with the conditional class `dU in M`, then the two mechanisms
agree:

`p divides d in M  iff  H_d localized at (p) is nonzero`, for `d>2`.

Thus norm support can serve as a torsion realization of prime divisibility
that was defined intrinsically in `M`.  The bridge is not automatic: it
requires the correspondence degree to be derived as the same additive
component class, rather than supplied by an unrelated cardinality lens.

The `d=2` exception persists: `H_2=0`, so norm homology is not a faithful
detector of all intrinsic primes.  The operator relation `T^2=2T` retains the
missing information, but the homology quotient does not.

## Verdict

The strongest supported statement is therefore

`intrinsic primes on conditional pi_0: yes;`

`prime emergence from norm homology alone: no;`

`norm support as a downstream detector of intrinsic divisibility: conditional.`

This reopens the long-horizon program at the correct type.  Frobenius must be
an operation attached functorially to intrinsic prime elements of `M`, not
scalar multiplication on `H_d`.

## Scope

No full-Carrier tensor, physical relative-chain pushforward, closed-point
geometry, Frobenius, or Euler product is obtained here.

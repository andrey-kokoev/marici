# Intrinsic primes generate a formal determinant Euler product

Epistemic-graph events: 1384; corrected claim notation superseded at 1385.

## Completed multiplicative monoid algebra

Let `M` be the conditional initial semiring and let `M_+` be its nonzero
multiplicative monoid.  Form the coefficientwise completion with basis
symbols `[a]`, `a in M_+`, and multiplication

`[a][b]=[ab]`.

Infinite sums are admitted when every basis coefficient is determined by
finitely many factorizations.  Unique factorization in `M` makes the Euler
product below coefficientwise well-defined.

## Local determinant factors

For each intrinsic prime element `p`, take the singleton identity inertia
object.  Its permutation representation is rank one with identity operator.
Weighting its formal variable by the intrinsic monoid class `[p]` gives

`L_p=det(1-[p] Id)^(-1)`

`=(1-[p])^(-1)=sum_(r>=0)[p^r]`.

No external list of primes is used: the index set is the internally defined
irreducible locus of `M`.

## Global formal Euler theorem

Unique factorization gives the coefficientwise identity

`product_(p intrinsic prime) (1-[p])^(-1)`

`=sum_(a in M_+) [a]`.

Indeed, the coefficient of `[a]` on the product side counts exponent vectors
in a prime factorization of `a`; existence and uniqueness make that
coefficient exactly one.

This is a genuine formal Euler product built from rank-one determinants and
intrinsically derived primes.  Unlike the norm-support construction, it does
not begin with a selected integer degree.

## Analytic evaluation boundary

After identifying the initial semiring by its universal property and choosing
the analytic character

`chi_s([a])=a^(-s)`, `Re(s)>1`,

the formal identity evaluates to

`product_p (1-p^(-s))^(-1)=sum_(a>=1)a^(-s)=zeta(s)`.

The Euler product in its half-plane of absolute convergence is therefore a
readout of the formal theorem.  But the analytic character, complex spectral
parameter, continuation beyond `Re(s)>1`, gamma factor, and functional
equation are not derived from the Carrier.  Consequently the formal product
does not yet define a global operator whose spectrum contains the nontrivial
zeros.

## Scope

The result is conditional on the pointed `pi_0` initial-semiring theorem.  It
does not lift to the full `D4` Carrier, authorize the `D4_ab` quotient
physically, or derive analytic continuation or a zero spectrum.

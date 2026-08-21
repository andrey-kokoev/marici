# The derived Euler realization stops in a zero-free domain

Epistemic-graph event: 1387.

## Analytic realization

Ledger 1360 constructs the intrinsic formal identity

`product_p (1-[p])^(-1)=sum_(a nonzero)[a]`.

For `s` with real part `sigma>1`, the character `[a] -> a^(-s)` is
absolutely summable.  Indeed,

`sum_p p^(-sigma) <= sum_(n>=2)n^(-sigma)<infinity`.

The logarithmic expansion of each local factor therefore converges
absolutely, and the product evaluates to a finite nonzero number:

`zeta(s)=product_p(1-p^(-s))^(-1) != 0`, for `Re(s)>1`.

Thus the entire analytic region presently justified by the intrinsic formal
Euler product is zero-free.

## Exact boundary of the spectral question

The nontrivial-zero question requires leaving the domain controlled by the
Euler product.  To do that canonically requires at least:

1. analytic continuation or a global determinant defined beyond absolute
   convergence;
2. the archimedean gamma factor;
3. a duality producing the functional equation; and
4. an operator or cohomology whose determinant realizes the completion.

None follows from unique factorization, singleton inertia determinants, or
finite cycle traces.  Consequently the current construction derives the
Euler product and its zero-free half-plane, but not a space in which the
nontrivial zeros can occur.

## Falsifier

This boundary is crossed only by a source-derived continuation mechanism or
global operator whose determinant agrees with the completed zeta function.
Merely importing the known meromorphic continuation of `zeta(s)` does not
explain it from the Carrier.

## Scope

This is an analytic-strength audit of the conditional formal Euler theorem,
not a new proof about the location of classical zeta zeros.

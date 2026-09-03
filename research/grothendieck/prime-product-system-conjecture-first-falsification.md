# First falsification of the prime product-system conjecture

## Target

The conjecture asserted that a minimal faithful regular dilation with

`C_n=J*V_nJ`

and `V_mV_n=V_(mn)` would force prime-power composition of the compressed transfers.

## Exact counterexample

Let `H_infinity=C^3`, let `V` be the unitary three-cycle

`e_0 -> e_1 -> e_2 -> e_0`,

and let `H_0=C e_0` with inclusion `J`. Define

`C_k=J*V^kJ`.

Then

`C_1=0`, `C_2=0`, and `C_3=I`.

The dilation is unitary, regular, and minimal because the orbit of `e_0` spans `C^3`. The embedding is injective. Nevertheless,

`C_1^3=0 != I=C_3`.

Thus compression of a semigroup representation is not itself a semigroup representation. The conjecture as stated does not solve the first of the three target problems and is falsified before any Weil calculation.

## Missing hypothesis

Composition passes to compression only with an additional invariant-subspace condition. A standard sufficient condition is joint coinvariance:

`V_p* JH_0 subset JH_0`

for every prime generator, together with the identification

`C_p*=V_p*|_(JH_0)`.

Then products of adjoints restrict correctly, yielding the compressed semigroup law. Merely specifying matrix coefficients `J*V_nJ` is insufficient.

## Consequence for the unified programme

The revised conjecture must require a **minimal faithful regular coextension**, not an arbitrary regular dilation:

1. `JH_0` is jointly coinvariant under all prime isometries;
2. compressed adjoints are the declared transfer adjoints;
3. the regular/Nica covariance holds on the dilation;
4. the Weil coefficient identity and quotient injectivity hold;
5. finite prime translates span densely.

This is strictly stronger and more falsifiable. The first local test is no longer only the Brehmer defect: one must also test the coinvariance residual

`(I-JJ*)V_p*J`.

A nonzero residual shows that the proposed dilation cannot enforce prime-power composition even if every finite Gram matrix is positive.

## Disposition

The original conjecture is rejected. Its explanatory mechanism survives only after adding joint coinvariance/coextension. Whether the complete Weil transfers admit that stronger structure remains open.

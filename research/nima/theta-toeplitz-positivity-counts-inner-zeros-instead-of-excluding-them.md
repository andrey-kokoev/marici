# Toeplitz positivity counts inner zeros instead of excluding them

## Question

Half-line compression is the first genuinely noncommutative operation left after the arithmetic inverse-derivative incidence becomes diagonal.

Let \(H^2\) be a Hardy space with projection \(P_+\), and define

\[
T_\phi=P_+M_\phi P_+.
\]

The Toeplitz product defect can be a signed Hankel square. Could its positivity provide the missing RH orientation?

The answer is negative without an additional source-derived coisometry law.

## One-zero witness

Let \(B_a\) be a Blaschke factor with one zero \(a\) in the Hardy domain. On the boundary,

\[
|B_a|=1.
\]

Multiplication by \(B_a\) preserves the Hardy space, so

\[
T_{B_a}h=B_a h.
\]

It is an isometry:

\[
T_{B_a}^*T_{B_a}=I.
\]

But it is not onto. Its range is

\[
B_aH^2,
\]

and the orthogonal complement

\[
K_{B_a}=H^2\ominus B_aH^2
\]

is one-dimensional. Therefore

\[
I-T_{B_a}T_{B_a}^*
=
P_{K_{B_a}}
\ge0.
\]

The positive defect does not forbid the zero of \(B_a\). It is the projection that records that zero.

## Finite Blaschke products

For a finite Blaschke product \(B\) of degree \(m\),

\[
T_B^*T_B=I,
\]

while

\[
I-T_BT_B^*
=
P_{K_B},
\qquad
K_B=H^2\ominus BH^2.
\]

Its defect rank is

\[
\operatorname{rank}P_{K_B}=m,
\]

counting zeros with multiplicity.

Thus Toeplitz–Hankel positivity naturally supports a divisor. It converts the divisor into positive cokernel geometry.

## Consequence for the puncture picture

This is the operator form of the earlier correction to naive holonomy:

- an off-sector zero creates an inner factor;
- the inner factor creates a model-space state;
- the compressed multiplier remains contractive or isometric;
- its positive defect is the zero-state projection.

Hence neither contractivity nor positivity of the Hankel defect proves zero confinement. Those laws are compatible with arbitrarily many interior zeros.

The puncture/cohomology intuition survives in a more precise form: zero multiplicity equals Toeplitz cokernel dimension. This is an index theorem, not a vanishing theorem.

## What would exclude zeros

To eliminate the inner divisor, one would need

\[
T_BT_B^*=I
\]

in addition to

\[
T_B^*T_B=I.
\]

Then \(T_B\) would be unitary and \(K_B=0\). For a scalar inner multiplier, this rules out every nonconstant Blaschke factor.

But asserting coisometry for the inner factor extracted from the completed section is equivalent to asserting that the section has no zeros in the Hardy domain. It is RH-strength unless derived independently from the labelled theta/Tate source.

## Hostile multiplier survives the boundary laws

A hostile Blaschke factor preserves boundary modulus:

\[
|B|=1.
\]

Therefore it preserves any law depending only on:

- boundary unitarity;
- scalar functional-equation symmetry after reciprocal pairing;
- contractivity of compression;
- positivity of the Toeplitz or Hankel defect.

Yet it inserts an interior divisor and a nonzero model space \(K_B\).

This is the exact finite falsifier for any claim that boundary Toeplitz positivity alone confines zeros.

## Relation to the three lenses

The ordered lens does retain more information than determinant and logarithmic current: it sees the model-space cokernel that scalar boundary modulus misses.

However, the retained information is diagnostic rather than prohibitive. It tells us where the missing states live and how many there are. It does not force their absence.

The source-derived theorem still required is not positivity. It is a completeness or surjectivity law for the compressed transport.

## Admissible next gate

A noncircular advance must construct the theta/Tate compressed operator before extracting the divisor and prove one of the following from source operations:

1. its range is dense and closed;
2. its adjoint kernel vanishes;
3. it is coisometric as well as isometric;
4. its model-space defect is supported only on the critical seam through a typed two-sector relation.

Each claim must survive hostile inner multipliers for a reason that refers to labelled source incidence, not merely boundary modulus or functional symmetry.

## Finite falsifier

Insert a degree-one Blaschke factor into any proposed scalar symbol. Compute

\[
I-T_BT_B^*.
\]

If the proposed law accepts this nonzero positive rank-one projection while claiming to prohibit the zero, the law is insufficient.

If a proposed source law rejects the factor, the rejection must occur before inspecting \(a\), through a failed constructor, incidence, domain, or completion relation.

## Disposition

Toeplitz/Hankel compression is genuinely noncommutative and therefore richer than the scalar Euler product. But its canonical positivity counts interior zeros rather than excluding them.

The RH-bearing question is now exact: which labelled theta/Tate source operation forces the compressed transport to have no off-seam model-space cokernel?

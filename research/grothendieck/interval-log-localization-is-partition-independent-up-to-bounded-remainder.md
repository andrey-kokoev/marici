# Interval logarithmic localization is partition-independent up to bounded remainder

## Question

Does choosing a particular two-chart partition alter the closed local Weil operator or only its explicit order-zero comparison constant?

## IMS identity for a quadratic partition

Let `A=log(1+|D|)` and choose real bounded windows `chi_j` with

`sum_j chi_j^2=1`.

On a common smooth core,

`A-sum_j chi_j A chi_j`

`=(1/2)sum_j [chi_j,[chi_j,A]]`.

If every first commutator `[A,chi_j]` is bounded, then the localization error is bounded, with

`||A-sum chi_j A chi_j||`

`<=sum_j ||chi_j||_infinity ||[A,chi_j]||`.

Voevodsky's Fourier-moment estimate supplies

`||[A,chi_j]|| <= sum_k |k| |chi_hat_j(k)|`,

and the septic smoothstep profile gives a finite explicit derivative bound for this moment.

## Bounded change of partition

For another quadratic partition `eta_k`, subtract the two IMS identities:

`sum_j chi_j A chi_j-sum_k eta_k A eta_k`

is the difference of two bounded double-commutator remainders. Therefore any two admissible partitions with finite first Fourier moments produce localizations differing by a bounded self-adjoint operator.

The underlying unlocalized closed form and operator do not depend on the partition. Only the sufficient Gårding constant changes.

## Coordinate transfer

An affine chart coordinate `y=ax+b` transforms the principal logarithmic multiplier by

`log|D_y|=log|D_x|-log|a|`

under the corresponding unitary dilation, modulo the chosen low-frequency regularization. The scale change is an explicit scalar bounded term. Translation `b` contributes no multiplier change.

Thus chart-coordinate normalization cannot alter the logarithmic principal reserve; it adds an explicit `|log|a||` budget.

## Applying the septic profile

The septic smoothstep can be converted to a quadratic partition, for example by normalized windows derived from `s_h` and `1-s_h`. Its endpoint vanishing order is sufficient to retain smoothness after the required normalization, but the exact derivative budget must be recomputed for the normalized square-root windows rather than copied from the linear partition.

Alternatively, one may retain the linear partition and derive its corresponding localization identity directly. Mixing the linear derivative constant with the quadratic IMS identity would be a normalization error.

## Consequence

No arithmetic authority is needed to select the interval cover or overlap width. They are analytic auxiliary data. A valid proof must:

1. state the chosen linear or quadratic normalization;
2. compute its commutator constant;
3. include affine coordinate-scale constants;
4. show the final unlocalized form statement is unchanged under bounded partition replacement.

## Disposition

Partition independence is proved at the bounded-remainder level. Voevodsky's materialized septic profile supplies a valid linear auxiliary partition, but using the quadratic IMS formula requires a separately checked normalized profile constant.

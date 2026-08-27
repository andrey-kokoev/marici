# The labelwise backward equalizer leaves a cross-fiber augmentation kernel

## Valuation-fiber decomposition

Fix a prime `p`. Every positive integer has a unique form

\[
n=mp^j,
\qquad p\nmid m.
\]

Keep each `p`-free base `m` as a separate source label and sum only along its
valuation chain. Let `F_m` denote that chain's half-line transform, `R_m` its
grade-zero primitive transform, and `A_m,B_{m,2}` its one-cell primitive and
two-cell full seam terms.

The same source calculation as in the aggregate theorem applies independently
to every chain:

\[
(1+q)R_m-qA_m-q^2B_{m,2}=(1-q^2)F_m,
\qquad q=p^{-1/2-z}.
\]

Thus the desired labelwise backward packet exists before scalar aggregation.

## What a global zero actually says

The complete scalar readout is

\[
F=\sum_{p\nmid m}F_m.
\]

At a global zero,

\[
\sum_{p\nmid m}F_m=0.
\]

This is one augmentation equation. It does not imply `F_m=0` for each
valuation fiber. Consequently the vector residual

\[
\mathcal R_m
=(1+q)R_m-qA_m-q^2B_{m,2}
=(1-q^2)F_m
\]

need not vanish componentwise. It lies in the augmentation kernel:

\[
\sum_{p\nmid m}\mathcal R_m=0.
\]

For `d` retained `p`-free fibers, this kernel has dimension `d-1`.

## Smallest witness

With two fibers, take

\[
(F_{m_1},F_{m_2})=(1,-1).
\]

The scalar output vanishes, while both labelwise residuals are nonzero when
`q^2` is not one. The scalar equalizer is therefore the augmentation quotient
of a nontrivial vector identity, not a componentwise Ward balance.

## Consequence for the backward tower

Retaining labelwise mates repairs the rank-one loss found in the scalar dagger
lift. But scalar nullity supplies only one relation among them. Imposing the
zero-state equalizer independently on every fiber would silently strengthen
one observed scalar zero into `d` separate zeros.

The missing `+1` coherence therefore has a more precise domain:

```text
cross-fiber augmentation kernel of the labelwise backward packet
```

It must use a source-derived operation coupling distinct `p`-free bases. A
diagonal valuation recursion cannot control that kernel because it acts
independently on each chain.

Possible sources are global Poisson sewing, multiplicative convolution among
base labels, or an exterior observer retaining pairwise fiber interference.
Whichever is used must be constructed before scalar zero inspection and must
commute with cutoff restriction.

## Relation to `3+2+1`

The final mate cell is now seen to have its own internal tower:

```text
scalar mate
-> labelwise mate
-> augmentation-kernel comparison
-> sesquilinear/exterior Ward form
-> cutoff and completion coherence
```

This confirms the operator's earlier observation that a coherence cell across
the main towers can itself be a tower.

## Durable verification

- Checker: `checkers/check_labelwise_equalizer_augmentation_kernel.py`
- The checker verifies the kernel dimensions and the smallest nonzero
  two-fiber scalar-null witness exactly.

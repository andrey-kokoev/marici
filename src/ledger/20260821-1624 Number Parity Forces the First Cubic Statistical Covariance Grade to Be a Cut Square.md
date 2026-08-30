# 1624 — Number Parity Forces the First Cubic Statistical Covariance Grade to Be a Cut Square

## Question

With a nonzero Gaussian first jet present, can interference linear in the cubic production amplitude escape the positive labelled Cut pairing in the second covariance grade?

## Source-compatible filtration

After imposing the source tadpole/centering condition, a Gaussian state lies in the even number-parity sector.  One cubic insertion lies in the odd sector.  The centered covariance observables

\[
a^\dagger a,
\qquad
aa,
\qquad
a^\dagger a^\dagger
\]

are parity-even.

Therefore, for every centered Gaussian state and one-cubic state,

\[
\boxed{
\langle\Psi_{\rm G}|O_2|\Psi_{\rm cubic}\rangle
=0.
}
\]

Nonzero squeezing changes coefficients inside the even sector but does not change this selection rule.

## Consequence

Every covariance contribution linear in the cubic amplitude vanishes.  The first statistical cubic grade is quadratic:

\[
\delta V_{\rm cubic}^{(2)}
=
\operatorname{Tr}_{qk}
|\Psi_{\rm cubic}\rangle
\langle\Psi_{\rm cubic}|,
\]

which is exactly the labelled Cut square of Entries 1617--1618 and 1623.

The checker verifies all even/odd matrix-element supports for number states through occupation 13 and audits complex Cut-norm positivity.

## Narrow result

\[
\boxed{
\text{In the centered Gaussian-plus-cubic sector, no linear cubic interference lies outside the Cut norm.}
}
\]

Thus the positive second-Rees completion survives a nonzero Gaussian first jet.  The cubic statistical correction begins at second normal order for a structural parity reason, not by cancellation fitted to a kernel.

## Qualifications

- A nonzero one-point function must first be removed by the source tadpole condition.
- The result concerns centered two-point covariance; parity-odd observables can have linear cubic terms.
- Quartic interactions are parity-even and require a separate test because they can interfere linearly with the Gaussian sector.

## Architectural consequence

The second-Rees order is selected jointly by coefficient parity and the existing Cut calculus.  No new carrier incidence is needed.

## Durable artifacts

- `research/benincasa/checkers/gaussian_cubic_parity_cut.rs`
- `research/benincasa/results/gaussian-cubic-parity-cut.json`
- `research/benincasa/gaussian-cubic-parity-cut.md`

## Next hostile falsifier

Repeat the covariance-grade test for a source-admitted quartic interaction.  Because a single quartic insertion is parity-even, it can interfere with the Gaussian sector at first order.  Determine whether that term is a Hamiltonian tangent, a source-normalization correction, or a genuinely non-Cut statistical direction.  Freeze the quartic source and tadpole/normalization prescription before calculation.

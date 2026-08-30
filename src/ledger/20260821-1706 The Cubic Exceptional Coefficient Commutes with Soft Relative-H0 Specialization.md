# 1706 — The Cubic Exceptional Coefficient Commutes with Soft Relative-H0 Specialization

## Physical-coefficient falsifier

Entry 1705 closes the bare sign costalk under nested softening.  Couple the
actual cubic Cut pair coefficient to the exceptional covariance tensor and
test the same square.

## Labelled contraction

Let `C_ij` denote the source-derived cubic pair coefficients and

\[
\Xi_{ij}=u_iu_j.
\]

On a nonzero support graph `H`, define the componentwise exceptional
coefficient

\[
F_C(H)=\sum_{(i,j)\in E(H)}C_{ij}\Xi_{ij}.
\]

For a deeper support `H2 subset H1`, restriction takes principal labelled
submatrices of both `C` and `Xi`.  Therefore

\[
\boxed{
F_C(H_2)
=\sum_{(i,j)\in E(H_2)}C_{ij}u_iu_j
}
\]

whether restriction is performed before or after forming the labelled tensor
contraction.

The conditional fiber multiplier from Entry 1697,

\[
s^2-1,
\]

is common to every component and commutes with the same maps.  Components that
disappear under deeper softening contribute zero by extension-by-zero.

## Narrow result

\[
\boxed{
\text{the physical cubic exceptional coefficient commutes strictly with nested soft relative-}H_0\text{ specialization.}
}
\]

No coefficient extension survives on disappearing components.  The existing
labelled Cut restriction, symmetric-square Rees tensor, and support costalk are
sufficient for this test.

## Durable artifacts

- `research/benincasa/checkers/cubic_soft_costalk_naturality.rs`
- `research/benincasa/results/cubic-soft-costalk-naturality.json`
- `research/benincasa/cubic-soft-costalk-naturality.md`

## Next falsifier

Replace the Gaussian pair tensor by the first non-Gaussian connected tensor
from Entry 1692.  Test whether the odd third-cumulant coefficient extends by
the same support maps or couples nontrivially to the component-sign costalk.

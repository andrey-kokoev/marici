# 1640 — Correlated Gaussian Support Is Not an Ordinary CP Assignment Channel

## Hard-to-vary claim

Entry 1639 identifies a nonempty quantum compatibility domain for the opposite-momentum Gaussian correlation.  Test whether that domain is merely the restriction of an ordinary state-independent Gaussian CP assignment channel.

## Assignment forced by marginal preservation

A Gaussian assignment acts by

\[
V\longmapsto XVX^T+Y.
\]

Preserving the observed covariance and mean while fixing the partner covariance (aI) and correlation (cZ) forces

\[
X=\begin{pmatrix}I\\0\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&cZ\\cZ&aI\end{pmatrix}.
\]

Its complete-positivity condition is

\[
Y+i(\Omega_{\rm out}-X\Omega_{\rm in}X^T)\succeq0.
\]

## Finite obstruction

The observed-(q)/partner-(q) principal submatrix is

\[
\begin{pmatrix}0&c\\c&a\end{pmatrix},
\]

with determinant

\[
\boxed{-c^2.}
\]

It is negative for every (c\ne0).  Therefore no ordinary Gaussian CP assignment can preserve the observed state while adjoining a fixed nonzero opposite-momentum correlation.

At (c=0), the remaining CP block is (aI+iJ), with eigenvalues (a-1) and (a+1).  It is positive for (a\ge1), recovering the generic product assignment.

## Narrow result

\[
\boxed{
c\ne0:\ \text{physical compatibility domain but no ordinary CP assignment};
\qquad
c=0:\ \text{ordinary product CP assignment}.
}
\]

Thus Entry 1639's supported object is genuinely richer than a channel restricted after the fact.  It must retain the initial correlation and its admissible interventions as relational/process-tensor data.  The obstruction is coefficient-theoretic and occurs on the already existing opposite-momentum support; it is not evidence for a new carrier stratum.

This result does not yet construct the process tensor or prove positivity of an interacting reduced evolution.

## Durable artifacts

- `research/benincasa/checkers/correlated_gaussian_cp_assignment_no_go.rs`
- `research/benincasa/results/correlated-gaussian-cp-assignment-no-go.json`
- `research/benincasa/correlated-gaussian-cp-assignment-no-go.md`

## Next falsifier

Construct the minimal intervention superchannel on the correlated pair without demanding a state-independent assignment from the observed marginal.  Test whether the labelled cubic Cut step gives a positive multilinear functional on all compatible Gaussian instruments and whether its (c\to0) specialization equals the generic product channel.

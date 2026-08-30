# 1673 — Flagged Covariance Degeneration Has One Quadratic Form per Normal Block

## Uniform-rank falsifier

Entry 1672 finds a secondary quadratic normal coordinate at the first rank-one
degeneration. Test whether successive covariance-rank drops require new
structure or follow one invariant rule.

For a vanishing graded covariance block, write

\[
K(t)=W(t)BW(t),
\qquad
v(t)=W(t)\gamma,
\]

where

\[
W(t)=\operatorname{diag}(t^{w_1},\ldots,t^{w_s})
\]

has arbitrary positive integral weights and (B) is an invertible symmetric
normal-block covariance.

Then

\[
K(t)^{-1}=W(t)^{-1}B^{-1}W(t)^{-1},
\]

so

\[
\boxed{
v(t)^TK(t)^{-1}v(t)=\gamma^TB^{-1}\gamma.
}
\]

For every matrix term, the normal exponent cancels:

\[
w_i-(w_i+w_j)+w_j=0.
\]

Thus the finite nearby correction is invariant under the choice of weighted
coordinates inside the graded block.

The exact checker verifies 60 correlated positive-definite normal blocks of
ranks one through six, 910 matrix-inverse identities, 60 positive quadratic
forms, and 3,640 independent flag-weight cancellations.

## Narrow result

\[
\boxed{
\text{each covariance normal block contributes one invariant quadratic Schur form.}
}
\]

The tempting description as one scalar ratio per vanishing eigen-direction is
not invariant when the normal block is correlated. It is merely the diagonal
basis presentation of

\[
\gamma^TB^{-1}\gamma.
\]

Successive rank drops are therefore governed by the existing flagged normal
calculus with sector-specific symmetric-form coefficients. No additional
carrier incidence or higher sewing primitive is indicated.

This theorem assumes that the graded normal block (B) is invertible. Its own
rank-drop locus must be handled by the next flag grade, as in Entries 1671--1672.

## Durable artifacts

- `research/benincasa/checkers/flagged_covariance_quadratic_normal_form.rs`
- `research/benincasa/results/flagged-covariance-quadratic-normal-form.json`
- `research/benincasa/flagged-covariance-quadratic-normal-form.md`

## Next falsifier

Compare this covariance flag with the cosmological energy-normal/Rees flag.
Test whether their product degeneration obeys a strict external tensor rule or
whether mixed energy--covariance normal terms survive. A nonzero mixed term
would be the first coupling not explained by separate carrier flags and
coefficient quadratic forms.

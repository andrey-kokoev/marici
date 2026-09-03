# Mellin–Poisson normalization square

## Question

Which source operation converts the reciprocal theta family into the rapidly decaying even source whose bilateral transform is the centered completed zeta function?

## Claim boundary

This identifies the normalization and reciprocal-natural square. It supplies no positivity theorem or zero localization.

## Logarithmic source

Set \(q=\log u\),

\[
g(q)=\psi(e^q),
\qquad
h(q)=g(q)+\frac12.
\]

Theta reciprocity is

\[
h(-q)=e^{q/2}h(q).
\]

Define

\[
L=2\partial_q^2+\partial_q.
\]

Under bilateral Mellin integration against \(e^{sq/2}\), integration by parts turns \(L\) into

\[
2(s/2)^2-s/2=\frac{s(s-1)}2.
\]

This is precisely the factor converting \(\Lambda(s)\) to \(\xi(s)\).

## Completed even source

Define

\[
\Phi(q)=e^{q/4}Lh(q).
\]

The operator annihilates both asymptotic polar modes, the constant and \(e^{-q/2}\). Differentiating the reciprocity law gives

\[
(Lh)(-q)=e^{q/2}(Lh)(q),
\]

hence

\[
\Phi(-q)=\Phi(q).
\]

In the centered coordinate \(w=s-1/2\),

\[
\xi(s)=\int_{\mathbb R}\Phi(q)e^{wq/2}\,dq.
\]

Evenness of \(\Phi\) induces \(w\mapsto-w\), so the Mellin normalization and Poisson reciprocity routes commute.

## Completion consequence

If the stated rapid decay of \(\Phi\) is retained, compact-uniform domination makes this transform entire and completes affine fillers independently of the scalar Euler coefficient space. The failed \(B_\epsilon\) embedding therefore obstructs only the Euler-cutoff realization.

## Disposition

The Mellin–Poisson normalization square is constructed symbolically. The remaining RH-strength gate is not normalization, reciprocal coherence, or filler completion; it is a source-derived positivity property strong enough to force real spectral zeros.

## Verification

- `research/voevodsky/mellin-poisson-normalization-square-v1.json`
- `research/voevodsky/checkers/check_mellin_poisson_normalization_square.py`
- `research/voevodsky/results/mellin_poisson_normalization_square.json`

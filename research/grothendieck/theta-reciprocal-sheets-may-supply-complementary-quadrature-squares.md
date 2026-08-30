# Reciprocal theta sheets may supply complementary quadrature squares

## Correction and bounded question

The unit-coupling identity

\[
 |\psi|^2\pm\Re(\psi^2)=2A^2\ \text{or}\ 2B^2
\]

is nonnegative but degenerate. Can the two Fourier--Tate orientations supply
the two opposite signs canonically, so the complete Ubersector restores a
strict norm?

## Quadratic classification

Allow the spin-two component to have a source-fixed phase:

\[
 E_{\lambda,\theta}(\psi)
 =|\psi|^2+\lambda\Re(e^{-2i\theta}\psi^2).
\]

Writing `e^(-i theta) psi=A_theta+iB_theta` gives

\[
 E_{\lambda,\theta}
 =(1+\lambda)A_\theta^2+(1-\lambda)B_\theta^2.
\]

Therefore `|lambda|<1` is positive definite, `|lambda|=1` is a rank-one
quadrature square, and `|lambda|>1` is indefinite. Both the magnitude and
frame angle must descend from source normalization.

## Complementary-sheet theorem candidate

Let the direct and reciprocal sheets carry the same invariant trace and
opposite spin-two orientations in the same transported frame:

\[
 E_+=|\psi|^2+\Re(e^{-2i\theta}\psi^2),
\]

\[
 E_-=|\psi|^2-\Re(e^{-2i\theta}\psi^2).
\]

Then

\[
 \boxed{E_++E_-=2|\psi|^2.}
\]

The full two-sector energy is strictly positive for every nonzero amplitude,
although either sheet separately has a null quadrature. The hard source
statement is

\[
 \boxed{
 \text{Fourier--Tate exchange preserves the trace, reverses spin two,
 and transports the quadrature frame coherently}.}
\]

## Why sign reversal is plausible but unproved

The spin-two component is an oriented reflection-transverse jet. Reversing
valuation orientation should reverse its normal direction, whereas the
Hermitian trace is orientation-blind. But Fourier transform can also rotate
the quadrature frame. A sign flip in different frames does not produce
complementary squares. The complete metaplectic phase must be derived from
the labelled source.

## Finite matrix certificate

At cutoff `X`, express each completed bulk form in a common transported real
frame:

\[
 E_X(A,B)
 =\begin{pmatrix}A&B\end{pmatrix}
 Q_X\binom AB,
 \qquad
 Q_X=\begin{pmatrix}\alpha_X&\gamma_X\\
 \gamma_X&\beta_X\end{pmatrix}.
\]

Nonnegativity requires

\[
 \alpha_X\ge0,\qquad\beta_X\ge0,
 \qquad\det Q_X\ge0.
\]

Strict positivity requires `alpha_X>0` and `det Q_X>0`. For complementary
closure, test the stronger source identity

\[
 \boxed{Q_X^++Q_X^-=2c_XI,qquad c_X>0.}
\]

The scalar `c_X` must be source-normalized and cutoff-compatible.

## Falsifiers

Complementary closure fails if sheet exchange does not reverse spin two
exactly, if the frames differ, if the trace coefficients differ, if prime two
leaves a labelled off-diagonal residual, or if `c_X` degenerates under
completion.

If complementarity fails, the remaining unit-coupling route is a
source-derived transversality theorem excluding the null quadrature from the
two-endpoint boundary domain.

## Present boundary

The algebraic sum of opposite spin-two sheets is proved universally. Its
identification with the actual Fourier--Tate pair is conjectural. The next
calculation is the exact metaplectic transformation of the two-copy amplitude
and its real quadratic matrix at the smallest labelled cutoff containing
prime two and the archimedean channel.


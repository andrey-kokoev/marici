# Correction: the characterwise bare Hardy transition is not Hilbert--Schmidt, so the square-root-log sewing bound is unproved

## Claim being corrected

A proposed estimate factored the characterwise sewing term as

\[
|\mathcal E_{L,\chi}(g,h)|
\le
p_{L,\chi}^{1/2}d_\chi(g,h),
\]

with

\[
p_{L,\chi}
=
\|P Q(I-P)K_\chi\|_{HS}^2
\]

and assumed

\[
p_{L,\chi}
\le
C(1+|\chi|)^d(1+L).
\]

This treats the bare radial Hardy transition as Hilbert--Schmidt. It is generally not.

## Pure exponential counterexample

Take one radial Hardy fiber and the symbol

\[
\sigma_L(s)
=e^{-2iLs}
\]

with no Tate gamma perturbation. In the Fourier-dual variable, multiplication by `sigma_L` translates a Hardy half-line by length `2L`.

The difference of the two half-line projections is multiplication by the indicator of an interval of length `2L` on `L2(R)`.

That projection has infinite-dimensional range and infinite ordinary operator trace. It is not Hilbert--Schmidt:

\[
\boxed{
\|P Q_L(I-P)\|_{HS}
=\infty.
}
\]

Finite interval length in a continuous spectral variable does not mean finite operator rank or finite trace.

## Kernel diagnosis

The formal Hilbert--Schmidt integral for the Hardy commutator contains

\[
\iint_{\mathbb R^2}
\frac{
|e^{-2iLs}-e^{-2iLt}|^2
}{|s-t|^2}dsdt.
\]

The integrand depends only on `s-t`. Its integral in the center variable

\[
\frac{s+t}{2}
\]

is infinite. The previously computed `O(L)` integral was only the difference-variable density

\[
\int
\frac{
|e^{-2iLr}-1|^2
}{r^2}dr
=
C L.
\]

It is a trace **per unit center volume**, not a bare Hilbert--Schmidt norm.

## Gamma phase does not repair the bulk infinity

Multiplication by a unimodular Tate factor

\[
\gamma_\chi(s)
\]

does not localize the center variable. Its derivatives control symbol variation but do not make the bare translated Hardy interval finite-rank.

Thus

\[
H_{e^{-2iLs}\gamma_\chi}
\]

need not be Hilbert--Schmidt without observer or radial localization.

## What observer localization does

For a rapidly decreasing multiplier `m_(g,chi)`, the localized commutator

\[
[\Pi,M_{\sigma_{L,\chi}}]
M_{m_{g,\chi}}
\]

can be Hilbert--Schmidt. Its kernel has the additional factor `m(t)`, making the center-variable integral finite.

The valid bound is

\[
\boxed{
\|[\Pi,M_{\sigma_{L,\chi}}]
M_{m_{g,\chi}}
\|_{HS}^2
\le
C_{g,N}
(1+|\chi|)^{-N}
(1+L).
}
\]

After summing angular characters, this gives an observer-localized squared norm of order `O(L)`.

## Why square-root improvement does not follow

To get

\[
|\mathcal E_L|
=O(\sqrt L),
\]

one attempted to multiply:

- a bare transition norm of order `sqrt L`;
- a cutoff-independent observer boundary norm.

The first factor is infinite. Localizing it with the observer makes it finite, but then the second factorization changes; one cannot reuse the same observer commutator as an independent second factor without proving a new asymmetric Schatten decomposition.

The currently justified estimate is only

\[
\boxed{
|\mathcal E_{L,S}(g,h)|
=O_{g,h}(1+L)
}
\]

from the fully observer-localized Hardy analysis.

Therefore

\[
\boxed{
\mathcal E_{L,S}(g,h)
=o(L)
}
\]

is not yet proved.

## Finite radial regulator

Introduce a finite center-variable projection `Z_M` in the radial Mellin coordinate. Then

\[
Z_M P Q(I-P)Z_M
\]

may be Hilbert--Schmidt, with squared norm approximately

\[
ML.
\]

Removing `Z_M` sends the bare norm to infinity. Observer localization replaces `M` by an effective weighted center volume, but extracting a square-root bound requires exploiting cancellation or a trace-density pairing, not ordinary Cauchy--Schwarz against the unlocalized transition.

## Valid routes to `o(L)`

At least one genuinely new input is required:

### Relative trace cancellation

Compute the linear coefficient in the localized strong-Szego/Widom expansion and prove it cancels after bulk subtraction or opposite-polarity assembly.

### Asymmetric Schatten factorization

Factor the exact sewing product as

\[
XY
\]

with both `X,Y` Hilbert--Schmidt and only one factor carrying `sqrt L` growth, while the other is uniformly bounded. The observer must remain present in the factorization.

### Trace-density centering

Subtract the linear Hardy translation density before applying Cauchy--Schwarz, then prove the centered transition belongs to `L2` with bounded norm.

None of these follows from the polynomial gamma derivative estimate alone.

## Effect on finite-packet Douglas promotion

The finite-packet theorem remains correct as an implication:

\[
V_\Lambda^{-1}G_\Lambda^+
\to G_0
\Longrightarrow
\text{eventual Douglas equivalences}.
\]

But its analytic hypothesis has not been verified. The current `O(log Lambda)` sewing estimate is the same order as the bulk and does not imply normalized convergence.

Thus finite-packet cutoff correspondences have not yet been promoted to operators for the positive triple feature.

## Status table

| Statement | Status |
|---|---|
| observer-localized Hardy transition is Hilbert--Schmidt | established under declared symbol bounds |
| its squared norm is `O(1+L)` | established in the localized model |
| bare characterwise transition is Hilbert--Schmidt | false in the continuous radial model |
| total sewing is `O(sqrt L)` | unproved |
| total sewing is `o(L)` | unproved |
| finite-packet normalized positive Gram convergence | conditional |

## Disposition

The characterwise polynomial bound must be formulated for an observer-localized or trace-density transition, not

\[
\|P Q(I-P)K_\chi\|_{HS}^2.
\]

The square-root-log sewing conclusion is withdrawn. The next exact task is to compute and cancel the linear coefficient of the observer-localized relative Hardy trace, or construct a valid centered Schatten factorization.

# RH primitive principal-value pushforward needs relative moment cancellation

## Question

Does the primitive exponential arithmetic current act continuously on the odd
principal-value boundary channel after comoving pushforward?

## Principal-value tail

The principal-value boundary distribution is the Fourier image of the oriented
front. When it is evaluated against a localized test translated to large scale
(L), the result is a Hilbert-transform tail. Generically its leading behavior
is algebraic:

\[
H\varphi(L)
\sim
\frac{m_0(\varphi)}{L}
+\frac{m_1(\varphi)}{L^2}
+\cdots,
\]

where the coefficients are moments of the test.

This tail is qualitatively different from the localized delta response. Even
Gaussian localization does not by itself make the principal-value response
exponentially small at distant scale when the relevant moment is nonzero.

## Arithmetic consequence

The primitive scale measure grows exponentially. Multiplying a generic
(1/L) principal-value tail by the primitive weight therefore fails even the
term test for convergence. The square grade, with only harmonic-scale weight,
can pair with the same (1/L) tail because the resulting terms have square
summability type.

A dyadic surrogate makes the distinction exact:

- primitive weight: (2^n/n);
- square weight: (1/n);
- principal-value tail: (1/n).

Then the primitive terms are

\[
\frac{2^n}{n^2},
\]

which do not tend to zero, while the square terms are (1/n^2) and converge.

## Required relative cancellation

The primitive odd channel cannot be pushed forward separately on generic
localized tests. A relative sewing must first cancel the algebraic moment tail
using source-derived overlap, reciprocal, or archimedean boundary data.

In the surrogate, if the exact leading (1/n) response is removed and the
remaining response is (2^{-2n}), primitive weighting gives

\[
\frac{1}{n2^n},
\]

which converges. The subtraction coefficient cannot be fitted from desired
convergence. It must be the boundary moment supplied by the source sewing law.

## Refined four-lane status

- Square delta: compatible with the tempered grade subject to the existing
  nonfinite readout qualification.
- Square principal value: compatible with algebraic Hilbert tails in the
  surrogate.
- Primitive delta: requires the exponential test grade already identified.
- Primitive principal value: fails separate pushforward and requires relative
  moment cancellation before arithmetic aggregation.

Thus the four lanes do not have four independent scalar completions. Their
joint relative sewing is essential.

## DPC

Any proposed primitive principal-value completion must specify:

1. the test-space moments that generate the algebraic tail;
2. the source boundary channel supplying each subtraction;
3. a cutoff-independent subtraction law;
4. compatibility with reciprocal reflection and chart parity;
5. a remainder topology strong enough for primitive exponential weighting;
6. recovery of every finite cutoff before the infinite limit;
7. a hostile localized test with nonzero leading moment.

If only finitely many moments are cancelled while the remainder remains merely
algebraic, primitive exponential aggregation still fails. The source must
produce exponential remainder control or an exact nonperturbative relative
cancellation.

## Claim boundary

This packet proves an exact surrogate no-go and identifies the analytic
mechanism. It does not derive the actual theta/Tate moment subtraction, prove
the required exponential remainder, or establish RH.

## Disposition

Separate primitive principal-value scalarization is closed negative. The live
constructor is a relative boundary sewing that cancels the principal-value
moment tail before primitive prime aggregation.


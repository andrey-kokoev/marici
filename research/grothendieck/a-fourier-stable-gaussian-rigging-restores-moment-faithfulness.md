# A Fourier-stable Gaussian rigging restores moment faithfulness

## Question

Ordinary Hilbert completion of the Gaussian dilation orbit fills the entire
even carrier and reintroduces moment-invisible states.  Is there a
source-compatible finer completion that preserves Fourier transport,
dilation, comb sampling, and quasianalytic moment faithfulness?

## The candidate source steps

For (a,b>0), let (mathcal G_{a,b}) contain functions (f) for which
there is a constant (C) satisfying

\[
|f(x)|\le Ce^{-ax^2},
\qquad
|\widehat f(\xi)|\le Ce^{-b\xi^2}.
\]

Equip each step with seminorms controlling both displayed Gaussian bounds,
and take the inductive union

\[
\mathcal G
=
\bigcup_{a,b>0}\mathcal G_{a,b}.
\]

This is the Roumieu form of the critical Gaussian Gelfand–Shilov rigging.  It
contains the theta Gaussian and all of its finite dilations.

## Exact source covariance

Fourier transform swaps the parameters:

\[
\mathcal F:
\mathcal G_{a,b}
\longrightarrow
\mathcal G_{b,a}.
\]

For unitary dilation

\[
(U_qf)(x)=e^{q/2}f(e^qx),
\]

the parameters transform as

\[
(a,b)
\longmapsto
(ae^{2q},be^{-2q}).
\]

Both remain positive for every finite (q).  Thus the full dilation orbit and
Fourier reversal stay inside the inductive family.  On the reflection-even
sector, Fourier still acts as an involutive dagger.

## The comb is continuous

For (f\in\mathcal G_{a,b}),

\[
\sum_{n\in\mathbb Z}|f(n)|
\le
C\sum_{n\in\mathbb Z}e^{-an^2}
<\infty.
\]

Hence the integer-comb pairing is continuous on every step.  Poisson sewing
is therefore defined before scalar compression and respects the Gaussian
rigging.

## Why moments become faithful

Gaussian decay of (f) makes its Fourier transform entire.  The moments of
(f) determine all derivatives of (widehat f) at zero.  If every moment
vanishes, the entire Taylor series is zero, hence

\[
\widehat f=0
\]

and therefore (f=0).

Thus the complete moment germ is faithful inside (mathcal G), unlike in the
ambient Schwartz or even Hilbert carrier.

The previous compact Fourier-side bump is excluded.  Although its inverse
transform is Schwartz, the source and its Fourier transform cannot both obey
the required Gaussian bounds unless the state is zero.

## Why this is not topology fitting

The candidate was not selected merely to force moment determinacy.  Its three
defining features are already present in the source construction:

- the Gaussian theta vacuum;
- metaplectic Fourier transport;
- the full dilation orbit.

The topology is the smallest familiar Fourier-stable Gaussian decay class
containing those operations.  Nevertheless, source provenance is not yet
complete.  The nonarchimedean and boundary constructors must still decide
whether this archimedean choice is admissible in the full restricted product.

## Remaining gates

The candidate fails if any of the following cannot be established:

1. the primitive distributional current acts continuously on the combined
   adelic rigging;
2. the square Hilbert current and connected absolute-summable tail extend
   without being collapsed into the same grade;
3. the seam incidence and its adjoint are continuous;
4. the Hankel trace operator is continuous between the induced log-trace
   steps;
5. restricted-product completion preserves injectivity;
6. authorized arithmetic scale and Fock constructors remain continuous;
7. the topology is independent of Euler cutoff and zero data.

The main danger is the critical uncertainty boundary.  Gaussian decay on a
function and its Fourier transform cannot be strengthened arbitrarily without
forcing the space to zero.  The inductive parameters must therefore remain
part of the type rather than being replaced by one uniform strongest norm.

## Scope

Fourier covariance, dilation covariance, comb continuity, and moment
faithfulness are established for the candidate archimedean rigging.  Its
assembly with the full adelic arithmetic boundary vessel is open.  No RH
conclusion follows.

## Result

The first nontrivial completion candidate survives the flat-bump and Hilbert
cyclicity falsifiers.  A Fourier-stable Gaussian Gelfand–Shilov rigging keeps
the theta orbit, makes the comb continuous, and restores faithfulness of the
complete moment germ.  The research frontier moves to continuity of the
typed arithmetic boundary constructors on the combined restricted product.

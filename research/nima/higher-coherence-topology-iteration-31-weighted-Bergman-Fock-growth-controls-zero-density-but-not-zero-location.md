# Higher-coherence topology iteration 31: weighted Bergman/Fock growth controls zero density, but not zero location

## Candidate topology

Place the completed spectral section in a weighted entire-function Hilbert
space

\[
\mathcal F_\varphi
=
\left\{F:\int_{\mathbb C}|F(z)|^2e^{-2\varphi(z)}dA(z)<\infty\right\}
\]

or in a strip Bergman analogue adapted to Xi growth. Reproducing kernels make
all point and jet evaluations continuous, while Jensen/Carleson estimates
control zero density globally.

## Growth does not orient the divisor

Membership in such a space constrains the number and density of zeros, not
their placement on one line. If the weight admits the Xi section, polynomial
multiplication usually preserves membership after a finite weight adjustment.
The reciprocal-symmetric hostile

\[
F(z)\longmapsto(1-z^2)F(z)
\]

preserves entire order, reciprocal symmetry, and the broad growth class while
adding off-seam zeros at `plus-or-minus 1`.

Thus no topology defined only by radial growth, exponential type, or integrated
square norm can imply critical-line location.

## Reproducing-kernel consequence

Evaluation obeys

\[
|F(z)|^2\le K(z,z)\|F\|^2.
\]

This is an upper bound and gives no positive lower bound on `|F(z)|`. A
normalized sequence can converge to zero at selected points while retaining
bounded Fock norm. To exclude zeros one needs a frame lower bound or complete
interpolation theorem tied to the source divisor, not merely RKHS membership.

## Arithmetic Fock obstruction

On the prime-labelled symmetric Fock carrier,

\[
L(s)e_p=p^{-s}e_p
\]

and

\[
\|\Gamma(L(s))\|_1
=
\prod_p(1-p^{-\operatorname{Re}s})^{-1}.
\]

Trace class holds exactly for `Re(s)>1`. No equivalent Hilbert-Fock metric
moves this threshold to the critical strip, because bounded similarity
preserves trace-class membership.

A nonequivalent weight may force convergence only by changing the arithmetic
state object and requires a new source comparison.

## Higher-coherence interpretation

A weighted Fock tower can keep every finite spectral jet and organize growth
of increasingly high cone coordinates. But adding higher coordinates cannot
forbid a finite symmetric polynomial factor. Conversely, choosing a weight
that excludes the hostile factor while retaining Xi would encode detailed
knowledge of the divisor and be circular unless derived from source dynamics.

## Useful scope

The topology remains useful for:

- normal-family compactness;
- zero-density bounds;
- continuous all-jet evaluation;
- determinant-line growth control;
- separating finite arithmetic Fock provenance from the completed boundary
  pencil.

It does not provide line confinement.

## Verdict for topology 31

Weighted Bergman/Fock topology controls how many zeros can occur and how
sections behave at infinity, but is insensitive to the critical-line versus
off-line placement of a finite reciprocal zero set. Arithmetic Hilbert-Fock
completion also fails at the trace observer before reaching the critical strip.

The next nonredundant topology to test is a Paley--Wiener/de Branges exponential-
type topology with support constraints, where zero location may interact with
Fourier support and phase monotonicity more rigidly than in radial Fock spaces.
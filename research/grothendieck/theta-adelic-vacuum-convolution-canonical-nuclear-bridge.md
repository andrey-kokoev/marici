# The adelic vacuum gives a canonical nuclear integrality bridge

## Bounded question

Does the standard completed theta source select a particular smoothing map
between the two rigged Clifford charts, or does the spectral-multiplier
nonuniqueness of packet 100 remain?

## Source object

Let

\[
 \mathbb A=\mathbb R\times\prod_p'\mathbb Q_p,
 \qquad G=\mathbb A/\mathbb Q,
\]

with the standard global additive character and self-dual Haar measures.  Take
the factorized Schwartz--Bruhat vacuum

\[
 f(x)=e^{-\pi x_\infty^2}\prod_p1_{\mathbb Z_p}(x_p).
\]

Every local factor is Fourier-fixed, hence so is `f`.  Periodize it to `G`,

\[
 k_f(\bar x)=\sum_{q\in\mathbb Q}f(x+q),
\]

and let `K_f` be convolution by `k_f` on `L^2(G)`.

## Exact multiplier calculation

The character group of `G` is canonically `Q`.  On the character indexed by
`r in Q`, adelic Fourier expansion gives

\[
 K_f\chi_r=\widehat f(r)\chi_r=f(r)\chi_r.
\]

At the finite places,

\[
 \prod_p1_{\mathbb Z_p}(r)
 =
 \begin{cases}
 1,&r\in\mathbb Z,\\
 0,&r\in\mathbb Q\setminus\mathbb Z.
 \end{cases}
\]

Consequently

\[
 \boxed{
 K_f\chi_r=
 \begin{cases}
 e^{-\pi r^2}\chi_r,&r\in\mathbb Z,\\
 0,&r\notin\mathbb Z.
 \end{cases}}
\]

The operator is positive and trace class, and

\[
 \operatorname{Tr}K_f
 =\sum_{n\in\mathbb Z}e^{-\pi n^2}
 =\theta(1).
\]

The exponential multiplier makes it smoothing on the surviving integral
Fourier sector.  Its kernel is nevertheless infinite-dimensional:

\[
 \ker K_f
 =\overline{\operatorname{span}}\{\chi_r:r\in\mathbb Q\setminus\mathbb Z\}.
\]

Thus completion does not identify the two charts by an invertible transition.
It first enforces integrality by annihilating the nonintegral rational modes,
then smooths the admitted integer sector.

## What selects this bridge

Packet 100 allowed arbitrary positive trace-class multipliers `g(A_Phi)`.
The present operator is more rigid because it is derived before spectral
functional calculus from simultaneous local source conditions:

1. the Gaussian vacuum at the real place;
2. the compact-open vacuum `1_Zp` at every finite place;
3. restricted-product factorization;
4. Fourier self-duality with the global additive character;
5. periodization along the diagonal rational lattice.

These conditions explain both parts of the spectrum: the finite vacua impose
the exact arithmetic projector, while the real vacuum supplies the heat
weight.  This removes the static multiplier ambiguity only relative to this
specified adelic source packet; uniqueness under a larger class of
self-Fourier Schwartz--Bruhat sources is not claimed.

## Dilation and the modular family

For `t>0`, replace the real Gaussian by

\[
 f_{\infty,t}(x)=e^{-\pi t x^2}.
\]

Its Fourier transform is

\[
 \widehat f_{\infty,t}(\xi)
 =t^{-1/2}e^{-\pi\xi^2/t}.
\]

The trace of the periodized convolution is therefore

\[
 \operatorname{Tr}K_t
 =t^{-1/2}\sum_{n\in\mathbb Z}e^{-\pi n^2/t}
 =\sum_{n\in\mathbb Z}e^{-\pi t n^2},
\]

where the last equality is adelic Poisson sewing.  The Mellin transform of
this trace family, after separating the zero mode and retaining endpoint
terms, is the standard route to the completed zeta function.  The modular
parameter is therefore source-derived; it is not an arbitrary heat time.

## Geometric-algebra interpretation

The two Clifford charts of packet 99 contain complementary localizations:
currents in one chart and distributional charges in the other.  `K_f` is a
typed cross-chart correspondence with a large, meaningful kernel.  The pure
spinor incidence relation from packet 97 is not lost; the finite adelic
vacuum selects exactly the integral sublattice on which that relation can be
read by the real Gaussian channel.

This makes the operator's earlier intuition precise:

\[
 \boxed{
 \text{failure of integrality}
 \;=\;
 \text{membership in the kernel of the completed adelic bridge}.}
\]

That statement concerns source admissibility, not zeros of `Xi`.  A theta
zero would have to arise later, from loss of transversality inside the
surviving integral sector after the dilation/Mellin comparison.

## Scope and falsifier

This packet proves a canonical theta-producing nuclear bridge and identifies
its kernel.  It does **not** construct a self-adjoint operator with Riemann-zero
spectrum, prove off-seam coercivity, or prove RH.

The next falsifier is exact: construct a different factorized adelic source
obeying the same five local conditions above whose periodized convolution is
not `K_f`.  If one exists, the claimed source-level uniqueness fails.  If the
conditions do determine `f`, the remaining RH question is no longer bridge
selection but orientation of the Mellin-transformed integral sector.

## Reference normalization

This uses the standard Tate normalization: the rational adeles are
self-dual, `Q` is its own annihilator, the Gaussian and `1_Zp` local vacua are
Fourier-fixed, and adelic Poisson summation produces the theta functional
equation.  See the [Warwick Tate-thesis notes](https://warwick.ac.uk/fac/sci/maths/people/staff/sheth/tatesthesis_notes.pdf)
and the [Abel Prize account of Tate's work](https://abelprize.no/sites/default/files/2021-09/The%20Abel%20Prize%202008-2012_Full_.pdf).

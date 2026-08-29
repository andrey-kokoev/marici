# The adelic vacuum supplies a canonical trace-class sandwich after wall removal

## Ideal-class problem

After coefficient-space wall subtraction, the represented regular part is generally a bounded multiplication operator

\[
M_r
\]

on a non-atomic analytic \(L^2\) space. Unless \(r=0\), this operator is not compact.

Therefore a Fredholm object requires an independently source-derived smoothing correspondence.

## Existing source bridge

The completed Tate source supplies the factorized Schwartz–Bruhat vacuum

\[
f(x)
=
e^{-\pi x_\infty^2}
\prod_p1_{\mathbb Z_p}(x_p).
\]

After periodization on

\[
G=\mathbb A/\mathbb Q,
\]

convolution by its periodized kernel gives a positive trace-class operator \(K_f\).

On the character basis indexed by \(r\in\mathbb Q\),

\[
K_f\chi_r
=
\begin{cases}
e^{-\pi r^2}\chi_r,&r\in\mathbb Z,\\
0,&r\notin\mathbb Z.
\end{cases}
\]

Thus \(K_f\) performs two source-authorized operations:

1. projection onto the integral character sector;
2. Gaussian nuclear smoothing on that sector.

It is not an arbitrary spectral multiplier.

## Canonical sandwich

For any bounded represented regular operator \(R\), define

\[
\mathcal T_f(R)
=
K_f^{1/2}RK_f^{1/2}.
\]

Because \(K_f^{1/2}\) is Hilbert–Schmidt,

\[
\mathcal T_f(R)\in\mathcal S_1,
\]

and

\[
\|\mathcal T_f(R)\|_1
\le
\|R\|\,
\|K_f^{1/2}\|_2^2
=
\|R\|\operatorname{Tr}K_f.
\]

Therefore the source already contains a canonical route from a bounded wall-regularized operator to a trace-class operator.

## Correct order

The admissible order is

\[
\text{coefficient wall split}
\to
\text{quadratic multiplication representation}
\to
\text{bounded regular operator}
\to
\text{adelic vacuum sandwich}
\to
\text{trace-class object}.
\]

Sandwiching before wall removal also produces trace class, but it hides the identity residue inside regulator data and does not prove the source wall theorem.

## Faithfulness warning

The vacuum bridge has a large kernel:

\[
\ker K_f
=
\overline{\operatorname{span}}
\{\chi_r:r\in\mathbb Q\setminus\mathbb Z\}.
\]

Hence \(\mathcal T_f\) is not faithful on the full rational character space.

The first Adams incidence uses prime and prime-square labels, which are integral. This makes survival plausible, but the exact theorem must show that the complete mixed-incidence subspace lies in the surviving integral sector before sandwiching.

The gate is

\[
\ker K_f
\cap
\mathcal V_{\mathrm{mix}}
=
\{0\}.
\]

A labelled prime origin alone is insufficient if the comoving, reciprocal, or Green constructions generate nonintegral rational modes.

## Lower-frame issue

Trace-class smoothing strongly suppresses high integral modes:

\[
e^{-\pi n^2}\to0.
\]

Thus no uniform lower bound holds on the entire infinite integral sector. The sandwich is excellent for determinant typing but cannot itself provide completion-stable observability.

The programme must keep two geometries separate:

- the unsmoothed relative Green form for coercive or frame estimates;
- the vacuum-sandwiched trace-class form for determinant construction.

Using the smoothed norm to prove observability would create another vanishing-detector problem.

## Determinant authorization

For fixed source vacuum normalization,

\[
D_R(\lambda)
=
\det\left(I+\lambda\mathcal T_f(R)\right)
\]

exists.

But existence does not identify this determinant with the completed zeta or Xi section. The required comparison remains:

1. compute its logarithmic derivative from labelled source blocks;
2. recover primitive, square, connected, seam, and archimedean currents;
3. prove compatibility with modular dilation;
4. show the comparison unit with the independent completed section is nowhere zero.

## Dilation family

The source also supplies a modular Gaussian family \(K_t\). Each positive \(t\) yields trace-class smoothing, but determinants may depend on \(t\).

The self-dual point \(t=1\) is source-distinguished after Haar and Fourier normalizations, yet source self-duality alone does not prove RH relevance. A regulator-independent relative determinant or exact modular comparison is still required.

## Minimal hostiles

### Unsmoothed Fredholm claim

A nonzero multiplication remainder is called compact after wall removal.

### Arbitrary heat sandwich

A convenient trace-class multiplier is inserted without deriving it from the Tate vacuum.

### Kernel loss

The mixed incidence has a component in a nonintegral rational mode annihilated by \(K_f\).

### Smoothed observability

The Gaussian-suppressed determinant norm is used as a uniform lower-frame estimate.

### Determinant identification by fitting

The spectral parameter is chosen from Xi after the determinant is formed.

## Current frontier

The ideal-class problem has a source-native candidate solution:

\[
R
\longmapsto
K_f^{1/2}RK_f^{1/2}\in\mathcal S_1.
\]

The next exact calculation is to intertwine the wall-regularized Adams history with the adelic vacuum bridge and prove that the mixed-incidence subspace survives its integrality projector. Only then is a Fredholm determinant typed without inventing smoothing.

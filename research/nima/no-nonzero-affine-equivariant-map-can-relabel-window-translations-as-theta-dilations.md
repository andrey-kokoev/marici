# No nonzero affine-equivariant map can relabel window translations as theta dilations

The affine-group law upgrades the residual from event 10312 to an exact no-go
theorem.

## Source affine representation

Use

\[
(T_bf)(x)=f(x-b),
\qquad
(D_af)(x)=a^{1/2}f(ax),
\qquad a>0.
\]

These satisfy

\[
D_aT_bD_a^{-1}=T_{b/a}.
\]

The adjacent-window fronts lie in the additive translation orbit of the
Gaussian.

## Proposed direct relabelling

A direct window-to-theta relabelling would send additive displacement \(b\)
to logarithmic theta displacement, equivalently to multiplicative dilation:

\[
KT_b=D_{e^b}K.
\]

To preserve the already authorized scale action, it would also satisfy

\[
KD_a=D_aK.
\]

These two laws cannot hold nontrivially on an affine cyclic packet.

## Semidirect contradiction

Intertwine the source relation:

\[
K D_aT_bD_a^{-1}
=
K T_{b/a}.
\]

Using scale equivariance and the proposed translation-to-dilation rule, the
left side becomes

\[
D_aD_{e^b}D_a^{-1}K.
\]

Dilations commute, so

\[
D_aD_{e^b}D_a^{-1}K
=
D_{e^b}K.
\]

The right side is

\[
D_{e^{b/a}}K.
\]

Therefore

\[
\left(D_{e^b}-D_{e^{b/a}}\right)K=0
\]

for every \(a>0\) and \(b\in\mathbb R\).

For \(a\ne1\) and \(b\ne0\), the two dilation parameters differ. On any
dilation-faithful theta cyclic subspace their equalizer is zero. Hence

\[
K=0.
\]

Thus no nonzero comparison can simultaneously preserve source scale,
relabel additive translation as theta dilation, and respect affine
composition.

## Consequence

The missing comparison is not an ordinary natural transformation between the
window and theta representations. It must change representation type through
an additional constructor.

The admissible possibilities are narrower:

1. lattice sampling or periodization followed by Poisson summation;
2. an affine-to-Mellin integral transform retaining a continuous spectral
   parameter;
3. induction through a larger representation carrying both Heisenberg and
   Mellin actions;
4. a correspondence or bimodule rather than a single intertwining map.

A scalar or finite matrix \(K\) on the current packets cannot perform this
change while preserving all source operations.

## Why Fourier alone is insufficient

Fourier gives

\[
\mathcal FT_b\mathcal F^{-1}
=
M_{e^{-2\pi ib\xi}},
\]

so translation becomes modulation. Mellin transport diagonalizes dilation.
A Fourier-to-Mellin bridge still requires a change from additive characters
to multiplicative characters. That change is an integral kernel or
Poisson/lattice correspondence, not equality of the two actions.

## Smallest hostile

Take one Gaussian \(f_0\), one \(a\ne1\), and one \(b\ne0\). Compare the two
source-equal words

\[
D_aT_bD_a^{-1}f_0
\quad\text{and}\quad
T_{b/a}f_0.
\]

A proposed direct relabelling gives target words

\[
D_{e^b}Kf_0
\quad\text{and}\quad
D_{e^{b/a}}Kf_0.
\]

They differ whenever \(Kf_0\) is dilation-faithful. This four-word packet is
the minimal categorical falsifier.

## Revised frontier

The next source extraction must locate the actual representation-changing
constructor in the theta/Poisson grammar. It must specify:

- its source and target riggings;
- whether it is a map, relation, or bimodule;
- lattice-comb authority;
- normalization of additive and multiplicative Haar measures;
- treatment of the zero-mode wall;
- compatibility with the three completion-Jordan grades;
- endpoint and reflection behavior.

Only after that constructor exists can Kitaev's finite jet intertwiner be
posed on its essential image.

No mixed Green form, Adams edge, or boundary pencil is promoted.

## Source locators

- research/nima/additive-window-translation-does-not-intertwine-the-multiplicative-theta-label-orbit.md
- research/nima/additive-differentiation-is-the-source-incidence-between-even-and-odd-tate-ports.md
- research/nima/the-window-to-seam-comparison-must-pass-through-theta-completion.md
- research/nima/the-first-theta-label-completion-packet-has-three-explicit-jordan-grades-and-zero-wall-image.md

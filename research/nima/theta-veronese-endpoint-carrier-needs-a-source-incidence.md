# The Veronese Endpoint Carrier Needs a Tate Source Incidence

## Six dimensions do not determine the sewing type

The first nontrivial endpoint grade is

\[
H_1\cong\operatorname{Sym}^2\mathbb C^2,
\qquad
\dim H_1=3.
\]

One possible reciprocal carrier has dimension six:

\[
V_1=H_1^+\oplus H_1^-.
\]

But another inequivalent six-dimensional graded carrier is

\[
H_0\oplus H_2,
\qquad
1+5=6.
\]

Therefore Aspect's $6\times6$ experimental fixture cannot be typed from its
dimension.  The decomposition $H_1^+\oplus H_1^-$ is a candidate only if
the source basis and sewing maps preserve the two reciprocal grade-one
blocks.  A unit-plus-grade-two packet has different constructors and
coherence laws.

Any declared decomposition must remain distinguished until the completed
sewing map is applied.  Treating the six coordinates as an untyped Euclidean
vector erases the grade and endpoint incidences needed to choose between
these carriers.

## Fourier action on the grade-one carrier

Let the spinor quarter-turn act by

\[
J(u)=v,
\qquad
J(v)=-u.
\]

On $H_1$,

\[
u^2\mapsto v^2,
\qquad
uv\mapsto-uv,
\qquad
v^2\mapsto u^2.
\]

Hence the induced action has eigenvalue multiplicities

\[
m_+=1,
\qquad
m_-=2.
\]

The even Veronese representation sees an involution rather than the full
order-four spinor rotation because

\[
\operatorname{Sym}^{2}(-I)=I.
\]

Thus a grade-one source incidence can land only in the Fourier-even sector
with eigenvalues $+1$ and $-1$.  It cannot by itself represent the odd
$\pm i$ Fourier sectors carried by the full archimedean boundary cell.

## Formal Fourier embeddings are noncanonical

The real Hermite functions provide infinitely many Fourier eigenvectors with
the required signs.  One can choose three even Hermite functions with one
positive and two negative Fourier eigenvalues and thereby construct a linear
intertwiner

\[
H_1\longrightarrow\mathcal S(\mathbb R).
\]

But there are infinitely many such choices.  Fourier intertwining alone does
not select one, and a generic choice does not intertwine the Cartan
grade-changing constructors

\[
H_l\longrightarrow H_{l+1}.
\]

Consequently an arbitrarily selected Hermite triple would produce a unitary
optical control of exactly the kind prohibited by Aspect's source-map
contract.  It would not be a source-derived theta sewing basis.

## Representation mismatch

The full Veronese tower is the homogeneous two-mode spinor algebra

\[
\bigoplus_{l\ge0}\operatorname{Sym}^{2l}\mathbb C^2.
\]

A canonical oscillator realization uses two creation modes and fixed total
occupation $2l$.  The current one-dimensional Tate source has archimedean
space $\mathcal S(\mathbb R)$, whose ordinary oscillator energy levels are
one-dimensional.  It does not contain the multiplicities $2l+1$ as
canonical energy eigenspaces.

The reciprocal pair of Tate sectors is a candidate two-mode source, but this
requires a new theorem.  The two sectors are related localizations of one
source and cannot be promoted to independent oscillator modes merely to fit
the Veronese dimension count.

## Canonical boundary-Fock incidence

The external five-cell supplies a source-derived two-dimensional boundary
plane

\[
P_\partial=\operatorname{span}\{1,\delta_0\},
\]

with Fourier exchange

\[
\mathcal F1=\delta_0,
\qquad
\mathcal F\delta_0=1.
\]

This constructs a canonical algebraic incidence

\[
\jmath_l:H_l\longrightarrow\operatorname{Sym}^{2l}P_\partial
\]

by sending the two spinor generators to the ordered constant and delta ports.
Symmetric multiplication then intertwines the Cartan grade constructors
automatically.  The two Veronese extremals become the pure constant and pure
delta tensors, while mixed monomials retain their relationship incidence.

This corrects the earlier target.  The Veronese grade does not naturally land
in the one-particle trace range.  It lands in the even symmetric Fock algebra
of an external rigged boundary plane:

\[
\bigoplus_{l\ge0}H_l
\longrightarrow
\bigoplus_{l\ge0}\operatorname{Sym}^{2l}P_\partial.
\]

The constant and delta ports are not ordinary $L^2$ states and cannot be
inserted into the tail graph domain.  Their symmetric powers remain boundary
objects.

## Remaining trace-sewing lift

Aspect's algebraic sewing map is currently defined on the injective trace
range of Schwartz--Bruhat sources.  The boundary-Fock incidence requires a
rigged extension

\[
\tau_\partial:
\operatorname{Sym}^{\mathrm{even}}P_\partial
\longrightarrow
\mathcal T'_\partial
\]

and an induced sewing action compatible with Fourier exchange and symmetric
multiplication.  Neither $1$ nor $\delta_0$ can be presented as a finite
ordinary source basis vector without a declared approximation and completion
law.

There is also a phase gate.  Fourier acts involutively on the constant--delta
plane.  The spinor quarter-turn squares to $-I$.  On grade $l$, the two
actions differ by a possible grade character $(-1)^l$.  A metaplectic phase
or equivalent normalization must be source-derived before identifying these
actions.

## Exact grade-one algebraic fixture

Use the normalized symmetric basis

\[
c^2,
\qquad
\sqrt2\,c d,
\qquad
d^2,
\]

where $c=1$ and $d=\delta_0$.  The unphased Fourier exchange has matrix

\[
B_1=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix}.
\]

It satisfies

\[
B_1^*=B_1,
\qquad
B_1^2=I.
\]

Multiplying the spinor Fourier action by the metaplectic phase $i$ changes
the grade-one symmetric-square action to $-B_1$.  This has the
one-positive, two-negative eigenvalue multiplicity of the spinor
quarter-turn convention.

If the six-dimensional carrier is explicitly declared to be
$H_1^+\oplus H_1^-$, the reciprocal exchange candidate is

\[
\mathbb J_1=
\begin{pmatrix}
0&B_1\\
B_1&0
\end{pmatrix}.
\]

Then

\[
\mathbb J_1^*=\mathbb J_1,
\qquad
\mathbb J_1^2=I.
\]

This matrix is derived from the declared boundary-plane exchange rather than
chosen from the discrete Fourier group.  It is a valid algebraic positive
fixture for the sewing compiler.  It is not a physical finite source map:
the vectors $1$ and $\delta_0$ remain rigged boundary distributions, and
the metaplectic grade phase still requires source authority.

## Metric and uncertainty gate

If a rigged trace-sewing lift exists, its source Gram or pairing matrices are

\[
G_l^\pm=(\tau_\partial\jmath_l^\pm)^*
G_{\partial,\pm}(\tau_\partial\jmath_l^\pm).
\]

Completed sewing must be tested using the block metric

\[
G_l=G_l^+\oplus G_l^-.
\]

The native residual is

\[
J_l^*G_lJ_l-G_l,
\]

not $J_l^*J_l-I$ unless a preregistered whitening has already been applied.
If $G_l$ is experimentally estimated, its calibration error must enter the
uncertainty compiler independently of the map-entry error and systematic map
bias.

The current Aspect threshold is therefore authoritative only for a frozen
normalized frame with an exact or separately bounded Gram calibration.

## Finite DPC

At grade one, the route passes only if all of the following are supplied
before science outcomes:

1. a declared six-dimensional grade decomposition rather than a dimension-only
   basis;
2. the boundary-Fock incidence from the constant--delta plane;
3. a rigged trace extension on the resulting symmetric tensors;
4. exact or preregistered Fourier matrices in those typed coordinates;
5. the source pairing blocks and their calibration bounds;
6. the metaplectic grade phase;
7. one grade-change naturality square linking $H_0$, $H_1$, and $H_2$.

The last gate rejects isolated Fourier-compatible triples that do not belong
to the Veronese tower.

## Result

The even Veronese theorem supplies a canonical boundary-Fock algebra over the
constant--delta control plane.  It does not uniquely type Aspect's
six-dimensional fixture, and it does not embed those boundary distributions
into the ordinary Schwartz--Bruhat trace range.  The missing constructor is a
grade-natural rigged trace-sewing lift of the symmetric boundary algebra.

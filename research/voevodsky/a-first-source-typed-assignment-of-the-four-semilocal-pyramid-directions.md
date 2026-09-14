# A first source-typed assignment of the four semilocal pyramid directions

## Principle

The four tetrahedral vertices should be four presentations of the **same finite-stage semilocal functional**, not four sequential operations. Edges are comparison maps between presentations; triangular faces assert compatibility of three comparisons.

Fix a finite place/conductor stage `S`.

## Vertex assignment

### `V_1`: source test/polarization presentation

Let

\[
V_1(S)=
\mathcal A_S,
\]

where `A_S` is the test-function convolution `*`-algebra on the semilocal idele class group, together with convolution-square observers

\[
h=g*g^*.
\]

This is the source presentation from which the Weil functional is evaluated.

### `V_2`: semilocal geometric presentation

Let

\[
V_2(S)=
\left(
L^2(X_S)^{K_S},
U_S,
F_S
\right).
\]

It contains:

- the semilocal adele-class Hilbert space;
- the unitary scaling representation `U_S`;
- the semilocal Fourier transform `F_S`;
- the physical and Fourier cutoff projections.

### `V_3`: dual/canonical spectral presentation

Let

\[
V_3(S)=
\left(
H_S^+,
H_S^-,
J_S,
D+V_{loc,S}
\right).
\]

Here:

- `H_S^plus-or-minus` are the dual and canonical Hardy--Titchmarsh weighted spaces;
- `J_S` is their unimodular Euler--gamma pairing phase;
- its logarithmic derivative is the local Weil connection.

### `V_4`: cutoff-trace presentation

Let

\[
V_4(S)=
\left(
P_\Lambda,
\widehat P_\Lambda,
R_\Lambda=P_\Lambda\widehat P_\Lambda,
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}(R_\Lambda U_S(-))
\right).
\]

Connes's Theorem 4 identifies this finite-part trace with the sum of local Weil distributions for the places in `S`.

`V_4` is a signed trace presentation, not yet the positive apex. Positivity belongs to an additional filler or completed observation.

## Six conductor edges

### `C_12`: source to semilocal geometry

\[
C_{12}:
\mathcal A_S
\longrightarrow
(L^2(X_S)^{K_S},U_S),
\qquad
g\longmapsto U_S(g).
\]

For convolution squares,

\[
U_S(g*g^*)
=
U_S(g)U_S(g)^*.
\]

Status: **source-defined and positive at the representation level**.

### `C_13`: source to spectral duality

\[
C_{13}:
g
\longmapsto
(\Omega_S^+g,
\Omega_S^-g).
\]

Its relative scattering operator is

\[
(\Omega_S^+)^*
\Omega_S^-
=M_{J_S^{-1}},
\]

and differentiating its phase gives the gamma--prime current.

Status: **constructed from the canonical/dual Hardy--Titchmarsh transforms**.

### `C_14`: source to local Weil finite part

\[
C_{14}:
h
\longmapsto
W_S(h).
\]

Equivalently,

\[
W_S(h)
=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h)).
\]

Status: **Connes semilocal Theorem 4**.

### `C_23`: semilocal geometry to spectral presentation

\[
C_{23}:
L^2(X_S)^{K_S}
\longrightarrow
H_S^\pm
\]

is given by the canonical and dual Hardy--Titchmarsh transforms.

Status: **unitary/two-space source theorem**.

### `C_24`: semilocal geometry to cutoff trace

\[
C_{24}:
(U_S,F_S)
\longmapsto
P_\Lambda F_SP_\Lambda F_S^{-1}U_S(-).
\]

This constructs the operator whose trace appears in Theorem 4.

Status: **source-defined**, with trace asymptotics supplied by Theorem 4.

### `C_34`: spectral connection to cutoff finite part

This edge should compare

\[
\frac1{2i}
\partial_s\log J_{loc,S}(s)
\]

with the normalized local principal-value distributions obtained from the cutoff trace.

Status: **local distributionally expected and formally matched prime by prime, but the complete operator intertwiner with the cutoff/Prolate presentation is not yet constructed**.

This is currently the least complete conductor edge.

## Four triangular faces

### Face `123`

Semilocal amplification followed by the Hardy--Titchmarsh transform must equal the direct spectral transform of the source observer:

\[
C_{23}C_{12}
\Rightarrow
C_{13}.
\]

Status: supplied by the commutative diagrams in Propositions 4.3 and 4.7.

### Face `124`

Representing the source observer geometrically and then applying the cutoff trace must equal the direct Weil finite-part functional:

\[
C_{24}C_{12}
\Rightarrow
C_{14}.
\]

Status: supplied asymptotically by Connes's Theorem 4.

### Face `134`

Differentiating the spectral pairing phase and passing to its principal-value observation must equal the source Weil functional:

\[
C_{34}C_{13}
\Rightarrow
C_{14}.
\]

Status: local formulas match, but the completed operator-level face is open.

### Face `234`

The cutoff trace transported through the Hardy--Titchmarsh presentation must equal the trace/connection observation in spectral variables:

\[
C_{34}C_{23}
\Rightarrow
C_{24}.
\]

Status: this is the missing spectral--cutoff intertwining face.

## Inner tetrahedral filler

The inner filler asserts that the two proofs from `V_1` to `V_4` agree:

\[
C_{24}C_{12}
\simeq
C_{34}C_{23}C_{12}
\simeq
C_{34}C_{13}
\simeq
C_{14}.
\]

Its coherence equation compares the homotopy through faces `123` and `134` with the homotopy through faces `124` and `234`.

This is the first precise form of the central missing filler.

## Polarity

The opposite tetrahedron exchanges:

\[
H_S^+
\leftrightarrow
H_S^-,
\]

\[
J_S
\leftrightarrow
J_S^{-1},
\]

\[
P_\Lambda\widehat P_\Lambda
\leftrightarrow
\widehat P_\Lambda P_\Lambda.
\]

The source and semilocal geometric vertices remain fixed up to adjoint/opposite-category structure. The two tetrahedra must meet in the Hermitian polarization of `W_S`.

## Important limitation

A barycentric lattice node

\[
X_{a_1a_2a_3a_4}
\]

cannot yet be interpreted merely as “`a_i` copies of presentation `V_i`.” A concrete edgewise-subdivision functor must specify how repeated elementary transfers compose. Until then, the four vertex assignments and six edge comparisons are typed, but the 120 interior nodes are only combinatorial placeholders.

## Disposition

The first source-backed assignment is

\[
\boxed{
V_1=
\text{test/polarization},
\quad
V_2=
\text{semilocal geometry},
\quad
V_3=
\text{dual/canonical spectrum},
\quad
V_4=
\text{cutoff finite-part trace}.
}
\]

Three faces are source-backed at least distributionally; the decisive missing data are concentrated in `C_34` and face `234`, the spectral--cutoff/prolate comparison. A positive rung-four apex remains an additional filler beyond the signed trace vertex.

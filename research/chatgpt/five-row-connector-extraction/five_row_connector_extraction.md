# Five incoming connector rows: extraction and graded evaluation

Date: 2026-09-06  
Branch: A  
Pinned Marici commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and limits

The five-row **target extraction** is completely determined. The complete
normalization-to-PC connector matrix is not supplied by the inspected
integration, uniqueness, operator-descent, or normalized-blowdown checkers.
Accordingly no value is assigned to its missing full-source rows.

There is nevertheless a new forced evaluation. For any occurrence-homogeneous
connector in the independent-normal model, all five rows vanish on the
three-face D03 normalization sector of degree

\[
\sigma=\epsilon_{35}-\epsilon_{03}.
\]

In words: the source sector has occurrence weight minus one in the D03
coordinate, whereas every selected incoming target state has weight zero
there. The coefficient ring has no negative occurrence powers.

Consequently the radial composite is literally zero on this sector, and the
mixed operator has the already coefficient-legal, endpoint/Q-relative local
nullhomotopy there. This is not a calculation of its value on every generator
of the uncollapsed normalization source.

## 1. Fixed coefficient model

Let \(\mathcal D\) be the nine diagonals of the labelled hexagon and let

\[
R=\mathbb Z[X_d,u_d:d\in\mathcal D].
\]

For a noncrossing set \(F\) and a marked subset \(H\subseteq F\), the
coefficient module of \(e_{F,H}\) is

\[
R[u_d^{-1}:d\in F\setminus H].
\]

Its homological degree is \(3-|F|+|H|\). The differential has the source's
radial coefficients \(X_d/u_d\), normal coefficients one, and fixed
incidence/exterior signs. Remove the two complete endpoint packets to obtain
\(E\). Original indices in the 215-generator enumeration are retained in
the certificate; \(E\) itself has 199 generators.

Set \(a=03\), \(b=13\), \(c=04\), and \(d=35\). With the ordered exterior
contractions, define

\[
T_{ab}=\frac1{u_au_b}\iota_b\iota_a.
\]

The local homotopy is

\[
H_{ab}e_{F,H}
=
\frac{(-1)^{3-|F|}}{u_au_b}\iota_b e_{F,H}
\]

when \(a\in F\setminus H\) and \(b\in H\), and zero otherwise. The radial
operator is defined by the computed commutator

\[
\mathcal R_{ab}=d_EH_{ab}+H_{ab}d_E-T_{ab}.
\]

In words: this definition derives the residual columns from the full
source-signed differential, rather than entering the desired five rows as
an assumed map.

## 2. Extracted rows and exact composite

Write

\[
v=\frac{X_{03}}{u_{03}^2u_{13}}.
\]

Let \(s_i\) and \(t_i\) be the following incoming and outgoing basis states.

| i | Incoming state s_i | Degree | Outgoing state t_i | Coefficient |
|---|---|---:|---|---:|
| 1 | [{13},{13}] | 3 | [{03,13},empty] | -v |
| 2 | [{04,13},{13}] | 2 | [{03,04,13},empty] | +v |
| 3 | [{04,13},{04,13}] | 3 | [{03,04,13},{04}] | -v |
| 4 | [{13,35},{13}] | 2 | [{03,13,35},empty] | +v |
| 5 | [{13,35},{13,35}] | 3 | [{03,13,35},{35}] | +v |

For a degree-zero chain map \(\kappa:\mathcal S\to E\), define its actual
row maps by

\[
K_i=\operatorname{coeff}_{s_i}\kappa.
\]

Then, without any additional assumption about \(\kappa\),

\[
(\mathcal R_{03,13}\kappa)(z)
=v\left(-K_1(z)t_1+K_2(z)t_2-K_3(z)t_3
       +K_4(z)t_4+K_5(z)t_5\right).
\]

In words: the expression is an exact five-row matrix multiplication. The
five output states are different. Each permitted coefficient localization
is a domain and multiplication by \(v\) is injective. Thus strict vanishing
is equivalent to all five row maps being zero. This criterion concerns
strict maps, not the weaker question of vanishing of a homotopy class.

## 3. The five rows form a quotient complex

Projection onto these five states is a chain map; no discarded state has a
differential term entering the selected states. In the order
\((s_1,s_3,s_5)\) in degree three and \((s_2,s_4)\) in degree two, its
quotient complex is

\[
U_3=R^3,
\qquad
U_2=R[u_{04}^{-1}]\oplus R[u_{35}^{-1}],
\]

\[
d_U=
\begin{pmatrix}
X_{04}/u_{04}&-1&0\\
-X_{35}/u_{35}&0&1
\end{pmatrix}.
\]

In words: the complete row extraction is a map \(\mathcal S\to U\), not
five unrelated scalar choices. Its chain equations include

\[
K_2d_{\mathcal S}
=\frac{X_{04}}{u_{04}}K_1-K_3,
\qquad
K_4d_{\mathcal S}
=-\frac{X_{35}}{u_{35}}K_1+K_5.
\]

The three degree-three rows also vanish on source boundaries from degree
four. These equations still require the actual source differential and row
values before they determine a full composite.

The output states also form a subcomplex. The radial map factors as this
quotient projection followed by the displayed signed multiplication map,
with the appropriate homological shift by minus two.

## 4. Evaluation forced by the source's fixed multidegree

Entries 386 and 387 independently give the common degree of the three
normalized source combinations

\[
H_{\rm Morse}p,\qquad q_Jp,\qquad
(d\widetilde\xi)h_3
\]

as \(\sigma=\epsilon_3-\epsilon_{D03}\). Here the repository's short
label \(x_3\) means the diagonal \(35\). Its target occurrence weights are

\[
\deg_X e_{F,H}=-\sum_{f\in F}\epsilon_f.
\]

The marked set changes normal grading, not occurrence grading. If \(z\)
has degree \(\sigma\), a coefficient in its \(s_i\) image would need degree

\[
\deg_X K_i(z)=\sigma+\sum_{f\in F_i}\epsilon_f.
\]

All five \(F_i\) omit \(03\). Therefore

\[
\left(\deg_X K_i(z)\right)_{03}=-1.
\]

Every allowed coefficient is polynomial in the occurrence variables. No
normal localization changes that condition. Hence, for each of the five
rows,

\[
K_i(z)=0.
\]

Explicitly, the needed occurrence degrees are:

| Rows | Required occurrence degree |
|---|---|
| 1 | -epsilon_03 + epsilon_13 + epsilon_35 |
| 2,3 | -epsilon_03 + epsilon_04 + epsilon_13 + epsilon_35 |
| 4,5 | -epsilon_03 + epsilon_13 + 2epsilon_35 |

Thus

\[
(\mathcal R_{03,13}\kappa)|_{\mathcal S_\sigma}=0.
\]

In words: the radial defect is zero on the fixed homogeneous normalization
sector. This is derived from source grading, not assigned by copying a
signature or setting missing rows to zero.

The homogeneous piece is a subcomplex because the differential preserves
occurrence degree. On it, the previously defined homotopy gives

\[
d_E(H_{ab}\kappa)+(H_{ab}\kappa)d_{\mathcal S}
=T_{ab}\kappa.
\]

The actual target boundary map \(\rho=(\pi_Q,\kappa_+,\kappa_-)\) obeys
\(\rho H_{ab}=0\). Therefore this nullhomotopy preserves the retained
endpoint and Q components in the tested coefficient category. This is not
an assertion of additional raw six-functor/source-relative admissibility.

The same grading argument applies to any specified source generator whose
03 occurrence weight is negative. It does not apply automatically to every
source generator. In particular, the normalization combinations in Entry
386 need not form a basis of the complete uncollapsed normalization object.
Nor does this calculation identify a Rees parameter of negative occurrence
weight with an independent normal coefficient.

## 5. Why the full row extraction is not available from the inspected code

The following complete files were inspected at the pinned commit.

* `check_global_mixed_variance_transform.py` records a scalar signature and
  compares it with `dict(transform_signature)`. It defines no generator map
  into the loaded PC basis.
* `check_cellular_log_kernel_framed_identification.py` compares two signature
  dictionaries. Its local deformation and automorphism ranks are assigned
  as previously claimed inputs; it does not build the relevant Hom matrices
  or the five row functionals.
* `check_global_cartier_operator_descent.py` constructs the augmented
  three-chart nerve and its contraction. Its local operator commutators are
  inserted as zeros; the actual mixed-normal matrix is not included.
* `check_d03_normalized_blowdown_counit.py` gives an explicit map of loaded
  barycentric flags and verifies the Morse identity. Its basis is a flag
  of faces with occurrence coefficients, not the normal-marked PC basis
  \([F,H]\). It does not supply the comparison that converts a circled
  incoming corridor into the five states used above.

The finite-to-Cech map, a normal-chart isomorphism, and the scalar endpoint
matrix cannot be substituted for the complete normalization-derived
\(\kappa\). They have different domains or omit the required normal and
incidence components.

Consequently the certificate uses `null` for each full physical connector
row and for the complete composite. Zero is used only for the rigorously
identified homogeneous sector.

## 6. Controls

The checker reconstructs the 215 target states and 522 differential arrows,
then works in the 199-state endpoint quotient. It verifies the differential,
secondary map, radial commutator, five-row quotient, output subcomplex,
permitted localizations, and the complete target boundary restrictions.

Two negative controls prevent overinterpreting the zero result.

First, if the source occurrence degree equals that of a selected PC state,
the corresponding identity coefficient is legal and nonzero. Thus the
multigrading test does not prove the target operator or every connector
zero.

Second, an explicit contractible two-generator source supplies a nonzero
five-row chain map whose endpoint and Q images are all zero. Its radial
composite is nonzero as a chain map but has a boundary-relative primitive.
This shows both that boundary readouts alone do not recover chain-level
rows and that strict nonzero rows do not establish nonzero derived action.
This control is not claimed to preserve the physical source's fine degree
or additional source-specific structures.

The standalone run completed 1,610 exact assertions. No run is claimed for
an unavailable full normalization connector matrix.

## Sources

Marici, pinned commit listed above:

1. `research/voevodsky/check_ringed_alexandrov_pc_target.py`.
2. `src/ledger/20260817-386 The Three-Face Source Has One Common Shift.md`.
3. `src/ledger/20260817-387 The Literal Incidence Shift Kills the Endpoint Hom.md`.
4. The four audited scripts named in Section 5.

Prior calculation in this session:

* `mixed_connector_normal_variation.md`.
* `check_mixed_connector_normal_variation.py`.

Stacks Project, Hom complexes, tag 0A8H, gives the mapping differential and
composition signs. Derived hom, tag 0A5W, explains the bounded-projective
source requirement for interpreting ordinary Hom computations as derived
Hom. Neither theorem supplies missing source-to-target coefficients.

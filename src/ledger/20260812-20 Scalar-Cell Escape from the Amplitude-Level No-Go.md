# Scalar-Cell Escape from the Amplitude-Level No-Go

## Record

Date: 2026-08-12

Status: the summed scalar amplitude and its Laurent-leading coefficient provably underdetermine
the QTDS polarity homotopy. The canonical scalar cubic-tree presentation retains more information
and yields an exact six-point escape: QTDS is the unique alternating local redistribution of two
parity-central scalar grade cells among three quadrangulation fibers. Entry 21 promotes this to a
genuine presentation-cellular tripod lift. At eight points, parity-core cells form a Möbius
carrier whose boundary is the unresolved octagon. The octagonal coherence and scalar-to-twisted
comparison remain open.

## Correction to the normal-language shorthand

For a fixed cyclic order \(\alpha\), define

\[
F_{\alpha,+}(X,t)
=
A^{\operatorname{Tr}\Phi^3}
\left(
X+\frac{\sigma^\alpha}{t}
\right),
\qquad
t=\delta^{-1},
\]

where \(\sigma^\alpha\) gives opposite shifts to even-even and odd-odd planar variables and leaves
odd-even variables unshifted. At six points,

\[
F_{\alpha,+}(X,t)
=
t^4a_{R,6}(\alpha;X)+O(t^5).
\]

The opposite alternating coloring is \(t\mapsto-t\), so it has the same fourth initial
coefficient.

This supplies a valid \(t\)-adic initial form. By itself it does **not** define:

- a kinetic bundle map whose rank jumps;
- a stratified parameter space \(B_6\) and rank locus \(R_6\);
- a constructible or filtered scalar chain complex near \(t=0\);
- Verdier specialization of such a complex.

Accordingly, “rank-jump associated grade” remains Marici's physical-geometric interpretation of
the scalar large-mass limit. At chain level the established source object is presently a Rees or
Laurent grade of rational scalar data.

## Amplitude-level no-go

At six points, write the two QTDS presentations as

\[
q_\pm
=
\left(
\frac{N_0^\pm}{Y_0},
\frac{N_1^\pm}{Y_1},
\frac{N_2^\pm}{Y_2}
\right)
\in V=K_6^3,
\]

where \(Y_i\) are the three physical odd-block channels. The summed scalar amplitude sees only

\[
\epsilon:V\to K_6,
\qquad
\epsilon(v_0,v_1,v_2)=v_0+v_1+v_2.
\]

The established equality says

\[
\epsilon(q_+)=\epsilon(q_-)=a_{R,6}.
\]

Thus

\[
c=q_+-q_-\in\ker\epsilon.
\]

No functor of only the summed amplitude and its leading Laurent coefficient can recover \(c\):
contact redistribution changes \(c\) without changing \(\epsilon(q_\pm)\). The triangle flow
solving \(\partial h_6=c\) is even less determined. Its solutions form an affine line over

\[
H_1(C_3;K_6)\simeq K_6.
\]

The zero-circulation inverse-Laplacian solution uses the triangle metric, which the summed
amplitude also forgets. This is an information-theoretic obstruction, not merely failure to
guess a formula.

## Why the one-parameter normal link does not repair it

The minimal complex base for the documented shift is

\[
U_X\times\Delta_t,
\qquad
R=U_X\times\{0\}.
\]

Its complex normal link is an unmarked circle; on the real slice it is \(S^0\). The three NLSM
channels are tangential divisors in \(X\), not three marked normal directions in \(t\). A triangle
is a possible cellulation of a circle, but its channel labels and equal-edge metric are extra
data. Hence the QTDS flip triangle is not the natural link of the documented one-parameter shift.

Verdier specialization requires

\[
(B_6,R_6,\mathscr K_6),
\qquad
\mathscr K_6\in D_c^b(B_6),
\]

together with an extension or lattice and monodromy. It is not defined by a rational function
alone. The notation \(\operatorname{Sp}_{R_6}(\mathscr K_6)\) remains a target type, not an
already constructed scalar object.

## The scalar-cell escape hatch

The scalar master at tree level has more structure than its sum: it is canonically presented by
planar cubic trees, equivalently polygon triangulations. Retain those cells while taking the
fourth \(t\)-grade.

For the hexagon:

- twelve scalar triangulations contain one allowed odd-block diagonal;
- each of the three quadrangulations has exactly four cubic refinements;
- two scalar triangulations contain no allowed diagonal.

The last two cells are the parity-central triangulations. One contributes

\[
C_{\rm odd}=-(x_1+x_3+x_5);
\]

the other contributes

\[
C_{\rm even}=-(x_0+x_2+x_4),
\]

where \(x_i=s_{i,i+1}\). Thus the unresolved scalar contact is

\[
C=C_{\rm odd}+C_{\rm even}
=
-\sum_{i=0}^{5}x_i.
\]

This information is lost by the final scalar sum but retained by the cubic-cell grade.

## Exact QTDS redistribution

Let \(G_i\) be the fourth scalar grade summed over the four cubic refinements of

\[
D_i=(i,i+1,i+2),
\qquad
i=0,1,2.
\]

The exact symbolic identities are

\[
\begin{aligned}
q_0^+&=G_0-(x_3+x_4),&
q_0^-&=G_0-(x_0+x_1),\\
q_1^+&=G_1-(x_1+x_2),&
q_1^-&=G_1-(x_4+x_5),\\
q_2^+&=G_2-(x_5+x_0),&
q_2^-&=G_2-(x_2+x_3).
\end{aligned}
\]

For either polarity, the three contact pairs partition the six boundary variables exactly once:

\[
\sum_i(q_i^\pm-G_i)=C.
\]

The two global choices are the two cyclic perfect matchings between odd and even boundary
contacts. They are exchanged by one-step rotation. The alternating cyclic lift therefore supplies
precisely the program datum required to distribute the two parity-central scalar cells.

The diagramwise polarity difference is

\[
\begin{aligned}
c_0&=(x_0+x_1)-(x_3+x_4),\\
c_1&=(x_4+x_5)-(x_1+x_2),\\
c_2&=(x_2+x_3)-(x_5+x_0),
\end{aligned}
\]

with \(c_0+c_1+c_2=0\). The canonical cyclic zero-circulation flow is

\[
H_{ij}=\frac{c_i-c_j}{3}.
\]

This proves:

> The six-point QTDS polarity comparison is scalar-derived from the **cell-resolved** fourth
> grade plus the alternating cyclic lift. It is not derivable from the summed scalar amplitude.

The result is exact in the nine-variable formal planar kinematic space.

## The parity-core forgetting map

For a scalar triangulation \(T\) of an even polygon, retain only its allowed diagonals:

\[
\pi_{\rm core}(T)
=
\{D\in T:D\text{ splits the polygon into even subpolygons}\}.
\]

This is a noncrossing partial quadrangulation. It gives a canonical combinatorial map from scalar
associahedral cells to the partial-quadrangulation or Fuss--Catalan complex.

The exact distributions by core size are

\[
n=6:\quad\{1:12,\ 0:2\},
\]

\[
n=8:\quad\{2:96,\ 1:32,\ 0:4\},
\]

\[
n=10:\quad\{3:880,\ 2:440,\ 1:100,\ 0:10\}.
\]

At full core, every quadrangulation of a \(2m\)-gon has

\[
2^{m-1}
\]

cubic refinements, one choice of diagonal in each quadrilateral. This gives \(4\) refinements at
six points and \(8\) at eight points.

## Eight-point scalar origin of the coherence faces

At eight points:

- each of the twelve quadrangulations has eight scalar cubic refinements;
- each of the eight one-channel cores has four scalar triangulations;
- there are four zero-core scalar triangulations.

Each zero-core triangulation has one central same-parity diameter:

\[
(0,4),
\qquad
(1,5),
\qquad
(2,6),
\qquad
(3,7).
\]

For each diameter, the four compatible quadrangulations are exactly the four vertices of one
square in the projective-plane medial complex of entry 19. Thus the four square coherence faces
are canonically labeled by four scalar central cells.

Each one-channel core is labeled by one of the eight physical diagonals and belongs to the
corresponding factorization triangle. This gives a scalar associahedral explanation for

\[
8\text{ factorization triangles}
+
4\text{ square cells}.
\]

The remaining global octagon is not yet derived from the core map. It is the natural location for
the relation among parity-central transfers, cyclic rotation, and nontrivial \(\mathbb Z_2\)
holonomy.

## What is and is not now intrinsic

Established at scalar-cell presentation level:

1. the parity-core map;
2. full quadrangulation fibers;
3. the two six-point parity-central scalar cells;
4. their exact QTDS contact redistribution;
5. the local six-point deck flow;
6. the eight one-channel/factorization labels;
7. the four central-diameter/square labels.

Still missing after the presentation-cellular construction of entry 21:

1. the global eight-point octagonal filler and its integral/sign-local-system test;
2. Jordan-valued edge syzygies compatible with the scalar carrier;
3. a filtered facewise map into scalar-normal or worldsheet twisted chains;
4. a residue-free twisted image of the six-point scalar tripod;
5. a chain-level inverse of the scalar pairing at resonant boundaries.

The naive alternating sum of four Jordan-decorated vertices around a square is nonzero even in a
special associative Jordan pair. The square filler must use edge syzygies; incidence and vertex
bracketings alone do not produce the Jordan identity.

## Minimal Frost and YM handoff

Frost should construct or obstruct a filtered scalar/surface complex

\[
(C^\bullet_{n,\alpha},d,F_t^\bullet,\Sigma_{n,\alpha}(t))
\]

whose associated grade retains the parity-core decomposition, together with

\[
\iota_\alpha:
C_\bullet(\mathfrak M_n;\mathcal L_\alpha)
\longrightarrow
\operatorname{gr}_t C^\bullet_{n,\alpha}
\]

compatible with cuts. The map should be sought as pushforward or homotopy transfer along
\(\pi_{\rm core}\), not invented from an unmarked one-parameter link.

YM should construct or obstruct

\[
\Phi_\alpha:
\operatorname{gr}_t C^\bullet_{n,\alpha}
\longrightarrow
(\Omega^\bullet(\mathcal M_{0,n}),\nabla_\omega)
\]

and a chain-level scalar duality map. At six points it must send the exact cell-resolved flow to

\[
\nabla\eta_6=\omega_{6,+}-\omega_{6,-}
\]

and intertwine every channel residue with the Alexander--Whitney coproduct.

## Reproducible audit

Run:

`python research/nima/check_qtds_descent.py`

The script checks the six-point Laurent identities, scalar parity-core counts through ten points,
the eight-point refinement fibers, the central-diameter/square correspondence, and the previously
recorded projective-plane and Jordan-endpoint tests.

## Sources and provenance

- [Arkani-Hamed, Cao, Dong, Figueiredo, and He, *NLSM inside Tr(Phi cubed)*](https://arxiv.org/html/2401.05483)
  supplies the one-parameter alternating shift, large-\(\delta\) grade, scalar cubic-tree
  factorization, and broader mixed-shift landscape.
- [Cao, Han, and Zhu, *NLSM amplitudes from a quartic two-derivative theory*](https://arxiv.org/html/2607.27345v1)
  supplies the target QTDS tree grammar.

The parity-core map, exact scalar-cell contact decomposition, and eight-point square labeling are
Marici calculations.

## Decision

Reject the statement that the documented **summed amplitude** intrinsically contains a QTDS
chain homotopy.

Promote the more precise positive statement:

> The scalar **cell-resolved associated grade**, enriched by the alternating cyclic lift, contains
> the complete six-point QTDS contact redistribution and exposes the correct eight-point
> coherence skeleton.

The primary frontier is now to turn this parity-core transfer into a cut-compatible chain map and
to determine whether its Jordan-valued edge syzygies and octagonal holonomy exist.

# Cut Recollement, the Möbius Nerve, and the Global Orientation Line

## Record

Date: 2026-08-14

Status: exact integral \(n=8\) cellular theorem.  This entry constructs the
pair \((K_5,B_{\rm cut})\), its relative/Borel--Moore chain carrier, and its
dihedral module.  It does not define a Grothendieck topology or identify the
resulting global orientation line with entry 66's alternating conductor.

## The cellular pair

Let \(K_5\) be the five-dimensional octagon associahedron.  Its cells are
noncrossing octagon dissections, and a cell with fixed dissection \(S\) has
dimension \(5-|S|\).  Let

\[
B_{\rm cut}
=\bigcup_{D\in\mathcal D_{\rm phys}}X_{\{D\}}
\subset K_5
\]

be the union of the eight facets indexed by opposite-parity diagonals.  This
is a cellular subcomplex: adding a diagonal to a dissection that already
contains a physical diagonal cannot leave \(B_{\rm cut}\).

The checker uses the integral Loday realization to orient every cell.  It
constructs all signed cellular boundary matrices and verifies \(d^2=0\).
Unit-pivot Smith elimination reaches zero remainder in every degree, so every
nonzero Smith factor is one.  The exact cell counts and boundary ranks are

\[
\begin{array}{c|c|c}
&\#C_d\ (d=0,\ldots,5)&\operatorname{rank}\partial_d\ (d=0,\ldots,5)\\
\hline
K_5&(132,330,300,120,20,1)&(0,131,199,101,19,1)\\
B_{\rm cut}&(128,304,240,76,8,0)&(0,127,172,68,8,0)\\
(K_5,B_{\rm cut})&(4,26,60,44,12,1)&(0,4,22,33,11,1).
\end{array}
\]

Consequently,

\[
H_*(B_{\rm cut};\mathbb Z)
=\mathbb Z[0]\oplus\mathbb Z^5[1],
\qquad
H_*(K_5,B_{\rm cut};\mathbb Z)
=\mathbb Z^5[2],
\]

with no torsion.

Degreewise, the cellular complexes form the exact sequence

\[
0\longrightarrow C_*(B_{\rm cut})
\longrightarrow C_*(K_5)
\longrightarrow C_*(K_5,B_{\rm cut})
\longrightarrow0.
\]

Thus the locally closed complement has a genuine relative/Borel--Moore
carrier.  This is the cellular recollement of a closed subcomplex and its
complement, not a claim of Cut-only sheaf descent.

## The rank-four occurrence kernel does not survive

The four Cut-invisible triangulations are still exactly the zero-core
vertices

\[
16,\quad24,\quad96,\quad100.
\]

However, the relative differential

\[
\partial_1:C_1(K_5,B_{\rm cut})
\longrightarrow C_0(K_5,B_{\rm cut})\cong\mathbb Z^4
\]

has Smith rank four.  Therefore

\[
H_0(K_5,B_{\rm cut})=0.
\]

The rank-four kernel in entry 90 is a true statement about the free module on
triangulation occurrences, but it is not cellular/Cousin homology.  The
incident scalar-flip edges attach all four generators.  The genuine contact
carrier first appears as the rank-five relative group in degree two.

## Möbius nerve and four local squares

Write the eight physical diagonals cyclically as

\[
p_i=\{i,i+3\},\qquad i\in\mathbb Z/8.
\]

Two Cut facets intersect precisely when their diagonals are compatible.  Each
\(p_i\) is compatible with \(p_{i+3},p_{i+4},p_{i+5}\).  There are 12
compatible pairs and no compatible triples.  Every nonempty intersection is
an associahedral face and hence contractible.  Therefore the good-cover nerve
of the eight Cut facets is the Möbius ladder

\[
\Gamma_8,
\qquad |V|=8,\qquad |E|=12,\qquad b_1=5,
\]

and the integral cellular calculation agrees with the nerve theorem:

\[
B_{\rm cut}\simeq\Gamma_8.
\]

The four zero-core charts have one-flip exits to the following four nerve
squares:

\[
\begin{array}{c|c}
16&\{0,1,4,5\}\\
24&\{2,3,6,7\}\\
96&\{1,2,5,6\}\\
100&\{0,3,4,7\}.
\end{array}
\]

Their oriented square boundaries span a saturated rank-four sublattice

\[
S\subset H_1(\Gamma_8;\mathbb Z),
\qquad
H_1(\Gamma_8;\mathbb Z)/S\cong\mathbb Z.
\]

Let \(o\) be the oriented outer octagon of the Möbius ladder.  In the
primitive quotient generator \(g\), the exact integral relation is

\[
\boxed{o=2g\pmod S.}
\]

Equivalently, the five cycles consisting of the four local square boundaries
and the outer octagon generate an index-two sublattice of
\(H_1(\Gamma_8;\mathbb Z)\).  This is the integral Möbius-band relation: the
boundary winds twice around its core.

## Dihedral module and the connecting map

The checker obtains the cellular \(D_8\) action from the signed incidence
matrices and verifies the chain-map identity over every facet.  The character
of both \(H_1(B_{\rm cut})\) and \(H_2(K_5,B_{\rm cut})\) is

\[
\chi(r^k)=(5,1,1,1,-3,1,1,1),
\qquad
\chi(r^ks)=-1
\quad(0\leq k<8).
\]

Since \(K_5\) is contractible, the long exact sequence gives a certified
equivariant isomorphism

\[
\delta:
H_2(K_5,B_{\rm cut};\mathbb Z)
\xrightarrow{\ \sim\ }
H_1(B_{\rm cut};\mathbb Z).
\]

Over \(\mathbb Q\), the character decomposes as

\[
H_1(B_{\rm cut};\mathbb Q)
\cong
\mathbb Q_{\rm or}\oplus V_1\oplus V_3.
\]

Integrally, the four-square lattice is the saturated rank-four part and the
quotient is the primitive orientation line:

\[
r\mapsto+1,
\qquad
s\mapsto-1.
\]

This proves that the fifth mode is global and orientation odd.  It does
**not** yet identify that line with the local three-road character \(\chi_N\):
the latter additionally contains the polarity/core-exchange typing of entry
89.  Nor is there a chain map from this eight-point relative complex to entry
66's six-term symbol \(\sigma_{\rm alt}\).  Both identifications remain
untyped.

## Consequence and next falsifier

The corrected contact picture is therefore

\[
\boxed{
\text{four local square modes}
\quad+\quad
\text{one primitive global Möbius/orientation mode},
}
\]

not a free direct sum on four uncovered triangulations.  The index-two
relation is essential integral data and rules out a naive integral splitting
with the outer octagon as primitive generator.

The next exact test is to construct an actual coefficient-loaded Cousin map
from the primitive orientation quotient to the boundary-costalk complex of
entry 89.  It must reproduce the road/core character after the relevant
stabilizer restriction and match the six supported terms and signs of entry
66.  Until that map exists, calling the global line
\(\boldsymbol\sigma_{\rm alt}\) would be premature.

The eight channel triangles, if introduced, must be exhibited as a
medial/barycentric refinement of \(\Gamma_8\); they were not used in this
certificate.

## Exact certificate

Run:

```text
rustfmt --edition 2021 --check research/voevodsky/check_n8_cut_recollement.rs
rustc --edition=2021 -D warnings -O research/voevodsky/check_n8_cut_recollement.rs -o "$env:TEMP\\marici-n8-cut-recollement.exe"
& "$env:TEMP\\marici-n8-cut-recollement.exe"
```

Certificate SHA-256:

```text
aa00f6339347cb82743dce569c5c42725a6a42c500d7ec1650fed04bbbce9cc9
```

## Internal dependencies

- Entry 48: Cuts plus ultraviolet boundary data are conservative.
- Entry 66: the six-point alternating-conductor coefficient symbol and its
  missing chain lift.
- Entry 89: boundary-costalk pairing and the local character \(\chi_N\).
- Entry 90: closed scalar incidence and the rank-four free-occurrence Cut
  kernel.
- `research/voevodsky/check_n8_scalar_cd_site.rs`.
- `research/voevodsky/check_n8_cut_recollement.rs`.

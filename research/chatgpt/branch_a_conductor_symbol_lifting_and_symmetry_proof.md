# Branch A — conductor-symbol lifting and symmetry

Date: 2026-09-07.

## Result and scope

The first-conductor symbol can be tested before constructing a new complete conductor–Morse map. In the six occurrence weights previously used, at regulator-normal grade three, the specified complete endpoint/Q frame has:

- 134 closed first-order coefficient symbols;
- 74 independent integral quadratic compatibility conditions;
- a rank-60 lattice of symbols satisfying those conditions.

Every compatible first-order symbol has exactly one full coefficient-cycle lift in these weights. There are no degree-three higher-conductor corrections available, and the differential of a degree-three chain contains conductor orders at most two. Thus the quadratic test is both necessary and sufficient; no higher-order obstruction is deferred.

The published cellular reflection fixes a rank-59 first-symbol lattice and a rank-25 full-lift lattice. Restoring the actual three-member occurrence-mark orbit gives these same ranks for equivariant families under the six-element dihedral group. Among the 25 equivariant lift directions, 16 survive forgetting the primary-comparison homotopy and nine require that homotopy to remain specified.

The invariant obstruction sequence has an additional, explicitly computed index-two defect. An invariant quadratic defect can have ordinary preimages but no invariant integral preimage. Its double has an invariant preimage. The associated reflection defect lies entirely in the primary-comparison directions and is nullhomotopic as an ordinary supported map only by changing the primary homotopy.

None of these constructions selects the physical conductor–Morse class. The source's scalar conormal symbol does not itself specify a chain-valued symbol in the 134-dimensional receiving space.

## 1. Coefficients and the complete frame

Use the ordered diagonals

\[
\mathcal D=(02,03,04,13,14,15,24,25,35),
\]

and the ring

\[
R=\mathbb Z[\beta,X_d:d\in\mathcal D]/
(X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

Set

\[
I=(X_{02},X_{04},X_{13},X_{15},X_{24},X_{35}).
\]

The 430-state complex has basis

\[
[F,H,\varepsilon],\qquad H\subseteq F,\quad \varepsilon\in\{0,1\},
\]

with homological degree

\[
3-|F|+|H|+\varepsilon.
\]

The native differential removes a mark with coefficient \(\beta X_h\). The radial differential adds a noncrossing face label with coefficient \(X_d\). Their signs are the repository's cellular and ordered Koszul signs. The separate occurrence partner has differential \(X_{35}\), not \(\beta X_{35}\).

Both 16-state endpoint packets remain:

\[
V_-=\{02,04,24\},\qquad V_+=\{13,15,35\}.
\]

The short boundary has 416 states. Its actual quotient \(Q\) has fourteen states. No three-edge substitute is used.

If \(v\) denotes the graded projection to the full endpoint packet and \(q\) the genuine chain projection to \(Q\), the framed kernel is

\[
N_n=\{c\in(IC_\beta)_n:q(c)=0,\ v(c)=0,\ v(dc)=0\}.
\]

The extra condition \(v(dc)=0\) is required because graded endpoint projection alone is not a chain map. This is the largest subcomplex contained in the graded endpoint/Q kernel.

The quotient \(IC_\beta\to IC_\beta/N\) is an actual chain map. Its homotopy fibre retains the boundary-comparison homotopies and is equivalent to \(N\). The checker reconstructs the split graded bases and verifies the complete fibre contraction; it does not simply discard these homotopies.

The source for supported comparisons remains

\[
S_\beta=[Re\xrightarrow{\beta}Rp],\qquad |e|=3,\quad |p|=2.
\]

The fibre fixing the primary together with its comparison homotopy reduces explicitly to \(\operatorname{Hom}(R[3],N)\). Its degree-zero coordinate is \(b-\beta h\), not just the top value \(b\). Thus its differences are governed by \(H_3(N)\). This reduction is replayed in every occurrence component.

The integral polynomial family is a coefficient model. The source's exponential interpretation requires characteristic zero, and its geometric purity theorem assumes fixed nonzero regulator. No geometric purity theorem at \(\beta=0\) is inferred here.

## 2. The first-conductor symbol and its complete lifting equation

Give \(\beta\) and each native mark regulator-normal weight one; the separate occurrence partner has regulator-normal weight zero. Fix total regulator-normal weight three.

At occurrence weight \(m=\epsilon_a\), the coefficient of a state is forced to have occurrence exponents

\[
m+\mathbf1_F-\mathbf1_H-\varepsilon\mathbf1_{35}.
\]

It must be nonnegative, survive the mixed-sheet monomial ideal, and contain a short occurrence factor. The regulator exponent is \(3-|H|\). These requirements determine a finite integral lattice exactly; there is no arbitrary polynomial-degree cutoff.

The first associated-grade source is \(IC_\beta/I^2C_\beta\), with the induced differential and the full endpoint/Q frame. Its framed degree-three cycle lattice will be denoted \(J_a\). Its full-cycle counterpart is \(L_a\).

### Why all obstructions occur at the quadratic conductor order

For a degree-three state,

\[
|H|+\varepsilon=|F|.
\]

If \(\varepsilon=0\), all native marks are present and the occurrence coefficient is \(X_a\). If \(\varepsilon=1\), exactly one native mark is missing. Nonnegativity and the conductor condition again force the coefficient to contain exactly one short occurrence variable. Long factors do not change this conductor-order assertion.

Consequently, in the six tested weights,

\[
(I^2C_\beta)_3=0,
\qquad
(IC_\beta)_4=0.
\]

These equalities are componentwise statements in the specified occurrence and regulator grades, not claims about the whole ungraded complex.

The differential of a degree-three chain either preserves conductor order or raises it by one. Hence, for a first-order cycle \(j\), its unique polynomial representative has

\[
dj\in(I^2C_\beta/I^3C_\beta)_2.
\]

There is no degree-three order-two correction with which to change this boundary. Define

\[
\mathfrak o_a(j)=dj.
\]

Then

\[
j\text{ has a full lift}\quad\Longleftrightarrow\quad\mathfrak o_a(j)=0.
\]

The lift, when it exists, is the same degree-three polynomial chain. It is unique strictly, and there are no degree-four boundaries identifying different lifts.

This is the actual filtered-complex lifting equation. In more general weights a connecting class must be taken modulo possible higher-order primitives. Here that indeterminacy group is zero by degree and conductor order, so the equation is literal.

### Exact matrices

| Occurrence direction | Closed first symbols | Independent quadratic equations | Full lifts |
|---|---:|---:|---:|
| 02 | 19 | 10 | 9 |
| 04 | 19 | 10 | 9 |
| 13 | 19 | 12 | 7 |
| 15 | 19 | 12 | 7 |
| 24 | 19 | 10 | 9 |
| 35 | 39 | 20 | 19 |
| Total | 134 | 74 | 60 |

The literal quadratic target has 237 labelled coefficient rows. Its matrix has rank 74. Every nonzero diagonal factor under the exported unimodular reduction is one. Taking the actual saturated image as the obstruction lattice gives

\[
0\longrightarrow L\longrightarrow J
\xrightarrow{\mathfrak o}O\longrightarrow0,
\]

\[
L\cong\mathbb Z^{60},\qquad
J\cong\mathbb Z^{134},\qquad
O\cong\mathbb Z^{74}.
\]

The certificate contains the literal quadratic matrices, the unimodular row and column operations, the injection of all full lifts into first-symbol coordinates, and the exact inverse change of basis on the kernel. This proves integral completeness and saturation.

Independent computations modulo \(I^3,I^4,I^5\) give unimodular transition maps on the full top-cycle lattices once the quadratic equation is imposed. This is a check of the structural argument, not a finite-order extrapolation.

## 3. A first symbol that passes the linear test but cannot lift

Let

\[
F=\{02,03,04\},\qquad E=\{02,04\},
\]

and set

\[
U_{02}=X_{02}([F,F,0]-\beta[E,E,0]).
\]

Modulo \(I^2\), it is closed and its endpoint/Q components vanish. Its full boundary has five terms. One is

\[
-\beta^2X_{02}X_{04}[\{02,04\},\{02\},0].
\]

The corresponding coefficient functional evaluates \(dU_{02}\) to \(-1\) in the forced homogeneous basis. This monomial survives the normalization relations, since both short variables lie on the same sheet.

No order-two degree-three chain exists in this weight to cancel that term. Thus \(U_{02}\) has no full framed lift. Multiplication by the actual source coefficient \(-X_{14}\) preserves the obstruction; that long coordinate is not inverted or cancelled.

By contrast, the earlier marked-gallery cycle

\[
Y_{02}=X_{02}([\{03,13,35\},\{03,13,35\},0]
-\beta[\{13,35\},\{13,35\},0])
\]

is closed before any conductor truncation. Its short-normal boundary terms vanish through the mixed-sheet relations. It is one of the 60 compatible first symbols.

The test distinguishes genuine lifts from symbols that become closed only after discarding their quadratic conductor boundary.

## 4. Symmetry must transport the occurrence correction

Use exactly the published cellular action

\[
r(v)=v+2\pmod6,
\qquad s(v)=2-v\pmod6,
\]

with top-cell signs \(+1,-1\), respectively. The normal marks carry their ordered exterior permutation signs. The regulator and the two abstract generators \(p,e\) of \(S_\beta\) are fixed. This declares the representation convention; no extra sign twist is fitted.

Reflection fixes the occurrence label 35. Rotation transports it through

\[
35\longmapsto15\longmapsto13\longmapsto35.
\]

Therefore a full dihedral family uses all three occurrence-labelled complexes. The checker reconstructs their 1,290 states and verifies differential naturality and all group relations on every column.

Let \(H=\langle s\rangle\). The calculated invariant lattices are

\[
\operatorname{rank}J^H=59,
\qquad
\operatorname{rank}L^H=25,
\qquad
\operatorname{rank}O^H=34.
\]

A compatible family over the three-member mark orbit is determined by its 35 component fixed by its stabilizer. The certificate explicitly rotates each of the 25 fixed lift generators and verifies the complete family against both group generators. No averaging or division by two or three occurs.

Of the 25 equivariant lift directions, sixteen survive forgetting the primary-comparison homotopy. Nine lie in the primary-homotopy summand. This is verified as a direct-sum decomposition for the actual reflection matrix, not inferred from dimensions.

For example,

\[
Y_{02}+sY_{02}
\]

is a four-term reflection-invariant full lift. Its rotation orbit is a genuine dihedral family with zero complete endpoint and Q values. Its fully marked coefficients include \(\pm1\) with no factor of \(\beta\), so it is ordinarily detectable as a supported map.

## 5. An index-two obstruction remains in invariant preimages

Taking invariants of the exact obstruction sequence is not exact on the right. Here the full integral computation gives

\[
0\longrightarrow\mathbb Z^{25}
\longrightarrow\mathbb Z^{59}
\longrightarrow\mathbb Z^{34}
\longrightarrow\mathbb Z/2
\longrightarrow0.
\]

The final cokernel is certified by 33 unit diagonal factors and one factor two in the map from invariant first symbols to the saturated invariant quadratic-obstruction lattice.

The certificate supplies an explicit invariant quadratic defect \(o_*\), an ordinary first-symbol preimage \(j_*\), and an invariant first-symbol preimage of \(2o_*\). They satisfy

\[
\mathfrak o(j_*)=o_*,\qquad so_*=o_*.
\]

There is no invariant integral preimage of \(o_*\). The obstruction is expressed by

\[
b_*=sj_*-j_*\in L,
\qquad sb_*=-b_*.
\]

In the integral reduction of \(s-1\) on \(L\), the transformed coordinates of \(b_*\) include an odd entry on a diagonal-two row. Hence

\[
b_*\notin(s-1)L.
\]

This is an explicit integral failure of equivariant choice, rather than a rank mismatch.

Every ordinarily detectable coordinate of \(b_*\) is zero. The complete polynomial representative has a termwise factor of \(\beta\):

\[
b_*=\beta B_*,\qquad dB_*=0.
\]

The ordinary supported-map homotopy with value \(B_*\) on \(p\), zero on \(e\), kills the map difference with top \(b_*\). It changes the primary-comparison homotopy. In the primary-fixed fibre the coordinate remains \(b_*\neq0\).

This \(\mathbb Z/2\) is not integer torsion in the free lift lattice, and it is not assigned to the physical \(\Delta_J\). It is the precise obstruction to choosing an invariant integral first-symbol preimage of a specified invariant quadratic defect. It is separate from the all-zero-defect problem, whose equivariant solution lattice has rank 25.

## 6. What the scalar normalization symbol supplies

The source fixes

\[
\sigma_{\rm alt}
=y_2\,dx_1+y_1\,dx_3+y_0\,dx_5
-y_1\,dx_0-y_0\,dx_2-y_2\,dx_4.
\]

In the zero-based polygon labels used by this calculation,

\[
y_0=X_{03},\quad y_1=X_{14},\quad y_2=X_{25},
\]

and

\[
\sigma_{\rm alt}
=-X_{14}[X_{02}]-X_{25}[X_{04}]
+X_{25}[X_{13}]+X_{03}[X_{15}]
-X_{03}[X_{24}]+X_{14}[X_{35}].
\]

Here \([X_d]\) denotes the first conductor symbol. The checker verifies its covariance under the published dihedral subgroup. The source's polarity twist under the additional one-step sheet exchange remains distinct; no unsupported action of that exchange inside one fixed occurrence-corrected complex is introduced.

These six signs and long-coordinate factors do not specify which marked degree-three coefficient chain accompanies each conormal symbol. That missing chain-valued placement is required to obtain an element of \(J\).

The prescribed long-coordinate multipliers are nonzero divisors on these coefficient chains. They preserve the quadratic failures and the valid cycle directions; none supplies an automatic cancellation of the obstruction. The checker verifies this on every exported lift basis vector.

Thus an independently supplied **complete chain-valued first symbol** is enough to decide the lift: apply the 74 exported compatibility equations. If it passes, its full polynomial lift is unique in the specified weights. The scalar six-term symbol alone is not that chain-valued input.

## 7. Verification and artifacts

The standalone checker uses only the Python standard library. It reconstructs the complete signed complexes, all coefficient subquotients and frame kernels, the actual first-symbol basis, the quadratic boundary map, its integral kernel and image, the primary-fibre reduction, and the transported group action. All polynomial and integer basis changes used in the results have explicit inverses or unimodular operation logs.

The certificate distinguishes:

- actual closed first symbols from full lifts;
- invariant deformations from invariant preimages of nonzero defects;
- ordinary supported homotopies from homotopies preserving the primary comparison;
- this coefficient computation from the unconstructed physical conductor–Morse map.

Reproduce with:

```bash
python branch_a_conductor_symbol_lifting_and_symmetry_checker.py --output branch_a_conductor_symbol_lifting_and_symmetry_certificate.json
```

No external files, network requests, zip archives, optional packages, or coefficient cutoffs are needed.

### Source inputs

Repository commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

1. `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, blob `b967151cb0ee822e2361b9334a4ab26082c12682`: native/radial differential, labelled support subcomplexes, and cellular dihedral signs.
2. `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: alternating normalization ring and source-defined first conductor symbol.
3. `src/ledger/20260813-66 Alternating Fusion Conductor Symbol and the First Cross-Normal Relation.md`, blob `1982f7a4babc13ff92f2ec1f52ca4c86f109df54`: the original one-based short/long coordinate dictionary.
4. The previously supplied first-conductor coherent-primary-lifts checker supplies the reconstructed reference coefficient model. Its algebraic routines are included in this standalone file and its relevant conclusions are recomputed rather than trusted as signature values.

General homological conventions:

- Stacks Project, Hom complexes: https://stacks.math.columbia.edu/tag/0A8H
- Stacks Project, connecting morphisms: https://stacks.math.columbia.edu/tag/0117

The finite matrices prove the stated coefficient assertions. These sources do not establish a physical conductor–Morse realization, a BRST map, or geometric purity at regulator zero.

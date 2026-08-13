# Lowering Operators Are a Cellular Coframe, Not the Jet Adjoint

## Record

Date: 2026-08-13

Status: literal adjunction falsified as a typed intrinsic statement; a weaker
cellular-coframe/augmentation relation survives and gives the correct next test.

## Question

The publication sweep suggested testing

\[
\langle J^1 f,g\rangle
\stackrel{?}{=}
\langle f,J^{1\dagger}g\rangle,
\qquad
J^{1\dagger}\in
\operatorname{span}\{\mathcal D_\Gamma\},
\]

where \(J^1\) denotes the scalar-scaffolding first normal operation and
\(\mathcal D_\Gamma\) denotes a differential operator extracting a planar cubic
scalar diagram from a scaffolded Yang--Mills amplitude.

The test has a sharp answer:

> The published \(\mathcal D_\Gamma\) are not the adjoints of the scalar
> multi-normal jet. They are coordinate-dependent cellular extraction maps.
> Their complete family may furnish a presentation-level coframe whose
> augmentation is a scalar transmutation, but an actual adjoint exists only
> after gauge descent, Verdier duality, normal-line bookkeeping, cellular
> augmentation, and the physical scalar quotient.

Thus the discovery is real, but its algebraic role is different from the first guess.

## The raising operation is not an ordinary derivative

For \(n\) scaffolded gluons the scalar construction begins with \(2n\) scalar
legs and the fusion locus

\[
\mathfrak f
=
\bigcap_{a=1}^{n}D_a,
\qquad
D_a=(s_a=0).
\]

Entry 08 corrected the slogan “first jet” to the multi-normal coefficient

\[
\mathbb J_{\mathfrak f}F
=
[s_1s_2\cdots s_n]F
\in
L_{\mathfrak f},
\qquad
L_{\mathfrak f}
=
\bigotimes_{a=1}^{n}N_{D_a}^{\vee}.
\]

The physical operation is

\[
J_{\rm phys}
=
H_{\rm gauge}\circ\mathbb J_{\mathfrak f}.
\]

It therefore has four features that any adjoint must remember:

1. it is supported on a codimension-\(n\) fusion stratum;
2. it changes effective arity from \(2n\) scalar flags to \(n\) gluon flags;
3. it is valued in a tensor product of normal lines;
4. it becomes physical only after gauge cohomology.

A raw coordinate derivative in the already scaffolded \(n\)-particle variables
does not have this type.

## What a genuine adjoint would be

Let \(S_{2n}^{\pm}\) denote the two twist sectors of the scalar normal object and
let \(G_n^{\pm}\) denote the physical gauge sectors. Suppose one has perfect
pairings

\[
I_S:S_{2n}^{-}\otimes S_{2n}^{+}\longrightarrow K,
\]

and

\[
I_G:G_n^{-}\otimes G_n^{+}\longrightarrow K.
\]

The second pairing is not just the global BAS/KLT kernel: it also needs the
physical transverse-polarization coevaluation. If

\[
J^+:S_{2n}^{+}\longrightarrow G_n^{+}\otimes L_{\mathfrak f},
\]

then its adjoint is forced by the pairings:

\[
(J^+)^{\dagger}
=
(I_S^{\flat})^{-1}
(J^+)^{\vee}
I_G^{\flat}.
\]

After moving the normal-line factor to the source or target, this is a map of the
form

\[
(J^+)^{\dagger}:
G_n^{-}
\longrightarrow
S_{2n}^{-}\otimes L_{\mathfrak f}^{\vee}.
\]

Geometrically, the Verdier dual of a normal residue is a Gysin/Thom-type
extension from the fusion stratum. It is not, without an additional comparison
theorem, an \((n-1)\)-fold coordinate derivative on the fused kinematic space.

This already rules out a literal identification with the published operators.

## What the differential operators actually do

Dong--Su--Yang define operators of the form

\[
\mathcal D
=
\frac{\partial^{n-1}}
{\partial X_{2a',2b'}
 \partial X_{2a_1,2b_1-1}
 \cdots
 \partial X_{2a_{n-2},2b_{n-2}-1}}.
\]

Their power counting explains the order \(n-1\): a Yang--Mills amplitude has
scaffold degree \(X^2\), whereas a planar cubic diagram has degree
\(X^{-(n-3)}\).

The construction fixes adjacent even labels, conventionally \((2,2n)\), and
then uses \(\partial_{X_{1,4}}\). Vertices 1 and 3 consequently play a special
role. The paper explicitly leaves a reference-independent construction for
future work.

For the distinguished Yang--Mills amplitude, selected operators obey

\[
\mathcal D_\Gamma A_n^{\rm YM}
=
b_\Gamma,
\qquad
b_\Gamma
=
\prod_{e\in\Gamma}\frac1{X_e},
\]

where \(\Gamma\) is a planar cubic graph. Other allowed derivative strings can
give a sum of diagrams or zero.

This is a coordinate-extraction statement on a distinguished amplitude. It is
not an operator identity on the full physical gauge complex.

## The four-point discriminant

At four points the paper gives

\[
D_s A_4^{\rm YM}
=
\frac1{X_{1,5}},
\qquad
D_t A_4^{\rm YM}
=
\frac1{X_{3,7}},
\]

with

\[
D_s
=
\mathcal D_{(2,8)(1,4)(1,6)},
\qquad
D_t
=
\mathcal D_{(2,8)(1,4)(3,6)}.
\]

Therefore

\[
(D_s+D_t)A_4^{\rm YM}
=
\frac1{X_{1,5}}
+
\frac1{X_{3,7}},
\]

which is the full planar cubic scalar amplitude for that cyclic order.

This reveals the right interpretation:

- \(D_s\) and \(D_t\) resolve the two cubic cells;
- summation is the cellular augmentation;
- only the augmented object is the ordinary scalar amplitude.

The generic four-point twisted half-space has dimension

\[
(4-3)!=1,
\]

whereas the planar cubic presentation has two cells. Hence the two raw
extractors cannot themselves be a canonical basis of the paired physical
half-space. A nontrivial presentation kernel is unavoidable already at four
points.

At five points the same distinction is larger: one planar chamber has five
cubic localization cells, whereas a generic BCJ-sized basis of global twisted
half-classes has dimension two. These are different index sets; neither is a
basis for the other without the face complex, assembly across orderings, and
physical quotient. The numerical counts are not proposed as a general equality;
their mismatch at the first nontrivial arities is enough to disprove a direct
identification of the two modules.

## Five independent obstructions to literal adjunction

### 1. Normal-line and arity obstruction

\(J_{\rm phys}\) is a \(2n\)-to-\(n\) fusion residue valued in
\(L_{\mathfrak f}\). The \(\mathcal D_\Gamma\) act after fusion and return
\(n\)-point rational scalar diagrams. They carry neither the missing
\(2n\)-point support nor the dual normal determinant.

### 2. Pairing obstruction

The scalar intersection pairing contracts ordering/twist data. The gauge
pairing additionally requires transverse state coevaluation. No chain-level
\(I_G\) is supplied by the differential-operator construction, so the equation
defining an adjoint cannot yet even be evaluated.

### 3. Presentation-versus-cohomology obstruction

An individual cubic graph is a term in the cellular or Cousin presentation of a
loaded associahedron. It is not by itself a representation-independent CHY
half-class. Index raising by the inverse BAS pairing is defined only after
descent to a BCJ-sized physical quotient, not graph by graph.

### 4. Naturality obstruction

A true adjoint of a monoidal normal operation would satisfy the transposed
base-change law induced by Cut/sewing. The paper proves its graph rules by
factorization for selected infinite families, not a universal chain-level
Cut-naturalness theorem. Its mixed-amplitude generalization first develops
gauge-invariance counterexamples at nine points.

### 5. Insufficient test-vector obstruction

The published equations evaluate \(\mathcal D_\Gamma\) on the canonical
amplitude \(A_n^{\rm YM}\). Adjunction is a bilinear identity for arbitrary
classes in two paired spaces. Agreement on one distinguished section cannot
establish that identity.

Any one of the first three obstructions defeats the literal claim. The last two
show why the presently available evidence cannot repair it implicitly.

## The surviving cellular-coframe statement

Let

\[
C_n^{\rm cub}
=
\bigoplus_{\Gamma\in\operatorname{Tri}(n)}
K\,|\Gamma\rangle
\]

be the planar cubic presentation module and let

\[
\epsilon_{\rm cub}(|\Gamma\rangle)
=
b_\Gamma
\]

be its amplitude augmentation.

Whenever \(\mathcal D_\Gamma g\) is divisible by \(b_\Gamma\), define the
presentation coefficient

\[
c_\Gamma(g)
=
b_\Gamma^{-1}\mathcal D_\Gamma g
\]

and the tentative coframe map

\[
\widehat{\mathcal D}(g)
=
\sum_\Gamma c_\Gamma(g)|\Gamma\rangle.
\]

For the canonical Yang--Mills amplitude, the published diagram extractors give

\[
c_\Gamma(A_n^{\rm YM})=1
\]

for every graph covered by the prescription. Consequently,

\[
\epsilon_{\rm cub}
\widehat{\mathcal D}(A_n^{\rm YM})
=
\sum_\Gamma b_\Gamma
=
A_n^{\phi^3}
\]

once completeness of the graph prescription is assumed.

This is the meaningful sense in which the derivatives lower Yang--Mills to the
scalar sector. They behave as a cellular coframe followed by augmentation.
They are much closer to coordinate functionals

\[
\mathcal D_\Gamma\circ J
\stackrel{?}{=}
\pi_\Gamma
\]

than to the metric adjoint of \(J\).

The equation is still conjectural because the left side has not been
constructed on a common scalar chain complex. But it is correctly directed and
matches the observed single-diagram extraction.

## Corrected adjunction conjecture

A relation to the true adjoint can only have the composite form

\[
\rho_{\mathfrak f}\circ(J^+)^{\dagger}
\stackrel{?}{=}
q_{\rm phys}\circ
\epsilon_{\rm cub}\circ
\widehat{\mathcal D}.
\]

Here:

- \(\rho_{\mathfrak f}\) is a specified fusion/arity-reduction map together
  with a trivialization or contraction of \(L_{\mathfrak f}^{\vee}\);
- \(\widehat{\mathcal D}\) is a complete gauge-descended, dihedrally
  equivariant cellular coframe, not merely its values on
  \(A_n^{\rm YM}\);
- \(\epsilon_{\rm cub}\) sums the cubic cells;
- \(q_{\rm phys}\) descends through the PT/KK/BCJ or twisted-cohomology
  quotient.

None of these arrows may be silently omitted. In particular, the corrected
formula is not currently proved.

An equally plausible interpretation is that the augmented lowering map is a
transmutation counit rather than an adjoint. These two possibilities are
distinguished by the pairing matrix test below.

## Smallest decisive matrix test

At four and five points:

1. choose bases of the scalar fusion-normal module and physical gauge
   cohomology;
2. compute the multi-normal residue matrix \(J\);
3. compute the generic scalar pairing \(I_S\);
4. compute the gauge pairing \(I_G\), including transverse state
   coevaluation;
5. form the unique metric adjoint

   \[
   J^{\dagger}_{\rm metric}
   =
   I_S^{-1}J^{\mathsf T}I_G;
   \]

6. construct every cubic extractor \(\mathcal D_\Gamma\), its cellular
   augmentation, and its physical quotient;
7. compare the resulting matrix with
   \(\rho_{\mathfrak f}J^{\dagger}_{\rm metric}\);
8. repeat after cyclically moving the distinguished scaffold labels;
9. test the transposed Cut square on every four/five-point channel.

Three outcomes are now cleanly separated:

- equality gives a genuine adjunction theorem;
- equality only after augmentation gives a counit/coframe theorem;
- reference-dependent disagreement falsifies even the corrected relation.

This is a finite symbolic calculation. Rust becomes useful only when extending
the complete graph/reference/channel matrix beyond low arity.

## Decision

Reject:

\[
J^{1\dagger}
\in
\operatorname{span}\{\mathcal D_\Gamma\}
\]

as a literal intrinsic claim about the operators currently defined.

Retain:

> The scaffold differential operators resolve a scalar transmutation into
> Catalan cubic cells. Their natural algebraic role is a cellular coframe or
> coordinate-extraction family. A true jet adjoint, if related to them, is the
> gauge-descended, augmented, physically quotiented, normal-line-corrected
> composite—not an individual derivative.

This weakens the proposed generator list in a productive way. The primitive
operation is not every \(\mathcal D_\Gamma\) separately. The likely primitive
is a single intrinsic lowering/transmutation morphism; the
\(\mathcal D_\Gamma\) are its coordinates in an associahedral presentation.

## Sources

- [Dong, Su, and Yang, *On differential operators for scalar-scaffolded
  gluons*, v2](https://arxiv.org/html/2512.15882v2)
- [Arkani-Hamed et al., *Scalar-Scaffolded Gluons and the Combinatorial Origins
  of Yang--Mills Theory*, v3](https://arxiv.org/html/2401.00041v3)
- Entries 08, 11, 13, 36, and 39 of this ledger.

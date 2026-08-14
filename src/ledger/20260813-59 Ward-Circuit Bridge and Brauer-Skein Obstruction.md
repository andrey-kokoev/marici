# Ward-Circuit Bridge and Brauer-Skein Obstruction

## Record

Date: 2026-08-13

Status: the residual equal-endpoint Ward kernel on the marked theta is
integrally and \(S_2\times D_3\)-equivariantly isomorphic to
\(H_1(K_{2,3};\mathbb Z)\).  Every spanning-tree chord generator maps
individually to a populated oriented resolved-circuit support.

This does **not** produce an additive Ward-to-curve dictionary.  The canonical
map runs from oriented circuit tags to homology.  It has no integral
\(D_3\)-equivariant section, every pair of primitive circuit tags intersects
once on the punctured torus, and no audited noncrossing Brauer state contains
two closed circuits.  Entry 60 sharpens the consequence: the nonsplit
two-term tag resolution already solves the additive problem integrally, while
an oriented Brauer--skein crossing/smoothing cell is required only for
multiplicative two-cycle coherence.

Reproducible certificate:

```text
research/nima/check_ward_cycle_brauer_map.rs
```

## Integral Ward--homology bridge

Orient the six edges of \(K_{2,3}\) from the two core vertices to the three
road vertices and order them by road, then core.  Every graph cycle is

\[
c(p,q)=(p,-p,q,-q,-p-q,p+q).
\]

Use the Ward quotient coordinates

\[
(l_{00},l_{01},l_{10},l_{11},q_0,q_1,q_2),
\]

after removing one local cyclic generator at each core vertex.  The exact
unimodular bridge is

\[
\boxed{
\Theta(c(p,q))
=(q,-p,-q,p,-p,-q,p+q).}
\]

It satisfies

\[
t\Theta(c)=0,
\qquad
\Theta^{-1}\Theta(c)=c,
\]

and intertwines the full \(S_2\times D_3\) action.  Thus

\[
\ker t\cong H_1(K_{2,3};\mathbb Z)
\]

as saturated integral symmetry modules, not merely as rational vector spaces
of the same rank.

All twelve spanning trees supply two primitive fundamental chord cycles.
The resulting 24 generators lie in unimodular bases, and all 144 changes
between tree bases are unimodular.

## Ribbon topology and determinant character

The graph-addition stages thicken as

\[
(0,1)\longrightarrow(0,2)\longrightarrow(1,1):
\]

disk, annulus, once-punctured torus.  Reversing the order of the two added
chords reverses the determinant orientation in all twelve spanning-tree
presentations.

On

\[
\det H_1(K_{2,3}),
\]

road rotation acts by \(+1\), road reflection by \(-1\), and core exchange by
\(+1\).  This identifies the previously observed two-sewing sign with the
ordinary orientation character of handle homology.

## Three circuit tags and the index-three obstruction

The three primitive oriented road-pair circuits are

\[
c_{01},\qquad c_{12},\qquad c_{20},
\]

and obey

\[
\boxed{c_{01}+c_{12}+c_{20}=0.}
\]

Hence there is a canonical surjective class map

\[
\operatorname{cl}:\mathbb Z^3_{\rm oriented\ tags}
\longrightarrow H_1(K_{2,3};\mathbb Z)
\]

with diagonal kernel.  The class matrix is saturated.  A non-equivariant
integral splitting can therefore be chosen, but no such choice is canonical
under road symmetry.

For a cycle with coordinates \((p,q)\), three times the unique
\(D_3\)-equivariant rational section has tag coordinates

\[
(p-q,\ p+2q,\ -2p-q).
\]

Some entries are not divisible by three.  Equivalently, the invariant
diagonal together with the sum-zero tag lattice has index

\[
\boxed{3}
\]

inside \(\mathbb Z^3\).  Thus a symmetric additive section requires
\(1/3\).  This is the same denominator pattern seen in the earlier attempt to
average pointed two-sewing fillers, now derived from the circuit-tag
extension itself rather than from an arbitrary origin simplex.

Orientation is indispensable.  A road reflection can fix an unoriented
circuit support while reversing its class in \(H_1\), so the ordinary free
module on unoriented Brauer loops cannot carry the bridge equivariantly.

## The integral answer is a resolution, not a section

Let

\[
\mathsf T_{\rm circ}
=\mathbb Z\langle c_{01},c_{12},c_{20}\rangle
\]

and let \(\mathsf K_{\rm rel}\) be the rank-one symmetry module carried by the
diagonal relation.  The canonical object is the nonsplit equivariant
extension

\[
\boxed{
0\longrightarrow\mathsf K_{\rm rel}
\xrightarrow{\Delta}
\mathsf T_{\rm circ}
\xrightarrow{\operatorname{cl}}
H_1(K_{2,3};\mathbb Z)
\longrightarrow0,
\qquad
\Delta(1)=c_{01}+c_{12}+c_{20}.}
\]

No denominator is needed if this extension is retained as the two-term
complex

\[
\mathcal R_{\rm circ}
=
[\mathsf K_{\rm rel}\xrightarrow{\Delta}\mathsf T_{\rm circ}].
\]

The index-three calculation obstructs an equivariant chain-level splitting;
it does not obstruct the quasi-isomorphism from this resolution to \(H_1\).
This is another instance of the project-wide rule: resolve first and only then
pass to homology or augmentation.

The relation-line character must not be silently identified with
\(\det H_1\).  Core exchange reverses every oriented circuit tag while its
action on \(\det H_1\) has determinant \(+1\).  The physical comparison may
therefore need an additional core-orientation twist.

The three tags are also the vertices of a Farey triangle: on the one-holed
torus, an \(S\)-move joins two curve classes intersecting once, and Hatcher's
pants complex fills a three-move cycle by a \(3S\) cell.  This makes that cell
a natural candidate realization of the relation generator.  It is not yet an
identification.  The \(3S\) cellular boundary is a cycle of moves, while
\(\Delta(1)\) is a relation among oriented curve classes; the required degree
shift and incidence map remain to be constructed.

## Exact comparison with resolved Brauer states

Among all

\[
3^5=243
\]

local contraction patterns, exactly nine carry a formal closed-circuit factor
\(D\).  Retaining support before applying \(D\mapsto1\), these nine states
split into precisely the three circuit supports above, each with multiplicity
three.

Every one of the 24 fundamental chord generators lands, up to orientation,
on one of these populated supports.  This is an exact individual-cycle bridge.

But:

- every one of the three tag pairs has algebraic intersection of absolute
  value one;
- no pair has a simultaneous noncrossing realization;
- none of the 243 resolved patterns contains two closed circuits.

Therefore

\[
H_1\not\cong
\{\text{noncrossing resolved circuits}\}
\]

as additive coefficient objects.  The rank-two homology and the resolved
curve states are related by the derived presentation
\(\mathcal R_{\rm circ}\), not a basis bijection.

## Correct next carrier

At the additive level the missing generator is exactly the relation generator
in \(\mathsf K_{\rm rel}\), one degree above the three tags.  At the
multiplicative level, let \(R_+\) and \(R_-\) be the two local smoothings of
one oriented intersection.  A further local generator has schematic boundary

\[
\boxed{dX_{a,b}=R_+(a,b)-R_-(a,b).}
\]

The coefficient and sign in the physical theory are not yet known; this
formula records only the required chain type.  The sought object is an
oriented Brauer--skein coefficient complex

\[
C_*\bigl(\mathsf{Curv}^{\rm sk}(\Sigma)\bigr)
\xrightarrow{\operatorname{cl}}
H_1(\Sigma)
\]

with a homotopy-coherent section, not a strict map from homology to a set of
non-overlapping curves.  Its crossing cell should carry the intersection form

\[
\omega:H_1\otimes H_1\longrightarrow\mathbb Z
\]

and its determinant parity.  This localizes the first genuinely non-strict
coherence to intersecting coefficient states; the undecorated marked-deletion
carrier remains strict.

## Evidence boundary

Proved by the exact certificate:

- the saturated integral Ward--\(H_1\) isomorphism;
- all stated symmetry and determinant characters;
- individual chord-to-populated-support matching;
- the three-tag relation and index-three equivariant splitting obstruction;
- pairwise intersection one and absence of simultaneous resolved pairs.

Not proved:

- a scalar-derived signed coefficient for either smoothing;
- that the existing surface carrier contains the required degree-one cell;
- compatibility with a separating or nonseparating physical Cut;
- a cyclic/BV chain map from the scalar first jet;
- higher-genus skein coherence.

## Subsequent outcome and next falsifier

Entry 60 proves that the ordinary 243-state transition graph cannot realize
the unpointed oriented relation by itself, but that no additive split is
needed: retaining
\(\mathsf K_{\rm rel}\to\mathsf T_{\rm circ}\) gives the canonical integral
resolution.  Entry 61 extends this to the all-\(m\)
\(A_{m-1}\) circuit resolution on \(K_{2,m}\).

Construct the one-crossing oriented Brauer--skein complex on the
once-punctured torus.  Determine its boundary coefficients from the actual
scalar first-jet Ward/contact identity, then test one separating and one
nonseparating Cut before applying \(D\mapsto1\).  If no signed filler exists
in the scalar-derived coefficient complex, the proposed cyclic dictionary is
falsified at the first handle.

## Primary source

- Allen Hatcher, *Pants Decompositions of Surfaces*, including the one-holed
  torus Farey triangulation and \(3S\) relation:
  <https://arxiv.org/abs/math/9906084>.

## Internal dependencies

- Entry 46: resolved closed-circuit Brauer augmentation.
- Entries 49--52: marked-handle state and surface dictionaries.
- Entry 56: graph-multiplihedral sewing-stage carrier.
- Entry 57: off-shell Ward exact sequence and even endpoint gluing.
- Entry 58: general finite evidence for strict marked deletion.
- Entries 60--61: the integral nonsplit resolution and its all-\(m\)
  \(A\)-type extension.
- Working context: `research/nima/ward_brauer_math_context.md`.

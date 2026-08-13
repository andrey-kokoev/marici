# Rank-Four Saturation and the Full Associahedral Envelope

## Record

Date: 2026-08-13

Status: the rank-four test at twelve points confirms and sharpens the obstruction of entry 29.
The rank-three saturation does not cover the complete boundary of four of the five possible
rank-four dependency-block faces. Only the pure four-cube closes without new cells.

Adjoining the missing rank-three facets from the scalar associahedron completes every
four-dimensional boundary as an exact integral three-sphere, with full one-step deck covariance.

The repeated pattern identifies the correct source object: not an iterative list of selected
paths and repairs, but the full product-associahedron carried by each dependency block.

## Rank-four dependency partitions

At \(n=12\), every zero-core marked transfer has four physicalizing steps. Their distribution
among dependency chains is one of

\[
1+1+1+1,
\qquad
2+1+1,
\qquad
2+2,
\qquad
3+1,
\qquad
4.
\]

The corresponding four-dimensional scalar faces are

\[
I^4,
\qquad
K_2\times I^2,
\qquad
K_2\times K_2,
\qquad
K_3\times I,
\qquad
K_4.
\]

Here \(K_r\) denotes the \(r\)-dimensional associahedron, so

\[
K_1=I,
\qquad
K_2=\text{pentagon},
\qquad
K_3=\text{hexagon associahedron}.
\]

Their vertex counts are respectively

\[
16,\ 20,\ 25,\ 28,\ 42.
\]

The exact scalar face enumeration reproduces all five numbers.

## Boundary types

The rank-three facets of these products are determined by the ordinary product-face rule.

### Four-cube

\[
I^4
\]

has eight cube facets.

### Pentagon times square

\[
K_2\times I^2
\]

has

\[
5\ \text{cube facets}
\qquad\text{and}\qquad
4\ \text{pentagonal-prism facets}.
\]

### Pentagon times pentagon

\[
K_2\times K_2
\]

has ten pentagonal-prism facets.

### Hexagon associahedron times interval

\[
K_3\times I
\]

has

\[
3\ \text{cube facets},
\qquad
6\ \text{pentagonal-prism facets},
\qquad
2\ K_3\text{ facets}.
\]

### Four-dimensional associahedron

The facets of \(K_4\), the associahedron of a heptagon, correspond to the fourteen diagonals of
that heptagon:

\[
7\ \text{pentagonal-prism facets}
\qquad\text{and}\qquad
7\ K_3\text{ facets}.
\]

## Coverage by the rank-three saturation

The rank-three surfaces constructed in entry 29 cover the following facets:

| rank-four carrier | covered cubes | covered prisms | covered \(K_3\) | missing cubes | missing prisms | missing \(K_3\) |
|---|---:|---:|---:|---:|---:|---:|
| \(I^4\) | 8 | 0 | 0 | 0 | 0 | 0 |
| \(K_2\times I^2\) | 3 | 4 | 0 | 2 | 0 | 0 |
| \(K_2\times K_2\) | 0 | 6 | 0 | 0 | 4 | 0 |
| \(K_3\times I\) | 0 | 4 | 2 | 3 | 2 | 0 |
| \(K_4\) | 0 | 0 | 5 | 0 | 7 | 2 |

Thus

\[
\boxed{
\text{previous-rank saturation is not automatically face-complete
at the next rank}.
}
\]

The only exception is the fully independent partition \(1+1+1+1\), whose face is cubical.

## Parity grading of the missing facets

The new facets again split into same-core scalar refinements and core-raising physical
incidences.

For \(K_2\times I^2\), the two missing cubes are:

- one scalar;
- one physical.

For \(K_2\times K_2\), the four missing prisms are:

- two scalar;
- two physical.

For \(K_3\times I\), the five missing facets are:

- two scalar cubes;
- one physical cube;
- one scalar prism;
- one physical prism.

For \(K_4\), the nine missing facets are:

- five scalar prisms;
- two physical prisms;
- one scalar \(K_3\);
- one physical \(K_3\).

The asymmetry in the \(K_4\) prism counts is genuine. It reflects the directed marked transfer,
not a failure of deck covariance; one-step rotation carries the complete pattern to the opposite
polarity sheet.

As at rank three,

\[
\text{scalar facet}:p\mapsto p,
\qquad
\text{physical facet}:p\mapsto p+1.
\]

Higher coherence therefore cannot live on the physical-core poset alone.

## Scalar-side completion

Fix a marked rank-four face \(F_4\). Every missing rank-three carrier is an actual facet

\[
F_3\subset\partial F_4
\]

of the scalar associahedron. Its complete signed polygonal-facet boundary was constructed by the
rank-three scalar saturation of entry 29.

Orient all rank-three facets coherently. Along each shared rank-two face, the two induced
oriented surfaces agree with opposite incidence sign. Hence

\[
\boxed{
\partial
\left(
\sum_{F_3\subset\partial F_4}
\epsilon(F_3,F_4)\,[F_3]
\right)
=0.
}
\]

This is an exact cellular three-sphere relation. The computation retains the complete signed
rank-two surface on every rank-three facet; it does not infer closure from facet counts.

No coefficient is divided, no singular pairing is inverted, and no formal filler is introduced.
Every carrier belongs to the scalar presentation geometry.

## Exact twelve-point certificate

The exact marked occurrence counts are:

| rank-four carrier | marked occurrences | distinct unmarked faces |
|---|---:|---:|
| \(K_2\times I^2\) | 120 | 120 |
| \(I^4\) | 30 | 30 |
| \(K_2\times K_2\) | 30 | 30 |
| \(K_3\times I\) | 60 | 60 |
| \(K_4\) | 12 | 12 |

Thus \(252\) marked rank-four hypersurfaces are completed.

Entry 29 supplied \(1344\) marked rank-three surfaces. Rank-four face completion forces \(672\)
additional distinct marked rank-three facets:

\[
1344\longrightarrow 2016.
\]

Run:

    python -B research/nima/check_core_incidence_rank_four.py

The script verifies:

1. all five dependency-partition face types;
2. their exact vertex and facet profiles;
3. inherited rank-three coverage;
4. scalar/physical grading of every missing facet;
5. exact signed rank-two cancellation on each completed three-sphere;
6. full one-step rotation of sources, marks, faces, facets, surfaces, and orientations.

## The emerging all-rank formula

Let a local dependency block take \(r_a\) consecutive steps from chain \(a\), with

\[
r=\sum_a r_a.
\]

The rank-two, rank-three, and rank-four data all satisfy

\[
\boxed{
F_{\mathbf r}
\cong
\prod_a K_{r_a}.
}
\]

The direct monotone states occupy only

\[
\prod_a(r_a+1)
\]

vertices. The complete scalar face has

\[
\prod_a C_{r_a+1}
\]

vertices, where \(C_j\) is the Catalan number. The additional vertices and facets are exactly the
scalar refinements required for higher coherence.

This formula has a direct planar explanation. A consecutive block in one dependency chain is a
connected strip in the rooted dual tree. Removing its selected diagonals exposes one polygonal
region whose triangulation complex is \(K_{r_a}\). Blocks in distinct dependency chains are
separated by fixed diagonals and therefore contribute independent factors.

A formal all-arity proof now reduces to the following block-face lemma:

> The common dissection of all direct prefix states for a block
> \(\mathbf r=(r_a)\) has unresolved polygonal components of dimensions \(r_a\), one for each
> nonzero block, and no further unresolved component.

Once that lemma is written, the product-associahedron formula follows from the standard face
decomposition of the scalar associahedron.

## The full marked associahedral envelope

Define

\[
\operatorname{AssEnv}(\Phi_\epsilon)
\]

by assigning to every marked dependency block its complete face

\[
F_{\mathbf r}=\prod_a K_{r_a},
\]

not merely the monotone direct states or the facets inherited from smaller direct blocks. Its
cellular boundary includes every scalar and physical facet with the ordinary associahedral
incidence sign.

This definition absorbs the iterative saturations of entries 29 and 30 from the outset.

It has four immediate virtues:

1. all higher source coherences are supplied by actual scalar cells;
2. products over independent dependency chains are literal product faces;
3. the marked contact diagonal remains fixed on every face;
4. one-step rotation acts cellularly and exchanges the polarity sheets.

The envelope is the natural cofibrant or Stasheff-type source resolution suggested by the
earlier consultations, now embedded in the scalar geometry rather than freely adjoined.

## What rank four changes conceptually

After entry 29 one could still hope that a single rank-three repair would finish the incidence
problem. Rank four rules that out. The missing-facet phenomenon recurs whenever a dependency
block contains an associahedral factor of dimension at least two.

Therefore the correct program is not

\[
\text{direct paths}
\rightarrow
\text{rank-two repairs}
\rightarrow
\text{rank-three repairs}
\rightarrow\cdots.
\]

It is

\[
\text{direct marked transfer}
\rightarrow
\operatorname{AssEnv}(\Phi_\epsilon)
\rightarrow
\text{coefficient cosheaf}
\rightarrow
\text{filtered twisted-chain comparison}.
\]

The first arrow is now concrete. The remaining difficulty is transporting the full envelope,
including its forced same-core and core-raising faces, into the physical chain theory.

## Epistemic boundary

This entry establishes exact rank-four scalar presentation closure at twelve points and provides
strong evidence for the all-rank product-face formula.

It does not yet establish:

1. the formal all-arity block-face lemma;
2. a coefficient cosheaf compatible with every scalar and physical facet;
3. a QTDS target for the newly forced higher cells;
4. a loaded Pochhammer or logarithmic Cousin chain map;
5. acyclicity of the comparison kernel;
6. a canonical twisted-form representative;
7. chain-level factorization naturality of \(\mathsf J\).

The full scalar associahedral envelope is a correctly typed source candidate, not yet the
intrinsic half-object itself.

## Primary next step

Do not continue rank by rank unless needed as a regression test. Prove the block-face lemma and
construct the cellular coefficient system.

For a marked cell \((d,F_{\mathbf r})\), the coefficient system must simultaneously encode:

- the contact label \(-X_d\);
- retained physical denominators;
- same-core scalar-refinement maps;
- physical-core Gysin or residue maps;
- regional tensor products;
- the polarity sign local system.

Then seek a finite-\(\alpha'\) comparison

\[
\chi_{\rm Ass}:
C_*\bigl(\operatorname{AssEnv}(\Phi_\epsilon);\mathcal L_J\bigr)
\longrightarrow
\operatorname{gr}\,C_*^{\rm Poch/Cousin}
\]

whose boundary on every forced facet is the already known lower-dimensional transport.

The smallest decisive target is the universal missing pair in

\[
K_2\times I:
\]

one scalar square and one physical square. If their loaded-current images can be constructed
compatibly, the mechanism tensors into many of the higher missing facets. If not, the
half-object fails at the first mixed scalar/physical higher-coherence square.

## Decision

Promote:

> The scalar-derived QTDS presentation has a canonical full marked associahedral envelope.
> Rank four proves that iterative lower-rank carriers are insufficient, while complete
> product-associahedral faces close integrally and deck-equivariantly. The unresolved problem is
> no longer which scalar cells to add, but how to equip those cells with the physical coefficient
> cosheaf and transport them to the filtered twisted-chain theory.

The next high-value Nima result should be the all-rank block-face lemma or the universal mixed
scalar/physical square comparison—not another amplitude equality.

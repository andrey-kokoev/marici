# All-Rank Block-Face Lemma and Associahedral Envelope Theorem

## Record

Date: 2026-08-13

Status: the product-associahedron formula conjectured in entries 29 and 30 follows at all even
arity from the dual-tree structure of the direct Catalan transfer.

For every marked source, every transfer prefix, and every finite block of future
physicalizing steps, the unique scalar face containing all direct block states is

\[
\boxed{
F_{\mathbf r}
\cong
\prod_a K_{r_a},
}
\]

where \(r_a\) is the number of consecutive selected steps taken from dependency chain \(a\).

This proves the full scalar-side associahedral envelope and supplies all higher cellular source
coherences. It does not yet equip that envelope with the physical coefficient cosheaf or map it
to the filtered Pochhammer/Cousin complex.

## Setup

Fix:

- an even multiplicity \(n\);
- a zero-core scalar triangulation \(T\);
- a marked scalar diagonal \(d\in T\);
- a polarity sheet \(\epsilon\).

The direct Catalan construction of entry 26 gives disjoint ordered dependency chains

\[
C_a=(f_{a,1},\ldots,f_{a,\ell_a}).
\]

Choose an arbitrary transfer prefix

\[
\mathbf p=(p_a),
\qquad
0\leq p_a\leq\ell_a,
\]

and denote the resulting triangulation by

\[
T_{\mathbf p}.
\]

Now choose a nonnegative block vector

\[
\mathbf r=(r_a),
\qquad
0\leq r_a\leq\ell_a-p_a,
\]

not identically zero. The selected future block in chain \(a\) is

\[
S_a
=
\{f_{a,p_a+1},\ldots,f_{a,p_a+r_a}\},
\]

and

\[
S=\bigsqcup_a S_a,
\qquad
r=|S|=\sum_a r_a.
\]

The direct block states are all

\[
T_{\mathbf p+\mathbf q},
\qquad
0\leq q_a\leq r_a.
\]

They form the monotone grid

\[
\prod_a [0,r_a].
\]

## Fixed-complement lemma

Let

\[
D_{\mathbf p,\mathbf r}
=
\bigcap_{0\leq\mathbf q\leq\mathbf r}
T_{\mathbf p+\mathbf q}
\]

be the common dissection of every direct block state.

Then

\[
\boxed{
D_{\mathbf p,\mathbf r}
=
T_{\mathbf p}\setminus S.
}
\]

### Proof

Every diagonal outside \(S\) is untouched by every flip in the chosen block, so it belongs to
every direct state.

Every selected diagonal \(f\in S\) is absent after its own flip, so it cannot belong to the
intersection.

Every replacement diagonal created during the block is absent in the initial state
\(T_{\mathbf p}\), which is itself one of the direct block states, so no replacement diagonal
belongs to the intersection.

There are no other changing diagonals. Hence the intersection is exactly
\(T_{\mathbf p}\setminus S\).

In particular,

\[
|T_{\mathbf p}|-|D_{\mathbf p,\mathbf r}|=r,
\]

so the corresponding associahedral face has dimension \(r\).

The marked diagonal is never selected:

\[
d\notin S.
\]

Therefore

\[
d\in D_{\mathbf p,\mathbf r}
\]

and is fixed on the entire face.

## Dual-tree block lemma

Consider the ordinary dual tree of the current triangulation \(T_{\mathbf p}\). Its vertices are
the triangular regions and its internal edges are the triangulation diagonals.

The rooted construction of entry 26 has the following property:

> The selected future diagonals form a disjoint union of paths in the dual tree, one path for
> each dependency chain.

A consecutive block \(S_a\) is therefore a path segment with \(r_a\) dual edges. It joins exactly

\[
r_a+1
\]

triangles. The union of those triangles is a polygon with

\[
(r_a+1)+2=r_a+3
\]

vertices.

Distinct chain blocks lie in distinct selected-edge components. Their polygonal regions are
separated by diagonals retained in \(D_{\mathbf p,\mathbf r}\).

Thus cutting along the common dissection leaves precisely one nontriangular unresolved region

\[
R_a
\]

for each nonzero \(r_a\), with

\[
|R_a|=r_a+3.
\]

Every other region is a triangle and contributes no positive-dimensional factor.

## Associahedral face theorem

A standard face of a polygon associahedron is the product of the associahedra of the polygonal
regions left unresolved by its defining dissection.

Applying that theorem to \(D_{\mathbf p,\mathbf r}\) gives

\[
F(D_{\mathbf p,\mathbf r})
\cong
\prod_{a:r_a>0}
K_{|R_a|-3}.
\]

Since \(|R_a|=r_a+3\),

\[
\boxed{
F(D_{\mathbf p,\mathbf r})
\cong
\prod_{a:r_a>0}K_{r_a}.
}
\]

This proves the block-face formula at arbitrary rank and arbitrary even multiplicity.

## Vertex count

The \(r_a\)-dimensional associahedron \(K_{r_a}\) is the triangulation polytope of an
\((r_a+3)\)-gon. It has

\[
C_{r_a+1}
\]

vertices. Therefore

\[
\boxed{
|\operatorname{Vert}F_{\mathbf r}|
=
\prod_{a:r_a>0} C_{r_a+1}.
}
\]

By contrast, the direct monotone grid has only

\[
\prod_{a:r_a>0}(r_a+1)
\]

vertices.

The difference

\[
\prod_a C_{r_a+1}
-
\prod_a(r_a+1)
\]

measures the scalar refinement states omitted by the direct transfer presentation. Those states
are not optional: entries 29 and 30 show that their faces are forced by higher cellular closure.

## Recovery of the low-rank carriers

The theorem simultaneously explains all exact local types already found.

At rank two:

\[
1+1
\longmapsto
K_1\times K_1=I^2,
\]

the square, while

\[
2
\longmapsto
K_2,
\]

the pentagon.

At rank three:

\[
1+1+1\longmapsto I^3,
\]

\[
2+1\longmapsto K_2\times I,
\]

\[
3\longmapsto K_3.
\]

At rank four:

\[
1+1+1+1\longmapsto I^4,
\]

\[
2+1+1\longmapsto K_2\times I^2,
\]

\[
2+2\longmapsto K_2\times K_2,
\]

\[
3+1\longmapsto K_3\times I,
\]

\[
4\longmapsto K_4.
\]

The vertex counts are respectively

\[
4,\ 5;
\]

\[
8,\ 10,\ 14;
\]

and

\[
16,\ 20,\ 25,\ 28,\ 42.
\]

## Full marked associahedral envelope

For every marked direct-transfer datum \((T,d,\epsilon)\), define

\[
\operatorname{AssEnv}(T,d,\epsilon)
\]

to contain the complete face \(F_{\mathbf r}\) for every prefix \(\mathbf p\) and every nonzero
block \(\mathbf r\), with the ordinary cellular incidence relations inherited from the scalar
associahedron.

The block-face theorem makes this definition intrinsic and nonrecursive:

\[
\operatorname{AssEnv}(T,d,\epsilon)
=
\bigcup_{\mathbf p,\mathbf r}
F(D_{\mathbf p,\mathbf r}).
\]

No rank-by-rank repair choices remain.

Every cell is:

- an actual scalar presentation cell;
- canonically determined by a common dissection;
- a product of standard associahedra;
- marked by a diagonal fixed on the whole cell;
- compatible with products over independent dependency chains.

## All higher scalar-source coherence

Each \(F_{\mathbf r}\) is a convex polytope. Its cellular chains satisfy

\[
\partial^2=0.
\]

Products of independent chain blocks carry the standard product differential

\[
\partial(x\otimes y)
=
\partial x\otimes y
+
(-1)^{|x|}x\otimes\partial y.
\]

Therefore the complete envelope supplies every higher Stasheff coherence on the scalar source
side. Squares, pentagons, rank-three surfaces, and rank-four hypersurfaces are its first visible
layers, not separate structures requiring independent choices.

This closes the purely scalar **carrier-existence** problem.

It does not close the comparison-map problem because a source cellular boundary need not have a
canonical loaded-current image.

## Deck covariance

One-step rotation \(\rho\):

- rotates the zero-core source;
- rotates the mark;
- sends every dependency chain to the corresponding chain on the opposite polarity sheet;
- sends prefixes and consecutive blocks to prefixes and blocks of the same length;
- rotates the common dissection.

Hence

\[
\rho F_{\mathbf r}^+
=
F_{\mathbf r}^-\rho
\]

and therefore

\[
\boxed{
\rho\operatorname{AssEnv}(T,d,+)
=
\operatorname{AssEnv}(\rho T,\rho d,-).
}
\]

The polarity torsor survives, but the complete envelope descends equivariantly without choosing
an absolute sheet.

## Regional and partial-core extension

At a partial physical core \(P\), entry 27 decomposes the scalar cell into independent even
regions. The marked Catalan transfer and its dependency chains are regional.

Applying the block-face theorem region by region gives

\[
\operatorname{AssEnv}_{P}
\cong
\prod_{R\in\mathcal R(P)}
\operatorname{AssEnv}_{R}.
\]

Thus the all-rank scalar carrier is monoidal under fixed-core cuts. Blocks lying in different
regions contribute independent product factors.

The unresolved issue is compatibility of the physical coefficient maps as the core itself
changes.

## Exact exhaustive certificate through twelve points

The standard-library audit checks every marked zero-core source, both polarities, every transfer
prefix, and every nonempty future block through \(n=12\).

At twelve points the exact block counts are:

| rank | partition | complete face vertices | marked blocks |
|---:|---|---:|---:|
| 1 | \(1\) | 2 | 4,368 |
| 2 | \(1+1\) | 4 | 2,340 |
| 2 | \(2\) | 5 | 936 |
| 3 | \(1+1+1\) | 8 | 480 |
| 3 | \(2+1\) | 10 | 720 |
| 3 | \(3\) | 14 | 144 |
| 4 | \(1+1+1+1\) | 16 | 30 |
| 4 | \(2+1+1\) | 20 | 120 |
| 4 | \(2+2\) | 25 | 30 |
| 4 | \(3+1\) | 28 | 60 |
| 4 | \(4\) | 42 | 12 |

For every block, the audit verifies:

1. \(D_{\mathbf p,\mathbf r}=T_{\mathbf p}\setminus S\);
2. one selected dual-tree component per nonzero chain block;
3. a component with \(r_a\) edges joins \(r_a+1\) triangles;
4. its exposed polygon has \(r_a+3\) vertices;
5. the product-Catalan vertex count;
6. exact one-step rotation of the full marked block record.

Run:

    python -B research/nima/check_associahedral_envelope.py

The proof is all-arity; the computation is an exhaustive low-rank regression certificate.

## Candidate pre-half-object

The source-side result suggests the correctly typed pre-half-object

\[
\mathsf J_{\rm pre}
=
C_*^{\rm cell}
\left(
\operatorname{AssEnv}(\Phi);
\mathcal L_J
\right),
\]

where \(\mathcal L_J\) must be a coefficient cosheaf encoding the scalar associated grade.

The present theorem constructs the cellular carrier

\[
C_*^{\rm cell}\bigl(\operatorname{AssEnv}(\Phi)\bigr).
\]

It does not yet construct \(\mathcal L_J\).

That distinction prevents the source topology from being mistaken for the physical half-object.

## What is now established

1. the common direct-state dissection is the current triangulation minus the selected block;
2. dependency-chain blocks are path components in the triangulation dual tree;
3. a length-\(r_a\) block exposes an \((r_a+3)\)-gon;
4. distinct blocks give independent unresolved regions;
5. every block face is \(\prod_a K_{r_a}\);
6. its vertex count is \(\prod_a C_{r_a+1}\);
7. the full marked associahedral envelope exists at all rank and all even arity;
8. all scalar-source higher cellular coherences follow from its ordinary boundary;
9. the construction is deck-equivariant;
10. it tensors over partial-core regions.

## What remains open

The theorem does not provide:

1. the coefficient cosheaf \(\mathcal L_J\);
2. scalar- and physical-facet transition maps;
3. a QTDS chain target for higher cells;
4. a filtered Pochhammer/Cousin comparison;
5. an acyclic composition-stable comparison kernel;
6. a canonical twisted de Rham representative;
7. chain-level identification with \((\operatorname{Pf}'A)^2\);
8. a resonance-safe worldsheet boundary construction.

Accordingly, factorization naturality of the intrinsic half-object remains conditional, although
the scalar carrier and its complete higher coherence are no longer missing.

## Primary frontier

The highest-value next object is the coefficient cosheaf

\[
\mathcal L_J
\]

on the envelope.

Its restriction maps must distinguish two universal facet types:

\[
\text{scalar refinement}:p\longmapsto p,
\]

\[
\text{physical incidence}:p\longmapsto p+1.
\]

The minimal mixed coherence test is the pentagonal prism

\[
K_2\times I.
\]

Its boundary contains the inherited pentagon homotopies together with exactly two forced square
facets, one scalar and one physical. Construct loaded-current images for that pair and verify
that the complete signed prism boundary vanishes at finite nonresonant \(\alpha'\).

If this succeeds, product faces propagate the mechanism to a large part of the envelope. If it
fails, the obstruction is now localized to a universal mixed scalar/physical square rather than
to an unspecified global chain map.

## Decision

Promote:

> Every dependency block in the scalar Catalan transfer carries a canonical product-associahedron
> \(\prod_a K_{r_a}\). Their union is the full marked associahedral envelope, which supplies all
> higher scalar-source coherences integrally, regionally, and deck-equivariantly.

The scalar carrier problem is solved. The Nima frontier is now the physical coefficient cosheaf
and its filtered twisted-chain realization.

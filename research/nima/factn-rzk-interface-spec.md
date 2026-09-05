# `Fact_n` Rzk interface specification

## Claim boundary

The first formal target is combinatorial. It constructs the refinement category of polygon dissections and the product decomposition of the upper interval above a dissection. It does not yet construct geometric associahedra, differential forms, residues, or amplitudes.

## Finite polygon data

For fixed `n`, require:

- `Vertex_n`, a finite discrete type;
- a cyclic betweenness relation `Cyclic(a,b,c)`;
- `Diagonal_n`, unordered pairs of distinct nonadjacent vertices;
- `Crosses : Diagonal_n -> Diagonal_n -> U`, valued in propositions;
- `Dissection_n`, finite families of diagonals with pairwise noncrossing proof.

Equality of vertices and diagonals must be discrete. Pairwise compatibility proofs must be propositions so they do not create extra arrows.

## Refinement

Define

```text
Refines(D,D') := every diagonal of D occurs in D'.
```

Required laws:

```text
refines-id    : Refines(D,D)
refines-comp  : Refines(D,D') -> Refines(D',D'') -> Refines(D,D'')
refines-prop  : is-prop(Refines(D,D'))
refines-antisym : Refines(D,D') -> Refines(D',D) -> D = D'
```

The direction is coarse to fine: an arrow adds compatible diagonals. Antisymmetry requires extensional equality of finite diagonal families, not merely equality of compatibility witnesses.

## Simplicial type

`Fact_n` is the Rezk nerve of this refinement poset:

- 0-simplices are dissections;
- 1-simplices are refinement witnesses;
- 2-simplices are composable pairs and their composite inclusion;
- an `m`-simplex is a chain `D_0 <= ... <= D_m`.

The Segal map is an equivalence because an `m`-chain is uniquely reconstructed from its adjacent refinement arrows and all refinement hom-types are propositions. Rezk completeness follows because an invertible refinement gives inclusions both ways, and antisymmetry identifies its endpoints.

This must be constructed; the existing generic Rzk modules only consume `is-segal` or `is-rezk` as premises.

## Regions

For `D : Dissection_n`, define `Regions(D)` as the finite type of connected polygonal components obtained after cutting along every diagonal in `D`. Each region carries an induced cyclic order and boundary-edge inclusion into the original polygon.

Required one-cut theorem: if `e` is compatible with `D` and lies in region `R`, then

```text
Regions(D union {e})
  = (Regions(D) minus {R}) union {R_left(e), R_right(e)}.
```

The equality should be an equivalence of finite region types preserving their induced cyclic orders, not equality of cardinalities.

## Residual face as an upper interval

Define the combinatorial residual face

```text
Face(D) := Σ (D' : Dissection_n), Refines(D,D').
```

For each region `R`, let `Fact(R)` be its dissection refinement type. The precise product theorem is

```text
face-product(D) : Face(D) ≃ Π (R : Regions(D)), Fact(R).
```

Forward map: restrict each added diagonal of `D'` to the unique region of `D` containing it.

Inverse map: take the union of the regional dissections with `D`.

The proofs must establish:

1. every diagonal compatible with `D` belongs to a unique region;
2. regional restrictions remain noncrossing;
3. union preserves noncrossing across distinct regions;
4. restriction after union and union after restriction are inverse.

## Naturality under refinement

For `r : Refines(D,D')`, define:

- `face-restrict(r) : Face(D') -> Face(D)` by composition of refinements;
- `region-refine(r)`, which replaces each region of `D` by the regions induced by `D'` inside it;
- `product-restrict(r)` by regrouping the `Fact(R')` factors over their parent regions.

The central theorem is a homotopy-commutative square:

```text
face-product(D) (face-restrict(r)(x))
  = product-restrict(r)(face-product(D')(x)).
```

For two composable refinements, these comparison paths must agree with the retained Rzk two-simplex. For three refinements, agreement is inherited from the Segal associativity filler rather than postulated as another equation.

## Implementation order

1. finite discrete vertices and unordered diagonals;
2. crossing and dissections;
3. refinement laws and propositionality;
4. Rezk nerve `Fact_n`;
5. region type and unique-region lemma;
6. `face-product` equivalence;
7. one-refinement naturality;
8. compatibility with two- and three-simplex fillers.

## First acceptance test

Implement `n=5` without a generic finite-set library shortcut. The five-gon has 11 dissections: one empty dissection, five single-diagonal dissections, and five triangulations. Verify that the upper interval over a single diagonal is equivalent to the dissection type of the unique quadrilateral region and that both two-step triangulation refinements compose to the same terminal object. This tests objects, arrows, regions, face products, Segal composition, and naturality before generic `n` recursion.

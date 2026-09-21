# The seam realization of the nonsplit connecting map requires a two-stage correspondence

The relation-to-seam comparison now determines the remaining constructor.

Let

    P = I^2,
    C = I/I^2,
    delta : C -> P[1]

be the source-generated nonsplit triangle. The ordinary one-seam derivative gives an injective map

    j_1 : C -> H_seam^(-1),

but annihilates P. The labelled joint two-seam construction gives an injective map

    j_2 : P -> H_joint^(-2),

where the middle vertex and both seam positions are retained.

There is therefore no single one-seam chain map whose degree-minus-one component realizes the full triangle: its Leibniz rule forces `D(I^2)=0`. The required object is a two-stage correspondence

    H_joint^(-2)  <-  P  <-delta-  C  ->  H_seam^(-1),

with the middle arrow retained as source extension data. Equivalently, form the mapping cone of the transported connecting morphism

    j_2 delta : C -> H_joint(P)[1],

provided the joint-seam target is equipped with the source action and the comparison is defined on the full extension, not only on its two graded pieces.

The compatibility condition is the chain-level square

    j_2 delta  =  Delta_seam j_1,

where `Delta_seam` is a typed, middle-label-preserving seam connecting map. It cannot be obtained by applying the ordinary path derivative after composition, because that composite is zero on `P`.

Thus the missing constructor is a **two-stage seam correspondence with an explicit connecting map**, not another homology group and not a choice of vector-space splitting. Its source definition is canonical from the nonsplit exact sequence; its target must retain the joint two-seam product carrier.

## Immediate finite test

Use the 24 product basis indexed by a two-event middle vertex and a pair of local diamond relations. For each basis product:

1. compute its two local seam images;
2. retain the middle label;
3. apply the source extension action defining `delta`;
4. compare with the proposed connecting map on the conormal basis.

The test must verify the chain identity, not only ranks. A rank-24 joint minor proves injectivity of `j_2`, but does not by itself construct `Delta_seam` or prove compatibility with `delta`.

Until that square is supplied, the conormal and product seam realizations are faithful separately but are not yet a realization of the nonsplit attachment as one derived object.

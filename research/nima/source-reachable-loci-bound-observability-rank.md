# Source-reachable loci bound observability rank

## Result

Let (P) be the preparations admitted by a source grammar, and let

[
phi:Plongrightarrow V
]

be their feature map into a finite-dimensional affine feature space. Suppose each
measurement row has the affine form

[
r(p)=(1,phi(p)).
]

For every finite probe family (p_1,ldots,p_N), the resulting observation
matrix satisfies

[
operatorname{rank} R
le 1+dimoperatorname{aff}phi(P).
]

Consequently, full observation of a carrier with one normalization coordinate
and (d) independent residue coordinates requires the source-reachable feature
locus to affinely span all (d) residue directions.

This is a source-grammar gate before frame optimization. Repetition, copying,
or denser sampling within the same affine locus cannot create a missing
direction.

## Proof

Choose an affine origin (v_0) in the affine hull of (phi(P)), and write

[
phi(p)=v_0+w(p)
]

with every (w(p)) in the associated translation space (W). Every row then
lies in the linear space spanned by ((1,v_0)) and ((0,W)). That space has
dimension at most (1+dim W), proving the bound.

The bound is sharp precisely when the selected preparations affinely span the
reachable locus.

## Optical instantiation

Aspect's frozen post-balanced-splitter grammar reaches only

[
phi(arphi)=(cosarphi,sinarphi,0).
]

Its affine hull has dimension two. Therefore every probe family formed at that
interface has observation rank at most three. No number of equatorial phases
can recover the missing Z-sensitive residue.

A calibrated bypass/preparation selector adds a pole outside that plane. The
reachable affine hull then becomes three-dimensional, and four-state
faithfulness becomes possible. Within this constrained grammar the optimum is
one pole plus three equatorial phases separated by one third of a turn, with
condition number approximately (2.48421).

A variable-ratio splitter reaches arbitrary latitude and admits the tetrahedral
optimum with condition number (sqrt 3).

Thus these are three different claims:

1. the target feature space algebraically contains a good frame;
2. the source grammar reaches a spanning locus;
3. the admitted preparations can be jointly executed and stably completed.

Only the second is settled by the affine-hull theorem.

## Cross-lane transfer

### Flavor

Before adding fitted observables, compute the affine hull of the feature images
produced by the admitted flavor-source operations. If its dimension is below
the residue carrier dimension, no multiplicity of readouts from that same
grammar can identify all residue coordinates. The first missing object is then
a preparation or intervention constructor, not another numerical estimator.

### Strominger

A magnetic-only source grammar can be fully faithful on its reachable magnetic
locus while having a structural zero column in the electric direction. More
magnetic ports cannot repair that defect. The missing electric observer must
also be reachable in the same typed acquisition interface before a joint
conditioning claim is meaningful.

### Grothendieck

Apply the theorem only after choosing a finite jet carrier and deriving its
source feature map. If the admitted seam repairs occupy a proper affine
subspace of the required odd-jet directions, repeated seam sampling cannot
close the next odd jet. This does not itself prove the observed third-jet
failure: the theta/Tate feature map must be constructed first.

### Kitaev

Repeated controls or preparations inside one reachable control orbit do not
increase affine span. A missing logical or character direction requires a
source-authorized constructor that leaves the old orbit's affine hull, not a
duplicate observation in a new presentation.

## Finite falsifier

Given an alleged faithful source-generated probe family, form its observation
matrix and compute either:

- a nonzero vector in its right kernel; or
- the affine rank of the reachable feature rows.

If

[
dimoperatorname{aff}phi(P)<d,
]

faithfulness on (d) residue coordinates is impossible. A proposed repair is
genuine only if its new preparation has feature image outside the previous
affine hull and is authorized by the source grammar.

## Boundary of the theorem

Affine span is necessary, not sufficient. It says nothing by itself about:

- conditioning;
- noise robustness;
- simultaneous resource availability;
- compatibility of measurements;
- completion stability;
- authority for the preparation constructor.

Those remain separate typed gates.

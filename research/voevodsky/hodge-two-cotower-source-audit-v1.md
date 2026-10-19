# Hodge two-cotower source-interface audit

## Question and scope

Execute the workbench's bounded source audit: compare the RH composition/source-coherence towers with actual Hodge maps, test one available square and grading, and stop at the first missing source map. SCC obligations: typed forward realization and mixed interchange, then readout descent. No physical time or identification of simplex dimension with codimension is supplied.

## Actual interfaces

| Role | RH source | Hodge data actually supplied |
| --- | --- | --- |
| Compositional objects | Graded domains with d,Q,N and ordered composites | CH^3(X)_Q and Hdg^3(X,Q), not indexed towers |
| Source realization | Labelled theta/Tate constructors and their ordered incidence | Algebraic cycles, structure sheaves and mapped fundamental chains |
| Comparison | Source realization versus composition, with independently supplied mixed cell | cl:CH^3(X)_Q -> Hdg^3(X,Q), natural under specified algebraic isogenies |
| Reciprocal orientation | Left/right RH sectors and contraction signs | No corresponding pair of Hodge sectors or reciprocal contraction supplied |
| Lattice translation | Barycentric source objects and conductor-transfer maps | No X_a or elementary transfer d_ij(a) assigned to the 120 lattice positions |
| Central mark | A proposed comparison at the common center | Fixed alpha is a cohomology class; it is not a supplied algebraic cycle |

The two RH towers are independent structures, not a construction of two Hodge cotowers. A candidate role assignment is not an indexing system, inverse system, graded double category, or realization functor. The first missing object is the Hodge-side indexed source assignment a -> X_a together with an actual elementary transfer. There is therefore no licensed mixed lattice square to compute for alpha.

## A genuine Hodge square is available

For the algebraic finite etale isogeny f=2+i, the already supplied interface is

    CH^3(X)_Q --f^*--> CH^3(X)_Q
        | cl                | cl
        v                   v
    Hdg^3(X,Q) --F--> Hdg^3(X,Q).

Standard cycle-class naturality gives cl f^*=F cl, including ordered powers. The polynomial projector P_CH therefore obeys cl P_CH=P(F) cl. This is a genuine mixed algebraic/cohomological comparison; it closes, rather than exhibiting a new defect. It preserves algebraic classes, not necessarily their individual representatives or the central-i invariant subspace.

On the fixed Hodge basis (E^3,R,I), F is diag(125, [[-117,44],[-44,-117]]) and P(F)=diag(0,1,1). The checker evaluates the source polynomial exactly on this matrix. It verifies the known divisor line and both Weil directions. These cohomological calculations do not compute CH^3 or prove the naturality theorem; that theorem is standard imported mathematics. No all-cycle annihilation is inferred.

## The recovered quadratic-stage clue and its correction

The RH two-tower note uses Pauli X,Z: X^2=Z^2=I but XZ=-ZX. The two ordered routes have the same squared norm on every input while differing as operators. This is specifically loss of a route's central phase, not a source vector in the kernel of B. Both routes are invertible, so they have no nonzero dark input.

The companion Koszul-normalization note corrects a possible false anomaly. If both crossed maps are genuinely source-odd, the required interchange sign is -1 and the normalized residual is I. If the prescribed interchange is ordinary/even, the same raw residual remains -I. Degrees must be derived from the source, not assigned after observing the residual.

For this Hodge square f^* and cl have cohomological degree zero. Classes of codimension three have degree six, which is even. Codimension p=3 alone does NOT authorize an odd Koszul assignment. Differentials in a resolution can be odd, but they are different arrows and require their actual complexes. One cannot transfer the Pauli sign to f^* and cl by naming two towers.

Thus the remembered quadratic-effects mechanism has a closer source: norms can forget the difference between two invertible realization routes. It is not yet an established Hodge defect, a dark kernel, or an empty realization fiber.

## Lattice audit

Eight vertices per edge gives seven intervals, degree-seven barycentric integer coordinates summing to seven, and 120 vertices. The source gives 343 unimodular top tetrahedra. The barycenter (1/4,1/4,1/4,1/4) is not a vertex, since 7/4 is not integral. The checker counts vertices and checks this obstruction; it does not construct all 343 simplices or a Hodge-valued simplicial map.

An ordinary category nerve can force higher composition identities once lower data are fixed. For a weak/higher target, the relevant independently supplied fillers depend on the exact target. No blanket claim that all horns or full boundaries fill is imported from the RH sketch. The missing Hodge target and edge assignment come before either option.

## Disposition

The bounded audit is complete with an INCONCLUSIVE source-binding disposition: a genuine cycle-class naturality square is identified and a quadratic route-phase-loss control is checked, but neither supplies the two indexed Hodge cotowers. The four substantive Hodge conjectures remain open and blocked. This is not a constructed binding, rejection of their existential claims, or permission to rerun the same search indefinitely.

Reopening requires actual Hodge lattice source objects and an elementary operation with its degree, domain, codomain and relation to cl. No new waiting-only successor is created. Base iteration52/pins55 and the fixed X,p,alpha are unchanged.

Sources: hodge-cycle-map-scope-v1.md; hodge-weil-projector-v1.md; hodge-cycle-packet-dictionary-v1.md; research/nima/rh-two-tower-four-structures-need-a-mixed-interchange-cell.md; research/nima/rh-cube-coherence-must-be-koszul-normalized.md; the eight-node pyramid note cited by the overlay. Verification is written imported mathematics plus finite exact controls, not formal certification or independent review.

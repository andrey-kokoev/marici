# Domain gate: the existing shared-leg matrix reader does not yet read the seam

## Question

Can the already retained shared-leg matrix fixture and its trace preparation/readout evaluate the seed triangle-incidence correction -Delta/4, without inventing matrix assignments?

## Inspected implementation

`checkers/check_shared_leg_dg_realization.py`, function `build`, declares:

- independent direct reference d:A->B;
- arrow-block legs ax_i:A->U and ay_j:U->B;
- state-block legs sx_i:A->V and sy_j:V->B.

Its values are explicit supplied matrices X_i=I+(i/3)H, Y_j=I+(j/5)K, d=2I. Its corners are Y_j X_i:A->B, and its mixed rectangle evaluates as (Y_j-Y_c)(X_i-X_r). `check_source_exchange_end_to_end.py` uses these fixture residuals for the separately declared preparation gamma*tr(Y_j X_i-d), gamma=1/4.

These are legitimate operations on that fixture. None of these definitions assigns a matrix to the actual seed arrows AB, BC, CA, AD, DB, BA.

## Obstruction to the proposed direct reuse

The seam has x_i:A_seed->B_seed and y_j:B_seed->A_seed. To map x_i to fixture X_i requires

    F(A_seed)=A_fixture, F(B_seed)=U_fixture.

Mapping its return y_j to fixture Y_j also requires

    F(B_seed)=U_fixture, F(A_seed)=B_fixture.

The two requirements on F(A_seed) conflict: A_fixture and B_fixture are distinct source objects. The state block has the same issue with V instead of U. Choosing indices i,j does not fix it.

Equivalently, the seam corners are endomorphisms of A_seed; the fixture corners are maps between distinct endpoints. Equal 2x2 array dimensions do not identify those typed domains. Treating every object as the same vector space could support a NEW matrix realization, but is not a retained source map into this existing DG path fixture.

The fixture's underlying degree-zero graph is directed acyclic. A functor sending a seed cycle to nonempty paths cannot close it there. Collapsing the strongly connected seed to identities would destroy precisely the nontrivial path distinctions under test; it is not the proposed assignment to X and Y.

## Result

The required seed corner family is outside the supplied adapter's current typed domain. Therefore this turn reports neither zero nor nonzero numerical seam response. The existing nonzero fixture rectangle is not evidence of a nonzero seed triangle signal.

The bilinear covariance identity and the retained original-triangle incidence remain valid. They do not close this domain gate. In particular, importing a convenient 2x2 subrectangle and reporting its trace would add both a source identification and a value assignment that have not been justified.

## Precise missing input

A future constructor must explicitly supply a representation of the actual seed paths, including how the shared-seam return composes back to the starting object, before applying the existing trace/readout recipe. Alternatively it must supply a justified transport/closure from the fixture's output object to its input object and prove that this corresponds to the actual seed return. Merely inserting an inverse reference matrix would be a new assumption; no such insertion is made here.

Weights, state preparation and detector calibration remain separate conditional inputs even after a typed representation is supplied.

## Follow-up search: the semantic binding is already an identified missing input

The next search recovered `actual-seed-pointed-binding-field-audit.md`. It inspected the actual seed constructors: the primitive packets retain label, source and target; the spectral/incidence implementations add an explicitly chosen coefficient representation. They do not supply the semantic carrier maps on the six primitive arrows. Its existing `agda/SeedPointedTriangleBinding.agda` is a requirements contract, not a concrete seed instance.

`co-constructed-seam-reference-hypothesis.md` independently preserves the same boundary: BA is a retained return path, not an inverse map; the parallel direct/indirect paths have not acquired numerical responses. `channel-triangle-map.md` uses supplied abelian unit channel weights on a different labelled triangulation construction and explicitly disclaims source authority. It cannot provide the missing seed assignments.

For the narrower MATRIX task here, the missing input is a carrier space at each seed vertex and a map for each primitive arrow, with its source justification and readout compatibility. Primitive maps need not be invertible merely to evaluate path products. The stronger native pointed-equivalence/admission requirements in the recovered audit apply only if claiming that stronger binding; they should not be smuggled into the linear representation task as necessary assumptions.

Once such a representation is supplied, ordinary composition defines all four corners, and the covariance calculation requires no new formula. But neither the reviewed seed definitions nor the existing fixture chooses that representation. Merely using the same vector space at all vertices, setting unit matrices, or declaring BA inverse to AB would be a NEW interpretation.

### Stopping decision

Do not build another abstract contract or numerical example: the contract gap is already explicit. Keep the proven triangle-context incidence and conditional covariance law. Resume numerical synthesis only when a concrete semantic seed binding is located or the operator explicitly selects an externally specified representation hypothesis. No source-derived matrix response is claimed by this bounded search.

## Evidence scope

This is a source-definition/type inspection, not a new numerical execution. The cited fixture and preparation definitions were read directly. No matrix values, bridging arrows, new reader, or formal proof were added. Existing covariance and table-family verification results are unchanged.

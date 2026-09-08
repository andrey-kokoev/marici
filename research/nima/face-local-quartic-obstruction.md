# Face-local constant refinement obstruction

## Question

Can distinct constant allocations for distinct quartic faces restore the six-point triangle quadrics while keeping the source amplitude unchanged?

## Claim boundary

For each of the 15 four-element subsets q of the six polygon vertices, introduce a constant a_q. A quartic face with sorted cyclic labels q0<q1<q2<q3 allocates a_q to (q0,q2) and 1-a_q to (q1,q3). The same face receives the same parameter wherever it appears. For a diagram with two quartic vertices, multiply their allocations. This is a test of context-independent local constant splitting, not arbitrary source-preserving changes of presentation.

Each graph's refinement allocations sum identically to one. The actual source coefficients, contact normalization and pole residues therefore remain unchanged. Canceled propagator factors make the resulting 14 triangulation weights polynomial in formal channels, with no added poles.

## Disposition

All three six-point rectangle identities were expanded as polynomials in the nine channel variables and g,lambda. Equating coefficients gives 30 distinct polynomial equations in the 15 face parameters. Their exact grevlex Groebner basis over Q is {1}. Thus no simultaneous solution exists, even with complex constants, for generic formal channels and couplings. The computation completed within its 30-second execution cap; input caps were 300 equations of total parameter degree at most four. The actual constraints are recorded verbatim in results/face_local_quartic.json.

This strengthens the previous universal-alpha obstruction: different labelled faces do not rescue a context-independent constant rule with independent local splitting at the two quartic vertices. The cubic source remains a valid baseline; the contradiction is for a polynomial identity in the full cubic-plus-quartic source, not a claim about the special lambda=0 locus. Fixed-dimensional kinematic restrictions and momentum-dependent or diagram-context-dependent allocations remain outside scope.

The result supplies no higher homotopy or physical cohomology class. It supports the diagnosis that forcing genuine quartic interactions into a triangle-only local presentation loses source structure. In particular a rule satisfying the off-pole quadrics cannot belong to this declared local allocation family.

A distinct remaining rival is correlated allocation of the two-quartic diagrams: allow an independent distribution among each graph's four refinements instead of demanding a product of two local splits. Testing that relaxation can locate whether independence of vertex allocations, rather than constancy alone, is responsible. It does not authorize interpreting any successful correlated assignment as a source-local triangle vertex.

Verification: checkers/check_face_local_quartic.py and results/face_local_quartic.json; the source checker is rerun as a prerequisite. All arithmetic is exact. No Git operations; the prohibition remains active.

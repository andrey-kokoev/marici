# Boundary tetrahedron: typing, filler, and information loss

## Question

Operator instruction: 'type the faces, test their filler, then test what the encoding forgets'. Does the supplied coefficient-marked boundary furnish a literal coherent tetrahedron, and is its primitive encoding sufficient for the unreduced coefficient markings?

## Claim boundary

This is a bounded audit of research/chatgpt/coefficient-marked-boundary/check_coefficient_marked_boundary.py, SHA256 ffc4660d2681fa8f13015eab8e9ee0c64243a9a2d787fe1a88d8a7592d0e2051. Only inspected matrix-construction helpers and Loaded were evaluated from its AST. The supplier main, upstream pipeline, published certificate, and pinned Git objects were not executed or authenticated. Standard-library targeted execution ran our checker, including the supplier local contraction audit; no Git operation or other-owner mutation occurred.

Bold conjecture: restriction-compatible primitive contractions furnish filled local tetrahedra, but their scalar-normalized encoding is not faithful on the unreduced conductor markings. Rivals: individually valid faces fail their joint filler; the primitive encoding preserves all normalized coefficient components. Risky consequences: the exact degree-minus-one filler obstruction vanishes for all 24 chart-overlap incidences, while distinct conductor markings can have identical encoded data.

## Typed faces

Work in the dg category of integral cochain complexes (the local complexes are bounded free complexes). For a chart A and incident overlap B, let P:A -> B be coordinate restriction, epsilon_A and epsilon_B empty-cell evaluation, i_B:Z -> B the normalized unit, and H_B the supplied degree-minus-one contraction satisfying delta H_B=1-i_B epsilon_B. Here delta is the mapping-complex differential.

Use four labelled vertices (A,B,B,Z). Vertices 1 and 2 have the same underlying complex; distinct underlying objects are not required for a simplex. Assign the six edges:

| Edge | Map |
|---|---|
| 01 | P |
| 02 | P |
| 03 | epsilon_A |
| 12 | i_B epsilon_B |
| 13 | epsilon_B |
| 23 | epsilon_B |

Use the convention delta H_ijk=f_jk f_ij-f_ik.

| Face | Degree-minus-one comparison | Boundary equation |
|---|---|---|
| 012 | -H_B P | delta H_012=i_B epsilon_B P-P |
| 013 | 0 | epsilon_B P-epsilon_A=0 |
| 023 | 0 | epsilon_B P-epsilon_A=0 |
| 123 | 0 | epsilon_B i_B epsilon_B-epsilon_B=0 |

Restriction compatibility P H_A=H_B P and P i_A=i_B is checked independently. The construction contains a genuine contraction comparison; it does not consist solely of four tautological zero faces.

## Filler

The tetrahedral boundary in Hom^-1(A,Z) is

R=H_013+H_123 f_01-H_023-f_23 H_012.

Its mapping-complex differential is zero by the face identities. Here R=epsilon_B H_B P=0, verified generatorwise. Thus the explicit degree-minus-two filler K=0 satisfies delta K=R. We assert existence, not uniqueness of fillers or absence of further coherence obligations.

The checker constructs all eight 1,075-generator charts and twelve 125-generator overlaps. All 24 incidences pass 25,800 generator-level face/filler checks. The supplied local differential and integral-contraction identities are also rerun on all 10,100 chart-plus-overlap generators. These are repeated local incidences, not a new count of independent physical degrees of freedom.

Strongest falsification controls:

- Reverse the sign of H_012. Its required face boundary fails on 3,000 chart generators across the incidence tests. The test does not silently absorb a sign change.
- Take V with one integral generator in each cohomological degree -1 and 0 and zero differential. Let all four vertices be V and all six edges be identity. Set H_012 to the map from degree 0 to degree -1 and all other faces to zero. Every face boundary holds, but R=-H_012 is nonzero and Hom^-2(V,V)=0. No filler exists. Four valid faces therefore do not in general imply a filled tetrahedron.

## What the encoding forgets

Define the candidate encoding explicitly: retain the fixed primitive chart/restriction/contraction tetrahedra above and the unit-monomial coefficient of the common conductor value of a global branch pair. This is an additive readout encoding, not a claim that the complete physical source supplies this reduction.

In the supplied conductor diagram the constant compatible global sections a=(1,1) and b=(1+z_plus,1) both have conductor value one, hence exactly the same encoded primitive data. Their difference (z_plus,0) is nonzero in the kernel conductor diagram K_L concentrated in degree zero. Its derived sections admit a nonnegative cochain model, so no degree-minus-one boundary identifies those degree-zero sections. They represent distinct pi0 markings. This proves that this specified encoding loses normalized branch information; it does not prove that every tetrahedral encoding loses it.

The example is a subfamily of the full polynomial model and suffices as a counterexample to faithful reconstruction. No finite support census is being promoted to an exhaustion theorem. Extra polynomial source modes can also be discarded by scalar coefficient extraction; the branch example alone already refutes the rival.

## Disposition

The local filled-tetrahedron conjecture survives the exact tests; faithfulness of the scalar primitive encoding is refuted by the explicit pair. A literal tetrahedron and a richer coefficient diagram coexist. Thus they are not mutually exclusive accounts, and tetrahedral fillability does not establish that a tetrahedron exhausts Marici's pyramid.

This is not yet an assignment of the four named global Marici obligations to four faces. Here the faces are specific contraction and normalization comparisons; the geometric source-realization obligation remains upstream. The first missing typed object for that stronger claim is a source-defined, transport- and readout-compatible comparison from the full physical relative coefficient system to this primitive model. Acceptance requires that comparison with its kernel/relative fibre and a justified account of which distinctions it may discard. No waiting issue is created and no global pyramid closure is claimed.

Verification: python research/nima/checkers/check_boundary_tetrahedron.py, exit 0 through structured-command; execution_ref structured_command_execution:e_10780_1788711784320845800_109. Results: research/nima/results/boundary_tetrahedron.json. All three audit files are newly written and uncommitted; Git remains prohibited. Graph admission, when reported separately, does not certify mathematics or a Git checkpoint.

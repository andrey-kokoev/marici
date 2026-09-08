# Rzk coefficient interface v2: source-admissible comparisons

## Question and scope

Operator instruction: strengthen the coefficient interface using the source-admissible-overlap audit. This version extends rzk-coefficient-interface-v1.md; its object, grading, relative-fibre, and probe distinctions remain in force. It supersedes acceptance of an underlying chain identity alone as a structured filler certificate. Fact_n and generic Segal/Rezk composition are unchanged. These are specification records, not compiled Rzk definitions.

Source: research/chatgpt/source-admissible-overlap/source_admissible_overlap.md. The source packet distinguishes an integer filler, a pair-local coefficient-compatible replacement, and a separately declared independent-normal polynomial lift. Do not identify the lift with the complete physical PC/Rees/Gysin system.

## Admissibility is part of the comparison type

AdmissibilityContext records the coefficient base and source/target module actions; allowed localization sets including mandatory Cut coordinates; support and spectator preservation; cohomological degree and multidegree; filtration action; required symmetry action (strict or coherently equivariant); exact source locators and assumptions. Strict and coherent equivariance are different contracts.

For objects A,B and comparison degree q, specify AdmissibleComparison(context,A,B,q) with an underlying map and witnesses for the declared requirements. An admissible filler is an element of this type satisfying its boundary equation, not an arbitrary solution in the underlying integer mapping complex with a later prose assertion of admissibility.

The constructor must prove that its boundary lies in the stated boundary type. If using an admissible dg subcomplex, prove closure under its differential and the relevant additive and composition operations. A pair-local ansatz need not be closed in this way: then state a typed boundary map for that ansatz and its target instead of falsely calling it a dg subcomplex. Higher comparisons use their own admissibility conditions and typed boundary maps.

FillerCertificate includes immutable boundary maps, context, underlying filler, admissibility witnesses, and exact boundary equation. HigherFillerCertificate includes both original fillers and its own admissibility witnesses. An integer-linear higher homotopy between two fillers does not establish their equivalence as coefficient-localization-compatible fillers.

For the formal independent-coordinate localization rings, an identity-on-monomials column R_L -> R_T is admitted when L is a subset of T. If a lies in L but not T, R_0-linearity and f(1)=1 would give v_a f(v_a^-1)=1 in R_T. Evaluating v_a at zero is defined in R_T and contradicts that equation. This criterion concerns these rings and coefficient-identity columns, not all module maps: the zero map is not excluded.

## Boundary revision is a separate constructor

BoundaryRevision records old and new maps, coefficient context, changed factors, source justification or declared-test status, and any comparison or specialization between the two problems. It never relabels a filler for the new maps as a filler for the old maps.

For the independent-normal test, old maps are rho_c; new maps are sigma_c=w_c rho_c. The polynomial weighted filler has the new discrepancy as boundary. The original discrepancy has a nonzero value on a cocycle and is not null-homotopic. The specialization w_a=1 recovers a unit-coefficient problem but is not authorized implicitly in a filtered physical problem.

## Normalization transport is independent

NormalizationTransport records the coefficient-change functor, old and new module sources/probes, degree and orientation conventions, readout comparison, and the image of the prescribed normalization value. A fixed normalized fibre may be transported only with this data. Otherwise record the new problem as unconstructed or empty under its declared condition.

In the unlocalized polynomial lift a unit empty-cell cocycle requires 1+w_c b_c=0. Evaluation w_c=0 proves that no polynomial b_c solves this. This refutes reuse of that normalization, not every possible supported, localized, or Gysin normalization. Do not manufacture a filler or normalize by dividing a nonunit.

## Exact regression fixtures

The accompanying standard-library checker implements two bounded fixtures plus normalization and revision controls:

1. Identity-on-coefficients localization: source inverses {04}, target inverses {03,05} must fail. A pair-local mixed input with source inverses {05,04} and target inverses {03,05,04} must pass. Tests compute inclusion rather than assuming it. The general impossibility proof is the evaluation argument above.
2. Independent two-normal block over Z[u,v]:

    d0 = [[1,u,0,0], [1,0,v,0], [0,-1,0,v], [0,0,1,-u]];
    z = (-uv,v,u,1);
    m_old = (0,1,-1,0).

   Check d0 z=0 and m_old z=v-u, a nonzero polynomial. For every proposed homotopy row h, h d0 z=0; therefore h d0=m_old is impossible. This is a cocycle obstruction, not failure of a search over finitely many h.

   The revised mismatch is m_new=(0,u,-v,0). The explicit row h_new=(0,0,-u,-v) satisfies h_new d0=m_new. This is a factor-retaining replacement with no denominators, not repair of the fixed old boundary. Specializing u=v=1 makes the two boundary problems coincide; the checker verifies that fact without treating the specialization as physical authority.

The checker represents polynomials by sparse integer coefficient dictionaries and checks exact identities, never random numerical samples. The two-normal block is a mathematical regression, not a rerun of all octagon generators. Full pair-local equivariance, support filtration, and higher-comparison admissibility remain source-packet claims pending independent formal realization; the checker does not certify every field of this interface.

## Disposition and verification boundary

Conjecture: explicit admissibility, revision, and normalization constructors block the false promotions exhibited by the source audit. Rivals: an underlying integer chain identity suffices; changing normal factors preserves the same boundary and normalization. The forbidden-localization and nonzero polynomial residual refute those rivals in the declared models. They do not prove universal completeness of the interface.

Checker: research/nima/checkers/check_rzk_coefficient_interface_v2.py. Results: research/nima/results/rzk_coefficient_interface_v2.json. Invocation: python research/nima/checkers/check_rzk_coefficient_interface_v2.py through structured-command. No Rzk core, other-owner checker, or proof-backend bridge is changed. Formal Rzk realization and the full physical source comparison remain unimplemented. Git operations remain prohibited.

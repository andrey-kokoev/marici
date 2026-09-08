# Rzk coefficient interface v1

## Question and scope

Operator instruction: implement the coefficient-interface distinctions and regression examples motivated by the boundary/interior and conductor-supported packets. This is a source-level interface extension to factn-rzk-interface-spec.md and simplicial-rzk-and-cubical-agda-amplitude-category-comparison.md, not a change to the checked Rzk core. The regression checker below checks exact mathematical fixtures in Python. No new Rzk definition or theorem is asserted to typecheck.

The combinatorial Fact_n remains the refinement poset of unmarked dissections. Its propositional hom-types do not imply propositional coefficient marking or comparison types. Loaded objects (F,M), coefficient localizations, and signed cellular complexes require their own typed index or comparison to Fact_n. Do not silently identify the 7100-object localization boundary with the 10100-generator cellular Cech totalization.

## Interface records (specification pseudocode, not Rzk syntax)

CoefficientContext:
- index: a specified directed category, with objects, arrows, relations, and source locators;
- target: the category of structured coefficients, including coefficient ring, variance, support, grading, and retained symmetry action;
- coefficients: a coherent diagram on index;
- interpretation: maps from the declared source presentation, with exact assumptions; absence is recorded, not filled by is-segal or is-rezk premises;
- allowed_equivalences: source-authorized structured equivalences, independently of any selected readout.

CoherentBoundaryComparison:
- I: interior coefficient object;
- V: chart section object;
- E: overlap section object;
- Delta: V -> E, with ordered restrictions and signs;
- B := fib(Delta), represented cohomologically by B^q=V^q plus E^(q-1), D(v,e)=(dv,Delta v-de);
- rho: I -> V, a degree-zero chain map;
- ell: I^q -> E^(q-1), satisfying d_E ell + ell d_I = Delta rho;
- Phi: I -> B, Phi(a)=(rho(a),ell(a));
- chain_map_witness: D Phi=Phi d_I;
- relative_object: F := fib(Phi), retained even when a marking fibre is contractible.

This two-column presentation applies to the stated boundary with no triple patch intersections. A cover with higher intersections needs its corresponding totalization and higher comparison cells. The existence of ell is not implicit in the existence of rho. Strict descent is the special case Delta rho=0, ell=0; it is not the general constructor.

MarkingProblem:
- context and coefficient object C;
- probe P, including its module action and cohomological shift;
- readout map r: Map(P,C) -> Y, with normalization target Y declared;
- fixed target value y:Y;
- normalized_markings := hofib_y(r);
- result: theorem about this particular space, not an unqualified 'unique' or 'contractible' flag.

ExtensionProblem:
- coherent comparison Phi:I -> B;
- probe P and fixed boundary marking b:Map(P,B);
- extensions := hofib_b(Map(P,Phi));
- stable_relative_object := fib(Phi), recorded separately;
- conclusions separately typed as existence, contractibility for this probe, relative cohomology, and structured equivalence of Phi.

SupportedComparison:
- ringed source and conductor immersion i, with A-module categories explicit;
- original Q, supported i^!Q, pushforward i_*, and counit eta:i_*i^!Q -> Q;
- comparison triangle including Cone(eta), not just the supported marking space;
- any grading shift and orientation compensation recorded separately;
- coefficient-localization naturality and required symmetry compatibility;
- physical identification: separate source-derived comparison or explicit missing datum.

The counit is not the ordinary evaluation Q -> R and is not a source-authorized equivalence merely because its supported normalized marking is contractible. Applying i^! changes the module source of a mapping problem as well as its target; it is not an automatic map from every integer-linear marking of Q to a supported marking.

## Equivalence and filler gates

For a dg model, delta h=d_target h-(-1)^degree(h) h d_source. A prescribed triangular comparison has delta H_ijk=f_jk f_ij-f_ik. A prescribed tetrahedral boundary has residual

R=H_013+H_123 f_01-H_023-f_23 H_012.

An admitted filler includes K of degree -2 and delta K=R. In an arbitrary target use the corresponding mapping-space boundary and filler, not these additive formulas without a dg interpretation.

A generic Segal composition theorem constructs coherent composites with its own boundary data. It does not establish fillability of every independently prescribed full tetrahedral boundary. Retain this distinction even when the refinement index is a poset.

A contractible normalized marking space does not imply that Phi is an equivalence. In a stable target, an equivalence test requires its full fibre to be zero; an equivariant target requires the equivariant statement. Testing one unshifted probe cannot establish that condition. Probe-wise promotion requires a declared jointly conservative family and its theorem, not a finite sample.

A constant scalar readout does not identify distinct branch-polynomial markings. Rezk completion does not authorize adding their comparison to the allowed equivalences. Readout descent remains an independent coherent comparison.

## Required regression fixtures

1. Non-strict descent: Delta rho is nonzero, ell supplies its exact boundary, and Phi is a chain map. Deliberately omit ell and require a nonzero chain-map defect. This prevents a strict-only interface.
2. Probe versus stable fibre: use the eight-vertex twelve-edge graph and I=Z[0] -> B=[Z^8 -> Z^12] given by the diagonal unit. Prove integrally H^2(fib(Phi))=Z^5 and all other cohomology zero. Unshifted relative mapping space is contractible, but pi0 Map(Z[-2],fib(Phi))=Z^5. The exact graph fixture certifies neither full loaded-source provenance nor physical readout.
3. Noninvertible counit: the constant-coefficient normalization sequence gives a counit whose cone contracts to Z^2, not zero. Record the cone instead of promoting the supported line to an equivalence. This fixture is not a computation of the entire polynomial A-module derived adjunction.
4. Branch collision: (1,1) and (1+x,1) are distinct conductor-normalized markings in the nonnegative coefficient diagram. Their common readout cannot certify their equivalence. No finite polynomial cutoff is used to claim global completeness; one explicit pair refutes injectivity.
5. Prescribed-boundary failure: V has one generator in each degree -1 and 0, d=0; all edges are id; only H_012 maps degree 0 to degree -1. All face equations hold, but the nonzero residual cannot be the boundary of a degree -2 map, since no such map exists. This prevents using generic associativity as a filler for an arbitrary supplied boundary.

## Disposition and verification

Governing conjecture: these separately typed records prevent the demonstrated false promotions without altering combinatorial Segal/Rezk composition. Rival: an unqualified contractibility/equivalence flag or strict-only descent interface suffices. Risky tests and deliberate failures are the five fixtures above; passing them validates the bounded examples and makes the interface requirements falsifiable, not a theorem of universal adequacy.

Checker: research/nima/checkers/check_rzk_coefficient_interface_v1.py. Results: research/nima/results/rzk_coefficient_interface_v1.json. Invocation: python research/nima/checkers/check_rzk_coefficient_interface_v1.py through structured-command. Standard library only. Formal Rzk realization remains unimplemented; no cross-backend bridge is introduced.

Source packets: research/chatgpt/boundary-interior/boundary_interior_extension.md; research/chatgpt/conductor-support-comparision/conductor_supported_comparison.md; research/chatgpt/coefficient-marked-boundary/coefficient_marked_boundary.md; research/nima/boundary-tetrahedron-audit.md. The new fixtures do not rerun the full source checkers or authenticate their pinned Git sources. Other-owner files and Rzk modules remain unchanged; Git operations remain prohibited.

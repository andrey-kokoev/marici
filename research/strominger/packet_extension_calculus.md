# Retained-packet extension calculus: common-record coherence and the first three-way defect

Date: 2026-10-28.

## Evidence boundary

The source input is the supplied `su32-native-window-operation-v1.md`, included unchanged in this bundle. It supplies exact lifted ports, an integer period lattice, and an invertible regrouping of 420 wire values when all external slots are retained. It explicitly says that this operation introduces no comparison-packet constructor. Its own Node verification is reported in the source; it has not been rerun here.

Earlier conversation constructions supply examples, not additional native axioms. In particular, neither a four-bit cube, a free groupoid, a circle action, nor a Hopf fibration is inserted into the calculus below.

This note supplies a proposed interface for actual local rules, a general theorem for one precisely specified class of those rules, two finite countermodels, and a new calculation using the source period formula. Native release/swap records evaluated: **zero**. No Agda or Lean run was performed.

## 1. The smallest useful interface

Keep the adopted indexing: a 4-packet is a point, a 3-packet a line, a 2-packet a square, and a 1-packet a cube. This is not ordinary simplicial dimension indexing. The interface does not assume that these names already certify the required incidence geometry.

A point occurrence p retains its source identity and interface. For a native lifted port, the identity includes the complete port/face/axis label and the integer lift a, not just a cell name or a projected coordinate.

For a requested extension direction i, write E_i(p) for the family of source-admitted witnessed extensions. Each element u retains:

- its actual source derivation and exact input boundary;
- its target occurrence p_i(u), with complete output boundary;
- the native action or observation map, when supplied;
- an inverse witness only when the source supplies one.

The symbol i is a requested direction, not permission to flip an independent Boolean coordinate. E_i(p) may be empty, singleton, or larger. An appended step retains the preceding history. Reading a path backward is not automatically permission to execute a reverse native step.

These requirements distinguish a *move between point occurrences* from a *release operation that constructs a family or higher cell*. The uploaded source defines its wire move and regrouping, but does not yet define every proposed polarity release. We therefore do not infer a new native extension by changing a sign in notation.

Raw histories are stored as syntax. Composition concatenates their actual admitted steps. Rebracketing concatenation can be accounted for without identifying different words. A history that returns to an old endpoint is still a nonempty history.

## 2. Two extensions: the comparison request

The two ordered families are dependent:

    H_ij(p) = sum over u in E_i(p) of E_j(p_i(u)),
    H_ji(p) = sum over v in E_j(p) of E_i(p_j(v)).

There is no assumption that these families have equal size or even that both are inhabited. The source must first admit the corresponding four-edge boundary and give compatible full endpoints. Equal deck displacement is only part of that endpoint test.

In the reversible exchange fragment considered here, a square is supported by an admitted comparison chi_ij between the appropriate compatible route families, over that full boundary, with an actual inverse comparison. This comparison preserves the retained witness information; it is not equality of the two raw construction histories. A particular source may supply comparisons only for some boundaries rather than one total equivalence H_ij ~= H_ji.

An inverse comparison is used in the reverse direction. We do not deduce that an arbitrary forward native operation squares to the identity.

This is a test interface, not an axiom requiring every square to exist. If either route is inadmissible, or if no comparison is generated, the extension fails at this stage.

## 3. A constructive positive theorem

Here is a sufficient local mechanism that needs no independently chosen higher reordering fillers at the level of sets and maps.

Fix a family of admitted operations and a joint record set M. For each admitted ordering sigma, let H_sigma be the set of complete records in that ordering. Suppose that there is a bijective decoder

    d_sigma : H_sigma -> M

which retains every relevant witness field, and that each admitted local exchange is exactly

    chi_(sigma,tau) = inverse(d_tau) after d_sigma.

Then

    chi_(tau,rho) after chi_(sigma,tau) = chi_(sigma,rho).

Proof: cancel d_tau after inverse(d_tau). Repeated cancellation proves the same statement for every finite comparison route. Any two admitted comparison routes with the same source and target act by the same bijection. Every comparison loop acts as identity on M.

Nothing is inferred about orderings or edges the source does not admit. Nor does the proof generate new geometric cells.

This theorem is stronger than checking endpoint values only: the decoders must be lossless on the witness data whose coherence is claimed. It is a strict set-level theorem. For higher types, replace bare inverse equations by the appropriate coherent equivalence data rather than treating that upgrade as automatic.

### Relation to the uploaded native operation

The source already supplies this mechanism for *complete wire-value presentations*: identify each slot with its exact wire, reconstruct the assignment, and present it elsewhere. The semantic record is the assignment on the same 420 wire identities. This recovers the previous all-length regrouping theorem.

The upload does not establish such a decoder for every proposed packet-release history or its higher comparison witnesses. It explicitly disclaims introduction of a comparison-packet constructor. Applying the stronger witness-level theorem to those objects is an additional source obligation.

The checker implements an independent-record example. Every witness tag survives the exchanges. It retains the comparison route as a separate receipt, so two routes can induce the same map while remaining different histories.

## 4. First overlapping coherence test: three extensions

Assume a chosen triple A,B,C is admitted in the six relevant orders, and that its six adjacent-order comparisons have been supplied with inverses. These assumptions must be checked before this test applies.

There are two three-comparison routes from ABC to CBA:

    ABC -> BAC -> BCA -> CBA,
    ABC -> ACB -> CAB -> CBA.

Call their composite witness maps L and R. Their discrepancy is

    Omega = inverse(R) after L : H_ABC -> H_ABC.

It fixes the complete external boundary when every local comparison does.

For equality of set-valued comparison maps, the required equation is Omega=id. For a higher-categorical source, the next request is an admitted higher comparison L => R, equivalently an appropriate homotopy of Omega to the identity. A nonidentity function is not automatically a topological obstruction when additional homotopies are allowed. The discrete countermodel below deliberately has none.

The six orderings form a hexagon. Its edges record exchanges of extension order. This is not the same object as the physical contact triangle, a 2-packet square, or the pentagon of parenthesizations in a Segal test. In the standard cube-of-independent-steps picture, the six exchanges correspond to its six square faces; their compatibility is the first three-direction coherence test.

### Complete discrete countermodel

Give each H_sigma an extra retained bit h. Keep all visible endpoints and wire values fixed. Each undirected hexagon edge carries a bit epsilon_e; crossing it acts by

    h |-> h XOR epsilon_e.

Every local comparison is invertible, and its reverse recovers the entire bit. The two routes disagree by

    Omega(h) = h XOR (sum of the six epsilon_e modulo 2).

Choose epsilon=1 only on ABC <-> BAC and zero on the other five edges. Then

    L(h) = h XOR 1,
    R(h) = h.

All two-order comparisons exist and are reversible. Their three-order compatibility fails on retained data.

There are 64 assignments to the six edge bits. Exactly 32 have zero discrepancy and 32 have nonzero discrepancy. The program exhausts all of them.

This is a constructed diagnostic model, not a measured defect in Su-32.

### The defect cannot be removed by a coordinate rename

Changing the bit coordinate at order sigma by h'=h XOR k_sigma changes an edge label to

    epsilon'_sigma,tau = epsilon_sigma,tau XOR k_sigma XOR k_tau.

Around the hexagon, every k appears twice, so the sum and the defect are unchanged. Conversely, zero parity allows coordinates to be propagated from one selected order consistently around the cycle. Thus this binary example has precisely two coordinate-invariant defect classes.

The checker tests all 4096 edge-assignment/vertex-relabel combinations. This is a complete finite classification of this example, not a proof that all possible source witnesses are binary.

## 5. Coherence and cubical independence are separate

Even complete comparison coherence does not prove that a generated cube has eight different point occurrences in a chosen observation.

As an explicit control, use the three translations of F_2^2 by

    A=(1,0), B=(0,1), C=(1,1).

They commute and are involutions. Every pair has four distinct subset endpoints and hence an ordinary square orbit. All three together still have only four endpoints, because A+B+C=0.

Retaining the eight subset histories preserves eight *formal occurrences*. Projecting them to the four states folds them together. A cubical set is allowed repeated vertices, so this example does not prohibit a cubical object. It refutes the inference from pairwise square geometry to an embedded, eight-vertex cube.

Thus three questions are distinct: existence of the required extension histories; compatibility of their comparison witnesses; faithfulness of the chosen geometric realization.

## 6. A source-specific fourth-order dependence

The upload supplies the period generators

    g_i = (1,1,1,1) - 4 e_i,     i=0,1,2,3.

This determines an exact integer map G:Z^4 -> Z^4:

    G(c) = sum_i c_i g_i
         = (sum_i c_i) (1,1,1,1) - 4(c_0,c_1,c_2,c_3).

Therefore G(c)=0 exactly when all four c_i are equal:

    ker G = Z(1,1,1,1).

Every proper subset of the four generators is linearly independent, while

    g_0+g_1+g_2+g_3=0.

This proves, without extrapolation from finite samples, that the auxiliary subset map

    b in {0,1}^4 |-> sum_i b_i g_i

has exactly 15 distinct endpoints. Its only collision is between 0000 and 1111. Indeed, two binary vectors with the same image differ by an integral multiple of (1,1,1,1), which can only be 0 or the two opposite-corner differences.

Every proper coordinate face is vertex-injective. The checker verifies all 32 one-dimensional faces, 24 square faces and 8 three-dimensional faces, followed by the unique global corner collision. Thus even passing every proper-face independence test does not force four independent global directions.

This is a calculation about the period formula, not a new native release sequence. The g_i have NOT been identified with the four polarity flips, and no native port sequence realizing all four periods has been supplied. The 15 endpoints are not the source's 16 residue types, its 16 P cells, or its complete cell inventory.

If such a four-step word is later admitted, its return to the same coordinate does not erase its retained history or prove that the corresponding loop has a filler. That distinction is exactly what the calculus preserves.

## 7. Consequence for C1

The positive theorem isolates one genuine mechanism: lossless common-record reconstruction makes every finite reordering comparison coherent at the stated data level. The source already implements its wire-value instance.

The triple defect isolates the first overlapping witness-level obstruction after pairwise exchanges have been admitted and inverse laws supplied. An implementation can now distinguish a missing route, a missing pairwise comparison, a nontrivial Omega, a higher witness relating L and R, and geometric folding. These should not be reported as the same failure.

This is not a proof of 2-Segality or coskeletality for Su-32. Those statements require an actual simplicial object and its specified face/degeneracy maps. In particular, our six-order hexagon is not a substitute for the relevant simplicial reconstruction maps.

The ordinary nerve of a category is a 2-coskeletal baseline, but using its formal composition does not identify arbitrary native parallel histories. Higher-dimensional rewriting gives a method for generating global comparison data from appropriate local confluence and wellfoundedness hypotheses. It does not license filling every loop, and reversibility alone does not supply termination. An orientation used to normalize presentation order must not be mistaken for the physical or native direction of evolution.

## Reproduction

Run with Python 3.10 or later:

    python check_packet_calculus.py --output results.json

The program uses only the standard library. `results.json` separates the canonical common-record model, the binary comparison countermodel, the cubical-independence control, and the source-period calculation. It explicitly records zero native release/port records evaluated.

Source snapshot and SHA-256 manifests are included. No repository files were modified.

## References and provenance

1. User-supplied `su32-native-window-operation-v1.md`: Global source operation; Restrict the global family to the actual window; Two state domains; Remaining construction. This is the basis for all native facts in this note.
2. Previous conversation artifact `su32_lifted_square_continuation.md`: complete wire regrouping and exact lifted endpoint tests. The present note reuses, rather than claims to newly discover, the value-map cancellation theorem.
3. Previous conversation artifact `su32_three_contact_results.md`: history-aware completion, distinction between a source port map and a lattice symmetry, and the declared nature of its free-groupoid example.
4. Jacob Lurie, Kerodon, Coskeletal Simplicial Sets, Definition 3.5.3.1 and Examples 3.5.3.4-5, https://kerodon.net/tag/051Z (consulted 2026-10-28). Ordinary and bicategorical nerves have different coskeletality bounds; neither supplies a native comparison constructor by itself.
5. Nicolai Kraus and Jakob von Raumer, A Rewriting Coherence Theorem with Applications in Homotopy Type Theory, arXiv:2107.01594, https://arxiv.org/abs/2107.01594 (consulted 2026-10-28). Sections 1.1 and 1.2 distinguish normal forms, coherence among reduction paths, and proof-relevant higher paths.

The explicit three-way bit classification, coordinate-invariance calculation, independence control, and binary-subset period calculation are calculations in this note. The citations do not assert that these countermodels occur natively in Su-32.

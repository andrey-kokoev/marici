# Deeper prior-research search: binding the analytical filler to F736

## Target and method

Target: identify the prior analytical witnesses with E514/E539/E515 and the two local H134 presentations of F736, preserving full represented observers, finite-cutoff residuals, endpoints and ordered placements.

Read the prior analytical ledger, its incidence builder and existing census, the exact regulator-transport construction, eight-leg construction, and the Hardy-placement correction chain. This is a source search and extraction, not a new proof or a rerun of analytical/census checkers. Prior status claims below remain subject to their stated hypotheses.

## 1. Concrete incidence data already exist

Source: `research/voevodsky/results/esd7_explicit_analytical_census.json`; inspected alongside `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`.

| vertex | cumulative coordinates | barycentric coordinates |
|---|---|---|
| V104 | (4,5,5) | (4,1,0,2) |
| V111 | (5,5,6) | (5,0,1,1) |
| V113 | (5,6,6) | (5,1,0,1) |

In geometric orientation:

- E514: V104 -> V111, increment mask `13`;
- E539: V111 -> V113, increment mask `2`;
- E515: V104 -> V113, increment mask `123`.

F736 therefore compares the ordered blocks `13 | 2` with direct `123`.
These mask digits index cumulative coordinate increments, NOT source chart labels and NOT the seven semantic operations A,J,P,C,T,E,F.

The two incident tetrahedra expose the cross-occurrence comparison:

- T324: V104 -> V105 -> V111 -> V113, increment order `3,1,2`;
- T325: V104 -> V110 -> V111 -> V113, increment order `1,3,2`.

Their shared E514 is block `13`, internally factored as `3 then1` or `1 then3`. A witness-preserving binding must identify these factorizations, and then carry that comparison through increment2 and the direct block123. Thus a concrete next comparison is already isolated; merely matching the two local H134 labels omits it.

Caution: the census builder supplies the mask and generic analytical-form descriptions. It does not itself define numerical/closed operator formulas for these masks. A nonempty `form` field is not an analytical existence proof.

## 2. The analytical ledger has much more than a parent remainder

Source: `research/voevodsky/eight-node-lattice-analytical-form-coverage-ledger.md`, especially its late sections on residual-augmented strictification and geometric registries.

It supplies the target coordinates

    (relative bulk, Hermitian ordered placement, skew placement commutator,
     finite-part trace, endpoint residue, localized boundary class).

Its triangle prototypes are AP,AE,JP,JC,JE,PC,CE,TE. PC retains the noncommuting placement channel; TE retains the endpoint residue correction. The claimed higher strictification is in these enlarged coordinates, NOT a claim that the original operators commute.

The ledger also gives twelve triple prototypes, including JPC (Fourier transport of both placement channels) and JCE (transported cutoff and endpoint packet). Its named geometric face constructors explicitly characterize H134 as regulator transport retaining Hermitian/skew placement coordinates, and H234 as rapid-decay comparison retaining finite-part/residue data.

This substantially sharpens the target: extract a semantic realization/refinement of the actual increment blocks13 and2, and use the corresponding retained-coordinate interchange. Do not assume that the geometric index13 means semantic JP or any other pair; no such identification was found in the inspected records.

The ledger contains multiple historical frontiers and later closures at different strengths. Early statements that coverage is open must not be quoted as its final disposition. Conversely, its completed coverage statements must not be promoted to explicit native F736 operator bindings without inspecting the constructors.

## 3. Actual finite-regulator transport formulas are available

Source: `research/voevodsky/exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md`.

On a declared angular fiber, with L=log Lambda, the exact physical-to-Hardy unitary U_chi gives

    U_chi P_Lambda U_chi* = Pi,
    U_chi Q_Lambda^T U_chi* = Q_L^T,
    Q_L^T = M_(exp(2iLs) gamma_chi) Pi M_(exp(2iLs) gamma_chi)*,
    Q_L^0 = M_(exp(2iLs)) Pi M_(exp(2iLs))*.

The physical reference is defined by inverse transport, not freely replaced by an inversion model. The outer regulator is exactly

    Z_tilde = U_chi Z_physical U_chi*.

Observer convolution becomes its full Mellin multiplier. Exact finite ordered trace transport retains Z_tilde, Pi and the observer in their inherited positions. There is no license to commute the observer past Pi or replace Z_tilde by a convenient Mellin interval.

This supplies a candidate analytical ingredient for the local H134 regulator-transport prototype. It is not yet a declaration that E514 is U_chi or that the F736 native inversion reference equals this transported reference.

## 4. The finite placement witness retains an explicit sewing defect

Source: `research/voevodsky/an-eight-leg-cross-polarized-positive-dilation-realizes-the-exact-left-cutoff-relative-product-placement.md`.

For DeltaQ=Q^T-Q^0 and a cutoff projection P:

    P DeltaQ - P DeltaQ P = P DeltaQ (I-P).

The four-leg feature and symmetry are

    Psi x = (Q^T x,(I-Q^T)x,Q^0 x,(I-Q^0)x)/sqrt(2),
    J4 = diag(I,-I,-I,I),
    Psi* J4 Psi = DeltaQ.

The doubled eight-leg feature represents the cross-polarized placement, with Hermitian readout

    (P DeltaQ + DeltaQ P)/2,

and a separately retained skew readout

    (P DeltaQ - DeltaQ P)/(2i).

These are concrete finite-regulator coordinates for the witness; setting the latter to zero or dropping P DeltaQ(I-P) would lose the intended analytical data. For regulated observer operators use the exact left/right legs inherited from trace cyclicity, not an unproved symmetric placement.

## 5. The Hardy-placement proof has a correction chain

Read together:

1. `research/voevodsky/correction-the-relative-projection-trace-formula-does-not-directly-evaluate-the-left-hardy-compressed-product.md`;
2. `research/voevodsky/translation-covariance-makes-the-left-hardy-placement-converge-to-the-full-relative-projection-trace.md`;
3. `research/voevodsky/correction-translation-strong-convergence-leaves-an-observer-hardy-commutator-remainder.md`.

The uncompressed projection-pair trace is not automatically the trace of Pi DeltaQ. Even trace-class membership does not identify these two values.

After conjugating out the common cutoff translation, let Pi_L=U_L* Pi U_L and T_(g,h)=M_h* DeltaQ_0 M_g. The corrected formula is

    Tr(M_h* Pi_L DeltaQ_0 M_g)
      = Tr(Pi_L T_(g,h)) + C_L(g,h),
    C_L(g,h)=Tr([M_h*,Pi_L] DeltaQ_0 M_g).

Sufficient hypotheses are:

- T_(g,h) is trace class;
- [M_h,Pi] and DeltaQ_0 M_g are Hilbert--Schmidt;
- DeltaQ_0 is fixed after cutoff translation;
- all kernels are measured in the same Hardy coordinates.

Then the exterior term converges by strong convergence against a trace-class operator. The commutator term tends to zero by Riemann--Lebesgue applied to its L1 kernel product with modulation exp(-2iL(s-t)). Its Hilbert--Schmidt norm is constant, not decaying. The finite estimate is

    |C_L(g,h)| <= ||[M_h*,Pi_L]||_2 ||DeltaQ_0 M_g||_2.

This is an iterated-regulator result under the specified localization hypotheses. It does not provide a rapid-decay rate from Riemann--Lebesgue alone, nor automatically prove a simultaneous-regulator limit. Endpoint/index pieces and angular summability have their own declared treatment.

## 6. Graph-chart transport helps typing but is not the whole witness

Source: `research/voevodsky/a-common-graph-presentation-generates-all-opposite-edges-at-fixed-realization-dimension.md`.

Retaining a common source anchor produces fine maps

    (x,q^[r](x)) -> (x,q^[r+1](x))

and exact opposites on the anchored graph. This can organize the common analytical domain and shared-edge identifications. It does not supply missing q^[r] coordinates or identify transported graph topology with an independently prescribed physical topology. Its strict triangle cannot substitute for the retained regulator-placement residual.

For the pasting law use `research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md`: schematic edge equality and equality of chosen homotopies are distinct obligations.

## Search disposition

The prior research supplies more concrete ingredients than the six initial imports alone:

- actual shared increment-block data for F736;
- residual-augmented analytical prototypes;
- exact finite physical/Hardy regulator transport;
- explicit eight-leg sewing and placement coordinates;
- a repaired trace-limit proof with an explicit observer--Hardy commutator remainder.

The remaining extraction is now precise: give the source-typed stage objects/maps for increments1,3,2 in T324/T325; identify the two `13` composites with the same E514; paste their retained regulator/endpoint comparison through E539 to E515; and compare that pasted witness with the correlated seven-occurrence realization. Keep the occurrence5 parent H234 distinct from both local H134 roles.

No direct F736-specific analytical operator formula beyond the Strominger construction was found in the searched prior Markdown files. The existing incidence generator's generic labels do not by themselves close that extraction. This search does not establish that no such formula exists elsewhere.

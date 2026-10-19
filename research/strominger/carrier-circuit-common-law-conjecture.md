# DPC: one carrier law, distinct particle-window compositions

## Question, claim boundary, disposition

Can P/N/E be explained as different compositions of the SAME carrier operations,
rather than three independently adjustable circuit-element laws?

**Native conjecture: OPEN.** The full source context transports and primitive
operator constructor are missing. The checker below tests a conditional algebraic
criterion and deliberate false positives, not a native particle realization.
**Control status:** 42 checks pass. All 4096 declared binary-matrix triples
agree with the independent linear-system consistency test: 127 compatible,
3969 incompatible. This verifies the conditional gate and its discriminating
controls, not the native conjecture.

Operator request: "let's stare at this hard and develop a Deutsch-Popperian
Conjecture". This follows the original sensed particle-circuit direction; no new
confidence modality is inferred. The earlier shared-boundary construction gave
compatibility rules but did not derive a common operating law. Prospective
stimulus/conjecture/test proposal:
`ep_d2ffda78-433f-4be0-8490-88783ebaa611`, recorded 2026-10-15T21:05:21Z.

## Bold conjecture

Within one independently typed carrier/context class, particle names introduce
NO additional primitive operating laws. Every C-to-M occurrence uses one
source-constructed A; every M-to-C occurrence uses one source-constructed B.
The C continuation T and all context transports are fixed from source, not
chosen to make particle responses match. Interactions use the admitted shared-
carrier composition law, not a freely fitted particle-specific joint box.

This is a conjecture about reuse of operating laws, not the assertion that C and
M labels alone determine matrices. It must predict held-out occurrences after
the primitive constructor and context transports are frozen.

## Typed realization and a risky prediction

The supplied words are P=C0->M0->C1, N=M0->C1->M1, E=M1->C1->C2.
C0/C1/C2 and M0/M1 are NOT silently identified. The hypothesis requires
independently source-authorized context transports into common role carriers
C and M. Equal dimensions, spectra or particle nicknames do not construct them.

In such a chart, on the faithful-continuation stratum, let

    A:C->M,  B:M->C,  T:C->C_out (invertible).
    P=BA,    N=AB,    E=TB.

Matrix products mean composition, not physical time. No adjoint or inverse
relation between A and B is assumed. These are proposed WINDOW operators, not
an identification with the existing native 1836/144 coefficient returns.

Define P_out=TPT^-1. The hypothesis forces

    BN=PB,    NA=AP,    EN=P_out E.

The last identity is an independently testable cross-window condition when
P,N,E and T are supplied with their complete source-typed interfaces. Also
`det(I-zP)=det(I-zN)` by the rectangular determinant identity: the nonzero
spectral data agree. That spectral consequence is weaker than the full law.

## Complete finite-dimensional compatibility gate

Fix T BEFORE comparing P,N,E and set B=T^-1 E. Over finite-dimensional Q vector
spaces there exists an A with BA=P and AB=N exactly when:

1. im(P) is contained in im(B);
2. ker(B) is contained in ker(N);
3. PB=BN.

Necessity follows from the two factorizations. For sufficiency split
M=M1 direct-sum ker(B), C=im(B) direct-sum C0 and put B in the block form
`[[I,0],[0,0]]`. The first two conditions force

    P=[[P11,P12],[0,0]],   N=[[N11,0],[N21,0]].

The third gives P11=N11. Then A has blocks
`[[P11,P12],[N21,Z]]`, with Z free. This proof is conditional linear algebra,
not a source constructor. It is stratified by (dimC,dimM,rankB).

The invisible freedom is Hom(C/im(B),ker(B)), of dimension
`(dimC-rankB)*(dimM-rankB)`. Therefore even exact agreement of all three window
operators need not determine a unique primitive A. Do not quotient that
freedom as gauge without a separate source witness; it can affect another probe.

## Issue-boundary Deutsch-Popperian conjecture

1. **Problem.** Calling the windows capacitor/inductor/transistor or attaching a
   freely chosen coupling box can redescribe almost any circuit. It does not
   explain why different windows must obey one another's constraints.
2. **Bold conjecture.** One source-fixed, instance-independent primitive law
   generates the window operators and their admitted gluings. A particle name
   cannot authorize an extra matrix, frame correction or interaction parameter.
3. **Named rivals.** Independent particle laws; accidental spectrum agreement;
   context-specific primitives disguised by fitted transports; intertwiner-only
   matching with hidden kernel/image defects; common-law compatibility mistaken
   for construction or uniqueness of the source law.
4. **Risky consequences.** Freeze primitives and source context maps, then predict
   the repeated C->M and M->C occurrences in the other windows. Require all three
   compatibility gates and the transported electron intertwiner. Require complete
   frame covariance; changing T alone after inspecting a failed triple is not a
   coordinate change. Rank-deficient cases must retain their invisible primitive
   freedom rather than claim unique recovery.
5. **Strongest falsification.** With fixed T=I, take P=N=diag(1,0), E the binary
   swap matrix. Spectra agree but EN-PE=[[0,-1],[1,0]], of rank two. Separately,
   P=N=I and E=diag(1,0) pass the intertwiner while failing BOTH image and kernel
   conditions. The checker independently compares the three gates with solvability
   of A->(BA,AB) on all 4096 zero/one 2x2 B,P,N triples. A nonzero discrepancy
   falsifies the algebraic criterion, not the native physical conjecture.
6. **Disposition.** The conditional controls pass in
   `structured_command_execution:e_28364_1792098357452082300_219`; native conjecture
   remains OPEN. The spectrum spoof has rank-two intertwiner obstruction; the
   intertwiner-only spoof has image and kernel obstructions of one each. The
   nonzero primitive ambiguity survives all three window observations. A native
   failed held-out occurrence, with source frames fixed, refutes this common-law
   realization. Do not repair it by fitting a particle-specific A, B or T. Legitimate
   source-enlargement revisions must be declared separately with new predictions.

## Why the explanation is hard to vary

A shared law couples the predictions: changing A or B changes more than one
window. In particular E is constrained to intertwine N with the transported P.
It cannot be chosen independently while leaving all other data fixed.

The spectrum-spoof fixture can be made to pass by changing ONLY T from I to
swap. The checker retains that tempting repair as a forbidden source change.
Transporting the entire packet consistently under an actual frame change leaves
the obstruction nonzero. Thus fixing context transports independently is an
essential falsifiability condition, not administrative bookkeeping.

A passing factorization solver establishes compatibility only. Explanation
requires a source-derived primitive constructor and successful held-out tests;
there is no arrow from a fitted A to an independently established carrier law.

## Frozen test envelope and reopening boundary

Fixture: `inputs/carrier-circuit-common-law-v1.json`.
Checker: `checkers/check_carrier_circuit_common_law.py` (exact standard library).
Model: `scc-models/carrier-circuit-common-law-v1.json`.
Receipt: `results/carrier-circuit-common-law/verification.json`.
The positive and hostile SCC diagrams retain complete evaluated composites;
compiler tokens hash those computed matrices, not unproved word equalities.

    python research/aspect/scc/scc.py check carrier-circuit-common-law-v1 --verbose

Pre-test coordinates: one common-law conjecture; three named algebraic false-
positive mechanisms plus primitive ambiguity; 4096 declared matrix controls;
no native source admission. No numerical excitement/confidence score is inferred.
Post-test coordinates, recorded before user-facing synthesis: 42/42 controls;
4096/4096 criterion/linear-system agreements; 127 compatible and 3969 incompatible
binary triples; rank-B strata contain 256/2304/1536 cases at ranks 0/1/2. The
conditional SCC cell passes, the spectral-spoof cell fails, and the native claim's
SCC inverse report still lists missing source witnesses. A one-dimensional
primitive ambiguity is explicitly retained in the rank-one example. No native
admission or source-law selection was gained by the census.

The obligation is conditional forward realization and static intertwiner
compatibility, not native attachment equivalence or readout descent.

First missing typed object for the native branch: independently source-authorized
context transports for C0/C1/C2 and M0/M1. Acceptance requires their full interfaces
and composition coherence to be fixed without fitting P/N/E. Then freeze the
primitive constructor before held-out occurrence checks. This branch is deferred,
not represented by an open wait-for-data leaf. No chemical, energy, stability or
physical-time claim is tested here.

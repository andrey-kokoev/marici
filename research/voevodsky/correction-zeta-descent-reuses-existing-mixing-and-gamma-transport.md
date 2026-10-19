# Correction: reuse the existing mixing descent and analytic gamma transport

## What was overstated

The closeout for `zeta-five-arrow-descent-v1.md` said that a nontrivial descent
needs coordinate-mixing arrows and left that possibility open. This is too
broad if read as saying no such descent has been constructed. The checker
only classified diagonal operators under one fixed projection; it did not
search or refute the existing non-diagonal constructions.

## Prior constructions found by the requested search

1. `research/strominger/source-arrow-hamiltonian-top-down-descent.md` already
   constructs D12=C12-C12^T independently of D4 from the actual source cycle.
   It proves P D12=D4 P, retains nonzero hidden dynamics, and supplies the
   reducing-mode schedule 12->11->10->9->8->6->4. This is an existing
   non-diagonal descent through precisely the projection used by our test.
   It was read during that test; its constructive consequence was not carried
   into the final recommendation.
2. `research/nima/triangle-coherent-generator-transport.md` repairs an earlier
   stage mismatch by E_(n+1)=F_n E_n C^-1 rather than independent section
   minimization. Its full generator, hidden state and conditional metric
   commute with native extension. This is a distinct retained-history bridge,
   not automatically the same finite projection.
3. `research/voevodsky/mellin-diagonalization-of-the-oriented-radial-fourier-kernel-recovers-the-tate-gamma-matrix.md`
   already derives an actual mixing gamma matrix from the radial Fourier
   kernel: M_log W_or=G(t) R_t M_log. It does not merely insert scalar gamma
   multipliers as edge labels.
4. `research/voevodsky/the-oriented-hurwitz-polylogarithm-pair-closes-the-source-comb-fourier-intertwiner.md`
   applies that operator to the shifted comb and constructs the ordered
   Hurwitz/polylogarithm four-port Fourier orbit, retaining the zero atom
   separately. Its named boundary is external G4 topology/Gram acceptance,
   not an unknown analytic kernel or missing phase.
5. `research/voevodsky/retained-four-port-attachment-provenance-is-complete-across-its-required-rungs.md`
   closes local attachment provenance on the retained graph, ideal and Mellin
   domains. It explicitly warns against reopening the generic internal
   transpose-range problem; global determinant sewing and external G4
   identification are different questions.

## Corrected next task

Do not reconstruct a generic mixing operator or repeat scalar-versus-diagonal
controls. Compare the EXISTING analytic Fourier/Mellin representation with the
EXISTING source-cycle/four-mode or retained-T9 representation at their declared
types. A Fourier quarter-turn, a skew-part angular flow, and a scalar
multiplication edge are different operators and cannot be identified merely
because their pictures have four vertices.

The bounded search found existing nontrivial descent and an existing analytic
gamma intertwiner. It did not locate a completed common-domain attachment
carrying all five particular zeta-completion arrows into Strominger's native
rung map. This is a search result, not a repository-wide nonexistence theorem.
The new diagonal checker remains valid for its narrow class; it is not evidence
that the broader constructive problem is untouched.

This correction is based on fresh source reads, not new execution of the
cited suites. Their stated verification counts remain historical receipts.

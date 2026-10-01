# Iteration 3: shared matrix-leg preparations are not exchange-closed

## Fresh source and candidate tested

The oscillator instrument leaves a state-identification gate. Freshly reread
`check_shared_leg_dg_realization.py`: the native comparison assembly has shared
2-by2 matrix legs X_i and Y_j, with composite C_ij=Y_j X_i and a separately
retained direct reference d. There are11-by11 arrow composites and4-by4 state
composites, not137 independently editable primitive matrices.

Test the explicit scalar record candidate

    w_ij = tr(Y_j X_i),

and its fixed-reference version w_ij=tr(Y_j X_i-d). Trace is a declared linear
readout here, not a physically selected measurement. Other nonlinear, matrix-
valued or witness-enriched adapters are not excluded by this test.

## Exact closure obstruction

For arbitrary2-by2 legs, tr(Y_j X_i) is a bilinear pairing of four matrix entries.
Consequently its11-by11 arrow block W has rank at most4. This constraint applies
to every possible reassignment of the same shared2-by2 legs, not just the initial
fixture. With a fixed reference, add tr(d) back to each entry before this test.

Choose four invertible real matrices

    I, diag(1,-1), [[0,1],[1,0]], [[0,1],[-1,0]].

Cycle through these as X_i; use their transposes divided by2 as Y_j. Every leg
is invertible, and W_ij is1 iff i and j agree modulo4, otherwise0. W has rank4.
Every row and column class occurs at least twice among the11 indices. Thus each
coordinate vector e_i lies outside the column space of W, and each e_j outside
its row space. A nonzero single-cell update

    W_next = W+t e_i e_j^T

has rank5. This follows by putting the rank4 block into row/column normal form:
the rank-one addition has nonzero components outside both existing spaces.
It is checked exactly for all121 cells at t=1/7, as well as for the actual pulse.

With zero initial carrier, exchanging port(0,0) replaces its record with zero.
For raw trace records the reconstructed product block now has rank5. For the
existing independent reference d=2I, the same exchange also gives rank5 after
adding tr(d)=4 back. No reassignment of the shared2-by2 legs can produce it.

This is not merely a poorly chosen zero-carrier preparation. Carrier signals
on arrow pairs have form

    S_ij = a_i^T G4 Z G4 b_j /20,

where a_i,b_j are four-state difference vectors. The difference-vector matrices
have rank3, so S has rank at most3 for EVERY16-component carrier state Z. Both
tested record blocks, W and W-4*ones, have rank4. Therefore at least one arrow
port is mismatched for any carrier preparation. Exchanging that port changes
one cell nontrivially and leaves the shared-leg image. Choosing another carrier
state alone cannot make this preparation closed under all selectable exchanges.

The failure concerns the fixed-reference trace adapter and the full declared
shared-leg state class. It does not prove that a restricted physical preparation
class, varying-reference model, or different observable cannot work.

## What a sufficient retained completion contains

A conditional extension keeps the original preparation and reference, and adds
an addressable record correction e_i plus the ordered event history:

    w_i = w_i_initial + e_i,
    delta_i = w_i - u_i^T q,
    e_i_next = e_i-delta_i,
    q_next = q+u_i delta_i.

Initially all corrections vanish. Afterwards w is a retained record of exchange,
not necessarily the current trace of any shared-leg product. The exact checker
runs a five-event word both directly and through this corrected packet; they
agree after every event, including the16 conserved anchors and total budget.
The correction vector is a sufficient storage representation, not a minimality
claim or a derivation of137 new independent physical degrees of freedom.

The seed legs and reference remain provenance. The existing faithful packet
(a,delta) still reconstructs current q,w, but does not replace that provenance
or ordered history. If histories are averaged out, the established covariance
channel is still required; this deterministic-word check performs no averaging.

## Precise missing constructor

Independent oscillator records cannot be silently equated with composite
shared-leg values. The source must provide retained record memory with an
operation that updates it separately from the initial composite preparation.

The next nonredundant test is whether existing comparison witnesses already
supply that memory and operation. Their evaluated boundaries are constrained
by endpoint differences; being a retained witness does not automatically make
its scalar reading independently writable. Check that constraint before adding
another new layer of state by fiat.

## Verification

    python research/nima/checkers/check_matrix_leg_exchange_closure.py
    python research/aspect/scc/scc.py check nima-matrix-leg-exchange-closure

Exact Fraction arithmetic, no random sampling or tolerances. The checker uses
the freshly read shared-leg composition convention and constructs a new hostile
fixture; it does not rerun the entire DG checker. Report:
`research/nima/results/matrix-leg-exchange-closure.json`.

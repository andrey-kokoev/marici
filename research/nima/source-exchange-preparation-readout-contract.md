# Iteration 1: labelled-source exchange adapter and signed echo

## Fresh state and scope

The preceding [adapter audit](exchange-feedback-adapter-and-covariance.md)
established the faithful16-anchor/137-mismatch packet and rejected the natural
identification with family-mean relaxation. This iteration builds on the old
exchange law, not on that rejected identification.

A conditional adapter now connects the labelled tensor-comparison realization
to the exchange state. It preserves label identity, reference transport and
ordered operation histories. It does NOT yet map the native matrix-valued rung
legs into this tensor realization or supply a physical instrument.

## State contract: labels are not amplitudes

The source view retains two four-state labels, all directed legs, and the
separately marked reference. The counted selection excludes the marked directed
leg on each side. Its labels are the121 selected arrow pairs and16 state pairs;
a pair is a comparison slot, not automatically a composable path.

For state labels use e_i; for arrows i->j use e_j-e_i. Tensor these to obtain
v_i in R16. Reuse the earlier probe metric

    G4 = 10 I4+J4,   K0 = G4 tensor G4,   C^T C = K0.

Arrow-pair feature norms are20; state-pair norms are11. Given an additional
prepared raw tensor amplitude z and independent labelled scalar records w_i,

    q = C z,
    u_i = C v_i / n_i,
    n_i = sqrt(v_i^T K0 v_i),
    s_i = u_i^T q = v_i^T K0 z/n_i.

Labels determine features and port addresses, not the prepared amplitudes.
Simultaneously reversing both arrows can leave v_i unchanged while changing
the port label. Those records remain distinct and their exchanges differ.
Compressing by equal features would destroy the adapter.

The retained packet is a=q+U^T w, delta=w-Uq, with reconstruction and covariance
as previously derived. The metric and amplitude interpretation are inherited
assumptions of this response realization, not consequences of the count137.

## Operation contract and the exact additional axiom

At labelled port i the raw-coordinate exchange is

    z_next = z + v_i (w_i-s_i)/n_i,
    w_i_next = s_i,

with other records fixed. Whitening gives exactly the prior exchange law.

There is a conditional uniqueness statement. Require an event to be:

1. linear and norm-preserving;
2. supported only on the selected carrier component s_i and record w_i;
3. pointwise nondisturbing on every matched state s_i=w_i;
4. nonidentity.

On the two-dimensional selected plane an orthogonal map fixing the diagonal
line acts by either +1 or -1 on its orthogonal line. Nonidentity selects -1,
so the event is the swap (s_i,w_i)->(w_i,s_i). This explains exactly which
operational assumptions select exchange. The label geometry alone does not
prove these assumptions for a native comparison or a physical apparatus.

A quarter-turn (s_i,w_i)->(w_i,-s_i) preserves the same norm and port support,
but violates matched-state nondisturbance. It is an explicit competing coherent
operation when that additional axiom is not admitted.

## Reference and history transport

For independent permutations of the two four-state carriers, move the marked
reference and every slot label along with the basis. If R is the tensor basis
permutation, its whitened action is T=C R C^-1. Metric invariance makes T
orthogonal. With the induced record permutation Pi,

    q_new = T q,   w_new = Pi w,
    U_new = Pi U T^T,
    a_new = T a,   delta_new = Pi delta.

Every event intertwines under this transport; hence every ordered word does.
The checker tests all137 events under three reference transports, including
transports that move the marked reference, and tests a multi-event history.
An explicit two-event hostile shows that unordered multisets of labels cannot
replace ordered histories. Although a repeated swap has identity endpoint,
the two-event word must still be retained separately from the empty history.
This is relabelling covariance, not arbitrary rung/reference-gauge transport.

## Preparation and readout contract

A candidate apparatus must support the following operations before the model
can be identified as its description:

- Prepare zero carrier amplitude and one signed record amplitude A at port i.
- Execute one or two identical addressed pulses without intermediate reset.
- Read a signed record amplitude relative to the preparation reference.
- For a separate one-pulse diagnostic, read carrier components s_j.

Use separate identically prepared trials for one-pulse and two-pulse readouts;
do not silently insert a destructive intermediate probe into the echo trial.
Preparation, reset, readout back-action, noise and pulse timing are currently
unmodelled physical resources, not cost-free operations derived by this audit.

For the exchange law, one pulse predicts

    q_after = A u_i,   w_i_after = 0,
    s_j_after/A = u_j^T u_i.

Two identical pulses predict w_i_final/A=+1 and zero carrier amplitude. The
quarter-turn predicts the SAME first-pulse state for this preparation and the
SAME final quadratic budget, but w_i_final/A=-1. Thus a signed echo, not an
energy-only measurement, distinguishes the models. Matched-state preparation
provides a second direct test of the missing nondisturbance axiom.

These are conditional instrument predictions, not reported experimental data.
Same-channel amplitude ratios cancel a common linear detector gain provided
that gain and the signed reference are stable. They do not fix energy units,
pulse strength, charge/current normalization, or electromagnetic coupling.
No equilibrium1/137 claim is used in this discriminator.

## Verification and next gate

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_source_exchange_contract.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-source-exchange-contract

The prior closed-record fixture is rerun. All checks use NumPy tolerance1e-10
and a fixed seed; the report is `results/source-exchange-contract.json`.

Next: find an existing source operation or instrument realization that can
justify the locality, norm preservation and matched-state nondisturbance axioms,
including its preparation and probe costs. Then test the signed echo and the
full cross-port response, rather than choose an operation merely to obtain a
preferred scalar constant. The matrix-leg-to-tensor preparation map remains a
separate explicit obligation.

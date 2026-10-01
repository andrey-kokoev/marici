# Reuse the prior exchange law: exact reduction, failed family-feedback adapter

## Source and obligation

This is a route/readout compatibility test between existing constructions, not
a new guessed dynamics. Reuse the prior real closed-record exchange fixture:
16 whitened carrier coordinates q,137 retained scalar records w, normalized
features u_i, and the declared state-independent schedule that waits half the
time and otherwise selects an exchange uniformly.

This source already supplies endogenous increments:

    delta_i = w_i-u_i^T q,
    q' = q+u_i delta_i,
    w_i' = w_i-delta_i.

Each event is an orthogonal reflection of the full153-dimensional state.
The operation, normalization and schedule remain model assumptions, but B is
not an arbitrary external matrix in this branch.

## A faithful packet for the existing source

Stack u_i^T as the137-by16 matrix U. Define

    a = q+U^T w,
    delta = w-Uq,
    G = I16+U^T U,
    K = I137+UU^T.

The16-vector a is conserved by every individual exchange. The packet (a,delta)
recovers the complete current state:

    q = G^-1(a-U^T delta),
    w = delta+Uq.

Its quadratic budget is

    ||q||^2+||w||^2 = a^T G^-1 a + delta^T K^-1 delta.

The mismatch metric is therefore supplied by this source realization, rather
than borrowed from the newer matrix feedback's control metric. Each realized
exchange preserves both a and the mismatch budget. This packet is not yet an
identification with the30 primitive matrix legs.

## The actual mean-feedback operator

Let D have columns (u_i,-e_i)/sqrt(2), and L=(-U,I). For the declared lazy schedule,

    M = I153-DD^T/137,
    E[x_next] = M E[x],
    L M = R L,
    R = I137-K/(2*137).

Thus the closed mismatch-mean update is

    E[delta_next] = E[delta]-K E[delta]/274.

It is a source-derived feedback kernel under the specified schedule. There is
no need to insert a freely chosen family projection or replace it by one merely
because both operations contract something. Raw records w alone do not close:
the same w with a different q produces a different next record mean.

## Mean contraction does not discard the conserved budget

Let mu and Sigma be the full-state mean and covariance, and Phi the schedule-
averaged second-moment channel. Then

    mu_next = M mu,
    Sigma_next = Phi(Sigma)+Q(mu),
    Q(mu) = sum_events p_event (H_event mu-M mu)(H_event mu-M mu)^T.

Q is positive semidefinite. Orthogonality of every realized event gives

    tr(Q(mu)) = ||mu||^2-||M mu||^2,
    tr(Sigma_next)+||mu_next||^2 = tr(Sigma)+||mu||^2.

For the deterministic one-record test, the initial budget1 becomes mean-square
budget0.992727369599 plus covariance trace0.007272630401. This is ensemble
redistribution, not physical energy loss. The exact formulas close first and
second moments for the state-independent linear schedule; they do not encode
all schedule histories or higher moments.

## The new family law is not this reduction

The actual target-slot family projector P has rank32. The new full calibration
acts on its factored slot values as P. A linear slot interpolation
N_eta=(1-eta)I+eta P fixes all32 family-constant directions. Partial primitive-leg
relaxation has additional bilinear scaling and is not in general N_eta on slots.

By contrast K is positive definite, so R has no nonzero fixed mismatch mean.
A minimal hostile uses the singleton state family at slot121. Its unit vector
v is fixed by P and every N_eta, but

    (R v)_121 = 136/137,   not1.

The natural slot identification therefore fails. More generally, a linear
intertwiner J from mismatch means satisfying J R=N_eta J would obey

    P J (R-I)=0.

Since R-I is invertible, P J=0: it cannot retain nonzero family means. For an
adapter from the full153-dimensional mean state, conserved linear observations
factor through its16-dimensional fixed sector, so it cannot independently
supply all32 unrestricted family-mean coordinates either.

These are bounded first-moment linear obstructions. They do not exclude an
adapter with additional invariant preparation data, retained histories,
covariances, nonlinear readouts, or a different target operation. The complex
phase/backreaction model is also a different source and is not ruled out here.

## Disposition

The earlier work already provides the coherent endogenous response law that
this branch was seeking. Retain its (a,delta) packet and covariance channel as
the established conditional exchange-model reduction. Keep family-disagreement
relaxation as a distinct candidate; do not transfer the earlier equilibrium
1/137 result or conserved budget to it.

Next identify the carrier/record variables and source-derived exchange kernel
with the intended rung transport, or supply an explicitly larger adapter.
Physical charge/current normalization and the relation to the matrix-leg
amplitudes remain open. A preserved quadratic budget alone does not identify
physical energy.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_feedback_adapter.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-exchange-feedback-adapter

The prior closed-record checker is rerun. NumPy checks use tolerance1e-10 for
all138 schedule outcomes, packet reconstruction and budget splitting, the
mean/covariance channel including a nonzero initial covariance, repeated budget
accounting, fixed-space ranks and the singleton-family hostile. Algebraic
identities and the linear obstruction are explained above. This does not rerun
the separate2000-step equilibrium checker or claim a physical normalization.
Machine result: `research/nima/results/exchange-feedback-adapter.json`.

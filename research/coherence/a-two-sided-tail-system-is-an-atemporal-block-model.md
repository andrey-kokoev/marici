# A two-sided tail system is an atemporal block model

## Global block

Take one finite ordered event packet

\[
u=(u_{-N},\ldots,u_N)
\]

and a correlation parameter \(0<\rho<1\). The complete packet is specified at once; no event is generated during the construction.

Define the past-facing and future-facing tails

\[
P_n=\sum_{j\le n}\rho^{n-j}u_j,
\]

\[
F_n=\sum_{j\ge n}\rho^{j-n}u_j.
\]

Every cut \(n\) carries the local observer state

\[
\mathcal O_n=(P_n,F_n).
\]

## Boundary reset

Impose zero exterior conditions

\[
P_{-N-1}=0,
\qquad
F_{N+1}=0.
\]

These are the finite version of residue reset at the two infinities.

The tails satisfy opposite recurrences:

\[
P_n=u_n+\rho P_{n-1},
\]

\[
F_n=u_n+\rho F_{n+1}.
\]

The first can be computed left-to-right; the second right-to-left. In the block interpretation, these are two compatible factorizations of one global object rather than competing causal laws.

## Local consistency cell

At every event,

\[
u_n=P_n-\rho P_{n-1}
=F_n-\rho F_{n+1}.
\]

Equivalently,

\[
P_n-\rho P_{n-1}
-F_n+\rho F_{n+1}=0.
\]

This four-term equation is the local gluing condition between the past and future presentations of the block.

## Reflection

Reversing event order exchanges the two tails:

\[
P_n\longleftrightarrow F_{-n}.
\]

The complete observer double is therefore reversal closed. Choosing only \(P\) or only \(F\) introduces a causal orientation; retaining both leaves the model atemporal.

## What an internal observer sees

An observer localized at cut \(n\) has access only to \((P_n,F_n)\), not directly to the entire packet. Moving the cut changes this local state according to the consistency equations. That change can appear evolutionary even though all cuts coexist in the global block.

```text
global description:
  one completed event packet with two zero exterior boundaries

local description:
  neighboring observer states connected by update equations
```

## Infinite limit

On a bi-infinite packet in an admissible sequence space, require

\[
P_n\to0\quad(n\to-\infty),
\qquad
F_n\to0\quad(n\to+\infty).
\]

The two convolution fields then solve the recurrences uniquely. The “zero at infinity” selects the global solution but does not force finite local states to vanish.

## Status

This is a precise toy block model. It does not identify the index with physical time or derive relativity. Its established content is:

- atemporal global specification;
- local past/future observer doubles;
- boundary reset at both ends;
- exact local reconstruction;
- reflection exchanging temporal orientations.

A physical interpretation would require an independent map from events and cuts to spacetime observables.

## Verification

```text
python research/coherence/check_two_sided_block_observer_model.py
```

The checker verifies 100 exact rational blocks of 21 events, including both reconstructions and reflection covariance.

Artifacts:

- `check_two_sided_block_observer_model.py`
- `two-sided-block-observer-model.v1.json`

# Local Green–Schwarz split realizability fiber: WP1111

## Question

Can WP1068's parent coefficient \(k_{\rm GS}=-3\) admit a local endpoint split
compatible with WP1110's seven-channel lift?

## Exact split fiber

Parametrize the endpoint split by

\[
g_0=-\frac32+t,\qquad g_\pi=-\frac32-t,
\]

so \(g_0+g_\pi=-3\). For the one-quartet remnants, the two gauge-gravity
inflow levels become

\[
k_4=-\frac14-t,\qquad k_2=-t.
\]

Thus:

- exact WP1110 target \((-1/4,0)\) requires \(t=0\);
- at the mod-\(\mathbb Z\) shifted-lattice level, any \(t\in\mathbb Z\)
  preserves the same coset;
- endpoint exchange sends \(t\mapsto -t\), so reflection invariance would
  force \(t=0\).

No current source authorizes endpoint exchange or selects \(t=0\).

## Classification

Conditional gate. The local split is realizable over the integer/orientation
fiber, but the parent coefficient alone does not select it.

Checker: `research/flavor/checkers/wp1111_local_gs_split_realizability_fiber.py`

Result: `results/wp1111_local_gs_split_realizability_fiber.json`

---
author: marici.Grothendieck
---

# 3051 — The Minimal Theta Source Has No Finite Constant-Coefficient Scalar Closure

The positive-chart primitive theta label can be written, up to a positive
constant, as

\[
\phi_1(u)=x^{1/4}(4x^2-6x)e^{-x},
\qquad x=\pi e^{2u}.
\]

For (D=\partial_u=2x\partial_x), write

\[
D^j\phi_1=x^{1/4}e^{-x}q_j(x).
\]

The exact recurrence

\[
q_{j+1}=2xq_j'+\left(\frac12-2x\right)q_j
\]

gives

\[
\deg q_j=j+2,
\qquad
[x^{j+2}]q_j=4(-2)^j.
\]

Consequently, for every nonzero constant-coefficient operator

\[
P(D)=\sum_{j=0}^r a_jD^j,
\qquad a_r\ne0,
\]

the degree-(r+2) term of (P(D)\phi_1) is uniquely contributed by the
highest derivative and cannot cancel. Thus (P(D)\phi_1\ne0).

The full positive-chart theta sum has the same property. At large positive
(u), its first label has exponential scale (e^{-\pi e^{2u}}), while all
later labels are exponentially smaller. They cannot cancel the first label's
nonzero leading polynomial identically.

Therefore the theta source has no finite constant-coefficient scalar jet
closure. A Green conservation system that retains only finitely many
aggregate derivatives necessarily loses source information; the labelled or
infinite-dimensional state is mandatory.

## Scope

This excludes only finite constant-coefficient linear scalar closure. It does
not exclude variable-coefficient or nonlinear identities, independently
retained arithmetic variables, or infinite labelled systems. It does not
prove RH.

## Durable verification

- Research packet: `research/grothendieck/the-minimal-theta-source-has-no-finite-constant-coefficient-scalar-closure.md`
- Exact checker: `research/grothendieck/checkers/minimal_theta_no_constant_ode.py`
- Result: `research/grothendieck/results/minimal_theta_no_constant_ode.json`
- Sequence claim: `seqclaim-fa6c5c9e4561161320df4eba`
- Graph event: `ev-000000006071-a6009d29-6539-45b9-8caf-be18690a6512`

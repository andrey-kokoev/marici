---
author: marici.Benincasa
date: 2026-08-27
---

# 3637 — The Physical Odd Endpoint Divisor Is Principal Integrally

## Exact correction

Let

\[
D_+=p_\infty^+-p_0^+,
\qquad
D_-=p_\infty^--p_0^-.
\]

Entry 3627 derived

\[
\operatorname{div}(\phi_+)=2D_+,
\qquad
\phi_+=\frac{W-xt^2+y}{t^2}.
\]

The source coordinate has

\[
\operatorname{div}(t)=-(D_++D_-).
\]

Adding these principal divisors gives

\[
\operatorname{div}(t\phi_+)
=D_+-D_-
=\tau.
\]

An explicit principal witness is therefore

\[
t\phi_+
=
\frac{W-xt^2+y}{t}.
\]

Hence

\[
[\tau]=0
\quad\text{in}\quad
\operatorname{Pic}^0(E_X)
\]

integrally. The earlier order-two statement was true but non-sharp: the order
divides one.

## Consequences

The following survive:

- \(\tau\) is a nonzero labelled zero-chain;
- \(\tau=\partial(\gamma_+-\gamma_-)\) in the marked relative-chain packet;
- the raw rational extension block is gauge;
- deck and reciprocal involutions act by sign on the chosen divisor lift.

The following are withdrawn:

- a nonzero integral endpoint two-torsion Jacobian class;
- a characteristic-two Cartan-module attachment;
- a discrete torsion holonomy;
- a Weil-pairing frontier for \(\tau\).

The surviving object is relative incidence, not an absolute Picard class.
The next calculation must remain inside the marked relative complex and test
whether the principal witness supplies a canonical splitting compatible with
the physical finite-part covector.

## Evidence

- `research/benincasa/checkers/check_endpoint_odd_divisor_principal.py`;
- `research/benincasa/results/endpoint-odd-divisor-principal.json`.

The exact checker passes five of five gates.

Epistemic graph event:
`ev-000000007813-4be5fef6-eb71-4eea-9de6-66c3a6136263`.

Allocator claim: `seqclaim-66e0fd8302f48a32a8514a62`.

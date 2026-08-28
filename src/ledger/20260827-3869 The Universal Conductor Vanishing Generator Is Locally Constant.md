---
authors:
  - marici.Benincasa
date: 2026-08-27
---
# 3869 — The Universal Conductor Vanishing Generator Is Locally Constant

## Local specialization object

Away from the existing triangle support, (S\neq0), the active conductor has
the completed double-cover model

\[
w^2=R^2+qS.
\]

At (q=0) this is a node. Its fiber Jacobian ideal is ((2w,-2R)), so the
Milnor algebra is one-dimensional. The specialization cone of Entry 3866
therefore carries one universal local vanishing direction.

Set

\[
R=\lambda t,
\qquad
w=\lambda\sqrt{t^2+1},
\qquad
\lambda^2=qS.
\]

For the physical exponent (\alpha=-\tfrac12+\epsilon), the universal local
measure scales as

\[
dR\,K^\alpha
\sim
(qS)^\epsilon
\frac{dt}{(1+t^2)^{1/2-\epsilon}}.
\]

After the source normalization cancels the local (1/\epsilon) pole, the
universal grade-zero vanishing generator is independent of (q) and (S).
The first epsilon grade contains (\log q+\log S).

## Necessary scope correction

This does not prove that the complete source conductor port is horizontal.
The full iterated residue also contains the source numerator and all spectator
marked-wall denominators evaluated at the conductor. Those coefficients vary
with the external kinematics, as the explicit formulas and asymmetric sample
in Entry 3862 already show.

The correctly typed factorization is therefore

\[
\text{source conductor port}
=
\text{variable source coefficient}
\otimes
\text{constant universal }A_1\text{ generator}.
\]

Only the second factor has been trivialized here. Testing horizontality of the
first factor still requires the labelled specialization map from the rank-26
connection. Scalar differentiation of the residue formula alone does not
replace that map.

## Narrow result

The local coefficient object is exactly one rank-one specialization costalk;
no additional local carrier or higher-rank coefficient block is needed away
from triangle support. Its universal generator is locally constant at grade
zero. The complete source-selected section remains untested for Gauss--Manin
horizontality.

## Verification

- checker: `research/benincasa/check_rank26_conductor_cone_gradezero_horizontality.py`;
- packet: `research/benincasa/rank26-conductor-cone-gradezero-horizontality.json`;
- allocator claim: `seqclaim-e83876dc6d9624688d7cb338`.

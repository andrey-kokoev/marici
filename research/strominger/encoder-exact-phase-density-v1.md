# Exactly executable bank phases retain the continuous reachable closure

## Question and disposition

The operator requested a test of the shared premise behind terminating certified
synthesis: replacing arbitrary continuous bank phases by an exactly executable,
countable vocabulary must not destroy the preceding reachability result.

The premise survives in the declared software model. Dyadic parameters give
exact phases in the arithmetic field already used by the source bank-pulse
implementation. Their finite words have the same closure as the continuous
family. This is not physical switching admission or a completed encoder compiler.

## Exact source-compatible phase vocabulary

For rational t define

    z(t)=(1-3t^2)/(1+3t^2) + i sqrt(3) * 2t/(1+3t^2).

The source arithmetic represents a+i sqrt(3)b with a,b in Q(sqrt(2)); here both
are rational. No trigonometric or floating evaluation is needed. The existing
bank-pulse implementation in `check_neutron_canonical_record_binding.py` takes
such a phase and checks its norm. The present checker uses the same R, add, mul,
conj, scale and norm operations, on the exact 45-coordinate extension of that
stored bank projector P.

    |z(t)|^2=1,
    z(-t)=conjugate(z(t)),
    U(t)=I+(z(t)-1)P.

P is the actual metric-self-adjoint rank-one projector. Therefore U(t) is exactly
metric-unitary on every input; its inverse is U(-t). The phase -1 is also
retained explicitly as the existing exchange endpoint.

## Quantitative density, not sampled density

A sparse exact polynomial calculation verifies the cleared-denominator identity

    |z(t)-z(s)|^2 = 12(t-s)^2 / ((1+3t^2)(1+3s^2)).

Its denominator is at least one for real t,s. Hence

    |z(t)-z(s)| <= 2 sqrt(3)|t-s| <= 4|t-s|.

Every circle point a+i sqrt(3)b except -1 has parameter t=b/(1+a), because
its norm equation is a^2+3b^2=1. Dyadic rationals approximate every real t.
Together with the explicit -1 endpoint, the vocabulary is dense in the entire
unit circle. These are general algebraic and real-analysis arguments; the
finite phase fixtures below are regressions, not a promotion of samples.

For the inherited operator norm,

    ||U(t)-U(s)|| = |z(t)-z(s)|,

since a nonzero orthogonal projector has norm one. Metric-unitary conjugation by
any retained discrete control word preserves this bound. Telescoping products
of unitary operations gives total word error at most the sum of phase errors.
Replacing L phase parameters by dyadics within 2^-n therefore gives a bound
4 L 2^-n; discrete conjugating operations contribute no approximation error in
this exact arithmetic model.

Consequently every finite continuous-control word is approximable by exactly
executable words, and the two generated groups have the same closure. Combined
with the preceding written u(39) theorem and its exact source certificate,
the polar encoder remains in this closure. This conclusion uses the same
software composition/inversion contract, not hypothetical independent phase
actuators on all seam or memory-write projectors.

## Explicit fair word enumeration

At stage n>=1 include t=m/2^n for |m|<=n*2^n, the phase -1, all existing discrete
seam/write reflections, R, and R^-1. Enumerate every primitive word of length
at most n over that finite stage alphabet. Each dyadic phase and every finite
word eventually appears; no bound on efficiency is claimed. The countably
infinite parameter vocabulary is not replaced by a fixed finite grid.

A control demonstrates the direct-approximation error from truncating parameters:
for |t|<=1, |z(t)+1|^2=4/(1+3t^2)>=1. Adding -1 alone still leaves missing arcs
in that single-phase set. This is NOT a group obstruction: products of phases
from an arc can cover the circle. The hostile only rejects identifying a bounded
parameter interval with a direct dense parametrization of all phases.

## What this resolves for a future compiler

The exact alphabet does not destroy the reachable closure. Finite matrices of
these words can be evaluated in the source field without a binary64 accuracy
floor. A certified evaluator for the exact polar target is still needed.

With such an evaluator, a baseline can dovetail word enumeration and evaluation
precision, accepting only a rigorous strict upper bound below epsilon. It must
not wait forever on one word whose distance equals the threshold. Reachability
supplies a word with strict margin, so convergent interval bounds would eventually
accept it. This is an algorithm specification conditional on that evaluator,
not an executed compiler or its WG composition.

## Fresh verification

    python research/strominger/checkers/check_encoder_exact_phase_density.py

The final execution passes 50 phase fixtures and 2250 full-basis inverse tests,
exact source projector identities, the general cleared-denominator polynomial
identity, and the bounded-single-phase control. It also validates source/checker
hashes from the preceding orbit and controllability receipts.

Receipt: `results/encoder-exact-phase-density.json`.
No polar evaluator, optimized gate word, formal-kernel certificate, hardware
capability, or fresh predecessor-suite replay is claimed. No commit or push.

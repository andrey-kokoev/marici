# `q_g2` tangency descent: fourth conjecture cycle

## Problem

The conductor-closed wall class has Kummer character `+1`, while a generic ambient meridian around the transverse branch divisor has character `-1`.

## Bold conjecture

The character mismatch kills every nearby-cycle transport of the wall class into the ambient exceptional surface.

## Named rivals

1. the wall loop transports to one ambient branch meridian and is killed;
2. it transports to a cycle enclosing both split branch points, whose product character is `+1`;
3. no local nearby-cycle model is defined from the tangency data.

## Risky consequences

A local smoothing of the double cover must either have no annular cycle compatible with wall character or exhibit an explicit even cycle. This must follow from the local equation, not from desired nonvanishing.

## Strongest falsification attempt and residual

Let `s=xi+kappa` and let `t` be the transverse `a-p` coordinate. Up to a nonzero scalar, the local double cover is

\[
W^2=ps^2+(\kappa^2-1)t.
\]

Set

\[
U=W+\sqrt p\,s,
\qquad V=W-\sqrt p\,s.
\]

Execution `structured_command_execution:e_7396_1788303248179082200_12` verifies

\[
UV=(\kappa^2-1)t.
\]

This is the standard nodal smoothing. For nonzero `t`, its annular nearby cycle projects to a loop enclosing both split branch points. Each single branch meridian has character `-1`, but the enclosing cycle has product character `(+1)`. Therefore the wall class is not locally killed; the bold conjecture is falsified.

## Disposition and residual conjecture

The conductor-closed wall class has a canonical local transport to the even two-branch nearby cycle. It cannot transport to either odd single-branch meridian. The remaining conjecture is physical rather than local-algebraic: the positive-cut relative chain maps to this even nearby-cycle class. If it has an odd branch component, the conductor class is obstructed.

The next falsifier is to derive the branch-parity of the positive-cut chain from its source inequalities or contour prescription, rather than infer it from the desired pairing.

## Evidence

- `research/nima/checkers/check_qg2_tangency_nearby_cycle.py`
- `research/nima/qg2-wall-kummer-euler-dpc.md`

# Return-leg unitarity test

Checker: `checkers/check_return_leg_unitarity.py`.
Receipt: `results/return-leg-unitarity.json` — 32 exact checks.

## Affine candidate rejected

The implemented leg is `(1-t)v+tPv`. For either source bit flip and each of the four basis vectors, the midpoint has squared norm `1/2`. Thus the current affine return realization is not unitary.

## Local unitary replacement

For either flip `P`, put `Q=(I-P)/2` and `A=I-Q`. The exact matrix checks establish that `Q,A` are orthogonal self-adjoint projectors. Set

`U(t)=A+exp(-i*pi*t)Q`.

For every real `t`, projector orthogonality gives

`U(t)* U(t)=A+|exp(-i*pi*t)|²Q=I`.

Also `U(0)=I`, `U(1)=A-Q=P`, and `i U'(t)=pi Q U(t)`. The left generator is `pi q ⊗ I`, the right is `I ⊗ pi q`, where `q=(I-X)/2`; they commute. This proves factorwise locality for the full real-parameter family, not just the sampled phases.

At `t=1/2`, the replacement sends a basis vector to `(1-i)e/2+(1+i)Pe/2`, of squared norm one. The checker verifies this and the endpoints using rational complex arithmetic.

A two-segment return path can therefore reverse the schedule order and use these unitary legs with the same intermediate corners. Composing unitary legs preserves norm and the seam agrees exactly. Positive continuation along the reversed order is not automatically the time reversal of the forward curve: literal time reversal uses inverse phases. That convention must be fixed when connecting to source reversal.

## Next implementation

Construct the complex completion phase `exp(-i*pi*t)` and prove its unit norm, endpoints, and continuity; then replace affine legs while retaining the whole-Tick reconstruction and schedule-swap laws. The current test establishes the matrix-level replacement, not this completion implementation.

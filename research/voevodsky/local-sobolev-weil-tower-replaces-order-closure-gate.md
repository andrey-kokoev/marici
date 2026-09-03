# Local Sobolev Weil tower replaces the order-closure gate

## Question

Can the completed-form layer be constructed source-first without proving closability of the completed-heat Hankel form on the order realization?

## Claim boundary

Yes, locally in logarithmic support. Prior source-side estimates construct a bounded compact self-adjoint Weil operator on every positive Sobolev completion of every fixed support window. This removes raw Hankel/order closability as an RH prerequisite. It does not provide the global support coherence, identify the local source form with the Gaussian Hankel form, or prove positivity.

## Local objects

For \(L>0\), set

\[
C_L=C_c^\infty((-L,L)).
\]

For any \(s>0\), complete this core as

\[
X_{L,s}=H_0^s((-L,L)).
\]

The endpoint and prime sectors are \(L^2\)-bounded on fixed support. The gamma multiplier grows as \(O(\log(1+|u|))\), hence is bounded relative to every positive Sobolev norm. The completed source form therefore has a bounded self-adjoint representative

\[
Q_L(f,g)
=
\langle A_{L,s}f,g\rangle_{H^s}.
\]

For \(s>0\), the representative is compact: the endpoint block is finite rank, prime translations factor through the compact Sobolev embedding, and the Sobolev-normalized gamma symbol tends to zero.

## RH-bearing condition

The domain problem and positivity problem separate. The local condition is

\[
A_{L,s}\geq0.
\]

RH requires the corresponding Weil positivity statement for every support window, with the precise source criterion retained. The completed operator exists independently of that positivity.

## Support coherence

For \(L\leq L'\), extension by zero defines a core map

\[
i_{L,L'}:C_L\longrightarrow C_{L'}.
\]

The source forms must obey

\[
Q_{L'}(i_{L,L'}f,i_{L,L'}g)
=
Q_L(f,g).
\]

The Riesz operators need not form a strictly commuting square because their ambient Sobolev inner products depend on \(L\). The invariant object is the compatible family of forms on nested cores, not literal equality of the representing operators.

## Gaussian comparison residual

The existing structural identities use Gaussian dilation vectors, which are not compactly supported. Therefore they do not lie in any single \(C_L\). The local Sobolev tower solves the source-form completion problem but does not itself enrich the Gaussian realization identity.

A comparison requires either:

1. a source-derived cutoff family whose limit preserves both the Weil form and the Gaussian observer identities; or
2. a common Fourier-stable Gaussian Gelfand--Shilov rigging on which the arithmetic boundary constructors are continuous.

This is a comparison gate, not a reason to return to raw Hankel/order closability.

## Galerkin consequence

A negative eigenvalue of compact \(A_{L,s}\) has a finite-dimensional witness. A positive finite compression does not prove positivity because unresolved eigenvalues may accumulate at zero. A positive certificate requires a signed tail estimate or a Schur bound controlling the complement and off-diagonal block.

## Disposition

The local completed-form layer is constructed. The next global coherencer is the nested-support form compatibility together with a source-derived comparison to the Gaussian rigging. The next RH-bearing analytic target is a signed Galerkin tail certificate. No RH implication is asserted.

## Sources

- `research/grothendieck/local-sobolev-completion-separates-weil-domain-from-positivity.md`
- `research/grothendieck/archimedean-weil-form-is-bounded-on-every-positive-sobolev-scale.md`
- `research/grothendieck/local-sobolev-weil-operators-are-compact-and-have-discrete-negative-spectrum.md`
- `research/grothendieck/sobolev-gap-gives-computable-galerkin-tail-rates-for-local-weil-operators.md`
- `research/grothendieck/a-fourier-stable-gaussian-rigging-restores-moment-faithfulness.md`
- `research/grothendieck/a-source-typed-fourier-order-kernel-exists-without-identifying-it-with-the-hankel-kernel.md`

## Verification

- `research/voevodsky/local-sobolev-weil-tower-plan-v1.json`
- `research/voevodsky/checkers/check_local_sobolev_weil_tower_plan.py`
- `research/voevodsky/results/local_sobolev_weil_tower_plan.json`

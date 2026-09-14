# Radial metric descent and the first RH-chain interface obstruction

## Question

Does the synthetic noise-whitened radial metric descend through gauge equivalence and pass into the current Evans/Green/RH interface?

## Claim boundary

This packet proves a conditional finite-dimensional descent theorem and checks it against the current synthetic calibration and radial-interface contracts. It does not construct the downstream Evans/Green/RH chain. The current contracts stop at the first missing typed comparison from the calibrated 26-coordinate record space to the four-trace radial interface.

## Conditional descent theorem

Let a group \(G\) act on a state space \(S\). Let \(Y\) be a finite-dimensional real record space with a positive-definite covariance \(\Sigma\), and let

\[
\mathcal R:S\longrightarrow Y.
\]

Assume either:

1. \(\mathcal R\) is invariant on \(G\)-orbits; or
2. \(G\) acts on \(Y\) by a representation \(T_g\), the record map is equivariant, and
   \[
   T_g^{\mathsf T}\Sigma^{-1}T_g=\Sigma^{-1}.
   \]

In the first case,

\[
d([x],[y])^2=(\mathcal R(x)-\mathcal R(y))^{\mathsf T}
\Sigma^{-1}(\mathcal R(x)-\mathcal R(y))
\]

is representative-independent. In the second case the same formula is invariant under simultaneous gauge transport of both records. It defines a metric rather than a pseudometric exactly when the induced record map on the chosen quotient is injective.

Proof: invariance follows by substitution. Positivity follows from positive definiteness of \(\Sigma^{-1}\). Vanishing implies equality of records; equality of quotient classes then requires injectivity of the induced record map.

If a Real involution \(J_Y\) on records satisfies

\[
J_Y\Sigma J_Y=\Sigma,
\]

then whitening commutes with the Real sector decomposition. Covariance terms between opposite Real parities must vanish; parity-matched cross-sector covariance is allowed.

## Application to the synthetic packet

The synthetic packet has two distinct gauge behaviors:

- Wilson holonomy is invariant under the declared vertex gauge action and therefore descends to the edge-connection quotient.
- Bulk node coordinates are gauge-covariant and retain local frames. They do not descend after forgetting those frames.

Consequently the 26-coordinate joint metric is defined on the framed bulk record space times the Wilson quotient. It is not yet a metric on an unframed bulk gauge quotient. The checker detects the attempted stronger descent.

The diagonal packet and the perturbed covariance family are positive and Real-compatible. Simultaneous coordinate and covariance congruence preserves the quadratic form. Holding covariance fixed while relabelling records does not.

## Pullback through a downstream map

For a typed map \(F:Z\to S\), the pulled-back quadratic form is

\[
g_z(v,w)=D(\mathcal R\circ F)_z(v)^{\mathsf T}
\Sigma^{-1}D(\mathcal R\circ F)_z(w).
\]

It is positive definite on a declared quotient tangent space exactly when \(D(\mathcal R\circ F)_z\) is injective there. Thus every downstream comparison must supply:

- its source and target spaces;
- its gauge and Real actions;
- the map into the calibrated record space;
- covariance transport or an isometry certificate;
- the kernel after quotienting.

Equal dimensions or a named response operator do not supply these data.

## Current RH-chain interface audit

The Aspect v3 contract declares four boundary traces \(P,Q,M,J\), responses \(K,H_K,J_K\), a radial Real structure, graph and ambient metrics, and an internal Euler-to-radial loading. It explicitly leaves the downstream Evans/Green/RH chain open.

The synthetic companion declares a 26-coordinate record \((R_X,R_M)\), its gauge policy, covariance, and Real grading. Neither contract declares a typed map

\[
C_{\mathrm{cal}}:\mathbb R^{26}\longrightarrow
Y_{P}\oplus Y_{Q}\oplus Y_{M}\oplus Y_{J}
\]

or the reverse observation map from four traces into the calibrated records. No dimensions, units, covariance pushforward, or kernel are supplied for such a comparison.

Therefore the first obstruction is not Evans determinant evaluation, Green inversion, or RH factorization. It is the absent calibrated-record-to-four-trace comparison. Every later metric-preservation question is deferred until this map exists.

## Acceptance test for reopening

A successor must provide:

1. a typed comparison between the 26 calibrated coordinates and the four trace spaces;
2. its matrix or evaluable rule on the retained lattice;
3. gauge equivariance and Real equivariance checks;
4. the pushed covariance;
5. the kernel on the declared quotient;
6. a rank test showing whether the pulled-back form is a metric or only a pseudometric.

## Disposition

The invariant conditional metric theorem survives. Wilson descent is established in the synthetic model; unframed bulk descent is not. The downstream chain is blocked at the missing calibrated-record/four-trace comparison, not at a failed RH theorem.

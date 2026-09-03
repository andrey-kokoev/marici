# Entire-kernel observer nerve

## Question

Does the latching--matching phase-space picture imply that each observer vertex is an independent identity-generator, or are several apparent vertices charts of one deeper object?

## Claim boundary

This packet identifies one entire kernel as the common generator of three observer charts and verifies the transition formulas on an exact atomic fixture. Global positivity remains open.

## Common analytic apex

Let

\[
K(t,z)=W\left(e^{-tu^2}e^{izu}\right).
\]

Assume \(K\) is even and entire in \(z\), and satisfies

\[
\partial_tK=\partial_z^2K.
\]

Three observer families are restrictions of this one object.

### Heat-jet chart

Define

\[
J_k(t)=(-1)^k\partial_t^kK(t,0).
\]

Evenness and the heat equation give

\[
K(t,z)=
\sum_{k\geq0}
\frac{(-1)^kJ_k(t)z^{2k}}{(2k)!}.
\]

All heat jets at one fixed positive \(t\) determine the entire character kernel.

### Gram chart

For a finite translate packet \(I=(a_1,\ldots,a_r)\),

\[
G_I(t)_{ij}=K(t,a_i-a_j).
\]

All real character values determine the jets by differentiation, while rational real values determine the continuous real restriction densely. Entire continuation then determines \(K\).

### Shifted-Gaussian chart

Completing the square gives

\[
\Theta(t,\xi)
=
W\left(e^{-t(u-\xi)^2}\right)
=
e^{-t\xi^2}K(t,-2it\xi).
\]

Thus shifted Gaussians are the gauged imaginary-character restriction. They are not identical to real translation probes.

## Observer nerve

Let the central vertex be the entire kernel \(K\). The heat-jet, Gram, and shifted-Gaussian vertices are chart functors out of it. Their pairwise transition maps form triangular faces, and the comparison of those faces forms the next coherence level.

The completed diagram is:

\[
K
\longrightarrow
\{J_k\}_{k\geq0},
\qquad
K
\longrightarrow
\{G_I\}_I,
\qquad
K
\longrightarrow
\Theta.
\]

Each chart is conservative only with its analytic hypotheses:

- jets require entire Taylor reconstruction and growth control;
- real Gram values require continuity and analytic uniqueness;
- shifted Gaussians require holomorphic continuation along the imaginary locus.

Hence the vertices are not independent identity-generators. The entire \(K\) is the common generator; the other vertices are coordinate presentations of its observer content.

## Latching and matching reinterpretation

At a chart vertex, the latching object collects finite approximations already constructed. The matching object collects restrictions demanded by other charts. The local phase space pairs:

- what finite arithmetic or Taylor data have not yet constructed;
- what other charts can still detect.

When all transition cells are exact, the chart phase spaces contain only approximation residuals, not independent completed curvature.

## Four independent residual axes

The unified kernel does not merge the truncation errors:

| Axis | Residual |
|---|---|
| Arithmetic cutoff \(N\) | omitted endpoint/gamma/prime completion tail |
| Jet cutoff \(m\) | Taylor or Cauchy-circle remainder |
| Packet sampling \(I\) | finite restriction of the real character locus |
| Analytic continuation | growth bound justifying movement between real and imaginary loci |

A finite jet truncation and a finite prime cutoff can produce similar numerical errors but belong to different categorical arrows.

## Positivity transport

If one chart is proved positive and its transition functor is conservative and order-reflecting, positivity transports to the others. For example, positivity of every real Gram packet is the positive-definite-kernel face. Heat jets reconstruct the scalar kernel but do not make positivity termwise in \(k\).

Therefore one should prove positivity in the chart where the source constructor is strongest, then transport it. Reproving positivity independently in all three charts adds no logical strength.

## Exact atomic fixture

For an even two-atom measure at \(\pm a\),

\[
K(t,z)=e^{-ta^2}\cos(az).
\]

The checker verifies:

- the heat equation and evenness;
- six heat-jet coordinates;
- Taylor reconstruction through order ten with a nonzero order-twelve remainder;
- exact shifted-Gaussian pullback;
- finite Gram evaluation from the same \(K\).

## Current arithmetic status

The source-derived completed comparison has now been reported to commute with gamma integration, infinite prime summation, and every fixed derivative order on compact parameter strata. The completed cross-family face curvature is zero. At finite prime cutoff, its residual is only the controlled arithmetic tail.

The unresolved apex coordinate is still positivity of the common completed kernel or equivalent Douglas residual.

## Disposition

The observer pyramid compresses further: three apparent infinite observer families form the nerve of one entire analytic kernel. Identity generation occurs at the analytic apex; chart vertices inherit identities through restriction and reconstruction. Their finite residuals remain separately indexed, preventing arithmetic, Taylor, sampling, and continuation errors from being conflated.

## Verification

- `research/voevodsky/entire-kernel-observer-nerve-v1.json`
- `research/voevodsky/checkers/check_entire_kernel_observer_nerve.py`
- `research/voevodsky/results/entire_kernel_observer_nerve.json`

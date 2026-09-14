# The Euler product is compound Poisson only to the right of one

## Source-positive probability construction

For \(\sigma>1\), the Euler product gives absolutely

\[
\log\zeta(\sigma+it)
=
\sum_p\sum_{k\ge1}
\frac{p^{-k\sigma}}{k}e^{-itk\log p}.
\]

Therefore

\[
\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=
\exp\left[
\int_{\mathbb R}
(e^{-itx}-1)\,d\nu_\sigma(x)
\right],
\]

where

\[
\boxed{
\nu_\sigma
=
\sum_p\sum_{k\ge1}
\frac{p^{-k\sigma}}k\,\delta_{k\log p}
}
\]

is a finite positive measure. Thus the normalized Euler product is the characteristic function of a compound-Poisson random variable. The determinant cumulants \(p^{-k\sigma}/k\) are exactly the positive jump intensities previously obtained by applying the inverse-frequency port to von Mangoldt atoms.

This construction is entirely source-derived and uses no zero information.

## Critical-half-density obstruction

At \(\sigma=1/2\), the primitive jump mass is

\[
\sum_p p^{-1/2}.
\]

It diverges, since

\[
p^{-1/2}\ge p^{-1}
\]

and Euler's theorem gives \(\sum_p1/p=\infty\).

This divergence cannot be absorbed as ordinary infinite small-jump activity. The jump locations are

\[
k\log p\ge\log2,
\]

so every jump lies away from the origin. A Lévy measure must have finite mass outside every neighborhood of zero:

\[
\int(1\wedge x^2)\,d\nu(x)<\infty.
\]

Here that condition reduces to finite total mass and fails. Standard Lévy--Khintchine compensation subtracts a linear term only for small jumps; it cannot renormalize infinitely many large positive prime jumps.

Hence the positive prime-power Lévy measure has no direct continuation from \(\sigma>1\) to the critical half-density line.

## Completion does not preserve the probability law

The completed function introduces:

- pole/endpoint factors;
- the archimedean gamma factor;
- analytic continuation of the divergent Euler logarithm.

These operations produce the correct endpoint--gamma--prime explicit formula, but they are not addition of independent positive jump processes. At the critical line the prime contribution is a signed/renormalized distribution whose cancellation against endpoint and gamma is essential.

Consequently, interpreting completed \(\xi\) or its logarithmic derivative as an infinitely divisible characteristic function would require a new positive renormalization theorem. Constructing its Lévy measure from critical-line zeros would be circular; constructing it from the completed source is equivalent to the complete-Bernstein/Stieltjes gate already identified.

## Relation to Li conditional negative definiteness

Under RH, the Li sequence has a Hilbert cocycle and is conditionally negative definite. Schoenberg then produces positive-definite exponentials \(e^{-t\lambda_n}\). But its CND proof uses zero phases on the unit circle.

The Euler compound-Poisson law gives the desired positivity before zero data only for \(\sigma>1\). The gap between these two statements is now exact:

\[
\boxed{
\text{positive Euler jump measure for }\sigma>1
\quad\not\longrightarrow\quad
\text{critical Li/Weil positive measure at }\sigma=1/2.
}
\]

The failure occurs before endpoint normalization: the primitive large-jump mass already diverges.

## Comparison with another prior Lévy route

`primitive-fourth-cumulant-is-a-memorylessness-defect-balance.md` develops a source-specific Bernstein/subordinator conjecture for a positive primitive theta wall-flux carrier. That construction is mathematically substantive, including a forced Volterra deconvolution for its candidate Lévy tail. It concerns a different positive residual law and does not identify its Lévy exponent with the coupled endpoint--gamma--prime Weil functional. It therefore cannot presently cross the RH gate.

## Search result

Repository, PDF, and web searches found probability/Lévy reformulations and standard Li equivalences, but no published positive renormalization of the critical Euler jump process that reproduces the completed Weil observer.

The exact surviving probability question is:

> Can endpoint and gamma completion be realized as a source-authorized compensation of the divergent large-jump Euler process yielding a positive Lévy measure at half density?

Ordinary Lévy--Khintchine theory answers no for the unmodified prime atoms; any positive answer must introduce a genuinely coupled global boundary operation.

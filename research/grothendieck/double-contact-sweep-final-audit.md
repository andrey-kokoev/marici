# Audit of `double_contact_sweep.agent.final.md`

## Question

Does the sweep supply a correct noncircular reduction beyond the existing finite source certificates?

## Claim boundary

It contains useful interfaces and route obstructions, but its designated enclosure pipeline has two fatal mathematical defects and does not repair the unbounded-scale residual.

## Useful material

1. The corrected endpoint elimination

\[
A^2+\left(2\xi A+B/t\right)^2=e^{t/2-2t\xi^2}
\]

is consistent with direct differentiation.
2. The on-axis prime profile

\[
P(s)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-s(\log n)^2}
\]

is completely monotone. This may tighten bounded one-dimensional interval propagation, although complete monotonicity of the negative term alone does not prove positivity of the signed sum between sampled parameters.
3. The Paley--Wiener/Jensen density obstruction correctly eliminates exact compact-support cardinal isolation of all but one zero pair.
4. The report correctly rejects zero-number, variation-diminishing, average large-sieve, generic transversality, and compact-window-margin globalization as global contact exclusions.
5. Its requirement for certified endpoint, gamma, prime, tail, quadrature, and rounding enclosures matches the existing Arb architecture.

## Fatal defects

### Prime-tail direction is reversed

For fixed `n`,

\[
e^{-(\log n)^2/(4t)}
\]

increases with `t`. Therefore a phase-free tail bound uniform on `t in [t1,t2]` must use `t2`, not `t1`. Estimate E* instead places `t1` in the dominating exponential. No unspecified constant `C(t2)` repairs this as written without absorbing the entire missing exponential ratio.

The associated cost calculation is also inconsistent. Solving

\[
\frac{(\log N)^2}{4t}\approx |\log\varepsilon|
\]

gives

\[
\log N\approx2\sqrt{t|\log\varepsilon|}.
\]

At `t=2`, `epsilon=1e-12`, this is approximately `14.87`, so `N` is of order `2.8e6`, not `e^10.6 approximately 4e4`. Density and `n^{-1/2}` factors require further treatment rather than improving that discrepancy automatically.

### The three-way box test is not complete

The proposed alternative

\[
\Theta>\varepsilon\quad\lor\quad
|\Theta_\xi|>\varepsilon'\quad\lor\quad
\Theta_{\xi\xi}>\varepsilon''
\]

is not a complete exclusion criterion for double contact. Real analyticity implies finite order for a nonzero analytic germ, but does not force a quadratic fold. A contact can have order four or higher, with

\[
\Theta=\Theta_\xi=\Theta_{\xi\xi}=0.
\]

Nor does the exclusion target `Theta=Theta_xi=0` rule out a local maximum. A nondegenerate-fold assumption is generic, not proved for this arithmetic family. A complete certifier must either use value--slope separation directly, prove nondegeneracy, or support adaptive higher-derivative multiplicity tests.

## Additional corrections

- The statement that the modulated Gaussian is outside Weil's criterion because a self-convolution must be even is false for the complex Hermitian autocorrelation used by the complete Weil form. If `v(x)` is a modulated Gaussian, `v*tilde(v)` carries the modulation phase. The separate `Q_W(v)=2Theta` interface is the correct formulation.
- `A=K_Gamma+K_pr` is not bounded as `|xi|` grows: the digamma block has logarithmic growth. Coercivity can still follow, but not from the boundedness statement used in the E3 discussion.
- A finite first contact for each counterexample does not supply one uniform upper bound on its parameter. Protocol P1 certifies only a declared compact interval and cannot promote that interval to RH.
- Numerical agreement with finitely many known critical-line zeros validates conventions on those samples; it does not authorize a positive zero-side measure globally.

## Disposition

Do not implement Protocol P1 as stated. Retain the corrected contact identity, on-axis complete monotonicity, density obstruction, negative controls, and certificate packaging. Repair requires:

1. replacing E* by a correctly directed uniform tail theorem;
2. replacing the three-way fold test by direct value--slope exclusion or a proved multiplicity-complete alternative;
3. preserving the unbounded-parameter residual explicitly rather than treating compact certification as a global route.

# Translation covariance makes every theta-label shifted-history block unitarily equivalent

## Theta labels are logarithmic translations

The half-density chart at label \(n\) is

\[
(\mathcal M_nf)(u)
=
\sqrt n\,e^{u/2}f(ne^u).
\]

Let logarithmic translation act by

\[
(V_af)(u)=f(u+a).
\]

Then

\[
\mathcal M_n
=
V_{\log n}\mathcal M_1.
\]

Thus changing the theta label does not change the analytic fiber geometry. It
translates the logarithmic coordinate unitarily.

## History covariance

The completed causal history is translation convolution:

\[
(H_\Phi f)(u)
=
\int_0^\infty
\Phi(r)f(u+r)\,dr.
\]

Therefore

\[
H_\Phi V_a
=
V_aH_\Phi.
\]

The reciprocal shifted factors

\[
F_\pm
=
I\pm iH_\Phi
\]

also commute with every \(V_a\), and so do their positive squares

\[
D_\pm
=
\frac12F_\pm^*F_\pm.
\]

Hence

\[
D_\pm V_{\log n}
=
V_{\log n}D_\pm.
\]

## Exact label equivalence

On the label-\(n\) half-density fiber, define

\[
D_{n,\pm}
=
V_{\log n}D_{1,\pm}V_{\log n}^{-1}.
\]

Translation covariance gives the stronger equality

\[
D_{n,\pm}=D_{1,\pm}
\]

after the standard fiber identification.

In source coordinates,

\[
\mathcal M_n^{-1}
D_{n,\pm}
\mathcal M_n
=
\mathcal M_1^{-1}
D_{1,\pm}
\mathcal M_1.
\]

Thus the shifted-history metric is independent of the theta label.

## Resolvent covariance

Because the kernels and reduced supports are translation invariant,

\[
D_{n,\pm}^{\dagger}
=
V_{\log n}
D_{1,\pm}^{\dagger}
V_{\log n}^{-1}.
\]

For any Stieltjes disagreement vector \(d_p\),

\[
\left\langle
\mathcal M_nd_p,
D_{n,\pm}^{\dagger}
\mathcal M_nd_p
\right\rangle
=
\left\langle
\mathcal M_1d_p,
D_{1,\pm}^{\dagger}
\mathcal M_1d_p
\right\rangle.
\]

Since \(\mathcal M_1\) is unitary, this is exactly the master source
resolvent loading transported into the completed logarithmic chart.

No label comparison constant remains.

## Unit-fiber consequence

The canonical tensor-unit counit

\[
\varepsilon_1
=
\mathcal M_1^{-1}\operatorname{ev}_1
\]

selects a shifted-history block with exactly the same Green metric used by
every other theta label.

Therefore the first Adams edge can be formed on \(n=1\) without changing:

- the auxiliary gap;
- the Wronskian Schur loading;
- reciprocal orientation;
- primewise completion bounds.

The full theta-labelled observer is a family of unitary translates of this
same local Green cell.

## Completion

Translation covariance survives graph closure because:

- \(V_a\) preserves the rapid core;
- \(H_\Phi\) is bounded on the completed full-line carrier;
- the adjoint convolution is translation invariant;
- the shifted squares are closed positive forms;
- spectral calculus commutes with the translations.

Finite half-line or moving-window compressions may break literal translation
invariance. The theorem applies after transport to the completed full-line
history carrier, which is the declared target of the half-density comparison.

## Prime labels remain separate

The parameter \(n\) is a theta label, while \(p\) is a valuation label.
The equality above acts only in the analytic theta factor. It neither mixes
primes nor changes the Adams grade.

Consequently the tensor-unit evaluation commutes with prime idempotents and
cutoff restriction.

## What this closes

The remaining local condition from the tensor-unit packet was covariance of
the reciprocal shifted-history metric on the \(n=1\) fiber. Translation
convolution proves it exactly.

Combining prior results now gives:

1. exact base-plus-curvature constructor identity at every label;
2. canonical tensor-unit counit;
3. unitary Green-metric comparison;
4. reciprocal-odd Wronskian rank-one incidence;
5. prime-uniform Schur-loading margin;
6. trace-class completed return.

Thus the first enlarged Adams edge is locally source-authorized on the
faithful valuation-labelled carrier.

## Remaining global frontier

The next obstruction is no longer local construction of the first Adams edge.
It is assembly:

- compatibility of distinct prime cells under constructor sums;
- retention of wall and odd ports under scalar Euler pushforward;
- global five-margin coercivity;
- final spectral identification with the off-seam zero condition.

## Verdict

Theta labels act by unitary logarithmic translation, and the completed causal
history is translation invariant. Every shifted-history Green block is
therefore unitarily equivalent to the tensor-unit block.

This closes the last local metric-typing gate for the first Adams edge.

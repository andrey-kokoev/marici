# Expanded search finds a certified source-only bivariate contact-exclusion box

## Fresh result

The generic D1 enclosure described by the finite-double-contact sweep was not the latest repository state. Later work built a more stable correlated enclosure and certified the rectangle

\[
(t,\xi)\in[0.298,0.300]\times[4.5000,4.5050].
\]

Fresh replay under the vendored Arb backend gives

```text
status: passed
rectangle_margin_lower: 8.4484324965
```

from `check_dual_rectangle_manifest.py`.

The certification is source-only at verification time. It uses:

- the endpoint term;
- certified `acb.integral` digamma/polygamma coordinates;
- 117 exact prime-power terms through prefix 512;
- an all-integer majorant for the infinite von Mangoldt tail;
- a degree-ten correlated Taylor model in \(t\);
- a certified mean-value bound in \(\xi\);
- separately certified core, mixed, and far-tail remainders.

The zero side was used only during discovery of a separating witness. The frozen witness is subsequently checked entirely from source data.

## Why ordinary box arithmetic failed

Endpoint, gamma, and finite-prime terms are individually large and cancel to approximately \(10^{-10}\) in the relevant coordinates. Natural interval evaluation encloses each sector independently and inflates the residual to order one.

The successful method encloses the combined residual

\[
(A/C-R_{\le P},\,-A'/C-I_{1,\le P})
\]

by a joint Taylor model before taking its dual pairing. This preserves source cancellation. It is an important implementation constraint for any broader D1 functor: sectorwise interval hulls are too weak even when every individual hull is rigorous.

## Family correction

The shifted-spectral Gaussian

\[
\Theta(t,\xi)=\langle\mathcal W,e^{-t(u-\xi)^2}\rangle
\]

and the stationary translation kernel

\[
\mathcal K(t,a)=\langle\mathcal W,e^{-tu^2}\cos(au)\rangle
\]

are distinct real slices. They are related only through holomorphic imaginary-character continuation:

\[
\Theta(t,\xi)
=e^{-t\xi^2}\mathcal K(t,-2it\xi).
\]

Accordingly, \(\Theta\) satisfies

\[
4t^2\partial_t\Theta+\partial_{\xi\xi}\Theta+2t\Theta=0,
\]

not the ordinary heat equation in \((t,\xi)\). After the inverse-width change and normalization it can be represented as a heat convolution, but generic heat theory still does not exclude double contact.

The later exact two-Gaussian falsifier proves that Widder representation and Angenent zero-number monotonicity permit precisely such a first-contact event. Therefore the literature sweep's earlier suggestion that heat-equation verification would itself exclude contact is superseded.

## Exact claim boundary

The rectangle certificate excludes one arithmetic contact configuration on one small two-dimensional box. It does not prove \(\Theta>0\) there, universal Gaussian positivity, complete monotonicity, or rung-four Schwarz positivity.

Its significance is methodological and noncircular:

1. source-only correlated Arb enclosures are feasible;
2. prime-tail formulas and gamma-tail formulas are already executable;
3. a bivariate continuum claim, rather than sampled points, has been certified;
4. expansion should reuse the dual-witness atlas and correlated Taylor arithmetic, not restart with naive D1 boxes.

## Fresh verification

```text
PYTHONPATH="$PWD/research/benincasa/.tmp_flint" \
python research/grothendieck/checkers/check_dual_t_interval_manifest.py

PYTHONPATH="$PWD/research/benincasa/.tmp_flint" \
python research/grothendieck/checkers/check_dual_rectangle_manifest.py
```

Both manifests passed in the current mutable state.

## Durable sources

- `research/grothendieck/exact-prefix-positive-tail-contact-obstruction.md`
- `research/grothendieck/explicit-two-variable-weil-heat-source-formula.md`
- `research/grothendieck/shifted-gaussian-is-an-imaginary-character-pullback.md`
- `research/grothendieck/the-shifted-gaussian-source-kernel-is-not-the-heat-character-kernel.md`
- `research/grothendieck/widder-angenent-do-not-exclude-weil-double-contact.md`
- `research/grothendieck/results/dual-rectangle-manifest.json`

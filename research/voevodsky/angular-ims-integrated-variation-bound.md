# Integrated-variation improvement for the angular IMS window

## Question

Can the directed angular localization constant be reduced without trusting the numerical scout?

## Claim boundary

This packet improves the certificate by integrating each chain-rule term instead of multiplying a pointwise supremum by the full transition length. It remains an upper bound, not an exact norm.

## Integrated estimate

For \(\rho(t)=\sin(\pi s(t)/2)\),

\[
|\rho'''|
\le
\frac{\pi^3}{8}(s')^3
+
\frac{3\pi^2}{4}|s's''|
+
\frac\pi2|s'''|,
\]

because the septic smoothstep is monotone. Each integral is explicit:

\[
\int_0^1(s')^3dt
=140^3\operatorname{B}(10,10),
\]

\[
\int_0^1|s's''|dt
=\left(\frac{35}{16}\right)^2,
\]

since \(s'\) rises once to \(35/16\) and then falls to zero, and

\[
\int_0^1|s'''|dt=rac{336\sqrt5}{25}.
\]

Hence

\[
\lVert\rho'''\rVert_1\le B_{\rm var},
\]

with

\[
B_{\rm var}
=
\frac{\pi^3}{8}140^3\operatorname{B}(10,10)
+
\frac{3\pi^2}{4}\left(\frac{35}{16}\right)^2
+
\frac{168\sqrt5\,\pi}{25}.
\]

For two windows, two transitions, and normalized angular overlap \(h_\theta=\pi\),

\[
C_{\rm loc}^{\rm var}
\le \frac{2}{3\pi}B_{\rm var}.
\]

## Disposition

This replaces the prior directed value \(104.4254\) by a smaller rigorous constant. It still remains separate from the non-directed scout \(9.84825790\). If the improved value still forces an intractable cutoff, the next target is directed interval integration of \(|\rho'''|\), not enlargement of the low block.

## Verification

- `research/voevodsky/checkers/check_angular_ims_integrated_variation.py`
- `research/voevodsky/results/angular_ims_integrated_variation.json`

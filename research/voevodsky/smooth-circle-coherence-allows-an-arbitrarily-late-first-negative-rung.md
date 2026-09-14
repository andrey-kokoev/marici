# Smooth circle coherence allows an arbitrarily late first negative rung

For each \(n\geq3\), choose

\[
r_n=-\frac12\left(\frac1{n-2}+\frac1{n-1}\right)
\]

and define the smooth even circle density

\[
w_n(\theta)
=
1+2r_n\sum_{m=1}^{n-1}\cos(m\theta).
\]

Its Fourier moments through order \(n-1\) are

\[
k_0=1,
\qquad
k_m=r_n.
\]

The resulting Toeplitz packet is the equicorrelation matrix. Every rank below \(n\) is positive definite because

\[
1+(n-2)r_n>0,
\]

while rank \(n\) fails because

\[
1+(n-1)r_n<0.
\]

Thus the first negative rung may occur arbitrarily late even when all of the following hold exactly:

- the observer is a smooth circle density;
- the moments are Hermitian Toeplitz;
- translation stationarity holds;
- reversal symmetry holds;
- every principal successor square commutes;
- every preceding rank is positive.

The density is signed, which is precisely the unresolved distinction. Smoothness and complete finite coherence do not force it into the positive-measure cone.

## Consequence

The coherence architecture correctly localizes RH at universal rung-four Schwarz positivity, but architecture alone cannot prove that positivity. Any proof must use quantitative information special to the endpoint–gamma–prime source values.

In particular, no combination of the following generic properties is sufficient:

\[
\text{Toeplitz}
+
\text{reversal}
+
\text{smoothness}
+
\text{restriction coherence}.
\]

The next noncircular target is therefore a genuinely arithmetic bound on the coupled centered functional

\[
L_E(q^*q)+L_\Gamma(q^*q)+L_P(q^*q),
\qquad L(q)=0.
\]

## Verification

```text
python research/voevodsky/checkers/check_smooth_circle_arbitrarily_late_negative_rungs.py
```

Artifacts:

- `research/voevodsky/checkers/check_smooth_circle_arbitrarily_late_negative_rungs.py`
- `research/voevodsky/results/smooth_circle_arbitrarily_late_negative_rungs.json`

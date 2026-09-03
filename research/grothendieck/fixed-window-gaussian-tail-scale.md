# Fixed-window Gaussian truncation has a narrow parameter scale

## Question

Can the claimed localized Weil margin at support half-width `L=0.8` control the discarded tail of every inverse shifted-Gaussian factor?

## Exact tail identity

For

\[
F_{t,\xi}(u)=e^{-\frac t2(u-\xi)^2}
\]

under the Fourier convention `exp(-2 pi i u x)`, the inverse transform has modulus

\[
|f_{t,\xi}(x)|
=\sqrt{\frac{2\pi}{t}}e^{-2\pi^2x^2/t}.
\]

Translation by `xi` contributes only a unit-modulus phase. Therefore the relative squared `L2` mass outside `[-L,L]` is exactly

\[
r_L(t)
=\frac{\int_{|x|>L}|f_{t,\xi}(x)|^2\,dx}
       {\int_{\mathbb R}|f_{t,\xi}(x)|^2\,dx}
=\operatorname{erfc}\!\left(\frac{2\pi L}{\sqrt t}\right),
\]

independently of `xi`.

## Comparison with the reported margin

Using `L=0.8` and the unverified reported localized margin

\[
m_{0.8}=8.9\times10^{-18},
\]

the equation `r_0.8(t)=m_0.8` gives

\[
t=0.6852540534182593\ldots.
\]

Sample exact tail fractions are:

| `t` | `r_0.8(t)` |
|---:|---:|
| 0.25 | `7.16e-46` |
| 0.50 | `8.90e-24` |
| 0.75 | `2.24e-16` |
| 1.00 | `1.17e-12` |
| 2.00 | `4.99e-7` |
| 4.00 | `3.79e-4` |

Thus the raw `L2` tail already exceeds the reported margin for `t>0.6853`. This is not a proof that the Weil-form error exceeds the margin: the required form-continuity constant and signed cancellation have not been bounded. It is a scale diagnostic showing that a fixed `L=0.8` comparison cannot be presumed uniform in `t`.

## Consequence

The compact-window route needs a theorem of the form

\[
|Q(f)-Q(f_L)|
\le C(t,L)\,\|f-f_L\|\,(\|f\|+\|f_L\|)
\]

in a norm on which the completed Weil form is continuous, followed by an explicit comparison with `m_L`. An ordinary unit-scale `L2` estimate would at best reach approximately `t<=0.6853` at `L=0.8`; larger `t` requires either a much sharper structured error estimate or verified positive margins for larger windows.

This also determines the quantifier structure: one fixed finite window does not control all Gaussian parameters. A global argument requires a source-derived family `L(t)` and verified margins `m_{L(t)}`, or a separate theorem reducing the unresolved parameter range.

## Verification

- Checker: `research/grothendieck/checkers/gaussian_window_tail_scale.py`
- Result: `research/grothendieck/results/gaussian-window-tail-scale.json`

The checker uses the exact complementary-error-function identity, verifies monotonicity in `t`, and deliberately rejects the exponent obtained by forgetting that `L2` mass squares the Gaussian modulus.

## Disposition

The `L=0.8` truncation proposal is retained only for a bounded small-`t` experiment. It is not a global double-contact exclusion method. The next required object is a Weil-form continuity estimate for compact truncation; the reported Zhu margin remains unusable until its absent certificate package is obtained or independently reconstructed.

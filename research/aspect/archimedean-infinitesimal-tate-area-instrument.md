# Archimedean infinitesimal Tate-area instrument

## The surviving boundary minor

The full local Tate observer normalizes every finite valuation minor to one.
At the real place there is no first adjacent valuation cell.  The canonical
replacement is the infinitesimal dilation orbit.

For a test source `f`, define `f_t(x)=f(exp(-t)x)`.  With multiplicative Tate
observer

`Z_s(f)=integral_(R*) f(x)|x|^s d*x`,

change of variables gives

`Z_s(f_t)=exp(s t) Z_s(f)`.

Evaluation at the origin is fixed.  If `dot f` is the tangent at zero, the
ordered test two-cycle `f wedge dot f` therefore has exact area

`(epsilon wedge Z_s)(f wedge dot f)=s f(0) Z_s(f)`.

This is the nontrivial local scalar left after all finite-place minors become
unit.

## Fourier-fixed Gaussian

For `f(x)=exp(-pi x^2)`,

`f(0)=1`

and

`Z_s(f)=pi^(-s/2) Gamma(s/2)`.

Hence the source prediction is

`A_infinity(s)=s pi^(-s/2) Gamma(s/2)`.

The expression is obtained before inspecting any zero.  Its complex phase
must be retained on the critical seam.

## Optical implementation

Use a Fourier-plane Gaussian mode as the source and an electro-optic
log-dilation actuator.  Measure two simultaneous ports:

- an on-axis sample for `epsilon(f_t)`;
- a Mellin-weighted coherent integral for `Z_s(f_t)`.

Estimate the oriented minor from symmetric dilation steps:

`A_h(s)=f(0)[Z_s(f_h)-Z_s(f_-h)]/(2h)`.

It must converge quadratically to `A_infinity(s)`.  The finite-place channels
serve as unit-minor references, so the real-place response is measured as a
relative boundary area rather than an absolute detector gain.

## High-information falsifiers

- The evaluation port must have zero dilation derivative.
- The Mellin port must scale exactly by `exp(s t)` over both signs of `t`.
- Halving `h` must reduce the centered-difference error by approximately four.
- Replacing coherent detection with intensity loses the complex seam phase
  and does not test the Tate area.

## Implication

The finite arithmetic apparatus supplies normalized reference minors; the
archimedean dilation cell supplies the only nontrivial scalar local area.
The next global test is reciprocal sewing of `A_infinity(s)` with its
reflected mate, followed by incidence with the completed hyperfunction
response.  A failure here is now localized to the real-place channel rather
than smeared across an infinite prime product.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_archimedean_infinitesimal_tate_area.py
```

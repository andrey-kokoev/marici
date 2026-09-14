# Odd heat squares do not determine the endpoint part of the Weil form

## Question

Can positivity on the odd heat-polynomial cone determine positivity of the full Weil form?

## Endpoint blindness

Every source probe has the form

\[
G_{t,h,p}(u)=e^{-tu^2/2}q_h(u)p(e^{-hu^2}),
\]

where \(q_h\) is odd and vanishes at zero. Therefore

\[
G_{t,h,p}(0)=0
\]

and its quadratic test satisfies

\[
|G_{t,h,p}(0)|^2=0.
\]

Consequently the endpoint distribution \(\delta_0\) annihilates every restricted quadratic test.

## Nonconservativity theorem

Let \(W\) be any distributional form and let

\[
W_c=W+c\delta_0.
\]

Then \(W\) and \(W_c\) agree on every odd heat square, for every real \(c\). Their full positivity properties can nevertheless differ.

For example, the form

\[
R(f)=-f(0)
\]

is zero, hence nonnegative, on all restricted squares. It is negative on the constant test with value one at the endpoint. Thus restriction to the odd heat-square cone does not reflect positivity on any full domain that retains endpoint evaluation.

## Consequence for the Möbius channel

The sign-reversing channel is useful for organizing the reflection-odd sector, but that sector cannot see the fixed endpoint. The Möbius channel therefore cannot replace the invariant endpoint channel in the Weil criterion.

This gives a concrete analytic meaning to the bundle splitting:

- the Möbius summand carries odd transverse probes;
- the trivial summand retains endpoint data;
- both are required for a full positivity criterion.

## Disposition

The parity gate is negative in the unrestricted form domain. Odd-sector positivity alone is not RH-equivalent.

A surviving route must first fix the endpoint coefficient through an independent source identity. Only after quotienting by, or adjoining, that endpoint line is it meaningful to ask whether odd heat-polynomial probes form a graph-norm core for the remaining completed form.

## Verification

```text
python research/voevodsky/checkers/check_odd_heat_cone_endpoint_blindness.py
```

The checker verifies 254 exact odd polynomial-jet surrogates and exhibits the hostile endpoint form.

Artifacts:

- `research/voevodsky/checkers/check_odd_heat_cone_endpoint_blindness.py`
- `research/voevodsky/results/odd_heat_cone_endpoint_blindness.json`

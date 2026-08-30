# Dual--dual covariance selector gate

## Missing pairing

The completed seam conormal lives in the continuous dual. To recover its
three pure quadratic controls, source theory must provide a smoothing
covariance

`G:E'->E`.

Then two seam covectors pair through

`B_G(lambda,mu)=<lambda,G mu>`.

This avoids a Riesz identification because `G` is an explicit typed map from
dual to test state.

## What Fourier symmetry selects

In the minimal two-port model, write a general symmetric covariance as

`G=[[a,b],[b,c]]`.

Invariance under the Fourier quarter-turn forces

`a=c` and `b=0`.

Therefore every positive invariant covariance is

`G=scale I`, with `scale>0`.

Fourier symmetry removes anisotropy and mixed covariance, but it does not fix
the remaining scale.

## Gaussian rigging interpretation

Grothendieck's Fourier-stable Gaussian rigging supplies plausible smoothing
operators from dual to test space, such as Fourier-commuting oscillator heat
kernels. They form a positive family. A heat time or vacuum normalization is
still required to select one member.

The theta Gaussian may provide that normalization, but it must be derived in
the combined adelic rigging. Choosing the scale after observing seam data
would be metric fitting.

## Consequence for 3+4+3

The completed tower now has an exact conditional form:

- bulk `3`: derived;
- mixed `4`: derived from state--dual evaluation;
- seam `3`: derived once a normalized continuous covariance `G` is supplied.

Thus `sp4` is one scalar selector and one continuity theorem away, not an
unstructured missing block.

## Apparatus extension

Implement the candidate smoothing covariance between the two conormal
functionals and tomograph its symmetric two-by-two response. The off-diagonal
entry must vanish and the two diagonal entries must agree. The apparatus may
measure the common scale only after source theory predicts it; otherwise the
honest result is an unselected positive one-parameter family.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_dual_dual_covariance_selector_gate.py
```

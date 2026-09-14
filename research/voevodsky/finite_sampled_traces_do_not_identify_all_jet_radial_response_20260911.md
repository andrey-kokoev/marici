# Finite sampled traces do not identify the all-jet radial response

## Question

Can the coherent 26-coordinate synthetic chain be identified with the current radial interface's all-jet, function-valued trace and response objects?

## Claim boundary

No, not without a source-derived finite-determination theorem. This packet proves noninjectivity of the twelve-point sampling map on an unrestricted function or all-jet carrier. It does not refute the finite synthetic chain, and it does not show that the source trace carrier contains every polynomial.

## Exact obstruction

The synthetic trace family samples bulk functions at

\[
r_j=\frac{j+1/2}{12},\qquad j=0,\ldots,11.
\]

Consider

\[
p(r)=\prod_{j=0}^{11}(r-r_j).
\]

This is a nonzero degree-twelve polynomial satisfying \(p(r_j)=0\) for every retained sample. Hence zero and \(p\) have identical twelve-point records although they are different functions. Their jet records differ because

\[
p'(r_j)=\prod_{k\ne j}(r_j-r_k)\ne0.
\]

Therefore evaluation at the twelve nodes is not faithful on any source carrier containing this polynomial and zero. Applying the argument independently to the real and imaginary bulk ports leaves the Wilson pair unchanged, so the 26-coordinate record map cannot identify an unrestricted four-port all-jet object.

## What would make sampling faithful

One of the following additional arrows is required:

- a declaration that each bulk trace lies in a polynomial space of degree at most eleven, with interpolation as inverse;
- a source-derived finite-dimensional basis and an invertible evaluation matrix;
- a bandlimit and a sampling theorem with its topology and reconstruction map;
- a jointly conservative derivative family extending point values;
- retention of the full function-valued trace rather than promotion of finite samples.

These are different assumptions. Finite computation alone supplies none of them.

## Consequence for the chain

The synthetic chain is coherent on its declared retained-lattice carrier. Its comparison with Aspect's interface stops at the phrase `all_jet_laplace_readout`: neither the v3 contract nor the synthetic packet declares a finite-determination theorem connecting all jets to twelve samples.

The exact reopening acceptance test is a typed reconstruction map from the twelve samples to the declared source trace carrier, together with a proof that sampling followed by reconstruction is the identity on that carrier. Without it, the comparison is a lossy projection and downstream agreement remains synthetic only.

## Disposition

The finite synthetic RH chain survives on its own carrier. Identification with the source all-jet radial response is rejected at the finite-sampling interface unless a reconstruction theorem or finite source model is supplied.

# Function-valued Clark faithfulness supersedes finite spectral rank probes

## Disposition

The finite spectral matrix probe is not the analytical receiver. It sampled a small number of spectral points and therefore produced rank 12 for the three-prime packet. That result is discarded as a discretization diagnostic, not treated as an analytical failure.

The intended Clark feature is function-valued:

    L(v)(z,t)=h_v(z) exp(i z t)

in the function space over an open upper-half-plane spectral region and the positive half-line in t. The source map first sends a chamber vector v to the actual shell forcing

    f_v(x)=sum_i v_i 1_(I_i)(x) Phi(x).

For compactly supported shell forcing, each tail trace h_v(z) is entire in z. If L(v) vanishes on the open spectral region, the zeroth trace vanishes there and hence everywhere by analytic continuation. Fourier uniqueness then gives f_v=0, and disjoint nonzero shell densities give v=0. Thus the analytical feature map is injective on the finite chamber source by the established theorem.

## Exact finite source checks

The typed source receiver independently verifies:

- full three-prime joint marked rank 48;
- terminal rank 26;
- first and second single-cut ranks 36 each;
- stacked marginal rank 46;
- exact two-dimensional marginal ghost space;
- full-cut left inverse;
- marked coproduct and coassociativity;
- 8,144 cut-tree roundtrips and 96,848 regrouping comparisons.

The completed first-theta-atom correlation injectivity checker passes all 12 symbolic checks. These exact results support the function-valued theorem; they do not license replacing it by a finite sampled spectral matrix.

## Source evaluator status

`research/voevodsky/clark_feature_evaluator.py` now contains:

- canonical port order `(+,0),(-,0),(+,1),(-,1)`;
- normalized Clark matrix compatibility;
- the explicit atom `Phi_n`;
- finite completed source `phi_completed`;
- exact incomplete-gamma pair-shell density for the atoms;
- exact arithmetic route-window construction via `event_intervals`.

The numerical evaluator remains a regression adapter. It is not a proof of function-space injectivity or of the completed infinite theta sum without a separate tail bound.

## Consequence for the derived seam lane

The 24- and 720-dimensional shifted relation layers should be transported through the function-valued Clark carrier, not tested by finite pointwise rank. Their source-side maps are already exact:

- conormal layer into the single-seam complex;
- product layer into the labelled joint two-seam complex;
- shifted connecting projection into the joint seam target.

The remaining analytical comparison is the signed Green pairing on that function-valued image, with all spectral indices retained pairwise. Aggregating the numerator before dividing by a single spectral denominator is invalid.

## Verification commands

    uv run --with sympy python research/voevodsky/checkers/check_completed_theta_correlation_injectivity.py
    uv run --with sympy python research/grothendieck/checkers/check_typed_cut_reconstruction.py
    uv run --with sympy python research/grothendieck/checkers/check_endpoint_decorated_history.py

All pass. The finite sampled rank-12 probe is retained only as a documented implementation warning.

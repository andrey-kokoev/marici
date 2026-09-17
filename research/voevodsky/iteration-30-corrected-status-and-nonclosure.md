# Iteration 30: corrected status and nonclosure

The current machine-readable audit is
`results/gate_closure_audit_v5.json`.  This note supersedes numerical claims
based on the stale `physical_regularized_residual_gram_*_refined_matrices.npz`
`lower_form` fields.  Eight of those nine fields did not satisfy their stated
formula; see `results/stale_complete_lower_artifacts_L0649_L065.json`.

## Corrected slab result

All 33 degree-32 Chebyshev source nodes on `[0.649,0.65]` have been evaluated.
The corrected complete lower forms are smooth and positive at the nodes.  For
the stored degree-16 polynomial, three directed low-branch intervals and a
cellwise min--max bulk estimate give

\[
 \lambda_{\min}(H_{\rm poly})\ge 1.9142621922585368\,10^{-11},
 \qquad
 \lambda_4(H_{\rm poly})\ge 1.6779707241264095\,10^{-4}.
\]

The degree-32 reconstruction differs from degree 16 by at most
`9.563428097303899e-14` on the dense scout grid, and the degree 17--32
coefficient norm sum is `1.23530375748735e-13`.  This is strong evidence but
not a source enclosure: no directed analytic bound for coefficients beyond
32 has been proved.  Gates 2 and 3 therefore remain open.

## L = 0.75 tail

The rank-1000 residual and boundary-jump tails through derivative order three
remain directed.  The complete finite boundary expansion through order 149
has now been evaluated at high precision on selected modes.  It exhibits
large nonmonotone intermediate cancellation and leaves oscillatory smooth
residual coefficients of order `1e-13`--`4e-12` near modes 1000--1200.  No
analytic norm bound for the infinite smooth residual tail has been proved.
Gate 7 remains open; `L=0.55` and the remaining finite thresholds are also
not certified.

## Decisive arithmetic obstruction

Gate 6 asks for a uniform unconditional signed weighted-Hankel discrepancy
bound above an explicit finite threshold.  The zero-free-region PNT estimate
is insufficient after the `n^{-1/2}` weighting.  Together with the finite
certificates and form-core passage, the requested bound would establish
global Weil positivity and hence RH under the standard Weil criterion.  No
such theorem is proved in this repository.  It cannot be supplied by
rounding promotion, additional quadrature, or finite computation.

## Disposition

None of Gates 2, 3, 6, or 7 is closed.  The local computations materially
narrow Gates 2, 3, and 7, but claiming the overall objective would be false;
in particular it would silently assume the RH-strength content of Gate 6.

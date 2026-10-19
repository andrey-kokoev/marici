# H7: native leakage of the corrected response128 state

## New source-bound test

The completed H6 cache supplies the actual corrected center state u, its 548-column internal embedding V, and the projected operator. Rebuilding the source raw internal H gives a direct test of whether the new response span is invariant.

Let G=V*V and Pi=V G^(-1) V*. The checker uses this orthogonal projection rather than replacing the stored Gram matrix by I. Define

    L=(I-Pi) H V.

The original 420 eigenmode columns have only small numerical leakage. The additional 128 response/Ritz columns have a nonzero native leakage block. The corrected prepared state also has nonzero L u. Thus a small **projected** Ritz identity V*HV approximately diag(e) does not make the added space invariant under H.

The old frozen-source residual construction projects only the geometric potential, diagonal contact and hinge-source terms. That was appropriate for its invariant native spectral subspace, but reusing it unchanged on the corrected non-invariant response basis would omit L u. The new checker evaluates both components in the same raw 12,250-dimensional internal coordinates and records their norms and combined norm.

Neither their sum nor either separate norm is claimed as the complete outgoing residual. The original radial square-root law and outgoing entrance boundary operator also depend on the internal operator: applying their scalar spectral functions to the compressed Ritz spectrum does not generally equal compressing the full raw functional calculus. Those missing actions must be reconstructed consistently. Native and other residual contributions may cancel; a nonzero native component is not by itself a counterexample to H7 or a lower bound on total response error.

## Energy convention made explicit

The packet interval [3.09,3.51] is **radial K**, not total operator energy. The source internal matrix excludes the common pose shift. For that convention the operator argument is E_op=e0+K; the displayed total energy is E_total=e0+K+CPOSE. The audited central state has K=3.30. The same common energy reference must be used on both retained and omitted blocks. H7 is written explicitly as A(K), meaning the full outgoing operator evaluated at E_op=e0+K, rather than leaving these two meanings of E conflated.

## Disposition

This is fresh partial progress on the **corrected** residual, not another replay of the old frozen source. H7 remains open. The next reconstruction must include the raw radial/boundary functional-calculus actions, a positive solver norm or controlled trace elimination, and a uniform invertibility certificate. H6's finite-response numerical result is unchanged: H7 asks about the larger raw model, whereas H6's outstanding errors concern its fixed response approximation.

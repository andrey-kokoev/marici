# The Positive-Mode Endpoint Dominance Is an Exact Rank-Two Gram Factorization

For a positive exponential packet, put

\[
K_z(0)=\sum_n\frac{c_n}{\alpha_n^2-z^2},
\qquad
w_n=\frac{c_n}{|\alpha_n^2-z^2|^2},
\qquad
z=a+it.
\]

If

\[
S_z=\sum_{m<n}w_mw_n(\alpha_m-\alpha_n)^2,
\]

then the endpoint amplitude and the pair-separation current obey the exact
identity

\[
|K_z(0)|^2-4t^2S_z
=
\left(\sum_nw_n(\alpha_n^2-|z|^2)\right)^2
+
\left(2t\sum_nw_n\alpha_n\right)^2.
\]

For `t != 0` and a nonzero positive packet, the second square is strictly
positive. Combined with the positive-mode Wronskian formula, the oriented
face difference is therefore

\[
\Delta_{\rm face}
=
2a\left(|K_z(0)|^2-4t^2S_z\right),
\]

and has exactly the sign of `a`. This is a complete coupled orientation
theorem on the positive exponential cone. Its application to RH remains
conditional on deriving the actual completed theta forcing in this cone, or
in a source-authorized closure that preserves the identity.

Research packet:
`research/grothendieck/the-positive-mode-endpoint-dominance-is-an-exact-rank-two-gram-factorization.md`

Checker:
`research/grothendieck/checkers/check_positive_mode_endpoint_rank_two_gram.py`

The checker passes 5/5 gates.

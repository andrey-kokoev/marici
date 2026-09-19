# The adjoint incidence extends to the endpoint-split jet graph, but the forward jet incidence is new data

Let `B_Sigma:U_ar->L2(R_x)` be the established Hilbert--Schmidt incidence and
`B_Sigma^dagger:L2(R_x)->U_ar` its bounded return.  For `0<r<pi`, apply the
return pointwise to the endpoint-split holomorphic history:

\[
(\widetilde B_\Sigma^\dagger F)(t)=B_\Sigma^\dagger(F(t)).
\]

For every compact subdisc `|t|<=r'<r`,

\[
\sup_{|t|\le r'}\|\widetilde B_\Sigma^\dagger F(t)\|_{U}
\le
\|B_\Sigma^\dagger\|
\sup_{|t|\le r'}\|F(t)\|_{L^2}.
\]

The same estimate applies to the `x` graph components whenever the return is
used after the history inclusion.  Hence the adjoint incidence extends
continuously

\[
\mathcal O_0(D_r;L^2(\mathbb R))
\longrightarrow
\mathcal O_0(D_r;U_{\rm ar}),
\]

with a bound independent of the disc radius.  Derivative evaluation at zero is
also continuous on each strict subdisc by Cauchy's estimate, so the forced
endpoint-return term remains typed before taking `r -> pi`.

There is no analogous automatic extension of the forward incidence.  The old
map

\[
B_\Sigma:U_{\rm ar}\to L^2(\mathbb R)
\]

has no canonical codomain in `O_0(D_r;L2)`: the constant lift does not vanish
at `t=0`, while choices such as `t B_Sigma x` add an unsupported jet profile.
A valid forward lift must provide source-derived holomorphic columns

\[
b_p(t)\in\mathcal O_0(D_r;L^2(\mathbb R))
\]

whose first jet recovers the declared incidence and whose higher jets obey the
theta forcing connection and cutoff bonding laws.

Therefore the return half of the completed Schur graph is continuous, but the
forward half is genuinely new constructor data.  Boundedness of the old
incidence alone cannot choose it.

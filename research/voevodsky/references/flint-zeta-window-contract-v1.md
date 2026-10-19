# Freshly inspected FLINT zero/count contracts

URL: https://flintlib.org/doc/acb_dirichlet.html

HTML response SHA-256: `2b6ee81653fa0197cb5d07a06fda9ebae718e82185a41731bc60e25ad38f9f35`.
Inspected directly during iteration5. Installed python-flint is0.9.0, FLINT3.6.0.

The documentation for `acb_dirichlet_zeta_nzeros` states:

> Compute the number of zeros (counted according to their multiplicities)
> of ζ(s) in the region 0 < Im(s) <= t.

The documentation for `acb_dirichlet_zeta_zeros` states:

> Sets the entries of res to len consecutive nontrivial zeros of ζ(s)
> beginning with the n-th zero. Requires positive n.

The counting/isolation section describes Turing's method and defines N(T)
using all zeros with positive imaginary part, counted with multiplicity.
It is not a count of an assumed critical-line-only scout.

Iteration5 does not rely on a zero evaluation merely containing zero as an
existence certificate. It proposes21 locations using `acb.zeta_zeros`, then
rigorously brackets21 critical-line roots by opposite signs of the real
completed xi function, in disjoint intervals. The certified total count N(80)
is21, also constant across a neighborhood of80. Together these certify the
complete window and multiplicities. Only this finite window is verified on
the critical line; the infinite tail admits every beta in [0,1].

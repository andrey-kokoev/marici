# Arbitrary-n,k one-loop BCFW term count and parity

The sourced one-loop recursion states that the number of nonvanishing contributions to the planar one-loop integrand is

$$
N_{n,k}^{(1)}
=
\binom{n-2}{k}
\binom{n-2}{k-2},
$$

in the convention where MHV has `k=2`.

The source derives this after choosing the forward-limit recursion that singles out `(AB)`: precisely the inverse-soft configurations involving `A` or `B` vanish, while all remaining contributions survive. The two binomial factors count the two independent boundary-choice sets left by this exclusion.

## MHV specialization

At `k=2`,

$$
N_{n,2}^{(1)}
=
\binom{n-2}{2}\binom{n-2}{0}
=
\frac{(n-2)(n-3)}2,
$$

which is exactly the Kermit-cell count.

## Parity

Parity exchanges

$$
k\longleftrightarrow n-k.
$$

Using binomial symmetry,

$$
\binom{n-2}{n-k}
=
\binom{n-2}{k-2},
$$

and

$$
\binom{n-2}{n-k-2}
=
\binom{n-2}{k}.
$$

Therefore

$$
N_{n,n-k}^{(1)}=N_{n,k}^{(1)}.
$$

In particular, the MHV and anti-MHV sectors have the same number of one-loop BCFW terms.

## Evidence and boundary

`check_arbitrary_nk_one_loop_bcfw_term_count.py` verifies nonnegativity, parity symmetry, and both extremal-helicity specializations for all physical `k` through `n=50`, covering 1,128 `(n,k)` instances.

This is a counting theorem. It does not construct the individual `N^kMHV` terms, verify their Grassmann degree, or prove their spurious-pole cancellation.

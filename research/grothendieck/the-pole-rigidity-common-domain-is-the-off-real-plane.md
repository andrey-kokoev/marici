# The pole-rigidity common domain is the off-real plane

## Question

Can the remaining analytic-continuation obligation in the generic-mesh proof be stated on one explicit common domain?

## Completed residual measure

Assume all-rank remainder Hankel positivity and use endpoint asymptotics to subtract the forced atom. The completed localizer moments are

\[
\ell_n=H(t+nh)-H(t+(n+1)h).
\]

The unconditional general-zero estimate gives a positive spectral decay rate

\[
\operatorname{Re}\lambda_\rho\ge\delta>0.
\]

Together with the zero count, this yields

\[
|\ell_n|=O(e^{-nh\delta}).
\]

Hence the unique positive representing measure `nu_(t,h)` has support in

\[
[-q_h,q_h],
\qquad q_h=e^{-h\delta}<1.
\]

Its moment transform

\[
S_{t,h}(z)=\int\frac{d\nu_{t,h}(y)}{1-zy}
\]

is holomorphic on the complex plane minus the two real rays where `1/z` meets the support. In particular, it is holomorphic at every nonreal finite point.

## Zero-side continuation

The general-zero expansion gives

\[
Z_{t,h}(z)
=
\sum_\rho
\frac{e^{-t\lambda_\rho}(1-e^{-h\lambda_\rho})}
{1-ze^{-h\lambda_\rho}}.
\]

Because `Re(lambda_rho)` grows quadratically with the ordinate and `N(T)=O(T log T)`, this series converges normally on compact sets avoiding its pole set. Its poles

\[
z_\rho=e^{h\lambda_\rho}
\]

have no finite accumulation point.

Both `S` and `Z` equal the ordinary moment power series in a neighborhood of zero. The identity theorem therefore continues their equality along every path in the intersection of their domains containing zero.

## Nonreal-pole contradiction

Choose a generic mesh so distinct `lambda` values do not alias. Repeated zeros only multiply the nonzero residue

\[
e^{-t\lambda}(1-e^{-h\lambda}).
\]

If some `lambda` is nonreal, `z=e^(h lambda)` is a nonreal pole of `Z`. The positive-measure transform `S` is holomorphic there. Since isolated zero-side poles can be approached through the common off-real domain, the continued equality is impossible.

Thus every `lambda_rho` is real, and the critical-strip formula forces RH.

## What remains to cite

The proof now needs only source citations for:

1. the exact general-complex-zero Gaussian expansion;
2. a uniform positive lower bound `delta` from the low-ordinate zero-free region;
3. the standard zero count;
4. locally uniform interchange producing `Z` near zero.

No unspecified common continuation domain remains.

## Boundary

The exact location of the real cuts depends on the proved support bound and can be enlarged harmlessly to the full real axis. Multiplicity grouping and generic-mesh selection must be stated before pole comparison.

## Disposition

Use the connected off-real plane, with a small disk around zero attached across the real complement of the support, as the pole-rigidity continuation domain. This closes the analytic shape of the sampled-cone implication, pending classical source citations.
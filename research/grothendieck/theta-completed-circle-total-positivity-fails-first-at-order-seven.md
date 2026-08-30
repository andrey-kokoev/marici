# Completed-circle total positivity fails first at order seven

## Question

Does the completed circle kernel remain sign-regular at every order, as
suggested by the exact order-two and order-three theorems?

## General Wronskian residual

For

\[
 f_\lambda(t)=(2\lambda t-3)e^{-\lambda t},
\]

the derivative formula of packet 109 makes the order-`r` Wronskian an
exponential, a Vandermonde, and the symmetric multi-affine residual

\[
 \boxed{
 P_r(y_1,\ldots,y_r)
 =\sum_{j=0}^r
 (-1)^{r-j}2^j(2r-2j+1)!!\,e_j(y_1,\ldots,y_r),}
\]

where `y_i=lambda_i t` and `e_j` is the elementary symmetric polynomial.

The formula follows directly from determinant multilinearity.  In row `k`,
one chooses either degree `k` or degree `k+1`.  Any nonsuffix pattern repeats
a degree and has zero determinant, so only the `r+1` suffix choices survive.

## Inductive derivative identity

The coefficients satisfy

\[
 \boxed{
 \partial_{y_i}P_r
 =2P_{r-1}(y_1,\ldots,\widehat y_i,\ldots,y_r).}
\]

At the rational boundary `y_i=3`, the first values are

\[
 P_r(3,\ldots,3)
 =3,15,57,369,891,15903
\]

for `r=1,...,6`.  Induction using the derivative identity therefore proves

\[
 P_r>0\quad\text{on }[3,\infty)^r,
 \qquad 1\le r\le6.
\]

Since the physical domain has `y_i>=pi>3`, the completed spectral kernel is
strictly sign-regular through order six.

## Exact order-seven failure

On the diagonal, the seventh residual is

\[
\begin{aligned}
 q_7(y)=P_7(y,\ldots,y)
 ={}&128y^7-1344y^6+10080y^5-58800y^4\\
 &+264600y^3-873180y^2+1891890y-2027025.
\end{aligned}
\]

Exact rational evaluation gives

\[
 q_7(22/7)
 =-\frac{37328273323}{823543}<0,
\]

whereas

\[
 q_7(7/2)=66304>0.
\]

Because `P_6>0` on the domain, the derivative identity makes `q_7` strictly
increasing there.  Using the classical rational bound `pi<22/7`, we obtain

\[
 q_7(\pi)<q_7(22/7)<0.
\]

Hence there is a unique diagonal crossing in

\[
 \boxed{22/7<y_*<7/2.}
\]

Continuity supplies ordered, pairwise-distinct spectral tuples arbitrarily
near the diagonal on both sides.  The oriented seventh Wronskian therefore
changes sign within the completed physical chart.

## Disposition

The all-orders total-positivity conjecture is false, and its first possible
failure is exactly order seven:

\[
 \boxed{
 \text{strict sign regularity holds through order six and fails at order
 seven}.}
\]

This is a structural falsifier, not a numerical counterexample.  The
constants, residual polynomial, and crossing bracket are exact.

The result explains why low-order positivity can look exceptionally rigid
while never extending to an RH proof.  The completion polynomial creates a
single higher-order orientation transition just above the self-dual spectral
boundary.

## New live direction

Ordinary total positivity is closed.  The surviving possibility is a
**completed signed circuit**: the order-seven reversal may be repaired by the
zero-mode endpoint channel or by the reciprocal chart, exactly as the
rank-one circle seam repairs the local commutator.

The next test must therefore include the endpoint mode and reciprocal sewing
before forming the seventh determinant.  If the augmented determinant still
changes sign, the variation-diminishing programme is falsified in its
completed form.  If the endpoint contributes a source-fixed rank-one repair
with the required sign, order seven is the first place where completion is
genuinely more than positivity of the outer-chart kernel.

## Verification boundary

Exact symbolic factorization was used to expose the residual formula.  The
proof of its sign and failure uses determinant multilinearity, induction, and
rational evaluations only.  No finite floating-point census is evidence for
the claim.

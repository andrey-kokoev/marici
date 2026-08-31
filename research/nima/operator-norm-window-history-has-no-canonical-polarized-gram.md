# Operator-norm window history has no canonical polarized Gram

## Qualification of the scale comparison

The source window history

\[
t\longmapsto M_{W_t}
\]

is bounded in the operator norm, and its graph-size estimate has the same
\(\sqrt{L}\) order as the resolved vector \(W_L\).  That proves a two-sided
comparison of **sizes** on each one-dimensional labelled fiber.

It does not produce the two-column source Gram required for the first-Adams
quadratic comparison.

## Operator norm is not Hilbertian

The multiplier carrier

\[
\mathcal B(L^2(\mathbb R))
\]

with norm

\[
\|M_f\|_{\mathrm{op}}=\|f\|_\infty
\]

is a Banach space, not a Hilbert space.  Its norm does not satisfy the
parallelogram identity in general, so it has no canonical polarization

\[
\langle M_f,M_g\rangle_{\mathrm{op}}.
\]

Consequently the graph-size expression

\[
\int_L^{2L}
\left(
\|M_{W_t}\|_{\mathrm{op}}^2+
\|M_{\partial_tW_t}\|_{\mathrm{op}}^2
\right)dt
\]

cannot be polarized to recover a mixed source entry for
\((W_L,W_{2L})\).

## Hilbert--Schmidt repair is unavailable

On a nonatomic infinite-measure \(L^2\) space, a nonzero multiplication
operator is not Hilbert--Schmidt.  In particular,

\[
M_{W_t}\notin\mathcal S_2
\]

for \(t>0\).  Therefore the formal trace pairing

\[
\operatorname{Tr}(M_{W_a}^*M_{W_b})
\]

is not available.  Replacing operator norm by Hilbert--Schmidt norm would not
repair the source carrier.

## State-dependent Hilbertization

A Hilbert pairing can be obtained only after choosing additional source data,
for example a vector or density operator:

\[
\langle M_f,M_g\rangle_\psi
:=\langle M_f\psi,M_g\psi\rangle_{L^2},
\]

or

\[
\langle M_f,M_g\rangle_\varrho
:=\operatorname{Tr}(\varrho M_f^*M_g).
\]

For the first choice,

\[
\langle M_f,M_g\rangle_\psi
=\int\overline{f(q)}g(q)|\psi(q)|^2\,dq.
\]

To recover the ordinary resolved window pairing

\[
\int\overline{f(q)}g(q)\,dq,
\]

one would need \(|\psi(q)|^2=1\) almost everywhere.  The constant vector is
not in \(L^2(\mathbb R)\).  No normalized vector state gives the unweighted
Lebesgue pairing on the full line.

A trace-class density likewise gives a weighted diagonal measure, not
canonically Lebesgue measure, unless a separate semifinite trace or rigged
weight is declared.

## Exact missing datum

The two-column comparison therefore requires a source-authorized
semifinite/relative pairing on multiplier-valued endpoints whose restriction
to the source-generated window algebra is

\[
\tau(M_f^*M_g)=\int\overline f g.
\]

Such a weight is natural on a commutative multiplication algebra, but it is
not a bounded state and is not defined on all of
\(\mathcal B(L^2)\).  Its domain, closability, and compatibility with the
history derivative and wall ports must be proved.

## Revised frontier

The logarithmic norm scale is matched, but the polarized metric is not.  The
earliest local theorem is:

> Construct the source-authorized semifinite relative weight on the endpoint
> multiplier algebra, prove that the window and derivative-history products
> lie in its finite domain, and show that its polarization equals the selected
> resolved window Green form.

Only then is a two-by-two source Gram available for comparison with the
explicit resolved matrix.  Ordered linking continuity and radical descent
remain downstream.  No RH conclusion is authorized.

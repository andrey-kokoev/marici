# Bounded Exactness Protocol for the Five-Site Weight-Five Block

Fix the external parameter \(t\) and let \(D\) be the product of the 25
fiber-dependent marked norm divisors: five edge norms and twenty proper-section
norms. The total-energy norm is parameter-only and may be restored as an
overall scalar. Put

\[
B=\prod_{i=1}^5R_i,
\qquad
A_j=\frac12\partial_j\log B.
\]

For a degree bound \(d\), test primitives of the form

\[
\eta=
\frac{p_1}{D}\,du_2\wedge du_3
-\frac{p_2}{D}\,du_1\wedge du_3
+\frac{p_3}{D}\,du_1\wedge du_2,
\qquad
\deg p_j\le d.
\]

Writing the correctly projected rational trace as

\[
f_{12345}\,du_1\wedge du_2\wedge du_3,
\]

the equation \(\nabla_{12345}\eta=f_{12345}\,du_1\wedge du_2\wedge du_3\)
is the linear identity

\[
\boxed{
f_{12345}
=\frac1D\sum_{j=1}^3
\left(
\partial_jp_j
-p_j\partial_j\log D
+A_jp_j
\right).
}
\]

For each monomial \(m\) and component \(j\), the sampled matrix column is

\[
\frac1D
\left(
\partial_jm-m\partial_j\log D+A_jm
\right).
\]

Everything in this column is available without expanding the saturated
denominator:

- \(f_{12345}\) comes from the 32-sheet rational Walsh oracle;
- \(D\) and \(\partial_j\log D\) come from the 25 explicit orbit norms;
- \(A_j\) comes from the five quadratic radicands.

## Certification ladder

For each \(d\):

1. build the matrix at more generic samples than unknown coefficients;
2. compare coefficient rank with augmented rank over two independent primes;
3. reject every sample meeting any of the 31 logarithmic supports;
4. verify a witness, if found, on held-out primes and points;
5. call a failure only a degree-\(d\), common-simple-denominator exclusion.

A failed bounded solve is not a non-exactness theorem: primitives of higher
degree, different pole filtration, or Čech-supported form remain possible.
A successful solve is likewise only a candidate until exact rational
substitution or sufficiently strong modular reconstruction is supplied.

The first ladder should use \(d=0,1,2,3\), with respectively

\[
3,12,30,60
\]

unknown coefficients.

## First replicated outcome

The sampled ladder was run over \(\mathbf F_{1009}\) and
\(\mathbf F_{1013}\). The coefficient and augmented ranks agree across the
two primes:

\[
\begin{array}{c|c|c|c}
d&\text{unknowns}&\operatorname{rank}M&\operatorname{rank}[M\mid f]\\\hline
0&3&3&4\\
1&12&10&11\\
2&30&21&22\\
3&60&36&37
\end{array}
\]

Thus no common-simple-denominator primitive exists in the sampled polynomial
ansatz through degree three. The stable rank-one augmentation is suggestive,
but it is not called a cohomology dimension: higher degree, a different pole
filtration, and Čech-supported primitives remain outside the test.

Checker and result:

- `research/nima/check_five_site_weight_five_bounded_exactness.py`
- `research/nima/results/five-site-weight-five-bounded-exactness.json`

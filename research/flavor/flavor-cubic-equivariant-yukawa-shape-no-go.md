# Cubic One-Tensor Equivariance Cannot Select a Hierarchical Shape

Work package: WP926

## Question

Can the most general cubic biunitary-equivariant beta law for the surviving
WP925 tensor generate an isolated nondegenerate singular-value hierarchy?

## Complete cubic normal form

For one complex family tensor transforming as

\[
Y\longmapsto U_LYU_R^\dagger,
\]

the cubic covariants reduce to

\[
\beta_Y=A Y+BYY^\dagger Y.
\]

The scalar (A) may contain gauge couplings, scalar couplings, and trace terms
such as (\operatorname{tr}(Y^\dagger Y)). Those contributions multiply every
singular direction equally. The coefficient (B) is left arbitrary; the
theorem does not require its loop value.

Let (s_i>0) be singular values and (x_i=s_i^2). Then

\[
\frac{\dot s_i}{s_i}=A+Bx_i,
\]

so common terms cancel from ratio flow:

\[
\frac{d}{dt}\log\frac{s_i}{s_j}=B(x_i-x_j).
\]

## Exact dichotomy

If (B\ne0), simultaneous stationarity of two independent ratios forces

\[
x_1=x_2=x_3.
\]

The cubic spectral discriminant then vanishes. The only isolated nonzero shape
available to this normal form is degenerate and cannot support normalized
Jarlskog coordinates on the nondegenerate physical16 domain.

If (B=0), every ratio flow vanishes identically. All spectral shapes form a
marginal continuum, so stationarity supplies no selection.

No choice of (A) repairs either branch because (A) cancels exactly from
the ratio equations.

## Smallest hostile

At the hierarchical Gram spectrum

\[
(x_1,x_2,x_3)=(1,4,9)
\]

and (B=1), the independent ratio flows are

\[
-3,
\qquad
-5.
\]

Thus this ray is not stationary. Setting (B=0) makes it stationary only by
making every competing ray stationary as well.

## Verdict

The cubic one-tensor equivariant normal form is a dynamical obstruction, not a
hierarchical shape selector. Exchange-reflection does not alter the theorem;
it merely identifies the conjugate tensor copy.

The claim is bounded. It does not exclude coupled up/down tensors,
higher-loop or higher-dimensional covariants, nonpolynomial source geometry,
or source-derived boundary conditions. But at least one such additional
structure is necessary. Its coefficients and tensor contractions must be
derived independently of measured physical16 data.

The next bounded problem is the coupled two-tensor cubic covariant census and
its four-ratio fixed-ray equations. No detector gate opens before that source
dynamics and its thresholds exist.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp926_cubic_equivariant_yukawa_shape_no_go.py
~~~

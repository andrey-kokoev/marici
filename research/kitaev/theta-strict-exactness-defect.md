# The completion defect is a kernel invariant, not automatically a derived invariant

Owner: `marici.Kitaev`

## Bounded question

Does derived-completion or \(\varprojlim^1\) language provide an independently
computable obstruction to a distinguished source line becoming invisible, or
does it merely rename the completed detector kernel?

## Three distinct completion failures

Let \(D:E\to F\) be a bounded detector between normed source and target
spaces, with extension \(\widehat D:\widehat E\to\widehat F\).

The excess-kernel defect is

\[
\Delta_{ker}(D)
=
\ker\widehat D\big/\overline{\ker D}.
\]

It must be separated from:

- failure of \(\operatorname{ran}\widehat D\) to be closed;
- collapse of the lower-bound constant while \(\widehat D\) remains injective.

For example, the diagonal map \(e_n\mapsto n^{-1}e_n\) on \(\ell^2\) is
injective after completion but has nonclosed range and no positive lower bound.
It does not create an ordinary completed kernel. Its normalized basis vectors
become asymptotically invisible, and only an ultraproduct converts that escape
sequence into a literal kernel class.

This corrects any identification of asymptotic invisibility with a kernel in
ordinary Hilbert completion.

## Finite-stage limit witness

The matrix family

\[
D_N=\begin{pmatrix}1&0\\0&1/N\end{pmatrix}
\]

is invertible at every finite stage and converges in operator norm to

\[
D_\infty=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Thus a singular normalized limit can have a one-dimensional kernel although
all finite kernels vanish. The exact obstruction is the collapse of the least
singular value. Calling the resulting kernel a derived-completion defect does
not compute it before the limit.

## Strict exactness criterion

Completion preserves injectivity on the admitted source sector whenever

\[
\lVert Dv\rVert_F\ge c\lVert v\rVert_E
\]

for one \(c>0\). For a cutoff family at fixed spectral parameter \(s\), the
required statement is

\[
\inf_N c_N(s)>0.
\]

No uniformity in spectral height is asserted. The norms and bonding maps are
part of the source typing; changing them changes the claim.

## Frame invariance

For invertible source and target changes \(A_N,B_N\), set

\[
D'_N=B_ND_NA_N^{-1}.
\]

If \(A_N,A_N^{-1},B_N,B_N^{-1}\) are uniformly bounded, then lower-bound
collapse is invariant. More precisely,

\[
\sigma_{\min}(D'_N)
\ge
\frac{\sigma_{\min}(D_N)}
{\lVert B_N^{-1}\rVert\lVert A_N\rVert},
\]

and the reverse comparison follows by exchanging primed and unprimed frames.
If the frames converge to invertible limits, the dimension of the limiting
kernel is also invariant.

Unbounded rescaling can manufacture or hide collapse and is not an authorized
change of source trivialization.

## Derived-completion gate

A \(\varprojlim^1\) description requires a specified inverse system or a
source-derived resolution. Without such data there is no canonical derived
object. If one defines the object only after forming \(\widehat D\), its
degree-zero defect is exactly \(\Delta_{\ker}(D)\).

On a distinguished complex line, where the finite kernels vanish,

\[
\Delta_{\ker}(D)=\ker\widehat D.
\]

Determining whether this is zero is the completed scalar nonvanishing claim.
The derived notation supplies no independent constructor, estimate, or finite
falsifier.

Therefore a derived-completion route is explanatory only if theta/Tate source
geometry independently supplies:

1. the inverse system or resolution;
2. typed bonding maps;
3. a computable derived class before scalar completion; and
4. a theorem identifying its vanishing with strict exactness.

Those data are currently absent. The bare \(\varprojlim^1\) reformulation is
closed as a relabeling of scalar nonvanishing.

## Disposition

The independently useful invariant is the cutoff-uniform lower-bound profile
in frozen source graph norms. Ordinary completion kernel, asymptotic escape,
and ultraproduct kernel must not be conflated. Derived completion remains a
conditional organizational language, not a new RH-bearing observable.

## Claim strength

Exact finite-dimensional limit theorem and functional-analytic typing
correction. No theta/Tate strict-exactness theorem is claimed.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_strict_exactness_defect.py`.
The result is written to
`research/kitaev/results/theta-strict-exactness-defect.json`.


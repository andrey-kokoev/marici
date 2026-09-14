# The dyadic prolate defect tower resolves near-one eigenvalue gaps at scale two to the minus j

## Scalar defect filters

For

\[
0\le\lambda\le1,
\]

define

\[
\boxed{
w_j(\lambda)
=
\lambda^{2^j}
\left(
1-\lambda^{2^j}
\right).
}
\]

The `j`-th positive prolate defect feature has squared spectral weight `w_j(lambda)`.

The telescoping identity is

\[
\boxed{
\lambda
=
\lambda^{2^n}
+
\sum_{j=0}^{n-1}
w_j(\lambda).
}
\]

For `lambda<1`, letting `n->infinity` gives

\[
\lambda
=
\sum_{j\ge0}
w_j(\lambda),
\]

while `lambda=1` is retained by the eigenvalue-one projection.

## Location of one defect band

Set

\[
x=
\lambda^{2^j}.
\]

Then

\[
w_j=x(1-x),
\]

which is maximal at

\[
x=\frac12.
\]

Therefore the peak eigenvalue satisfies

\[
\boxed{
\lambda_j^*
=2^{-1/2^j}.
}
\]

Its gap from one is

\[
1-\lambda_j^*
=
1-
e^{-(\log2)/2^j}
=
\frac{
\log2
}{2^j}
+O(4^{-j}).
\]

Thus

\[
\boxed{
w_j
\text{ detects }1-\lambda
\asymp
2^{-j}.
}
\]

The tower is a canonical logarithmic resolution of near-one prolate gaps.

## Exponential variable

Write

\[
\lambda=e^{-\delta},
\qquad
\delta\ge0.
\]

Then

\[
\boxed{
w_j(e^{-\delta})
=
e^{-2^j\delta}
\left(
1-
e^{-2^j\delta}
\right).
}
\]

This depends only on the scaled gap variable

\[
2^j\delta.
\]

Hence each defect level is a fixed profile translated along logarithmic gap scale.

## Soft bulk cutoff

The concentrated remainder after `n` levels is

\[
\lambda^{2^n}
=
e^{-2^n\delta}.
\]

It has the following exact bounds:

- if `delta>=epsilon`,
  \[
  \lambda^{2^n}
  \le
  e^{-2^n\varepsilon};
  \]
- if `delta<=epsilon`,
  \[
  1-
  \lambda^{2^n}
  \le
  2^n\varepsilon.
  \]

The second follows from `1-e^(-x)<=x`.

Thus `B^(2^n)` is a soft spectral projection onto gaps

\[
\boxed{
1-\lambda
\lesssim
2^{-n}.
}
\]

No sharp spectral threshold is required.

## Operator bounds

Let

\[
E_B([0,1-\varepsilon])
\]

be the spectral projection onto eigenvalues at least `epsilon` away from one. Functional calculus gives

\[
\boxed{
\left\|
B^{2^n}
E_B([0,1-\varepsilon])
\right\|
\le
(1-\varepsilon)^{2^n}
\le
 e^{-2^n\varepsilon}.
}
\]

On the near-one band `E_B([1-epsilon,1])`,

\[
\boxed{
\left\|
(I-B^{2^n})
E_B([1-\varepsilon,1])
\right\|
\le
2^n\varepsilon.
}
\]

These estimates are uniform for every positive contraction; no prolate-specific theorem is used.

## Joint cutoff--depth rule

Suppose a prolate spectral theorem identifies a relevant near-one gap scale

\[
\varepsilon_\Lambda
\to0.
\]

To separate eigenvalues with gaps much larger than `epsilon_Lambda` from those much smaller, choose `n(Lambda)` satisfying

\[
\boxed{
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1.
}
\]

Equivalently,

\[
\boxed{
n(\Lambda)
=
\log_2
\frac1{\varepsilon_\Lambda}
+O(1).
}
\]

This is the exact relation between dyadic tower depth and the prolate near-one scale.

## Observer-weighted counting measure

For observer amplitude `A`, define the positive spectral measure

\[
\mu_{\Lambda,g}(E)
=
\operatorname{Tr}
\left(
A^*
E_{B_\Lambda}(E)
A
\right).
\]

Then the `j`-th defect norm is

\[
\boxed{
\|\Phi_{\Lambda,j}^{tr}(g)
\|_{HS}^2
=
\int_{[0,1]}
w_j(\lambda)
d\mu_{\Lambda,g}(\lambda).
}
\]

The concentrated remainder is

\[
\boxed{
\|B_\Lambda^{2^{n-1}}A\|_{HS}^2
=
\int
\lambda^{2^n}
d\mu_{\Lambda,g}(\lambda).
}
\]

Thus the joint asymptotic depends only on the observer-weighted distribution of eigenvalue gaps near one, not on the undefined bare angular trace.

## Required near-one input

A sufficient prolate theorem would describe the rescaled measures

\[
\boxed{
\nu_{\Lambda,g}
=
(\delta\mapsto
\delta/\varepsilon_\Lambda)_*
\mu_{\Lambda,g}
}
\]

near `delta=1-lambda` or `delta=-log lambda`.

If these measures converge after subtraction of the Plancherel bulk density, then every dyadic defect level has a limit by integration against the fixed profile

\[
e^{-x}(1-e^{-x}).
\]

This converts the positive boundary problem into convergence of one observer-weighted near-one spectral measure.

## Relation to Sonin sector

The exact eigenvalue-one mass is

\[
\mu_{\Lambda,g}(\{1\})
=
\|P_{\{1\}}(B_\Lambda)A\|_{HS}^2.
\]

It is not captured by any finite defect level because

\[
w_j(1)=0.
\]

Therefore the Sonin/intersection sector remains a separate harmonic atom at gap zero, while the dyadic tower resolves all positive gaps approaching it.

## Relation to sewing

Any boundary sewing map acting diagonally in prolate spectral variables can now be tested scale by scale. A bounded contraction on the defect tower must satisfy

\[
\sum_j
\|\mathcal C_j
\Phi_{\Lambda,j}^{tr}(g)
\|^2
\le
\sum_j
\|\Phi_{\Lambda,j}^{tr}(g)
\|^2.
\]

The relevant arithmetic information is how the Tate scattering phase acts on the rescaled gap measure and on the separate eigenvalue-one atom.

## Refinement interpretation

The dyadic index `j` is not another prime label or barycentric coordinate. It is the logarithmic scale of the prolate angle defect

\[
1-\lambda.
\]

Accordingly the positive refinement is naturally filtered or pro-simplicial. A finite ten-node model can retain a cutoff depth `n(Lambda)`, while the complete object is the compatible inverse/direct system over all `j`.

## Disposition

The positive defect tower has an exact spectral meaning:

\[
\boxed{
\Phi_{\Lambda,j}^{tr}
\text{ resolves gaps }
1-\lambda
\asymp2^{-j}.
}
\]

The joint depth must satisfy

\[
\boxed{
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1.
}
\]

The remaining analytic datum is the observer-weighted near-one gap scale `epsilon_Lambda` and the limiting rescaled spectral measure of `P_Lambda Q_Lambda P_Lambda`.

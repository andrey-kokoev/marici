# Generic-mesh pole comparison removes zero-side cancellation

## Question

Can quartet grouping, repeated zeros, or mesh aliasing invalidate the implication from remainder Hankel positivity to RH?

## Generating function

For fixed `t,h`, let `a_n` be the gamma-plus-prime remainder-localizer moments. After extracting the endpoint atom, their zero-side generating function is formally

\[
G_{t,h}(z)
=
\sum_\rho
\frac{e^{-t\lambda_\rho}(1-e^{-h\lambda_\rho})}
{1-ze^{-h\lambda_\rho}}.
\]

Gaussian decay in the zero ordinate gives normal convergence on compact sets avoiding the pole set. Thus `G_(t,h)` is meromorphic there.

## Multiplicity and functional-equation grouping

Zeros with the same `lambda_rho` add their multiplicities. Their coefficient is

\[
m_\lambda e^{-t\lambda}(1-e^{-h\lambda}),
\]

which is nonzero for positive sufficiently small `h` because `lambda` is nonzero. Hence repeated zeros do not cancel a pole.

The functional-equation partner `1-rho` has the same `lambda`. Complex conjugation contributes `conj(lambda)`, producing the conjugate pole rather than canceling the original one.

## Generic mesh

Distinct spectral parameters can alias at one mesh only when

\[
e^{-h\lambda}=e^{-h\lambda'},
\qquad
h(\lambda-\lambda')\in2\pi i\mathbb Z.
\]

For each pair this is a discrete set of positive meshes. The union over the countable zero set is countable. Since the cone is required for every positive `h`—and rational-mesh results extend by source continuity—one may choose a generic `h` outside this exceptional set. Every distinct `lambda` then gives a distinct pole with nonzero residue.

## Real-measure obstruction

All-rank remainder Hankel positivity plus endpoint asymptotics gives a compact positive representing measure. After endpoint subtraction, completed heat decay bounds its support inside `[-1,1]`. Its moment generating function is a Cauchy transform whose singular support lies on the real axis.

At a generic mesh, a zero with nonreal `lambda` creates an uncanceled pole at

\[
z=e^{h\lambda},
\]

which is nonreal. Equality by analytic continuation with the positive-measure transform is impossible. Therefore every `lambda_rho` is real. Because

\[
\operatorname{Im}\lambda_\rho=-2\gamma(\beta-1/2)
\]

and `gamma` is nonzero, every zero has `beta=1/2`.

## Remaining analytic obligations

A complete theorem must state one common continuation domain and justify equality of the moment transform and zero-side meromorphic continuation across paths avoiding real support. It must also cite the exact general-complex-zero heat expansion and its locally uniform convergence.

## Disposition

Multiplicity, quartet symmetry, and fixed-mesh aliasing are not structural escape routes. Generic mesh separates the poles, and positivity forbids every nonreal one. The remaining source challenge is exactly to prove the remainder Hankel cone.
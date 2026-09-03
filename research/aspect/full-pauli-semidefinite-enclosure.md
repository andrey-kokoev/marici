# Full Pauli semidefinite enclosure

## Question

Can all fifteen drift-uncertain path–polarization Pauli coordinates be enclosed with an exact certificate of positivity and a robust entanglement-witness bound?

## Claim boundary

This packet gives an exact rational enclosure around a full-rank Werner-type state. It certifies one fifteen-dimensional uncertainty box without a floating-point SDP solver. It is not a general-purpose semidefinite optimizer or a certificate for arbitrary experimental intervals.

## Pauli-coordinate state region

Write a trace-one Hermitian operator as

\[
\rho(r)=\frac14
\left(I+\sum_{k=1}^{15}r_kP_k\right),
\]

where \(P_k\) are the fifteen nonidentity two-qubit Pauli products. Efficiency intervals and click records produce intervals

\[
r_k\in[\underline r_k,\overline r_k].
\]

The rigorous feasible region is

\[
\mathcal R=
\left\{r:
\underline r_k\le r_k\le\overline r_k,
\quad \rho(r)\succeq0
\right\}.
\]

This is the intersection of a rational box with a spectrahedron.

## Certified full-dimensional box

Take the center

\[
\rho_0=(1-v)I/4+v\lvert\Phi^+\rangle\langle\Phi^+\rvert,
\qquad v=4/5.
\]

Its Pauli center has

\[
r_{XX}=4/5,
\qquad r_{YY}=-4/5,
\qquad r_{ZZ}=4/5,
\]

and the other twelve coordinates zero. The smallest eigenvalue is

\[
\lambda_{\min}(\rho_0)=\frac{1-v}{4}=rac1{20}.
\]

Give every one of the fifteen coordinates independent radius

\[
\delta=1/300.
\]

For any perturbation \(\Delta r\) in this box,

\[
\left\|ho(r)-\rho_0\right\|
\le\frac14\sum_{k=1}^{15}|\Delta r_k|
\le\frac{15\delta}{4}
=rac1{80}.
\]

Weyl's inequality therefore gives

\[
\lambda_{\min}(\rho(r))
\ge\frac1{20}-rac1{80}
=rac3{80}>0.
\]

Thus the entire fifteen-dimensional box lies strictly inside the positive cone. The semidefinite constraint is certified everywhere, not sampled.

## Witness extremum

The \(\Phi^+\) fidelity is

\[
F_{\Phi^+}(r)=
\frac{1+r_{XX}-r_{YY}+r_{ZZ}}4.
\]

Because the whole box is positive, its linear minimum occurs at the corresponding box corner. Hence

\[
F_{\Phi^+}\ge
\frac{1+3(4/5-1/300)}4
=rac{339}{400}.
\]

Since \(339/400>1/2\), every state in the full fifteen-coordinate enclosure is entangled. The twelve nuisance coordinates may vary independently; the result is not restricted to Bell-diagonal states.

## Failure gate

If the common radius is enlarged to \(1/50\), the same norm estimate becomes

\[
15/(4\cdot50)=3/40>1/20.
\]

The positivity certificate fails. This does not prove that every enlarged-box state is nonpositive; it proves that this enclosure argument cannot admit the larger box. Refinement would require tighter operator-norm bounds or an actual semidefinite extremization.

## General certificate form

For a center with certified spectral margin \(\gamma>0\) and coordinate radii \(\delta_k\), the sufficient positivity condition is

\[
\frac14\sum_k\delta_k<\gamma.
\]

For a linear witness \(W=w_0I+\sum_kw_kP_k\), interval evaluation gives a rigorous extremum over the box. When the entire box is positivity-certified, the box corner attaining that interval bound is itself a density operator, so the linear bound is exact over the enclosure.

## Exact diagnostic

A rational checker verifies all fifteen coordinate radii, the spectral margin \(3/80\), the exact fidelity minimum \(339/400\), the hostile-radius certificate failure, and nonzero width in every Pauli direction.

## Disposition

A full fifteen-dimensional drift enclosure can be certified semidefinite by combining an exact center spectral gap with a Pauli operator-norm perturbation bound. The resulting region is strictly positive and uniformly entangled. Arbitrary wider experimental boxes still require a rigorous SDP or sharper interval spectral method.

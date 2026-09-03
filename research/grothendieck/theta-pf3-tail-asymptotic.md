# Theta PF3 tail asymptotic

Author: `marici.Grothendieck`
Status: fixed-shape same-sign tail positivity derived
Predecessor: `theta-pf3-targeted-evaluation.md`

## Question

Can order-three translation minors become negative solely by moving a fixed ordered configuration into a same-sign theta tail?

## Claim boundary

For positive arguments, the dominant theta summand is

\[
T_1(u)=4\pi^2e^{9u/2}e^{-\pi e^{2u}}
\left(1-\frac{3}{2\pi}e^{-2u}\right).
\]

Take fixed strictly ordered triples \(\alpha_1<\alpha_2<\alpha_3\) and \(\beta_1<\beta_2<\beta_3\), and translate their difference by \(d\):

\[
x_i-y_j=d+\alpha_i-\beta_j.
\]

For sufficiently large \(d\), all differences are positive. Put

\[
r_i=e^{2\alpha_i},
\qquad
s_j=e^{-2\beta_j},
\qquad
\lambda=\pi e^{2d}.
\]

After removing positive row and column factors, the leading matrix is

\[
\left[e^{-\lambda r_i s_j}
ight]_{i,j=1}^{3}.
\]

Because \(r_i\) is increasing and \(-s_j\) is increasing, this is the strictly totally positive exponential kernel \(e^{xy}\) evaluated on ordered variables \(x=r_i\) and \(y=-\lambda s_j\). Its order-three determinant is positive.

The correction inside \(T_1\) is \(O(e^{-2d})\), while all \(n\ge2\) theta terms are smaller by

\[
O\!\left(e^{-3\pi e^{2d+2m}}\right),
\qquad
m=\min_{i,j}(\alpha_i-\beta_j).
\]

For each fixed strictly separated shape \((\alpha,\beta)\), continuity of the normalized determinant therefore gives a threshold \(d_0(\alpha,\beta)\) beyond which the full theta PF3 minor is positive.

## Mixed-sign normalized search

A seeded search sampled 300,000 pairs of ordered triples in \([-1,1]\), retained 269,819 configurations whose difference matrices contained both signs, and minimized the positive row--column and Vandermonde normalized minor

\[
Q_3=\frac{\det N}{V(x)V(y)}.
\]

No negative value occurred. The minimum was

\[
Q_3=2997.0495143605935,
\qquad
\det N=6.884528692241432\times10^{-5},
\]

at

\[
x=(-0.1104837609,-0.0800115911,-0.0118415398),
\]

\[
y=(-0.0616152479,-0.0434597001,0.0265639685).
\]

Execution reference: `structured_command_execution:e_19044_1788225901421197100_10`. This is exploratory rather than interval-certified, but it targets the mixed-sign regime excluded from the same-sign tail theorem and retains a positive normalized margin.

## Order-four coalescent center test

The signed coalescent PF4 minor at the even center is

\[
H_4(0)=\det[\Phi^{(i+j)}(0)]_{i,j=0}^{3},
\]

because the orientation factor is \((-1)^6=1\). Termwise differentiation through order six gave

\[
(\Phi,\Phi'',\Phi^{(4)},\Phi^{(6)})(0)
=(0.8933938009,-16.7305007747,812.1628334554,-50735.7259061687)
\]

and

\[
H_4(0)=84332487.94045542>0.
\]

Execution reference: `structured_command_execution:e_19044_1788226016415109200_11`. The calculation is non-certifying but has a large positive margin. PF4 therefore survives this coalescent center falsifier; iterating center tests order by order would not establish total positivity.

## Schoenberg zero obstruction

Schoenberg's characterization of integrable Pólya-frequency kernels states that if \(\Phi\) were totally positive of all orders, its bilateral Laplace transform would have the form

\[
\mathcal L\Phi(z)=\frac1{\Psi(z)}
\]

on its convergence strip, where \(\Psi\) is an entire Laguerre--Pólya function. Such a reciprocal has no zeros wherever the Laplace transform is finite and analytic.

The exact source normalization instead gives

\[
\mathcal L\Phi(z)=2\,\xi\!\left(\tfrac12+z\right)
\]

before the fixed \(u=2q\) rescaling. The completed Riemann function has known nontrivial zeros on the critical line, so this bilateral transform has zeros inside its entire analytic domain. Therefore \(\Phi\) is not a Pólya-frequency kernel of infinite order.

This resolves the total-positivity branch independently of RH: known critical-line zeros already contradict the zero-free reciprocal form. The successful PF2 theorem and exploratory PF3/PF4 tests imply only that the first failing translation minor occurs at a higher order or away from the tested configurations. Searching for that minor may localize the failure but cannot restore a PF-infinity confinement proof.

## Disposition

A fixed ordered configuration cannot generate a PF3 counterexample merely by translation into a same-sign tail. The result is not uniform as spacings coalesce or the shape varies with \(d\), because the leading strictly positive determinant can then approach zero. Remaining falsifiers must involve a bounded offset, mixed-sign differences, or a simultaneous tail-and-coalescence degeneration.

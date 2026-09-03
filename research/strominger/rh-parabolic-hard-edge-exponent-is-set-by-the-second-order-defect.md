# The parabolic hard-edge exponent is set by the second-order defect

## Question

Which coefficient asymptotic would produce the observed \(n^{-2}\) compact mass?

Assume

\[
a_n=A n^s(1+O(n^{-1})),
\qquad
\varepsilon_n=\frac{a_n+a_{n+1}-b_n}{a_{n+1}}
=\frac{C}{n^2}+O(n^{-3}).
\]

After removing the alternating sign by \(Q_n=(-1)^n u_n\), the recurrence is

\[
u_{n+1}-(1+r_n-\varepsilon_n)u_n+r_nu_{n-1}=0,
\qquad
r_n=\frac{a_n}{a_{n+1}}
=1-\frac{s}{n}+O(n^{-2}).
\]

Substituting \(u_n\sim n^p\) gives the Euler indicial equation

\[
p(p-1)+sp+C=0,
\]

or

\[
p^2+(s-1)p+C=0.
\]

For the Weibull diagnostic scale \(s=4\), the choice \(C=2\) gives roots

\[
p=-1,-2.
\]

The slower recessive branch \(Q_n(x)=O(n^{-1})\) on a fixed compact interval has squared mass \(O(n^{-2})\), exactly the variational rate required.

The finite defect values \(n^2\varepsilon_n\) rise toward this candidate but have not reached it on the available low-degree grid.

## Disposition

Resolve the conditional indicial calculation. The next leaf is `hard-edge-defect-two-limit`: prove or falsify

\[
n^2\frac{a_n+a_{n+1}-b_n}{a_{n+1}}\longrightarrow2
\]

for the truncated Weibull recurrence.

## Claim boundary

Neither \(C=2\) nor selection of the \(p=-1\) branch is proved. Both coefficient asymptotics and solution normalization require independent control.

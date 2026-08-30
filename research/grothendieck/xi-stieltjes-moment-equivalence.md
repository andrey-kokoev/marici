# The xi Weyl measure is equivalent to a Stieltjes moment problem

Epistemic-graph event: 1423.

## Squared spectral variable

Let

\`B(y)=Xi(i y)=xi(1/2-y)=xi(1/2+y)\`

and, for \`x>0\), define directly from the theta integral

\`R_Xi(x)=d/dx log B(sqrt(x))
=B'(sqrt(x))/(2 sqrt(x) B(sqrt(x)))\`.

The apparent singularity at \`x=0\` is removable because \`B\` is even.
This scalar function is the squared-variable form of the imaginary-axis Weyl
data in Ledger 1383.

## Exact Stieltjes equivalence

The following are equivalent:

1. the Riemann hypothesis;
2. \`R_Xi\` is a Stieltjes function, with its meromorphic continuation defined
   by the theta-derived \`Xi\`.

Under RH, the symmetric canonical product gives

\`B(y)/B(0)=prod_(gamma>0)(1+y^2/gamma^2)^(m_gamma)\`.

Therefore

\`R_Xi(x)=sum_(gamma>0) m_gamma/(gamma^2+x)
=integral_[0,infinity) d mu(t)/(t+x)\`,

where

\`mu=sum_(gamma>0) m_gamma delta_(gamma^2)\`

is positive. The convergence condition
\`integral (1+t)^(-1)d mu(t)<infinity\` follows from the order-one zero count.

Conversely, a Stieltjes transform is analytic off the negative real axis and
has nonnegative measure there. Since the theta-defined \`R_Xi\` is
meromorphic, its representing measure must be atomic at its poles. Every zero
of \`B\` is a pole of its logarithmic derivative with positive integer
residue. Stieltjes analyticity therefore forces every such pole to lie at
\`x=-gamma^2<0\`; hence every zero of \`B(y)\` lies at \`y=+/- i gamma\`, and
every zero of \`Xi(z)=B(-i z)\` is real. This is RH.

Thus

\`RH iff R_Xi is Stieltjes\`.

## Source-only positivity hierarchy

A Stieltjes function is completely monotone on the positive axis:

\`(-1)^n R_Xi^(n)(x)>=0\`, for all \`n>=0\`, \`x>0\`.

For the atomic representation,

\`(-1)^n R_Xi^(n)(x)
=n! sum_gamma m_gamma/(gamma^2+x)^(n+1)\`.

These derivative inequalities are necessary source-only hostile tests. Their
Hankel moment matrices must also be positive:

\`[(-1)^(j+k) R_Xi^(j+k)(x)/(j+k)!]_(j,k)>=0\`.

Passing complete monotonicity alone is not sufficient for the Stieltjes
property; the analytic continuation and Stieltjes moment conditions must also
hold. A single violated derivative or Hankel minor falsifies the positive
Weyl construction.

## Operator meaning

The measure \`mu\` is exactly the positive spectral measure of the squared
conditional operator from Ledger 1382. If a source construction produces
this Stieltjes representation directly from theta/prime data, then taking the
signed square-root double gives eigenvalues \`+/- gamma\`, the Gaussian paired
polarization supplies the double, and the second regularized determinant is
\`Xi(z)/Xi(0)\`.

This formulation separates the two missing proofs:

1. construct the positive Stieltjes measure without locating zeros; and
2. identify its multiplication realization with the Mellin boundary defect
   space rather than only an abstract moment model.

## Scope

This is an unconditional equivalence and a source-only falsifier hierarchy.
It does not prove the Stieltjes property or construct the required boundary
map.

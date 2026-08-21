# The intrinsic-prime trace is off-diagonal free propagation

Epistemic-graph event: 1430.

## Green-kernel identity

Let \`H_0=-d^2/du^2\` on the real logarithmic line. For \`x>0\), the resolvent
kernel is

\`G_x(u,v)=(H_0+x)^(-1)(u,v)
=exp(-sqrt(x)|u-v|)/(2sqrt(x))\`.

The prime contribution in Ledger 1388 is therefore

\`R_prime(x)
=-sum_(n>=2)Lambda(n)n^(-1/2)G_x(0,log n)\`,

valid for \`sqrt(x)>1/2\`. At finite cutoff this is an exact matrix element
between the boundary point at zero and the source

\`q=sum_n Lambda(n)n^(-1/2)delta_(log n)\`.

The Euler prime-power trace is thus not an abstract fitted fluctuation: it is
free propagation across the logarithmic distances \`log n\` selected by
intrinsic norms.

## Why it is not a positive diagonal resolvent

For one nonzero distance \`a>0\), set

\`g_a(x)=exp(-a sqrt(x))/(2sqrt(x))\`.

On the Stieltjes cut \`x=-t+i0\`,

\`g_a(-t+i0)
=-sin(a sqrt(t))/(2sqrt(t))
-i cos(a sqrt(t))/(2sqrt(t))\`.

Stieltjes inversion would assign density

\`rho_a(t)=cos(a sqrt(t))/(2pi sqrt(t))\`,

which changes sign infinitely often. Therefore \`g_a\` is not a Stieltjes
function for \`a>0\). Each nontrivial prime distance is an off-diagonal
resolvent matrix element, not a positive quadratic resolvent
\`<v,(A+x)^(-1)v>\`.

Positive von Mangoldt weights cannot remove this obstruction termwise.

## Paired-channel interpretation

Off-diagonal Green functions belong naturally to a paired system. At finite
cutoff, introduce two boundary channels with cross-resolvent entry

\`<delta_0,(H_0+x)^(-1)q>\`.

The coefficient--Betti symplectic double supplies exactly the algebraic
distinction between source and dual readout needed for such a cross term.
The negative Euler sign can then arise from a Schur complement or from the
orientation of the paired boundary form.

This is only a typing match, not yet a construction. A self-adjoint block
operator requires:

- actual Hilbert-space boundary vectors rather than delta distributions;
- a cutoff-independent domain and convergence proof;
- a positive Schur complement equal to the full completed \`R_Xi\`; and
- the gamma channel and Gaussian corner in the same Green identity.

## Sharp next falsifier

Any proposed block boundary must reproduce the finite-cutoff identity above
before continuation. Its Schur complement must then be Nevanlinna. Failure of
the block Green identity, positivity, or cutoff convergence kills the proposal
without reference to Riemann zeros.

The result also excludes a simpler route: no direct sum of independent
positive prime resolvents can equal the Euler term, because direct sums
produce diagonal Stieltjes matrix elements whereas the prime propagators have
sign-changing cut densities.

## Scope

This is an exact finite-cutoff/free-resolvent realization and a no-go for
diagonal positive prime measures. The paired self-adjoint block and its
completed Schur complement remain unconstructed.

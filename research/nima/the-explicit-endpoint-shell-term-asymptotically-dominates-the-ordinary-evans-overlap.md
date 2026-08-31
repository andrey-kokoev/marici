# The explicit endpoint shell term asymptotically dominates the ordinary Evans overlap

## Question

On late consecutive-prime shells, can the ordinary overlap cancel the newly
explicit derivative-plus-wall endpoint term by itself?

## Claim boundary

No under the frozen unit coefficient convention for those two terms. The
endpoint term is positive and larger than the negative ordinary overlap by an
unbounded factor set by the theta logarithmic decay rate. Reciprocal or linking
ports must therefore supply the dominant compensating contribution. A different
source coefficient must be inserted before applying this conclusion.

## Late-tail data

Let

\[
 \Lambda(q)=-\frac{\Phi'(q)}{\Phi(q)}.
\]

For the positive theta tail,

\[
 \Lambda(q)\longrightarrow\infty,
 \qquad
 \frac{\Lambda'(q)}{\Lambda(q)^2}\longrightarrow0.
\]

For fixed \(z\) in a compact parameter set, the right Evans history satisfies

\[
 u_z(q)
 =-\frac{\Phi(q)}{\Lambda(q)+z}\left(1+o(1)\right)
\]

locally uniformly in \(z\).

Take consecutive primes \(p<q\) and set

\[
 a=\log p,
 \qquad
 b=\log q.
\]

The prime gap gives \(b-a\) much larger than the theta decay scale
\(\Lambda(a)^{-1}\) on every sufficiently late shell; for the leading Gaussian
term, \(\Lambda(a)\sim2\pi p^2\).

## Ordinary term

In the Hermitian diagnostic lane,

\[
 I_{p,q}^{(0)}(z)
 =\int_a^b\Phi(x)\overline{u_z(x)}\,dx.
\]

Its real part is negative. Endpoint Laplace asymptotics gives

\[
 \operatorname{Re}I_{p,q}^{(0)}(z)
 =-\frac{\Phi(a)^2}{2\Lambda(a)^2}
 \left(1+o(1)\right).
\]

The upper endpoint contribution is negligible because the theta profile loses
many decay lengths across one late prime shell.

## Endpoint totalization

The derivative-plus-wall term is

\[
 I_{p,q}^{({\rm end})}(z)
 =\Phi(b)\overline{u_z(b)}
 -\Phi(a)\overline{u_z(a)}.
\]

Using the same Evans asymptotic,

\[
 \operatorname{Re}I_{p,q}^{({\rm end})}(z)
 =\frac{\Phi(a)^2}{\Lambda(a)}
 \left(1+o(1)\right)>0.
\]

Therefore

\[
 \frac{
 \operatorname{Re}I_{p,q}^{({\rm end})}(z)
 }{
 |\operatorname{Re}I_{p,q}^{(0)}(z)|
 }
 =2\Lambda(a)(1+o(1))
 \longrightarrow\infty.
\]

The two terms do not cancel. Their sum is eventually positive and asymptotic
to the endpoint term.

## Analytic-transpose lane

Replacing Hermitian conjugation by the analytic dual pairing gives holomorphic
shell functions with the same scale separation on compact parameter sets. The
real-sign statement applies only on a declared real structure or sewing locus;
the magnitude asymptotic remains the relevant obstruction for analytic jets.

## Required remaining compensation

If the complete shell identity is to vanish, then

\[
 I_{p,q}^{({\rm recip})}
 +I_{p,q}^{({\rm link})}
 =-
 \left(
 I_{p,q}^{(0)}+I_{p,q}^{({\rm end})}
 \right).
\]

Thus the reciprocal-plus-linking contribution must have the endpoint scale

\[
 \frac{\Phi(a)^2}{\Lambda(a)},
\]

not merely the smaller ordinary-overlap scale

\[
 \frac{\Phi(a)^2}{\Lambda(a)^2}.
\]

A boundedness theorem does not supply this magnitude or sign.

## Coefficient qualification

The conclusion uses the same frozen shell coefficient on the ordinary and
first-order Green totalization. If the final source joint column assigns a
factor \(c_p\) to one port, the asymptotic comparison must include it. Such a
factor must come from the source metric or incidence map and cannot be chosen
after observing this mismatch.

## Disposition

The first two computable shell pieces fail to cancel and have parametrically
different sizes. Candidate one now demands a source-derived reciprocal or
linking term at the larger endpoint scale, for every shell and multiplicity
jet. No such identity is currently established. No RH conclusion is
authorized.

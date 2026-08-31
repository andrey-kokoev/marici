# Every Evans multiplicity jet retains the same endpoint dominance on late prime shells

## Question

Could higher parameter derivatives remove the scale mismatch between the
ordinary overlap and derivative-plus-wall endpoint term?

## Claim boundary

No. For every fixed jet order, both terms acquire the expected additional
inverse powers of the theta logarithmic decay rate, but their ratio still grows
like \(2\Lambda(\log p)\). Thus every multiplicity jet requires a dominant
reciprocal or linking compensation. This is an asymptotic necessity, not a
construction of that compensation.

## Evans jet asymptotic

For the positive-end Evans history,

\[
 u_z(x)=-\int_x^\infty e^{z(x-r)}\Phi(r)\,dr.
\]

Differentiating \(j\) times gives

\[
 \partial_z^ju_z(x)
 =-\int_x^\infty (x-r)^j e^{z(x-r)}\Phi(r)\,dr.
\]

Let

\[
 \Lambda(x)=-\frac{\Phi'(x)}{\Phi(x)}.
\]

Endpoint Laplace asymptotics, uniformly for \(z\) in compact sets, gives

\[
 \partial_z^ju_z(x)
 =(-1)^{j+1}\frac{j!\,\Phi(x)}{(\Lambda(x)+z)^{j+1}}
 \left(1+o(1)\right).
\]

The slow-variation condition

\[
 \frac{\Lambda'(x)}{\Lambda(x)^2}\to0
\]

controls the error for every fixed \(j\).

## Ordinary jet shell

For consecutive primes \(p<q\), put \(a=\log p\) and \(b=\log q\). In the
analytic-transpose lane, the ordinary jet has leading scale

\[
 \partial_z^j I_{p,q,{\rm an}}^{(0)}(z)
 =(-1)^{j+1}
 \frac{j!\,\Phi(a)^2}{2\Lambda(a)^{j+2}}
 \left(1+o(1)\right).
\]

The factor \(2\Lambda(a)\) in the denominator comes from integrating a tail
whose pointwise decay rate is asymptotically \(2\Lambda(a)\).

## Endpoint jet shell

The analytic endpoint term is

\[
 I_{p,q,{\rm an}}^{({\rm end})}(z)
 =\Phi(b)u_z(b)-\Phi(a)u_z(a).
\]

The upper endpoint is negligible on a late prime shell. Hence

\[
 \partial_z^jI_{p,q,{\rm an}}^{({\rm end})}(z)
 =(-1)^j
 \frac{j!\,\Phi(a)^2}{\Lambda(a)^{j+1}}
 \left(1+o(1)\right).
\]

The ordinary and endpoint jets have opposite leading signs in the real
convention, but unequal magnitudes.

## Persistent ratio

For every fixed \(j\),

\[
 \frac{
 |\partial_z^j I_{p,q,{\rm an}}^{({\rm end})}(z)|
 }{
 |\partial_z^j I_{p,q,{\rm an}}^{(0)}(z)|
 }
 =2\Lambda(a)(1+o(1))
 \longrightarrow\infty.
\]

Thus parameter differentiation does not restore ordinary/end cancellation.

## Required compensation at multiplicity m

If \(z_0\) is a Xi zero of multiplicity \(m\), candidate one requires for each
\(0\le j<m\)

\[
 \partial_z^j
 \left(
 I^{(0)}+I^{({\rm end})}+I^{({\rm recip})}+I^{({\rm link})}
 \right)(z_0)=0.
\]

The combined reciprocal-plus-linking jet must therefore have leading endpoint
scale

\[
 \frac{j!\,\Phi(a)^2}{\Lambda(a)^{j+1}}
\]

with the source-forced opposite phase, separately at every jet order.

A construction that cancels only \(j=0\) does not preserve local module length.

## Uniformity boundary

The asymptotic is uniform for bounded jet order and \(z\) in compact parameter
sets. No threshold uniform over the unbounded sewing axis or unbounded
multiplicity is asserted.

Any prime-dependent port coefficient must be inserted before comparing these
scales.

## Disposition

The endpoint dominance is stable under all fixed Evans parameter derivatives.
Multiplicity strengthens the shell obstruction: reciprocal/linking transport
must reproduce an entire factorial inverse-decay hierarchy, not one scalar
cancellation. No such source identity is currently proved. No RH conclusion is
authorized.

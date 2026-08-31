# The reciprocal-linking shell must match a two-term asymptotic, not only the leading endpoint flux

## Question

What precise late-shell asymptotic must the combined reciprocal and linking
ports satisfy if candidate one is true for every multiplicity jet?

## Claim boundary

They must cancel both the leading endpoint term and the first smaller ordinary
overlap term. Matching only the leading boundary flux leaves a definite
nonzero residual one inverse decay rate lower. This supplies a two-term hostile
test for any proposed source response law.

## Frozen asymptotics

Let \(a=\log p\) for a late consecutive-prime shell and let

\[
 \Lambda(a)=-\frac{\Phi'(a)}{\Phi(a)}.
\]

For every fixed jet order \(j\), the analytic-transpose ordinary and endpoint
terms satisfy

\[
 \partial_z^j I^{(0)}
 =(-1)^{j+1}
 \frac{j!\Phi(a)^2}{2\Lambda(a)^{j+2}}
 \left(1+o(1)\right),
\]

\[
 \partial_z^j I^{({\rm end})}
 =(-1)^j
 \frac{j!\Phi(a)^2}{\Lambda(a)^{j+1}}
 \left(1+o(1)\right).
\]

Write

\[
 R_j(a,z)
 =\partial_z^j
 \left(I^{({\rm recip})}+I^{({\rm link})}\right)(z).
\]

## Necessary two-term law

The shell equation requires

\[
 R_j
 =-\partial_z^j
 \left(I^{(0)}+I^{({\rm end})}\right).
\]

Therefore a necessary asymptotic is

\[
 R_j(a,z)
 =(-1)^{j+1}
 \frac{j!\Phi(a)^2}{\Lambda(a)^{j+1}}
 \left(
 1-\frac1{2\Lambda(a)}+o\left(\Lambda(a)^{-1}\right)
 \right).
\]

The leading coefficient is fixed to unit magnitude in the frozen shell
normalization. The first correction is also fixed.

## Leading-only hostile

Suppose a proposed reciprocal law supplies only

\[
 R_j^{\rm lead}
 =(-1)^{j+1}
 \frac{j!\Phi(a)^2}{\Lambda(a)^{j+1}}
 \left(1+o(1)\right)
\]

without the subleading coefficient. After leading endpoint cancellation, the
remaining shell is

\[
 (-1)^{j+1}
 \frac{j!\Phi(a)^2}{2\Lambda(a)^{j+2}}
 \left(1+o(1)\right),
\]

which is the ordinary overlap and is nonzero on every sufficiently late shell.
Thus flux cancellation alone does not imply arithmetic adjoint cancellation.

## Multiplicity coherence

For a zero of multiplicity \(m\), the same two-term law must hold for
\(0\le j<m\). A source operator independent of \(j\) may generate the factorial
hierarchy through parameter differentiation, but it must reproduce the same
unit leading coefficient and the correct subleading coefficient at every
order.

A law fitted at \(j=0\) cannot be promoted to this jet family without an
analytic source identity.

## Coefficient qualification

If the final joint column assigns port weights, let \(c_0,c_{\rm end}\) be the
ordinary and endpoint coefficients. The necessary benchmark becomes

\[
 R_j
 =-c_{\rm end}\partial_z^jI^{({\rm end})}
  -c_0\partial_z^jI^{(0)}.
\]

The displayed unit and \(-1/2\) coefficients apply when
\(c_0=c_{\rm end}=1\). Source weights must be frozen before using the hostile.

## Cheapest source test

For any proposed reciprocal/linking constructor:

1. compute its late-shell endpoint expansion through relative order
   \(\Lambda^{-1}\);
2. compare the leading coefficient with \(-I^{({\rm end})}\);
3. compare the next coefficient with \(-I^{(0)}\);
4. repeat after one parameter derivative.

Failure at any step rejects complete shell divisibility without evaluating the
full Xi zero set.

## Disposition

Candidate one imposes a two-term asymptotic response law on every late shell
and multiplicity jet. Maximal-isotropic boundary flux can explain at most the
leading term; the subleading ordinary overlap remains an independent arithmetic
condition. No source law currently supplies both coefficients. No RH conclusion
is authorized.

# Continuous Krein test does not descend to logarithmic-label atoms

## Question

Can indeterminacy of the continuous Weibull moment measure be transferred directly to the discrete logarithmic-label measure when \(0<\beta<1/2\)?

## Two distinct measures

The coefficient completion supplies the atomic measure

\[
\mu_{a,\beta}
=
\sum_{n\ge2}rac{1}{n e^{2a(\log n)^\beta}}
\delta_{\log n}.
\]

Its integral-test comparator is the absolutely continuous measure

\[
d\nu_{a,\beta}(x)=e^{-2ax^\beta}\,dx.
\]

They have comparable tail masses because the logarithmic cell
\([\log n,\log(n+1))\) has length asymptotic to \(1/n\). Comparable tails do not identify their \(L^2\) polynomial closures.

## Krein typing obstruction

The standard continuous Krein sufficient condition evaluates a positive density through an integral of its logarithm. The atomic measure \(\mu_{a,\beta}\) has no positive Lebesgue density: its Radon--Nikodym derivative is zero almost everywhere. Substituting that derivative makes the logarithmic-density integral divergent rather than finite. Substituting the smooth density of \(\nu_{a,\beta}\) changes the measure and the Hilbert space.

Therefore the continuous Weibull Krein calculation, even when it proves indeterminacy of \(\nu_{a,\beta}\), does not prove indeterminacy of \(\mu_{a,\beta}\), non-density of polynomials in \(L^2(\mu_{a,\beta})\), or existence of a discrete flat coefficient vector.

## Cell comparison is insufficient

The mass comparison

\[
\mu_{a,\beta}(\{\log n\})
\asymp
\nu_{a,\beta}([\log n,\log(n+1)))
\]

controls positive tail sums. Polynomial-density transfer would additionally require a bounded sampling/reconstruction pair intertwining multiplication by \(x\) and preserving polynomial closures. No such pair is present in the theta source packets. Point sampling is not bounded on an untyped \(L^2(\nu_{a,\beta})\) space.

## Disposition

Direct continuous Krein promotion is blocked by measure type. The surviving discrete question requires either a discrete moment-problem criterion using the actual masses and support, or an explicit coefficient vector with controlled weighted norm and vanishing moments.

## Claim boundary

This is not a determinacy theorem for \(\mu_{a,\beta}\). It rejects one invalid inference. The sub-Hardy discrete measure may still be determinate, indeterminate but polynomially dense, or indeterminate with a nontrivial polynomial orthogonal complement.

# Fourier transport of primitive and square anomaly increments

## Exact action

At each prime, with `q=p^(-s)` and `r=p^(s-1)`, the direct-to-dual line
transition is

`gamma_p(s)=(1-q)/(1-r)`.

Reciprocal reflection exchanges `q` and `r`, hence

`gamma_p(1-s)=gamma_p(s)^(-1)`.

In a local convergent chart, the grade coordinate

`c_(p,k)(s)=(r^k-q^k)/k`

therefore satisfies `c_(p,k)(1-s)=-c_(p,k)(s)` for every `k>=1`. In
particular, primitive and square increments transform exactly as

`Delta C_(1;X,Y)(1-s)=-Delta C_(1;X,Y)(s)`,
`Delta C_(2;X,Y)(1-s)=-Delta C_(2;X,Y)(s)`.

No logarithm branch is needed at the line-transition level.

## Triangle coherence

For cutoff inclusions `X subset Y`, put

`U_(X,Y)(s)=product_(X<p<=Y) gamma_p(s)`.

The transition law `U_(Y,Z)U_(X,Y)=U_(X,Z)` is preserved under reflection:
each factor is inverted, and the transition group is commutative. In additive
coordinates, sign reversal preserves

`Delta C_(k;X,Z)=Delta C_(k;X,Y)+Delta C_(k;Y,Z)`.

Thus Fourier--Tate transport defines a canonical coherent action on the
relative primitive and square anomaly torsors. The finite-prime naturality
residual is exactly zero grade by grade.

## Typing correction

This action exchanges the positive and negative cyclic valuation towers; it is
not an endomorphism of one unilateral Euler tower. The relative line system or
bilateral group completion is the correct target. Fourier saturation preserves
the primitive and square grades separately and does not make their inequivalent
completion norms uniformly comparable.

## Remaining attachment gate

Arithmetic increment transport is not the missing confinement law. The next
residual can occur only when this inverted arithmetic torsor is attached to
the archimedean/polar Poisson four-channel packet and then descended through
the complete Green boundary form. That mixed attachment must be checked before
forming the scalar completed section.

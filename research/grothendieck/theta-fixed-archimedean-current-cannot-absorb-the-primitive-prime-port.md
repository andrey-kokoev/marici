# A fixed archimedean current cannot absorb the primitive theta prime port

## Primitive cutoff readout

The atomic primitive incidence current has finite-cutoff odd readout

\[
 C_{1,X}(t)
 =2i\sum_{p\le X}p^{-1/2}\sin(t\log p)
 =2i\operatorname{Im}
 \sum_{p\le X}p^{-1/2+it}.
\]

This is the exact `P` output before completion.

## Prime-number-theorem asymptotic

For fixed nonzero real `t`, partial summation with the prime number theorem
gives

\[
 \sum_{p\le X}p^{-1/2+it}
 \sim
 \frac{X^{1/2+it}}
 {(1/2+it)\log X}.
\]

Consequently the primitive odd current has an oscillatory envelope of size

\[
 \boxed{
 |C_{1,X}(t)|\ \text{along subsequences}
 \asymp\frac{\sqrt X}{\log X}.}
\]

It does not converge as the prime cutoff tends to infinity.

## Fixed-`A` no-go

Let `A(t)` be any cutoff-independent archimedean boundary current, including
one obtained from a fixed gamma factor.  Then

\[
 C_{1,X}(t)+A(t)
\]

retains the same unbounded oscillatory envelope.  Therefore

\[
 \boxed{
 \text{no fixed archimedean current can absorb the primitive }P
 \text{ cutoff divergence}.}
\]

This falsifies the naive interpretation of the packet-138 anomaly-inflow
conjecture as additive cancellation by a cutoff-independent gamma endpoint.

## Compiler consequence

The formal operations `P` and fixed `A` commute because they act on separate
typed factors, but neither order completes the primitive readout:

\[
 PA=AP,
 \qquad
 \lim_{X\to\infty}(C_{1,X}+A)
 \text{ does not exist}.
\]

The braid residual is zero while the completion residual is nonzero.  This is
an explicit example of why braid coherence alone does not prove that a repair
compiler closes its defects.

## What can still work

Any surviving completion must use one of the following stronger operations:

1. a cutoff-covariant boundary countercurrent `A_X` with the exact opposite
   moving asymptotic;
2. a global Poisson/explicit-formula transform that never forms the primitive
   scalar sum separately;
3. a relative distributional pairing in an exponential Mellin test space,
   followed by analytic continuation as one inseparable operation.

The first option is admissible only if `A_X` is derived from the same finite
source cutoff and is compatible under cutoff inclusion.  Subtracting the
displayed asymptotic after inspection is not source authority.

## Contrast with the square port

The `k=2` current is much milder:

\[
 C_{2,X}(t)=i\sum_{p\le X}p^{-1}\sin(2t\log p).
\]

For nonzero `t`, its continuum prime-density model is an oscillatory
logarithmic integral and may converge conditionally.  It still is not
trace-class and must remain typed, but it does not share the primitive
`sqrt(X)/log(X)` obstruction.

## Revised singular gate

The next source operation is not `P` followed by `A`.  It must be a joint
constructor

\[
 \boxed{
 \mathfrak A(P_X,A_X)
 \quad\text{or}\quad
 \mathfrak E(\mu_1,\text{theta boundary})}
\]

whose finite-cutoff value is defined before scalar compression and whose
cutoff transition maps telescope exactly.  The primitive port and completion
cannot be compiled independently.

# A formal common-phase Z4 average enforces the diagonal grade rule but has no current source authority

## Question

What algebraic projector would remove all delay grades not divisible by four,
and can it be identified with the retained Fourier action?

## Claim boundary

A simultaneous common-phase quarter rotation of both reciprocal delay atoms
has exactly the required invariant subalgebra. Its Reynolds average kills total
grades not divisible by four. The current source audit does not authorize
identifying this formal action with theta Fourier transport, causal reflection,
or the wall Fourier–Tate exchange.

## Formal action

Let \(\gamma\) act by

\[
 \gamma(S_+,S_-)=(iS_+,iS_-).
\]

Then \(\gamma^4=1\). On a monomial,

\[
 \gamma\left(S_+^rS_-^s\right)
 =i^{r+s}S_+^rS_-^s.
\]

The Reynolds projector is

\[
 \mathcal P_4f
 =\frac14\sum_{j=0}^3f(i^jS_+,i^jS_-).
\]

Therefore

\[
 \mathcal P_4(S_+^rS_-^s)
 =\begin{cases}
 S_+^rS_-^s,&r+s\equiv0\pmod4,\\
 0,&r+s\not\equiv0\pmod4.
 \end{cases}
\]

On the reciprocal-balanced diagonal \(r=s=k\), this retains exactly even
\(k\), hence orders

\[
 p^{-2},p^{-4},p^{-6},\ldots.
\]

It kills the forbidden balanced terms \(p^{-1},p^{-3},\ldots\).

## Why ordinary reciprocal phase does not suffice

A conjugate phase action

\[
 (S_+,S_-)\longmapsto(iS_+,-iS_-)
\]

acts on \(S_+^kS_-^k\) by the trivial factor one. It preserves every balanced
grade, including the forbidden grade-two term \(S_+S_-=p^{-1}\).

Thus reciprocal balance alone does not imply the modulo-four rule. The needed
formal symmetry rotates both sheets by the same phase.

## Source-authority obstruction

Existing source audits distinguish:

- theta Fourier presentation;
- causal reflection, equivalent to a Fourier half-turn on history;
- wall Fourier–Tate exchange, an anti-symplectic involution;
- determinant-line or Maslov phase.

The normalized completed Gaussian and arithmetic comb are Fourier-fixed, and
one Fourier application does not create an authorized relative tail quadrature.
The wall exchange squares to the identity rather than acting as the common
phase \(i\). Causal reflection supplies sheet reversal, not simultaneous
common-phase rotation.

Consequently no existing arrow identifies any retained source operator with
\(\gamma\).

## Conditional construction target

A source-derived implementation of \(\mathcal P_4\) would require a typed
operator \(J\) on the completed ordered-pair response carrier satisfying

\[
 J^4=I,
\]

\[
 J(S_+,S_-)=(iS_+,iS_-)
\]

in the delay-coordinate comparison, together with compatibility with:

- prime and ordered-pair labels;
- the analytic-transpose Green form;
- reciprocal reversal;
- endpoint codiagonalization;
- the completed-theta response map.

A determinant-line phase could implement this only after a proved functor back
to the response carrier.

## Hostile

Applying the actual wall exchange or conjugate reciprocal phase to
\(S_+S_-\) leaves it invariant. Any claim that these known actions enforce the
grade-two cancellation is therefore false.

## Disposition

The common-phase Z4 Reynolds projector is the exact algebraic mechanism for the
divisible-by-four selection rule, but it is currently only a conditional
template. Attributing it to Fourier transport would repeat a retracted source
typing error. The diagonal reciprocal response remains open pending an
independently sourced common-phase action or another cancellation theorem. No
RH conclusion is authorized.

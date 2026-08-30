# Theta boundaryless band sum is beyond all algebraic orders

## Bounded question

Why can the full undecomposed oscillatory source behave qualitatively
differently from every finite terminal band block?

## Full source moments

Let

\[
\mathcal I_J(a,b)
=
\int_0^\infty J_a(r)\cos(br)\,dr,
\]

and

\[
\mathcal I_W(a,b)
=
\int_0^\infty rW_a(r)\sin(br)\,dr.
\]

The completed theta density decays super-exponentially. Its tilted
autocorrelation \(W_a\), its tilt derivative \(J_a\), and all separation
derivatives therefore decay at infinity rapidly enough for repeated
integration by parts.

## Parity removes the seam jets

Autocorrelation makes both \(W_a\) and \(J_a\) even functions of separation.
Consequently,

\[
J_a^{(2n+1)}(0)=0
\qquad
(n\ge0).
\]

Also

\[
h_a(r)=rW_a(r)
\]

extends to a smooth odd function, so

\[
h_a^{(2n)}(0)=0
\qquad
(n\ge0).
\]

Repeated integration by parts in the cosine transform exposes only odd
derivatives of \(J_a\) at the origin. Repeated integration by parts in the
sine transform exposes only even derivatives of \(h_a\) there. Every such
boundary jet vanishes. The boundary at infinity vanishes by source decay.

Therefore, for every integer \(N\ge1\),

\[
\mathcal I_J(a,b)=O_{a,N}(b^{-N}),
\qquad
\mathcal I_W(a,b)=O_{a,N}(b^{-N}).
\]

After multiplication by the physical coefficients
\(\beta=O(b)\) and \(\alpha=O(1)\), the complete angular block still satisfies

\[
\beta\mathcal I_J(a,b)+\alpha\mathcal I_W(a,b)
=
O_{a,N}(b^{-N})
\]

for every \(N\), after relabelling the order.

## Contrast with finite terminal blocks

A finite block ending at \(R\) produces the algebraic term

\[
\frac{2}{b}
\left[J_a'(R)-aR W_a(R)\right],
\]

whose coefficient is strictly negative for every finite \(R>0\). The full
source has no terminal endpoint, so that entire algebraic hierarchy is absent.

Thus the infinite limit does not turn a negative algebraic coefficient into a
positive one. It removes the artificial coefficient because the operation
that created it, terminal truncation, is absent.

## Result

The boundaryless completed source is beyond all algebraic high-frequency
orders, whereas every finite terminal band block carries a negative algebraic
endpoint defect. Band truncation is therefore not an asymptotically faithful
localization of the full angular observable.

The sign of the complete source lives in exponentially small or more general
nonperturbative transform data. No finite separation jet and no fixed or
bounded-width band grouping can see it.

## Deutschian explanation

Infinity is qualitatively different here for a source-derived reason:

1. the full correlation has exact even/odd sewing at the origin;
2. the completed theta tail removes the boundary at infinity;
3. a finite band cutoff manufactures a terminal boundary current;
4. strict log-concavity orients that manufactured current negatively.

The mystery is therefore not how infinitely many negative blocks become
positive. Finite terminal blocks are different objects with an additional
boundary capability. The full source never possessed that capability.

## Remaining theorem

Algebraic asymptotics are now exhausted. The surviving task is to derive the
first nonperturbative contribution directly from modular theta geometry and
orient it without using zero data.

A hostile source should preserve smoothness, positivity, strict
log-concavity, parity, and rapid decay while changing that nonperturbative
orientation. Such a witness would prove that modular self-reciprocity or
arithmetic label coherence supplies the missing information.

## Prime-square typing boundary

The prime-square current

\[
\mu_2=\frac12\sum_p p^{-1}\delta_{2\log p}
\]

does not by itself act as the spectral-jet number operator. Differentiating
its transform produces moment weights \((2\log p)^m\), hence a coupled moment
or Hankel packet. The number operator instead multiplies the jet grade by
\(m\). Converting one into the other requires the independently sourced jet
dilation generator. Prime-square incidence alone therefore does not supply
the \(m\)-weighted diagonal energy requested by the Fock-square repair.

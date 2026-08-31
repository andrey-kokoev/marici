# Existing Weibull data do not cap the endpoint kernel

## Question

Do the current continuous-moment artifacts provide a quantitative upper bound for the endpoint reproducing kernel at \(x_0=\log3\)?

## Available statements

Three established statements have different directions.

1. Krein integrability for \(0<\beta<1/2\) proves
   \[
   K(x_0,x_0)<\infty.
   \]
   It supplies no numerical value.
2. The degree-\(K\) Christoffel quantities
   \[
   K_K(x_0,x_0)=v_K^*H_K^{-1}v_K
   \]
   increase to \(K(x_0,x_0)\). Every computed value is therefore a lower bound.
3. Entrywise gamma comparators bound the moments forming \(H_K\), but independent entry intervals do not preserve Loewner order under inversion.

None gives an upper bound on the positive tail

\[
K(x_0,x_0)-K_K(x_0,x_0)
=
\sum_{n>K}|P_n(x_0)|^2.
\]

## Missing constructor

A quantitative cap requires at least one of:

- an explicit Nevanlinna matrix for the shifted Weibull problem;
- recurrence-coefficient estimates controlling \(P_n(x_0)\);
- a trial representer \(g\in L^2(\nu)\) satisfying
  \[
  p(x_0)=\langle p,g\rangle
  \]
  for every polynomial, with computed \(\|g\|^2\);
- a positive matrix majorant for the orthogonal-kernel tail.

No such object occurs in the inspected artifacts.

## Disposition

The endpoint kernel is known to be finite but is not quantitatively capped. The degree-six endpoint ratio near \(0.0422\) cannot be promoted to an upper bound or inserted into the remaining \(1/6\) coercivity budget.

This blocks the current coarse quadrature proof, not atomic coercivity itself. A different tail split or a sharper positive quadrature form may enlarge the budget without computing the exact endpoint kernel.

## Claim boundary

This is an implication audit of the current artifacts. It does not prove that no endpoint cap exists and does not treat absence of a recorded constructor as mathematical impossibility.

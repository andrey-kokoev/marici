# A relative wall cocycle does not determine absolute return coercivity

## Question

Can the available source-relative wall cocycle certify strict physical return while its absolute-lift torsor remains unresolved?

## Quotient obstruction

Let the relative datum be a projection

\[
\pi:V_{\rm abs}\longrightarrow V_{\rm rel}
\]

with nontrivial kernel. A relative cocycle \(q\in V_{\rm rel}\) determines the affine lift torsor

\[
\pi^{-1}(q)=c_0+\ker\pi,
\]

not an absolute normalized coupling. Return coercivity depends on the norm of an absolute lift, which need not descend through \(\pi\).

The obstruction already appears in two dimensions. Take

\[
\pi(x,y)=x,
\qquad
q=\frac35.
\]

Three lifts of the same relative class are

\[
c_0=\left(\frac35,0\right),
\qquad
c_1=\left(\frac35,\frac45\right),
\qquad
c_2=\left(\frac35,1\right).
\]

With identity diagonal forms, their squared normalized norms are respectively

\[
\frac9{25},
\qquad
1,
\qquad
\frac{34}{25}.
\]

Thus the same relative cocycle admits a strictly coercive lift, a terminal lift, and a superunit lift. Relative-class closure does not determine even the sign of the absolute return margin.

## Rank-seven consequence

Nima reports that the present \(q_{G12}\) wall cocycle has an unresolved rank-seven absolute-lift torsor. One invisible direction is already enough for the hostile family above; seven directions enlarge rather than remove the ambiguity. Dimension alone does not show that the invisible directions couple to the physical norm, but absent a theorem that they are null or quotiented by a proved physical equivalence, coercivity cannot descend.

## Acceptance alternatives

The physical branch must provide at least one of:

1. a source-selected absolute lift;
2. a proof that every torsor direction is null for the diagonal reference form and return pairing;
3. a uniform norm bound on the entire admissible lift torsor that stays below one;
4. a faithful quotient coordinate on which the physical return norm is well-defined.

A minimum-norm lift chosen for convenience is not source-derived and gives no bound on other admissible lifts.

## Verification

`research/aspect/checkers/check_relative_lift_coercivity_obstruction.py` verifies with exact rationals that one fixed relative class has strict, terminal, and superunit absolute lifts.

## Disposition

The current source-relative cocycle cannot certify scalar-null confinement. The first missing typed object is an absolute physical lift or a descent theorem for the norm/coercivity form. Further finite-return approximation should stop until one of these objects exists.

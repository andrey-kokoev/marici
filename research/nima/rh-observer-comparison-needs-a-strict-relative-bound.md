# RH observer comparison needs a strict relative bound

## Question

Suppose source transport supplies a cone-positive moving observer `m`, while the
zero condition is read by a fixed Evans observer `e`. What finite comparison is
enough to transfer nonvanishing from `m` to `e`?

Write the observer defect as

\[
d=e-m.
\]

On an admissible transported state `y`, assume

\[
m(y)>0
\]

and a source-derived relative estimate

\[
|d(y)|\leq \rho m(y).
\]

If `rho < 1`, then

\[
e(y)=m(y)+d(y)\geq (1-\rho)m(y)>0.
\]

Thus the required coherencer is not equality of the two observers. It is a
strictly contractive comparison cell on the admissible cone.

## Exact hostile boundary

Take

\[
U=\operatorname{diag}(1,-1),\qquad x=(1,1),\qquad y=Ux=(1,-1),
\]

with fixed observer `e=(1,1)` and transported observer

\[
m=eU^{-1}=(1,-1).
\]

Then

\[
m(y)=2,\qquad e(y)=0,\qquad d(y)=-2.
\]

The sharp relative constant is therefore `rho = 1`. Non-strict domination
does not prevent a zero; the hostile saturates the comparison bound exactly.

## DPC

Input:

- a source-derived transported cone;
- its positive moving observer;
- the independently fixed Evans observer;
- an authorized comparison seminorm on their difference.

Pass condition:

- one cutoff-independent `rho < 1` controls the observer defect on every
  admissible state and survives completion.

Immediate falsifiers:

- a state with positive moving margin and zero fixed readout;
- constants `rho_X < 1` at each cutoff with `rho_X` tending to one;
- a comparison obtained by division by the Evans function;
- a bound valid only after scalar projection;
- an observer identification introduced by a fitted frame choice.

## Consequence

The RH-bearing datum has been reduced to a quantitative source question:
does theta/Tate sewing generate a strict angular gap between the transported
positive dual cone and the fixed Evans wall? Positivity, reciprocity, and
contragredient transport alone do not supply that gap.


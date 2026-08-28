# 3855 — The Source Endpoints Fix the Principal Conductor Laurent Jets

## Question

What does the source-normalized analytic family (K^{-1/2+\epsilon}) assign to the two active conductor costalks?

## Universal local integral

Use the source polynomial (R_i) itself as the conductor coordinate. Let (A_i) and (B_i) be its positive absolute values at the two endpoints of the selected physical wall segment.

The principal singular model is

\[
J_i(\epsilon)
=
\int_{-B_i}^{A_i}|r|^{-1+2\epsilon},dr
=
\frac{A_i^{2\epsilon}+B_i^{2\epsilon}}{2\epsilon}.
\]

Its Laurent expansion is

\[
J_i(\epsilon)
=
\frac1\epsilon
+
\log(A_iB_i)
+O(\epsilon).
\]

Thus the pole normalization and principal finite logarithm are both fixed by the source segment.

## Exact endpoint products

Entry 3829 gives the endpoint values of (R_1) and (R_2). Their absolute products are

\[
P_1=A_1B_1
=(y+z)(x-y-z)^2(x-y+z)(x+y-z)(x+y+z),
\]

\[
P_2=A_2B_2
=-(x+z)(x-y-z)(x-y+z)^2(x+y-z)(x+y+z).
\]

Both are positive in the strict triangle chamber.

At ((x,y,z)=(2,3,4)),

\[
P_1=4725,
\qquad
P_2=2430.
\]

Hence the principal finite terms are respectively

\[
\log4725,
\qquad
\log2430,
\]

multiplied by the corresponding oriented conductor coefficients from Entry 3832.

## Result

The local finite logarithmic scale is not arbitrary. It is supplied by the source endpoint geometry once the normalized analytic family is retained.

The complete finite wall period is not yet computed. Subtracting the constant singular coefficient leaves a nonsingular remainder whose analytically regulated integral contributes an additional, but still source-defined, finite term.

## Classification

- pole coefficient: conductor costalk residue;
- principal finite logarithm: source endpoint data;
- regular remainder: coefficient/readout integration still required;
- arbitrary cutoff scale: absent from the frozen source;
- new Carrier datum: none.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_conductor_principal_laurent_jet.py`
- `research/benincasa/results/rank26-conductor-principal-laurent-jet.json`

The checker passes six exact gates.

## Next falsifier

Perform the exact singular-subtraction decomposition of each full wall one-form:

\[
f_i(r)=f_i(0)+r,g_i(r).
\]

Integrate (g_i(r)|r|^{2\epsilon}) over the complete source segment and determine whether the finite remainder lies in the expected polylogarithmic coefficient field. Failure of integrability or dependence on a non-source scale would reject the canonical Laurent readout.

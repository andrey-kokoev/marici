# 894 — The Finite Five-Point Parke–Taylor Periods Obey the Source Sine Circuit

## Hard-to-vary claim

Fix the source cocycle

\[
\Phi=\operatorname{PT}(12345)
\]

and chambers \((12354),(13254),(14253)\). Their finite-\(\alpha'\) periods obey Mizera's source circuit

\[
\boxed{
Z(12354)
=
-\frac{\sin\pi(s_{12}+s_{23})}{\sin\pi s_{12}}Z(13254)
-\frac{\sin\pi s_{24}}{\sin\pi s_{12}}Z(14253).
}
\]

No circuit coefficient is fitted from the periods.

## Frozen common convergence point

Use

\[
(s_{12},s_{24},s_{13},s_{34},s_{23})
=
\left(\frac9{20},-\frac{17}{40},\frac{11}{8},-\frac{17}{5},\frac12\right),
\]

with all remaining invariants fixed by the source-free row sums. Relabel each chamber to \(0<xy<y<1\), retaining the fixed cocycle and ordered orientation. Every integral becomes

\[
\operatorname{sgn}(\beta)\int_0^1\!\int_0^1
x^{A_\beta-1}(1-x)^{B_\beta-1}
y^{C_\beta-1}(1-y)^{D_\beta-1}(1-xy)^{E_\beta}\,dx\,dy.
\]

The source-derived parameter table is

\[
\begin{array}{c|c|ccccc}
\beta&\operatorname{sgn}&A&B&C&D&E\\
\hline
12354&+&9/20&1/2&93/40&101/40&-21/40\\
13254&-&19/8&1/2&93/40&19/40&61/40\\
14253&+&5/2&23/40&101/40&19/40&53/40.
\end{array}
\]

For every row,

\[
A,B,C,D>0,
\qquad
B+D+E>0.
\]

Thus all three Euler integrals and their \({}_3F_2(1)\) reductions converge simultaneously. No branch phase is chosen numerically.

## Independent period evaluation

Each period is evaluated as

\[
\operatorname{sgn}(\beta)B(A_\beta,B_\beta)B(C_\beta,D_\beta)
{}_3F_2\!\left(
\begin{matrix}-E_\beta,A_\beta,C_\beta\\
A_\beta+B_\beta,C_\beta+D_\beta
\end{matrix};1\right).
\]

The circuit coefficients are evaluated only from the frozen Mandelstam point. The relative residual is

\[
1.84\times10^{-14},
\]

below the predeclared tolerance \(5\times10^{-13}\). The durable packet is at

research/benincasa/string-five-point-period-circuit.json.

## Narrow result

The first nontrivial finite-\(\alpha'\) Parke–Taylor period circuit closes with the source sine coefficients and source-labelled orientation.

This strengthens the preceding evidence:

- Entry 888 derived the exact coefficient circuit;
- Entry 889 checked its field-theory associated grade;
- Entry 891 fixed one finite-\(\alpha'\) period normalization;
- this entry verifies the complete finite-\(\alpha'\) circuit on a common convergence locus.

The result supports

\[
\boxed{
\text{fixed incidence carrier}
+
\text{Koba–Nielsen coefficient monodromy}.
}
\]

No new string-sector carrier cell or mixed resonance divisor is required.

## Scope boundary and next falsifier

This is a convergent representative of the meromorphic identity, not an explicit transport of Entry 891's original loading through a branch wall.

The next falsifier is monodromy-sensitive: continue one period around a single source letter divisor and verify that its half-monodromy phase and the sine circuit transform covariantly. Failure would locate missing data in the coefficient local system, not in the chamber carrier.

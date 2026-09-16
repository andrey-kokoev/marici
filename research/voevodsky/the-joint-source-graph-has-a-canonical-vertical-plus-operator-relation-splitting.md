# The joint source graph has a canonical vertical-plus-operator relation splitting

## Closed source relation

Let

\[
\mathscr G_S
=
\overline{
\{(i_{bulk}g,i_{end}g):g\in\mathcal C_S\}
}
\subset
\mathscr E_S\oplus\mathscr H_{end,S}.
\]

This is a closed linear relation from the bulk completion to the endpoint
completion.

## Vertical part

Define its multivalued or vertical part

\[
\mathscr V_S
=
\{e\in\mathscr H_{end,S}:(0,e)\in\mathscr G_S
\}.
\]

Because \(\mathscr G_S\) is closed, \(\mathscr V_S\) is a closed endpoint
subspace. It contains exactly the endpoint classes represented by source
sequences converging to zero in the bulk norm.

Let

\[
P_V:\mathscr H_{end,S}\to\mathscr V_S
\]

be the orthogonal projection and set

\[
\mathscr H_{op,S}=\mathscr V_S^\perp.
\]

## Single-valued operator part

For \((x,e)\in\mathscr G_S\), define

\[
T_Sx=(I-P_V)e.
\]

This is well-defined: if \((x,e_1)\) and \((x,e_2)\) lie in the relation, then

\[
(0,e_1-e_2)\in\mathscr G_S,
\]

so \(e_1-e_2\in\mathscr V_S\), and their projections to
\(\mathscr V_S^\perp\) agree.

Its domain is

\[
D(T_S)=\{x:\exists e, (x,e)\in\mathscr G_S\}.
\]

The graph of \(T_S\) is

\[
\mathscr G_S\cap
(\mathscr E_S\oplus\mathscr H_{op,S}),
\]

hence \(T_S\) is closed.

## Canonical decomposition

Every relation vector decomposes uniquely as

\[
\boxed{
(x,e)=(x,T_Sx)+(0,v),
\qquad
v=P_Ve\in\mathscr V_S.}
\]

Therefore

\[
\boxed{
\mathscr G_S
=
\operatorname{graph}(T_S)
\widehat\oplus
(0\oplus\mathscr V_S),}
\]

orthogonally in the endpoint coordinate. This splitting is canonical and
source-derived from the closed joint graph; no arbitrary section is selected.

## Bounded graph realization

Although \(T_S\) need not be bounded in the bulk norm, equip its domain with

\[
\|x\|_{T_S}^2
=
\|x\|_{\mathscr E_S}^2+
\|T_Sx\|_{\mathscr H_{op,S}}^2.
\]

Then \(D(T_S)\) is Hilbert and

\[
T_S:(D(T_S),\|\cdot\|_{T_S})
\to\mathscr H_{op,S}
\]

is contractive. Thus the nonvertical endpoint observation has a canonical
bounded realization after passing to the relation graph norm.

## Effect on the endpoint obstruction

The endpoint problem separates into two parts:

1. **operator part:** controlled automatically by the graph norm of \(T_S\);
2. **vertical part:** the finite-dimensional endpoint sector \(\mathscr V_S\),
   invisible to the bulk completion and therefore requiring its own signed
   metric treatment.

After even/odd endpoint diagonalization, the unresolved negative direction is
the odd component of \(\mathscr V_S\), not an unbounded coupling hidden in the
operator part.

## Revised positivity target

The Green form on \(\mathscr G_S\) can now be tested using the canonical
coordinates

\[
(x,T_Sx,v).
\]

The operator contribution is continuous in the graph norm. Positive rung-four
coherence reduces to the finite-dimensional vertical Schur condition after the
positive graph energy is retained.

This does not prove that vertical Schur condition, but it constructs the
previously missing source-derived splitting and localizes the remaining
obstruction to the vertical endpoint fiber.

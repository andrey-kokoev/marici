# 960 — The Barycentric Corner Hosts Diagonal Inertia Without an Exceptional Divisor

## Frozen refinement audit

Entry 21 predeclares, for every cyclic order \(\alpha\), the carrier

\[
C_*(\operatorname{sd}K(\alpha);\mathcal L_\alpha).
\]

The barycentric subdivision contains a vertex \(b(F)\) for every
associahedral face \(F\), including each codimension-two corner identified in
Entry 958.  It also contains the saturated incidence flags

\[
b(F)<b(F_1)<b(K(\alpha)),
\qquad
b(F)<b(F_2)<b(K(\alpha))
\]

through the two incident facets.

## What this refinement does not contain

The cellular barycentric subdivision is not the geometric log blowup of the
normal-crossing pair \(F_1\cap F_2\).  In particular, it does not add a new
codimension-one boundary divisor whose primitive normal is

\[
(1,1)
\]

and whose monodromy is \(mn\).

Entry 957's exhaustive facet census confirms this concretely: none of the
four product/ratio monodromies is a facet channel of any frozen chamber.

## Canonical existing home

The corner itself is nevertheless already a labelled carrier cell.  Its
normal link is the two-normal torus with characters \(m,n\).  Therefore the
diagonal character

\[
\chi_{(1,1)}=mn
\]

is legitimate coefficient data on the existing barycentric corner.

The four source factors are typed as

\[
\boxed{
(b(F),\mathcal K_{mn})
\quad\text{with resonance}\quad mn-1=0,
}
\]

not as four newly adjoined exceptional carrier facets.

This gives the complete carrier/coefficient classification:

\[
\begin{array}{c|c}
A_2,A_3,A_2B_{24},A_3B_{34}
&\text{codimension-one facet coefficients}\\
ZA_2,ZA_2B_{24},A_3/Z,A_3B_{34}/Z
&\text{diagonal Kummer coefficients on codimension-two corners}.
\end{array}
\]

## Consequence for H2

No new string-specific carrier stratum is required.  The source Fitting
support is compiled from:

\[
\text{existing associahedral faces and barycentric incidence}
+
\text{sector-specific Kummer characters of their normal tori}.
\]

This is direct evidence for the H2 architecture: shared carrier and
support-sensitive calculus, with layer-specific coefficient objects.

It is not yet an integral de Rham--Betti comparison theorem.  The coefficient
line \(\mathcal K_{mn}\), its primitive lattice, and its maps along the two
barycentric flags remain to be constructed from loaded chamber chains.

## Next falsifier

Construct the rank-one corner Kummer system with generator \(e_F\) and
monodromy character \((1,1)\).  Derive its two restriction/Gysin maps along
the saturated flags to \(F_1\) and \(F_2\), including orientations.  Test
whether the resulting barycentric two-leg complex reproduces the source
branch columns and their multiplicities without choosing a diagonal
exceptional divisor.

## Evidence

- frozen carrier: Entry 21;
- saturated-flag typing constraint: Entry 84;
- chamber and corner census: Entries 957–958;
- inertia type gate: Entry 959;
- allocator claim:
  `seqclaim-1fbdfc85472d42ff7bfacca1`.
- epistemic event:
  `ev-000000000577-ab3a5213-6622-470c-84fa-d203b65c703f`.

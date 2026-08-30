# The base-plus-curvature Green square closes exactly on every theta label

## Complete differentiated source

Let

\[
b_p=T_Lf_0,
\qquad
T_L=U_{-2L}-U_{2L}-U_{-L}+U_L.
\]

Define the complete source

\[
s_p
=
T_LPf_0+[P,T_L]f_0.
\]

By the commutator identity,

\[
s_p
=
PT_Lf_0
=
Pb_p.
\]

This equality uses both the transported base channel and all four curvature
increments.

## Half-density comparison square

For each theta label \(n\),

\[
\mathcal C\mathcal M_n
=
\mathcal M_nP.
\]

Therefore

\[
\mathcal M_ns_p
=
\mathcal M_nPb_p
=
\mathcal C\mathcal M_nb_p.
\]

Since \(\mathcal C\) has the bounded quarter-gap inverse,

\[
\mathcal C^{-1}\mathcal M_ns_p
=
\mathcal M_nb_p.
\]

Applying the inverse half-density chart gives

\[
\mathcal M_n^{-1}
\mathcal C^{-1}
\mathcal M_ns_p
=
b_p.
\]

Thus the complete Green comparison square commutes exactly at every label.

## Diagram

The source identity is

\[
\begin{array}{ccc}
s_p & \xrightarrow{\mathcal M_n} & \mathcal M_ns_p\\
\downarrow P^{-1} && \downarrow \mathcal C^{-1}\\
b_p & \xrightarrow{\mathcal M_n} & \mathcal M_nb_p.
\end{array}
\]

No fitted normalization or asymptotic argument enters this square.

## Ordered primitive

The Stieltjes difference satisfies

\[
d_p
=
-\frac12S_{\mathrm{ord}}b_p.
\]

Consequently,

\[
d_p
=
-\frac12
S_{\mathrm{ord}}
\mathcal M_n^{-1}
\mathcal C^{-1}
\mathcal M_ns_p.
\]

This closes the first Adams constructor at the one-label, one-prime level,
including the exact ordered inverse and integration constant.

## Why curvature alone failed

If \(s_p\) is replaced by \([P,T_L]f_0\), then the Green inverse returns only

\[
P^{-1}[P,T_L]f_0,
\]

not \(b_p\). The missing term is exactly \(T_LPf_0\). The completed square
therefore confirms the earlier base-channel audit.

## Labelwise versus synthesized equality

The identity above holds separately for every \(n\). Hence it defines a
diagonal equality on the retained theta-label carrier:

\[
\bigoplus_n
\mathcal C^{-1}\mathcal M_ns_p
=
\bigoplus_n
\mathcal M_nb_p.
\]

Scalar theta synthesis is not an inverse to this diagonal embedding. After
labels are summed, recovering one copy of \(b_p\) requires a declared
theta-label counit or readout.

Thus two claims remain distinct:

- labelwise constructor identification: proved;
- identification after scalar theta augmentation: requires a source counit.

## Renormalized completion

The Euler--Maclaurin wall packet makes the theta-label side converge in the
quarter-gap graph. Since the square is exact at every finite label and the
Green inverse is bounded, the equality passes to the renormalized labelled
completion.

Prime idempotents and the wall--jump observer commute with every arrow in the
square.

## Frontier

The first Adams edge is now constructed on the faithful labelled carrier. The
only remaining question before scalar Euler readout is:

> What source-authorized theta-label counit maps the completed diagonal orbit
> to the single Stieltjes boundary copy without erasing wall or jump data?

If no such counit is part of the source theory, then the Adams operator must
remain label-valued and scalar theta synthesis can only be an observer.

## Hostile

Sum the copies \(\mathcal M_nb_p\) and then apply an arbitrary left inverse.
Many left inverses can recover \(b_p\) on this one-dimensional orbit, but they
differ off it and need not preserve the Green, wall, or reciprocal
structures. Labelwise equality does not authorize a fitted scalar counit.

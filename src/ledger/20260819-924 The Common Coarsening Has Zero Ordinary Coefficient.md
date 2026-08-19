# 924 — The Common Coarsening Has Zero Ordinary Coefficient

## Legitimate carrier span

Entry 922 proves that the diagonal and off-diagonal maximal flags have no common refinement. They do have a common coarsening obtained by deleting their incompatible middle cuts:

\[
F_x=(s_{14},s_{23},s_{235})
\longrightarrow
F_0=(s_{14},s_{235}),
\]

\[
F_y=(s_{14},s_{35},s_{235})
\longrightarrow
F_0=(s_{14},s_{235}).
\]

In both ordered flags the deleted cut occupies slot one, so the simplicial incidence signs agree:

\[
\epsilon(F_x,F_0)=epsilon(F_y,F_0)=-1.
\]

This is the first carrier-typed span between the two branches.

## Source-normalized coefficient on the coarsening

Use the frozen normalized transition

\[
\widehat T_3
=
\sin(\pi s_{14})\sin(\pi s_{235}),T_3.
\]

The common face is reached by

\[
A_4\to1,
\qquad
Q\to1,
\]

while retaining the middle-channel variables as tangential data.

The exact two-order audit gives

\[
\operatorname{Sp}_{A_4,Q}\widehat T_3
=
\operatorname{Sp}_{Q,A_4}\widehat T_3
=0.
\]

All twelve matrix entries vanish. Thus

\[
\boxed{\operatorname{rank}\mathcal L_0^{(0)}=0.}
\]

## Consequence for the span

At ordinary grade the coefficient-enhanced carrier span is therefore

\[
\mathcal L_x^{(1)}
\longrightarrow 0
\longleftarrow
\mathcal L_y^{\rm Rees}.
\]

The two incidence maps exist at carrier level, with matching signs, but their ordinary coefficient targets vanish. They induce no comparison or cancellation between the two rank-one higher-normal objects.

This explains why the lines can both arise over the same coarsening while remaining independent: they are distinct normal derivatives of a zero ordinary coefficient, in incompatible middle-channel directions.

## Narrow conclusion

The first legitimate deletion span is typed but coefficient-trivial:

\[
\boxed{
\text{common carrier coarsening}
+
\text{zero ordinary coefficient}
+
\text{independent higher-normal directions}.
}
\]

No new carrier cell or mixed differential is required. Conversely, the vanishing target does not prove that all higher coherence vanishes.

## Next falsifier

Compute the first nonzero multigraded normal module of (widehat T_3) over (F_0), preserving separately the labelled (x), (y), and (z) directions. Test whether the carrier deletion maps induce a Koszul relation among those grades. Only such a relation could couple the diagonal and off-diagonal lines without introducing an incompatible carrier stratum.

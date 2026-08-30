# 2132 — The Fermat Quartic Glues to Three Coordinate-Soft Endpoint Thresholds

> **Superseded by Entry 2135.** These are boundary branches of the absent
> global-sum denominator. They are not the source component-resolved Landau
> packet.

## Hard-to-vary claim

The boundary stationary branches of the grade-three deletion sector are exactly the three coordinate-soft vertex thresholds

\[
\boxed{
E_T=\pm2(P_j+P_k),
\qquad \{i,j,k\}=\{1,2,3\}.
}
\]

They glue to the interior Fermat quartic when the corresponding external triangle angle equals `120 degrees`.

## Boundary critical values

The grade-three normal is

\[
E_T+2S=0,
\qquad
S=y_{12}+y_{23}+y_{31}.
\]

At the external vertex opposite side `P_i`, one loop distance vanishes and the other two are the adjacent external side lengths `P_j,P_k`. Hence

\[
S_i=P_j+P_k.
\]

The corresponding analytically completed threshold equation is

\[
E_T^2-4(P_j+P_k)^2=0.
\]

Each branch lies on an already labelled coordinate-soft boundary of the Cayley--Menger contour.

## Gluing to the interior branch

At angle `i=120 degrees`, the cosine law gives

\[
P_i^2=P_j^2+P_k^2+P_jP_k.
\]

The triangle area is

\[
\Delta=\frac{\sqrt3}{4}P_jP_k.
\]

Substitution into the Fermat formula from Entry 2131 gives

\[
S_F^2
=\frac12
\left(
P_1^2+P_2^2+P_3^2+4\sqrt3\Delta
\right)
=(P_j+P_k)^2.
\]

Thus the interior Fermat critical point reaches the coordinate-soft vertex continuously, and its quartic meets the endpoint threshold there.

## Complete grade-three support packet

The stationary support of the sum-of-distances pushforward consists of:

1. the interior Fermat branch
   \[
   \mathcal F_3=0;
   \]
2. three coordinate-soft endpoint branches
   \[
   E_T^2=4(P_j+P_k)^2;
   \]
3. deeper degenerations on the external triangle wall and ordinary soft intersections.

No published \(\mathcal Q\) factor is generated.

## Classification

The grade-three packet uses only:

- the existing Cayley--Menger boundary;
- its labelled coordinate-soft faces;
- sector-specific pushforward discriminants.

It therefore supports H2:

\[
\boxed{
\text{shared Carrier and support calculus}
+
\text{correlator-specific Landau coefficient data}.
}
\]

## Next falsifier

Compute the Hessian of the planar distance sum at a generic Fermat point and the relative Morse index against the Cayley--Menger orientation. This determines whether `\mathcal F_3` carries a simple fold vanishing cycle and fixes its local Picard--Lefschetz sign before any physical contour pairing is attempted.

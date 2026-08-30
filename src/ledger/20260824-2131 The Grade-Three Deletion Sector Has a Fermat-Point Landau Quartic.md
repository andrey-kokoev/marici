# 2131 — The Grade-Three Deletion Sector Has a Fermat-Point Landau Quartic

> **Superseded by Entry 2135.** The all-deleted graph is a product of three
> contact components. It has three component-energy denominators and no pole
> at `E_T+2(y12+y23+y31)=0`. The Fermat quartic is a valid geometric
> discriminant for an absent denominator and is not a cosmological result.

## Hard-to-vary claim

The correctly typed all-deleted correlator summand has an interior relative-Landau branch governed by the planar Fermat point of the external momentum triangle. Its source-derived quartic is

\[
\boxed{
\mathcal F_3
=
\left[E_T^2-2(P_1^2+P_2^2+P_3^2)\right]^2
+12\Lambda(P_1^2,P_2^2,P_3^2).
}
\]

This quartic is distinct from the published homogeneous algebraic-letter quartic \(\mathcal Q\).

## Correct source normal

The grade-three sector has one total-energy normal:

\[
E_T+2(y_{12}+y_{23}+y_{31})=0.
\]

On the Cayley--Menger boundary, the loop point is coplanar with the external momentum triangle. Tangency of the sum-of-distances hyperplane to that boundary is precisely stationarity of

\[
S=y_{12}+y_{23}+y_{31}
\]

as the planar point moves.

## Fermat branch

At an interior stationary point, the three unit vectors from the loop point to the triangle vertices sum to zero. Hence their pairwise angles are `120 degrees`.

Writing their lengths as `r_1,r_2,r_3`, the external squared side lengths are

\[
\begin{aligned}
p_1&=r_2^2+r_3^2+r_2r_3,\\
p_2&=r_1^2+r_3^2+r_1r_3,\\
p_3&=r_1^2+r_2^2+r_1r_2,
\end{aligned}
\qquad p_i=P_i^2.
\]

If `Delta` is the external triangle area, then

\[
S^2
=
\frac12
\left(
p_1+p_2+p_3+4\sqrt3\,\Delta
\right).
\]

Using `E_T=-2S` and

\[
16\Delta^2=-\Lambda(p_1,p_2,p_3)
\]

eliminates the area square root and gives `\mathcal F_3=0`.

## Exact verification

The Rust/Symbolica checker

`research/benincasa/marici-gm/src/bin/three_site_grade3_fermat.rs`

verifies identically that `\mathcal F_3` vanishes under the complete labelled `120-degree` parameterization above. It also computes the homogeneous specialization `P_i=X_i`, `E_T=X_1+X_2+X_3` and compares it coefficientwise with the frozen source formula for \(\mathcal Q\).

Their difference is nonzero. Since both are quartic in the homogeneous energy scaling, they are not related by a source-fixed scalar unit.

## Classification

\[
\boxed{
\text{grade-three translated normal}
+
\text{Cayley--Menger boundary tangency}
\longrightarrow
\text{Fermat-point coefficient discriminant }\mathcal F_3.
}
\]

No new Carrier incidence is required: the quartic is a pushforward discriminant of the frozen Cayley--Menger carrier and source port.

This is a legitimate successor-polynomial result in the \(\mathcal Q\) microprogramme, but it does not relocate the old \(\mathcal Q\).

## Scope

`\mathcal F_3` is the interior Fermat branch. The complete grade-three discriminant may also contain boundary stationary points when an external triangle angle is at least `120 degrees`; these must be derived separately and are expected to yield lower threshold factors.

The literal positive chamber still obeys `E_T>0`, `S>=0`, so `E_T+2S` cannot vanish there. Physical activation requires analytic continuation.

## Next falsifier

1. derive the vertex/boundary stationary branches and complete the grade-three discriminant;
2. compute the local Hessian at a generic Fermat critical point to determine fold multiplicity and Kummer/Picard--Lefschetz character;
3. test whether the source-prescribed analytic continuation gives a nonzero relative-cycle intersection.

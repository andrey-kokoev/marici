# 1838 — The Homogeneous Physical Orbit Avoids the Polar Soft Section

## Polar boundary equation

For the representative owner segment \([C_2,C_4]\), the polar boundary
condition from Entry 1837 is

\[
|\ell-C_1|+|\ell-C_3|=|C_2-C_4|,
\qquad
\ell\in[C_2,C_4].
\]

Regular-pentagon cyclic geometry gives

\[
|C_2-C_4|=|C_1-C_3|.
\]

The triangle inequality can therefore be saturated only if

\[
\ell\in[C_1,C_3]
\]

as well.

## Exact disjointness certificate

The supporting lines of \([C_2,C_4]\) and \([C_1,C_3]\) have scalar triple
product in the certified positive interval

\[
1.3143\ldots<
(C_1-C_2)\cdot
\bigl((C_4-C_2)\times(C_3-C_1)\bigr)
<1.3144\ldots.
\]

They are skew and cannot intersect.  Hence triangle equality is impossible.
Orientation reversal gives the other endpoint of the same segment, and cyclic
symmetry gives all four active-soft occurrences.

## Result

\[
\boxed{
\text{polar active-soft collisions on the frozen homogeneous slice}=0.
}
\]

Entry 1837 remains the correct local boundary type for dehomogenized
kinematics, but it is not activated by the present symmetric physical orbit.

## Architectural consequence

On the homogeneous slice, the physical logarithmic orbit remains wholly in
the clean open stratum of Entry 1834.  Neither the generic second-Rees soft
chart nor the polar Morse--Bott chart contributes at its exact threshold.

No new carrier datum is indicated.  The first possible soft activation can
occur only after a sufficiently large external deformation brings the two
focal segments into the required incidence.

## Next falsifier

Determine the codimension and equation of focal-segment intersection in the
dehomogenized external kinematics.  Test whether it is already a frozen Gram,
triangle, or soft carrier condition.  Only if it is independent of all such
conditions would it challenge the shared-carrier hypothesis.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_soft_exclusion.py`
- `research/benincasa/results/five-site-region-pair-polar-soft-exclusion.json`
- Entries 1836--1837
- allocator claim: `seqclaim-d979eefe1c6cc14191ef3a0f`

# Cross-family comparison retains a nonzero regular germ

Continue the four residue/pushforward squares along the common positive E target curve (e,1,1,1,1,1,3,2), centered at r=44/445. For each local sheet, retain the chi1^4 chi5^4 coefficient of the common target-chart eight-form as a Laurent record:

F_i(e) = P_i/(e-r) + A_i + O(e-r).

This is evaluation of an eight-form's scalar coefficient along a curve, not pullback of an eight-form to a one-dimensional manifold.

The exact computation uses reconstructed rational inverse sources, derivative of the common target chart, source-matrix derivatives and determinant logarithmic derivatives. If F_i=v_i/w2_i with v_i regular, w2_i(r)=0 and a_i=w2_i'(r) nonzero, then

P_i=v_i(r)/a_i,
A_i=v_i'(r)/a_i - v_i(r) w2_i''(r)/(2 a_i^2).

For each role EB and FB, the cross-family difference has zero pole coefficient but a NONZERO finite part. The sum of these two finite differences is also nonzero. Thus the families agree at the residue observer while retaining distinct regular component data at the same wall.

Store the directed comparison as the explicit additive difference of germ records. These records satisfy

(F_zero3_EB - F_zero2_EB) + (F_zero3_FB - F_zero2_FB)
 = (F_zero3_EB + F_zero3_FB) - (F_zero2_EB + F_zero2_FB)

at both retained Laurent orders. This supplies a commuting additive comparison square for the measured component: compare families then sum, or sum then compare. Every record and intermediate term remains available.

This is a concrete first-order comparison model in a vector space of scalar Laurent coefficients. A nonzero additive difference is not by itself a HoTT path or a chain homotopy; assigning such a witness requires a specified comparison category. Extending to a full multivariable superform germ and filling the proposed cube remains a further task. Here the meaningful residual is regular, despite the cancelled pole.

Checker: `research/nima/checkers/check_nine_point_cross_family_regular_germ.py`.
Result: `research/nima/results/nine-point-cross-family-regular-germ.json`.

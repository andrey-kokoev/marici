# History6 — full quotient Grassmann top bridge

At the operator's request, extend the full-component bridge rather than invent a lower-degree boundary map. Freshly read the top bosonization checker, owner supertwistor/exterior algebra and current work-net (pins v37).

## Universal normalized extraction

Choose four independent bosonic active columns M in support (1,2,3,5,6,8). Subtract their bosonic combinations from the two remaining columns. The six-dimensional bosonized determinant reduces exactly to

    det(Z_bosonized) = det(M)*det_2(sum_A phi_rA q_s^A),

where q1,q2 are the two residual fermionic linear forms. At reference Y0=[I2|0], the complementary four-bracket denominators are independent of phi and eta.

The universal Grassmann identity is

    [phi_top] det_2(sum_A phi_rA q_s^A)^4 / 2880
      = product_{A=1..4}(q1^A wedge q2^A).

Proof: treat the eight q_s^A as independent odd generators. The determinant's fourth power has degree eight in phi and degree eight in q. There is a unique top monomial in each set. The independent 2x2 exterior-algebra calculation fixes its coefficient 2880. Substitution of arbitrary odd linear forms proves the identity for all components, including independently chosen pairs in different SU(4) sectors. The normalization is not fitted from the generalized-R values.

## Full source comparison, not merely eta23

At each of three exact momentum-conserving fixtures, construct all source theta-to-chi coefficients and the Schur residual q forms. Impose supermomentum conservation separately in each SU(4) sector, eliminating eta7,eta8 using the invertible lambda7,lambda8 block. Compare the resulting six-variable two-forms with the owning outer/transported-inner generalized-R two-form:

- all fifteen reduced sector pair coefficients agree up to one nonzero derived scale;
- the source prefactor times scale^4 equals the bosonized Schur prefactor;
- all seventy unreduced lambda-augmented four-minor numerator comparisons agree independently;
- explicit mixed, non-diagonal SU(4) component controls agree.

The per-fixture sector scales are -405972815184, -958778479360, -14189433336000/7. These are basis changes derived from the two-forms, not adjustable normalization constants. The factorized polynomial identity certifies all 15^4=50625 degree-eight mixed quotient components at each fixture; this count describes certification by factorization, **not** a brute-force enumeration.

Since the omitted-update eta rows are unchanged, and the reference-plane c6 is phi-independent, multiplication by c6 and 1-c6 gives the full unupdated F0 and difference Ft-F0 quotient polynomials under the same extractor, not only their eta23 scalar images.

## Scope and remaining extraction gate

The Berezin/Schur identity is universal algebraically. Agreement with the owning generalized-R product is freshly verified at three nonsingular external fixtures; this is not a generic symbolic identity in all external kinematics. The explicit map acts at top degree eight and returns a quotient superfunction. It still supplies no degree-seven/six boundary Berezin or delta measure, nor a physical codomain retaining the exceptional direction. Applying it directly to the seven-form is still invalid.

All earlier local differential boundary and target-blowup witnesses, positive-endpoint split residuals, extra meromorphic pole and unavailable ordinary blowdown seven-form are preserved. No ordinary single-seed admission, global BCFW covering or weighted nine-form theorem is promoted.

Next: derive a degree-preserving boundary extraction from the source Grassmannian delta-integral or an explicitly source-authorized boundary superdistribution with its normal/delta measure and direction data. Alternatively extend the full external comparison to a generic rational identity. Both are nonredundant continuations.

Evidence: `checkers/check_history6_full_component_bridge.py`, `results/history6_full_component_bridge.json`. Attached as precursor evidence only; scientific node verdicts unchanged. Successor pins v38 and structural net/SCC checks are distinct from the actual full quotient calculation.

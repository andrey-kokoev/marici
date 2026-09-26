# Symbolic parity beyond the moment curve

Fresh checker `check_seven_point_symbolic_parity_surface.py` proves full parity equality over Q(u,v) with Z_i=(1,i,i^2,i^3) for i=1,...,6 and Z_7=(1,7,u,v). Unlike the previous one-parameter curve, arbitrary u,v move the seventh twistor off that curve. All420 entries of the common single-flavor embedding vanish exactly, and all15 reduced symmetric quartic identities vanish exactly. No interpolation, probability, or finite sampling is used to prove these equalities. The uniform moment-curve point only selects a regular basis.

The result is recorded in results/seven-point-symbolic-parity-surface.json with all weights and reduced coordinates. Scope remains a two-parameter family, not generic kinematics.

To make that distinction precise, `check_seven_point_kinematic_chart.py` constructs projective invariants by expressing each free point in the first-four-twistor frame and normalizing against the fifth point. Their Jacobian has rank2 on the proved surface. Thus u and v are genuinely independent projective shape parameters, not gauge motions.

The same checker supplies a six-modulus generic chart: fix the first five twistors to their moment-curve values and take Z_6=(1,a,b,c), Z_7=(1,d,e,f). Five general projective points fix PGL(4); the six remaining affine coordinates have a nonzero symbolic six-dimensional invariant Jacobian. The checker records that determinant in results/seven-point-kinematic-chart.json. This establishes a concrete domain for the remaining generic proof, not that proof itself.

Fresh commands: both named checkers under uv run --with sympy python. Both pass.

Next expand the amplitude identities to the full six-modulus chart, preferably exploiting the three-dimensional supersymmetric quotient before computing large minors. A staged three-parameter seventh-twistor proof is executable, but will still leave the sixth-twistor moduli fixed. Neither a dimension count nor additional slices alone can establish the generic rational identity.

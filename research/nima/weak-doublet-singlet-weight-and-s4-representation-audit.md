# Weak doublet/singlet weighting and S4 representation audit

## Outcomes

1. On the ordinary SM matter space, a common positive doublet weight d and singlet weight s produce sin^2(theta)=3d/[4(d+s)] under common inverse-trace normalization. The candidate 3/13 requires s/d=9/4.
2. The cited four-point permutation carrier does not supply the asserted doublet/singlet split. Its representation is 1+3, not 1+sign+2.

## Weighted matter calculation

Per generation, weak doublets contribute weak trace 2 and hypercharge trace 2/3. Weak singlets contribute weak trace zero and hypercharge trace 8/3. Apply the same weight operator to both gauge traces:

    C2 = 2d,
    CY = (2/3)d + (8/3)s,
    C2/(C2+CY) = 3d/[4(d+s)].

Solving for 3/13 yields s/d=9/4. This is a required weight ratio, not an independently selected carrier value. A weight is per matter state; it is not the total number of singlet or doublet multiplets.

## Representation audit

The source research/nima/foundational-derivation-boolxbool-to-gram.md section 7 identifies the natural four-point permutation representation of S4 with 1+sign+2. A transposition fixes two of the four points, so its natural character is 2. In the proposed sum its character is 1-1+0=0. The representations therefore differ.

The exact checker enumerates all 24 permutations. It constructs the two-dimensional irrep character from the action on the three partitions of four points into unordered pairs, subtracting the constant line. Nine group elements distinguish the claimed sum from the natural permutation representation. The actual natural representation splits into its constant line and the three-dimensional sum-zero standard representation.

Consequently a doublet/singlet physical realization requires a separate representation or a specified symmetry reduction and action. A four-dimensional space having the same dimension as 1+sign+2 is insufficient to identify their group actions. Choosing a different representation remains possible; the carrier-to-representation map must be constructed.

## Witness-stabilizer construction

Fix carrier point 0 as the witness. Its stabilizer is S3, permuting the other three points. The natural representation restricted to this subgroup splits as 1+1+2. Explicit orthogonal sectors are:

- uniform line u=(1,1,1,1);
- witness-versus-remainder line v=(3,-1,-1,-1);
- contrast plane H={x: x_0=0, x_1+x_2+x_3=0}.

Both lines are trivial S3 representations; the plane is its standard two-dimensional representation. This is an actual witness-induced split. It does not assign hypercharges or identify the finite S3 action with physical SU(2).

For self-overlap 12 and mutual overlap 1 the Gram is G=11I+J, with J the all-ones matrix. It acts by 15 on u and 11 on v and H. (Writing G=12I+J would instead give diagonal 13.)

An S4-invariant positive weight has eigenvalues a on u and b on its orthogonal complement. If the two fixed lines are additionally identified as equally represented singlet states, their mean weight is (a+b)/2; the contrast-plane weight is b. This provisional identification gives s/d=(a+b)/(2b). The identity, Gram, and inverse-Gram choices give ratios 1, 13/11, and 13/15 respectively. The required 9/4 would demand a/b=7/2. No such ratio is selected by those three choices.

If only S3 invariance is required, the two trivial lines admit an arbitrary positive 2x2 weight block, while the irreducible plane has a scalar weight. Thus symmetry alone leaves additional freedom rather than selecting 9/4. The physical matter multiplicities are also additional to this four-dimensional representation.

Exact checker research/nima/checkers/check_witness_stabilizer_doublet.py verifies invariance and Gram actions for all six stabilizer permutations, and the rational weight ratios.

## Explicit weak and hypercharge actions

Complexify the witness-fixed decomposition and use an orthonormal basis (u,v,h1,h2). The unitary transformations preserving each of its three sectors form U(1) x U(1) x U(2). This supplies a possible continuous extension of the sector structure. Gauging it and identifying its action on physical matter are further choices.

Choose weak generators zero on the two lines and sigma_a/2 on the contrast plane. Every commuting Hermitian hypercharge generator has the form

    Y = [[B, 0], [0, y_d I_2]],

where B is a Hermitian 2x2 operator on the weak-singlet space. Requiring preservation of the two separately named lines (or commutation with the nondegenerate Gram eigenvalues on those lines) reduces this to diag(y_0,y_w,y_d,y_d).

With unit comparison measure, the weak trace per generator is 1/2 and the hypercharge trace is y_0^2+y_w^2+2y_d^2. The conditional inverse-trace mixing fraction is

    (1/2)/(1/2 + y_0^2+y_w^2+2y_d^2).

The same geometry therefore admits multiple fractions. Charges (0,0,1/2) give 1/2; (1,0,1/2) give 1/4; the target-selected example (1,2/3,1/3) gives 3/13. The latter merely exhibits a possible solution, with no claimed physical matter or anomaly properties. Compact U(1) additionally requires a charge-lattice normalization; a common rescaling can make each rational example integral, with the coupling convention adjusted accordingly.

Outcome: the witness split permits explicit weak and commuting charge actions, but leaves hypercharge eigenvalues and the kinetic/comparison metric undetermined. The four-dimensional sector space is not the full Standard Model matter representation. The algebraic construction therefore localizes the remaining input: a carrier-selected charge operator, its normalization relative to weak generators, and its lift to physical matter.

Exact checker: research/nima/checkers/check_witness_gauge_assignment.py. It verifies the trace values and orthogonality to T3 for the displayed diagonal actions. It does not test anomalies or physical gauge dynamics.

## Carrier-defined centered witness charge

With the Euclidean metric on carrier coordinates, the witness supplies a rank-one projector P_w. A direct traceless candidate is Y=P_w-I/4. It has charges (3/4,-1/4,-1/4,-1/4), assigning one value to the witness and another to its complement. It acts as -I/4 on the contrast plane and commutes with its weak action. Its squared trace is 3/4. Under the same unit-measure inverse-trace ansatz the mixing fraction is (1/2)/(1/2+3/4)=2/5.

This candidate mixes the uniform and witness-contrast lines in the adapted basis and fails to commute with G=11I+J. It therefore does not generate a unitary symmetry preserving that fixed Gram. If the Gram is dynamical or symmetry-breaking, a transformation rule and action would be needed instead.

The primitive integral normalization 4Y has charges (3,-1,-1,-1), squared trace 12, and gives 1/25 if the same common kinetic-normalization coefficient is held fixed. This exposes another unresolved choice: in physical gauge theory, Y->cY accompanied by g'->g'/c is a convention change preserving g'Y. A common inverse-trace ansatz must specify its embedding/kinetic metric to define the physical comparison with the weak coupling. Holding the ansatz fixed while rescaling Y is a different relative-normalization model, not a new observable from a change of units.

Achieving 3/13 by scaling this centered witness charge alone requires c^2=20/9. That factor is solved from the target. No carrier principle selecting it was found in the inspected source.

Outcome: the witness constructs a concrete charge-like operator. The operator fails both the fixed-Gram symmetry test and the 3/13 normalization target under the stated choices. The investigation now needs the gauge action and its kinetic/comparison metric; counting additional slots cannot select them.

Exact checker: research/nima/checkers/check_witness_charge_operator.py verifies the trace, contrast-plane action, Gram noncommutation, and normalization fractions.

## Gram-preserving charge family and kinetic freedom

Spectrally project the centered witness charge onto the commutant of the Gram: E(Y)=P_u Y P_u+(I-P_u)Y(I-P_u), where P_u projects onto the uniform line. In the adapted orthonormal basis this yields diag(0,1/2,-1/4,-1/4). Its squared trace is 3/8 and the conditional unit-trace mixing angle is 4/7. This operation repairs fixed-Gram compatibility, but does not recover 3/13.

All traceless Hermitian charges commuting with both the fixed Gram and the chosen weak action have the form

    Y = x Q0 + y Qw,
    Q0 = diag(3,-1,-1,-1),
    Qw = diag(0,2,-1,-1).

Their Euclidean trace metric is Tr(Q0^2)=12, Tr(Qw^2)=6, Tr(Q0 Qw)=0. Therefore Tr(Y^2)=12x^2+6y^2. With weak trace 1/2, the 3/13 target asks for the ellipse 12x^2+6y^2=5/3. Symmetry provides this family and its metric; it selects no point on the ellipse. Compact charge-lattice conditions constrain possible directions but do not supply the relative kinetic coefficient.

There is also kinetic freedom even after fixing a charge generator. For a chosen weak SU(2) and hypercharge U(1), gauge invariance permits independent positive kinetic coefficients k2 and kY, with g^2=1/k2 and g'^2=1/kY in a fixed generator convention. The angle is k2/(k2+kY). For the larger two-Abelian-direction family, a positive 2x2 Abelian kinetic matrix, including offdiagonal mixing, is permitted. A universal trace coefficient is an additional dynamical ansatz rather than a consequence of gauge invariance.

Outcome: the complete traceless Gram-preserving charge family has been constructed. It leaves the hypercharge direction and kinetic metric undetermined. Deriving an action, matter-induced kinetic term, or other independently specified carrier weighting is the next required source calculation. The present structural data cannot predict a unique weak angle. This is the endpoint of the symmetry-only branch.

Exact checker: research/nima/checkers/check_gram_preserving_charge_family.py verifies the pinched witness charge, trace metric, and general-family formula.

## Gauge kinetic forms built from the Gram

Consider an explicitly postulated gauge kinetic form with B_W(X,Y)=Tr(WXY), W=f(G)>0. In the adapted basis W=diag(a,b,b,b), where a=f(15), b=f(11). For generators commuting with G the form is gauge invariant. The construction supplies an allowed kinetic form; a dynamical principle must still select it.

For the Gram-compatible witness charge Y=Qw/4:

    k2 = B_W(T3,T3) = b/2,
    kY = B_W(Y,Y) = 3b/8,
    sin^2(theta) = k2/(k2+kY) = 4/7.

This holds for every positive spectral function f, including identity, Gram, inverse Gram, and Gram squared. Thus tuning a function of the Gram alone cannot change this candidate's fraction to 3/13. The cancellation follows because both relevant generators are supported inside the same eigenvalue-11 subspace.

For the full charge family x Q0+y Qw the kinetic norm is (9a+3b)x^2+6b y^2, with zero cross term. The free hypercharge direction remains and is not fixed by adopting a spectral trace form.

A different suggested construction based on Tr([X,G]^dagger[X,G]) vanishes on all selected weak and hypercharge generators, since they commute with G. It therefore supplies no nondegenerate kinetic metric for these gauge directions. Such a commutator term can instead characterize response to changes of the Gram or symmetry-breaking directions; a gauge-field curvature term needs additional connection/dynamical data.

Outcome: the pinched-witness charge plus any positive Gram spectral kinetic weight predicts 4/7. The symmetry-preserving commutator response is zero. An induced matter kinetic term returns to the matter representation, charge assignments, and scale dependence audited earlier. Further progress requires an independently constructed matter action or connection dynamics; neither a new power of G nor slot arithmetic supplies it.

Exact checker: research/nima/checkers/check_gram_gauge_kinetic_weights.py. All trace identities and commutator support checks pass. The general spectral-function statement follows algebraically from the two eigenspaces.

## Next object

Specify the physical matter representation supplied by the carrier and its positive comparison-weight operator W. Then derive the doublet/singlet weight ratio independently of the angle. This would supply a genuine test of the required 9/4 ratio. The natural four-point permutation action alone supplies neither that split nor that weight ratio.

## Verification

research/nima/checkers/check_carrier_doublet_singlet_split.py passes exact character and rational-weight checks, writes no artifacts, and leaves historical sources unchanged.

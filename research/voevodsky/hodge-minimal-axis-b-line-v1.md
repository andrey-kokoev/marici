# Global iteration 44, fifth series 3/10: a parameter-line CM-factor screen

## Outcome

Vary b in

    W:y^2=x(x-1)(x-2),
    g_b=(y+b(x^2-2))/(x^2-4x+2),
    V_b/W: w^2=g_b^3-g_b.

This fixes lambda=2,a=4, not the whole scalar family. The complete regular-chart census at17 gives:

| b modulo17 | conclusion |
|---|---|
|2,15|no extra E_i in the complementary sevenfold; excludes the corresponding algebraic congruence classes from Y3 even up to complex isogeny|
|3,6,11,14|extra E_i-type Frobenius roots exist in reduction; these classes survive this necessary screen only|
|0,1,16|infinity is a special branch value; outside the quartic chart used here, NOT excluded|
|4,5,7,8,9,10,12,13|the displayed regular reduction chart fails; NOT excluded as complex sources|

The rational lifts b=3 and b=6 actually give smooth C17/D9/B5 sources with primitive theta-four axes, by the same explicit construction as iteration42. Their second complex CM axes, theta degrees, End, X6/Y3 match and cycles remain uncomputed. Surviving reduction is not a lifting theorem.

## 1. What the chart certificate means

Write P=x(x-1)(x-2), D=x^2-4x+2, N_b=b(x^2-2) and F_c=P-(cD-N_b)^2 for c=0,1,-1. For every b in F17, the checker first separates b=0,+1,-1. At those values a special fibre meets W's infinity; its finite elimination polynomial has degree3 rather than4. These may be legitimate smooth sources in a different chart. They are not called singular or excluded.

For all other b it tests that all F_c retain degree4, are squarefree and coprime to P, and that D and F_0 are coprime. The fixed D is squarefree and coprime to P, as already verified by the preceding source and arithmetic checkers. The regular residues are exactly2,3,6,11,14,15. All remaining residues merely fail this sufficient displayed good-model certificate. No minimal-model or potential-good-reduction conclusion is drawn for them.

Over Q, separate exact Euclidean gcd tests verify the same conditions for the literal lifts b=3,6. The identity x^2 N_b(2/x)=-2 N_b(x), together with the fixed D identity, proves g_b(p+k)=-g_b(p). Thus the SAME T, tau and order-four kappa from iteration42 give C_b=T times_W V_b, free rho(t,w)=(t+kappa,i w), genera17/9/5 and the degree-two ramified-to-principal Prym isogeny. The map to E_i has degree8 and theta degree4. The earlier primitivity proof uses only these genera, the degree-two map to T and the anti-action of h, not b=2: a nontrivial elliptic isogeny factor would give a birational pair of elliptic maps of degrees2,d<=4 and genus at most9, contradicting17. The resulting theta-four axes are therefore actual primitive axes, not degrees assigned before saturating a kernel.

## 2. Counts and full polynomials

The new crate-free Rust counter includes the existing checked field kernel without modifying it. It enumerates ordinary AND rho-Frobenius fixed points for ALL six regular residues over F17^n, n=1,2,3,4:24 rows of both counts. Full primitive-generator cycles verify each field. Infinity is counted using g_b(infinity)=b. The nonsplit two-isogeny torsor and fixed-fibre formula are those proved in iteration43; they do not depend on b=2. The base torsor count is checked against #W in every extension.

Independent digitwise Python arithmetic enumerates ordinary degree1,2 counts and directly tests the rho Frob17 fixed-point equations inside F17^4 for b=2,3,6. It does not reuse the Rust torsor parametrization. On V, (p,w)->(-p,i w) identifies the reductions for b and-b and commutes with rho; the six separately counted profiles verify these sign pairs.

Subtract the known beta=1+4i axis. The four Gaussian power traces recover a1,...,a4 of the degree-seven K-character polynomial. In all cases a3 is nonzero, so unitary reciprocity gives a7=17^3*a4/conjugate(a3), then a5,a6. Gaussian integrality, all reciprocal identities, and the rational norm polynomial are checked. These are complete polynomials by the same proved reconstruction as iteration43, not an interpolation claim for four ordinary traces. A fifth count is not claimed for the new cases; only the old b=2 control inherits iteration43's unused fifth-trace validation.

For b=3 the rational characteristic polynomial's descending coefficients are

    [1,-6,27,-124,361,-954,2907,-2312,49419,-275706,
     1773593,-10356604,38336139,-144825414,410338673].

For b=6 they are

    [1,-6,59,-188,953,-1690,7915,-14536,134555,-488410,
     4682089,-15701948,83771563,-144825414,410338673].

The b=2,15 profile reproduces the previous rejected control exactly. All six Gaussian and rational polynomials and complete certificates are retained in the receipt.

## 3. Complete CM-factor certificates, including positive factors

For each rational polynomial F, form N(U)=F(beta U)F(conjugate(beta)U), degree28. As before, every root-of-unity CM ratio has order m with phi(m)<=28, hence m<=1568. All55 orders including1 are considered.

Unlike iteration43, some cyclotomic factors now genuinely divide N. The checker extracts them by EXACT integer monic division, recording multiplicity. It then proves the residual coprime to every one of the55 cyclotomic polynomials by modular gcd witnesses. A failed modular exclusion is not treated as positive evidence: positive factors require exact division. This gives the COMPLETE cyclotomic part, not merely a list of factors found.

For b=2,15 it is empty. For b=3,14 it is Phi_2^2*Phi_4. For b=6,11 it is Phi_1^6. Because beta/conjugate(beta)=(-15+8i)/17 is not a root of unity in Q(i), no Frobenius root is counted in both ratio orientations. Half the cyclotomic degree is thus the E_i isogeny multiplicity of Q7 over F17bar: respectively0,2,3. This finite-field interpretation uses the standard semisimple Tate isogeny category; it is NOT a complex Hom computation.

Exact synthetic division of the Gaussian polynomial accounts for every CM root:

| representative b | roots in the native i-character polynomial of Q7 |
|---|---|
|2|none|
|3|-i*beta once; -conjugate(beta) once|
|6|beta once; conjugate(beta) twice|

These identify both beta-unit and conjugate-beta-unit arithmetic types in the surviving reductions. They do not compute a restricted theta degree or produce a primitive opposite-character axis over C. Including the known first axis, the reduced source has E_i multiplicity1,3,4 respectively; desired complex multiplicity2 is still possible for the latter two, since specialization may INCREASE Hom.

## 4. The new characteristic-zero exclusion really is a congruence-class result

Let b be algebraic, integral at a place above17, with residue2 or15. All regular-chart tests are units there. The family therefore has the same good special fibre as the excluded b=2 or15 control, after extending the residue field. Its complementary sevenfold still has no geometric E_i factor in reduction.

A complex extra E_i factor would descend to a finite extension of the number field of definition. Nonzero Hom specializes faithfully at good reduction, contradicting the special fibre. Hence every such algebraic b is excluded from the fixed Y3 isogeny class, not only the literal b=2. For rational integral b, this excludes b=2 or15 modulo17. No statement is made about transcendental b without such a number-field specialization setup.

Conversely a special fibre containing E_i factors gives only an upper bound on generic Hom, never their lift. Thus b=3,6 remain candidates, not identified targets and not rejected merely because their reductions have more CM factors than Y3. No reduction of the fixed transcendental-period X or Y3 is needed for the negative direction; their known E_i multiplicity2 suffices.

## Next executable gate and scope

Test the literal new sources b=3 and b=6 at another certified good split prime before attempting to lift the opposite-type elliptic factor. If a control survives multiple necessary screens, construct an actual opposite-character map and verify its primitive theta degree6 and joint kernel. Then the complementary X6, principal period/correspondence matching and denominator768/four-channel transfer gates remain. Alternatively vary a/lambda or analyze the three infinity-branch residues with a correct projective chart. The birational genus-five-image route remains open.

Contract: `research/conjecture_net/contracts/hodge-minimal-axis-b-line.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_minimal_axis_b_line.py`, `count_hodge_minimal_axis_b_line.rs`.
Data: `research/voevodsky/inputs/hodge-minimal-axis-b-line-v1/counts.json`.

Trust: written projective-family, primitive-axis, Gaussian reciprocity, finite-field CM-factor and faithful-Hom specialization arguments, complete finite counts, independent small counts, exact divisions and exhaustive modular certificates. Standard abelian-variety facts are imported, not proof-assistant verified or independently reviewed. Iteration43 and pins v1-v46 remain immutable. No complex CM lifting, End computation, family-wide exclusion, target cycle or Hodge verdict is supplied.

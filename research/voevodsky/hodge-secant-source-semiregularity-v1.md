# Global iteration 33 (fourth series 2/10): a source-level weak-semiregularity obstruction

## Scoped rejection

Keep the corrected d=9 **perfect complex E on the auxiliary ppav fourfold A0**, under iteration32's transverse-incidence hypotheses. It has306 normalized isolated nodes. This turn shows that the source-complex analogue of the proposed weaker semiregularity criterion fails:

    sigma_E restricted to im(ev_E:HH^2(A0)->Ext^2(E,E)) is not injective.

In fact its kernel on that image has dimension at least two. Thus ordinary injectivity of sigma_E also fails for this source complex. This does not refute Question11.4, which asks for a deformation theorem under a hypothesis; it shows that this particular source object does not satisfy the hypothesis's analogue for perfect complexes. The actual eightfold transformed object has not been evaluated here.

The witness includes a bivector/noncommutative direction and a gerbe/B-field direction. It does **not** prove that all ordinary complex-structure Hodge-locus deformations are obstructed. Nor does nonzero evaluation assert that a particular geometric deformation has a nonzero obstruction. These distinctions are part of the contract.

## 1. Global character action and a six-dimensional family of annihilators

Write t=[Theta] and

    ch(E)=1+3t-(9/2)t^2-(9/2)t^3+(27/8)t^4
         =a exp(s t)+b exp(-s t), s^2=-9.

On an abelian fourfold, Todd=1 and the HKR space is

    HH^2=H^2(O) direct_sum H^1(T) direct_sum H^0(wedge^2 T),
    dimensions 6+16+6=28.

Use the standard HKR action on Hodge cohomology: B-fields wedge, Kodaira-Spencer tensors wedge/contract, and bivectors contract twice. For any global holomorphic bivector beta, define

    gamma_beta=(1/2) contraction_beta(t^2) in H^2(O).

The exponential identity, or the coefficient recurrence c_(q+2)*(q+2)*(q+1)=-9*c_q, gives

    contraction_beta ch(E) = -9 gamma_beta wedge ch(E).

Therefore

    xi_beta=(9 gamma_beta, 0, beta) in HH^2
    satisfies xi_beta acting on ch(E)=0.

This uses the complex Hochschild deformation space; no rationality of beta is required. The finite exterior calculation chooses t=sum x_i wedge y_i for four holomorphic and four antiholomorphic generators, verifies all six basis bivectors, and computes the full character-action rank12, hence annihilator dimension16. The compensation sign is tested: replacing9 by8 fails.

## 2. The same direction evaluates nontrivially at a normalized node

Choose one normalized node p. Its transverse local parameters a,b,c,d and iteration32's free model give E locally in degrees-1,0,1:

    R^2 --Dminus1--> R^4 --D0--> R,
    Dminus1=[-b  0], D0=[-a -b c d].
            [ a  0]
            [ 0 -d]
            [ 0  c]

The top local self-Ext is k^2, the quotient of Hom(R^2,R)=R^2 by mR^2. For a free complex over a smooth ring, the Atiyah class is represented by derivatives of its differential. The local HKR bivector evaluation is its antisymmetrized Atiyah square, up to a universal nonzero normalization factor. Modulo m this has rows

    (partial_a D0)(partial_b Dminus1)
      -(partial_b D0)(partial_a Dminus1) = [2,0],
    (partial_c D0)(partial_d Dminus1)
      -(partial_d D0)(partial_c Dminus1) = [0,-2].

Mixed pairs vanish. Thus the two evaluations are independent nonzero local Ext classes. Since A0 is abelian, evaluation of translation-invariant global holomorphic bivectors at p is an isomorphism onto wedge^2 T_p A0. Choose global beta values partial_a wedge partial_b and partial_c wedge partial_d at p. Only their values at p matter for this finite-length quotient, not how these vector fields are expressed away from p in the chosen local parameters.

The H^2(O) component of xi restricts to zero as an Ext action on the formal affine local ring: its representative is a global degree-two O-cohomology class. Hence it cannot cancel either displayed local bivector class. Consequently ev_E(xi_beta) is nonzero globally, and the two chosen global evaluations are independent because their local restrictions are independent.

## 3. Trace compatibility proves the criterion fails

Use the standard Atiyah-Chern trace compatibility for a perfect complex on a smooth variety:

    sigma_E composed with ev_E = HKR action on ch(E).

The retained Markman survey, PDF p20, Lemma11.3 and its proof, describes this diagram and its relevance to Question11.4. Applying the identity to perfect complexes uses the usual finite locally free resolution and derived trace, not a claim that our E is a sheaf. The local derivative representative, HKR compatibility and trivial Todd correction are explicit mathematical imports in this written argument; the checker is not a proof assistant for them.

For the xi_beta above the right side vanishes, but the evaluations are independent nonzero classes. This proves a kernel of dimension at least two on im(ev_E). Since the character-action image has dimension12, rank(ev_E)>=14. We have not computed its exact rank or the dimension of all global Ext^2.

As an independent numerical control, Hirzebruch-Riemann-Roch gives

    chi(E,E)=integral ch(E dual)ch(E)=1296.

The checker evaluates the top coefficient exactly. This Euler characteristic is not a dimension of one Ext group. The previous sheaf-Ext length1116 is not used as a global dimension either.

## 4. What this does and does not rule out

Reject the direct assertion that the corrected **source fourfold complex** already satisfies the full-HH^2 weaker criterion. Merely repairing the character and then invoking that criterion on E is insufficient: the criterion actually fails here.

A derived equivalence on a fixed category transports the Hochschild action/evaluation compatibility, so re-expressing the same object by an equivalence cannot repair this criterion. However, a full higher-dimensional construction may involve external products, different objects, quotients or restrictions to a smaller deformation problem. This turn does not assert that every such operation retains the exhibited kernel, or that the precise eightfold object has been constructed and tested. Those require their own maps and hypotheses.

Next specify the actual eightfold construction and test whether these explicit evaluation classes persist. If they do, this candidate's use of the proposed criterion is rejected there too; if a different construction removes them, identify the mechanism and the valid deformation theorem. Alternatives include different secant objects, a theorem for a smaller commutative deformation locus, actual ramified generalized-Prym target matching, and direct non-divisor cycles.

The fixed X/alpha/Y2, all cycle transfers and previous conditional censuses are unchanged. No actual target cycle, target cover, all-cycle obstruction, Hodge verdict or independent review results.

## Verification

Contract: `research/conjecture_net/contracts/hodge-secant-source-semiregularity.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_secant_source_semiregularity.py`.
Receipt: `research/voevodsky/results/hodge-secant-source-semiregularity-v1.json`.

The checker retains the prior source/local receipts freshly, computes the exact28-column exterior action and rank, checks all compensated bivectors, and computes the local derivative compositions. The universal interpretation is supplied by the written HKR/Atiyah argument, not by a finite search. Iteration32 and immutable pins v1-v34 are preserved.

# Comparison-slot normalization and carrier closure residual

## Hypothesis

The integer comparison count describes an abstract carrier comparison. Its physical realization retains a reference relationship and must close coherently with its carrier environment. The resulting closure residual modifies comparison weights without changing the number of slots. Cosmological curvature and the noninteger electromagnetic normalization are proposed to be different readouts of that same residual structure.

This is a hypothesis developed from the operator's comparison-slot interpretation, not a recovered earlier theorem.

## Comparison domain

Two T1 carriers are compared relative to their direct relationship. That relationship supplies the reference and is excluded from the counted domain. Each carrier contributes eleven remaining arrows and four state values (Bool x Bool).

The proposed domain is the disjoint union of 121 arrow-arrow slots and 16 state-state slots. Its cardinality is 137. Here 4 squared and 2 to the fourth power count the same ordered pairs of two-bit states. The two blocks are alternatives, not state labels independently attached to every arrow pair.

T0 retains identities; T1 carries relationships and witnessed round-trip agreement; T2 carries coherent extension. These labels denote relational levels, not powers of time. Neither this construction nor its orientation requires physical chirality.

## Abstract versus carrier-realized normalization

Give each abstract slot unit normalization weight. Then Z_EM = 137 and the normalized weight of a unit comparison is 1/137.

For a realized carrier let the slot weights be w_s = 1 + epsilon_s. The proposed electromagnetic normalization is

    Z_EM = sum_s w_s = 137 + sum_s epsilon_s,
    alpha = 1 / Z_EM.

This introduces two explicit hypotheses: physical realization modifies the normalization weights, and the electromagnetic reference channel remains unit-normalized. Individual normalized slots have weights w_s/Z_EM, not necessarily 1/Z_EM. In particular, the arithmetic mean of all 137 normalized slot weights remains exactly 1/137. The decimal tail concerns the inverse total normalization, not a change in that arithmetic mean.

Using the rounded low-energy value alpha^-1 = 137.036 requires

    sum_s epsilon_s = 0.036,
    mean_s epsilon_s = 0.036/137 = 0.0002627737.

These are target constraints, not independently calculated carrier weights. No fractional comparison slot is added.

## The existing cosmological residual

Source: research/nima/checkers/check_cosmological_sum_closure.py.

The checker defines

    Omega_b  = 6/121,
    Omega_DM = 6/23,
    Omega_de = 11/16.

Their closure deficit is exactly

    kappa = 1 - Omega_b - Omega_DM - Omega_de
          = 91/44528
          = 0.002043657923104563.

The source proposes identifying this deficit with Omega_k. It is a budget-closure calculation, not a calculation of stochastic variance.

A shared-residual hypothesis posits an underlying carrier residual R and two readouts:

    P_cos(R) = kappa,
    P_EM(R)  = (Z_EM - 137)/137.

The maps must come from the respective comparison constructions. Equal underlying residual does not mean equal numerical readouts.

## Numerical test of a common scalar normalization

If the cosmological deficit simply reduced electromagnetic normalization efficiency by the same factor, the prediction would be

    alpha^-1 = 137/(1-kappa) = 137.28055449287757.

That does not produce 137.036. Therefore the shared-residual hypothesis requires a sector-dependent readout, not a universal multiplication by 1/(1-kappa).

Using the rounded observed electromagnetic value, the required ratio is

    P_EM(R)/P_cos(R) = 0.1285800914414053.

This is a diagnostic target. Choosing that factor to match the observation would be a fit, not an explanation. The next calculation must obtain the electromagnetic readout from the retained direct reference and the two comparison blocks, without using 137.036 to choose its coefficients.

## Noise-floor meaning

The proposed carrier floor is a residual that remains even when laboratory imperfections are removed. Its mean shifts the effective coupling; fluctuations around its mean would produce noise. A nonzero mean residual need not produce fluctuations. A quantitative noise floor requires a distribution or covariance for R and its propagated readout, neither supplied by the budget deficit alone.

## Finished hypothesis and test

Abstract slot counting determines the integer normalization. Realizing the comparison on its own carrier contributes a closure residual. Cosmology reads this residual as a budget deficit; electromagnetic comparison reads it as a correction to reference-channel normalization. The 137 slots remain intact.

To test the hypothesis, construct R and both readouts from the carrier independently of the measured fine-structure constant. Recovering the cosmological deficit but forcing the universal scalar correction above would reject this explanation of the electromagnetic tail. A successful electromagnetic readout must also specify why the direct reference keeps unit weight (or calculate its correction) and distinguish the low-energy offset from energy-dependent running.

## First explicit two-block feedback trial

Trial assumptions fixed before evaluating the target: the reference selects one of the 121 arrow-comparison slots uniformly on an outward leg, then one of the 16 state-comparison slots uniformly on the return leg. Successive legs factor, retain the same sign, and repeat with unchanged gain. This is a toy routing model, not a consequence of the slot count.

The round-trip gain is L = (1/121)(1/16) = 1/1936. Assume each return adds normalization load to the reference. Then

    alpha^-1 = 137 (1 + L + L^2 + ...) = 137/(1-L).

The first return gives 137.0707644628099. Resumming all returns gives 137.07080103359172, exactly 265232/1935. Thus this uniform sequential routing predicts a tail of 0.070801, not 0.036.

This trial concerns propagation between the already counted blocks; it does not replace their disjoint-union slot count by a product. Its sign, routing, factorization, and reference-load rule are additional assumptions. In particular, load addition is not the same model as the opposing sequential multiplicative factors used by the Machian checker.

For diagnosis only, reproducing the rounded target in this model would require L = 9/34259, or 0.5085962813 times the trial gain. No such factor is adopted. The next structural question is which block-to-block return paths actually reach the retained direct reference, and with what signs. A return-incidence rule is needed to calculate that gain rather than fit it.

## Endpoint-reversal test

The sequential trial has 1936 path labels (i,j,a,b), where i,j range over eleven arrows and a,b over four states. Endpoint reversal is the involution (i,j,a,b) -> (j,i,b,a). It fixes 11*4 = 44 paths. The remaining 1892 paths form 946 reversal pairs. Thus the symmetric subspace has dimension 990 and the antisymmetric subspace dimension 946.

Under an incoherent uniform path ensemble, projection retains fractions 990/1936 = 45/88 and 946/1936 = 43/88 respectively. If this survival fraction multiplies the earlier loop gain without renormalizing the surviving ensemble, the same load-resummation model gives:

- symmetric projection: L = 45/170368, alpha^-1 = 137.036195933608;
- antisymmetric projection: L = 43/170368, alpha^-1 = 137.034586819316.

No measured value selects these fractions. The symmetric result reproduces the rounded .036 tail but differs from 137.036 by about 0.000196; it is not a precision prediction of the measured coupling.

Critically, projector rank fractions apply to an incoherent uniform ensemble. A coherent uniform vector is already symmetric: symmetric projection retains all of it, while antisymmetric projection removes it. Endpoint symmetry alone therefore does not supply the numerical correction. The candidate mechanism specifically requires incoherent path averaging, symmetric return selection, retained original normalization, and the assumed reference-load rule. These are the physical questions exposed by the count.

The 1936 labels belong to sequential return histories, not to the original 137-slot domain. Diagonal label matching also presumes an identified common arrow/state labeling at the two endpoints.

## Separate legs and the two-mode determinant

Keep distinct names for the outward leg a, return leg b, round-trip gain g, and mode magnitude ell. With the same trial assumptions:

    a = 1/121,
    b = (1/16)(45/88) = 45/1408,
    g = ab = 45/170368.

The legs are unequal. Treating them as opposing scalar multiplicative responses gives 137/((1-a)(1+b)) = 133.8633631566873; reversing the signs gives 140.36308528679504. Neither gives the small positive tail.

However a coupled two-block feedback operator K = [[0,a],[b,0]] has K^2 = ab I. Its eigenvalues are +ell and -ell, with ell = sqrt(ab) = 0.016252203225777143. Consequently

    det(I-K) = (1-ell)(1+ell) = 1-ab,
    137/det(I-K) = 137.0361959336085.

This realizes the proposed paired-factor form exactly, but its factors are collective feedback modes, not the individual unequal legs. It is the same round-trip resummation expressed spectrally, not an independent improvement in precision.

The inverse matrix is (I-K)^-1 = [[1,a],[b,1]]/(1-ab). Thus a source and readout on the same single block have diagonal response 1/(1-ab). A source exciting both blocks, or a mixed readout, generally also has numerator terms. The direct-reference source/readout must therefore be identified before using the denominator alone as the electromagnetic correction.

Opposite eigenvalue signs do not mean opposite edge signs. If the physical return edge is negative, K = [[0,a],[-b,0]], then det(I-K) = 1+ab and this positive-tail mechanism changes sign. The present model has positive cross-block couplings and opposite collective mode eigenvalues.

## Reference input/readout and memory test

A concrete proposed port assignment is to inject the direct reference into the arrow block and read the returned arrow response at that same port. Let x be arrow response, y state response, and u the direct-reference input. With the positive trial gains above:

    x = u + a*y,
    y = b*x.

For u = 1, x = 1/(1-ab), y = b/(1-ab). This same-port readout supplies the denominator-only response, and the normalization-load hypothesis gives alpha^-1 = 137*x = 137.036195933608. It does not count y again as a separately observed reference: y influences x through the return loop. This is a proposed port assignment, not a result forced by calling the source an arrow.

Other readouts demonstrably differ. Reading x+y gives 141.415903900237 after multiplication by 137. Reading (121*x+16*y)/121, normalized to unit response at zero feedback, gives 137.615330871344. Thus the near-.036 tail depends on reference-local readout, not simply the existence of two coupled blocks.

There is a further memory choice hidden in replacing a projector by a scalar survival fraction p = 45/88. Write g0 = 1/1936 for the unfiltered loop gain.

- Independently re-randomized paths each loop: response = 1/(1-p*g0), giving 137.036195933608.
- Persistent reversal sector: response = (1-p) + p/(1-g0), giving 137.036205073996.

The first-return terms agree. Higher returns differ because a persistent projector obeys P^2=P, whereas independent survival probabilities multiply to p^2. The difference in inverse coupling is 0.000009140387. Both remain above the rounded observed value. A carrier transport rule must decide whether path sectors persist or reset; the numerical target cannot decide that rule.

## Partial-memory family: a lower bound

Extend the memory test without choosing a coefficient from the target. Let p = 45/88 be the initial retained fraction, g0 = 1/1936 the unfiltered loop gain, and r in [0,1] the conditional probability of retaining the next return after an accepted return. The nth positive return has weight p*g0^n*r^(n-1). Hence

    alpha^-1(r) = 137 * (1 + p*g0/(1-r*g0)).

Reset corresponds to r=p; persistent retention corresponds to r=1; r=0 permits only the first return. The expression increases with r. Its minimum is therefore 137.036186373028, already above the rounded target 137.036. Solving for r from that rounded target gives -10.022727..., outside the admissible interval. No change of positive-return memory in this family fixes the discrepancy. More generally any additional nonnegative returns added to this fixed first return cannot lower it.

Retaining T1 witnesses favors keeping their labels in a T2 extension, but does not itself establish a stochastic memory law. Nevertheless the numerical test settles that memory selection alone is not the source of the remaining correction. The structural work must return to the first-return transfer: its normalization, signed/phase contributions, reference source/readout, and whether diagonal endpoint-fixed histories survive reference subtraction. These are distinct mechanisms to derive from actual comparison maps, not coefficients to tune.

## Reference subtraction is not endpoint-fixed-path deletion

The 44 fixed paths satisfy i=j and a=b. They express matched endpoint labels. The direct relationship itself was excluded before constructing this domain, so its identification with any of these fixed paths does not follow.

Tested three explicit choices under the reset/rank-fraction trial:

| Subtraction | Symmetric rank | Inverse coupling |
|---|---:|---:|
| None | 990 | 137.036195933608 |
| One embedded symmetric reference direction | 989 | 137.036159362409 |
| Entire endpoint-fixed subspace | 946 | 137.034586819316 |

None reproduces the rounded target. A rank-one reference subtraction is geometrically distinct from deleting all fixed paths. For a normalized uniform symmetric reference vector u, the centered projector Q = P_plus - u*u^* is idempotent, has rank 989, and annihilates u. Thus if the same uniform vector is also taken as the injected coherent source, this subtraction removes its whole response, not merely one uniformly weighted return. Incoherent rank averaging and coherent reference injection cannot be silently exchanged.

At the comparison-data level, subtracting a specified direct reference is generally an affine discrepancy (assembled comparison minus reference), not automatically an orthogonal projection or deletion of slots. Such subtraction retains the comparison domain. Choosing a projector requires a separately supplied inner product and embedded reference direction.

The next necessary carrier object is the actual assembly map from the slot data to the direct-reference comparison space. Its endpoint/composition constraints determine the residual. The count alone cannot select a deletion rule or a return gain. The numerical tests rule out the simple deletions above; they do not justify searching for a number of deleted modes that fits the target.

## A typed linear assembly prototype

To make the missing operation explicit, use endpoint spaces A,B and intermediate spaces U,V. Specify maps x_i:A->U and y_j:U->B for eleven arrow labels each, and s_a:A->V and t_b:V->B for four state labels each. The state labels must be realized as maps for this construction: four possible values by themselves do not provide these maps. The common intermediate spaces are also additional structure.

All 121 maps y_j composed with x_i and all 16 maps t_b composed with s_a now have endpoints A->B, as does the direct reference d. In a linear target the proposed equal-weight assembly is

    C = (sum_ij y_j x_i + sum_ab t_b s_a)/137,
    R = C - d.

There are no mixed terms because this prototype supplies no U-to-V or V-to-U adapters. This is a declared typed separation, not a proof that the carrier forbids such adapters. Outside a linear target, summing and subtracting maps must be replaced by an appropriate comparison construction.

An exact rational 2x2 matrix test uses identity reference and identity component maps. It finds:

- all composites equal the reference: R=0;
- perturb one arrow leg by H: R=(11/137)H;
- perturb two arrow legs by H and -H: R=0, with all 137 slots retained;
- perturb one state leg by H: R=(4/137)H;
- change the reference alone by H: R=-H.

These examples show why reference subtraction is not deletion. They also show that identical counts and endpoint types admit different residuals. A scalar electromagnetic correction needs a specified readout of R and a rule returning it to the comparison maps. Neither is determined by the number of slots. The prior near-.036 calculation remains a separate toy routing model, not a consequence of this assembly.

Executable: research/nima/checkers/check_comparison_slot_reference_assembly.py. All tests use exact fractions and write no artifacts.

## Verification

Read the cosmological closure checker and research/nima/checkers/check_constant_table.py. Recomputed the closure deficit and scalar-normalization test using Python fractions.Fraction, without executing the checkers' artifact-writing routines. No physical readout map or noise covariance was computed.

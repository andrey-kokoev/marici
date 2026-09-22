# Private-row redundancy improves cubic norms and reduces full optimization to LP

## Follow-up

The full-optimization gate below is now closed for the declared unscaled continuous-response protocol by `matched-private-corrections-attain-the-full-cubic-observer-norm.md`. Exact window-matched corrections attain the crossed-source lower bound; its numerical enclosure has ratio below 1.033. The sixteen-row result here remains a valid, restricted-family certificate.

## Result and what was still open at this stage

The previously calibrated two-private-row observer is NOT finite-background optimal. At A=2, y=3 and gamma=1, using eight proved-private rows for each visible source basis product reduces its norm by a certified factor greater than 7.8, in the SAME full labelled response norm.

The new rational observer permits total independent response noise 10^(-542) while retaining a margin greater than 0.05 w_seam^2, including shared-template error and calibration discrepancy from the original functional.

Its ideal coefficients are exactly optimal within the declared fixed-residual-test family on these sixteen rows. This is a feasible upper bound for the FULL optimization, not its claimed solution.

The full problem has an exact finite weighted-l1 optimization formulation after resolving the actual analytic shape blocks. Below we also provide 270 private correction pivots, allowing rigorous repair of numerical primal feasibility. A near-matching numerical primal/dual certificate for the FULL carrier remains open.

## 1. Freeze the domain, functional and norm

Use Voevodsky's existing six-event, two-feature source corner and its 270 actual minimal cubic basis products. Keep the original source functional Lambda, whose only nonzero basis values are S_0 and S_x on

    v_0=mixed(2,3)mixed(5,7)forgotten(11,13),
    v_x=mixed(2,5)mixed(3,7)forgotten(11,13).

As in the calibration theorem, write S_0 and S_x below per w_seam^2. Physical w_seam^2 is restored in every observer.

Use the same unscaled labelled l1 sum of ordered projective response tensors as the supplied observer-optimization theorem. No source Gamma norm is substituted for this data norm. Every new row below is already present in that full output.

## 2. Eight private copies of each useful row

For v_0 choose independently:

- its first retained seam 2->4 or 2->6;
- its second retained seam 12->60 or 12->84;
- the forgotten first seam 420->4620 or 420->5460.

For v_x use instead:

- 2->4 or 2->10;
- 20->60 or 20->140;
- the same two forgotten first seams.

All coefficient buffers are vacuum. Each family contains eight distinct balanced rows. Enumeration against ALL 270 actual source columns proves each row has coefficient +1 or -1 on its designated basis product and zero on every other product. The checker retains each actual sign.

Using a forgotten SECOND seam instead is not automatically private: the audit finds shared rows with other source products. Such rows are not included in the private certificate merely because they occur in the witness.

## 3. Exact optimum for the fixed residual-test family

Keep the norm-one residual test

    kappa(w)=sqrt(8) integral_0^infinity exp(-5u)w_res(u)du.

For a window F define its positive scalar response

    k_F=sqrt(2)h X_F(mu_F-L), h=1/sqrt(8).

All factors needed here are certified positive. The sums of the eight unsigned private row values are

    N_0=2[k_(2,2)+k_(2,3)][k_(12,5)+k_(12,7)],
    N_x=2[k_(2,2)+k_(2,5)][k_(20,3)+k_(20,7)].

Here k_(A,p) refers to the actual window A->pA; the leading factor two counts the two forgotten-first seams.

On each private family give row r coefficient sign_r*S_i/N_i multiplying kappa tensor kappa. This represents the original functional on ALL 270 source basis products. Its norm per w_seam^2 is

    max(|S_0|/N_0,|S_x|/N_x).

This is the exact optimum among tests using this fixed kappa tensor kappa on these sixteen rows. Indeed coefficients bounded in magnitude by t can produce at most t*N_i on basis product i, and the displayed choice attains that bound simultaneously.

This restricted-family optimum is not the optimum over arbitrary tests even on these rows: the full five-label response can supply additional norming information. Nor does it optimize over all other balanced outputs.

## 4. Arb calibration and norm improvement

The checker freshly reruns the scaled completed-theta integration and adds the actual windows 2->6, 2->10, 12->84 and 20->140. It compares both ideal and rational-calibrated observer norms to the earlier one-private-row-per-basis tests.

Both norm improvements are certified greater than 7.8. Rational coefficients, attached with the exact source row signs, have calibration errors below 0.002 on each of v_0,v_x and zero on the other source basis products. As before, these are absolute basis-value errors; no uniform relative bound on cancellation-prone source combinations is inferred.

The same finite residual template contributes its already certified private-test factor rho>0.9997. With total independent projective-response noise 10^(-542), Arb verifies

    calibrated positive signal - noise error
        - original-functional calibration discrepancy >0.05

per w_seam^2. The artifact records the rational coefficients and exact error enclosures.

The improved tolerance uses all sixteen measured rows. It does not retrospectively improve a data protocol that records only the original two private rows.

## 5. Why the entire continuous-output problem is finite dimensional

At the fixed imaginary spectral point, all prepared one-feature responses lie in

    E=span{c_even,v_e},
    c_even=O(e_y,0),
    v_e=(0,0,0,e_y,0).

These two vectors occupy disjoint response coordinates. Thus, putting C_even=||c_even|| and h=||e_y||_Hminus,

    ||a c_even+b v_e||=C_even|a|+h|b|.

Moreover E is 1-complemented in the actual response space. Choose a norming functional for c_even on its four-coordinate carrier and the norming functional for e_y on the residual coordinate. Their direct-sum reconstruction has norm at most one. This is a finite-dimensional response projection, not a source inverse.

Consequently E tensor_pi E is isometrically a weighted l1 space of four coordinates and is 1-complemented in the ambient projective response tensor space. This follows by tensoring the norm-one projection and inclusion. No general injectivity of projective tensoring or tensor-dual surjectivity is assumed.

There are only finitely many actual shape blocks reached by the finite source corner. Restriction to those blocks is contractive. Therefore the full optimal extension problem is exactly a finite weighted-l1 problem on the ACTUAL analytical source images, with the existing labels and any declared fixed shape weights retained.

## 6. The exact primal/dual optimization

After forming the analytical block coefficients, let B be the real matrix sending the 270 source coefficients c to those scalar coordinates. Let w_l be the positive coordinate weights, incorporating C_even, h and the frozen shape weights. Let s have entries S_0,S_x in the two visible columns and zero elsewhere.

Then

    ||Yc||=sum_l w_l |(Bc)_l|.

The optimal full-output observer norm per w_seam^2 is equivalently

    min t subject to B^T z=s and |z_l|<=t w_l,

or

    sup s^T c subject to sum_l w_l |(Bc)_l|<=1.

The second expression is the norm of the original functional on the source image; Hahn--Banach and finite-dimensional LP duality give equality. Real optimization suffices here: rotate a complex source coefficient vector so its functional value is real, then take its real part, which cannot increase the weighted-l1 output norm.

This statement does NOT identify formal coefficient-potential keys with independent noisy response channels. The finite audit finds 108720 formal record keys, with 79200 singly supported and 29520 supported on two source columns. Potential-buffer coordinates must be substituted and combined in their owning analytical shape blocks BEFORE their response norms are taken. A naive weighted LP on all those formal keys could optimize a different, enlarged data norm.

## 7. Rigorous feasibility repair is available on all 270 columns

There is an actual private residual-test pivot for EVERY source basis product. Choose the first seam in each two-event block, retaining its feature when the block is mixed. All buffers are vacuum. The three block-start vertices fix the ordered pair partition and the seam marks fix the retained distribution.

The checker verifies that each such row has coefficient +1 on its column and zero on all 269 other columns. Its kappa-tensor evaluation E_j is nonzero: every retained window begins at least at 2, and x tanh(3x) at log 2 already exceeds the enclosed L(7/2).

Suppose a numerical candidate test Lambda_0 has residual source values

    d_j=s_j-Lambda_0(Yv_j).

Adding d_j/E_j times the corresponding private pivot test makes the source identities EXACT. The pivot rows are distinct, so the correcting test has norm

    max_j |d_j|/E_j.

Thus a rigorous upper certificate can combine an interval bound on ||Lambda_0|| with this correction bound. Tiny E_j require adequate relative precision; feasibility cannot be declared from a small unscaled floating residual.

For a lower certificate choose an exact finite source vector c, enclose its actual output norm from above and |s^T c| from below, then take their ratio. This gives a genuine source-based lower bound, including crossed directions, rather than a witness-only estimate.

## 8. Remaining full-optimization gate

The exact reduction, correction pivots and improved feasible test are established. What remains is to:

- assemble B in the true analytical blocks, including memory features;
- enclose C_even and all required window coordinates in the declared response norm;
- solve the resulting finite problem and certify a near-matching feasible upper bound and source lower bound.

No numerical full-carrier optimum is claimed by the present sixteen-row calibration. The all-depth observer-module tower is a separate structure; these fixed-corner norm improvements imply no uniform depth bound.

## Reproduction

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_redundant_private_cubic_observer.py

Artifact:

`research/grothendieck/results/redundant-private-cubic-observer.json`.

Inputs are the existing actual cubic source checker, Voevodsky's private-sector optimization theorem, and the scaled-theta calibration from `scaled-theta-calibration-makes-cubic-template-certificates-robust.md`.

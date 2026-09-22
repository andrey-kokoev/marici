# An extra existing sector gives order-optimal cubic observer noise

## Result

The cubic observer can be made substantially more noise-robust WITHOUT changing its value on any genuine source in the entire six-event, two-feature I^3 corner.

There are two different measurement schemes:

1. Using ONLY the original four selected response sectors, an admitted recalibration has asymptotically optimal norm order

   `A^(-2y-5) exp(901pi A^2)`.

2. Reading ONE additional existing sector of the same source packet permits an admitted recalibration of asymptotically optimal norm order

   `A^(-2y-5) exp(101pi A^2)`.

The original four-sector observer had norm order A^(-2y-5)exp(904pi A^2). Both improved exponents and their polynomial factors have matching lower bounds for the specified measurement schemes. Optimality here means growth order up to fixed positive constants, not an exact minimum calibration constant.

The second improvement genuinely uses additional labelled data. It is not attainable from the original four sectors alone. No new edge, source relation, arithmetic coefficient, or response counterterm is introduced.

### Concurrent closure and attribution

Voevodsky's `../voevodsky/alternative-balanced-sectors-reduce-cubic-response-amplification-to-sharp-gaussian-order.md` independently supplies these sectors and strengthens the conclusion: it computes the exact four-sector continuous-extension norm and proves the exponent-101 growth order optimal for the FULL labelled balanced response, not just the five-sector restriction analyzed here. Its explicit unit weak-residual-coordinate test also improves the calibration constant relative to retaining o_0. This note records the independent o_0-based constructions and their all-basis regression checks; it does not supersede those stronger results.

## 1. Freeze the source functional and the noise norm

Use the translated packets and notation of `translated-cubic-observers-have-sharp-gaussian-source-growth.md`, with initial arithmetic vertex A=2Q, fixed primes (2,3,5,7,11,13), and fixed 1/2<gamma<y<beta.

Let L_A be the ORIGINAL four-sector functional on V_A, the full two-feature I^3 component in this six-event corner. Keep the physical seam weight w=w_seam.

For a window F put

`X_F=X_F(iy)>0`, `m_F=mu_F-L_0`, `L_0=(xi'/xi)(1/2+y)`.

Keep the existing observer port o_0=(e_y,-2L_0 e_y), e_y(u)=exp(-yu), and its admitted response test

`psi(z)=conjugate(<E o_0,z>)`.

Let t_0=||psi|| on the original one-slot response space R. This is finite, positive and independent of A. On actual window inputs,

`psi(O Psi(F))=X_F m_F/(sqrt(2)y)`.

For measurements, use the l1 sum of the selected UNscaled two-feature response sectors, each with its projective R tensor R norm and unit vacuum spectators. The scalar functional restores the SAME w^2 factor. This specifies exactly the noise norms in which optimality will be proved.

For all sufficiently large A, every m_F used below is positive: mu_F>=h_y(log(start F)) and h_y(x)=x tanh(yx) tends to infinity. Thus the displayed divisions are legitimate. At the finitely many smaller admitted backgrounds one can retain the original observer. No claim of a new numerical calibration at those backgrounds is needed.

## 2. The two-dimensional visible source data

The previous note proves that the minimal cubic source has 270 disjoint-support basis products. For the original four sectors only two basis products are visible:

`v_0=mixed(2,3) mixed(5,7) forgotten(11,13)`,

`v_cross=mixed(2,5) mixed(3,7) forgotten(11,13)`.

Their selected coefficient vectors are

`v_0: (1,1,1,1)`, `v_cross: (0,1,0,0)`.

The order is (A_1B_1,A_1B_2,A_2B_1,A_2B_2). On these products the functional to be preserved is

`S_0=L_A(v_0)=w^2 Delta_A Delta_B/(2y^2)`,

`S_cross=L_A(v_cross)=-w^2 m_(A_1)m_(B_2)/(2y^2)`,

where Delta_A=mu_(A_2)-mu_(A_1), Delta_B=mu_(B_2)-mu_(B_1).

All other source basis products have zero value. Agreement on these two coordinates and annihilation of the other 268 products therefore proves agreement on ALL of V_A, not just the positive witness.

## 3. Best growth order without adding a measured sector

Use only sectors A_1B_1 and A_1B_2, setting the other two observer coordinates to zero. Place d_0 o_0 tensor o_0 in the first and d_1 o_0 tensor o_0 in the second, with

`d_1=-1/[X_(A_1)X_(B_2)]`,

`d_0=[Delta_A Delta_B+m_(A_1)m_(B_2)]
      /[X_(A_1)X_(B_1)m_(A_1)m_(B_1)]`.

The resulting measurement is w^2[d_0(psi tensor psi)(z_0)+d_1(psi tensor psi)(z_1)]. On v_cross it equals S_cross. On v_0 its first term is S_0-S_cross and its second is S_cross, so it equals S_0. Every other basis product is still invisible.

These are finite elementary tests in the same admitted normalized sectors as the original observer. Only their scalar coefficients have changed. No new tensor-dual element is asserted to descend.

Its ambient response norm is exactly

`t_4(A)=w^2 t_0^2 max(|d_0|,|d_1|)`.

As A tends to infinity, m_F/log A->1, while the gaps tend to log 2 and log 5. Consequently d_0~1/[X_(A_1)X_(B_1)], and d_1 dominates exponentially. Hence

`t_4(A) ~ w^2 t_0^2/[X(A,2)X(30A,7)]
         is comparable to A^(-2y-5)exp(901pi A^2)`.

Section 5 shows that no bounded observer agreeing with L_A on V_A can improve this order if only these original four sectors are measured.

## 4. One additional admitted early sector

The same six-event Boolean packet already contains the actual retained edge

`D_1: 10A -> 30A`, with window [log(10A),log(30A)].

Add the selected sector whose three seams are

`2: A->2A`, `3: 10A->30A`, `11: 210A->2310A`,

with the two first seams retained and all buffers and the third seam evaluated in their existing vacuum sectors. Call it A_1D_1.

This is a sector of D3 in the original packet, not a replacement edge or an independently prepared state. Its preimage route has events 2,5,3,7,11,13. It sees v_cross with coefficient +1 and annihilates the other 269 basis products: the selected first and third event positions fix the first two pair blocks to (2,5),(3,7), and the final seam fixes (11,13).

Now use only A_1B_1 and A_1D_1, with coefficients

`e_0=Delta_A Delta_B
      /[X_(A_1)X_(B_1)m_(A_1)m_(B_1)]`,

`e_cross=-m_(B_2)/[X_(A_1)X_(D_1)m_(D_1)]`.

The corresponding w^2 psi-tensor tests give S_0 on v_0 and S_cross on v_cross, respectively. They vanish on all other basis products. Thus this new observer has exactly the original functional L_A on the entire source corner.

Its norm on the FIVE-sector measurement space (the original four plus this sector) is

`t_5(A)=w^2 t_0^2 max(|e_0|,|e_cross|)`.

The crossed coefficient dominates, and m_(B_2)/m_(D_1)->1. Therefore

`t_5(A) ~ w^2 t_0^2/[X(A,2)X(10A,3)]
         is comparable to A^(-2y-5)exp(101pi A^2)`.

The test still uses only o_0 and the existing unit vacuum observations. Its source action and balancing are those of the existing normalized record sectors; it is not an appeal to surjectivity of a tensor dual.

## 5. Matching lower bounds from actual source images

Write r_F=O Psi(F). Because all windows prepare the SAME exponential e_y at this spectral point,

`||r_F||_R=sqrt(2)X_F [C_u+c_r |m_F|]`,

where

`c_r=||e_y||_(H_(-gamma))=1/sqrt(2(y+gamma))`,

`C_u=||B_rig e_y||+||leak_rig e_y||
      +||J_end beta_end(e_y)||+||e_y||_(H_(-gamma))`.

These are fixed finite constants in the declared sum response norm. Thus

`||r_F||_R ~ sqrt(2)c_r X_F log A`.

Let Y_4 and Y_5 be the four- and five-sector measurement maps. The actual crossed source has

`||Y_4(v_cross)||=||r_(A_1)|| ||r_(B_2)||`,

`||Y_5(v_cross)||=||r_(A_1)||[||r_(B_2)||+||r_(D_1)||]`.

These equalities use elementary projective tensor norms and the direct-sum norm of distinct labelled sectors, not a norm estimate inferred from source weights.

Any bounded measurement functional ell satisfying ell Y_k=L_A on V_A must obey

`||ell|| >= |S_cross|/||Y_k(v_cross)||`.

For k=4 this lower bound is asymptotic to

`w^2/[4y^2 c_r^2 X_(A_1)X_(B_2)]`.

For k=5, X_(B_2)/X_(D_1)->0, and the lower bound is asymptotic to

`w^2/[4y^2 c_r^2 X_(A_1)X_(D_1)]`.

The admitted tests constructed in sections 3 and 4 achieve these orders. The lower bound applies even to all bounded ambient functionals, and hence also to the smaller admitted class. No existence theorem for arbitrary descended duals is used.

In particular exponent 101 is impossible from the ORIGINAL four sectors alone. Conversely exponent 904 was not intrinsic to the original source functional: it came from its chosen redundant calibration.

## 6. Relation to source norms, priors and noise certification

The source-functional norm remains exactly the one computed previously, because the functional on V_A has not changed:

`a_R(A) ~ C A^(-2beta-7)exp(101pi A^2)`.

Its polynomial power differs from the response-noise norm, even after the improved five-sector measurement. No source and response norms have been identified.

On any fixed finite packet, a response error epsilon in the chosen measured-sector sum norm produces scalar error at most t_k(A)epsilon. Thus the same positive source observation S_0 has a substantially better sufficient noise tolerance under the new calibrations. Numerical uncertainty in X, m, gaps or the new coefficients requires a separate certified calibration budget; the asymptotic theorem supplies no Arb tolerance by itself.

The general observer-family/source-prior criterion is unchanged, while its forward measurement constant is improved. Native/inherited source comparisons and convex packet projections keep the same ideal and labels.

Optimality has been proved for the explicitly specified four- and five-sector noise norms. No assertion is made that these are globally optimal among every possible larger receiver, alternative physical measurement norm or additional source calibration data. Nor does source-functional agreement make the two observers identical on arbitrary noisy records outside the actual image.

The shared-template theorem `../grothendieck/two-feature-field-transport-preserves-the-cubic-observer-with-shared-templates.md` concerns a DIFFERENT error structure. The old observer cancels a common even-template term on v_0. The recalibrations here agree on genuine source images, not arbitrary coherently perturbed records, and need not retain that exact cancellation. For example, writing the common scalar template term as C and its residual correlation as a, the new five-sector value on the simulated v_0 is

`2w^2 Delta_A Delta_B [a+C/m_(A_1)][a+C/m_(B_1)]`,

rather than the old `2w^2 Delta_A Delta_B a^2`. Thus optimality for independent norm-bounded noise does not imply superiority for every structured error model.

## Verification

`uv run --with sympy python research/nima/checkers/check_optimized_cubic_observer.py`

The checker enumerates all 270 actual minimal cubic source products, verifies the additional isolating sector, and checks both recalibrations on every basis vector. It verifies the symbolic noise-order formulas and the original source-functional values. Infinite optimal growth uses the actual theta asymptotics and source-image lower bounds above, not a numerical optimization over arbitrary tests.

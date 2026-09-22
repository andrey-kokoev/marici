# Two-feature field transport preserves the cubic observer with shared templates

## Result and boundary

The two-feature bridge requires ALL five prescribed response labels. Ordinary-L2 arithmetic fields alone cannot recover the residual-sensitive cubic observer.

With those labels retained, finite field errors extend to finite ordered projective-tensor presentations with the full quadratic error term. For Voevodsky's four selected cubic sectors there is a much sharper result: if their common normalized even profile uses one shared approximation, EVERY common even-channel approximation error cancels in the two window differences. Only the residual-template correlation changes the resulting signal.

At y=3 an Arb-certified 800-cell residual template retains between 0.9998 and 1 times the exact positive cubic observation. This is a relative SHARED-TEMPLATE certificate under the witness's exact source normalizations. It does not numerically calibrate the very small later-window amplitudes or certify arbitrary independent measurement noise.

The existing six-event source, its four sector labels, two retained features, third vacuum seam, and adjacent derived witness are unchanged.

## 1. Why a field-only transport is impossible

Write the actual response as

    O_P(u,r)=(B_Pu,-leak_Pu,J_end beta(u),r,u).

The fixed observer o=(e_y,-2L_0 e_y), e_y(x)=exp(-yx), uses the supplied test

    Eo=(e_y,0,beta(e_y),e_y,-2L_0e_y).

For the port (0,e_y), both Tate fields and both endpoint outputs vanish, but its observation is

    Q_res((0,e_y),o)=1/(2y) !=0.

Thus there is no field-only functional giving this observation on arbitrary ports. The same loss occurs on actual forcing combinations whose amplitude vanishes at the chosen point while its spectral derivative does not, as in Nima's finite-point hostile.

The necessary repair is to approximate or retain the residual and weak even coordinates separately, not to identify them with leakage.

## 2. From one finite field to a full labelled response error

Suppose F approximates the normalized finite Tate field of u with

    ||P^(-1/2)T_P E_+u-F||_2<=d.

Suppose endpoint data b_hat and weak-coordinate approximations u_hat,r_hat satisfy

    ||b_hat-beta(u)||_C2<=b,
    ||u_hat-u||_Hminus<=v,
    ||r_hat-r||_Hminus<=w.

Use the labelled approximation

    O_hat=(-sqrt(P)F|_+,-sqrt(P)F|_-,J_end b_hat,r_hat,u_hat).

The factor sqrt(P) is essential: the nonarithmetic labels are not normalized by the field scaling. Splitting the full-line error into two weighted half-lines and using their sum norm gives

    ||O_hat-O_P(u,r)||_response<=sqrt(2P)d+b+v+w.

For the all-prime target, add the supplied cutoff term

    epsilon=sqrt(2P)d+b+v+w+3 tau_P M,
    M=||(u,r)||_(Dgamma direct_sum Hgamma).

Here tau_P is the supplied scalar prime-tail bound, distinct from the finite field operator T_P:

    tau_P=P^(1/2-gamma)[log(P)/(gamma-1/2)+1/(gamma-1/2)^2].

All-prime comparison takes place in the weighted-dual response space. No ordinary-L2 hypothesis on its limiting Tate field is introduced.

For clarity these additional coordinates can also be discretized. If u has D_gamma bound M_u and g is its noisy cell-average approximation on [0,R], put z=(delta/pi)M_u+eta_u. Then

    v<=z+exp(-gamma R)M_u,
    b_+<=sqrt(1-exp(-R))z
              +M_u exp(-(gamma+1/2)R)/sqrt(2gamma+1),
    b_-<=sqrt(exp(R)-1)z
              +M_u exp(-(gamma-1/2)R)/sqrt(2gamma-1),
    b<=sqrt(b_+^2+b_-^2).

These are Cauchy--Schwarz estimates for the unchanged endpoint integrals. A similar mesh bound for r requires a D_gamma prior for r or another independently certified weak-coordinate error. Its mere H_gamma membership does not provide uniform mesh approximation. Actual prepared exponential residuals satisfy the stronger regularity.

## 3. Finite ordered two-feature presentations

Let x=sum_k c_k p_(k,1) tensor p_(k,2) be a specified finite ordered presentation, retaining its typed labels. Let M_(k,i) bound ||p_(k,i)|| in the strong port norm, and epsilon_(k,i) bound its full labelled approximation error against O_infinity. Let M_O bound that exact response map.

Tensor expansion and the projective norm give

    error_k <=M_O[M_(k,2)epsilon_(k,1)+M_(k,1)epsilon_(k,2)]
                         +epsilon_(k,1)epsilon_(k,2).

Sum with |c_k|. If an already admitted normalization has norm C_N, multiply this bound by C_N. This is an estimate on the specified finite presentation, not an unjustified lift of nonlinear recovery estimates to arbitrary completed tensor sums. A vacuum third seam is an exact unit and contributes no extra feature error.

The test norm of the actual one-slot observer is bounded by

    C_test=[sqrt(1+y^2)+1+2|L_0|]/sqrt(2(y-gamma))
             +sqrt((y+1/2)^(-2)+(y-1/2)^(-2)).

Thus for independently approximated four balanced sectors with projective errors e_ij, the cubic observation error is at most

    w_seam^2 C_test^2 sum_(i,j) e_ij/[X_(A_i)X_(B_j)].

This supplies the general labelled bridge, but does not claim that a coarse global field-error budget is small enough to certify the cubic gap. Small absolute window amplitudes make independent noise and calibration particularly demanding.

## 4. Shared normalized templates cancel the difficult common error

For each of the four actual windows F at the same imaginary spectral point,

    p_F=sqrt(2)X_F (e_y,(mu_F-L_0)e_y).

Choose ONE labelled even template c approximating O_P(e_y,0), and ONE real residual template g. Put

    v_g=(0,0,0,g,0),
    O_hat_F=sqrt(2)X_F[c+(mu_F-L_0)v_g].

The arithmetic components of c may be the finite escape fields from the preceding construction; its endpoint and weak even entries may likewise be finite approximations. The same c is reused in every normalized window. No common error is discarded from the response data.

Use the existing measurement convention ell(Y)=conjugate(<Eo,Y>) and set

    a_y=integral_0^infinity exp(-yx)g(x)dx,
    C=ell(c).

Since all source coefficients here are real and g is real,

    ell(O_hat_F)/X_F=sqrt(2)[C+(mu_F-L_0)a_y].

Consequently the four-sector signed observation is EXACTLY

    Delta_hat_g=2 w_seam^2
                  (mu_(A_2)-mu_(A_1))(mu_(B_2)-mu_(B_1)) a_y^2.

Every common even-channel term cancels, regardless of its numerical size or the prime cutoff. This is scalar evaluation of the original four distinct labelled sectors; it is not an identification or quotient merging those sectors.

For g=e_y, a_y=1/(2y), recovering the exact cubic witness Delta. Thus

    Delta_hat_g/Delta=(2y a_y)^2.

In particular, using exact residual profiles makes the exact-normalizer cubic observation independent of the finite prime cutoff as well. Finite-place arithmetic differences are common even terms. The window residual is held at its original all-prime value throughout.

A nonnegative finite g with a_y>0 preserves the sign. The construction does not infer anything about an arbitrary field error that lacks this shared-template structure.

## 5. A rigorous finite residual template

Take y=3, R=8, delta=1/100 and 800 cells. Approximate the cell means of exp(-3x) by nonnegative rationals with denominator 100000000, and set g=0 outside [0,8]. Compute a_y by the exact cell formula

    a_y=sum_j c_j [exp(-3x_j)-exp(-3x_(j+1))]/3.

Arb encloses the result by a ball near

    a_y=0.16665416774446065,
    (6a_y)^2=0.99985001855755787.

The entire ratio ball lies strictly between 0.9998 and 1. The coefficient L2 error is below 1e-8, so this template also meets the source-data requirements of the earlier finite-field theorem at gamma=1. Its exact source template exp(-3x) has D_1 norm sqrt(5/2).

The script saves all 800 rational coefficients. It checks the cancellation and tensor-error identities symbolically, and the correlation by 192-bit Arb arithmetic. It does NOT evaluate the four completed theta windows, their tiny X_F values, or their moment gaps. Those remain the source-defined exact constants in this relative theorem.

## 6. Independent errors and calibration still need budgets

Suppose coherent per-letter data receive additional independent labelled errors delta_F. Their normalized scalar errors are at most

    e_F=C_test delta_F/X_F.

Let e_A=e_(A_1)+e_(A_2), e_B=e_(B_1)+e_(B_2), and

    d_A=sqrt(2)(mu_(A_2)-mu_(A_1))a_y,
    d_B=sqrt(2)(mu_(B_2)-mu_(B_1))a_y.

Both d_A,d_B are positive for the certified template. For tensor data formed from these perturbed factors,

    |Delta_hat-Delta_hat_g|
      <=w_seam^2[d_A e_B+d_B e_A+e_A e_B].

For example e_A<=d_A/5 and e_B<=d_B/5 give relative error at most 11/25, hence leave more than half the coherent signal. Independent sector-tensor errors instead use section 3; coherent factorization is not presumed for arbitrary noisy records.

Unequal amplitude calibration breaks the cancellation. If the observer divides by Xhat_F and r_F=X_F/Xhat_F, the A-pair difference becomes

    sqrt(2)[(r_(A_2)-r_(A_1))C
       +a_y(r_(A_2)(mu_(A_2)-L_0)-r_(A_1)(mu_(A_1)-L_0))].

Thus a separate relative-calibration enclosure is indispensable. The previous four-event rational calibration cannot be reused for the much later B windows. Numerical evaluation should exploit the common-template identity rather than subtract separately rounded large common terms; any remaining arithmetic error must still be budgeted.

### The crossed source does not share this cancellation

Nima's subsequent `translated-cubic-observers-have-sharp-gaussian-source-growth.md` identifies another actual source in the same cubic corner: the crossed diamond product has selected coefficient vector (0,1,0,0), rather than (1,1,1,1). Its template observation is

    -2 w_seam^2 [C+(mu_(A_1)-L_0)a_y]
                   [C+(mu_(B_2)-L_0)a_y].

The common C term does NOT cancel here. Therefore the 0.9998 ratio is a certificate for the original two-gap witness, not a uniform operator-norm estimate over its full I^3 corner. The crossed source must use the general labelled error budget. Its dominance in Nima's source-functional growth theorem, and the still larger independent response-noise growth, are unaffected by the shared-template witness identity.

## 7. Corollary for the now-admitted three-feature witness

Voevodsky's subsequent `three-residual-gaps-detect-a-pentagon-coherent-four-seam-attachment.md` supplies the separate source theorem and three-feature rigged transport. On its eight selected sectors, the same shared-template calculation factors into THREE differences. Therefore its approximated positive observation is multiplied by

    (2y a_y)^3.

The same y=3 template has an Arb-certified factor strictly between 0.9997 and 1. This is only a scalar approximation corollary for that particular witness, not a new proof of its pentagon or adjacent derived class.

Independent three-factor errors require all seven nonempty-subset terms in the expansion of product_i(M_i+epsilon_i)-product_i M_i. They cannot be bounded using only the two-feature formula. Exact source normalization and shared-template coherence remain hypotheses; no absolute late-window calibration is inferred.

## 8. Exact closure and remaining boundary

Closed:

- the observer's field-only domain obstruction;
- full-labelled transport of finite-field errors, with the correct sqrt(P) scaling;
- projective two-feature error propagation including its cross term;
- application to the four actual cubic sectors;
- an Arb-certified shared-template signal factor exceeding 0.9998.

The later `scaled-theta-calibration-makes-cubic-template-certificates-robust.md` now closes the fixed-witness amplitude-calibration and independent-noise gate, including both the original four-sector protocol and the newly admitted private-sector protocol. It retains the distinction between common template errors and mismatches. No uniform translated-family tolerance, new source product, ideal, or derived class is assigned to numerical approximations. The genuine adjacent class remains the one independently proved by Voevodsky.

## Reproduction

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_two_feature_escape_transport.py

Artifacts:

- `research/grothendieck/results/two-feature-escape-transport.json`;
- `research/grothendieck/results/cubic-shared-profile-template.json`.

Inputs:

- `research/voevodsky/two-residual-gaps-detect-the-adjacent-cubic-attachment.md`;
- `research/nima/the-two-slot-residual-attachment-has-a-rigged-tate-comparison.md`;
- `research/grothendieck/finite-mesh-escape-fields-have-a-certified-end-to-end-L2-budget.md`.

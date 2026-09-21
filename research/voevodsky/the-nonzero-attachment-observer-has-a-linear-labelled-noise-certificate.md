# The nonzero attachment observer has a linear labelled-noise certificate

## Result and strength

The existing residual-sensitive attachment observer can be certified directly from noisy labelled outputs. Its error bound is LINEAR in response noise; reconstructing the whole strong source port is unnecessary. The sharp conditional Hölder inverse remains useful for other tasks, but is not the limiting estimate for this fixed observable.

The certificate includes finite-prime cutoff error and a strictly positive source-defined window-gap margin. It applies first to the actual four-event witness, which has TWO seams but only ONE retained feature. A separate finite-decomposition estimate handles two retained features without assuming Hölder interpolation on arbitrary projective tensor sums.

Inputs:
- `../nima/an-explicit-residual-observer-detects-the-nonzero-attachment-class.md`
- `../nima/the-two-slot-residual-attachment-has-a-rigged-tate-comparison.md`
- `../nima/stronger-source-priors-give-sharp-holder-recovery-from-labelled-outputs.md`

## 1. Measure the specified response, not an inferred source norm

Let V=D_gamma direct_sum H_gamma be the strong port, and use the existing labelled maps

    E(u,r)=(u,0,beta_end(u),u,r),
    O(u,r)=(B_rig u,-leak_rig u,J_end beta_end(u),r,u).

The test space Z and response space R have their supplied sum norms and original componentwise unweighted evaluation. Its bound is one, and

    <E p,O p'>=Q_res(p,p').

For a FIXED observer port o, Hermitian symmetry gives

    Q_res(p,o)=conjugate(<E o,O p>).

Thus define its measured value on ANY response vector y by conjugate(<E o,y>). If ||y-O p||_R<=epsilon, its error is at most

    ||E o||_Z epsilon.

This is a bounded linear/conjugate-linear measurement, according to the chosen slot convention. It neither inverts O nor presumes that noisy y has a source preimage.

## 2. An explicit test norm for the actual observer

Use the supplied witness point z_0=i y, y>gamma>1/2, and

    e_0(u)=exp(-y u),  L_0=L(1/2+y),
    o_0=(e_0,-2L_0 e_0).

Its test norm is bounded, in fact given by the indicated sum-norm expression, by

    C_test=[sqrt(1+y^2)+1+2|L_0|]/sqrt(2(y-gamma))
            +sqrt((y+1/2)^(-2)+(y-1/2)^(-2)).

The endpoint norm here is Euclidean. The negative-side test coordinate is zero, just as in the prescribed source test map. Leakage remains part of the measured response even though this particular observable does not test it.

All spectral evaluation is at the fixed admitted interior point. No boundary continuation or unknown source amplitude division is involved in this test norm.

## 3. Exact finite witness and a source-defined positive margin

Keep the actual first retained diamond on 2,3 and the appended forgotten diamond on 5,7. The two selected balanced sectors have feature ports

    p_i=Psi(f_i)(i y),
    f_1=1_[log 2,log 4] Phi,
    f_2=1_[log 4,log 12] Phi.

Set X_i=X_(f_i)(i y)>0 and mu_i=iX_(f_i)'(i y)/X_i. Their coefficients are +1, and all spectators have unit vacuum observations. The fixed observer eta gives

    Delta=w_seam sqrt(2)(mu_2-mu_1)/(2y)>0.

This remains the exact witness, not a new surrogate source packet.

For an explicit strictly positive lower bound, let a=log 2, c=log 4, b=log 12, b_1=(a+c)/2 and a_2=(c+b)/2. Put h(x)=x tanh(yx), and define the positive normalized masses

    p_1=[integral_a^b1 cosh(yx)Phi(x)dx]/X_1,
    p_2=[integral_a2^b cosh(yx)Phi(x)dx]/X_2.

Monotonicity of h gives

    mu_1<=h(c)-p_1[h(c)-h(b_1)],
    mu_2>=h(c)+p_2[h(a_2)-h(c)].

Hence

    g_*=p_1[h(c)-h(b_1)]+p_2[h(a_2)-h(c)]>0,
    Delta>=Delta_*=w_seam sqrt(2)g_*/(2y).

These are specified positive source integrals, not numerical theta samples. Independently certified lower bounds for them may replace the exact values in a numerical implementation.

## 4. The noise threshold

Let y_i be the measured, labelled, unscaled feature response in the corresponding normalized balanced sector, with

    ||y_i-O p_i||_R<=epsilon_i.

The known seam multiplier, source coefficients, vacua and observer normalizations are retained exactly. Define

    Delta_hat=w_seam [conjugate(<E o_0,y_2>)/X_2
                      -conjugate(<E o_0,y_1>)/X_1].

Then

    |Delta_hat-Delta|
      <=w_seam C_test(epsilon_1/X_1+epsilon_2/X_2).

In particular, if the right side is <=Delta_*/2, then

    Re Delta_hat>=Delta_*/2>0.

For a common error epsilon_i<=epsilon, the explicit half-margin threshold is

    epsilon <= sqrt(2)g_*/[4y C_test(1/X_1+1/X_2)].

The seam multiplier cancels from this per-feature threshold because it scales signal and observation error equally. If noise is instead stated in a physically weighted whole-record norm, retain that norm's fixed multiplier when converting to the feature errors.

The X_i used to specify the fixed observer are assumed known from its source definition. Uncertainty in those calibration constants requires a separate error budget; it is not silently counted as response noise.

## 5. Include the finite-place approximation error

The supplied finite-place response theorem uses the SAME all-prime window residual and gives

    ||O p_i-O_P p_i||_R<=3T_N ||p_i||_V

when P contains every prime <=N. If the measured vector is within epsilon_i of O_P p_i and P_i>=||p_i||_V is a certified bound, replace each error by

    epsilon_i,eff=epsilon_i+3T_N P_i.

Thus the sufficient certificate is

    w_seam C_test sum_(i=1,2) (epsilon_i+3T_N P_i)/X_i
      <=Delta_*/2.

The known explicit tail T_N tends to zero. A cutoff and noise budget can therefore be chosen independently, without changing the window residual to force finite-cutoff agreement.

For a common measurement tolerance epsilon, writing S_X=1/X_1+1/X_2 and S_P=P_1/X_1+P_2/X_2, one may use

    epsilon <= Delta_*/(2w_seam C_test S_X)-3T_N S_P/S_X,

provided the right side is positive.

## 6. Stronger priors are available for these actual ports

Choose 0<delta<y-gamma. The actual exponential ports satisfy Nima's prior

    M_i=||U_i||_(H^2_(gamma+delta))+||V_i||_(H_(gamma+delta))
       =sqrt(2)X_i [sqrt(1+y^2+y^4)+|mu_i-L_0|]
          /sqrt(2(y-gamma-delta)).

In particular P_i may be taken to be M_i. This gives a concrete admissible prior rather than an assumed regularity class for the witness.

For arbitrary admissible candidates on prior balls, the supplied sharp Hölder theorem still bounds their strong-port discrepancy. Combining that discrepancy with the bounded observer form gives a valid Hölder certificate. But the direct test in section 4 is stronger for this fixed observation: its linear estimate requires no reconstruction prior at all, except when a prior is used to budget cutoff or tensor-factor errors.

There is no conflict with inverse instability. Stable evaluation of one known bounded response functional does not reconstruct the entire source.

## 7. Two retained features: a finite projective estimate

Do not identify the witness's two seams with two features. For a genuinely two-feature finite record, specify an actual ordered decomposition

    x=sum_(j=1)^J c_j p_(j,1) tensor p_(j,2),

with its typed labels and prior bounds M_(j,k)>=||p_(j,k)||_V. A stronger source prior may supply these numbers, and the finite projective budget is sum_j |c_j|M_(j,1)M_(j,2).

Let M_O bound O:V->R. If response factors y_(j,k) approximate O p_(j,k) with errors epsilon_(j,k), tensor expansion and the projective norm give

    ||y_(j,1) tensor y_(j,2)
       -O p_(j,1) tensor O p_(j,2)||_pi
    <= M_O[M_(j,2)epsilon_(j,1)+M_(j,1)epsilon_(j,2)]
       +epsilon_(j,1)epsilon_(j,2).

Sum with |c_j|. Apply the EXISTING finite labelled normalization/balancing map N to both exact and measured records; if its bound in the chosen presentation norms is C_N, multiply the resulting error by C_N. With a quotient projective norm the quotient step is contractive; any additional cut normalization retains its independently specified bound.

A fixed descended observer with norm C_eta on the normalized response presentation multiplies this error by at most C_eta. For elementary two-slot tests its norm is bounded by the product of the two one-slot test norms, together with the known label/memory multipliers. Only observers and balancing operations already admitted by the actual paired comparison are used here.

This estimate is for a specified finite decomposition or an independently controlled projective error. It is NOT a theorem lifting nonlinear one-slot Hölder estimates to arbitrary completed tensor sums. No tensor-dual surjectivity or tensor-injectivity assumption is required.

For the actual witness of sections 3--4, there is only one retained feature in each selected sector, so the direct linear estimate applies without a two-factor error term.

## 8. What the certificate means for the attachment class

The exact source packet and its chain map remain those whose source-equivariant nullhomotopy obstruction was already proved. A measured scalar interval excluding zero certifies that exact observation when the declared error bound holds.

An arbitrary noisy record need not be a cycle or a chain map. We do not assign it a derived attachment class. If comparing TWO genuine source-equivariant attachment realizations with exact chain/balancing identities, the same bound guarantees preservation of the nonzero observation under the stated perturbation; the existing finite projective argument then applies to the genuine realization.

Thus the result is a quantitative certificate for the established attachment, not a claim that noise itself preserves algebraic structure.

## Verification

Fresh checks pass:
- `uv run --with sympy python research/voevodsky/checkers/check_noisy_attachment_certificate.py`
- `uv run --with sympy python research/nima/checkers/check_residual_attachment_nonzero.py`
- `uv run --with sympy python research/nima/checkers/check_conditional_labelled_recovery.py`

The new checker verifies conjugate output evaluation, tensor noise expansion, the half-margin threshold and the positive subwindow-gap algebra. Actual balancing and the witness remain checked by their owning finite source checker. The analytic noise estimates are the proofs above.

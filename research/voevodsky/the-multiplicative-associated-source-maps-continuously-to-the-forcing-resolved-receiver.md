# The multiplicative associated source maps continuously to the forcing-resolved receiver

## Result

There is a continuous multiplicative comparison

    completed associated source -> forcing-resolved balanced records
                                 -> normalized analytical balanced records.

It uses explicit radius loss and descends through the actual closed source presentation kernels. It does not identify these completions as the same space or infer forcing norms from analytical output norms.

Consequently the separately convergent bulk, forcing, and vacuum currents can be pulled back to the same completed associated-source algebra whose multiplication was just constructed. Their compatibility is no longer contingent on an unspecified comparison of source topologies.

Inputs:
- `../grothendieck/the-completed-associated-source-is-multiplicative-with-controlled-scale-loss.md`
- `bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`
- `the-forcing-resolved-completion-embeds-faithfully-in-normalized-clark-features.md`

## 1. Construct the forcing lift before taking a quotient

At each finite packet, map a chamber coefficient to its actual forcing function 1_I Phi in H_beta. Disjoint nonzero shell densities make this coefficient map injective. Extend it to ordered tensor histories; projective tensor completion is not needed at this finite stage.

The original terminal recorder is therefore realized in the forcing tensor algebra. Its source kernel I still records zero, and D(I^2)=0 follows from the derivative product rule. Apply the same path derivative and balanced normal-form construction, now with H_beta feature slots rather than their Clark transforms.

This constructs a forcing-resolved associated-layer map j_F. Its finite factorization descent follows from the source-balanced construction, not from assuming a coarse Green form descends. The ordinary normalization removes only artificial cuts, retains seam edges and buffer endpoints, and uses associative forcing-record multiplication.

Use the target presentation with individually shifted seams, Z_(F,r)=(T_F[-1])^(tensor r), for the strict multiplicative identity. Transport to the raw shifted target carries the already prescribed phase c_r=(-1)^(r(r-1)/2).

## 2. Explicit norm comparison

Let a_A>=1 be the fixed analytical letter bound used in the associated-source weights. Let B_0 be the global weighted forcing bound from the theta-tail theorem, and put

    a_F=max(1,max(tau,sqrt(w_seam)) B_0),
    kappa=max(1,a_F/a_A).

On a depth-r source presentation of total length n, a forcing derivative term has norm at most a_F^n. There are at most (1+n)^r terms. The target feature-radius multiplier is b^m with m<=n. The depth graph factor b_s(r) is the same on source and target. Hence

    b_s(r)(1+n)^r b^m a_F^n
       <= b_s(r)(1+n)^r (kappa b a_A)^n.

If F_(s,b) denotes the forcing-resolved projective/cut-l1 target scale, this proves

    ||j_F x||_F(s,b) <= ||x||_X(s,kappa b).

The analytical source parameter b in this estimate is a source path/feature radius, not a change to the fixed physical memory weight tau.

The normalized one-letter transform has norm at most C_feature. Put c=max(1,C_feature). Its tensor transfer Psi satisfies

    ||Psi u||_Y(s,b) <= ||u||_F(s,c b).

Thus the source-to-analytical map factors continuously through F, with overall source radius loss at most kappa c. All-radius intersections absorb these fixed constants.

## 3. Closed-kernel descent and multiplicativity

The forcing lift annihilates every finite associated-layer presentation kernel: both balancing and next-layer relations were removed by the source construction in section 1. The estimate extends it continuously to the presentation completion. It therefore annihilates the closure of those kernels. Taking infima over presentation representatives gives the same bound on the quotient; no bounded section is chosen.

On finite presentations, j_F(xy)=j_F(x) tensor_balanced j_F(y) in the individually shifted target. The associated-source multiplication bound uses input scales (2s,2b), and the forcing tensor bound loses only the depth factor two. Together with the fixed kappa comparison, these give a common input scale controlling both sides. Density extends the equality to the scale intersection.

Psi also commutes with ordered tensoring and the admitted coefficient concatenations. Therefore

    Psi j_F = j_A

as continuous multiplicative maps with the declared suspension normalization. The endpointwise injectivity of j_A implies injectivity of j_F. Independently, Psi is injective on its labelled forcing normal-form domain by the projective tensor separation theorem.

No surjectivity onto the whole forcing-record space is claimed. In particular this is a bridge between different completions, not an identification of their norms or underlying spaces.

## 4. Separately labelled currents on the associated algebra

For a compact spectral set K, choose a forcing radius b large enough for the separate current estimates, for example b^2>=max(1,2 C_total(K)). Each labelled current family then has a continuous bound on F_(s,b), so its pullback along j_F is continuous on X_(s,kappa b).

This applies to bulk, forcing, and vacuum incidence separately, including all newly matching cut shapes. Closed source-kernel descent occurs through j_F itself, so well-definedness of the individual channels is not inferred from cancellation in B+R.

The completed relative sewing and pentagon identities consequently hold for these source-algebra observations. Multiplication concatenates their ordered slot kernels; the root-state factor of a full receiver remains external and is not duplicated by this coefficient-algebra assertion.

## 5. Theta approximation without changing the source quotient

Replacing Phi by Phi_K is a linear substitution on chamber forcing coefficients, compatible with refinement. A zero formal record remains zero under that substitution. Thus the same fixed finite source presentation kernels are annihilated; no new source ideal is defined from a truncated numerical Gram matrix.

Let delta_F=max(tau,sqrt(w_seam)) B_K. Telescoping the feature slots gives at most n delta_F a_F^(n-1) per path term. The extra factor n is paid by an additional source radius two, since n<=2^n. Hence

    ||(j_F-j_(F,K))x||_F(s,b)
       <= (delta_F/a_F) ||x||_X(s,2 kappa b).

This yields quantitative convergence on the EXISTING all-radius source intersection, without introducing another family of source spaces solely for one extra path-length power. The same bound propagates through normalization. Applying the separate bilinear current estimates then proves convergence of each pulled-back channel, not merely its summed Clark numerator.

## 6. Scope

Closed: the explicit comparison from the completed multiplicative associated source to the forcing-resolved receiver, its closed-kernel descent, and continuous separate-current observations on that same source domain.

Not claimed: recovery of the original filtered source from its associated graded, a continuous inverse to the analytical realization, positivity of the source form, or identification of the bulk/forcing labels with the arithmetic gamma/prime decomposition. No independent root states are multiplied.

## Verification

Fresh source checker: `python research/grothendieck/checkers/check_completed_source_multiplication.py` passed all 20736 weight inequalities, 63 forgotten-suffix witnesses, and 1521 phase checks.

New checker: `uv run python research/voevodsky/checkers/check_associated_source_forcing_bridge.py` passed 9216 bridge weight comparisons and 1024 theta-error radius checks. The quotient and completed comparison are the proofs above, not conclusions drawn from finite spectral samples.

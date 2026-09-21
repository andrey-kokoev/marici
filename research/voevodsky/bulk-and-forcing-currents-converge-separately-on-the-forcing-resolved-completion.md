# Bulk and forcing currents converge separately on the forcing-resolved completion

## Strength and scope

Convergence theorem for the separately labelled source Green currents. The bulk and forcing densities extend independently to continuous sesquilinear maps from the weighted forcing domain to L1 spatial currents, uniformly on compact upper-half-plane spectral sets. Their multi-slot products and source collision sums converge on an explicitly forcing-resolved projective/l1 completion.

This closes the separate-channel convergence gate on that source domain. It does not infer forcing-norm control from the weaker output-feature norm, identify bulk/forcing with gamma/prime arithmetic channels, or extend to the real spectral boundary.

Inputs:
- `clark-source-interface-domain-and-positivity-audit.md`
- `weighted-theta-tails-and-path-length-domains-give-uniform-seam-bounds.md`
- `../grothendieck/relative-green-sewing-is-generated-by-slot-collisions-and-tail-flux.md`
- `holomorphic-feature-closure-retains-completed-cross-spectral-packets.md`

## 1. Independent source densities

Let H_beta have norm M_f=||exp(beta x)(1+x)f||_2 on the positive half-line. Fix a compact spectral set with

    eta<=Im z,Im w<=Y<beta,   |z|,|w|<=Z,
    a=beta-Y>0.

For the canonical four ports, let G_a(f;w;x) denote the actual oriented moment tail. For a prescribed constant port matrix M define

    B_M=sum_(a,b) M_ab i(sigma_b z-sigma_a conjugate(w))
                       conjugate(G_a(f;w)) G_b(g;z),

    R_M=sum_(a,b) M_ab [conjugate(x^j_a f) G_b(g;z)
                       +conjugate(G_a(f;w)) x^j_b g].

These are obtained from the tail ODE, not from a desired boundary scalar. Put d(w,z)=-i(z-conjugate(w)), so |d|>=2 eta. Use the already fixed signed matrix A_Cl^* J A_Cl and the signature-transformed matrices A_Cl^* J^(epsilon+delta+1) A_Cl. In the current normalization their entrywise absolute sums S_M are four; keeping S_M explicit makes the bound independent of that simplification.

## 2. Separate absolute-integral estimates

The prior source audit supplies, for every port,

    |G_a(f;z;x)| <= M_f exp(-beta x)/sqrt(2a),
    ||G_a(f;z)||_2 <= M_f/(2 sqrt(beta a)),
    ||x^j f||_2 <= M_f, j=0,1.

Therefore, without using cancellation between B and R,

    ||B_M/d||_L1 <= C_B M_f M_g,
    C_B=S_M Z/(4 eta beta a),

    ||R_M/d||_L1 <= C_R M_f M_g,
    C_R=S_M/(2 eta sqrt(beta a)).

The bulk estimate uses |sigma_b z-sigma_a conjugate(w)|<=2Z and Cauchy--Schwarz on the two tails. The forcing estimate applies Cauchy--Schwarz separately to its two source-tail products.

Exactly the same argument on [L,infinity) gives BOTH estimates with an additional factor exp(-2 beta L):

    ||G_a(f)||_L2(L,infinity) <= M_f exp(-beta L)/(2 sqrt(beta a)),
    ||x^j f||_L2(L,infinity) <= M_f exp(-beta L).

Thus each channel has a uniform spatial tail, independently of any cancellation in their sum.

## 3. Continuous extension and the boundary identity

For either channel A=B/d or R/d, its sesquilinearity gives

    ||A(f,g)-A(f_K,g_K)||_L1
      <= C_A [||f-f_K||_beta ||g||_beta
               +||f_K||_beta ||g-g_K||_beta].

All norms can be taken uniformly over the compact spectral set. Tail dependence is continuous in the spectral parameters by dominated convergence; the same estimates dominate the relevant densities. Hence these are continuous maps into C(K x K;L1(R_+)).

Compact source approximations converge in H_beta. The independently derived finite source identity consequently extends with separate absolutely convergent integrals:

    h_f(w)^* M h_g(z)/d(w,z)
      = integral B_M(x;w,z)/d(w,z) dx
        + integral R_M(x;w,z)/d(w,z) dx.

The flux at infinity vanishes by the pointwise tail bound. Each pair keeps its own d(w,z). No aggregate denominator, positive-sign hypothesis, or inference from a sampled matrix is used.

## 4. Theta truncation is uniform in packet windows

For f=1_E Phi and f_K=1_E Phi_K, the weighted theta theorem gives

    ||f-f_K||_beta<=B_K,  ||f||_beta,||f_K||_beta<=B_0,

uniformly over all event windows E in x>=log(2). Therefore each one-slot channel error is at most

    2 C_A B_0 B_K.

Spatial truncation error is at most C_A B_0^2 exp(-2 beta L). These two errors can be controlled independently. This proves convergence, not merely agreement of the final B+R sum.

## 5. Preserve every labelled product channel

For d retained features use d independent spatial variables. A channel label is a word in {B,R}^d (with its prescribed observer matrix in each slot). Tonelli's theorem and the one-slot estimates give

    ||product_i A_i(f_i,g_i)||_L1(R_+^d)
       <= product_i C_(A_i) ||f_i||_beta ||g_i||_beta.

Summing the norms over all 2^d channel labels is bounded by

    C_total^d product_i ||f_i||_beta ||g_i||_beta,
    C_total=max_M(C_B+C_R).

The sum here is a norm of a labelled direct sum, not a cancellation of channel values. The vacuum incidence channel remains a separate scalar summand with empty product one.

For window theta data, simultaneously truncating all factors changes this labelled family by at most

    2d C_total^d B_0^(2d-1) B_K.

Outside the spatial cube [0,L]^d, the labelled absolute integral is at most

    d exp(-2 beta L) C_total^d product_i ||f_i||_beta ||g_i||_beta.

The union bound accounts for which spatial coordinate exceeds L; no coordinates are identified.

## 6. The completion must retain forcing control

Use projective tensor products of H_beta for the source feature slots, and the l1 sum over typed shapes. Keep existing memory/seam norm multipliers and add b^d for d retained features. Keep the depth graph weights from the all-depth scale if allowing unbounded seam depth. This is a stronger SOURCE topology, not a new relation metric or an inverse bound for the feature map.

Choose b^2>=max(1,2 C_total). Then the slot-current bound after weighting is at most 2^(-d), and the extra d factor in the spatial-tail estimate is uniformly bounded. Consequently collision sums constructed from newly matching shapes converge absolutely in the labelled L1-current direct sum, uniformly on K x K. Their tails are bounded by exp(-2 beta L) times the two source norms.

On algebraic source windows, add the corresponding feature-degree and extra path-length weight to obtain the displayed uniform theta errors. Density extends the separately labelled current maps to the forcing-resolved completion. The earlier bounded feature map supplies a continuous map from this stronger source domain into the analytical receiver; its inverse is neither assumed nor needed.

This is not a theorem that separate source currents are continuous on every vector of the output-only holomorphic feature closure. The forcing topology is explicit and essential to the proof.

## 7. Refinement and sewing

Convex packet inclusions preserving an old event forcing leave all its tails, spatial densities, and spectral indices unchanged. Finite-support packet approximations in the stated l1 completion converge in the source norm. The separate-channel estimates therefore allow packet limits, theta truncation limits, and spatial integration limits to commute on this domain.

At finite level the nested-cut and pentagon currents are the same labelled products selected by first new matches. Their continuous extensions remain equal channel by channel. Spatial interface terms use the same transported tail state on both sides of a cut; approximation does not reset that state.

Thus completed relative sewing is now justified with BULK, FORCING, and VACUUM INCIDENCE retained separately on this forcing-resolved domain.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_separate_bulk_forcing_bounds.py`

Exact noncompact exponential-forcing fixtures verify independent absolute-integral majorants and the boundary identity for signed and opposite-signature-parity channels. For beta=3, eta=7/4, Y=Z=9/4, both matrices give C_B=4/7 and C_R=16/21. The infinite-dimensional extension, uniform tails, and product convergence are proved above; no quadrature or finite spectral-rank surrogate is involved.

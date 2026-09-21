# Weighted theta tails and path-length domains give uniform seam bounds

## Result and fixed data

For the declared completed theta forcing on x>=log(2), its truncations converge with an explicit packet-independent bound in the weighted forcing norm. Path-length weights then give continuous finite-depth seam observations into the cut-l1 carrier, including an operator-norm truncation estimate on a slightly stronger source domain.

This is a continuity/convergence theorem, not completed source injectivity or a claim about the unmodified cut-l2 topology.

Use the atom already defined in `clark_feature_evaluator.py`:

    Phi_n(x)=exp(x/2) [2(pi n^2 exp(2x))^2-3 pi n^2 exp(2x)]
             exp(-pi n^2 exp(2x)).

Fix beta>0 and the norm ||f||_beta=||exp(beta x)(1+x)f(x)||_L2([log 2,infinity)). The spectral region and normalized two-sheet sewing matrix A_Cl stay fixed, with eta<=Im z<=Y<beta.

## 1. An explicit completed-theta bound

Put y=exp(2x), y0=4, p=beta+13/2, and c=pi y0/2. For y>=4,

    1+(log y)/2 <= y,
    |Phi_n(x)| <= 5 pi^2 n^4 y^(9/4) exp(-pi n^2 y).

Since dx=dy/(2y),

    ||Phi_n||_beta^2
      <= (25 pi^4 n^8/2) integral_(y0)^infinity
                                  y^(p-1) exp(-2 pi n^2 y) dy.

The inequality 2 n^2 y >= n^2 y0 + y gives

    ||Phi_n||_beta <= C_beta n^4 exp(-c n^2),
    C_beta=(5 pi^2/sqrt(2)) sqrt(pi^(-p) Gamma(p,pi y0)).

For K>=0 define

    r_K=16 exp(-c(2K+3)),
    B_K=C_beta (K+1)^4 exp(-c(K+1)^2)/(1-r_K).

Here r_K<1. The ratio of successive n^4 exp(-c n^2) terms for n>=K+1 is at most r_K. Minkowski's inequality and the resulting geometric bound prove

    ||Phi-sum_(n=1)^K Phi_n||_beta <= B_K.

The series converges absolutely in this Hilbert norm. This also justifies its identification with the pointwise completed sum, for example by dominated absolute convergence using the same majorant. In particular M=||Phi||_beta<=B_0 uniformly over every finite packet window.

The bound is conservative. For beta=3, the numerical regression gives B_1 about 4.04e-9 and B_2 about 4.64e-22. These rounded decimals are illustrations, not interval-certified endpoints; the displayed formula is the analytic bound.

## 2. Transfer to normalized Clark letters

The existing trace estimate, now applied on the whole positive half-line, gives

    ||Lhat(f)|| <= C_feature ||f||_beta,
    C_feature=||A_Cl|| sqrt(mu(Omega)/((beta-Y) eta)).

Multiplying by an event-window indicator cannot increase the weighted forcing norm. Thus every event feature has norm at most C_feature B_0, and replacing Phi by Phi_K changes it by at most C_feature B_K, independently of the window and packet.

The full traces, including first moments, are retained. No shell-by-shell point normalization or underflow-dependent rescaling occurs.

## 3. A source domain for finite-depth derivatives

Let the degree-one memory norm multiplier be tau and the independent seam-feature norm multiplier be sqrt(w_seam), with unit vacuum/Omega. Set

    a=max(1, max(tau,sqrt(w_seam)) C_feature B_0).

A marked path of length n has every individual history/seam term bounded by a^n. The ordinary derivative sums n terms. The r-fold ordered distinct-seam expansion sums binomial(n,r) terms. For a specified r-factor product of paths of lengths n_i, the tensor of local derivatives has product_i n_i terms, bounded by binomial(sum_i n_i,r): each choice marks one site in each consecutive block.

Consequently the map on finite path or factorization presentations is bounded by the weighted l1 source norm

    ||x||_(r,a)=sum_P |x_P| (1+length(P))^r a^(length(P)).

Use the corresponding total-length weight for factorization presentations, retaining endpoint labels. Its seam image has cut-l1 norm at most ||x||_(r,a). Normalization then has norm at most one by `packet-uniform-relative-sewing-bounds-use-cut-l1-not-cut-l2.md`.

If passing to a balanced quotient, use the quotient seminorm and divide by its zero seminorm before completing, equivalently the quotient by the CLOSED balancing subspace in this Banach presentation. Continuity and vanishing on algebraic balancing extend to its closure. This supplies a continuous map but does not prove there are no additional completed kernel elements.

This defines an explicit weighted domain; it is not an estimate on all degree-adic histories or the unweighted path space. For r=3 it supplies the intended finite-depth bound without holding event length fixed.

## 4. Uniform truncation error for the receiver and its relative forms

Put delta_K=max(tau,sqrt(w_seam)) C_feature B_K. Both full and truncated letters obey the same a bound, by the absolute atom majorant. Telescoping a tensor of at most n features gives an error at most

    n delta_K a^(n-1)

per term. Therefore full and truncated depth-r maps P and P_K satisfy

    ||(P-P_K)x||_cut-l1 <= (delta_K/a) ||x||_(r+1,a).

The extra power of path length pays for the telescoping sum. Thus convergence is in operator norm on this stronger domain, uniformly over packets. Normalization preserves the bound.

On that domain both P and P_K have norm at most one. Any of the admitted integrated fine/coarse forms or a single collision correction has norm at most one in the cut-l1 topology. Hence its pullback changes by at most

    2(delta_K/a) ||x||_(r+1,a) ||y||_(r+1,a).

For a difference of two collision corrections use twice this constant. This estimates the integrated relative pairing; it does not claim pointwise evaluation is bounded on arbitrary completed L2 features. Full spectral labels remain in the underlying finite source-current identity.

## 5. Verification and remaining separation issue

`uv run --with mpmath python research/voevodsky/checkers/check_weighted_theta_tail_and_path_bounds.py`

The checker compares the analytic tail bound with incomplete-gamma atom-majorant sums at five cutoffs and checks the seam counting bounds. The regressions are not interval arithmetic. The proof above supplies the infinite tail estimate.

Combined with the cut-l1 estimate, this closes continuity of normalization, integrated relative forms, finite-depth path observations, and uniform theta truncation on the stated stronger domain. What is not proved is injectivity of the completed balanced source or compatibility of every possible packet refinement with its quotient topology. These cannot be inferred from finite ranks or from a uniform upper bound.

# Relative theta-tail control preserves the actual-letter Fox domain

## Result

The theta substitution gate in `../grothendieck/actual-letter-weights-characterize-marked-fox-summability.md` has a positive answer for the declared forcing on x>=log(2). There is a UNIFORM RELATIVE tail bound, independent of the event window and its location. It yields operator convergence of the full Fox family on the actual-letter domain with radius loss two, and separate-current convergence on that same enlarged domain.

The argument uses positivity of the individual theta atoms as source functions. It does not imply positivity of the signed Clark form.

## 1. Relative atom majorant

Write t=pi exp(2x). On x>=log(2), t>=4pi>12. The declared atoms are

    Phi_n(x)=exp(x/2) n^2 t (2 n^2 t-3) exp(-n^2 t).

Every atom is positive. Moreover

    Phi_n/Phi_1
      = n^2(2 n^2 t-3)/(2t-3) exp(-(n^2-1)t)
      <= (8/7)n^4 exp(-12(n^2-1)).

The polynomial bound follows from 2t/(2t-3)<=8/7 for t>=12. Let Phi_K=sum_(n<=K) Phi_n and, for K>=1, set

    r_K=16 exp(-12(2K+3)),
    epsilon_K=(8/7)(K+1)^4 exp(-12((K+1)^2-1))/(1-r_K).

The successive majorant ratios for n>=K+1 are at most r_K<1. Since Phi>=Phi_1>0,

    0 <= (Phi-Phi_K)/Phi <= epsilon_K < 1.

The bound tends to zero rapidly and holds on the ENTIRE admitted half-line. For illustration epsilon_1 is about 4.242e-15; the exact exponential expression, not this rounded decimal, is the certificate.

## 2. A bounded relative substitution on forcing space

On the H_beta subspace supported in [log(2),infinity), define the multiplication operator

    M_K f = (Phi_K/Phi) f.

Then

    ||M_K||<=1, ||1-M_K||<=epsilon_K,
    ||M_K^(-1)||<=1/(1-epsilon_K).

For an actual event forcing f_e=1_(E_e) Phi, its truncation is exactly M_K f_e. Thus

    ||f_e-f_(e,K)||_beta <= epsilon_K ||f_e||_beta

uniformly even for arbitrarily small late-window letters. The same statement holds for complex shell combinations, since it is an operator estimate, not an inference from a positive linear combination.

It does not provide a relative lower bound on normalized Clark OUTPUT norms. The forcing-to-feature map remains compact, and its cancellations are a separate issue.

## 3. The maximal actual-letter domain is unchanged

Let gamma_e=sqrt(w_seam)||f_e||_beta, and let gamma_(e,K) use f_(e,K). The operator inequalities give

    (1-epsilon_K) gamma_e <= gamma_(e,K) <= gamma_e.

For a length-n path with d<=n retained letters,

    (1-epsilon_K)^n Gamma(w) <= Gamma_K(w) <= Gamma(w).

Therefore the actual-letter factorial seminorms obey

    Q_R^(K)(x)<=Q_R(x),
    Q_R(x)<=Q_(R/(1-epsilon_K))^(K)(x),

rounding noninteger radii upward as necessary. The all-radius domains and their locally convex topologies agree for EVERY K>=1. This includes their intersection with the earlier common-path source and its record ideal.

The substitution is a linear map on the chamber forcing letters and extends by ordered tensoring. It preserves zero formal records, multiplication, and the balancing identities. It is not a new numerical source ideal defined by a truncated Gram matrix. Any root-state substitution must be made through its declared source operations; no root state is silently duplicated.

## 4. Uniform convergence of the summed jets

Each retained slot changes by at most epsilon_K times its forcing norm, while the truncated slot norm is no larger. Telescoping a d-slot projective tensor gives error at most d epsilon_K times the product of its original letter norms.

Use the exact marked Fox bound from the supplied note. For t=2 lambda s, summing over all k cuts of a length-n word bounds the total error by

    2 n epsilon_K n! (t b)^n Gamma(w).

Since n<=2^n,

    ||(D-D^(K))(x)||_F(s,b)
       <= 2 epsilon_K Q_(ceil(4 lambda s b))(x).

Thus the full jet substitution converges in operator norm from the indicated stronger seminorm on S_Gamma into every prescribed forcing receiver scale. This is stronger than pointwise convergence on finite sources and works on the enlarged marked domain that need not belong to the unweighted factorial source.

The zero-seam terminal record is included for the full algebra; on the record ideal it vanishes as before.

## 5. Separate currents and compatible operations

Fix a compact spectral interior and a feature radius large enough for the separate bulk/forcing current estimate. Let its labelled sesquilinear current map have norm C in that forcing scale, and put M=ceil(2 lambda s b). Both D and D^(K) have norm at most 2 Q_M on source vectors. The two-term difference estimate gives

    ||Current(Dx,Dy)-Current(D^(K)x,D^(K)y)||
       <= 8 C epsilon_K Q_(2M)(x) Q_(2M)(y).

This applies to the separately labelled bulk and forcing families and their admitted collision sums. Vacuum incidence is unchanged. The norm includes the spatial L1 and compact-spectral controls of the earlier theorem, so it does not rely on cancellation between bulk and forcing.

The uniform multiplicative substitution commutes with convex packet inclusions and word concatenation. Normalization and jet-order truncation keep their established bounds. Consequently theta cutoff, source approximation, jet-order cutoff, and the separately controlled spatial integrations converge compatibly on this actual-letter domain.

No evaluation at the spectral boundary, quotient of a nonzero relation direction, or new signed metric is introduced.

## Verification

Fresh `python research/grothendieck/checkers/check_marked_fox_summability_domain.py` passed 1456 all-order estimates, 4282 typed probes, 40 projection checks, and 124 relation-weight tests.

`uv run --with sympy --with mpmath python research/voevodsky/checkers/check_relative_theta_letter_truncation.py` passes the exact polynomial inequalities and tensor/radius controls. High-precision relative-atom fixtures are regressions only; the infinite relative bound is the geometric-series proof above.

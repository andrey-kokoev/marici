# General bilinear photon IR logs: a convergent physical-window kernel

[Contract](contracts/bilinear-photon-ir-series.v1.json) · [checker](check_bilinear_photon_ir_series.py) · [receipt](results/bilinear-photon-ir-series.v1.json)

## 1. Generalize the homogeneous audits without claiming an all-orders S matrix

The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) completed the first coupled homogeneous coefficient. Here construct a bilinear rule for every pair of Taylor degrees and prove an explicit convergence/remainder domain for the resulting **IR momentum series at fixed pure g2^4 order**. This is not convergence in the coupling or construction of the full quartic amplitude.

Keep the same conditional scalar-response family, no added massless poles and independent dimensionful couplings. The leading kernel is built from

    R(s)=sum_(k>=2) r_k*s^k,
    r2=c0, r3=c1, r_(n+4)=a_n/pi,
    a_n=n!*(n+1)!/(2*n+3)!.

The last equality is only the preceding contact-spectral-density control, not source-licensed UV matching. The real c0,c1 remain free. Other leading tensor structures or independent g3 contributions are not identified with this pure coefficient.

## 2. Ordered bilinear cut rule

Let e_kJ and h_kJ be the normalized monomial moments E_kJ,H_kJ of the photon-cut audit, u_k=1+e_k0 and v_k=-e_k0. For k,l>=2, m=min(k,l), q=k+l, define

    d0_kl=(u_k*u_l+v_k*v_l)/16,
    O_kl=(v_k*v_l-u_k*u_l)/16,
    D_kl(z)=d0_kl+sum_(even J=2..m) (2*J+1)*e_kJ*e_lJ*P_J(z)/8,
    M_kl(x)=sum_(J=2..m) (2*J+1)*h_kJ*h_lJ*x^2*P_(J-2)^(0,4)(2*x-1)/16.

These are **ordered-pair coefficients**. The full cut is sum_(k,l>=2) r_k*r_l*s^(k+l) times the usual four-helicity matrix with D_kl,O_kl,M_kl. For k!=l both orderings occur; do not multiply by another two. One pair at k=l reproduces the old monomial result, and two pairs at k!=l reproduce the interference audits. Positivity belongs to the complete coherent square A^dagger*A/8, not to individual signed coefficients or uncontrolled truncations.

This is also an executable homogeneous functional: for degree q sum k=2,...,q-2 with l=q-k. It retains the Bose normalizations, odd-J mixed sectors and all higher-J contributions when they first occur. The checker independently extracts degrees 4 through 10 from a four-term squared amplitude and compares normalized scalar and mixed-helicity projections.

## 3. Crossed logs and degreewise local running

For each ordered pair use the parent's field-strength logarithmic sections with q=k+l and D_kl,O_kl,M_kl. Let H_kl,a be their three channel coefficients, and H_kl=sum_a H_kl,a. Then

    B_log=-(1/pi)*sum_(k,l) r_k*r_l*sum_a H_kl,a*log(-S_a/nu),
    d B_local/d log(nu)=-(1/pi)*sum_(k,l) r_k*r_l*H_kl.

Nu>0 is an arbitrary fixed squared-mass reference. The leading r_k are held fixed at this perturbative order. This is not a running of g2,g3, a selected physical scale or a complete EFT anomalous-dimension matrix.

Every H_kl is a local polynomial tensor. D has degree at most m and only even powers; M starts at degree two. Thus the mixed sections have nonnegative powers S^(q-j-2)*(T-U)^j and S^(j-2)*T^(q-j), and the all-equal sections have S^(q-2). The lower bounds q-j>=max(k,l)>=2 and q-j-2>=0 forbid artificial Mandelstam poles. The field-strength vertices retain Ward covariance, pairing sums retain Bose/crossing covariance and proper Lorentz covariance holds degree by degree. Three-plus/one-minus logarithmic sections vanish here without excluding finite/rational terms.

For scalar parity, put sign=-1 or +1 and M_kl(x)=sum_j m_j*x^j. The universal rule is

    kappa=d0_kl+sign*O_kl,
    lambda=2*(-1)^q*sum_j m_j/(q-j+1)
           +sign*2*(-1)^q*O_kl/(q+1),
    Gamma=kappa+lambda.

The finite angular moment replaces each 1/(q-j+1) by -1/(q-j+1)^2, and similarly for the off-diagonal term. Odd and even crossing signs are both retained. General running is specified by its degreewise local tensor, without claiming a minimal off-shell operator basis at every degree. An infinite sum of these polynomials is not thereby a finite-derivative local density or a microcausality proof.

## 4. A genuine crossed-series majorant

The right-cut response has radius four, but that does not establish convergence of the crossed angular reconstruction. Use an independent coefficient bound.

The exact factorial moment formulas imply |e_kJ|,|h_kJ|<=1 and vanishing for J>k. Hence |u_k|<=2, |v_k|<=1 and |d0_kl|,|O_kl|<=5/16. For the monomial coefficient l1 norm,

    ||P_J(z)||_1 <=3^J,
    ||P_(J-2)^(0,4)(2*x-1)||_1 <=16*8^(J-2) <=8^J.

The first follows by induction from the Legendre recurrence. For the second, write n=J-2 and expand sum_m binom(n,m)*binom(n+4,n-m)*x^m*(x-1)^(n-m). Its norm is at most 2^n*binom(2*n+4,n)<=16*8^n by Vandermonde and the binomial sum.

For physical s>0, the three invariants are s,-s*alpha,-s*(1-alpha), 0<=alpha<=1. Any same-duality pairing has |S|,|T|,|U|<=s and |T-U|<=2*s. The pure-helicity phases 4*W/S^2 or -4*W/S^2 have modulus one away from their coordinate zeros; use the polynomial tensor extension at collinear limits. Define

    N_kl=sum_j |D_j|*2^j+2*sum_j |M_j|+3*|O_kl|.

This bounds each helicity entry and the sum needed for either equal-helicity scalar parity projection. It is not asserted to be a normalized full angular-operator norm. Using sum_(J=0..m)(2*J+1)=(m+1)^2,

    N_kl <=5/4+(m+1)^2*(6^m+8^m)/8
         <=(m+1)^2*8^m
         <=(9/4)*4^(k+l).

For the last inequality, (m+1)^2<=(9/4)*2^m holds at m=2 and propagates because ((m+2)/(m+1))^2<2. Then 2*m<=k+l gives the stated bound.

The moment bounds hold at every degree, not just tested degrees. For example |e_kJ| is maximal at J=0, and |h_kJ| at J=2, since the successive factorial ratios decrease; the maxima are 1/(k+1) and 1/(k+3). The exact checker supplies finite combinatorial witnesses, while these recurrences and inequalities give the general argument. They are documented mathematics, not a machine-formalized all-degree proof.

For the spectral input, a0=1/6 and a_(n+1)/a_n=(n+1)/(2*(2*n+5))<1/4. With pi>3,

    |r_k|<=A*4^(-k),    A=16+16*|c0|+64*|c1|.

In particular 4^(n+4)*a_n/pi<=256/(6*pi)<16. The deliberately loose A also covers r2,r3 without fixing either subtraction coefficient. Consequently an ordered pair contributes at most (9/4)*A^2*s^(k+l) to the cut/scale coefficient bound. There are q-3 ordered pairs at degree q.

## 5. Endpoint logarithms, convergence and explicit tails

For a physical channel ratio a=|S_a|/s in [0,1], its logarithm on the upper section has magnitude at most |log(s/nu)|+|log(a)|+pi. Each coefficient multiplying log(a) carries a power a^n with n>=2 (n=q in the all-equal case, n=q-j in the others). Since a^n*|log(a)|<=1, every angular endpoint is controlled, with zero at a=0 interpreted continuously. No collinear pole or infinite angular logarithm was dropped.

It follows that the crossed logarithmic series converges absolutely, uniformly in physical angle, for **0<s<1**. This is a certified sufficient domain, not a maximal radius, an arbitrary complex-kinematics domain or the whole 0<s<4 subthreshold interval. At this order its right-cut entries agree with the coherent cut functional by absolute summation. The degreewise scale functional also converges there.

If all homogeneous degrees through Q>=4 are retained, define

    U_Q(s)=(9/4)*A^2*sum_(q>Q)(q-3)*s^q
          =(9/4)*A^2*s^(Q+1)*[(Q-2)/(1-s)+s/(1-s)^2].

For each physical helicity entry and either scalar parity projection:

- the right-cut coefficient error is at most U_Q(s);
- the generated scale-running error is at most U_Q(s)/pi;
- the logarithmic-kernel error is at most U_Q(s)*[1+|log(s/nu)|+pi]/pi.

These are absolute errors for B at fixed pure g2^4 order; the full T carries b^2. No estimate of the unknown finite analytic matching amplitude follows. They also do not bound a coupling-series remainder.

For a reproducible comparison only, take c0=c1=0 and nu=1, without declaring either choice source-selected. On the entire 0<=s<=1/2 window, use s^q*|log s|<= (1/2)^(q-1), pi>3 and pi<4. This gives the uniform log-kernel tail

    error <=(7/3)*U_Q(1/2)=1344*(Q-1)/2^Q.

The extension at s=0 is continuous. At Q=40 this is <10^(-7); at Q=48 it is <10^(-9). The checker evaluates these rational inequalities and independently verifies the geometric tail identities. This certifies truncation without computing every retained degree in the example. Nonzero real c0,c1 are covered by the same formula with A^2 replacing 256.

## 6. What remains free, and the next executable gate

Convergent generated running does not imply convergence of an arbitrary finite counterterm series. Its independent constants could have different growth, and neither their values nor their convergence are selected here. The density extrapolation, physical scale, native preparation and source licensing remain unestablished. No full quartic amplitude, complete UV theory, exact scattering operator, physical rate or branching ratio is constructed. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings remain unchanged.

The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded.

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Distinguish these calculable moments from the global dispersion/growth assumptions needed for physical matching bounds.

```sh
python -S research/scattering/low-energy/check_bilinear_photon_ir_series.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_bilinear_photon_ir_series.py
```

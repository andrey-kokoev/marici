# Native mixed/capped two-point classification at arbitrary clocks

Owner `marici.Kitaev`; spatial-scaling iteration10/10. Selected node `issue-tree:87b983be841a61be1b85d24a:native-clock-classification:v1`.

## 1. Precisely classified family

Keep dyadic h=2^-n,arbitrary centered exhausting physical open boxes,the actual SU2 Hamiltonian/vacuum,once-counted squares,and0<eta_h<27/262144 at every mesh. Use the DECLARED canonical bare matching and magnetic-minus-electric trial

A_h(f)=-kappa_h sum_e f(mid_e)C_e-lambda_h sum_p f(center_p)w_p,
kappa_h=g_H^2/(2h),lambda_h=4/(h*g_H^2),eta_h=8/g_H^4.

All means are subtracted in the actual vacuum Omega_h. The clock is arbitrary:s_h>0,sigma_h=s_h*kappa_h, K_h=s_h(H_h-E_0,h). Define the effective amplitude

a_h=8eta_h/h^5>0.

The following theorem classifies THIS native trial and its preceding test-independent bounded Gauss-compatible Casimir-capped version. It does not classify arbitrary composite readers,opposite-sign near-Ward-null combinations,or a newly constructed infinite-volume electric representation. Bare matching is a declared convention,not nonperturbative calibration or a Lorentz-field identification.

**Theorem at written analytic scope.**

1. The joint two-point family is bounded in S'(R8) IF AND ONLY IF there are constants C,N,independent of h,with

   a_h<=C(1+sigma_h)^N.                               (1)

2. Every S'-bounded subsequence with sigma_h->infinity tends to ZERO jointly in S'(R8).
3. A full nonzero joint tempered limit exists IF AND ONLY IF

   a_h->a_*>0 and sigma_h->sigma_* in[0,infinity).       (2)

   Its necessarily unique kernel is

   W_*(t,x;s,y)=(3a_*/4)exp[-i3sigma_*(t-s)]delta^3(x-y). (3)

   The same criterion applies to a nonzero subsequential limit after restriction to that subsequence.
4. The full limit is ZERO if and only if(1) holds and,for every fixed M>0,

   a_h*1_(sigma_h<=M)->0.                             (2z)

   This includes interlaced small-amplitude and escaping-clock regimes; neither a_h->0 nor sigma_h->infinity is individually necessary for a zero full limit.

Every nonzero kernel(3) fails the relativistic forward-cone spectrum condition and is not Lorentz invariant. Zero amplitude at any clocks gives zero. S'-boundedness alone does NOT imply convergence when finite parameters oscillate.

The proof uses the already written actual-source coercivity,Ward/cap comparisons,source gap and compact-parameter outer-volume theorem. Uniform boundedness on Schwartz space,positive spectral measure estimates,functional calculus and the nuclear Schwartz tensor theorem are explicit analytic imports. Exact finite controls do not independently certify them.

## 2. Source estimates valid before any clock limit

Let v_h(f) be the actual centered vacuum vector of A_h(f). The Ward magnetic proxy has coefficient m_h=-2lambda_h/h^3 and squared amplitude |m_h|^2 h^3=a_h. With a fixed spatial weighted C1 Schwartz seminorm p_1,the actual source estimates give

||v_h(f)||<=C sqrt(a_h) p_1(f),
||v_h(f)-v_proxy,h(f)||<=C sqrt(a_h) h p_1(f).          (4)

The constants are independent of eta_h,box and clock. In particular no first energy moment for the MIXED electric vector is presumed; it is not supplied by the magnetic moment bound.

All these vectors are orthogonal to the actual vacuum. The retained physical full-domain source gap gives

K_h >= gamma*sigma_h on that orthogonal subspace,
gamma=5/64.                                         (5)

This is the actual interacting source gap,not a selected fast correlator or the charged one-link kinetic value.

There is also a MOVING spectral-window lower bound. Fix one nonzero real f in C_c^infinity and put I_h=h^3 sum_p f(center_p)^2->I=3 integral f^2>0. The positive proxy measure has mass>=a_h I_h/512 and first moment<=12sigma_h a_h I_h. Thus its mass below L sigma_h,with L=12288,is>=a_h I_h/1024.

Choose0<=rho<=1,smooth even compact support in[-2L,2L],equal to1 on[-L,L]. This is ONE fixed function rescaled by sigma_h,not a fixed target energy test. Apply rho(K_h/sigma_h) to both actual vectors in(4). The proxy filtered norm is>=sqrt(a_h I_h)/32; the mixed error is O_f(sqrt(a_h)h). Eventually the mixed filtered norm is at least half that lower bound,uniformly in sigma_h and eta_h. Therefore its positive spectral measure mu_h^f satisfies

mu_h^f([0,24576sigma_h])>=a_h I_h/4096>=c_f a_h,       (6)

with c_f>0 fixed. This derivation transfers a magnetic spectral estimate through a contraction; it does NOT infer a mixed first moment or equality of operators from a vacuum-channel identity.

## 3. Joint tempered boundedness forces polynomial amplitude

Assume the joint two-point family is S'-bounded,meaning pointwise bounded against every Schwartz test. Fix f above. Stationarity permits extracting its relative-time distribution without evaluating at a sharp time: for phi in S(R),choose chi in S(R) with integral chi=1 and set

Psi_phi(t,x;s,y)=phi(t-s)chi(s)f(x)f(y).

This is a continuous linear map S(R)->S(R8). Its pairing is exactly the relative-time correlation distribution C_h^f(phi). No spatial translation invariance is required. Fourier transformation is a continuous Schwartz isomorphism,so the positive spectral measures mu_h^f form an S'-bounded family on the energy line.

Schwartz space is barrelled. Uniform boundedness therefore supplies ONE finite Schwartz seminorm and constant controlling all these measures. Write its weight/derivative orders using a sufficiently large integer N. Choose a nonnegative smooth compact cutoff theta equal to1 on[-1,1],and theta_R(E)=theta(E/R) for R>=1. Its seminorm grows at most C_theta R^N. Positivity gives

mu_h^f([0,R])<=mu_h^f(theta_R)<=C R^N.                (7)

This is proved from tempered boundedness,not assumed as a spectral regularity axiom. Signed measures would not license the first inequality. Taking R=max(1,24576sigma_h) and using(6) proves(1). In particular bounded clocks force bounded amplitude without a continuum sharp-time vector or a separately assumed positive-time clock witness.

## 4. Inverse-gap integration by parts uses TIME tests only

For u in S(R4) define its actual smeared vacuum vector

V_h(u)=integral exp(itK_h)v_h(u_t)dt.

The centered inverse K_h^-1 is bounded by(gamma sigma_h)^-1. Repeated integration by parts in t gives,on the vacuum-orthogonal subspace,

V_h(u)=(-1/i)^k K_h^-k integral exp(itK_h)v_h(partial_t^k u_t)dt.

To justify it,start with K_h^-1 v_h(u_t),which lies in Dom(K_h),integrate its strong derivative,and use Schwartz decay to remove endpoints. Iterate. The electric vectors themselves need not lie in Dom(K_h^k). No spatial/group derivative of the vacuum or the drift is taken. Thus(4)-(5) imply

||V_h(u)||<=C sqrt(a_h)(gamma sigma_h)^-k p_k(u),      (8)

where p_k bounds time derivatives of the TEST through order k and spatial derivatives through order1. The k=0 bound is also valid. The nuclear Schwartz tensor theorem extends the resulting two-point bounds to a fixed continuous joint projective seminorm q_k:

|W_h(Psi)|<=C_k a_h sigma_h^(-2k) q_k(Psi), sigma_h>=1. (9)

For sigma_h<=1,use the k=0 bound.

If(1) holds,choose2k>=N. The two clock ranges give a common Schwartz bound,proving the sufficiency of(1). If in addition sigma_h->infinity,choose2k>N; then (9) tends to zero jointly in S'. This proves spectral escape is weak-zero for EVERY tempered escaping-clock subsequence,even if its unsmeared variance diverges. A polynomial energy-window estimate is necessary here; a gap alone with arbitrarily fast growing amplitude would not suffice.

The common-cap family differs from the mixed family by O(h) in a fixed joint seminorm,uniformly in clock and box. Hence their tempered boundedness and all joint limits are identical. No inverse-gap estimate for a hypothetical infinite electric operator is invoked.

## 5. Exhaust all possible nonzero limits

Suppose W_h converges to a nonzero tempered distribution. A convergent distribution sequence is S'-bounded by uniform boundedness,so(1) applies. If sigma_h were unbounded,a subsequence would escape to infinity and have zero limit by section4,a contradiction. Thus clocks are bounded. Equation(1) then bounds a_h.

If a subsequence had a_h->0,the k=0 vector bound in(4) would give zero jointly at ANY clocks,again a contradiction. Therefore a_h is eventually bounded away from0. Parameter pairs lie in a compact set [a_min,A] times[0,M]. Every parameter-convergent subsequence is covered by the preceding compact-parameter outer-volume theorem,with c_h=a_h/8,and has kernel(3).

For a_*>0 these kernels identify their parameter pairs uniquely: their relative-time spectral measures are nonzero atoms at energy3sigma_* with mass proportional to a_*. This uniqueness is a statement about explicit measures,not a sharp-time evaluation of an arbitrary limiting distribution. Two distinct cluster pairs would give two distinct limits. Compactness and uniqueness of the cluster pair therefore force the full convergence(2).

Conversely,(2) is exactly the preceding compact-parameter construction on arbitrary exhausting outer boxes,including sigma_*=0. It gives(3). Restricting this proof to any converging subsequence gives the subsequential classification as well.

For completeness,the zero-limit criterion(2z) follows from the same estimates. Necessity: a zero convergent family is bounded; if amplitude did not vanish along some bounded-clock subfamily,compactness would supply a positive-amplitude finite-clock cluster pair and hence a nonzero kernel. Sufficiency: under(1),choose2k>N. For sigma_h>=M>=1,(9) is uniformly O(M^(N-2k)); for sigma_h<=M,the k=0 bound tends to zero by(2z). First choose M large,then h small. This proves joint zero convergence and allows interlaced regimes. No all-orders existence theorem is inferred from identifying two-point limits.

## 6. Native path controls and scientific consequences

The theorem makes three distinct outcomes concrete:

* Finite positive a_*,finite sigma_*>=0: the explicit nonzero ultralocal kernel(3).
* Fixed retained eta_0>0 and sigma_h=1/h: a_h=8eta_0 h^-5=8eta_0 sigma_h^5. The family is tempered but tends to ZERO. With k=3,(9) is O(h) in a fixed higher-time-test seminorm. This is an actual interacting source example,not only the free-endpoint escape control.
* a_h=1/h,sigma_h=log_2(1/h)=n: eta_h=h^4/8 lies in the retained window eventually,but amplitude grows faster than every polynomial in sigma_h. This ACTUAL source trial is not S'-bounded. Declaring all escaping-clock paths zero would be false without temperedness.

Bounded parameters can also oscillate and give distinct nonzero cluster kernels. Thus boundedness is not full convergence. At sigma_*=0 the spectral measure is supported on E=0 with Lebesgue spatial momentum; it is not an atom at the spacetime origin. For any nonzero a_* and any finite sigma_*,the measure

(3a_*/4)delta_(3sigma_*)(dE)d^3p/(2pi)^3

has positive weight outside |p|<=E. All nonzero canonical-trial limits are therefore nonrelativistic. This is not a proof that every conceivable retained observable is trivial,nor a claim of Yang-Mills construction. A nonzero Lorentz-scalar successor must change or independently justify a premise outside this classified native branch (source regime,observable/renormalization class,calibration or faithful tempered comparison); relabeling its clock does not suffice.

## 7. Verification and completion boundary

Exact controls test moving-filter mass,rescaled positive Schwartz cutoffs,inverse-gap time-test powers,polynomial sufficiency and escape planners,actual retained parameter paths,kernel injectivity and oscillating-parameter failures. The predecessor order-audit receipt is freshly replayed. Finite checks do not certify uniform boundedness,functional calculus,nuclear Schwartz theory or the upstream actual interaction construction. Independent analytic review and the full physical/continuum/root gates remain open.

The ten-turn CANONICAL-TRIAL classification branch is complete at written analytic scope. The broader retained-observable objective still has one concrete,previously noted nonredundant constructor: critical MAGNETIC normalization h^(3/2) sum_p f(x_p)w_p at a FIXED eta>0. This is not the bare energy-density trial,whose amplitude then diverges. Its interacting temporal susceptibility need not equal the free oscillator atom. Existing coercivity gives nonzero bounded fluctuation vectors,and joint source clustering gives a summable Euclidean spatial covariance kernel. Derive its orientation-summed lattice susceptibility,spatial white-noise scaling and positive temporal spectral measure,or identify the first failed implication. Check lattice translation invariance,finite-box boundary comparison and real-time recovery rather than assuming a central limit theorem. No all-orders Gaussian claim or new Hamiltonian is needed for that two-point constructor. It remains an executable continuation of the declared retained-observable objective,not a waiting leaf or a revival of the deferred macroscopic-loop audit.

Contract: `contracts/yang-mills-native-clock-classification.v1.json`.
Checker: `checkers/check_yang_mills_native_clock_classification.py`.
Receipt: `results/yang-mills-native-clock-classification-v1.json`.

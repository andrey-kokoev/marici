# Windowed photon dispersion: a representative, not UV matching

[Contract](contracts/windowed-photon-dispersion.v1.json) · [checker](check_windowed_photon_dispersion.py) · [receipt](results/windowed-photon-dispersion.v1.json)

## 1. A definite finite-window prescription

The [bilinear audit](BILINEAR-PHOTON-IR-SERIES.md) constructed a convergent logarithmic kernel at fixed pure g2^4 order in the conditional scalar-response family. It left the analytic part unspecified. Here construct **one crossing-compatible finite-window Cauchy representative**, decompose its analytic remainder and bound truncation of that remainder. This does not determine the unknown physical matching term.

Use the same real r_k, with c0,c1 free and r_(n+4)=a_n/pi only in the unlicensed contact-spectral-density control. No extra massless pole or identification with independent dimensionful g3 couplings is supplied. T=(b/2)*A+b^2*B+... remains the normalization.

For a pure-duality section, factor a channel log coefficient as H_c=W_c*P_c(S,T,U). In the all-equal sector W_c is that channel's pair-vertex product and P_c=-4*O_kl*S_c^(q-2). In the two-plus/two-minus sector all three channels share the same-duality pair-vertex product W; P_c are the polynomial coefficients of the parent audit, including their factor four. All external vertices are held fixed when defining the following form-factor prescription.

For each channel c write z=S_c and Delta for the difference of the other two invariants, in a fixed ordering. Define its symmetric flow by

    S_c(x)=x,
    S_other1(x)=(-x+Delta)/2,
    S_other2(x)=(-x-Delta)/2.

It preserves the sum-zero relation, returns the external invariants at x=z, and is equivariant under channel permutations (swapping the other two labels sends Delta to -Delta). Let p_c(x,Delta)=P_c evaluated on this flow. Define

    B_tau=(1/pi)*sum_(k,l,c) r_k*r_l*W_c
                     *integral_0^tau p_c(x,Delta_c)/(x-S_c) dx.

Use the analytic Cauchy function off [0,tau] and its upper-rim boundary value inside the interval. This is an explicit **choice of off-cut continuation for tensor form factors**, not a fixed-t dispersion relation derived from a local QFT. Other prescriptions can differ by analytic terms. Pairing sums, symmetric flows and field-strength vertices retain Bose/crossing, Lorentz and Ward covariance.

## 2. Exact decomposition and branch audit

For a polynomial p(x)=sum_n c_n(Delta)*x^n, polynomial division gives

    integral_0^tau p(x)/(x-z) dx = p(z)*I_tau(z)+J_tau[p](z),
    I_tau(z)=log(tau-z)-log(-z),
    J_tau[p](z)=sum_(n>=1) c_n(Delta)
                         *sum_(h=0..n-1) tau^(n-h)*z^h/(n-h).

J is polynomial in the external invariants at each ordered input degree. On the upper physical rim,

    Im I_tau(z)=pi,    0<z<tau;
    Im I_tau(z)=0,     z<0 or z>tau.

For z>tau both logarithms have the same negative imaginary part and it cancels. The endpoint z=tau is an artificial branch point of the finite window. It is **not** the charged threshold at four, a new physical particle or a source-selected scale. Zero coefficients multiplying log(0) at a collinear physical limit are interpreted by the parent's continuous polynomial-times-log limit.

For 0<s<tau the physical right-cut residue is exactly the parent's H_s, since the flow at x=s returns the external invariants. Crossed invariants are negative there. The representative alone cuts off this contribution above tau; that is not a claim that the true spectrum ends there. Matching/completing the spectrum beyond the window is still necessary.

Do not discard J when p(z)=0. For example the ordered k=l=2 all-equal coefficient is p(x)=(5/12)*x^2. At z=0 and tau=1/2 it has p(z)=0 but J=5/96. After the external vertex factor this is an analytic contact contribution. The checker also retains a forward mixed-duality channel with H=0 but W*J nonzero. In general the window generates lower-degree analytic powers as well as the same-degree logarithm: the prescription does not select renormalized finite Wilson coefficients.

## 3. The calculable analytic remainder

Relative to the parent's arbitrary positive squared-mass reference nu,

    B_tau=B_log,nu+E_tau,nu,
    E_tau,nu=(1/pi)*sum_(k,l,c) r_k*r_l*W_c
              *[p_c(S_c,Delta_c)*log((tau-S_c)/nu)+J_tau[p_c]].

The massless logarithm cancels in E. Its reference derivative is -sum r_k*r_l*H_kl/pi, exactly cancelling d B_log/d log(nu). J has no nu dependence. Thus this prescription supplies one calculable analytic trajectory with the required running, not selected physical integration constants.

The distinction is essential: E_tau,nu is the analytic remainder **of this representative**. If a full completion is matched by an additional IR-analytic term, that term's values and bounds are independent data. No norm bound on unknown UV matching, no convergence of an arbitrary finite counterterm series and no complete amplitude are inferred here.

## 4. Normal convergence and analyticity of coefficient functions

One must establish more than the parent's physical-angle convergence to call E analytic. Its polynomial locality supplies the needed stronger bound. Put q=k+l, d=q-2. Each p_c(x,Delta) is homogeneous of degree d, with nonnegative powers. In the coefficient l1 norm the symmetric flow's linear forms have norm at most one, and any difference of two flow invariants has norm at most two. The parent's N_kl therefore gives

    sum_c ||p_c||_1 <=4*N_kl <=9*4^q.

For either scalar parity, include both relevant chiral sections; the same N includes their sum. No full angular-operator norm is asserted.

Before vertex products, the original P_c coefficient polynomials satisfy the same bound in a complex Mandelstam polydisc |S|,|T|,|U|<=b, S+T+U=0. Since |r_k|<=A*4^(-k), A=16+16*|c0|+64*|c1|, their normally convergent series is bounded on every b<1 by

    sum_(k,l,c) |r_k*r_l*P_c| <=9*A^2*b^2/(1-b)^2.

Consequently the summed coefficient functions are holomorphic on this constrained polydisc. This is a limited coefficient-domain result, not arbitrary complex-kinematics analyticity of a full scattering operator.

Choose 0<tau<1 and an external polydisc of size a<=tau/2. Along 0<=x<=tau, |Delta|<=2*a<=tau and both flowed complementary invariants have magnitude at most tau. The polynomial coefficient series therefore converges normally on the integration paths. In J, each monomial obeys

    |Delta|^(d-n)*sum_(h=0..n-1) tau^(n-h)*|z|^h/(n-h)
      <=tau^d/(1-a/tau)<=2*tau^d.

Thus the normally convergent J series has bound 18*A^2*sum_(q>=4)(q-3)*tau^(q-2) before vertex products. The remaining logarithm log((tau-S_c)/nu) is holomorphic for |S_c|<tau. These estimates prove analyticity of E near the origin and justify the summed Cauchy decomposition off the cuts and its retained physical boundary values. B_tau itself still has the massless cuts.

General normal-convergence, Cauchy and tensor arguments are documented mathematics, not machine-formalized proofs. The exact checker verifies polynomial division, coefficient norm witnesses, branch signs and all-outgoing/Ward/Lorentz identities. It does not promote those finite witnesses to a machine-formalized all-degree theorem.

## 5. A certified input-degree truncation tail

Let U_Q be the bilinear audit's tail after retaining all input degrees q<=Q. For physical entries or either scalar parity on 0<=s<=a<=tau/2, the omitted analytic remainder is bounded by

    |delta E| <= (1/pi)*[U_Q(a)*(|log(tau/nu)|+a/(tau-a))
                        +2*(a/tau)^2*U_Q(tau)].

The first term bounds the analytic logarithm. The second bounds J, using the physical |W_c|<=s^2/4. Note the appearance of U_Q(tau), not merely U_Q(s): polynomial division transfers higher input degrees into lower external-momentum analytic powers. This is an input-degree truncation estimate, not a claim that E starts at external degree Q+1.

As a comparison only, set tau=1/2, a=1/4, nu=tau and c0=c1=0. Using pi>3 gives the rational certificate

    |delta E| <= [U_Q(1/4)+(1/2)*U_Q(1/2)]/3.

It is <10^(-8) at Q=40 and <10^(-10) at Q=48. These numbers bound the representative's analytic remainder tail, **not the unknown physical UV matching remainder**. No window or subtraction choice is source-selected.

## 6. Scope and nonredundant successor

This constructs a retained-window photon-cut representative with a controlled analytic remainder in the conditional model. It is not a full pure-g2^4 amplitude, all-orders unitary S matrix, UV completion or native preparation. Finite/rational amplitudes in omitted helicity sectors remain unexcluded. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings are unchanged. No physical rate, branching ratio or coupling identification follows.

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not this representative's Taylor coefficients or finite matching bounds.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom.

```sh
python -S research/scattering/low-energy/check_windowed_photon_dispersion.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_windowed_photon_dispersion.py
```

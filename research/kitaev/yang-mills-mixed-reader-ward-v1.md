# Local electric/magnetic Ward comparison and normalization threshold

Owner `marici.Kitaev`; spatial-scaling iteration7/10. Selected node `issue-tree:87b983be841a61be1b85d24a:mixed-reader-ward:v1`.

## Question and disposition

Magnetic covariance coercivity does not extend to arbitrary mixed readers: the source eigen-equation has an exact global null direction(1,-eta). Does the actual interaction construction quantify the error for spatially varying tests,and distinguish noncancelling candidates?

**Written source-conditional result.** Let u=log Omega modulo constants and r_e=(C_e Omega)/Omega=C_e u-|gradient_e u|^2. For every finite actual source,0<h<=1 and real smooth f supported in a physical cube of half-side L>=1,

norm(center_nu[sum_e f(mid_e)r_e-eta sum_p f(center_p)w_p])_L2(nu)
 <= S_R*Lip(f)*sqrt(C_L/(1-beta))*h^-1/2,               (1)

R=(4096/3)eta<9/64, S_R=R+(8/3)R^2,beta=R/2,
C_L=6c^3+36c^2+216c+624,c=2L+6.

The constant is independent of the finite source volume,including arbitrarily distant boundaries. It is an upper rate,not an optimal asymptotic expansion. A uniformly translated cube has the same constant. Complex tests follow by real/imaginary decomposition with the sum of their Lipschitz seminorms.

For the centered vacuum channel of the mixed candidate

A_h(f)=h^3[z_E(h)sum_e f(mid_e)C_e+z_B(h)sum_p f(center_p)w_p],

put m_h=z_B+eta z_E and a_h=|m_h|^2 h^3. Its vacuum vector differs from that of the ACTUAL magnetic proxy m_h*h^3 sum_p f(center_p)w_p by at most

|z_E| S_R*Lip(f)*sqrt(C_L/(1-beta))*h^(5/2).            (2)

For same-sign real z_E,z_B,this is a relative O(h) error on the nonzero magnetic channel,uniform in retained coupling. At bounded clocks,a_h->infinity forces fixed-Schwartz mixed two-point divergence. For bounded a_h,the mixed/proxy difference tends to zero JOINTLY in S'(R8). No individual limit or Lorentz identification is supplied by that comparison.

A conditional canonical energy-density-difference trial has a_h=8eta_h/h^5. This distinguishes divergent,critical and weak-zero normalizations instead of claiming every retained coupling path diverges. Next execute the actual positive-coupling critical path eta_h=c*h^5,with a quantified source-to-free comparison; do not replace its vacuum by Haar without estimating the error.

## 1. Support-wise Ward identities from the actual fixed point

Retain the actual constructed decomposition u=sum_A Phi_A. Nonempty labels are connected unions of plaquettes,|A|>=4,and

sup_i sum_(A containing i)2^|A| W(Phi_A)<=R.

Use A0 for the unweighted Fourier trace norm. For each label A and e in A define

r_(A,e)=C_e Phi_A-sum_(B union C=A)Gamma_e(Phi_B,Phi_C),
Gamma_e(v,w)=sum_a (X_ea v)(X_ea w).

Terms with e outside the relevant support vanish. Ordered pairs B,C are counted exactly as in Gamma(u,u). The actual component fixed-point equation,after applying the electric L=sum_e C_e,is

L Phi_A=eta*1_(A is an elementary square p)*w_p
 +sum_(B union C=A)[Gamma(Phi_B,Phi_C)-Haar(Gamma(Phi_B,Phi_C))].

Here the original fundamental trace p in Phi_1=p/6 is2w_p,so L(w_p/3)=w_p; no factor2 is silently changed. Consequently

sum_e r_(A,e)=eta*1_(A=p)*w_p-k_A,                    (3)

where k_A is the Haar mean of the quadratic sum,a scalar. Also sum_A r_(A,e)=r_e. The relation is an actual vacuum-channel identity; C_e is NOT being replaced by multiplication by r_e on arbitrary states.

All operations use at most the retained Casimir-weighted second derivatives and first derivative products. Absolute Fourier control justifies termwise application on each finite source. No third derivative is assumed.

## 2. A charged anchored norm for the electric-channel components

Let V_A=sum_e ||r_(A,e)||_A0. The kinetic contribution satisfies

sum_e ||C_e Phi_A||_A0<=W(Phi_A).

The existing edge activity estimate is

||Gamma_e(v,w)||_A0<=3m_e(v)m_e(w),sum_e m_e(v)<=(2/3)W(v).

Anchor an output label at i and split i in B or C. In either half,the inner activity sum over C containing e is<=(2/3)R,and the outer activity sum over B containing i is<=(2/3)R. Union weights satisfy2^|B union C|<=2^|B|2^|C|. Thus the raw quadratic term costs at most2*3*(2R/3)^2=(8/3)R^2. It follows that

sup_i sum_(A containing i)2^|A| V_A<=S_R.              (4)

This charges derivatives before counting supports. It does not take a spatial derivative of r_e or of C_e Phi_A. The source window also gives

S_R <= (5632/3)*eta.                                 (5)

At eta=0 all these components vanish exactly.

## 3. Anchors,centering and physical variation of the test

For an elementary-square label choose its anchor x_A=center_p. For every other label choose the midpoint of a deterministic edge of A. Connectedness implies |mid_e-x_A|_infinity<=h|A|. Put f_A=f(x_A),f_e=f(mid_e),and

G_A(f)=sum_e(f_e-f_A)r_(A,e), G(f)=sum_A G_A(f).

Multiplying (3) by f_A gives the EXACT finite-source identity

center_nu[sum_e f_e r_e-eta sum_p f_p w_p]=center_nu G(f). (6)

The omitted term before centering is -sum_A f_A k_A,which is a scalar,not a source-mean-zero assertion about Gamma. Haar component centering and actual vacuum centering are different operations; (6) accounts for both.

For real f,write Lip(f)=sup_x sum_j|partial_j f(x)|. Then

||G_A(f)||_infinity<=h|A|*Lip(f)*V_A.

Locality of the support labels,not a formal global Ward identity alone,is what makes this error small. At first order the four midpoint average equals the center value for affine f,but not generally for quadratic f. Thus exact cancellation at arbitrary spatial weights is false. No optimality of the O(h) relative estimate is claimed.

## 4. Localized oscillation sum: no extensive-volume factor

Suppose supp f is in[-L,L]^3 and let B=[-L-1,L+1]^3. The same proof works about any center. For an arbitrary source link i put

k_i=floor(dist_infinity(mid_i,B)/h)>=0.

If G_A(f) is nonzero,at least one edge midpoint or its chosen anchor has nonzero f. Thus A contains an edge midpoint in B. This also holds for square-center anchors,since h<=1. Connectedness then gives |A|>=k_i for every i in A.

For every integer n>=4,n^2<=2^n; equivalently n*2^(-n/2)<=1. The base case is equality at4,and the next-step ratio is at most25/32<1 after squaring. Reserve half of the exponential support weight in (4). The single-link oscillation of G satisfies

delta_i(G)<=2h*Lip(f)*S_R*2^(-k_i/2).                 (7)

To sum its square,each of the three shifted link grids has at most[2(L+1)/h+2k+4]^3 points with k_i<=k. Therefore

sum_i 2^(-k_i)<=3h^-3 sum_(k>=0)2^-k(2L+6+2k)^3
=C_L h^-3.                                          (8)

The geometric moments are sum 2^-k=2,sum k2^-k=2,sum k^2 2^-k=6,sum k^3 2^-k=26. Finite boxes are subsets of these grids. This is why arbitrarily large exterior boxes cause no error,whereas a uniform oscillation bound multiplied by their total volume would fail.

## 5. Finite-source covariance comparison completes the proof

The actual conditional influence has the symmetric majorant

C_ij=2 sum_(A containing i,j) W(Phi_A), i!=j,C_ii=0,
row(C)<=R/2=beta<9/128.

The existing normalized-likelihood/Dobrushin covariance argument applies directly in each finite source. Its real continuous-cylinder estimate is

Var_nu(G)<=1/4*delta(G)^T (I-C)^-1 delta(G)
<=1/[4(1-beta)]*sum_i delta_i(G)^2.

The final step is the symmetric Schur bound,not an l1 oscillation estimate. Apply (7)-(8) to obtain(1). For complex f,apply the real bound to real and imaginary parts and use the sum of their Lipschitz seminorms. Functions containing C_e Phi_A need only be continuous here; no higher derivative is hidden in the comparison.

Multiplication by the actual normalized Omega is an isometry L2(nu)->L2(Haar). Projection off its vacuum span is actual vacuum centering. This proves(2) for the original unbounded electric vacuum channel. Existing bounded Casimir cap removal remains an independent observer operation on the same Hamiltonian and vacuum.

## 6. Mixed normalization,near-null directions and growth

For a fixed nonzero spatial f whose support is eventually covered by the source boxes,let I_h(f)=h^3 sum_p|f(center_p)|^2->3 integral|f|^2>0. The preceding magnetic theorem bounds the proxy vector norm below by

|m_h| h^(3/2)*sqrt(I_h(f)/512).

When m_h!=0 define t_h=h*|z_E|*S_R/|m_h|. Equation(2) is at most a test-dependent constant times t_h relative to this lower norm. Thus t_h->0 gives relative vacuum-channel agreement. Same-sign real coefficients obey

|m_h|=|z_B|+eta|z_E|, t_h<=(5632/3)h.                 (9)

This includes arbitrarily small positive coupling nets,not just fixed eta. At eta=0 the electric vector and Ward defect are exactly zero. If m_h=0,do not divide: (2) only bounds the remaining local Hamiltonian-density channel. Opposite-sign coefficients can approach this null direction so rapidly that t_h fails to tend to zero; the same-sign conclusion cannot be extended to them.

Relative comparison alone is not absolute two-point convergence when vector norms diverge. For divergence use an actual filter. At sigma_h<=M,choose the previous real Schwartz g with0<=g_hat<=1 and g_hat=1 on[-12288M,12288M]. The actual magnetic proxy has filtered norm at least

|m_h| h^(3/2)*sqrt(I_h(f))/32.

The filter is a contraction,so if t_h->0 the mixed filtered norm is eventually at least half this lower bound. Hence the SINGLE fixed spacetime test u(t,x)=g(t)f(x) satisfies

W_mix,h(conjugate(u) tensor u)>=|m_h|^2*h^3*I_h(f)/4096. (10)

If a_h=|m_h|^2 h^3->infinity,this forces nonboundedness in S'(R8). The same contraction argument with exp(-tau K/2),using the preceding magnetic Jensen lower bound,gives positive-time divergence at every fixed tau>=0 under the same conditions. This uses the actual interacting dynamics,not the free excitation3sigma.

## 7. Joint tempered source-to-source Ward comparison

A uniform joint comparison is also available in the finite-amplitude regime; it is NOT inferred merely from tensor-test pointwise convergence.

First extend (1) to spatial Schwartz tests. Use a smooth partition of unity by translates of fixed compact cubes. Bound each piece by the translated L=1 estimate. The sum of its Lipschitz seminorms is bounded by a fixed weighted C1 Schwartz seminorm (a power4 spatial weight suffices in dimension3). Summing the Hilbert norms gives

||v_mix,h(f)-v_proxy,h(f)||<=C |z_E| S_R h^(5/2) p_1(f),
||v_proxy,h(f)||<=C |m_h|h^(3/2) p_1(f),

uniformly in box and coupling. The second estimate uses magnetic l2 upper coercivity and the uniform weighted grid count. The partition constants are finite fixed analytic constants,not cutoff-dependent.

Time-smear these vacuum vectors with the SAME actual unitary dynamics. Integration of the spatial seminorm over time is bounded by a Schwartz seminorm p on S(R4). For tensor tests,the two-point difference is bounded by

C a_h*(t_h+t_h^2)*p(u)*p(v).                          (11)

The Schwartz kernel/nuclear-space theorem identifies the completed projective tensor product S(R4) tensor_pi S(R4) with S(R8). Consequently (11) extends to all joint tests with a fixed continuous projective Schwartz seminorm q(Psi). This standard topological theorem is an explicit analytic import; a finite tensor sample does not certify it.

For same-sign coefficients and bounded a_h,the difference tends to zero jointly in S'(R8),at rate O(a_h*h). If a_h->0,the proxy and mixed families themselves tend to zero in S',uniformly in clocks. If a_h stays bounded away from0,this proves identical limits IF an individual family converges,not existence or uniqueness. Arbitrary diverging a_h is not covered by absolute cap/Ward comparison solely because t_h->0; equation(10),not an invalid convergence claim,is the applicable growth witness.

This is a vacuum two-point comparison,not equality of operators or multitime products. In particular C_e Omega/Omega must not be substituted for C_e inside general operator strings.

## 8. Conditional bare-matched energy-density-difference trial

Keep separate the classical motivation and the quantum target. After removing its vacuum constant,the native magnetic-minus-electric energy-density trial has

z_E=-kappa_h/h^3,z_B=-lambda_h/h^3.

These coefficients have the same sign. The exact Ward effective coefficient is m_h=-2lambda_h/h^3,not zero; the opposite-sign conserved-Hamiltonian direction is a different observable.

Under the previously DECLARED canonical matching for once-counted squares,

kappa_h=g_H^2/(2h),lambda_h=4/(h*g_H^2),eta_h=8/g_H^4,

a_h=4lambda_h^2/h^3=64/(g_H^4*h^5)=8eta_h/h^5.         (12)

This is a conditional bare convention,not a proved nonperturbative anisotropy calibration or identification with a renormalized Lorentz scalar. Take eta_h>0 at each mesh if using this finite-g formula; eta=0 is its limiting endpoint,not a finite-g matching.

Equations(9)-(12) show:

* eta_h/h^5->infinity: at bounded source clocks the actual mixed trial fails fixed-test tempered boundedness.
* eta_h/h^5->0: the centered two-point family tends to zero jointly in S',at ANY clock.
* eta_h/h^5 remains finite nonzero: the Ward error vanishes absolutely and leaves a critical ACTUAL magnetic-proxy limit question. Neither existence nor Lorentz covariance follows yet.

Thus fixed retained eta has the growth obstruction,but a universal divergence statement for every retained coupling path would be false. A critical path can carry a nonzero nonrelativistic source channel; that possibility must be calculated rather than declared a physical continuum theory.

## 9. Falsifiers,verification and next executable construction

Exact controls check support-wise scalar/centering identities,edge-activity anchored bounds,physical midpoint defects at first order,exponential support reserve and shell moments,symmetric covariance resolvents,same-sign and near-null coefficient budgets,fixed-filter growth,and the corrected canonical threshold. They freshly replay the previous magnetic coercivity receipt. They do not certify the all-spin interaction constructor,Schwartz nuclear theorem or source analytic limits. Independent review remains open.

Next execute a specific POSITIVE-coupling critical sequence eta_h=c*h^5 with c>0,fixed sigma>0,and slowly expanding physical boxes,for example radius proportional to log(1/h). Compare its ACTUAL vacuum and unitary dynamics quantitatively to the free finite source before taking the spatial limit. The interaction's total bounded-potential norm is small on that chosen exhausting net; a residual/gap estimate can be much sharper for the vacuum vector than a global density-ratio bound. Pay the growing magnetic reader norms and lift the comparison jointly in S'(R8). Only then combine with the known free fluctuation limit and this Ward theorem. This could construct an explicit native nonzero mixed two-point limit while exposing its relativistic failure. No all-orders Gaussian or Lorentz/physical claim is licensed in advance.

Contract: `contracts/yang-mills-mixed-reader-ward.v1.json`.
Checker: `checkers/check_yang_mills_mixed_reader_ward.py`.
Receipt: `results/yang-mills-mixed-reader-ward-v1.json`.

# Native bounded electric/magnetic readers and vacuum-tail comparison

Owner: `marici.Kitaev`. Spatial-scaling iteration4/10. Selected issue: `issue-tree:87b983be841a61be1b85d24a:electric-magnetic-reader:v1`.

## DPC and disposition

**Problem.** The scalar/locality theorem assumes bounded cutoff readers. The actual electric Casimir is unbounded. Can a bounded Gauss-compatible observer approximate its physical-vacuum two-point functions after growing normalization,without changing the Hamiltonian or smuggling in higher regularity?

**Conjecture.** The retained weighted FOURIER norm,not a second moment alone,controls a conditional one-link exponential. SU2 representation dimension growth then supplies a uniform high-spin L2 tail for Casimir times the actual vacuum. A common measurement cap gives bounded linear reader maps and quantitative joint tempered cap removal.

**Rivals.** Replace the source by a spin-truncated Hamiltonian; confuse a moment bound with uniform integrability; omit the Fourier representation dimension; use an extensive global vacuum density ratio; choose test-dependent caps and lose linearity; require only vacuum-vector error even when normalized two-point norms diverge; infer Lorentz covariance or a continuum limit from a classical candidate formula.

**Risky consequence.** For spin cutoff S in half-integers,the source vacuum obeys ||Q_(j>S) C_e Omega||<=K_R/sqrt(2S+2),where C_e=-Delta_e and K_R=e^R*(exp(2R)-1)/2<=288/1265<1/4 in the retained window. This vanishes at the actual free source. A common cap can preserve finite-exponential norm budgets and remove itself in S'(R8),without constructing a continuum field.

**Strong falsifiers.** Uniform second moments can retain tail norm1. A spin-dependent rank-one Fourier example distinguishes the required d_j factor from an incorrect d_j^-1 rate for the norm. Polynomial vacuum-vector convergence alone can leave two-point errors uncontrolled; the reader cap must pay for the other diverging vector too.

**Disposition.** The conditional tail,Gauss-compatible candidate and cap-removal comparison are established below from the actual interaction input. Actual Lorentz convergence/nontriviality is NOT established. Next executable test is the exact free-source magnetic fluctuation scaling: identify a native nonzero ultralocal limit or the first growth failure,rather than call every limit zero or call a candidate Tr(F^2).

## 1. Source retained; conditional one-link factorization

At every actual finite open box,

Omega_Lambda=Z_Lambda^-1/2*exp(sum_(A subset Lambda) Phi_A),
N2(Phi)=sup_e sum_(A containing e)2^|A| W(Phi_A)<=R<9/64,
W(f)=sum_pi d_pi*(1+C_pi)*||f_hat(pi)||_1,
C_pi=sum_e j_e(j_e+1).

This is the previously written actual-vacuum interaction construction. Its harmonic analysis and fixed-point identification remain upstream unreviewed analytic inputs. No surrogate density is selected here.

Fix one link e and write the remaining configuration as z. Put

u_e(g,z)=sum_(A containing e)Phi_A(g,z), F_e(g,z)=exp(nu_e(g,z)),
Omega_Lambda(g,z)=c_e(z)*F_e(g,z).

Here c_e includes normalization and all interactions not meeting e. It need not have a volume-uniform pointwise bound. The anchored norm gives |nu_e|<=R. Therefore F_e is between exp(-R) and exp(R),and normalization alone gives

integral |c_e(z)|^2 dHaar(z)<=exp(2R).

This replaces an invalid extensive global max/min comparison.

## 2. One-link Fourier restriction and exponential algebra

Define on SU2

W_e(f)=sum_(j in half-integers>=0) d_j*(1+C_j)*||f_hat(j)||_1,
d_j=2j+1,C_j=j(j+1).

Evaluating all other group variables maps the product Fourier space boundedly into this one-link space,with norm at most1. In fact a product coefficient with pi=(j,rho) contributes

d_rho*Tr_rho[(I tensor rho(z))*f_hat(j,rho)]

to the j coefficient. Partial trace is trace-norm contractive,and multiplication by the unitary rho(z) preserves trace norm. The single-link weight1+C_j is at most1+C_(j,rho). Sum the absolute Fourier coefficients. This proves uniformly in z,

W_e(nu_e(.,z))<=sum_(A containing e)W(Phi_A)<=R.

All spins occur in this conditional kinematic function: do NOT substitute the physical loop Casimir3 for the one-link spectrum.

For two one-link functions,the Clebsch-Gordan decomposition has output spin l<=j+k and

1+C_l<=2(1+C_j)(1+C_k).

Indeed C_l<=2(C_j+C_k). Fourier-algebra multiplication,unitary Clebsch-Gordan block decomposition and trace-norm pinching give

W_e(fg)<=2 W_e(f)W_e(g).

To see the dimension accounting explicitly,the tensor coefficient d_j d_k(f_hat_j tensor g_hat_k) splits into diagonal l blocks; its output Fourier coefficient contains d_j d_k/d_l. In W_e the output d_l cancels that denominator. The sum of trace norms of the diagonal blocks is bounded by the input trace norm. Thus no dimension factor is lost.

Expand the exponential in this complete weighted algebra. Since W_e(1)=1,

W_e(F_e-1)<=sum_(n>=1)2^(n-1)*R^n/n!=(exp(2R)-1)/2=:B_R.

This bound controls derivatives through Casimir weight,not arbitrary higher derivatives. It does not require gauge invariance of the conditional one-link function.

## 3. The high-spin vacuum tail,with the SU2 dimension gain

Let Q_(>S) project onto spins j>S on link e. For S in half-integers,the smallest such dimension is d_min=2S+2. For any f with finite W_e,set a_j=d_j*(1+C_j)*||f_hat_j||_1. Plancherel and HS norm<=trace norm give

||Q_(>S) C_e f||_2^2
=sum_(j>S)d_j*C_j^2*||f_hat_j||_HS^2
<=sum_(j>S) a_j^2/d_j
<=[sum_(j>S)a_j]^2/d_min.

C_e kills constants,so apply this to F_e-1,then integrate the conditional factor c_e. It follows that Omega belongs to the local Casimir domain and

||Q_(>S) C_e Omega_Lambda||
<=exp(R)*B_R/sqrt(2S+2)=K_R/sqrt(2S+2).

The bound is uniform over link,box and every retained eta. It is a single-link Hilbert estimate in the ACTUAL normalized vacuum,not a common global Haar-density assertion. In particular ||C_e Omega||<=K_R/sqrt(2),using S=0.

For0<=R<=9/64,the elementary exponential/geometric bounds give

K_R<=Kbar_R:=R/[(1-R)(1-2R)]<=288/1265<1/4.

At R=0 the bound is0,as C_e annihilates the free constant vacuum. The norm rate is d_min^-1/2; claiming d_min^-1 from these data would be too strong for general conditional matrix coefficients.

A uniform bound on ||C_e Omega|| alone would NOT prove this tail rate. For example,vectors with squared mass L^-2 at a Casimir eigenvalue L have bounded second moment but unit norm of the Casimir-weighted high-energy tail as L increases. The extra weighted trace-Fourier input and d_j growth do the work.

## 4. Bounded Gauss-compatible readers; only observations are capped

Let M_S=S(S+1) and define the soft cap

C_e^[S]=min(C_e,M_S)

by spectral functional calculus. It is bounded,self-adjoint,of norm M_S,and supported on one link. It commutes with both left and right regular SU2 actions,hence with every vertex gauge transformation. The Hamiltonian,Hilbert space,Gauss constraint and actual vacuum remain UNCHANGED; all high-spin source states remain present.

Because0<=C_e-C_e^[S]<=C_e*Q_(>S),

||(C_e-C_e^[S])Omega||<=K_R/sqrt(2S+2).

Also ||C_e^[S]Omega||<=||C_e Omega||. Thus both capped and uncapped vacuum vectors have the same uniform primitive bound. The square-plaquette multiplication w_p=(1/2)Tr W_p is already bounded by1 and gauge invariant.

For real finite coefficients define a CANDIDATE

A_h(f)=sum_e a_(e,h)(f) C_e+sum_p b_(p,h)(f) w_p,
A_(h,S)(f)=sum_e a_(e,h)(f) C_e^[S]+sum_p b_(p,h)(f) w_p.

The uncapped operator is used on its actual smooth finite-source vacuum domain; two-point forms below need no product of unbounded operators on an unverified domain. The capped operator is bounded and preserves the physical subspace. These expressions allow either electric/magnetic sign; a classical B^2-E^2 interpretation is not a quantum Lorentz identification.

Put E_h(f)=sum_e|a_(e,h)(f)| and B_h(f)=sum_p|b_(p,h)(f)|. Then

||A_(h,S)(f)||<=M_S E_h(f)+B_h(f),
V_h(f):=E_h(f)*K_R/sqrt(2)+B_h(f)

bounds BOTH centered vacuum-vector norms. Indeed projection off the rank-one actual vacuum is a contraction,and the primitive capped vector is no larger in norm than the uncapped one. Centered vector error obeys

delta_h(f)<=E_h(f)*K_R/sqrt(2S+2).

Centering does NOT cost an extra factor2 in this vector error: it is exactly the vacuum-orthogonal projection of (A_h-A_(h,S))Omega. The centered OPERATOR norm may cost2,which must still be retained in locality budgets.

For every real unitary time,and every nonnegative Euclidean time,the same source dynamics has norm at most1. Thus the centered two-point difference is at most

delta_h(f)*V_h(g)+V_h(f)*delta_h(g).

For a diagonal reader it is<=2V_h(f)delta_h(f),uniformly over time and clock. No commutation of the cap with the magnetic Hamiltonian is assumed. Vacuum-vector error tending to0 by itself is insufficient when V_h diverges.

## 5. A single cap preserves linearity and finite-exponential budgets

Use actual sampling coefficients

a_(e,h)(f)=z_E(h)*h^3*f(mid_e),
b_(p,h)(f)=z_B(h)*h^3*f(center_p),

with real z_E,z_B. Electric and magnetic supports include their actual links. Set

D_h=max(1,|z_E(h)|+|z_B(h)|),
S_h=ceil(h^-2*D_h^4),0<h<=1.

This one integer spin cap is independent of f,its compact support and the source box. Therefore the capped family remains a real-linear map of spatial tests. For every fixed compact K,a geometric count gives E_h(f)+B_h(f)<=C_K*D_h*||f||_infinity. Hence

V_h(f)<=C_K D_h||f||_infinity,
delta_h(f)<=C_K K_R*h*||f||_infinity/D_h.

The resulting two-point cap-removal bound is O(h) times the product of those test seminorms. If limsup h log D_h=gamma<infinity,then limsup h log S_h<=4gamma,and the capped operator-norm exponential rate is at most9gamma (fixed test constants and polynomial factors do not contribute). With polynomially many links in a compact physical region,the reader families satisfy the previous finite-exponential locality criterion. Even the unbounded electric part therefore cannot by itself evade that criterion in this normalization class.

For a concrete unit-box example,h=1/N,|z_E|,|z_B|<=N^4 and ||f||_infinity<=1. Link/plaquette counts give E_h<=12N^4,B_h<=6N^4,so V_h<=9N^4. Taking S=N^18 gives delta_h<=3N^-5 and two-point error<=54/N. The uncapped-to-capped vector comparison alone would need only a weaker power; paying for the other divergent vector is why this example uses18 rather than a power merely greater than8.

The capped uncentered operator norm is<=30N^40,and its centered norm<=60N^40. A unit-box support has at most12N^3 links,so a pair's locality norm/support budget is at most21600N^83. The large polynomial is permissible; it is not a physical scaling law or an optimal numerical rate.

## 6. Joint tempered cap removal,not just a few insertion values

A uniform global bound is available for these sampled families. For a local primitive O_l=C_e or w_p,define its centered vacuum vector v_l and the time vector exp(it Htilde_h)v_l. The uncapped two-point form is their Hilbert pairing,so no unbounded operator product domain is asserted. It gives a finite-source tempered bidistribution by summing at the sampled spatial positions. The capped version uses the same vacuum and dynamics.

All primitive centered vector norms,both capped and uncapped,are<=1 in the retained window. The electric vector difference is<=K_R/sqrt(2S+2); magnetic difference is0. Therefore each ordered primitive two-point kernel differs by at most2K_R/sqrt(2S+2),uniformly in both real times and arbitrary positive whole-Hamiltonian clock factors.

Here is an explicit uniform weighted lattice count. For w(x)=(1+||x||_infinity)^-4,integral_R3 w=8. Associate each shifted grid point h(n+theta),theta in[0,1]^3,to its h-cube. Since h<=1,its weight is at most16 times the weight anywhere in that cube. Thus each shifted lattice has

h^3 sum_n w(h(n+theta))<=128.

There are three link orientations and three plaquette orientations,so each species contributes at most384. Finite boxes are subsets of these grids; boundaries only reduce the count.

For a Schwartz test Psi(t,x;s,y),let

p(Psi)=sup (1+|t|)^2(1+|s|)^2
 (1+||x||_infinity)^4(1+||y||_infinity)^4*|Psi(t,x;s,y)|.

This is bounded by a finite standard Schwartz seminorm. Both time weights integrate to2. Summing the actual coefficient magnitudes against the spatial weights and using D_h^2/sqrt(S_h)<=h yields

|(W_h^(2)-W_(h,S_h)^(2))(Psi)|
<=4*384^2*2K_R*h*p(Psi)
<=294912*h*p(Psi).

Consequently the two families differ by a quantity tending to0 in S'(R8),with an explicit common seminorm. This conclusion is uniform in finite source box,clock and retained coupling. It does NOT assert either individual family converges or is uniformly bounded: it says that any tempered limit of one family is exactly the limit of the other.

Combining with the preceding scalar/locality theorem,an uncapped electric/magnetic family in this finite-exponential normalization class cannot escape its conditional non-promotion result simply by invoking electric unboundedness. A nonzero Lorentz-scalar forward-spectrum limit with the specified zero-mode removal would contradict the retained source premises. No such limit has been constructed here.

## 7. What remains genuinely unproved

The reader is a native gauge-invariant electric/magnetic CANDIDATE. A valid scalar quantum field still requires the proper operator mixing,renormalization,state/observable comparison,Lorentz covariance,spectrum and nontriviality. Neither a cap nor a bare B^2-E^2 formula provides those. Arbitrary composite operators beyond this quadratic primitive class and arbitrary superexponential normalizations are not covered.

The algebra/Plancherel theorem and actual interaction input remain analytic imports; finite controls do not certify them. There is no global infinite Haar vacuum or volume-uniform pointwise Omega ratio in the proof.

## 8. Next executable source test

Determine the ACTUAL free-source magnetic fluctuation scaling at eta=0 using Haar/character orthogonality and the real finite-source dynamics. At this endpoint different elementary plaquette characters are orthogonal and each has electric energy3sigma. A spatial smear can therefore have zero,finite ultralocal,or divergent two-point scaling depending on its normalization. Derive that statement with the sampling/test topology explicit,and test the conventional h^-4 candidate rather than assume it converges. A nonzero ultralocal limit would be a native nonrelativistic control,not a continuum Yang-Mills construction or a theorem for eta>0.

This locates which comparison hypothesis actually fails in an available source,after the present cap theorem has removed the bounded-observer loophole. It is not another abstract assumption wrapper or a waiting leaf. Independent review and the full physical/continuum/root gates remain open.

Contract: `contracts/yang-mills-electric-magnetic-reader.v1.json`.
Checker: `checkers/check_yang_mills_electric_magnetic_reader.py`.
Receipt: `results/yang-mills-electric-magnetic-reader-v1.json`.

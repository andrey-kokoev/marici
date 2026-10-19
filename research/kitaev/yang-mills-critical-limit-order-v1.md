# Outer-volume independence of critical source two-point limits

Owner `marici.Kitaev`; spatial-scaling iteration9/10. Selected node `issue-tree:87b983be841a61be1b85d24a:critical-limit-order:v1`.

## Result and boundaries

Retain h_n=2^-n,eta_n=c h_n^5 with c>0,and fixed sigma>0. Keep the declared bare-matched mixed trial and its actual bounded Casimir-capped version. Every finite source has positive coupling and its ORIGINAL Hamiltonian and actual vacuum.

The previously obtained limit

W_*(t,x;s,y)=6c exp[-i3sigma(t-s)]delta^3(x-y)           (1)

holds on ANY centered mesh-aligned open outer-box sequence Q_n=[-R_n,R_n]^3 with R_n->infinity,with no upper bound on its growth. In particular the conclusion does not require eta_n P_outer,n->0. This is joint convergence in S'(R8),not only Euclidean insertion convergence.

The thermodynamic-first MAGNETIC source channel,defined by the already identified infinite-volume vacuum measure and closed Markov/gradient generator at each fixed mesh,has the same limit. Mixed and capped finite-source limits follow from their uniform Ward/cap comparisons. No new infinite-volume electric or capped quantum-observable representation is constructed here. There is no infinite Haar wavefunction or infinite total-potential perturbation.

As before,the nonzero limit is ultralocal and violates the relativistic forward cone. Standard source boundary-comparison,spectral measure,Laplace uniqueness and nuclear Schwartz kernel results remain analytic imports requiring independent review. The new proof audits their quantifiers and pays the changing reader budgets.

## 1. Adaptive finite buffer

Write h=h_n and let

r_n=h*floor(min(n,R_n/2)/h), Lambda_n=[-r_n,r_n]^3.

Eventually r_n>=1,and always r_n<=n, r_n<=R_n/2. Since both n and R_n tend to infinity,r_n->infinity. The buffer is an actual open sub-box of the outer source,not a new boundary condition imposed on the outer vacuum.

Its square count satisfies P_buffer<=36r_n^3 h^-3<=36n^3 h^-3. Hence

eta_n P_buffer<=36c n^3 h^2 ->0.                       (2)

The preceding residual and shifted-unitary proof applies WITHIN this buffer: its actual vacuum error is O_c(n^(3/2)h^(7/2)),its magnetic-vector error is O_c(n^(3/2)h^2),and its compact-time dynamics error is O_(c,sigma)(n^3 h^2). The free comparison box now has physical radius r_n->infinity instead of n,which is sufficient for its spatial quadrature limit. Thus the actual buffer magnetic proxy has limit(1),both at each nonnegative Euclidean time and jointly in real-time S'. This is a repetition of the estimates with (2),not an exchange of an infinite-volume limit.

## 2. Growing readers fit the existing finite-word boundary theorem

The proxy is

F_h(f)=-sqrt(8c)h^(3/2) sum_p f(x_p)w_p.

First take fixed real smooth compact spatial tests f,g supported in[-L,L]^3. Put

U_h(f)=sqrt(8c)h^(3/2) sum_p|f(x_p)|.

Once the buffer contains the complete test footprint,the same sampled reader and this budget occur in the buffer,outer and infinite sources. Then ||F_h(f)||_infinity<=U_h(f),and the sum of link-gradient sup norms obeys M(F_h(f))<=4U_h(f): each square has four links and each link-gradient norm is at most sqrt(3)/2<=1. The test-dependent budgets U_h(f),U_h(g) are O_c(h^-3/2). Zero readers are treated directly without division.

Normalize each nonzero reader by U_h. The actual finite-word comparison theorem bounds an uncentered two-insertion moment against the actual thermodynamic source by

8 C_R U_h(f)U_h(g)(3/4)^b, C_R<=18/5,

uniformly over ALL nonnegative Euclidean time separations and retained couplings. The one-insertion bound on each mean is4 C_R U_h(f)(3/4)^b. Subtracting the products of means therefore gives the CENTERED infinite-source/buffer bound

16 C_R U_h(f)U_h(g)(3/4)^b <=(288/5)U_h(f)U_h(g)(3/4)^b. (3)

Do not identify finite and thermodynamic vacuum measures; the separate mean terms are essential. Compare an arbitrary larger outer box to the buffer via their common thermodynamic source. The outer distance is no smaller than the buffer distance,so the centered outer/buffer bound is at most twice(3):

|C_outer,h(tau;f,g)-C_buffer,h(tau;f,g)|
 <=(576/5)U_h(f)U_h(g)(3/4)^b, tau>=0.                (4)

All states and semigroups in(3)-(4) are their ACTUAL retained source objects. Clock conversion replaces each source interval by s_h*tau; the finite-word theorem is horizon-uniform,so no divergent kappa_h or time factor appears.

## 3. Physical distance defeats the normalization

The link metric joins links sharing a square; one hop moves a midpoint by at most h in the spatial infinity norm. The reader support includes the four links of each sampled square,not only its center. A conservative buffer-distance lower bound is

b_n>=max(0,floor((r_n-L)/h)-3).

For every fixed f,g,eventually r_n>=L+1. Then

h^-3(3/4)^b_n ->0.                                  (5)

Indeed b_n>=floor(1/h)-3 already suffices,and exponential decay in1/h beats any fixed power. This conclusion is independent of how large or how slowly exhausting the OUTER source is. The only volume paid in(2) belongs to the chosen buffer. Combining (4)-(5) with its actual perturbative comparison proves,for every tau>=0,

C_outer,h(tau;f,g)->6c exp(-3sigma tau) integral f*g,
C_infinite,h(tau;f,g)->the same value.                 (6)

Complex tests follow by polarization,with integral conjugate(f)*g in the Hilbert convention. Equations(3)-(6) are scalar comparisons in the actual changing states,not Hilbert isometries between different vacua.

## 4. Identify the thermodynamic-first magnetic spectral carrier

At each fixed h the retained construction supplies nu_infinite,eta_h and its identified nonnegative closed gradient generator A_eta_h with unit kinetic coefficient,on the gauge-invariant part of L2(nu_infinite,eta_h). The vacuum is the CONSTANT1 in this weighted Hilbert space,not a density relative to infinite product Haar. Set

K_infinite,h=sigma*A_eta_h,
v_h(f)=F_h(f)-nu_infinite,eta_h(F_h(f)).

This is the native thermodynamic-first magnetic channel used in(3),(6). At fixed h compact f is a smooth cylinder; its source matrix elements and form are already identified by the finite-box propagator/core construction. The word theorem compares its Euclidean moments,including its state,with finite boxes.

For both this carrier and any actual finite outer source,the previous magnetic covariance and ground-state form estimates give

||v_h(f)||^2 <=(768/5) Q_h(f),
<v_h(f),K_h v_h(f)> <=12sigma Q_h(f),
Q_h(f)=8c h^3 sum_p|f(x_p)|^2.                        (7)

In infinite volume the inequalities pass at fixed h for cylinders; the gradient form is the already identified actual closed form. No infinite electric operator is needed. Weighted sampling bounds Q_h(f) uniformly for fixed spatial Schwartz f. Source gaps also bound the centered spectra below by5sigma/64,but the following recovery argument principally uses positivity,mass and first moment.

## 5. Recover real-time spectral convergence,not an analytic-continuation assertion

Let mu_h^f be the positive spectral measure of K_h and v_h(f). Its total mass and first energy moment are uniformly bounded by(7). Thus

mu_h^f((T,infinity)) <=12sigma Q_h(f)/T.              (8)

This supplies energy TIGHTNESS. Bounded finite positive measures with(8) have narrowly convergent subsequences. Every such subsequential limit has,by(6),Laplace transform

6c ||f||_L2^2 exp(-3sigma tau),tau>=0.

Uniqueness of Laplace transforms of finite positive measures identifies it as6c ||f||^2 delta_(3sigma). Hence the entire sequence,not just one subsequence,converges narrowly to that measure. This works for any outer-box exhaustion and for the thermodynamic-first magnetic channel.

Polarization gives cross measures. Their total variation and first weighted variation obey the corresponding Cauchy-Schwarz bounds from the diagonal measures. Consequently their Fourier transforms converge:

<v_h(f),exp(-itK_h)v_h(g)>
 ->6c exp(-i3sigma t) integral conjugate(f)*g.          (9)

Convergence is uniform on compact real-time intervals: the first-moment bounds give a common Lipschitz bound there (in fact globally). No quantitative real-time boundary rate is inferred from the exponential Euclidean comparison; the passage uses tightness and uniqueness. Imported finite-measure compactness and Laplace/Fourier facts are stated explicitly.

Why the extra argument matters: positive measures2^N delta_(N^2) have Laplace transforms tending to0 at every tau>0,but are NOT a bounded family of tempered measures. A fixed Schwartz energy test equal to2^(-sqrt(E)/2) for E>=1 has pairings2^(N/2)->infinity. Smooth extension elsewhere is possible and is Schwartz. This is a positive spectral countercontrol to promoting Euclidean insertion convergence alone to real-time S' convergence. It violates(7)-(8),not the source theorem.

## 6. Joint S'(R8) recovery and mixed/capped transfer

The l2 upper bound in(7),weighted lattice sampling,and unitarity give a common Schwartz seminorm p with

||integral exp(itK_h)v_h(u_t)dt||<=C_c p(u)

for all spacetime u and every finite outer or native infinite source. Begin with compact spatial tests; their smooth compact cutoffs are dense in spatial Schwartz space under the same weighted estimates. Equation(9),uniform kernel bounds and integrable time tests give convergence for time/spatial tensor tests. Finite sums of these are dense; the displayed uniform vector bound extends convergence to all u,v in S(R4).

The explicit nuclear Schwartz kernel theorem S(R4) tensor_pi S(R4)=S(R8),with this equicontinuity,then extends convergence to ALL joint tests. Tensor-test samples alone would not suffice. It follows that the proxy two-point distributions converge jointly to(1) on every exhausting outer-box net AND in the thermodynamic-first magnetic channel.

The actual mixed finite-source reader differs from the proxy by the proved uniform joint Ward error O_c(h),since its amplitude is8c. Its bounded Gauss-compatible common-cap version differs by the proved uniform joint cap error O(h). Both constants are independent of the outer box and clock. Thus BOTH finite-source families share(1) without a slow outer-volume restriction.

No existence of a thermodynamic-first capped electric quantum operator has been smuggled into this transfer. The infinite-source result above is precisely for the already identified magnetic Markov/spectral carrier. A full observable-algebra or operator-product representation would require additional work and is not a claim of this node.

## 7. Compact-parameter corollary and relativistic failure

The buffer estimates are uniform for0<c_h<=C and0<sigma_h<=M at each mesh; no positive lower bound on either parameter is needed. The vacuum residual cancels sigma between gap and perturbation. If c_h->c_*>=0 and sigma_h->sigma_*>=0,the same argument gives

W_h ->6c_* exp[-i3sigma_*(t-s)]delta^3(x-y).

If c_*=0,the uniform vacuum-vector bound gives zero directly. For c_*>0 and sigma_*=0,the positive limiting measure is supported on E=0 with Lebesgue spatial momentum; this is not a spacetime zero-momentum atom. It still fails the forward cone. All nonzero kernels in this corollary are nonrelativistic. No all-orders Gaussian,state reconstruction or Yang-Mills claim follows.

## 8. Verification and next executable arbitrary-clock classification

The checker replays the previous critical-limit receipt and the original finite-word boundary receipt separately. New exact controls test adaptive buffers,normalization budgets,centered comparison coefficients,distance suppression,positive spectral mass/moment tightness,polarization/continuity bounds,and the positive spectral countercontrol with convergent Euclidean values but unbounded tempered growth. They do not certify the analytic source construction,measure compactness,Laplace uniqueness or nuclear Schwartz theorem. Independent review remains open.

One substantive clock/normalization issue remains executable in the declared spatial-scaling objective: classify nonzero TEMPERED limits of the native bare-matched mixed/capped trial at arbitrary source clocks,not only compact parameter sequences. The effective amplitude is a_h=8eta_h/h^5. At bounded clocks unbounded a_h already violates fixed-test boundedness; at bounded a_h finite clock subsequences are now identified by this theorem. For escaping sigma_h,combine the uniform centered source gap with smooth time smearing and inverse powers of the generator to test spectral escape without unauthorized spatial derivatives. If a family is assumed S'-bounded,its positive spectral measures should impose a polynomial bound on mass in an energy window proportional to sigma_h. Couple that with the actual Ward/filter lower bound to constrain a_h,then determine whether every escaping-clock tempered subsequence is weak-zero. This would locate all possible nonzero native two-point limits and make the clock-independent scope precise; do not assume the required polynomial measure bound or equate nonzero ultralocal limits with relativistic ones.

Contract: `contracts/yang-mills-critical-limit-order.v1.json`.
Checker: `checkers/check_yang_mills_critical_limit_order.py`.
Receipt: `results/yang-mills-critical-limit-order-v1.json`.

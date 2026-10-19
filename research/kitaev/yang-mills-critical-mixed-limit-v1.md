# Actual positive-coupling critical mixed two-point limit

Owner `marici.Kitaev`; spatial-scaling iteration8/10. Selected node `issue-tree:87b983be841a61be1b85d24a:critical-mixed-limit:v1`.

## Result and explicit source net

There is a native nonzero TWO-POINT limit for the critical mixed trial,with positive interaction at every finite mesh. It is ultralocal and NOT a relativistic Yang-Mills field.

Fix c>0 and sigma>0. For sufficiently large integers n,set

h_n=2^-n, M_n=n*2^n, Q_n=[-n,n]^3,
eta_n=c*h_n^5,
g_H,n^2=sqrt(8/c)*h_n^(-5/2),
kappa_n=sqrt(2/c)*h_n^(-7/2), lambda_n=sqrt(2c)*h_n^(3/2),
s_n=sigma/kappa_n.

The vertices are h_n times integer triples in[-M_n,M_n]^3,with ordinary open links and each square counted ONCE. The physical box radius n tends to infinity; this is not a fixed-volume limit. Its plaquette count is

P_n=3(2M_n+1)(2M_n)^2
=24n^3 h_n^-3+12n^2 h_n^-2<=36n^3 h_n^-3.

Every eta_n is strictly positive,and eventually lies in the unchanged retained window. Discarding finitely many initial n is harmless. The displayed bare parameters use the previously declared once-counted canonical convention; no nonperturbative anisotropy calibration is thereby proved.

Let Omega_n be the ACTUAL positive normalized ground state of the original Hamiltonian H_n,and K_n=s_n(H_n-E_0,n). Center all readers in Omega_n. The magnetic-minus-electric energy-density trial,after removing its constant magnetic term,is

A_n(f)=-kappa_n sum_e f(mid_e)C_e-lambda_n sum_p f(center_p)w_p.

This is precisely the previous form h_n^3[z_E sum f C_e+z_B sum f w_p],with z_E=-kappa_n/h_n^3,z_B=-lambda_n/h_n^3. The unbounded reader is used through its actual vacuum vectors; no unverified operator-product domain is asserted.

Its connected joint two-point distributions converge in S'(R8) to

W_*(t,x;s,y)=6c*exp[-i3sigma(t-s)]*delta^3(x-y).        (1)

Actual bounded Gauss-compatible Casimir-capped readers on the same source have this identical limit. No Hamiltonian or vacuum is spin-truncated. The proof below compares actual finite sources rather than selecting Haar as their vacuum.

## 1. A residual/gap estimate for the actual vacuum

All comparisons in this section take place on the SAME finite physical Haar Hilbert space for box Q_n. Suppress n. Put L=sum_e C_e and

T=sH=sigma[L+eta sum_p(1-w_p)], T_0=sigma L,
E=sE_0, V=T-T_0.

Since0<=V<=2sigma eta P and its free-vacuum expectation is sigma eta P,the variational principle gives0<=E<=sigma eta P. The physical free mean-zero gap is3sigma,not the charged kinematic3sigma/4.

Write Omega=a*1+zeta with zeta perpendicular to1. Positivity fixes a=<1,Omega>>0. Projecting the actual eigen-equation gives

[Q_0(T-E)Q_0]zeta=-a Q_0 V1.

On the physical mean-zero subspace,the left operator is bounded below by sigma(3-eta P). Haar plaquette orthogonality gives the EXACT residual

Q_0 V1=-sigma eta sum_p w_p,
norm(Q_0 V1)=sigma eta sqrt(P)/2.

For eta P<3,it follows that

norm(zeta)<=eta sqrt(P)/[2(3-eta P)],
epsilon:=norm(Omega-1)<=eta sqrt(P)/(3-eta P).         (2)

The last inequality uses a>=0 and norm(Omega)=1; it is a conservative version of the additional sqrt(2) improvement. This is not a global density-ratio estimate.

On the chosen net,

eta P<=36c*n^3*h^2 ->0.

Eventually eta P<=1,and (2) gives

epsilon_n<=3c*n^(3/2)*h_n^(7/2).                     (3)

Smoothness/positivity and the finite-source eigen-equation are the retained actual-source analytic inputs. The inverse here is the full physical compressed operator,not a finite-spin matrix approximation.

## 2. Actual shifted dynamics is close in operator norm on this net

The free shifted generator is K_0=T_0. The actual one is K=T-E. Both are nonnegative self-adjoint operators with the same kinetic domain,up to a bounded perturbation. Explicitly

norm(K-K_0)<=3sigma eta P.                            (4)

This coarse bound includes the ACTUAL ground-energy shift. Bounded-perturbation Duhamel therefore yields

norm(exp(itK)-exp(itK_0))<=3sigma eta P*|t|.           (5)

Likewise the Euclidean contraction difference is<=3sigma eta P*tau for tau>=0. These statements do not assert smallness of an infinite-volume total potential; the global perturbation is small specifically on this chosen exhausting net.

## 3. Reduce the electric channel BEFORE changing the vacuum

The proved local Ward comparison gives the actual magnetic proxy coefficient

m_n=z_B+eta z_E=-2lambda_n/h_n^3
=-sqrt(8c)*h_n^(-3/2).

Define the bounded magnetic multiplication reader

B_n(f)=m_n h_n^3 sum_p f(center_p)w_p
=-sqrt(8c)*h_n^(3/2) sum_p f(center_p)w_p.

Let v_A(f),v_B(f) be the ACTUAL centered vacuum vectors. The previous support-wise Ward theorem supplies a fixed spatial weighted C1 seminorm p_1 with

norm(v_A(f)-v_B(f))<=C_c*h_n*p_1(f),                 (6)

uniform in boxes and clocks. Indeed the previous bound is C |z_E|S_R h^(5/2),and S_R<=(5632/3)eta; inserting this net gives (5632/3)sqrt(2c)*h. The effective variance scale is exactly |m_n|^2 h_n^3=8c.

Order matters. If Omega were replaced by1 BEFORE applying the original electric reader,C_e1=0 would erase the electric contribution. Keeping just z_B would incorrectly give variance scale2c and limiting amplitude(3/2)c,instead of8c and6c. The missed amplitude is(9/2)c. Thus norm(Omega-1)->0 alone cannot transport these growing unbounded operators. Equations(2)-(3) are used ONLY after the actual Ward reduction,not as a substitute for a graph-norm comparison of C_e.

## 4. Pay the magnetic reader norm and actual centering

For a spatial Schwartz f,let p_0(f)=sup_x(1+||x||_infinity)^4|f(x)|. The uniform weighted square-grid count gives

norm(B_n(f))<=384sqrt(8c)*h_n^-3/2*p_0(f),
norm(B_n(f)1)^2=(8c/4)*h_n^3 sum_p|f(center_p)|^2
<=768c*p_0(f)^2.                                    (7)

The free mean is zero. Set v_0(f)=B_n(f)1 and
v_B(f)=B_n(f)Omega-<Omega,B_n(f)Omega>*Omega.

For real f,the change of the scalar mean is at most2norm(B_n(f))*epsilon_n. The same absolute-value estimate holds for the complex-linear extension. Hence

norm(v_B(f)-v_0(f))<=3norm(B_n(f))*epsilon_n
<=C_c*n^(3/2)*h_n^2*p_0(f).                          (8)

The actual centered proxy norms are uniformly bounded by a fixed multiple of p_0,also directly following from the earlier actual magnetic l2 covariance upper bound. No uncentered expectation is silently identified across the two states.

Combining (5),(7)-(8),for every real t,

norm(exp(itK_n)v_B(f)-exp(itK_0,n)v_0(f))
<=C_(c,sigma)*n^3 h_n^2*(1+|t|)*p_0(f).              (9)

Using a global density ratio or simply the operator norm of the original electric reader would lose these estimates. The residual has sqrt(P),not P,and only the reduced magnetic reader incurs h^-3/2.

## 5. Joint tempered comparison,not insertion-point convergence alone

For u in S(R4),time-smear the vacuum vectors with their respective unitary dynamics. A continuous seminorm is obtained by bounding spatial derivatives up to order1 with weight(1+|t|)^3(1+||x||_infinity)^4. Its time integral,including the extra1+|t| in (9),is finite. Thus the smeared actual-proxy/free-vector difference is at most C*n^3 h_n^2*p(u),while both smeared vector norms are uniformly bounded by C*p(u).

The tensor-test difference of the two-point forms is consequently<=C*n^3 h_n^2*p(u)p(v). As in the previous Ward proof,the nuclear Schwartz tensor theorem S(R4) tensor_pi S(R4)=S(R8) extends this bound to a fixed continuous projective Schwartz seminorm q on ALL joint tests. This is an explicit analytic import,not a conclusion from a few separable samples.

Together with (6) and the already proved joint Ward comparison,

|(W_A,n-W_free-proxy,n)(Psi)|
<=C_(c,sigma)*[h_n+n^3 h_n^2]*q(Psi).                 (10)

All comparisons in(10) are performed before the limit,on actual finite source boxes with eta_n>0.

## 6. Compute the free comparison limit and its spectrum

For the free proxy,the previously derived exact character formula has a_n=8c and frequency3sigma. Its three once-counted square orientations and the actual physical box exhaustion n->infinity give

W_free-proxy,n ->6c exp[-i3sigma(t-s)]delta^3(x-y)

jointly in S'(R8). For example the earlier weighted quadrature estimate gives an error<=C[h_n+(1+n)^-1]q_R(Psi). Combining with (10) proves (1),with total error bounded by a fixed seminorm times

C_(c,sigma)*[h_n+n^3 h_n^2+(1+n)^-1] ->0.            (11)

No unidentified thermodynamic-first order of limits is exchanged. This is an actual specified finite-box spatial-scaling net. Other outer-volume growth rules are NOT yet covered by the global perturbation proof.

The positive relative-coordinate spectral measure is

mu_*=6c*delta_(3sigma)(dE)*d^3p/(2pi)^3.

It is nonzero,has a finite positive-time channel,and has no spacetime zero-momentum atom. It nevertheless has positive weight at |p|>3sigma and is not Lorentz invariant. Its antisymmetric two-point kernel is -12ic*sin(3sigma t)*delta^3(x). The limit is a spatial-white oscillator two-point distribution,not a relativistic scalar construction. The nonzero Euclidean channel is6c exp(-3sigma tau) integral|f|^2; Euclidean convergence for this chosen net also follows directly from the contraction form of (5).

No all-orders Gaussian convergence,operator products,OS reconstruction or interacting continuum theory is inferred from a two-point calculation. Every finite-mesh source is interacting; the limiting source channel is ultralocal and free-like.

## 7. Actual bounded electric/magnetic observers have the same limit

Use the preceding test-independent Casimir cap S_n=ceil(h_n^-2 D_n^4),where D_n=max(1,|z_E|+|z_B|). It changes only the reader C_e to min(C_e,S_n(S_n+1)). All Gauss transformations commute with this one-link bounded functional calculus. The source Hamiltonian,Hilbert space and actual vacuum retain all spins.

On this net D_n=O_c(h_n^-13/2),so S_n=O_c(h_n^-28),the capped local-smeared operator norm is O_c(h_n^-125/2),and a pair's compact-support norm/link budget is O_c(h_n^-128). These are polynomial observer budgets,not optimized physical exponents. The previously proved joint cap-removal bound is O(h_n) in a fixed Schwartz seminorm,independent of source box or clock. Thus the actual bounded capped family ALSO converges to(1). Large reader norms do not create propagation or repair its spectrum.

## 8. Verification,falsifiers and remaining executable issue

Finite exact controls test box counts,critical/bare coefficients,residual and energy budgets,normalized-vector geometry,reader/centering compensation,bounded-perturbation planners,the fourfold amplitude error from premature vacuum substitution,and the common cap exponents. They replay the previous Ward receipt. They do not certify the infinite-dimensional residual inversion,the all-spin interaction constructor,nuclear Schwartz theorem or analytic limits independently. Independent review remains open.

The important unresolved ORDER issue is now executable: remove the slow outer-box restriction,or identify its exact scientific necessity. The present total-potential estimate fails on sufficiently fast growing boxes and is meaningless on an infinite volume at fixed h. That failure does not itself imply a different local fluctuation limit. Use the established local source/semigroup boundary comparison with a slowly growing BUFFER box around the physical test support,quantify its polynomial reader budgets against exponential lattice boundary distance,and then identify real-time spectral limits using actual positive spectral measures and their uniform first energy moments. If a thermodynamic-first interpretation is used,identify its native source Hilbert/spectral channel rather than assume an infinite Haar wavefunction or an unprovided observable map. This can determine whether (1) is robust under arbitrary sufficiently large outer finite boxes and the actual thermodynamic-first magnetic channel,not merely a specially chosen diagonal net. Do not promote Euclidean insertion convergence alone to joint real-time S' convergence.

Contract: `contracts/yang-mills-critical-mixed-limit.v1.json`.
Checker: `checkers/check_yang_mills_critical_mixed_limit.py`.
Receipt: `results/yang-mills-critical-mixed-limit-v1.json`.

# Actual interacting magnetic covariance coercivity and growth

Owner `marici.Kitaev`; spatial-scaling iteration6/10. Selected node `issue-tree:87b983be841a61be1b85d24a:interacting-magnetic-coercivity:v1`.

## Question and disposition

The free endpoint did not determine interacting fluctuations. Exponential clustering and a gap supply upper bounds,not a coercive covariance matrix. Can the actual retained vacuum nevertheless control every plaquette smear from below?

**Yes,at written analytic scope throughout the original retained window.** A direct local-energy/weighted-Bochner argument avoids a covariance perturbation expansion. For every finite open source box and finite real or complex coefficients b_p,write

F=sum_p b_p w_p, Q=sum_p |b_p|^2, V=nu(|F-nu(F)|^2),
D=nu(|gradient F|^2), A=-(Delta+gradient log rho . gradient), rho=Omega^2.

The actual source satisfies

Q/512 <= V <= (768/5)Q,                                  (1)
D<=12Q, norm(A F)_L2(nu)^2<=(42+36R)Q.                  (2)

The constants are deliberately coarse. Neither the Hamiltonian nor vacuum is truncated or replaced. The proof imports the actual anchored interaction constructor,its C2/Hessian bounds,compact-group differentiation and weighted Bochner identity. Finite controls are not an independent analytic review.

A risky consequence is ACTUAL interacting h^-4 magnetic-reader divergence at bounded clocks,detected by a fixed Schwartz test. This no longer substitutes eta=0 for eta>0. The next executable question is the actual electric/magnetic Ward-cancellation audit: magnetic growth alone cannot establish mixed scalar-reader growth. Critical interacting two-point compactness remains a subsequent possibility,not a Lorentz or all-orders assertion.

## 1. Retained source and a genuinely local density bound

Retain 0<=eta=lambda/kappa<27/262144,R=(4096/3)eta<9/64. The actual finite vacuum has

log Omega=sum_A Phi_A+constant,
sup_e sum_(A containing e)2^|A| W(Phi_A)<=R,
||Hess log rho||_op<=3R.

Use the ACTUAL constructed decomposition: each nonempty label A is a union of elementary plaquettes and hence |A|>=4. The bound below uses this support fact,not just an arbitrary interaction norm after relabeling. In particular

sum_(A containing e)||Phi_A||_infinity<=R/16.

For any finite set B of links,condition on all outside links. Only interactions meeting B enter the nonconstant conditional log density. Its oscillation over B is at most

4 sum_(A meeting B)||Phi_A||_infinity <= |B|R/4.

Normalization therefore bounds that conditional density relative to normalized Haar_B from below by exp(-|B|R/4),uniformly in the conditioning configuration. For every nonnegative G depending only on B,

nu(G)>=exp(-|B|R/4)*Haar_B(G).                         (3)

This is a LOCAL conditional comparison. There is no global volume-uniform lower bound on rho and no comparison cost proportional to the entire box. Infinite spin modes remain in Omega.

## 2. Dirichlet lower bound from a thirteen-link star

For a fixed link e,gradient_e F involves only the at most four elementary squares containing e. Distinct squares share at most one link. The union B_e of those squares thus has at most1+3*4=13 links. The nonnegative function G_e=|gradient_e F|^2 depends only on B_e.

Under Haar_Be,distinct square traces are orthogonal,including shared-link neighbors,by integration of an unmatched fundamental link. Also C_e w_p=(3/4)w_p when e belongs to p and Haar(w_p^2)=1/4. Integration by parts gives

Haar_Be(|gradient_e F|^2)=(3/16) sum_(p containing e)|b_p|^2.

Apply (3) before summing over e. Every plaquette has four distinct links,so

D >= d_R Q, d_R=(3/4)*exp(-13R/4).                    (4)

Boundary incidence can only reduce the size of B_e; it does not remove any of the four links of a retained square. The argument is valid for arbitrary signed coefficients,not just positive uniform sums. Complex coefficients follow by applying the real identities to real and imaginary parts.

## 3. Pointwise derivative bounds and bounded overlap

In the specified radius-two metric,the fundamental generators have operator norm1/2. Normalized trace and unitarity give

|X_ea w_p|<=1/2,
|Hess_(ea,fb) w_p|<=1/4

when the indicated links belong to p,and zero otherwise. For equal-link indices the covariant Hessian is the SYMMETRIZED second frame derivative,not an uncorrected frame product; the bi-invariant connection subtracts half the commutator. For different links it is the ordinary mixed derivative. No derivatives of the vacuum Hessian are taken.

There are12 frame directions on the four-link plaquette. Hence pointwise

|gradient w_p|^2<=3, ||Hess w_p||_HS^2<=9.

At any fixed gradient component or Hessian matrix entry,at most four plaquettes contribute. Cauchy-Schwarz at that entry,THEN summation over entries,gives

|gradient F|^2<=12Q, ||Hess F||_HS^2<=36Q.              (5)

This order avoids a volume-dependent l1 coefficient bound. Individual local derivative estimates without bounded overlap would not imply an l2 smear estimate. These coarse inequalities do not require the sharper exact SU2 derivative identities.

## 4. Bochner upper bound plus Cauchy-Schwarz gives coercivity

All functions here are smooth on the actual finite compact product. Weighted integration by parts and the integrated Bochner identity give

norm(A F)^2=nu(||Hess F||_HS^2)
 +nu[(Ric-Hess log rho)(gradient F,gradient conjugate(F))].

Ric=1/2 in this normalization. The upper Hessian bound and (5) imply

norm(A F)^2 <= [36+12*(1/2+3R)]Q=(42+36R)Q=:B_R Q.     (6)

This is the UPPER curvature estimate,used in a different direction than the previous Poincare proof. Reusing only the lower-curvature gap would not suffice.

Let F_0=F-nu(F). Since A1=0,

D=<F_0,A F>, so D^2<=V*norm(A F)^2.

For Q>0,combine (4) and (6):

V >= d_R^2/B_R * Q.                                  (7)

For Q=0 everything is zero. No covariance row-sum expansion or nonzero interacting reader assumption has entered this deduction.

There is a fully rational uniform margin. Since exp(-x)>=1-x,

d_R >= (3/4)*(1-117/256)=417/1024,
B_R <=753/16,
(d_R^2/B_R) >=57963/16449536 >1/512.

Thus the left side of (1) holds over the ENTIRE original retained open window,including coupling nets approaching either endpoint. The right side follows separately from the existing actual weighted Poincare constant5/64 and D<=12Q:

V <=(64/5)D <=(768/5)Q.

The lower bound is NOT a reverse Poincare theorem for arbitrary functions. It uses the finite-degree plaquette primitive class,local conditional comparison and its bounded-overlap derivative structure. General bounded composite readers are not covered by (1).

## 5. Actual source spectral lower bounds at positive time

Center the actual Haar-space vector v=Omega*(F-nu(F)). For K=s(H-E0),sigma=s*kappa>0,the actual ground-state transform gives

norm(v)^2=V, <v,Kv>=sigma*D<=12sigma Q.

The positive spectral measure mu_v has mass V and first energy moment at most12sigma Q. This is an exact ground-state identity for the ORIGINAL Hamiltonian,not the free electric energy formula3sigma. Jensen's inequality gives,for every tau>=0,

<v,exp(-tau K)v>
>=V*exp[-tau*<v,Kv>/V]
>= (Q/512)*exp(-6144sigma*tau).                        (8)

Upper variance and the previously proved gap also give upper bounds,but are not needed for this positive-time obstruction. All constants are uniform over box,coefficients and retained coupling. The exponential is intentionally conservative and not a physical mass prediction.

## 6. Fixed Schwartz witness and the interacting h^-4 failure

A positive-time lower bound is not by itself a statement about real-time S' boundedness. Supply a FIXED real-time test as well.

Suppose sigma_h<=M<infinity; necessarily M>0. Set L=12288M. Markov's inequality for the positive energy measure yields

mu_v((L,infinity))<=12M Q/L=Q/1024,
mu_v([0,L])>=Q/1024.                                 (9)

Choose one real Schwartz g whose even smooth compactly supported Fourier transform equals1 on [-L,L]. For the field with spatial coefficients b_p=z_h*h^3*f(x_p),the fixed spacetime test u(t,x)=g(t)f(x) gives

W_h(conjugate(u) tensor u)=norm(g_hat(K_h)v_h(f))^2
>=Q_h(f)/1024.                                       (10)

The temporal Fourier sign convention is irrelevant to the even plateau. This argument uses the actual interacting spectral measure,not a presumed excitation at3sigma. Spatial f may be any fixed nonzero real C_c^infinity test. Assume the actual boxes eventually contain its support plus the plaquette footprint; whole-space exhaustion is a sufficient choice. The geometric sampling identity is

Q_h(f)=z_h^2*h^6 sum_p f(x_p)^2,
Q_h(f)/(z_h^2*h^3)->3 integral f(x)^2 dx.

Consequently any normalization with z_h^2*h^3->infinity has divergent pairing against this ONE fixed Schwartz test at bounded clocks,uniformly over arbitrary retained eta_h. In particular z_h=h^-4 gives order h^-5 lower growth and no S'(R8)-bounded magnetic two-point family. Equation(8) also diverges at each fixed positive Euclidean time when sigma_h<=M.

This resolves the actual-interacting magnetic growth question,not merely a cap-budget obstruction. It does NOT prove the same growth for arbitrary electric/magnetic combinations. Indeed there is an exact source obstruction to an indiscriminate mixed coercivity bound. The ground-state equation,followed by vacuum-orthogonal projection,gives

sum_e (I-P_Omega)C_e Omega = eta*sum_p (I-P_Omega)w_p Omega. (11)

Thus the full-box constant-weight electric/magnetic combination with coefficients(1,-eta) has EXACTLY zero vacuum vector,although the magnetic variance is positive. On the two global sums the covariance Gram matrix has the rank-one form V_mag*[[eta^2,eta],[eta,1]]. Same-sign coefficients do not cancel this global channel,but that observation alone does not control spatially varying smears. A slowly-varying local Ward audit is therefore necessary before applying magnetic growth to a candidate scalar. No Lorentz identification is supplied here. Escaping clocks remain outside (9)-(10); iteration5 already gives an actual weak-zero counterexample to inferring real-time divergence from equal-time growth alone.

## 7. Falsifiers and scope

The direct route must fail if the thirteen-link conditional comparison is replaced by a global extensive density ratio,if covariance coercivity is inferred from a gap alone,if unbounded overlap is hidden in a volume-dependent derivative sum,or if the connection correction is lost. It must also fail if a free source is substituted for the interacting spectral moment.

A finite full-support two-spin law with covariance rho close to1 and an independent-block reset generator of gap1 has Var(X-Y)=2(1-rho),arbitrarily small relative to coefficient norm2. Independent blocks cluster exactly. This refutes gap/clustering alone as a uniform coercivity premise; its strong local density tilt is not the retained small-interaction source. Independent weakly biased product laws also show that a global density minimum may decay with volume while local variance coercivity remains uniform. The proof above avoids both errors.

The exact controls check quaternion generator/connection normalization,open-box stars,bounded-overlap Haar energy accounting,normalized local-likelihood comparisons,rational Bochner/Cauchy margins,positive spectral Jensen/Markov tests,and normalization planners. They freshly replay the predecessor receipt. They do not certify the actual interaction constructor,weighted Bochner theorem or infinite-dimensional distributions by finite enumeration. Independent review remains open.

## 8. Next executable mixed-reader Ward audit

Quantify the slowly-varying version of (11),rather than incorrectly applying magnetic coercivity to arbitrary mixed readers. The actual electric vacuum channel is the multiplication function

r_e=(C_e Omega)/Omega=C_e u-|gradient_e u|^2, u=log Omega,

so the actual interaction fixed-point equation may give support-wise Ward identities for C_e Phi_A and contracted gradient products. Attempt a uniform error bound comparing sum_e f(mid_e)r_e with eta*sum_p f(center_p)w_p after actual vacuum centering. Charge the physical variation of f across a connected support by h*diameter(A),and check the existing weighted norm pays for all support moments without third derivatives. Determine which relative electric/magnetic normalizations preserve the magnetic growth and which approach the conserved Hamiltonian-density direction. State an obstruction if the needed norm estimate does not follow; do not infer local cancellations from the full-box constant-weight identity alone.

After this native mixed-reader gate,the l2 sandwich also makes critical h^-3/2 interacting two-point compactness an available substantive construction: fixed positive eta and clock,Schwartz-kernel equicontinuity,nonzero plateau witness and subsequential extraction. It would still not by itself imply uniqueness,Lorentz covariance,Gaussian all-orders convergence or field reconstruction. The immediate selected continuation is the mixed Ward audit,because it controls whether the present magnetic obstruction applies to the proposed electric/magnetic candidate.

Contract: `contracts/yang-mills-interacting-magnetic-coercivity.v1.json`.
Checker: `checkers/check_yang_mills_interacting_magnetic_coercivity.py`.
Receipt: `results/yang-mills-interacting-magnetic-coercivity-v1.json`.

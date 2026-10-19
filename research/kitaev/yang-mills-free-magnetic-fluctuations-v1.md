# Native free-source magnetic fluctuation scaling

Owner `marici.Kitaev`; spatial-scaling iteration5/10. Selected issue `issue-tree:87b983be841a61be1b85d24a:free-magnetic-fluctuations:v1`.

## Question, risky prediction and disposition

The bounded-reader audit supplied cap removal,not a continuum limit. Here the already admitted eta=0 endpoint supplies an EXACT native two-point calculation. It predicts a nonzero spatial-white oscillator two-point limit at fluctuation normalization h^-3/2,not universal triviality. At bounded clocks the h^-4 candidate instead fails joint tempered boundedness. Escaping clocks can make that same candidate tend to ZERO in S',despite divergent equal-time variance.

This endpoint calculation neither replaces the interacting source nor proves an eta>0 theorem. No bare finite-g matching is asserted at eta=0. A magnetic reader is not being identified with a Lorentz scalar. Standard Haar/Peter-Weyl identities,Schwartz Fourier analysis and Riemann quadrature are analytic imports. Finite controls below test their exact geometric and scaling consequences,not infinite-dimensional convergence mechanically.

## 1. Actual finite source covariance and energy

Use finite open cubic boxes,one variable per positive geometric link,one elementary square per geometric plaquette. At lambda=0 the unique normalized physical vacuum is Omega=1 in product Haar and

Htilde_h=s_h H_h=sigma_h sum_e C_e, C_e=-Delta_e, sigma_h=s_h*kappa_h>0.

For w_p=(1/2)chi_(1/2)(W_p),a link exclusive to p integrates its fundamental representation to0. Hence Haar(w_p)=0. For p!=q there is a link in one square and not the other,including when the squares share an edge. Integrating that link proves Haar(w_p*w_q)=0. For p=q the holonomy is Haar-distributed and character orthogonality gives Haar(w_p^2)=1/4. Thus

<w_p Omega,w_q Omega> = delta_pq/4.

Each of the four distinct links of p carries spin1/2. Applying its Casimir gives3/4,so Htilde_h w_p=3sigma_h w_p. Put omega_h=3sigma_h. The exact connected kernels are

<w_p Omega,exp(-it Htilde_h)w_q Omega>=delta_pq*exp(-i omega_h t)/4,
<w_p Omega,exp(-tau Htilde_h)w_q Omega>=delta_pq*exp(-omega_h tau)/4.

These are native finite-source statements on the Gauss subspace,not kinematic charged one-link excitations. Geometric plaquette multiplicity matters: counting opposite orientations as independent squares would change the answer.

## 2. Sampled field and joint spacetime distribution

Let the physical mesh tend to0. Take centered open boxes Q_h=[-R_h,R_h]^3 with R_h on the mesh and R_h->infinity. Plaquette centers x_p have three shifted-grid orientations. This exhausting-box condition is part of the claimed translation-invariant whole-space limit; a fixed physical box would instead retain its boundary indicator.

For real z_h,define B_h(f)=z_h*h^3 sum_p f(x_p)w_p and set a_h=z_h^2*h^3. At each finite source this is bounded and gauge invariant. Its exact two-point bidistribution on Psi in S(R8) is

W_h(Psi)=(a_h/4)*h^3 sum_p integral dt ds
 exp[-i omega_h(t-s)] Psi(t,x_p;s,x_p).                 (1)

It is supported on spatial coincidence already at each mesh. Positivity follows from the vacuum Gram form,not from a claimed scalar interpretation.

Assume a_h->a_*<infinity and sigma_h->sigma_*>=0. Then jointly in S'(R8),

W_h -> W_*,
W_*(t,x;s,y)=(3a_*/4)*exp[-i3sigma_*(t-s)]*delta^3(x-y). (2)

The factor3 counts the three once-counted square orientations. This is not merely convergence at a few insertion times. Here is a direct bound sufficient for (2). Set F(t,s,x)=Psi(t,x;s,x). Weighted supremum norms of F and its first x derivative,with weights (1+|t|)^4(1+|s|)^4(1+||x||_infinity)^4,are bounded by finitely many Schwartz seminorms of Psi. For every orientation,whole-grid h-cube quadrature has error<=C*h times these seminorms. The chain rule uses (partial_xi+partial_yi)Psi on the diagonal. The missing boundary grid tail is<=C/(1+R_h) times the same seminorms (for R_h>=2); the retained centers include every shifted point away from the O(h) boundary strip. The weighted grid count is uniform,as in the previous reader proof.

The phase error is<=3|sigma_h-sigma_*|*|t-s|; the time weights have an integrable first moment. Multiplying by bounded a_h and controlling |a_h-a_*| proves a fixed-seminorm bound

|(W_h-W_*)(Psi)|<=C*[|a_h-a_*|+a_h*(h+(1+R_h)^-1+|sigma_h-sigma_*|)]*q(Psi).

This establishes joint tempered convergence for the stated source net. No interchange of an unidentified interacting thermodynamic state with a continuum limit is used.

## 3. Normalization classification at bounded clocks

For z_h=c*h^-p with fixed nonzero real c,a_h=c^2*h^(3-2p).

* p<3/2: W_h->0,even without a clock bound,since the phase has modulus1 and the weighted quadrature bound is uniform.
* p=3/2 and sigma_h->sigma_*: equation(2) is a finite nonzero ultralocal two-point limit with a_*=c^2.
* p>3/2 and sup sigma_h=M<infinity: the family is NOT bounded in S'(R8). In particular it cannot have a finite tempered limit.

The last conclusion needs a FIXED spacetime test,not a sharp-time variance argument. Choose a nonzero real spatial f in C_c^infinity and real Schwartz g whose even smooth compactly supported Fourier transform equals1 on [-3M,3M]. For u(t,x)=g(t)f(x),equation(1) gives exactly

W_h(conjugate(u) tensor u)=(a_h/4)*h^3 sum_p f(x_p)^2,

which is asymptotic to (3a_h/4)*integral f^2 and diverges. The sign convention for the temporal Fourier transform is irrelevant because the plateau is even. Equivalently,for every fixed tau>=0 the positive-time spatially smeared correlation has the lower bound

C_h(tau;f)>=(a_h/4)*exp(-3M*tau)*h^3 sum_p f(x_p)^2.

Thus the h^-4 trial normalization has a_h=h^-5 and fails actual joint tempered boundedness at every bounded clock,not just a reader norm estimate. This tests a trial normalization at the endpoint,not a calibrated finite-g Yang-Mills trajectory. Electric normalization cannot cancel this TWO-POINT divergence at this source: C_e Omega=0,so all electric and mixed vacuum two-point vectors vanish identically.

## 4. The nonzero limit is not relativistic

For a_*>0 and omega_*=3sigma_*,the relative-coordinate kernel is

W_*(t,x)=(3a_*/4)*exp(-i omega_* t)*delta^3(x).

With W(t,x)=integral exp(-iEt+ip.x) mu(dE,dp),its positive measure is

mu=(3a_*/4)*delta_(omega_*)(dE)*d^3p/(2pi)^3.

It gives positive measure to open spatial momentum regions |p|>omega_*; hence it violates the relativistic forward-cone spectrum condition. It is also not Lorentz invariant. At sigma_*=0 it remains nonzero and fails that cone condition: Lebesgue spatial momentum is not a spacetime zero-momentum atom. At sigma_*>0 the energy channel survives and is finite at every positive Euclidean time,but no propagation is generated.

The antisymmetric two-point kernel is -2i*(3a_*/4)*sin(omega_*t)*delta^3(x). Its spatial support is ultralocal. Thus spatial clustering and spacelike commutativity do not themselves imply Lorentz covariance or the relativistic spectrum. The source calculation explicitly realizes the previously conditional nonrelativistic possibility; it is not a counterexample to the scalar no-promotion theorem,whose hypotheses it fails.

No all-orders Gaussian state,field reconstruction or convergence of operator products is claimed from this two-point result.

## 5. Two native scope falsifiers

### Escaping energies: equal-time divergence does not imply S' divergence

Take z_h=h^-4 and sigma_h=h^-1. Then a_h=h^-5,omega_h=3/h. Integrate equation(1) by parts SIX times in t. The previous weighted plaquette count is h^3 sum_p(1+||x_p||_infinity)^-4<=384 and each time weight (1+|t|)^-2 integrates to2. Therefore

|W_h(Psi)|<=384*a_h/omega_h^6*q_6(Psi)
=(128/243)*h*q_6(Psi)->0,

where q_6 is the weighted supremum of partial_t^6 Psi on spatial coincidence,with those time/spatial weights. This is a fixed continuous Schwartz seminorm. Equal-time variance still diverges like h^-5; the positive-time Euclidean channel tends to0 at every tau>0. The bounded-clock premise is therefore essential to the divergence classification. The example is an actual source-clock sequence,not a substitution of a different vacuum or Hamiltonian truncation.

### Pairwise orthogonality is not joint independence or operator convergence

For a link e in p,

<Omega,w_p C_e w_p Omega>=(3/4)*||w_p Omega||^2=3/16,

although C_e Omega=0. Electric vacuum-vector disappearance does not license deleting electric insertions from multitime products.

There is also an exact purely magnetic higher-moment control. Take all six faces of one elementary cube. Their one-point means are0 and distinct-pair covariances are0,but

Haar(product_(six faces) w_p)=1/1024 !=0.

Orient the face boundaries outward (SU2 traces are real and orientation invariant). Every link then occurs once forward and once backward. Haar contraction of a fundamental matrix with its inverse contributes1/2 per link and identifies matching end indices. There are12 links,6 normalized traces and8 free vertex index loops. The integral is2^(8-12-6)=2^-10. This finite-source calculation refutes treating the plaquette family as jointly independent. It does not refute a possible Gaussian fluctuation limit; surviving local higher moments may vanish under fluctuation scaling. Such an all-orders limit needs its own proof.

## 6. Scope and next executable interacting test

Written output: exact actual-source eta=0 covariance/evolution,joint tempered scaling under explicit box exhaustion,the h^-4 bounded-clock divergence witness,a nonzero nonrelativistic two-point limit,and an actual escaping-clock weak-zero control. No eta>0 assertion or Lorentz/Yang-Mills construction follows.

Next derive an interacting magnetic fluctuation coercivity estimate,or isolate the exact failure to derive it from the retained actual interaction norm. A useful target is,uniformly in box and coefficients,

Var_(nu_Lambda)(sum_p b_p w_p)>=c(eta)*sum_p|b_p|^2,

with c>0 on an explicitly justified retained subwindow. Pair it with an upper bound on the actual ground-state Dirichlet energy of this multiplication smear. Jensen's spectral inequality would then give a fixed-positive-time lower bound at bounded sigma,extending the h^-4 growth obstruction to actual interacting vacua rather than replacing them by the free endpoint. The covariance lower bound must be PROVED; exponential clustering or a gap upper-bound-on-variance alone does not supply it. Check whether the existing interaction norm controls covariance perturbations in an l2 row-sum sense,including shared-link neighbors. This is a new executable interacting estimate,not a request to wait for continuum construction or external review.

Contract: `contracts/yang-mills-free-magnetic-fluctuations.v1.json`.
Checker: `checkers/check_yang_mills_free_magnetic_fluctuations.py`.
Receipt: `results/yang-mills-free-magnetic-fluctuations-v1.json`.

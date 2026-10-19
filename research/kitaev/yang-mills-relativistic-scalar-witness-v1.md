# Scalar witness bridge: ultralocal commutators versus relativistic nontriviality

Owner: `marici.Kitaev`. Spatial-scaling iteration3/10. Selected issue: `issue-tree:87b983be841a61be1b85d24a:relativistic-scalar-witness:v1`.

## DPC and verdict

**Problem.** The arbitrary-clock theorem needs a nonzero limiting commutator witness. A finite nonzero Euclidean channel alone does not supply it. Which explicit continuum and observer-comparison hypotheses make it unavoidable?

**Conjecture.** For a centered Hermitian SCALAR two-point distribution with Lorentz covariance,positive relativistic spectral measure and no zero-momentum atom,spatial ultralocality of its commutator forces the entire channel to vanish. A faithful joint tempered cutoff comparison also supplies the Euclidean clock witness without assuming a sharp-time continuum field.

**Rivals.** Replace boosts by spatial rotations; replace the forward-cone spectrum by H>=0 alone; infer absence of zero modes from centering; treat pointwise insertion convergence as a joint distributional comparison; infer a continuum scalar from a magnetic plaquette label; assume uniform sharp-time vector norms for composite fields; promote a scalar-channel conditional obstruction to universal Yang-Mills triviality.

**Risky consequence.** A single-comparison conditional no-promotion theorem for the covered cutoff family,removing the previously additional timelike-witness assumption. Its actual state/field comparison remains an obligation,not something the theorem constructs.

**Falsifiers.** The positive ultralocal oscillator distribution exp(-i omega t)delta^3(x) has nonzero finite Euclidean correlations and zero separated commutators but fails Lorentz covariance and the relativistic spectrum. A centered random constant field has W=1 and a zero-momentum atom despite positivity/covariance; clustering or a genuine vacuum condition is essential. Local distribution convergence alone is not an automatic Fourier/Laplace convergence rule without further growth control.

**Verdict.** The conditional scalar/support/spectral theorem and a sufficient joint-tempered reader comparison are proved below at written-proof scope. No actual continuum field or cutoff scalar comparison has been constructed. Next executable task: construct actual bounded electric/magnetic scalar reader CANDIDATES and audit their vacuum truncation tails,so norm-budget coverage is not asserted for an unbounded or merely named field.

## 1. Continuum scalar assumptions,without assuming a reconstructed theory

Work in3+1 Minkowski dimensions,with p.x=p0*t-p_space.x. Let W in S'(R4) be a translation-invariant connected Hermitian scalar two-point distribution,with Fourier convention

W(x)=integral exp(-i p.x) mu(dp)

in the distribution sense. Assume:

(S1) mu is a positive tempered Radon measure supported in Vplus={p:p0>=|p_space|}. One may obtain this from positive type and the relativistic spectrum condition; here the measure and support are explicit assumptions.

(S2) W is invariant under proper orthochronous Lorentz transformations. Spatial rotation invariance alone does not suffice. This is a SCALAR channel,not one component of a tensor that mixes with omitted components under boosts.

(S3) mu({0})=0. Centering alone does not prove this. It follows,for example,from the centered channel in a positive-energy Hilbert realization whose only zero-energy vector is the vacuum,or from the appropriate connected spatial clustering property after the conclusion below reduces W to a constant.

Nontriviality for this theorem means mu is not the zero measure. No actual Yang-Mills field,OS reconstruction or equivalence of these assumptions to the full official target is supplied here.

Define the vacuum commutator distribution C(x)=W(x)-W(-x). It need not be a pointwise function.

## 2. Spatial coincidence plus Lorentz covariance implies contact support

Suppose supp(C) is contained in the time axis T={(t,0)}. Scalar Lorentz invariance makes supp(C) invariant under boosts. Every nonzero point (t,0) has a boost image with nonzero spatial coordinate. That image cannot lie in T. Therefore

supp(C) subset {0}.

This is a support statement,not a claim that Lorentz invariance maps separated lattice supports into themselves. It is applied only to the assumed CONTINUUM distribution after the cutoff comparison.

A distribution supported at one point has finite order there and is a finite sum of derivatives of delta. Its Fourier transform is a polynomial P(p),with convention-dependent constant factors irrelevant below. On the other hand,

C_hat=mu-check(mu), check(mu)(B)=mu(-B),

so supp(C_hat) lies in Vplus union Vminus. The spacelike momentum region is a nonempty open complement. The polynomial P vanishes there,so the polynomial identity theorem gives P=0 everywhere. Hence C=0 and mu=check(mu).

The equal measure is supported in BOTH cones,whose intersection is {0}. Thus mu=c*delta_0 with c>=0. By S3,c=0,so W=0.

This proves: a nonzero S1-S3 scalar channel must have a commutator with support outside spatial coincidence. No explicit nonzero numerical timelike matrix element was inserted. With ordinary local commutativity,the surviving support is causal (timelike OR lightlike),not necessarily strictly timelike: the four-dimensional massless free scalar is a light-cone-only warning. Locality alone does not justify the stronger word 'timelike'. The cutoff bound vanishes at ALL spatial separations and finite times,including the light cone,so the contradiction needs no such extra assertion.

## 3. Sufficient cutoff observer/state comparison

Use the SAME actual finite source boxes,physical vacua Omega_h,and clock-rescaled Hamiltonians Htilde_h as in the previous theorem. Their gap premise is Htilde_h>=c0*sigma_h*(I-Pvac_h),c0=5/64,and eta_h<=eta_star. At finite boxes the actual positive vacuum is unique; all centerings/projections below must match that actual vacuum.

Assume a real-linear family f->A_h(f) of bounded gauge-invariant Hermitian operators for real f in C_c^infinity(R3). Required comparison data are:

(O1) Actual link-midpoint support of A_h(f) lies in an epsilon_h-neighborhood of supp(f),epsilon_h->0. For every fixed spatially separated f,g,the norm/support budget

limsup h log max(1,|X_h(f)|*||A_h(f)||*||A_h(g)||/2)

is finite. Operators may have polynomial or finite-exponential cutoff norms. Neither a bounded sharp-time continuum field nor a uniform sharp-time Hilbert vector norm is assumed.

(O2) Center A_h in its actual vacuum. Time-translate using Htilde_h and smear in time with compactly supported smooth functions. Suppose these cutoff connected two-point forms extend to tempered bidistributions W_h^(2) on R4 times R4,AND

W_h^(2) -> W^(2), W^(2)(x,y)=W(x-y), in S'(R8),

where W satisfies S1-S3. The comparison includes both operator orderings and the same vacuum/clock; it is not a pairing copied between different cutoff Hilbert spaces.

The finite time-smearing integral can be defined strongly/weakly on vectors; norm continuity of every local bounded observable is not needed. O2 is an explicit joint state/observer hypothesis,not derived from the lattice Feller law or from convergence of finitely many insertion values.

### Why this is a substantive growth/convergence obligation

A sufficient route to O2 is to provide an actual continuous candidate W^(2),convergence on a test-function-dense tensor class,and a COMMON tempered seminorm bound for W_h^(2). Approximate a general test by that class; the common bound controls the approximation error uniformly in h,then continuity controls the candidate. This proves full S' convergence. The estimate and candidate must actually be supplied; dense-class convergence without uniform control is not a proof.

For the commutator-support step below,local D' convergence with its required continuity is sufficient. We use the stronger joint S' comparison also to justify the spectral Fourier/Laplace passage. If only weaker convergence is available,it needs its own positive-spectrum/growth argument or a separately verified Euclidean witness. No such upgrade is silently assumed.

## 4. Derive the clock witness from the same tempered comparison

Fix real compactly supported f and put v_h(f)=(A_h(f)-<A_h(f)>)Omega_h. Since the finite vacuum is unique,this is orthogonal to Pvac_h. Set

R_h(t;f)=<v_h(f),exp(-it Htilde_h)v_h(f)>.

Stationarity and O2 imply R_h -> R_f in S'(R): test W_h^(2) with q(t-s)chi(s)f(x_space)f(y_space),where q,chi are Schwartz and integral chi=1. The linear change to relative/center times preserves Schwartz test functions. Thus the source temporal spectral measures nu_(h,f),supported in[0,infinity),converge in S' to the continuum measure

nu_f(dE)=integral |f_hat(p_space)|^2*delta_(p0)(dE) mu(dp).

The Fourier normalization is fixed consistently. Positivity and the forward cone make nu_f a positive tempered measure: bounded energy intervals contain bounded spatial momentum,and the remaining growth is polynomial.

For any tau>0 choose a smooth Schwartz function g_tau(E) that equals exp(-tau E) on E>=0 and is cut off on E<=-1. The positive-energy support then gives

<v_h,exp(-tau Htilde_h)v_h> -> integral exp(-tau E) nu_f(dE).

This step uses tempered distribution convergence and a Schwartz test; it is not analytic continuation inferred from pointwise real-time values.

If mu is nonzero,there is an f with nu_f nonzero: choose a compactly supported smooth spatial test whose Fourier transform is nonzero near a point in supp(mu). Positive measure and continuity give positive mass there. The forward-cone condition and polynomial measure growth make its Euclidean integral finite for EVERY tau>0. It is positive. Hence the previous theorem's clock witness follows at tau=t*/2 and t*,with the SAME source family and clock. No sharp-time limiting vector has been used.

It follows that sigma_h is bounded and J_h=eta_h*sigma_h is bounded.

## 5. Transfer the locality bound to commutator support

For compact time tests q1,q2 and real spatial tests f,g with positively separated supports,O1 and the arbitrary-clock locality theorem give

||[tau_t(A_h(f)),tau_s(A_h(g))]|| ->0

uniformly for t,s in the fixed compact time supports. The identity [tau_t A,tau_s B]=tau_s([tau_(t-s)A,B]) permits the previous compact-time estimate. Smearing and vacuum expectation therefore tend to zero. O2 identifies this limit with the value of

C^(2)(x,y)=W(x-y)-W(y-x)

on q1(t)f(x_space)q2(s)g(y_space). The continuum distribution thus annihilates all such spatially separated tensor tests.

This implies supp(C^(2)) lies in the spatial diagonal {x_space=y_space}. Any compact subset of its complement has a finite cover by product rectangles with separated spatial projections; a partition of unity and density of smooth tensor products in the test-function topology extend the zero values to every test there. Crucially the extension uses continuity of the ALREADY ASSUMED limiting distribution. No cutoff limit is interchanged with an uncontrolled infinite tensor expansion.

Change variables z=x-y,u=y. For any compact test phi(z) supported where z_space!=0,pair C^(2) with phi(x-y)psi(y),integral psi=1. It gives C(phi)=0. Hence supp(C) is contained in the time axis. Section2 now forces W=0,contradicting the assumed nonzero scalar channel.

## 6. Combined conditional no-promotion theorem

There is no cutoff family simultaneously satisfying:

1. the retained physical gap-to-electric floor and bounded eta;
2. a positive whole-Hamiltonian clock factor;
3. actual bounded local scalar reader maps with O1;
4. the faithful joint tempered comparison O2;
5. a nonzero Lorentz-scalar positive forward-cone two-point measure with its zero-momentum atom removed as in S3.

The earlier two witnesses are no longer independent assumptions: O2 and nontriviality supply the Euclidean clock witness,and Lorentz/spectral assumptions supply the non-ultralocal commutator witness. One still MUST construct or justify O1-O2 for an actual source observable. This result does not assert that the source does so,nor identify a magnetic plaquette as a Lorentz scalar.

## 7. Sharp scope guards

### Positive Hamiltonian energy alone is insufficient

The ultralocal oscillator has W(t,x)=exp(-i omega t)delta^3(x),omega>0. Its Fourier measure is positive on p0=omega with unrestricted spatial momentum. It has positive Hamiltonian energy and finite nonzero Euclidean correlations after spatial smearing,but fails the relativistic cone spectrum and Lorentz covariance. Its commutator remains on the time axis. A boost of the rest momentum leaves that fixed energy hyperplane,and arbitrarily large spatial momenta are spacelike. This is a consistent nonrelativistic guard,not a relativistic Yang-Mills example.

### Centering is not removal of every zero mode

Take a random constant field with values+1,-1 and equal weights. Its mean is0 and W=1. It is positive,scalar Lorentz invariant,has mu=delta_0 and commutator0. The connected spatial clustering property fails. A Hilbert realization has an extra invariant vector; uniqueness of a centered expectation alone does not remove it. Therefore S3 cannot be omitted or replaced by the word 'centered'.

### Composite fields need not exist at sharp time

Positive spectral measures may have divergent total mass but finite Laplace integrals at all positive times. For example the truncated energy measures sum_(n=1)^N n^p delta_n,p=0,2,4,have diverging mass while their integrals against2^-E are bounded by1,6,150,respectively. They are spectral scope fixtures,not Lorentz-invariant field examples. Our proof never infers a finite limiting norm ||Phi(0,f)Omega|| from finite positive-time correlations.

### Topology and covariance must be actual hypotheses

The distributions 2^(2N^2)delta_(t=N) converge to0 on compactly supported time tests but not in S': pairing the Schwartz function2^(-t^2) gives2^(N^2). This generic non-positive-type example demonstrates the topology distinction; it is not a counterexample satisfying all spectral assumptions above. No unproved automatic Fourier passage is permitted.

A magnetic B^2 plaquette reader is not by itself a Lorentz scalar: boosts mix electric and magnetic components. Neither bare weak-field naming nor spatial rotation covariance supplies S2 or O2. Likewise a selected scalar channel is not automatically a faithful generating family for the full gauge theory.

## 8. Next actual-source task

The conditional relativistic witness bridge is supplied; the missing physics is now localized at the ACTUAL reader comparison. Construct a bounded gauge-invariant electric/magnetic scalar candidate without changing the Hamiltonian/vacuum. For example,a local Casimir cap is a bounded Gauss-compatible observer,not a spin truncation of the source. Track its norm/support budget and quantify the actual-vacuum tail needed to compare it with the intended uncapped operator after smearing/normalization.

Prove a sufficient source estimate or identify precisely what the retained C2 interaction control does not supply. Do not infer a continuum scalar comparison merely because the capped candidate is bounded or its classical weak-field expression resembles Tr(F^2). This is a nonredundant executable source-interface obligation following the theorem,not a waiting leaf for a future continuum construction.

Independent review,changed-regime refinement and full physical reconstruction remain open. The old loop-static task remains deferred and no frozen predecessor is rewritten.

Contract: `contracts/yang-mills-relativistic-scalar-witness.v1.json`.
Checker: `checkers/check_yang_mills_relativistic_scalar_witness.py`.
Receipt: `results/yang-mills-relativistic-scalar-witness-v1.json`.

# Actual ground-weighted relative-orientation readout

## Question and disposition

Does the separate-trace reader retain the shared-loop state under the actual thermodynamic vacuum, or was the old blindness result an artifact of using Haar rather than the ground measure?

**Written quantitative extension to the actual measure:** throughout 0<=r<27/262144, set R=4096r/3<9/64. Let S be the seven links of two distinct squares sharing one link, let x,y be their common-basepoint loop holonomies and put

\[
T=(\operatorname{Tr}x,\operatorname{Tr}y),\qquad
h=\operatorname{Tr}(xy)-\tfrac12\operatorname{Tr}x\operatorname{Tr}y.
\]

For the actual thermodynamic measure nu, define m(T)=E_nu[h|T] and h_perp=h-m(T). Then

\[
\mathbb E_\nu[h_\perp\mid T]=0,\qquad
\|h_\perp\|_{L^2(\nu)}^2
\ge\frac34e^{-7R/4}
\ge\frac34(1-7R/4)
>\frac{579}{1024}>0.
\]

Thus the actual separate-trace projection has a nonzero gauge-invariant kernel vector, with a volume-independent norm bound. Even augmenting this reader with every exterior link does not remove the averaged conditional-variance lower bound. The result concerns the equal-time L2 reader, not an energy estimate or a low-energy family.

The Haar-only counterexample is already in `yang-mills-quotient-descent-v1.md`. It is an input here, not a new result. The new constructor is the actual-density comparison and actual weighted centering, valid on the full existing strong-coupling window, rather than only the tiny mixed-covariance interval of iteration 5. Independent analytic review remains open.

## Issue-boundary conjecture and falsifiers

**Problem:** changing the measure changes conditional expectation. Haar-centered h need not remain orthogonal to the trace reader.

**Conjecture:** the actual seven-link conditional densities have a uniform lower likelihood bound, preserving a positive distance from h to every trace-only function after actual centering.

**Rivals:** reuse Haar centering; infer blindness without a lower density bound; turn an averaged conditional-variance bound into a uniform pointwise fiber bound; infer low energy or dynamical closure from L2 reader blindness.

**Risky consequences:** a seven-link log-likelihood oscillation at most7R/4; a strictly positive global projection residual; a tilted positive-law control in which raw h has nonzero reader projection; a singular orientation law in which the residual disappears when the density hypothesis is removed.

## Local likelihood bound from the actual source

Use the actual Gibbs specification constructed in `yang-mills-thermodynamic-vacuum-v1.md`, with N2(Phi)<=R and log interaction2Phi. Every retained nonempty label is a union of elementary plaquettes, so |A|>=4, even when its evaluated function has smaller support. Consequently

\[
\sum_{A:A\cap S\ne\varnothing}W(\Phi_A)
\le\sum_{e\in S}\sum_{A\ni e}W(\Phi_A)
\le\frac7{16}R.
\]

For fixed exterior eta the conditional log weight V_eta=2 sum_(A meets S)Phi_A has supremum norm at most7R/8 and oscillation at most D=7R/4. Terms are uniformly summable; no global infinite-product density is asserted. Its normalized density w_eta relative to product Haar mu_S therefore satisfies

\[
e^{-D}\le w_\eta\le e^D,
\qquad w_\eta(z)\le e^D w_\eta(z')
\quad(z,z'\in SU(2)^S).
\]

DLR disintegration gives the actual marginal density w_S(z)=int w_eta(z) nu_(S^c)(d eta). The same lower/upper bounds and pairwise ratio bound pass to this mixture. In particular the marginal is equivalent to Haar with a uniform positive lower bound; no identification of finite-box ground-state marginals is used. The same argument applies to each finite-box source conditional or marginal when S is inside that box.

## The Haar fiber calculation, used only as input

Under product link Haar, the two holonomies x,y are independent Haar. Write x=a+b u, y=c+d v where b=sqrt(1-a squared), d=sqrt(1-c squared), and u,v are independent uniform unit vectors in R3 conditional on a,c. Then

\[
h=-2bd\,u\cdot v,\qquad
E_\mu[h\mid T]=0,\qquad
v_0(T):=E_\mu[h^2\mid T]
=\frac43(1-a^2)(1-c^2).
\]

Quaternion second moments give E_mu h squared=3/4. These are known Haar identities, not statements about the actual conditional angular distribution.

A concrete actual centering is available without replacing the state. Push w_S mu_S forward to the two holonomies using a spanning-tree Haar parametrization, integrating the five tree variables; call its positive density K(x,y) relative to independent Haar. For |a|,|c|<1,

\[
m(2a,2c)=
\frac{\int_{S^2\times S^2}[-2bd\,u\cdot v]
 K(a+bu,c+dv)\,d\sigma(u)d\sigma(v)}
 {\int_{S^2\times S^2}K(a+bu,c+dv)\,d\sigma(u)d\sigma(v)}.
\]

The denominator is bounded below by e^(-D). Define m=0 at the degenerate fibers where bd=0; these have Haar and nu trace-marginal measure zero. This is a bounded measurable local readout, |m|<=2, constructed from the actual marginal. No assertion that it vanishes at positive coupling, or that its closed form is known, is required. Since h and T are gauge invariant, h_perp is gauge invariant and bounded by4.

## Variational proof and the stronger exterior reader

For every square-integrable trace-only g, marginal domination and Haar conditional centering give

\[
\int(h-g(T))^2\,d\nu
\ge e^{-D}\int(h-g(T))^2\,d\mu_S
=e^{-D}\left(\frac34+\|g(T)\|_{L^2(\mu_S)}^2\right).
\]

Equivalence of the marginal norms makes the comparison valid on the whole L2 reader, not just polynomials. Conditional expectation is the orthogonal projection onto the closed trace-reader subspace. Infimizing proves the stated3e^(-D)/4 bound. The rational inequality exp(-D)>=1-D, with D<63/256, gives the strict579/1024 lower bound. This is a single domination comparison, not two successive estimates that needlessly square the likelihood constant.

More strongly, let B=sigma(T,U_(S^c)). For any B-measurable g(T,eta), apply the same inequality inside each conditional kernel gamma_S( . |eta) and integrate nu_(S^c). The reference law is mu_S times the actual exterior marginal, so its conditional Haar centering remains valid. Therefore

\[
\mathbb E_\nu\operatorname{Var}_\nu(h\mid B)
\ge\frac34e^{-D}.
\]

At a fixed trace fiber the appropriate bound is instead

\[
\operatorname{Var}_\nu(h\mid T=t)\ge e^{-D}v_0(t)
\]

almost everywhere; conditioning the bounded-ratio marginal density onto the fiber preserves its ratio bound. The analogous conditional-on-exterior version also holds. The factor v0(t) can approach zero, so the global579/1024 bound is NOT a uniform lower bound for each trace fiber.

## Exact controls and deliberate failures

The checker freshly replays the mixed-correlator receipt. It checks243 labelled activity arrays against the7R/16 incidence bound and the exact rational cutoff arithmetic. A positive rational24-point rule on S3 (eight signed axes and sixteen sign vectors with coordinates plus/minus1/2, all weight1/24) has the true Haar moments through degree5. The checker verifies those monomial moments explicitly; it does not use signed-axis degree-two cubature for fourth moments.

For the artificial smooth tilt w_epsilon=1+epsilon h, |epsilon|<=1/4, the normalization is1 and the trace marginal is unchanged. Its exact conditional mean is epsilon v0(T), not zero, and

\[
\|h-\epsilon v_0(T)\|_{L^2(w_\epsilon\mu)}^2
=\frac34-\frac{25}{36}\epsilon^2.
\]

Here E_mu(v0 squared)=25/36 uses genuine fourth moments. The576 loop-pair cubature fixtures verify centering against bounded trace polynomials and the residual norm for five declared tilts, including407/576 at epsilon=1/4. These tilts are diagnostic laws, not the actual vacuum.

Two other failures delimit the argument. A singular law x=y makes h=-2(1-a squared) a function of T and its projection residual zero: without the actual lower density hypothesis, Haar blindness need not survive. Even the actual Haar source has v0(t) arbitrarily small near a trace endpoint, rejecting a constant pointwise-fiber bound. A one-link artificial activity also violates the7R/16 estimate if the retained-label minimum-size hypothesis is dropped; it is not an admissible source interaction.

## Scope, residual and next executable issue

The supplied object is a nonzero actual-ground-weighted local L2 cylinder in the orthogonal complement of the entire separate-trace reader, with a quantitative norm bound. The actual conditional mean is used, not assumed equal to the Haar mean. Neither smoothness nor membership of h_perp in the closed gradient form domain is proved here, and no energy/Rayleigh bound, low-energy counterexample, particle interpretation or continuum claim is made.

**Next:** test whether the separate-trace reader is invariant under the actual thermodynamic generator. A smooth input such as pq is in the existing source cylinder core; its generator can be compared with its reader projection without assuming regularity of m(T). This would distinguish missing equal-time data from a genuine failure of the reduced reader to carry source dynamics. The finite-electric shared-link failure is already known and must not be recounted as the positive-coupling thermodynamic result.

Contract: `research/kitaev/contracts/yang-mills-weighted-orientation.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_weighted_orientation.py`.
Receipt: `research/kitaev/results/yang-mills-weighted-orientation-v1.json`.

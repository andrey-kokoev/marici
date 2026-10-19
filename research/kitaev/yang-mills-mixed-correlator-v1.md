# A nonzero actual mixed-plaquette covariance with controlled remainders

## Question, claim boundary and disposition

Can the actual infinite-lattice vacuum have a certified nonzero connected correlation between two distinct link-sharing plaquettes, rather than merely a nonzero coefficient in a surrogate density?

**Written constructive witness:** let p,q be the fundamental traces on two elementary squares sharing one link in the bulk. Define r_star=(3/4)^512. For the actual thermodynamic source and every r in [r_star/2,r_star],

\[
\frac{r^2}{1404}\le
\operatorname{Cov}_{\nu_r}(p,q)
\le\frac{3r^2}{1404}.
\]

This is a very small positive subinterval of the existing electric-dominant regime. The proof combines an exact all-box coefficient, finite-box analytic normalization and Cauchy bounds, and the existing quantitative thermodynamic boundary comparison. It does not claim uniform analyticity of an infinite-volume complex state or require one. The enormous comparison box is defined analytically, not simulated or diagonalized.

This proves a nonproduct gauge-observable law at the stated lattice couplings, conditional on the written upstream analytic theorems. A nonzero two-point function is not proof of a non-Gaussian interacting continuum field theory. No continuum existence, weak-coupling refinement, physical mass/clock calibration or independent analytic review is supplied.

## Issue-boundary conjecture and rivals

- **Problem:** clustering upper bounds allow all mixed covariances to vanish; a formal Taylor coefficient does not control the actual infinite-volume expectation.
- **Conjecture:** the shared-spin channels produce coefficient 1/702 at order r squared, and explicit finite analytic and boundary budgets preserve its sign on a declared positive interval.
- **Rivals:** missing plaquette contributions cancel the coefficient; replacing the actual vacuum by a Taylor density; a complex normalization zero invalidates Cauchy estimates; finite-volume errors overwhelm the positive term.
- **Risky consequences:** the all-box coefficient is unchanged by spectator plaquettes, the selected complex partition denominator stays away from zero, and both remainder budgets are at most one quarter of the leading term.
- **Falsification/disposition:** exact Haar/cubical-parity and rational budget tests accompany the proof. A same-leading-coefficient sign-flip and a complex normalization-zero model reject the two shortcuts, not the scoped actual-source construction.

## Source and the all-box coefficient

Keep the actual source of the predecessor packets. Let p=Tr(W_p), q=Tr(W_q), so |p|,|q|<=2. The two fundamental loop holonomies x,y have independent Haar laws under product link Haar: conditioning on the shared link leaves the disjoint three-link outer products independent Haar. Write F=pq=F_0+F_1. The shared-link projection gives

\[
\|F_0\|^2=1/4,\qquad\|F_1\|^2=3/4,
\qquad\langle F_0,F_1\rangle=0.
\]

The actual second-order log-density pair interaction is

\[
J_{pq}=F_0/54-F_1/234.
\]

Consequently its Haar pairing is

\[
\langle F,J_{pq}\rangle
=\frac1{216}-\frac1{312}=\frac1{702}.
\]

Spectator terms do not change this coefficient. Multiplication of any link by the central element -I makes a nonzero Haar integral require even fundamental parity on every link. A nonzero finite cubical 2-cycle over F2 in the cubic lattice has at least six faces: cubical H2 vanishes, so it bounds a finite nonempty cube 3-chain, which exposes a face in each of the six extremal coordinate directions. Thus at most four distinct elementary plaquettes cannot form a nonzero closed 2-cycle. In the order-two density pairing with pq, only the matching unordered pair survives. Self-character terms have even link parity and cannot cancel the odd boundary of p+q. The shared-spin projection preserves the pair's center parity.

The first-order mean coefficients of p,q are each 1/3. Exponentiating the first-order log density contributes 1/9 to the second-order pq expectation, exactly canceled by the product of means. The surviving covariance coefficient is therefore 1/702. In every finite box containing the pair,

\[
C_\Lambda(z):=\nu_{\Lambda,z}(pq)
-\nu_{\Lambda,z}(p)\nu_{\Lambda,z}(q)
=\frac{z^2}{702}+O_\Lambda(z^3).
\]

Neither this formula nor fixed-box analyticity alone proves the witness.

## A finite complex disk with controlled normalization

Let E be the link count in a finite box and take

\[
\eta=\frac{3}{131072E}.
\]

Iteration 9's complex-bilinear interaction fixed point is analytic for |z|<27/262144 and has N_2(Phi(z))<=4096|z|/3. On |z|<=eta its finite sum u_Lambda(z)=sum_A Phi_A(z) obeys

\[
\|u_\Lambda(z)\|_\infty\le E N_2(\Phi(z))\le1/32.
\]

The inequality uses the actual labelled interaction sum; every nonempty component is counted by at least one anchored link. Constants do not affect normalization. Define the analytic expectation by exp(2u_Lambda(z)), with no complex conjugation off the real axis. For real nonnegative z this is the actual positive vacuum density. Replacing it by |exp(u(z))| squared off the real axis would destroy holomorphy and is not done.

Since exp(1/16)<=16/15,

\[
|Z_\Lambda(z)-1|\le1/15,\qquad
|Z_\Lambda(z)|\ge14/15.
\]

For |h|<=b the normalized analytic expectation has magnitude at most 8b/7. Therefore

\[
|C_\Lambda(z)|\le32/7+256/49=480/49<10.
\]

The disk lies strictly inside the contraction domain; its contraction ratio is 2/(9E)<1. The analytic branch exists on a neighborhood of the closed disk. Cauchy's coefficient estimate gives, for 0<=r<=eta/2,

\[
\left|C_\Lambda(r)-\frac{r^2}{702}\right|
\le\frac{10(r/\eta)^3}{1-r/\eta}
\le20r^3/\eta^3.
\]

This is a finite-box expectation remainder, not merely a log-density remainder. Its radius is allowed to depend on E.

## Boundary comparison and exact witness parameters

Set n=512, d=4n=2048, M=d+2 and use vertices in [-M,M]^3. Then L=2d+5=4101 and

\[
E=3L^2(L-1)=206863872300.
\]

Place the two squares near the origin, with their seven link-source coordinates inside [-2,2]^3. A plaquette-adjacency step changes any link-source coordinate by at most one. A link outside the induced box has a source coordinate of magnitude at least M, so the source support distance to the complement is at least M-2=d. This proves the required buffer without enumerating this box.

The previous thermodynamic comparison has prefactor at most 8/7. Single-link oscillation sums satisfy L(p)<=16, L(q)<=16 and L(pq)<=64: six outer links contribute at most 8 each and the common link at most 16. Using the sup norms 2 to compare the products of means gives

\[
|C_\infty(r)-C_\Lambda(r)|
\le\frac{1024}{7}(3/4)^d
= B r_\star^4,\qquad B=1024/7.
\]

The exact rational checker verifies

\[
r_\star<27/262144,\quad
r_\star\le\eta/2,\quad
r_\star\le\eta^3/56160,\quad
B r_\star^2\le1/11232.
\]

For every r in [r_star/2,r_star], the analytic error is at most r squared/2808 by the third inequality. The boundary error is at most r_star squared/11232 and hence at most r squared/2808 by the fourth inequality and r>=r_star/2. Subtracting or adding both errors to r squared/702 gives exactly the stated positive lower and upper bounds.

The limits are not interchanged: one declared finite comparison box and one coupling interval are chosen, its actual expectation is controlled analytically, and the established thermodynamic comparison controls the actual infinite-volume state. There is no claim of a volume-independent complex partition-function radius.

## Exact controls and surviving scope

The checker freshly replays the linked-density and source-clustering receipts. It computes the Haar pair moment with degree-two-exact signed coordinate-quaternion moments; scans finite cubic boxes for center-parity obstructions as a regression for the written all-box lemma; and verifies all normalization constants, coefficient arithmetic and interval error budgets with fractions. The 206-billion-link box is never materialized; only its count formula and integer powers are evaluated.

Two deliberate failures remain explicit. C_bad(r)=r squared/702-r cubed/(351r_star) has the same leading coefficient but negative value at r_star, violating the certified Cauchy coefficient budget. Also Omega_N(z)=(1+Nz,1-Nz) is entire and gives positive real normalization 1+N squared z squared, yet that normalization vanishes at z=i/N. Analytic numerator data and real positivity alone do not authorize the normalized complex disk used here.

**Disposition:** an actual mixed-plaquette nonproduct witness is supplied on the explicit tiny interval, not on the full earlier coupling window. The next executable issue is whether the separate-trace readout remains nonfaithful under the actual thermodynamic ground measure: construct a centered relative-orientation probe with a quantitative conditional-variance bound. The Haar-only counterexample already exists in `yang-mills-quotient-descent-v1.md` and must not be counted again as new work. This matters for source observable completeness, not as an automatic continuum bridge. The official existence/gap and parent continuum-correlation gates remain open.

Contract: `research/kitaev/contracts/yang-mills-mixed-correlator.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_mixed_correlator.py`.
Receipt: `research/kitaev/results/yang-mills-mixed-correlator-v1.json`.

# Uniform boundary leakage for every nontrivial finite cubic-box reader

## Question, quantifiers and disposition

Can enlarging the full local reader to a finite cubic box make it an exact invariant subsystem of the actual thermodynamic dynamics?

**Written uniform rejection:** let Lambda be the induced links of any translated cubic vertex box of side L>=2. Choose a plaquette trace p_Lambda in a coordinate plane at its lower corner. For the actual source projection Pi_Lambda=E_nu[ . |U_Lambda], Q_Lambda=I-Pi_Lambda,

\[
\|Q_\Lambda A p_\Lambda\|_{L^2(\nu)}
>\kappa r/4\qquad(0<r\le10^{-9}).
\]

The same coupling interval and constant work for every side length and translation. All internal link functions, not just separate traces, are allowed as predictors. The bound does not compare an entire box marginal with Haar.

**Necessary exception:** L=1 has no induced links or plaquette; its constant reader is invariant. The literal assertion for every box including this empty case is false. Nor is a theorem for every non-cubic finite edge set asserted.

The actual cylinder core gives the corresponding positive initial leakage rate, and the compressed semigroup's quadratic small-parameter memory coefficient on p_Lambda exceeds kappa squared r squared/16. These are source-unit statements with independently unreviewed analytic dependencies, not a continuum or mass-gap obstruction.

## Issue-boundary conjecture and rivals

**Problem:** the fixed seven-link proof compared its entire reader support inside one small resampling set. That argument cannot be copied to a large reader without paying a volume-dependent Haar-density factor.

**Conjecture:** conditional resampling of only the boundary plaquette and its neighbors preserves a positive residual even when the predictor retains every other box link.

**Rivals:** reuse a whole-box Haar comparison; quietly discard the predictor's exterior-to-neighborhood advice; replace actual weighted centering by Haar centering; repeat a fixed-patch fixture as a theorem over unbounded boxes; confuse nonclosure of a restriction with nonexistence of finite-volume source dynamics.

**Risky consequences:** at least six exterior neighbor channels for every L>=2; a fixed at-most-forty-link resampling set; a conditional variational bound valid for arbitrary box-measurable predictors; an actual all-orders tail smaller than the leading signal at one common coupling interval.

## Boundary geometry with only two side-length cases

Translate the box to vertices {0,...,L-1} cubed and take p in the xy plane based at(0,0,0). The plaquette has twelve link-sharing neighbors. Four perpendicular neighbors extend to z=-1 and are outside; four extend to z=+1 and are inside for every L>=2. Of the four coplanar neighbors, those across x=0 and y=0 are outside. The two across x=1 and y=1 are inside exactly when L>=3. Thus the number k of exterior neighbors is

\[
k=8\ (L=2),\qquad k=6\ (L\ge3).
\]

Let D contain p and all twelve neighbors, so |D|<=40 (the exact geometry has32 links). This set is independent of L up to translation. Let H be the sum of h_ps=-2Gamma(p,s) over the k neighbors not wholly contained in Lambda.

Each exterior neighbor has an edge outside Lambda, hence outside the predictor, with odd center parity in h_ps. Therefore

\[
E_{\mu_D}[H\mid U_{D\cap\Lambda}]=0,
\qquad\|H\|_{L^2(\mu_D)}^2=3k/4.
\]

Distinct channels are orthogonal because their parity product has nonempty boundary difference. These are Haar reference identities only. They do not assert the actual conditional mean is zero.

## Conditional comparison that retains all box information

The actual DLR kernel on D has density w_eta relative to mu_D satisfying w_eta>=exp(-10R), uniformly in its entire exterior eta, where R=4096r/3. This follows from minimum retained label size4, N2(Phi)<=R and |D|<=40.

Let g be any square-integrable function of all box links. For fixed eta outside D it becomes a function

\[
g_\eta(U_{D\cap\Lambda})
=g(U_{D\cap\Lambda},\eta_{\Lambda\setminus D}).
\]

In particular the predictor retains every observed link outside D; none is discarded or assumed Haar. DLR disintegration and the uniform lower likelihood yield

\[
\int|H-g|^2\,d\nu
\ge e^{-10R}\int\nu_{D^c}(d\eta)
\int\mu_D(dz)|H(z)-g_\eta(z)|^2
\ge e^{-10R}\,3k/4.
\]

The inner integral equals3k/4 plus the Haar norm squared of g_eta, by the conditional parity identity. Domination makes these integrals legitimate for every L2(nu) predictor. Taking the infimum over the full box reader proves

\[
\|Q_\Lambda H\|_{L^2(\nu)}
\ge\frac{\sqrt{3k}}2e^{-5R}.
\]

This is a bounded-neighborhood comparison against mu_D times the actual exterior marginal, not a product-Haar assertion about the whole source. Its constant does not depend on the number of observed exterior links.

## Actual generator and common remainder budget

Use the exact decomposition from the fixed-patch packet,

\[
A p/\kappa
=3p-\frac r3(4-p^2)
+\frac r6\sum_{s\sim p}h_{ps}-d_{tail},
\qquad\|d_{tail}\|_\infty\le T(r),
\]

\[
T(r)=\frac{a_0r\zeta}{1-\zeta},\quad
a_0=2048/3,\quad\zeta=262144r/27.
\]

This tail bounds the actual infinite interaction after its first coefficient, not a formal truncated dynamics. Terms from wholly internal neighboring plaquettes are box-measurable and disappear under Q_Lambda. Projection is L2-contractive, giving

\[
\|Q_\Lambda Ap\|/\kappa
\ge\frac{r\sqrt{3k}}{12}e^{-5R}-T(r).
\]

At r<=10^(-9), the previous exact budgets give5R<1/10 and T/r<1/24. Since k>=6 and sqrt(18)>21/5,

\[
\frac{\sqrt{3k}}{12}e^{-5R}
>\frac7{20}\frac9{10}=\frac{63}{200},
\qquad
\frac{63}{200}-\frac1{24}=\frac{41}{150}>\frac14.
\]

This proves the common positive lower bound for every nontrivial cubic box. Only p is acted on by A; no generator-domain regularity of a conditional projection is assumed.

For each box, the strong source derivative and the existing compressed-defect factorization give

\[
\lim_{t\downarrow0}\|Q_\Lambda P_t p\|/t
=\|Q_\Lambda Ap\|>\kappa r/4,
\]

\[
\lim_{t\downarrow0}t^{-2}
\langle p,(K_{\Lambda,2t}-K_{\Lambda,t}^2)p\rangle
>\kappa^2r^2/16.
\]

No explicit finite-time radius is constructed here.

## Exact checks and diagnostic failures

The checker freshly replays the fixed-patch receipt. Local edge membership, not a volume enumeration, tests sides2,3,4,8,1000 and10^12, two translations and all three coordinate-plane choices. It checks the k=8/6 classification, outside parity witnesses, cross-channel orthogonality witnesses and the uniform rational noncancellation constants. The all-size result is the written two-case geometry proof, not an extrapolation from those fixtures. L=1 is separately retained as the genuine constant-reader exception.

A rational conditional-law control has hidden z, observed x and exterior advice eta, all in {-1,1}, with density

\[
w_\eta(x,z)=1+z(x+\eta)/4\ge1/2.
\]

The actual reader mean is(x+eta)/4, not its Haar value0. Its centered residual norm squared is7/8. The checker tests625 arbitrary reader assignments on the four(x,eta) cells, including the exact minimizer, against the single local-likelihood variational bound. Thus exterior advice is retained while centering changes.

Appending N independent biased observed bits leaves this residual unchanged, while a whole-product Haar density floor decreases as2^(-N-1). Exact comparisons for several N illustrate why a whole-reader domination argument loses the uniform constant. These are diagnostic probability laws, not replacements for the SU2 vacuum.

## What this does not obstruct; next operation

Finite-volume Hamiltonians and their free-boundary semigroups still exist. The theorem rejects an exact invariant restriction of the actual infinite source, not the existence of autonomous finite-volume approximations. Its test plaquette sits at the boundary of each box; it is not a fixed bulk observable whose buffer grows along an exhaustion. No low-energy family, gap failure, physical clock or continuum no-go follows. Parent continuum/root gates and independent analytic review remain open.

**Next executable issue:** quantify compressed-memory error for fixed interior observables as their buffer grows, using the existing actual finite-box propagator comparison. Establish an explicit finite-horizon tolerance/buffer bound in the actual-state reader norm without identifying changing vacuum Hilbert measures. This will distinguish exact boundary nonclosure from controlled bulk approximate autonomy; a repetition of the existing full-semigroup convergence theorem alone is insufficient.

Contract: `research/kitaev/contracts/yang-mills-box-boundary-leakage.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_box_boundary_leakage.py`.
Receipt: `research/kitaev/results/yang-mills-box-boundary-leakage-v1.json`.

# Exterior magnetic leakage after restoring the full seven-link reader

## Question and disposition

Does retaining every function of the seven links of two adjacent plaquettes repair the dynamical failure of the two-trace reader?

**Written actual-source rejection at positive coupling:** fix coplanar adjacent plaquettes p,q0 in the bulk and their seven-link union S. Let Pi_S=E_nu[ . |U_S], Q_S=I-Pi_S for the actual thermodynamic vacuum. For fixed kappa>0 and

\[
0<r\le r_0:=1/10^9,
\qquad\|Q_S A p\|_{L^2(\nu)}>\kappa r/3.
\]

The input p is the fundamental trace of the first plaquette. The reader now retains all local link data, including relative orientation; the omitted channel is genuinely exterior. At r=0 this full local reader is dynamically invariant, so the positive-coupling result is distinct from the preceding electric/two-trace failure.

The proof controls the full actual interaction remainder and the actual weighted projection. It is not a first-order coefficient-only assertion. The stated subwindow is deliberately conservative and is not the full earlier coupling window. Independent analytic review remains open; this fixed-lattice source result supplies no continuum, physical-clock or gap obstruction.

## Issue-boundary conjecture and rivals

**Problem:** adding a missing internal orientation coordinate need not eliminate coupling to links outside the chosen patch.

**Conjecture:** the first magnetic drift sends the plaquette trace into eleven exterior orientation channels; their source-weighted distance from every seven-link function remains larger than the actual all-orders tail.

**Rivals:** assume orientation repair closes dynamics; replace the actual projection by Haar centering; substitute a Taylor drift for the actual one; use an uncontrolled O(r squared) to preserve a nonzero first coefficient.

**Risky consequences:** exactly twelve neighbors of p, only q0 wholly inside S; eleven orthogonal Haar channels conditionally centered against U_S; a local actual-density lower bound; an anchored all-orders drift error smaller than r/24. These are the declared tests and analytic obligations.

## Local geometry and canonical shared-link channels

Use p in the xy plane with corners (0,0,0),(1,0,0),(1,1,0),(0,1,0), and q0 immediately below it, sharing the x link at y=0. Each link of p belongs to three other elementary squares. Distinct elementary squares share at most one link, so p has twelve distinct link-sharing neighbors. Exactly one, q0, is contained in S. Let N_out be the remaining eleven neighbors and D the union of p and all its twelve neighbors. Then S is contained in D and |D|<=4+12*3=40.

For any neighbor s define the canonical invariant function

\[
h_{ps}:=-2\Gamma(p,s),\qquad
\Gamma(f,g)=\sum_e\nabla_e f\cdot\nabla_e g.
\]

The shared-link identity L(ps)=6ps+h_ps identifies this with the old relative-orientation function, choosing both loops to use the shared link in the same direction. Cyclic basepoint changes and edge inversion preserve the Casimir/Gamma identities. Its Haar norm squared is3/4. Define H=sum_(s in N_out) h_ps.

Each h_ps has center parity equal to the symmetric difference of the edge boundaries of p and s. Every exterior neighbor has an edge outside S, where this parity is odd. A Haar integration on that edge proves E_mu[H|U_S]=0. For distinct s,t, the product's center parity is the nonempty boundary difference of s and t, so the channels are Haar orthogonal. Thus

\[
\|H\|_{L^2(\mu_D)}^2=11\cdot3/4=33/4.
\]

These statements are reference-Haar facts, not claims that the actual weighted conditional mean of H vanishes.

## Actual conditional comparison, not Haar substitution

The actual retained interaction satisfies N2(Phi)<=R=4096r/3. Its labels have at least four links. On the at-most-forty-link set D, the conditional log-weight oscillation is at most |D|R/4<=10R, by the same local likelihood argument as the weighted-orientation packet. DLR marginalization therefore gives

\[
d\nu_D/d\mu_D\ge e^{-10R}.
\]

This is the actual marginal, not the free-boundary vacuum on D. For every square-integrable seven-link function g,

\[
\int|H-g(U_S)|^2\,d\nu
\ge e^{-10R}\left(33/4+\|g\|_{L^2(\mu_S)}^2\right).
\]

Infimizing over the entire reader gives

\[
\|Q_SH\|_{L^2(\nu)}\ge\frac{\sqrt{33}}2 e^{-5R}.
\]

This includes every internal orientation coordinate and every non-gauge-invariant link function as possible predictors. The input and its actual generator are gauge invariant; failure even in this larger reader rules out an internal gauge-invariant repair on the same patch.

## Actual generator and an all-orders remainder

Write Phi=r Phi1+Psi, where Phi1 has component s/6 on every elementary square. The Casimir-weighted Catalan majorant, starting at order two rather than three, gives

\[
N_2(\Psi)\le T(r):=\frac{a_0r\zeta}{1-\zeta},
\quad a_0=2048/3,\quad\zeta=262144r/27.
\]

This follows from Catalan(n-1)<=4^(n-1) and the geometric sum for n>=2. Exact retained-label restriction passes the finite-box tail bound to the global interaction: every finite collection of labels lies in a common box, and nonnegative anchored norm sums pass monotonically to the global bound. No new infinite-volume complex analyticity theorem is assumed.

For the tail drift beta_tail=2 sum gradient Psi, minimum label size4 gives ||beta_tail,e||<=T/4. The plaquette trace has four gradient blocks, each of norm at most1, so the actual scalar drift tail d_tail obeys ||d_tail||_infinity<=T.

The electric identity Lp=3p, the self-contraction Gamma(p,p)=4-p squared and Gamma(p,s)=-h_ps/2 give the exact actual-source decomposition

\[
A p/\kappa
=3p-\frac r3(4-p^2)
+\frac r6\sum_{s\sim p}h_{ps}-d_{tail}.
\]

All terms except the eleven exterior channels and d_tail are functions of U_S. Consequently

\[
\|Q_S A p\|/\kappa
\ge\frac{r\sqrt{33}}{12}e^{-5R}-T(r).
\]

The actual conditional expectation is used throughout; no unbounded generator acts on a conditional projection.

## Exact positive-coupling budget

At r0=1/10^9, the rational checker verifies r0<27/262144 and

\[
5R(r_0)<1/10,\qquad
\frac{a_0\zeta(r_0)}{1-\zeta(r_0)}<1/24.
\]

Both bounds extend monotonically to 0<r<=r0. Since sqrt(33)>5 and exp(-5R)>=1-5R>9/10, the leading residual is greater than3r/8 while T(r)<r/24. Their difference is greater than r/3. This proves the displayed actual generator leakage.

The existing cylinder core contains p. Hence the actual source semigroup satisfies

\[
\lim_{t\downarrow0}\|Q_SP_t p\|/t
=\|Q_SAp\|>\kappa r/3.
\]

The compressed memory-defect identity from the preceding packet also applies with Pi_S and input p; its quadratic small-t coefficient exceeds kappa squared r squared/9. No explicit uniform finite-time radius is asserted.

## Exact controls and strongest rival

The checker freshly replays the reader-dynamics receipt, enumerates the local cubic geometry and its eleven outside parity witnesses, checks all55 cross-channel parity obstructions, and regresses the canonical Gamma identity with direct first link derivatives. Rational Catalan/geometric-tail and density/noncancellation budgets are checked at the declared endpoint and selected interior parameters. The all-function harmonic analysis, actual DLR comparison and source operator-core statements remain written analytic inputs.

A deliberately bad quadratic correction d_bad(r)=r squared H/(6r0) cancels the entire exterior first-order term at r=r0 despite having formal order r squared. Its Haar norm already exceeds the certified supremum tail budget there, so it is excluded by the actual constructor. This locates the precise reason a nonzero formal first coefficient alone is insufficient. At r=0 the exact full reader closes and the magnetic residual vanishes; no positive r-independent leakage floor is claimed.

## Survivor and next issue

Resolved at written-proof scope: restoring all seven-link data does not close the actual dynamics on the stated positive-coupling subwindow. This is a fixed-patch statement, not yet a theorem that every finite patch fails at one common coupling. Nor does nonclosure obstruct the full quasilocal source theory, its source gap, or a history-bearing reduced model.

**Next executable issue:** determine whether the local resampling comparison yields a volume-independent boundary-leakage bound for every finite induced cubic box at a common positive coupling. Comparing an entire large-box marginal to Haar would lose the constant with volume; a successful argument must condition on the complement of a uniformly bounded boundary neighborhood instead. The previous exterior-augmented conditional comparison is available for this purpose. A repetition of the present seven-link fixture is not enough.

Contract: `research/kitaev/contracts/yang-mills-patch-leakage.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_patch_leakage.py`.
Receipt: `research/kitaev/results/yang-mills-patch-leakage-v1.json`.

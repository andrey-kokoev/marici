# Iteration 9 — close the anchored estimate by charging Casimir energy

## Question and disposition

Can iteration 8's support-cardinality loss be removed without a cutoff, a volume-dependent coupling window, or a replacement density?

**Yes for the actual finite-source log ground function at sufficiently small fixed r=lambda/kappa.** A Casimir-weighted Fourier norm and edge-resolved gradient estimate give a closed anchored bilinear bound. The resulting interaction fixed point converges uniformly over finite open boxes when0<=r<27/262144. It supplies an actual-source order-three-and-higher remainder estimate and conditional influence bounds.

**Still open in this turn:** the functional inequality converting those bounds into the required volume-uniform physical detector constant. `faithful-excitation-detection` is not closed by an influence estimate alone. No infinite-volume/continuum correlation theory, continuum scaling or official Yang–Mills target is constructed.

[Contract](contracts/yang-mills-anchored-casimir.v1.json). All previous source, quotient and vacuum choices remain unchanged. This is a small electric-dominant bare-parameter window, not a claimed weak-coupling continuum regime.

## Charge the derivatives before summing the overlaps

Use the compact-group Fourier conventions of iteration 8, but define

\[
W(f)=\sum_\pi(1+C_\pi)d_\pi
\|\widehat f(\pi)\|_{trace},\quad
C_\pi=\sum_e j_e(j_e+1).
\]

Write A0 for the unweighted Fourier norm and

\[
m_e(f)=\sum_\pi j_e d_\pi\|\widehat f(\pi)\|_{trace}.
\]

Since every nonzero spin is at least one half,

\[
\sum_e m_e(f)\le\frac23 W(f).
\]

This controls derivative activity, rather than counting every nominal support edge at full cost. The completed W space embeds in C1 at each finite graph. Fourier inversion, trace-class algebra estimates and unitary representation differentiation are the same imported harmonic analysis as before; no finite spin cutoff is assumed.

The physical mean-zero electric spectrum has C_pi>=3 by the previously proved Gauss/girth argument. Consequently

\[
W(L^{-1}h_c)\le\frac43\|h\|_{A^0}.
\]

Retain the edge-resolved estimate instead of replacing it by the product of total norms:

\[
\|\Gamma(f,g)\|_{A^0}\le3\sum_e m_e(f)m_e(g),
\]

\[
W(B(f,g))\le4\sum_e m_e(f)m_e(g),
\quad B(f,g)=L^{-1}\Gamma(f,g)_c.
\]

Centering deletes the constant Fourier block, not a factor-two triangle estimate. The physical inverse, not the kinematic3/4 eigenvalue, is used here. Individual derivatives leave the scalar invariant sector, but their contracted Gamma and the centered inverse preserve it.

## Closed anchored bound: the cardinality factor disappears

For specified connected-support interactions define

\[
N_t(\Phi)=\sup_e\sum_{A\ni e}t^{|A|}W(\Phi_A),\quad t\ge1.
\]

Each component is mean-zero and gauge invariant. Nonempty supports can be chosen as unions of connected elementary plaquettes. On a fixed box this is a finite direct sum of complete function spaces, so the interaction norm is complete. The function components themselves retain all Fourier modes. Their support labels need not be minimal or give a canonical decomposition.

Assign B(Phi_A,Psi_B) to A union B; it vanishes for disjoint edge supports. For an output anchored at e, split e in A or e in B. For the first half, use t raised to the union size <=t^|A|t^|B| and estimate

\[
4\sum_{A\ni e}t^{|A|}\sum_k m_k(\Phi_A)
\sum_{B\ni k}t^{|B|}m_k(\Psi_B).
\]

The inner sum is at most(2/3)N_t(Psi). Summing m_k(Phi_A), rather than merely counting k in A, costs at most(2/3)W(Phi_A). This half is bounded by16 N_t(Phi)N_t(Psi)/9. The other half has the same bound. Thus

\[
\boxed{N_t(B(\Phi,\Psi))\le
\frac{32}{9}N_t(\Phi)N_t(\Psi).}
\]

There is no cardinality norm on the right, no representation-frequency constant and no volume constant. This is a sharper estimate than iteration 8's coarse lift, not an assertion that its unclosed bound was sufficient.

## Actual interaction fixed point at a fixed small coupling

A plaquette trace has C_pi=3 in every Fourier block. The16 index-term bound gives W(p)<=64. Therefore the source interaction decomposition of S/6 satisfies

\[
N_t(S/6)\le\frac{128}{3}t^4,
\]

using at most four plaquettes per link. Choose t=2 and set a=2048/3 and K=32/9. The interaction map

\[
\Phi=r\Phi_1+B(\Phi,\Phi),\qquad
\Phi_1=\{p/6\}_{plaquettes}
\]

maps the radius R=2ar ball into itself and has Lipschitz constant at most2KR=4Kar. It is a strict contraction when

\[
\boxed{0\le r<\frac{27}{262144},\quad
R=\frac{4096}{3}r,\quad q=\frac{262144}{27}r<1.}
\]

All constants are independent of the number of plaquettes. Summing the components on each finite box gives a mean-zero W function u satisfying the actual centered log eigen-equation. The W norm controls C1; the equation and elliptic regularity justify the weak chain rule and bootstrap smoothness. Exponentiating gives a positive eigenfunction. By the uniqueness of the positive compact-source ground function, it is the actual Omega up to normalization, not a surrogate or an arbitrary solution of a formal series.

Gauge invariance, support preservation and positivity enter this identification exactly as in iterations 7–8. No interacting gap estimate is presumed. Boundary incidence is lower than the bulk upper bound used above.

The complex-bilinear map also constructs the analytic branch in the same disk as an interaction-valued series; the real nonnegative parameters identify the physical positive vacuum. This is a finite-box statement with uniform estimates, not yet a joint thermodynamic correlation construction.

## Uniform remainder, rather than fixed-box O(r cubed)

The coefficient recursion is dominated by the scalar quadratic equation X=ar+KX squared. Hence

\[
N_2(\Phi_n)\le\operatorname{Catalan}(n-1)
K^{n-1}a^n.
\]

The inequality Catalan(m)<=4^m gives the explicit tail estimate

\[
N_2\left(\sum_{n\ge3}r^n\Phi_n\right)
\le\frac{arq^2}{1-q}.
\]

The first two coefficients are those already computed from the actual operator. The normalized log-density tail differs from twice this interaction tail only by a constant. Therefore its conditional oscillation is at most four times the displayed bound, uniformly over finite boxes and conditioning configurations. This supplies the anchored remainder estimate missing in iteration 6; it does not follow from finite-order locality alone.

## Actual conditional influence, with a support weight that pays for the row sum

Write the actual normalized log density as2 sum_A Phi_A plus a constant. The single-link conditional log oscillation is at most4N_1(Phi)<=4R. For a change of conditioned link j, the log-likelihood/total-variation bound from iteration 6 gives

\[
c_{ej}\le2\sum_{A\ni e,j}W(\Phi_A).
\]

Summing over j not equal to e and using

\[
\sup_{n\ge1}(n-1)/2^n=1/4
\]

yields

\[
\sum_{j\ne e}c_{ej}\le\tfrac12N_2(\Phi)\le R/2.
\]

These estimates concern the actual Omega squared Haar measure, not exp(T2). At the interior point r=27/524288, q=1/2, R=9/128, the order-three tail bound is9/512 and the actual influence row is at most9/256. The numbers are deliberately conservative.

The full contraction window has R<9/64 and influence row<9/128. No conditional tensorization or spectral-gap conclusion is silently imported from that row bound. Its applicable functional-inequality constructor is the next explicit obligation.

## Verification, residual and next operation

The checker verifies the Casimir/edge-frequency inequalities on exact spin data, the overlap estimate with edge-resolved activity arrays, the support-weight inequality, the rational contraction constants, and Catalan/tail controls. These are exact finite regressions accompanying the all-spin proof, not numerical ground-state approximations. Existing source receipts and failed candidates remain retained.

**Remaining residual:** a checked volume-independent physical detection inequality. A promising executable route is to use the new Casimir-weighted interaction control to bound the Hessian of log rho and the weighted product-group curvature, then derive a Poincare inequality with its exact metric normalization. That derivation is not supplied merely by naming Bakry–Émery or a tensorization theorem.

`faithful-excitation-detection` and both root existence/gap outcomes remain open. No continuum scaling, nontrivial infinite-volume state or atomic Hamiltonian is selected.

Reproduce: `python research/kitaev/checkers/check_yang_mills_anchored_casimir.py`.
Receipt: `research/kitaev/results/yang-mills-anchored-casimir-v1.json`.

---
authors:
  - marici.Nima
date: 2026-08-18
---
# 672 — The Weighted Shared-Wall Exceptional Functional Has Rank One

## Hard-to-vary claim

The quadratic shared-wall tangencies of Entry 671 produce a finite
exceptional Stokes functional at \(\epsilon=0\).  On the three-dimensional
minimal source-syzygy space, the combined reduced-tangency evaluation has
rank one and kernel dimension two.

## Verified weighted normal form

For each repeated root of each shared-wall restriction, the wall-normal
derivative of \(K_E\) is nonzero.  Equivalently, the repeated quadratic
factor is coprime to the wall-normal derivative.  This holds for all three
shared walls at

\[
(x,y,z)=(2,3,4),(3,5,7),(5,7,9).
\]

Thus the local form is genuinely

\[
K_E=u\,n+v\,t^2+\text{higher},
\qquad u,v\ne0,
\]

where \(n=q_i\) and \(t\) is tangent to the wall.

## Exceptional Stokes order

Assign Newton weights

\[
\operatorname{wt}(t)=1,
\qquad
\operatorname{wt}(n)=\operatorname{wt}(K_E)=2.
\]

For a vector field logarithmic along both divisors,

\[
V(n)=\lambda n,
\qquad
V(t)=\beta t+\cdots,
\qquad
V(K_E)=\mu K_E.
\]

On the tangent axis the leading syzygy relation is

\[
2\beta=\mu.
\]

In the chart

\[
t=\delta,
\qquad
n=\delta^2s,
\]

the exceptional pullback of the primitive has order

\[
\boxed{\delta^{2\epsilon}}.
\]

It is therefore finite and generically nonzero at \(\epsilon=0\).  This is
the term absent from the transverse SNC model of Entry 670.

## Reduced tangency evaluation

Write

\[
K_E|_{q_i=0}=h_i^2.
\]

Vanishing of the exceptional coefficient requires \(\mu\) to vanish at the
reduced tangency points, so the correct condition is

\[
\mu\in(q_i,h_i),
\]

not the thicker condition \(\mu\in(q_i,K_E)\) used as a sufficient test in
Entry 669.

Imposing the reduced conditions for all three shared walls simultaneously
gives, on both exact syzygy fibers,

\[
\boxed{
\dim\ker E_{\rm exc}=2,
\qquad
\operatorname{rank}E_{\rm exc}=1.
}
\]

The calculation explicitly removes presentation kernels in the ideal
representations; the rank is a rank on the original three-dimensional
syzygy space.

## Consequence

The weighted conductor geometry supplies the first source-derived
rank-one detector in this branch.  It does not choose a unique primitive:
two primitive directions remain invisible.  But it canonically defines a
quotient line

\[
\operatorname{Der}^{(7)}(-\log D)/\ker E_{\rm exc}
\]

on the tested fibers.

This line is not yet identified with the physical algebraic line,
\(\mathcal Q\), or a coordinate in \(\mathcal T_7\).  Its significance is
more precise: the rank-one object is derived from the weighted
shared-wall/Cayley--Menger tangency, rather than fitted in the absolute
residue quotient.

## Updated frontier

Derive the quadratic factors \(h_i\) symbolically over the full kinematic
base and construct the exceptional evaluation map without fiber-specific
factor choices.  Then test whether its rank-one quotient has collision
divisor \(\mathcal Q=0\) or pairs with the physical wall cocycle
\(\rho_{\rm phys}\).

## Evidence

- `research/benincasa/physical_k_wall_singularity_audit.py`;
- `research/benincasa/physical_weighted_tangent_corner_stokes.py`;
- `research/benincasa/check_shared_wall_log_syzygy.rs`, schema v4;
- Entries 652 and 669--671.

## Outcome contract

~~~json
{
  "claim": "Weighted shared-wall tangency contributes no finite exceptional primitive functional at epsilon=0.",
  "status": "falsified",
  "weighted_local_model": "K_E=u*n+v*t^2",
  "normal_coefficient_nonzero": true,
  "exceptional_flux_order": "delta^(2*epsilon)",
  "physical_exceptional_order": 0,
  "minimal_syzygy_dimension": 3,
  "reduced_tangency_kernel_dimension": 2,
  "exceptional_evaluation_rank": 1,
  "canonical_primitive_selected": false,
  "canonical_quotient_line_candidate": true,
  "next_experiment": "Derive the reduced tangency factors and exceptional line symbolically over the kinematic base."
}
~~~

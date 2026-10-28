# Projective interval symmetry fixes the metric only up to a signed scale

## Scope and frozen test

Active SCC obligation: conditional continuum forward realization and metric-selection audit. The source is the existing selected-history interval construction, its containment order, and the supplied simultaneous projective endpoint action. This note does not derive that continuous action or a continuum limit from WG.

Test: do the inspected source constraints select the metric sign and absolute scale? Acceptance requires a source-selected normalization; rejection requires two inequivalent metric choices satisfying the same inspected constraints. Outcome: normalization selection is rejected even when interval containment is imposed as physical causal order. Sign selection is conditional on that extra causal interpretation, not on projective symmetry alone.

Inspected sources: `check_nnmhv_projective_interval_desitter_bridge.py`, `check_nnmhv_entanglement_crofton_bridge.py`, `check_nnmhv_interval_causal_diamond_bridge.py`, `check_nnmhv_mobius_wave_operator_bridge.py`, and `wg-interval-operation-bridge.md`.

## Classification theorem

On a connected chart U={(u,v):u<v}, consider smooth symmetric covariant two-tensors invariant under the diagonal local PSL(2,R) action wherever the endpoints stay in the chart. No positivity, entropy law or causal interpretation is assumed.

Translation invariance makes every component depend only on w=v-u. Positive dilation invariance then gives

    g = [A du^2 + C du dv + D dv^2]/w^2

for constants A,C,D. Here the mixed tensor component is g_uv=C/(2w^2).

The infinitesimal special-projective field is V=u^2 partial_u+v^2 partial_v. Its Lie derivative on the diagonal components is

    (L_V g)_uu = -2 A/w,
    (L_V g)_vv =  2 D/w,

while the mixed component has zero Lie derivative. Thus A=D=0. Conversely, for f(x)=(a x+b)/(c x+d),

    f'(u) f'(v)/(f(v)-f(u))^2 = 1/(v-u)^2,

where denominators are nonzero. Hence ALL invariant nondegenerate metrics are exactly

    g_C = C du dv/(v-u)^2,  C != 0.

Their determinant is -C^2/(4w^4), so both signs are Lorentzian. This is a local tensor classification, not an identification of a global spacetime or quantum theory.

## Curvature and the two local realizations

Use the Christoffel/Ricci convention of the old projective checker and choose negative norm for timelike vectors. The only nonzero Christoffel symbols are

    Gamma^u_uu = 2/w,    Gamma^v_vv = -2/w.

The diagonal Ricci components vanish, and Ric_uv=Ric_vu=2/w^2. Therefore

    scalar curvature = 8/C,
    sectional curvature K = 4/C,
    Ric = (4/C) g_C.

In dimension two these identities determine constant curvature. With x=(u+v)/2 and r=(v-u)/2>0,

    g_C = (C/4)(dx^2-dr^2)/r^2.

For C=4 ell^2, this is a local dS2 planar metric with time r. For C=-4 ell^2, it is a local AdS2 Poincare metric with time x and spatial coordinate r. The curvature radius ell is additional data. Both use the same projective action but DIFFERENT timelike cones. Merely reversing the overall sign is not a transport of the same physical causal interpretation. No global completion, boundary state or physical source law has been obtained.

## The causal-order discriminator

The interval-containment future cone is du<=0, dv>=0. In its interior du dv<0. Thus

    g_C(V,V)<0 for every interior containment-future V iff C>0.

The two one-sided extension edges are null for either sign; their combined interior is timelike only for C>0 in the fixed negative-timelike convention. Therefore requiring BOTH null families alone does not select a sign. Requiring their interval-containment combinations to represent physical causal propagation does select the dS sign. C<0 instead makes the interval-containment interior spacelike.

This is a conditional discrimination, not a claim that a combinatorial order has already been shown to be physical causality. A proposed common WG source may admit distinct observation/causal interpretations, but it cannot preserve this very same physical containment cone as timelike in both sign branches.

## Scale remains free even after imposing causality

C=4 and C=16 satisfy exactly the same projective invariance, Lorentzian signature, containment time orientation and unparameterized geodesic/connection conditions. Their scalar curvatures are respectively 2 and 1/2. Thus none of those conditions selects the original C=4. The shared Christoffel connection is itself blind to constant metric rescaling.

The entropy checker supplies S=(c/3) log(w/epsilon) and then explicitly chooses g=(12/c) partial_u partial_v S du dv. This sets C=4 by normalization; the code does not derive the factor 12/c from native WG operations. A positive entropy Hessian plus a stipulated positive metric coefficient would select the positive sign but still requires a physical identification and scale rule.

The discrete mixed-difference operator is also not a normalization proof. For the continuum metric above, Box_g=(4w^2/C) partial_u partial_v. The unweighted discrete incidence difference supplies neither this position-dependent factor nor a physical length calibration without an additional discretization/realization law.

## Disposition and next obligation

Completed: all invariant local metrics classified, their exact curvature computed, causal sign discrimination stated, and a same-causality scale counterexample supplied. The bounded `projective-metric-selection` test is REJECTED as a source-selection claim for the inspected constraints, not inconclusive. It does not refute the existence of a future additional selector or WG-G1.

The interval-route synthesis cannot consume a rejected metric-selection task as a constructed witness. Two separate repairs would be needed: an independently sourced scale rule, and, for both AdS/dS signs, explicit distinct causal realizations or a reason to relax preservation of the containment order. Native-law selection remains independently open.

No proof of metric emergence from WG, full AdS/dS codomains, continuum convergence, Einstein field equations or holographic duality is asserted.

## Verification

`checkers/check_projective_interval_metric_selection.py` uses exact rational arithmetic for independent Mobius pullbacks, Lie-derivative coefficients, curvature contraction, causal sign controls and the scale counterexample. The all-parameter classification is the algebraic argument above, not an extrapolation of finite tests. Results: `results/projective-interval-metric-selection.json`.

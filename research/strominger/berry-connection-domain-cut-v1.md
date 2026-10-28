# Continuous Berry connection through the retained-domain cut

## Domain and conventions

Extend the earlier four-projector example to the existing CP1 eigenline construction. On the overlap of north and south charts, use z=r exp(i phi), r>0, with normalized frames

    u_N=(1,r exp(i phi))/sqrt(1+r^2),
    u_S=(exp(-i phi),r)/sqrt(1+r^2).

The north chart excludes the south pole; the south chart excludes the north pole. The displayed polar formulas describe their overlap. The frame relation is u_S=exp(-i phi)u_N. Both frames define the same projector. Use A=-i u†du and phase exp(i integral A); changing the phase convention conjugates the corresponding phases.

The symbolic calculation yields

    A_N = r^2/(1+r^2) dphi,
    A_S = -1/(1+r^2) dphi,
    F = 2r/(1+r^2)^2 dr wedge dphi.

The connection difference is the transition contribution -dphi. Its winding is -1. Independently computing -i Tr(P[d_r P,d_phi P]) gives the same curvature. The curvature integral over the sphere is 2pi under this convention.

For every fixed radius r, the circle integral is 2pi r^2/(1+r^2). At the equator the phase is -1. These are exact symbolic identities and integrals, not a finite sample of parameter values.

## Same tower and triangle

Retain fourteen symbolic fields: both frames, the transition, both connection components, the curvature component and all four projector entries. Coordinates and their real/positive assumptions remain attached to the symbolic expressions; the chart meanings are fixed above, not supplied by the FCC chart coordinates.

Feed the field table through the same two incoming-family promotions, retained cone and decorated tetrahedral representation. For both endpoint policies and two distinct role charts, extract the triangle and reconstruct every symbolic field exactly. Recompute the transition law, curvature and equatorial loop phase from the recovered fields.

No new promotion or cone rule is introduced. The FCC-cell coordinates represent the retained package; they are not identified with the CP1 base coordinates.

## Equal projectors, different holonomy

On a separate annular domain, add alpha dphi to both local connection forms. The projector and curvature are unchanged; the closed-loop phase changes by exp(2pi i alpha). For alpha=1/2 the relative phase is -1. The enriched packets remain distinct and recover this difference after promotion and extraction.

This is the prior flat-central-twist warning made explicit. It is an annular example, not a claim that the simply connected sphere supports a nontrivial flat twist. A projector plus its canonical Berry prescription determines the canonical curvature; a projector alone does not determine every separately supplied connection.

Thus retained transition/connection data, not just endpoint rays or a scalar curvature value, are necessary for this broader domain. The full packet passes where a projector-only readout cannot.

## Disposition

The initial Berry branch is completed at the specified rank-one CP1/annular scope: a continuous parameter-family domain with transition, curvature and loop information passes the same retained representation. Arbitrary Berry families and non-Abelian degenerate transport are not covered by this result.

All three initial branches now have scoped instances. The governing conjecture is still open: their common generic constructor points toward a representation theorem under explicit domain-retention hypotheses, not an inference that three examples cover all laws.

Verification: `uv run --with sympy python research/strominger/checkers/check_berry_connection_domain_cut.py`, exit zero, execution `structured_command_execution:e_42200_1792521175065943100_42`. Receipt: `research/strominger/results/berry-connection-domain-cut/verification.json`. No fresh Agda compilation or physical experiment.

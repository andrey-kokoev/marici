# History6 — generic full-component top bridge

Freshly read the full quotient checker, owning generalized-R evaluator and work-net (pins v38). Extend the full-component comparison from three fixtures to a generic rational identity; do not invent a lower-degree map.

## Generic incidence open

On <12> != 0, translate x2 to zero and change the spinor frame so Z1=(1,0,0,0), Z2=(0,1,0,0). Z3,Z5,Z6,Z8 have sixteen independent bosonic components. A theta translation sets theta2=0, hence chi1=chi2=0. This does not constrain the physical Grassmann data: source theta differences are invariant under translation, and the Schur residuals annihilate the induced lambda-linear shifts. Chi3,chi5,chi6,chi8 remain arbitrary odd linear forms in each SU(4) sector; inactive chi4,chi7 drop out of the source circuits, rather than being set to chosen values.

Let x3 and theta3 be reconstructed from line(23), and x6 and theta6 from line(56). Incidence <8|x8=-mu8^T yields

    ut = mu8^T adj(x6),
    xi = (-mu8^T - <8|x6) adj(x6),
    L = xi*(-x3)*adj(x3-x6),
    K = xi*(-x6)*adj(x6-x3).

Also ut+xi=-<8|det(x6). The outer theta8 dependence therefore reduces to chi8, eliminating chi7. The actual source fermionic rows are

    q_outer = ut*theta6 - det(x6)*chi8,
    q_inner = L*theta6 + K*theta3.

The checker directly implements the owning evaluator's five denominator factors and angle numerators for both R factors, including the unupdated inner upper endpoint lambda6.

## Full polynomial and prefactor proof

Choose active bosonic Schur pivot columns (1,2,3,5), with residual columns (6,8). Build the two residual chi forms symbolically. Their wedge has six coefficients in the four active odd generators. Every source coefficient equals the corresponding Schur coefficient times one derived nonzero rational scale. The source outer*transported-inner prefactor times scale^4 equals the actual bosonized Schur prefactor identically.

Combining this with the independently normalized universal Berezin identity from the preceding receipt proves the complete mixed four-sector polynomial equality on this incidence open, not just eta23 or a family of numerical samples. Substitution of arbitrary odd linear forms restores every component in any allowed supermomentum quotient basis. The same generic calculation proves

    prefactor_unupdated / prefactor_transported = c6,
    F0 = c6*Ft,   Ft-F0 = (1-c6)*Ft,

with c6 the intrinsic bracket cross ratio. Both unupdated and difference bosonized top prefactors agree symbolically after the same scale^4 conversion. All raw denominator factors and Schur patch requirements are retained in the receipt; reduced cancellations do not enlarge the source localization.

## Scope and next gate

The full-component **top** bridge is now a generic normalized-incidence rational identity. This does not admit an ordinary unit canonical seed for F0 or assert a global covering/orientation theorem. It still evaluates a degree-eight density at the reference plane and extracts a degree-eight quotient superfunction.

No degree-seven/six boundary Berezin/delta measure or direction-retaining physical supercomponent codomain has been constructed. The actual differential boundary/blowup witnesses, positive-endpoint split residuals, extra meromorphic pole and unavailable ordinary blowdown seven-form remain as previously recorded. A top identity cannot assign a new degree to them.

Next executable task: read the owning Grassmannian delta-integral and boundary prescription, then formulate a degree-preserving boundary extraction with its actual normal/delta measure and retained exceptional direction. Do not infer that operator solely from the newly generic top equality.

Evidence: `checkers/check_history6_generic_top_bridge.py`, `results/history6_generic_top_bridge.json`. Attached as precursor evidence only; scientific node verdicts unchanged. Successor pins v39 and structural net/SCC validation remain distinct from the symbolic proof.

# Independent UV normalization is the missing selector datum (WP62, move 3/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Let finite RG transport be locally represented by an invertible map
(x_{IR}=Ax_{UV}). A UV boundary law (Bx_{UV}=b) pushes forward to

\[
BA^{-1}x_{IR}=b.
\]

If (B) has rank one, this selects a codimension-one physical family. Thus
transport plus an independently derived boundary law can be a selector even
though transport alone cannot.

The normalization (b) is decisive. The exact checker exhibits two hostile
IR points. A single frozen (b) admits one and excludes the other. If (b) is
recomputed from each IR point, both pass identically: the rule becomes
circular and predicts nothing.

The declared source supplies neither (B) nor an independently frozen (b).
It says UV physics may determine angles, but does not derive the boundary
equation or vacuum law. The minimal added structure is therefore exact: one
quotient-level source equation plus a normalization fixed independently of
the IR fit and a typed UV/threshold realization.

Verification:
`uv run --with sympy python research/flavor/checkers/wp62_uv_boundary_normalization_gate.py`.

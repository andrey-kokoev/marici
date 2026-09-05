# Native residual promotion gate

## Question

Can residual feedback remain a child-tower operation while parent re-entry is made impossible without a separately supplied authority object?

## Claim boundary

The module enforces an explicit authority argument at the Agda type level. It does not create, authenticate, or admit authority; the owning external surface must supply the authority type, its inhabitant, and the promotion map.

## Construction

`ResidualPromotion.agda` separates `ChildTower` from `ParentTower`. A `PromotionGate` contains an opaque `Authority` type and a map

\[
\mathsf{Authority}\to\mathsf{ChildState}\to\mathsf{ParentState}.
\]

The only exported re-entry combinator requires both the gate and an inhabitant of that authority type. Ordinary child residual steps have no parent codomain.

## Strongest falsification attempt

`negative/UnauthorizedPromotion.agda` applies parent re-entry with only a gate and child state. Agda rejects the term because the omitted authority leaves a function from `Authority` to `ParentState`, which cannot inhabit `ParentState`.

## Disposition

The child-to-parent promotion gate is natively enforced at the type level. This establishes dependency on explicit authority, not the provenance or legitimacy of any supplied token.

## Verification

- `research/voevodsky/agda/ResidualPromotion.agda`
- `research/voevodsky/agda/negative/UnauthorizedPromotion.agda`
- `research/voevodsky/results/cubical_agda_residual_promotion.json`

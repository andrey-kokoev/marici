# Concrete Cartier normal-symbol calculation

## Question

Can the one-normal block distinguish framed conormal normalization from the zero obtained by restricting a raw normal multiplier?

## Claim boundary

`agda/CartierNormalSymbol.agda` uses integer coefficient arrays indexed by t-degree and x-degree. These are coefficientwise formal series, not an assertion of convergence or of finite support. Multiplication by t and x is defined by shifts with zero padding; their commutation is proved on every coefficient. This is a concrete monomial-action model, not a general formal-power-series ring library.

Separate degree types H1 and P0 carry the normal differential d(h a)=p(tx a). `connecting` extracts the x-degree-one coefficient of that boundary. `connectingFormula` proves beta_x(a)=t times the x=0 restriction of a. Lift independence follows for any two arrays with the same x=0 restriction. `connectingHasNoConstant` proves the image has t-order at least one. `TConormal` retains the first-symbol target; its labelled t-frame evaluation is distinct from ordinary restriction. `framedEvaluation` gives the coefficient a(0,0); `unitSymbol` gives integer one. Representative independence is proved for equal constant coefficients.

The contrasting `rawRestrictionZero` gives zero on every t-coefficient after restricting tx a to x=0. `rawUnitRestriction` instantiates the unit input. Separate degree types K1 and K0 model K_x with d=x and H=t. `nullDegreeZero` and `nullDegreeOne` prove the two nonzero component identities of dH+Hd=tx id. The other compositions are zero by the two-term degree range. No inverses or division operations were introduced.

Scope limits: no full additive chain-complex package, derived-functor implementation, localized source-ring comparison, unframed line trivialization, arbitrary spectator coefficient ring, ordered multi-normal tensor theorem, analytic pole residue, or spatial Gysin assembly is formalized. Integer polynomial coefficient arrays satisfy the universal array equations, but no polynomial embedding or identification with B[t,x,(1+tx)^-1] is claimed. The source packet's global geometric interpretation remains separate.

## Disposition

Agda 2.8.0.1 with Cubical 0.9 accepted the module on the first targeted run, exit 0, no warnings, retaining --safe --cubical --guardedness. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/CartierNormalSymbol.agda"
```

Operator authorized shell Agda fallback. File writes used filesystem MCP. New owned files: this packet and its module. No existing analytic or comparison module edited, no aggregate rebuild or installation, no Git operations, commit, or push. The next source-level comparison must retain filtration, connecting degree and normal-frame metadata; this calculation does not construct that missing spatial natural transformation.

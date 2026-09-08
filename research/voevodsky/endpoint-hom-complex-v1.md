# Endpoint Hom complex and relative class

## Active objective

Formalize one actual source/target Hom complex and its boundary restriction, including prescribed connector cochains; prove differential/composition signs and compute its relative class.

## Chosen actual candidate

The formulas come from research/chatgpt/endpoint-boundary-restriction/endpoint_boundary_restriction.md, Sections 1–4. P is the two-variable Koszul endpoint hull, B its subcomplex in degrees one and zero, and C the two-term localized collar. These are a specified coefficient candidate, not the entire physical Q target. R=Z[x1,x5,X,U], L=R[U^-1], y=X/U is the intended realization.

`agda/EndpointHomComplex.agda` formalizes the displayed coordinate complexes uniformly for two commutative rings R,L, a map preserving zero/one/addition/negation/multiplication, regular x1,x5, and localized y. Distinct regular and localized types keep k/n coefficients regular and p coefficients localized. The actual polynomial/localization rings are NOT constructed or instantiated in this module. The theorem applies when that canonical realization is supplied; it does not assume that the regular-to-localized map is surjective.

## Checked construction

- Source boundaries and their square-zero law.
- Target boundary; complete nonzero Hom module coordinates in degrees -3,-2,-1,0.
- Actual Hom differentials and both nontrivial square-zero laws.
- Endpoint restriction to B, including the augmentation-induced higher connector terms; restriction chain law and boundary square-zero.
- Odd-degree differential sign for degree -1.
- Actual candidate f(e)=p and its primitive s(e)=n: d(s)=1, r(s)=0.
- Connector pair h=(h0,h2) remains an explicit input, not a zero default.

The additive coset type W is presented by relations v ~ v+y*iota(A)+iota(B), with set truncation. It is NOT the quotient by an L-ideal. The computed representative is

    I(f,h) = [f + iota(x1)*h0 - iota(x5)*h2].

For the unit attachment, `unitRelativeClass` proves I(1,h)=[iota(x1)*h0-iota(x5)*h2]. `zeroConnectorClass` proves the explicitly chosen zero-connector control vanishes. This control is not the physical choice of connectors.

`relativeBoundaryInvariance` proves invariance under (f,h) -> (f+d(s),h+r(s)). `higherConnectorInvariance` proves invariance under higher endpoint changes. `primitiveClassZero` proves a framed primitive has zero class. `fillFromDecomposition` constructs a framed primitive from a supplied equation f+x1*h0-x5*h2=y*iota(A)+iota(B). This is a constructive sufficient zero test, not an implemented Laurent-normal-form decision algorithm or a proved converse from equality in the HIT quotient.

`agda/HomComplexSigns.agda` proves the universal expanded composition sign identity

    a - (-1)^(p+q)c = (a - (-1)^p b) + (-1)^p(b - (-1)^q c)

and the middle-term cancellation for d_Hom squared, for all four parity cases over an arbitrary commutative coefficient ring. Here a=d_N g f, b=g d_M f, c=g f d_L. Operator factors are never commuted. These are pointwise expanded sign identities, not a complete degree-indexed DG-category implementation; additivity and typed composition across all homogeneous degrees still need wiring for that broader theorem.

## Verification

Both modules passed Agda 2.8.0.1 with Cubical 0.9, --safe --cubical --guardedness, exit0 without warnings. No holes or postulates. EndpointHomComplex imports HomComplexSigns; repeated targeted checks after adding source boundaries, relative invariance, and unit computations passed.

    pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/EndpointHomComplex.agda"

## Remaining objective gates

1. Instantiate the coefficient parameters with the actual polynomial ring and its U-localization, including a verified Laurent normal form for W. No nonzero residue is certified for the uninstantiated generic coefficient input.
2. Supply the independently prescribed physical connector cochains and the comparison identifying this candidate with the required physical restriction. The source packet explicitly says these are absent; setting them to zero would manufacture the answer.
3. If full general DG composition rather than its checked expanded sign law is required, wire the degree-indexed additive composition into the Hom implementation. Do not claim this is already done.

Thus the coordinate Hom calculation and relative invariant are checked, but the full physical relative class and all parts of the original objective are not closed. No analytic evaluator or earlier module was edited. No Git operation, commit, push, installation or aggregate rebuild. New owned artifacts: the two Agda modules and this packet.

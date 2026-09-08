# Signed Cech blocks, coefficient trace and change of coefficients

## Question

Formalize the Cech differential, trace and geometric base-change theorem for the explicit two-chart Rees calculation.

## Claim boundary

`agda/ReesCechBlocks.agda` implements the algebraic block calculation over an arbitrary Cubical commutative ring R. It imports the universal monomial classification. The X-only block differential is -id, the u-only block is id, and the common block differential is (a,b) -> b-a. The degree-one differential is zero. The homotopies are respectively -id, id and c -> (0,c). The coefficient traces are zero on single-chart blocks and (a,b) -> a on the common block; inclusions are zero or diagonal.

Checked identities: d^2=0; dH=id; Hd+include(trace)=id in degree zero; d(include)=0; trace(H)=0; and trace(include)=id for the common block. Thus single-chart blocks contract and common blocks retain one coefficient. These are actual ring identities proved with Cubical's commutative-ring solver, not assumed contraction fields.

`CoefficientNaturality` proves commutation of d,H,trace,include with every supplied additive coefficient map preserving zero, addition and negation. This applies in particular to underlying additive maps of ring homomorphisms; it is NOT a derived tensor or geometric base-change theorem. `Families` assembles the differential and contraction for arbitrary products of typed coefficient blocks. It is not silently identified with a polynomial direct sum.

The blockwise trace is only a coefficient-linear projection in this model. It is NOT asserted S-linear for S=k[X,u], since multiplying by a base monomial can move between block kinds. The geometric trace requires an S-linear quasi-isomorphism roof and its derived inverse, rather than promoting this projection.

## Disposition and exact unfinished request

Agda 2.8.0.1/Cubical 0.9 targeted run passed without warnings, exit0, retaining --safe --cubical --guardedness. A qualified unary-negation projection typo was corrected; both the block module and its subsequent family assembly reran successfully. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ReesCechBlocks.agda"
```

The geometric base-change theorem remains UNFORMALIZED. The source ring/sheaf Cech object and its comparison with these coefficient blocks have not been defined here. A bounded search in research/voevodsky/agda found no existing Blowup, blowup, Scheme, DerivedPullback or ProperBaseChange declaration/use. This is not a claim that the external Cubical library has no algebraic geometry; its filesystem source read was refused as outside the admitted root.

First missing implementation: a formal finite-support S-module Cech model of the two charts with their line transition, plus the S-linear map from S. Acceptance requires identifying its geometric derived pushforward, constructing the trace as a derived inverse, and proving comparison with derived Cartier pullback (retaining excess Tor at the centre). The additive coefficient-change square above is explicitly not accepted as a substitute. No geometric theorem has been encoded as an assumed field to claim completion. This is a partial implementation of the operator request.

Operator-authorized shell fallback was used only for Agda checks; file operations used filesystem MCP. New owned files: this packet and its module. No earlier module or analytic interface changed. No installation, aggregate rebuild, Git operation, commit or push.

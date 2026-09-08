# Two-chart Rees dualizing monomials

## Question

Can the explicit two-chart monomial cover and common-section parametrization be formalized without another abstract comparison interface?

## Claim boundary

`agda/ReesTwoChartMonomials.agda` models exponent descriptors of X^a t^b e_X, a nonnegative and b integral. A recursive classifier proves for every nonnegative b=n either n=a+gap (X-chart only) or a=n+k+1 (both charts). Negative b=-1-j has the u-chart descriptor u^a s^(a+j) e_u. `coverEveryMonomial` covers all descriptors without a degree cutoff.

Base monomial X^k u^n is represented by X^(n+k+1)t^n e_X. `reconstructCommon` reconstructs every descriptor with the common-section equation, and `commonBaseExponentUnique` proves uniqueness of k for fixed a,n by cancellation. The unit representative is X e_X; positive t^m e_X without its compensating X power is classified as X-chart only, whereas X^(m+1)t^m e_X represents the retained base monomial u^m.

Chart membership is encoded by these source-supplied exponent equations. No ring-of-sections semantics or derivation of the blowup transition from geometry is formalized. The negative-coordinate transition is a descriptor assignment, not an additional Laurent-ring theorem. This module does NOT yet assemble the integer Cech coefficient blocks, prove their differential exactness, construct an S-linear trace roof, or prove duality/base change. It establishes the bounded monomial combinatorics required by that calculation, not the complete proper trace. No missing logarithmic branch-selected excess map is supplied.

## Disposition

Passed Agda 2.8.0.1/Cubical 0.9 with --safe --cubical --guardedness, exit 0, no warnings, after repairing a parse error caused by using the reserved word overlap as a constructor name. The uniqueness extension was checked in a further successful run. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ReesTwoChartMonomials.agda"
```

Operator-authorized Agda shell fallback only. File writes used filesystem MCP. New owned files are this packet and its module. Analytic and prior comparison interfaces unchanged. No aggregate rebuild, dependency installation, Git operation, commit, or push.

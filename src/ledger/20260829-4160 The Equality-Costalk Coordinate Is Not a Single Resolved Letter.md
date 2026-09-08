# 4160 — The Equality-Costalk Coordinate Is Not a Single Resolved Letter

## Claim under test

Entry 4156 observed, on the one-parameter sample path
[
x=y,qquad z=x+2,
]
that the terminal structural Smith valuation obeyed
[
v_2(d_{mathrm{term}})=7+5v_2(x+1).
]

The hostile question was whether (x+1) is an intrinsic equality-costalk coordinate or only the restriction of a multivariate function to that path.

## Frozen computation

The source-fixed integral presentation of Entry 4147 was retained without renormalization:

- fixed denominator (2) on every de Rham row;
- multiplication rows retain source units;
- (K)-depth (3);
- labelled denominator depth (2);
- ambient degree (14);
- structural residual matrix size (14422	imes2278).

Only (z) was varied while (x=y) was held fixed.

## Results

The depth-(26) two-adic census gives:

| point ((x,y,z)) | terminal valuations |
|---|---|
| ((3,3,5)) | ((8,17)) |
| ((3,3,7)) | ((8,22)) |
| ((3,3,9)) | ((8,12)) |
| ((7,7,9)) | ((8,22)) |
| ((7,7,11)) | (8) detected; the second class lies beyond depth (26) |
| ((7,7,13)) | ((8,12)) |

At ((7,7,11)), the characteristic-zero rank remains (2194), while depth (26) detects rank (2193). Thus the unseen class is not a new free summand.

The first hostile point already falsifies the (x+1)-only law:
[
(3,3,5)mapsto17,qquad
(3,3,7)mapsto22,
]
although (x+1) is unchanged.

A second candidate,
[
7+5v_2!left(\frac{(x+1)(z-x)}2ight),
]
is also falsified:
[
(3,3,9)mapsto12,qquad
(7,7,13)mapsto12.
]

## Narrow conclusion

The spacing by increments of five survives, but the coordinate proposed in Entry 4156 does not.

What survives is:

1. one terminal class has constant valuation (8);
2. the second terminal class has a source-dependent valuation in the progression
   [
   12,17,22,ldots;
   ]
3. neither (x+1), (z-x), nor their product controls it globally on (x=y);
4. the path (z=x+2) collapsed a multivariate terminal function to (x+1).

Therefore Entry 4156 remains valid as a fiberwise barcode census and truncation warning, but its proposed fifth-order equality coordinate is withdrawn.

## Next falsifier

Do not fit another scalar from point valuations.

Preserve the fixed mod-(2) pivot schedule and construct the terminal mixed-Rees presentation before specializing ((x,y,z)). Extract its first two Fitting ideals in the local parameter ring. Only a source-derived generator of those ideals may be called the equality-costalk coordinate.
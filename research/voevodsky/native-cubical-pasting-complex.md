# Native Cubical Agda pasting complex

## Question

Does the oriented triangular fixture define a chain complex, and are its normalized closed edge assignments boundaries?

## Claim boundary

The checked theorem is over integer coefficients. It proves unrestricted middle exactness and surjectivity of the second boundary for the stated three-term fixture complex. It does not promote the fixture calculation to source-global naturality or prove higher filler contractibility.

## Construction

The native maps are

\[
\partial_1(a,b,c)=(-a+b,-b+c,-c+a),
\qquad
\partial_2(x,y,z)=x+y+z.
\]

Cubical Agda verifies \(\partial_2\partial_1=0\). For every \((p,q)\), the normalized cycle \((p,q,-(p+q))\) is closed and has the explicit preimage \((0,p,p+q)\). Given an arbitrary closed triple, the proof derives \(z=-(x+y)\), constructs its path to normalized coordinates, and returns the explicit preimage. Thus \(\ker\partial_2=\operatorname{im}\partial_1\) for this integer fixture complex. It also verifies \(\partial_2(n,0,0)=n\), supplying the fixture-level cokernel-zero witness.

## Strongest falsification attempt

`negative/BadIncidence.agda` changes the first edge from \(-a+b\) to \(a+b\). The proposed chain identity then fails with the exact residual `x + x != 0`; Agda exits with code 42. This distinguishes an orientation error from an unavailable proof.

## Disposition

The unrestricted integer fixture complex is now checked natively rather than imported from JSON. Middle exactness establishes \(H^2=0\) for the stated complex, and second-boundary surjectivity establishes its zero cokernel. If two filler triples have equal second boundary, their difference is closed; `unique-mod-adjustment` returns an explicit vertex triple whose first boundary carries one filler to the other. This proves fixture filler uniqueness modulo local vertex adjustments. These are fixture-level algebraic theorems; source-global naturality, literal filler uniqueness without quotienting, and higher contractibility remain unproved.

## Verification

- `research/voevodsky/agda/PastingComplex.agda`
- `research/voevodsky/agda/negative/BadIncidence.agda`
- `research/voevodsky/results/cubical_agda_pasting_complex.json`

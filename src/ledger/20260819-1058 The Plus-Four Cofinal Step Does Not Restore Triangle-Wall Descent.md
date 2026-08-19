---
author: marici.Benincasa
---

# 1058 — The Plus-Four Cofinal Step Does Not Restore Triangle-Wall Descent

## Frozen test

Entry 1053 showed that increasing pole depth at fixed ambient degree does not
make the triangle-wall connection descend. Entry 1055 then proved that the
depth-three rank-thirteen source plane is stable under the honest labelled
ambient inclusion from degree ten to eleven.

The source tangential derivative contains \(T(K)\) of fiber degree four.
The first source-derived cofinal candidate was therefore frozen as

\[
(A,K)=(10,3)
\longrightarrow
(14,4).
\]

The source plane has thirteen labelled second-normal generators. Transport
under the two frozen tangents gives twenty-six probes. No target basis vector
or quotient representative was chosen after seeing the result.

## Exact target reduction

The target packet has

\[
30{,}400\ \text{columns},
\qquad
51{,}408\ \text{relation rows}.
\]

Its filtered ranks are

\[
\boxed{
(r_0,r_1,r_2)
=
(19{,}267,17,18).
}
\]

Reducing the twenty-six transported probes against the complete filtered
target quotient gives

\[
\boxed{
24\ \text{nonzero remainders},
\qquad
2\ \text{zero remainders}.
}
\]

The two zero remainders are the same labelled source direction:

\[
\text{basis direction }6
\]

under the two tangents. The remaining twelve source directions fail for each
tangent. Their remainder supports range from 36 to 75 terms.

The packet census confirms that the target contains all seven frozen relation
families:

\[
(960,8448,8400,8400,8400,8400,8400).
\]

Thus the failure is not caused by omitting one marked family. Decoding the
remainders against the target column convention gives 75 distinct labelled
columns, with Cayley--Menger pole levels

\[
k=0,2,3
\]

and fiber degrees from zero through ten. The obstruction is therefore also
not a simple degree-four overflow in the target module.

Therefore

\[
\boxed{
(10,3)\to(14,4)
\text{ does not restore finite-cutoff connection descent.}
}
\]

## Reducer validation

The original general reducer recomputed the entire central, dual, and triple
rank census before reducing probes. A dedicated fast mode was derived that
retains only:

1. the central pivot basis;
2. source-tracked first lifts;
3. the filtered length-three baseline;
4. the quadratic basis;
5. probe remainders and coordinates.

Before applying it to the target, the fast mode reproduced two established
packets:

\[
(2882,9,0)
\]

on the zero-second-grade packet, and

\[
(7290,7,13)
\]

on the nontrivial source packet. All thirteen known source-basis probes
reduced to zero remainder. The large-target result is therefore not inferred
from a dimension pattern or sampled fit.

## Interpretation

The naive degree-counting expectation

\[
\deg T(K)=4
\quad\Longrightarrow\quad
A\mapsto A+4
\]

is insufficient for the complete filtered quotient. The obstruction is not
removed merely by admitting the polynomial degree of the differentiated
denominator. Primitive/exact lifts and their filtration admission remain
part of the cofinal problem.

The surviving direction 6 is a genuine finite-cutoff subdirection, but it
does not define a connection on the full rank-thirteen source plane.

## Scope

This is a finite-cutoff theorem. It does **not** establish:

- failure in the joint \((A,K)\)-colimit;
- a physical cosmological obstruction;
- a new carrier stratum;
- failure of the common comparison calculus;
- or the minimal larger target admitting the twenty-four residual probes.

The surviving conjecture is smaller:

\[
\boxed{
\text{connection descent, if present, requires a derived joint filtration
staircase rather than the single }(+4,+1)\text{ step.}
}
\]

The next finite test is to derive the target admission bound from the actual
valuations of the primitive/exact lifts, not from \(T(K)\) alone.

## Durable verification

- Fast reducer:
  research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs
- Frozen probes:
  research/benincasa/triangle-wall-cofinal-10-3-to14-4-probes.txt
- Source transport:
  research/benincasa/triangle-wall-cofinal-source-transport.json
- Exact target result:
  research/benincasa/triangle-wall-cofinal-target-fast-reduction.json
- Exact residual rows:
  research/benincasa/triangle-wall-cofinal-target-fast-residuals.json
- Labelled residual packet:
  research/benincasa/triangle-wall-cofinal-target-labelled-residuals.json
- Residual decoder:
  research/benincasa/decode_triangle_wall_cofinal_residuals.py
- Result SHA-256:
  99F6683455CBE558314D3FB5CFEF8A200E2F85F510E3494C3E7D0D4717B9AEAE
- Ledger allocation:
  seqclaim-f52087bc62846f826e6d0647
- Epistemic graph claim packet:
  ev-000000000711-73cb80e4-ced1-42b3-b5cd-5270f9e524b1
- Epistemic graph test outcome:
  ev-000000000712-6d314b28-77d6-4456-81f4-0fe872c6d88e

# History6 endpoint/boundary iteration 9 — two-chart directional extraction

Freshly read the target blowup receipt, excluded-corner source diagnostics and current work-net (pins v35). The resolved exceptional divisor has seven-form order (b1,R,b4,b5,b6,b7,b8), with K0/B22 coefficients 1/(1+R), R/(1+R). In the complementary V=1/R chart both coefficients acquire the seven-form minus sign. Deleting the direction has parity -1.

All endpoint and added-pole routes now agree with source residues and the decorated target extraction, including anticommutation at the resolved normal crossings:

| direction | exceptional then direction: K0 | B22 | direction then exceptional: K0 | B22 |
| --- | ---: | ---: | ---: | ---: |
| R=0 | -1 | 0 | +1 | 0 |
| R=-1 | +1 | -1 | -1 | +1 |
| R=infinity (V=0) | 0 | +1 | 0 | -1 |

The direction-first R=0 and V=0 routes exactly recover the retained original b2-then-b3 and b3-then-b2 diagnostics. The former apparent split-order mismatch is accounted for by different endpoint directions; it is not silently erased. The added R=-1 pole has residues (+1,-1) in both charts, with the actual seven-form transition sign included.

## Actual common six-form images

All three directional loci blow down to the same ordinary target corner. Their surviving six-coordinate source order is (b1,b4,b5,b6,b7,b8), and the actual CZ tangent map has rank six at both external fixtures. In the same selected row-major target coordinates, the common reference densities are

- D=5128776747428155590659/329446476889322956800;
- D=16097000442456902855258125/265114934131433581375488.

Multiply the first two table columns by D to obtain all six-form images. Both three-direction sums vanish separately for K0 and B22. This is the meromorphic projective-direction residue identity, not positive BCFW boundary-chain admission: R=-1 is outside the positive exceptional direction even though its image point is positive.

Keeping only the positive direction endpoints leaves **nonzero** split sums K0=-D and B22=+D at both fixtures. Their combined transported sum is zero. These exact residuals are retained; the indispensable added pole is not relabeled as a positive physical boundary. Orientation reversal gives nonzero endpoint defects. No fiber integration or averaging is introduced.

## Remaining physical typing gate

The actual local quotient differential maps, their decorated target modification and degree-six directional extractions are explicit. They still do not supply a source-authorized physical boundary-supercomponent object or global weighted-nine-form map. The ordinary blowdown exceptional seven-form remains unavailable, not zero.

Next nonredundant continuation: audit a normalized top-form bosonization/component bridge at a reference Y using the source F canonical density, and determine exactly which conditional linearity rule extends to the specified quotient weight. A ratio equality alone must not be promoted to a full supercomponent extraction; retain the positive-endpoint split residuals and extra meromorphic pole through any bridge construction.

Evidence: `checkers/check_history6_directional_boundaries.py`, `results/history6_directional_boundaries.json`. All scientific verdicts unchanged; successor pins v36 and structural net/SCC validation are separate from the actual signed residue tests. A nonredundant continuation remains.

# First source boundary for a WG-first Machian reconstruction

## Question

Recover a subsystem/complement interface from the existing carrier before choosing gravitational response coefficients. Use the smallest marked split: subsystem A and complement {B,C,D}. This choice is explicit, not a claim that the carrier uniquely selects A as a physical subsystem. Active obligation: source boundary inventory and composition of supplied primitive paths.

## Authoritative source

`checkers/check_natural_tower_return.py:PACKETS` supplies exactly

    AB, BC, CA, BA, AD, DB,

with directed endpoints corresponding to the two seed cycles ABC and ADB. No all-to-all completion is imported. The boundary inventory is:

- outward ports: AB, AD;
- inward ports: BA, CA;
- complement-internal arrows: DB, BC.

All six primitive records are accounted for exactly once in this partition. The complement is the directed chain D -> B -> C. Its incidence matrix on ordered coordinates (B,C,D) is nilpotent of index three.

## Exhaustive first-return packet

Composing existing arrows yields exactly four paths that leave A and return without an intermediate visit to A:

| Outward port | Inward port | Retained path | Length |
|---|---|---|---:|
| AB | BA | AB, BA | 2 |
| AB | CA | AB, BC, CA | 3 |
| AD | BA | AD, DB, BA | 3 |
| AD | CA | AD, DB, BC, CA | 4 |

Nilpotence proves that longer complement-only passages do not exist in this seed, so the inventory is exhaustive, not an arbitrary path cutoff. It does not exhaust repeated excursions through A.

All boundaries close as signed endpoint chains, but no path is identified with the empty history and no null-homotopy is asserted. In particular AB followed by BA retains two traversals; the second occurrence is not silently interpreted as undoing the first record.

With rows (BA,CA) and columns (AB,AD), the path-length generating matrix is

\[
K(z)=\begin{pmatrix}z^2&z^3\\z^3&z^4\end{pmatrix}.
\]

Every entry retains its labelled path witness in the result packet. Summing entries gives z^2+2z^3+z^4, but that aggregate is not substituted for the port data. The variable z is a formal traversal-count grade, not time, probability, energy or a physical transfer gain.

## Control against importing the old environment

The older normalized-eigenline model sums over all three other anchors, giving all twelve directed dependencies. Six of those are absent from this primitive packet inventory, including A->C and D->A. Adopting that richer support requires an additional source construction or response-law justification. This does not forbid generating such arrows; it prevents treating them as already present primitive edges. In particular AD,DA is not an available two-step first return here.

## Disposition and verification

The first missing geometric/compositional input is now explicit: two outward ports, two inward ports and four complete first-return histories through a retained complement. It was obtained without 1/90, -1/5280, an energy scale or a fitted return coefficient. This is an interface and path packet, not yet a physical outward comparison/reaction operator. A WG realization of a gravitational response must supply that next operation on these data, rather than replace them by an assumed scalar loop.

`python research/nima/checkers/check_seed_subsystem_complement.py` passed via `structured_command_execution:e_32876_1791229875068638100_56`. Results: `results/seed-subsystem-complement.json`, including source digest, typed arrows, path records and exact nilpotence checks. No commit or publication is claimed.

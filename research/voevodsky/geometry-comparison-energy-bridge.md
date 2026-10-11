# Geometry, comparison records and a proton–belt energy splitting

## Synthesis result

The first bridge is constructed: all 1836 shared-reference comparison slots now have an explicit invertible assignment to the actual retained proton coefficient transfers. Each record retains its typed endpoints, coefficient, geometric transport chart and chart signs.

The neutron-like belt has the same total support but interchanges the local-selection and alignment support budgets:

| Operation | Proton (12 placements, 3 coordinates) | Belt (3 sectors, 12 coordinates) |
|---|---:|---:|
| L: local selection | 108 | 432 |
| G: alignment | 432 | 108 |
| N: collective return | 1296 | 1296 |
| Total | 1836 | 1836 |

For the existing fully occupied stored-channel mechanism, with a common gap for each operation type, the structural energy difference is

    E_belt - E_proton = 324 (Delta_L - Delta_G).

Thus the total count agrees while the operation budgets differ. This makes the proposed neutron–proton comparison concrete: determine the relative energy cost of selection versus alignment in the retained dynamics.

This expression compares intrinsic channel contributions. A difference of bare-sector energies, physical interface contributions, or other interactions would add separately. Neutral-neutron sector protection and the physical energy unit are not supplied by this channel comparison.

## 1. Source data and the marked bridge

The comparison domain has a retained shared reference A. Its other vertices B,C,D determine three axes: the vectors from the tetrahedron center to the midpoints of AB, AC, AD point along x,y,z in the original source geometry.

Write E for the twelve directed nonidentity edges. The slots are

    E_outer × [(E × E)_arrow ⊔ ({B,C,D} × {B,C,D})_state].

The geometric proton has twelve triangle placements labelled by E and retained signed monomial transports R_t from reference placement AB. A co-moving coordinate a at placement t has global axis and sign given by column a of R_t.

The bridge uses these existing markings. It does not claim that the unmarked complex chooses A, AB, or an orientation by itself.

### State slots become local-selection transfers

Map (outer=t; state a,b) to

    raw(t, R_t b) -> local(t, R_t a).

There are 12 × 3 × 3 = 108 such transfers, precisely the actual L support.

### Arrow slots split intrinsically relative to the marked reference

For (outer=t; arrow pair s,e), distinguish two kinds of e:

- e=Aa, outgoing from the reference: map to the G transfer from local(s,R_s a) to aligned(t,R_t a). There are 12 × 12 × 3 = 432 records.
- Otherwise decode e as an ordered coordinate pair (a,b): an incoming edge aA gives (a,a), and an internal edge ab gives (a,b). Map to the N transfer from aligned(s,R_s b) to raw(t,R_t a). There are 12 × 12 × 9 = 1296 records.

The nine non-outgoing arrows are exactly the three diagonal plus six off-diagonal coordinate pairs. This is why the 144 arrow-comparison slots per outer placement split into 36 alignment records and 108 return records.

The program checks both directions of this map against the Merkle-reassembled source, with no missing or repeated arrow. Coefficients are copied from their verified source records, not invented from the slot labels. Source face-sector ownership remains recoverable through the retained placement labels and source geometry.

### What has been connected

This is a typed realization of the comparison **record set**, and supplies a way to transfer a record-indexed dressing energy to actual geometric operations. The original count-only slot domain had no sequential composition or Hamiltonian. The bridge equips it with the existing geometric port types; it does not prove that every earlier comparison-update prototype implements those operators.

Once the marked coordinate charts are fixed, the stated decoding is explicit and invertible. Its physical interpretation remains a choice to test through the resulting energies and interactions, not a uniqueness theorem over every possible bijection.

## 2. The proton–belt relation is contravariant at the support level

In co-moving charts, a monomial-projector support has coordinates (placement,local coordinate). The proton uses a 12-by-3 rectangle; the intrinsic belt uses a 3-by-12 rectangle.

Coordinate transposition exchanges the support conditions:

    L: same placement, arbitrary local coordinates
    G: arbitrary placements, same local coordinate.

To respect the actual three-stage ports while exchanging L and G, one must also reverse arrows. There is no covariant permutation of the three phase ports implementing this exchange. The unique contravariant phase map is

    raw -> aligned,
    local -> local,
    aligned -> raw.

The checker verifies this against every mapped transfer. The mapping uses the retained enumeration of the twelve proton placements and the belt's recorded twelve-coordinate sector chart. Their ordinal correspondence is explicit, not asserted to be a uniquely selected geometric identification.

This is an anti-isomorphism of the typed support graphs, not a forward physical process or a free inverse operation. Reversing a traversal does not refund its resource or erase its history.

## 3. Support duality is not coefficient equality

The complete coefficient arrays expose a further distinction. Proton G has diagonal coefficient 1/12 everywhere. Under the support exchange this would correspond to belt L, whose diagonal is nonuniform in its intrinsic twelve-coordinate chart.

An exact mismatch witness is retained in the bridge calculation. Hence the support anti-isomorphism does not intertwine the coefficient operators. The next coefficient comparison cannot be omitted by identifying the two rectangles.

This is also why equal counts and a support duality can coexist with different response and energy behaviour.

## 4. Transporting the existing stored-channel energy

Use the charged-core dressing model already constructed in `research/nima/mass-comparison-charged-core-dressing.md`. In its fully dressed sector, each occupied channel contributes its gap. Attach that gap to the operation role L, G or N through the new record map.

With common stage gaps and equal bare contributions:

    E_p = 108 Delta_L + 432 Delta_G + 1296 Delta_N,
    E_b = 432 Delta_L + 108 Delta_G + 1296 Delta_N.

Subtracting gives 324(Delta_L-Delta_G). Equal gaps recover the shared 1836 baseline. Selection more expensive than alignment makes the belt contribution larger; the reverse ordering makes it smaller. No measured mass was used to choose these gaps.

This is not a statement that merely relabelling a cost increases energy. Pulling an already assigned cost through the support anti-isomorphism preserves its sum. The difference above instead assigns the **same physical role cost** to L in both constructions and to G in both constructions. Because the anti-isomorphism exchanges the roles, these are different cost assignments under that map. A physical operation law must justify that role-based assignment.

The belt's 102-entry input and output adapters are not charged here: this compares intrinsic cores. Whether those adapters are physical maintained records or only external coordinate converters is a separate interface question.

Also, the dressing model's original positive-core charge assignment cannot silently be used as a neutral-neutron identification. This bridge transfers its channel-energy mechanism; a compatible neutral particle sector is still to be constructed.

## 5. Exact competing energy reader

We also evaluate the coefficient-quadratic reader directly on the stored coefficients, in their declared orthonormal bases:

| Sum of squared coefficient magnitudes | Proton | Belt |
|---|---:|---:|
| L | 12 | 3 |
| G | 3 | 12 |
| N | 1 | 1 |
| Total | 16 | 16 |

These equal the ranks of the corresponding orthogonal projectors, but the checker independently sums the actual coefficient magnitudes, including the belt's denominator factors.

With stage weights gamma_L,gamma_G,gamma_N, this reader gives

    E_b^quad - E_p^quad = 9 (gamma_G-gamma_L).

It has the opposite role preference from the occupied-channel reader. This is a useful discrimination, not an invitation to tune whichever expression fits a target: stored traversal/record energy and coherent coefficient energy are different observables. Retained dynamics must tell us which is the relevant rest-energy mechanism, or how both contribute.

The prior path-resource interpretation favours retaining independent record costs rather than collapsing paths to coherent feature norms. The new bridge makes that interpretation executable on the geometric arrows. It still needs a source-generated gap law and particle-sector dynamics.

## 6. What remains, now more narrowly

1. **Energy mechanism:** decide, using the retained operations, whether stored-channel costs, coherent quadratic costs, or a specified combination supply the persistent excitation energy.
2. **Stage costs:** derive Delta_L and Delta_G and any within-stage variation from those operations. The common N contribution cancels only under the stated common-gap assumption.
3. **Elementary reference:** connect the elementary excitation of the mass models to the two-component tetrahedral spinor or the four lowest pentachoron modes. No such identification is added here.
4. **Physical sectors:** retain opposite charge and spin for the proton/electron branch and construct the neutral belt sector without an unrecorded reassignment.
5. **Composite readout:** feed the resulting constituent energies into the existing hydrogen mass-and-recoil adapter, then derive its binding input and test the deuterium extension.

The first bridge is therefore complete as an explicit record-level construction. The proton–belt comparison now has a concrete role exchange, a proven variance, a coefficient mismatch, and two computable energy differences. The remaining question is no longer simply what 1836 counts: it is which retained operations have which physical energy costs.

## Reproduction

    python research/voevodsky/checkers/check_belt_three_by_twelve.py
    python research/voevodsky/checkers/check_geometry_comparison_energy_bridge.py

The proton Merkle reconstruction is replayed inside the new checker. The belt generator was also freshly rerun. All arithmetic is exact. Results and the complete invertible mapping, original proton coefficients, chart signs and corresponding belt coefficients are stored in:

- `results/geometry_comparison_energy_bridge.json`
- `results/geometry_comparison_energy_bridge_store.json`

The stored records bind both input coefficient stores by SHA-256. No coefficient tables or old constructions are modified.

# Elementary-gap adapter: keep the full interaction generator

## Construction and result

We constructed a common-clock internal-channel adapter and tested it against the actual normalized proton and belt contact spectra. It preserves both logical spin states and does not convert species.

The elementary reference is the gap of the existing spinor defect reader

    H_e = m_e I + E_star (I-N_e).

The coherent doublet and dark sector differ by E_star. This supplies a reference GAP; m_e remains a separate coherent-sector offset. The prior electron frontier already distinguishes these quantities. Setting E_star=1 fixes units in this test, not the electron rest energy.

The new interaction rule is to reuse the uniform involution generator E_star*(I-F)/2. We specify F as a swap between an auxiliary internal doublet and the normalized carrier contact, acting identically on both spins. Within each species the auxiliary carries the same Q and B as the carrier. The swap is a newly declared internal operation; it is not electron absorption or a map converting the elementary charged sector into a nucleon.

Let w be the unit contact and a the auxiliary basis vector. The complete exchange generator is

    P_exchange = (a-w)(a-w)^dagger / 2.

It contains the off-diagonal exchange AND the diagonal contact term |w><w|/2. Keeping only the exchange would not be the same elementary-gap rule.

### Test 1: one exchange operation

    H = mu I + E_star (K + P_exchange).

The actual K has coherent zero vector u. Choosing auxiliary amplitude <w,u> makes P_exchange annihilate the joint state. Both terms are positive, hence both carriers have exact ground energy mu. The splitting is zero.

This agrees with the earlier source-only elimination lesson in `source-channel-closure-and-all-face-dressing.md`: completing an exact positive compatibility operator does not create a rest-energy difference merely by changing its presentation. Here the added auxiliary also has a matched zero state.

### Test 2: exchange plus internal occupation

Add the occupation involution F_occ=I-2P_aux using the SAME elementary gap:

    H = mu I + E_star (K + P_exchange + P_aux).

For the lowest dimensionless energy y, eliminating the auxiliary gives

    R(-y) + 2 + 1/(1-y) = 0.

The relevant interval is between zero and the smaller of 1 and the first positive contact pole. The residual is strictly increasing there, tends to negative infinity at zero and positive infinity at its upper boundary. Thus its unique root is the lowest bright-sector energy. The unchanged native dark modes have no coherent zero mode left outside this sector and positive energies above the bracketed root. Each energy remains a logical spin doublet.

Exact rational root brackets give:

| Carrier | (E-mu)/E_star |
|---|---:|
| Proton | 0.0438854107578 |
| Belt | 0.0243143957456 |
| Belt minus proton | -0.0195710150122 |

This rule reverses the desired ordering. No measured masses selected an input.

## What the adapter resolves

A common bare offset and an overall clock scale cancel from the relative-energy test. We now have an explicit spin-compatible elementary-GAP interface and an executable full-generator comparison, rather than an unexplained identification of g with that gap.

The earlier heavier-belt result uses an independent auxiliary gap and an off-diagonal exchange. Its ordering cannot simply be carried over to this one-clock projector completion: the additional contact self-term changes the spectrum. Dropping it would change the interaction law.

The next constructive input is therefore the complete physical exchange generator, including its diagonal terms. It must preserve the source response advantage after its own self-energy is included. Multiplying the failed rule by an energy scale cannot repair zero or reversed splitting. The elementary rest offset is also not determined by a bright/dark gap.

## Verification

    python research/voevodsky/checkers/check_elementary_gap_contact_bridge.py

Results: `results/elementary_gap_contact_bridge.json`.

Exact checks cover metric-weighted Hermiticity, exchange-projector idempotence and rank, matched zero vectors, normalized source contact weights and disjoint rational root brackets. Species labels are constant on each block; tensoring every operation with I_2 preserves spin transport. The actual contact spectra and their provenance hash are retained unchanged. The elementary gap reader and uniform involution rule are reused mathematical constructions, not newly derived elementary dynamics.

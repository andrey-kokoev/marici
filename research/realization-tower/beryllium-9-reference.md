# Be-9 central-sleeve trial

The Be-9 reference starts from the eight retained Be-8 identities. The switchable
**Central neutron sleeve (trial)** is enabled by default; disabling it restores
the unmodified Be-8 clone. Be-8 itself never uses this switch.

## Explicit connection rule

Only the four mixed P/E strands change their middle route:

    input pole → entry rim port → centre → exit rim port → output pole

The old direct rim segment is replaced by two interior links. All eight IDs,
(t,p,e) labels, input slots and output slots remain unchanged. The four pure
white/blue strand guides remain exactly as before.

Using the output-slot strand labels displayed in the viewer:

- Incoming pair at (+,-): strands **7 and 2**.
- Incoming pair at (-,+): strands **1 and 8**.
- Outgoing pair at (++): strands **2 and 1**.
- Outgoing pair at (--): strands **7 and 8**.

The sleeve records four explicit identity-preserving passages. It is not an
unlabelled joining of crossing lines and does not create or discard conductors.
The original eight-by-eight endpoint permutation is unchanged; the edge–strand
incidence changes. There are twelve shell edges plus four interior links, with
seven routing vertices: six shell vertices and the central sleeve.

## Display

All three reference/component diagrams use the new complete guides. Four straight
segments on each affected route now have four white midpoint polarity markers.
Their 3D assemblies show a translucent central region of radius 0.2. Inside it,
the four rendered conductors pass through separate points in four quadrants,
each less than 0.057 from the centre. These display lanes preserve the recorded
entry/exit connections rather than visually merging the four conductors.

Depth-four simplex layers and Combined's candidate continuation rules are not
changed by this reference trial. The experiment adds a shared central region;
it does not calculate a binding energy or lifetime.

## Verification

- `node --test tests/beryllium-9-sleeve.test.mjs`
- `node scripts/test-beryllium-9-sleeve.mjs`

Checks cover the exact four selected identities, two input/output pairings,
unchanged endpoint permutation and other four guides, four distinct passages
inside the sleeve, all three assemblies, reversible toggle, persistence and
unchanged Be-8.

# Su-32 local geometry reproduction v2

## A coordinate-independent description of the reproduced switch

The v1 straight/swap table depended on independently numbering the ports at each
end. That table was correct in its stated convention, but its held-bit parity
was not an intrinsic geometric description. The reference admits a cleaner one.

For each of the eight upper mixing carriers:

1. One incoming arm is straight back along the carrier; the other is oblique.
2. The oriented carrier and the oblique incoming arm define a plane P.
3. Exactly one outgoing arm lies in P. The other lies outside P.
4. The varying polarity bit **+ selects the out-of-plane departure**;
   **− selects the coplanar departure**.

As in v1, a=+ selects p and a=− selects e. At entry, agreement of the selected
sign with b identifies the oblique arrival; disagreement identifies the straight
arrival. Thus a identifies the polarity being read, b identifies how it arrives,
and its sign chooses the geometric exit class. The full identity and payload
remain intact. The other polarity remains carrier context, not a separate
coordinate-order switch in this description.

This is reproduction of the existing reference's upper local transitions, not
a derivation of its globally chosen middle matching. The labels a,b,p,e are
still supplied by that reference, not assigned to the eight layers by this work.

## Verification and physical angle

All 16 passages match their actual next reference edges. All reverse passages
recover their inputs. Each motif is predicted by a rule learned from the other
seven. Prediction survives reversed port-array order, removal of the observed
route table, and a rotation, reflection, translation and uniform rescaling into
the viewer's actual 3D metric. Strand IDs are retained but not read to choose exits.

For vectors (carrier, oblique arrival, outgoing arm), native Gram determinants
are exactly 0 for the coplanar departure and 4 for the skew departure. The latter
has transverse cosine 1/3, hence an **unoriented plane angle acos(1/3) =
70.528779°** about the carrier; its supplementary oriented angle is 109.471221°.
These values come from the reference geometry. Neither is an assumed 120° twist.

Only one outgoing arm is skew. The entire three-arm output junction is not a
single plane. Rotating a complete planar fork as a rigid object would not
reproduce that junction.

| Motif | Retained identity | Colour | Selector | Arrival | Departure |
|---|---|---|---|---|---|
| 1 | `wire:++++` | white | p=+ | oblique | skew |
| 1 | `wire:++-+` | red-white | p=- | straight | coplanar |
| 2 | `wire:+-++` | white | p=+ | straight | skew |
| 2 | `wire:+--+` | red-white | p=- | oblique | coplanar |
| 3 | `wire:-+++` | white | e=+ | oblique | skew |
| 3 | `wire:-++-` | blue-white | e=- | straight | coplanar |
| 4 | `wire:--++` | white | e=+ | straight | skew |
| 4 | `wire:--+-` | blue-white | e=- | oblique | coplanar |
| 5 | `wire:+++-` | blue-white | p=+ | oblique | skew |
| 5 | `wire:++--` | blue | p=- | straight | coplanar |
| 6 | `wire:+-+-` | blue-white | p=+ | straight | skew |
| 6 | `wire:+---` | blue | p=- | oblique | coplanar |
| 7 | `wire:-+-+` | red-white | e=+ | oblique | skew |
| 7 | `wire:-+--` | blue | e=- | straight | coplanar |
| 8 | `wire:---+` | red-white | e=+ | straight | skew |
| 8 | `wire:----` | blue | e=- | oblique | coplanar |

## Larger carriers: bounded exhaustive search

Enumerated all 432 contiguous internal windows of the sixteen existing
routes, with either orientation: 353 distinct runs,
65 shared by at least two records. There are
46 eligible two-arrival/two-departure candidates, including
both all-traffic carriers and two-strand subtraffic without deleting other
identities. Eligible runs span 1, 2 or 4 edges; four was a result, not a search cap.
An independent strand-pair enumerator in the tests recovers all 44 two-record
cases; two additional candidates carry more than two records.

There are **no** matches to 120° three-stars at both ends, either using actual
first/last tangents or replacing the internal run by its endpoint chord. The
latter intentionally relaxes internal shape and length before testing angles.
A synthetic true hex carrier passes the same search as a positive control.

This excludes these particular shared-run coarse-grainings. It does not cover
arbitrary new paths, larger branched regions, virtual ports inside edges/faces,
or cross-layer identifications.

## Folding: one precise obstruction

For a filled planar chart, a non-stretching fold cannot increase the Euclidean
distance beyond the length of an available straight path on that chart.
Two unit arms 120° apart have endpoint distance sqrt(3). Each reference incoming
star instead contains an opposite pair of unit arms with endpoint distance 2.
The required squared-distance expansion is **4/3** at every upper motif.

Thus an ordinary non-stretching fold of that single filled white-edge
neighbourhood cannot reproduce these unit-edge junctions. This statement assumes
the chart contains the local straight chords. It is **not** a no-go theorem for
a freely hinged wire graph, a cut sheet, a branched coarse-graining, or a different
assignment of virtual boundary ports. Those require additional explicit geometry.

## What this establishes, and what remains

We now reproduce the local routing using intrinsic input-plane / output-plane
information, rather than arbitrary coordinate port numbering. The proposed
white connector needs to distinguish coplanar from noncoplanar continuation.
The current separate planar layers do not yet supply that interface: each of
their own complete white-edge stars has two coplanar outgoing arms.

The next geometric object to seek is a **branched multi-edge or cross-layer
interface with explicit boundary ports**, not another rigid alignment or a
longer shared chain. Any such correspondence must preserve the reference
records and predict the exit classes above. No inter-layer joins or routes were
added to either viewer by this investigation.

## Reproduction

- node --test tests/sulfur-local-geometry.test.mjs
- node scripts/check-sulfur-local-geometry.mjs
- Source: research/realization-tower/sulfur-local-geometry.mjs
- Receipt: results/sulfur-local-geometry-v2/verification.json

# Witness-preserving matrix packets and the finite-functor obstruction

## Source and type boundary

The retained comparison constructor supplies an equivalence witness. The137-slot
fixture separately supplies actual matrix leg values and d4=2I. Test whether
these can be attached without identifying unlike data or changing the old
readout. This is an attachment/composition obligation before scalar observation.

For the finite pointed comparison groupoid, use the previously derived
stabilizer coordinate h in S3, with endpoints and frames retained. A faithful
rational representation rho(h) acts on the sum-zero plane of the three unmarked
states. In basis e1-e3,e2-e3 it preserves the Gram matrix [[2,1],[1,2]]. This is a
representation metric, not a derived physical metric.

## The existing matrices cannot be just those finite equivalences

Every based loop in the finite groupoid has sixth power identity. A functor
sending its reference arrow to d4 and a comparison to C must therefore satisfy

    (d4^-1 C)^6 = I.

The existing base slot has C=I and d4=2I. Its normalized sixth power is I/64,
not I. Thus the present matrix assignments cannot all be functorial images of
that finite comparison groupoid. This is an obstruction to that identification,
not to a more general readout, a nonmultiplicative observer, or an enriched
source with additional amplitude data.

It also does not invalidate the original matrices as declared fixtures. It
shows that their response amplitudes were not derived merely by representing
finite equivalences.

## A faithful retained-data adapter

Attach the actual response and witness as distinct channels:

    packet(C,h) = diag(C,rho(h)),
    reference = diag(d4,I),
    return = diag(d4^-1,I).

Then reference-bridged composition is

    packet(C2,h2) return packet(C1,h1)
      = packet(C2 d4^-1 C1, h2 h1).

The top block gives exactly the previous matrix response; the lower block
recovers the six-valued witness. Even C=0 does not erase h. Endpoint records,
frame choices and parent histories remain attached metadata rather than being
replaced by the block matrix.

Assign the four typed primitive objects A,U,V,B to four differently pointed
copies of the source carrier. For each supplied primitive witness coordinate,
the endpoint-frame formula reconstructs its actual permutation. The checker
uses declared admissible sample witnesses on all primitive legs and verifies
composition into all137 slots. This supplies a typed conditional adapter, not
a physical selection of those samples.

The original slot matrices and all mixed rectangle responses survive unchanged.
There are still137 counted slots. The four-by-four block notation introduces
no claimed new physical field count, cost, or interaction.

## Why retaining the channels matters

Absorbing rho(h) into unrestricted C is not faithful: (I,h) and (rho(h),identity)
can give the same product C rho(h). Nor is averaging a replacement for retaining
witnesses. Averaging identity with a transposition produces a singular matrix;
averaging rho over all six witnesses gives zero. These averages are valid linear
readouts but are not individual equivalence witnesses.

Consequently promoted families must retain their members' witness channels.
Their mean response alone cannot reconstruct the source comparisons. The direct
block product used here preserves both channels but does not supply a physical
interaction between them.

## Result and remaining constructor

There is now a faithful data-level link between supplied finite comparison
witnesses and the actual137 matrix records, preserving both composition laws.
There is also a precise obstruction to identifying those two channels outright.

The remaining source question is how the response amplitudes are generated and
how they depend on, or interact with, the retained equivalence witnesses. Their
current numerical assignments and the sample witness assignments are inputs.
A physical metric, DG witness realization and completed rung transport are not
derived by this block encoding.

## Verification

    python research/nima/checkers/check_witness_matrix_packet_adapter.py
    python research/aspect/scc/scc.py check nima-witness-matrix-packet-adapter

Exact rational checks of the faithful S3 representation, typed primitive
composition, all137 decoded matrices and rectangles, bridge products, zero-
response witness retention, the finite-order obstruction, and failed witness
absorption/averaging. Machine result:
`research/nima/results/witness-matrix-packet-adapter.json`.

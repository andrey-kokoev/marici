# The original seed rotations resolve the seed-face blind spot

## Constructed result

The five hidden local-mode directions found in
`proton-native-task-catalogue-v1.md` can be resolved using a **word in the two
original seed rotations**, without supplying a new interaction matrix.

In application order, use

    (ABC), (ABC), (ADB).

The resulting vertex permutation is (AC)(BD). It exchanges the original face
pair ABC/ABD with its complementary pair ACD/BCD. In the supplied Cartesian
frame its spatial matrix is diag(-1,1,-1).

With the probe held at the seed-labelled ports, compare the original raw input
and this source-rotated raw input. The combined readout has full rank 36 on the
coefficient carrier. On the twelve-dimensional locally admitted subspace,
exactly **five additional independent complex readings** supplement the
original seed-face records and collective return. An explicit decoder is stored.

This extends the observation grammar: the original fixed L/G/N schedule does
not itself perform this word. The construction uses an existing geometric
source action on retained/reproducible raw data. It does not derive a physical
rotation gate, detector, extra copy of an unknown quantum state, or restored
information from an already projected output.

## Derive the coefficient operation from the seed

The unchanged source frontend discovers ABC and ADB from the six directed
arrows and generates their twelve-element proper-rotation group. For each
vertex permutation p, derive R_p from the supplied source coordinates. On an
outer-arrow-labelled triangle ab, define the coefficient action by

    (U_p x)_(p(a)p(b)) = R_p x_(ab).

Both the triangle address and its spatial coefficient frame are transported.
No desired response value enters this definition.

The checker verifies, exactly, for all twelve actions:

    U_p^dagger U_p=I,
    U_p L=L U_p, U_p G=G U_p, U_p N=N U_p=N.

It also checks every composition with each of the two generators, establishing
the generated action rather than a single hand-picked matrix identity.

A breadth-first search of the source generator words selects a shortest word
exchanging the observed and unobserved face pairs. Its three applications give
the word displayed above. The corresponding coefficient action is retained
in full sparse form in the receipt.

## Solve the actual reconstruction task

Let O be the baseline raw/local/aligned readout at all seed-face coordinates.
The original catalogue established

    rank O=19,
    rank OB=7,

where B encodes the twelve admitted local amplitudes. The new readout is OU,
with U the selected source action. Exact ranks give

    rank [O; OU]=36,
    rank [OB; OUB]=12.

The six triangles read in the second orientation are precisely the six absent
from the first. On arbitrary inputs the raw readings already cover all 36
coordinates; local/collective readings remain consistency checks.

On locally admitted inputs, fewer extra readings suffice. Keep:

1. one raw coordinate from each of the six original seed-face triangles;
2. one collective output coordinate, which fixes the total local-amplitude sum;
3. five independent fixed-seed coordinates after U.

The selected extra addresses are AB:x, AD:x, BA:x, BC:x and CA:x, **read after
the source action on the raw input**. Their matrix together with the seven
original readings is an invertible 12-by-12 local-amplitude observation map M.
The stored decoder satisfies D M=I12 exactly. Multiplication by B reconstructs
the complete locally admitted coefficient state.

Five is minimal for scalar complex-linear extra readings because the existing
map has a five-dimensional kernel. Four such readings cannot be injective on
that kernel. This is a readout-resource bound, not an arrow-cost or mass count.

## The earlier indistinguishable pair is now separated

Recall the two local-amplitude assignments:

- x has amplitudes 2 at AC and 0 at BD;
- y has amplitudes 0 at AC and 2 at BD;
- all other local amplitudes are 1 in both.

They have identical original seed records, identical whole return and equal
squared norm 210. At the fixed seed address CA:x after U, their readings are

    x: -1 + 3 sqrt(-3),
    y: 0.

Thus this is an explicit solution to the discrimination problem, not only a
count of increased observation rank. The source operation moves the unresolved
AC contribution into a seed-accessible address while preserving all native
coefficient relations.

## Two falsifiers that do not repair the problem

### Passive frame change

Transporting both state and observer gives

    (O U^-1)(U x)=Ox.

This adds no information. The positive result fixes the seed observer while
precomposing with U, or equivalently allows the corresponding readdressed
probe of the retained raw data. Simultaneously renaming everything is not that
capability. The passive cancellation is checked exactly.

### Rotation only after the collective projection

Because UN=N,

    O U N=O N.

Applying any of the twelve source rotations to the terminal collective record
cannot distinguish the pair. The information must be accessed while the raw
input or its pre-return local record remains available. The checker verifies
this negative control on the actual pair and as a matrix identity.

## Verification and status

The attachment-transport question, scope extension and three rival mechanisms
were frozen before running the new checker. SCC fingerprint:
`c1b2bcbeaab890f664f0a97159432ad682d246c4135f7325d802f51d0b1825a8`.

    python research/voevodsky/checkers/check_proton_seed_rotation_readout_repair.py

The checker passes source reconstruction, all twelve unitary/intertwining
identities, every generator composition, both full-rank conclusions, the exact
five-reading decoder, and the passive/post-return negative controls. An
independent rational-realification arithmetic implementation additionally
checks the ranks and decoder identity. All original source and native stores
are read-only.

Receipt: `results/proton-seed-rotation-readout-repair-v1.json`.
Contract: `inputs/proton-seed-rotation-readout-repair-v1.json`.

**Insight supplied by the relationship list:** fixed-seed observation and
source-generated readdressing have different information content. The native
collective return forgets where disagreement resides, but the seed's own
symmetries provide a sufficient family of probes while that information is
retained. This is a constructed mathematical task solution on the existing
coefficient realization, not a claim of general-purpose computation or a
physical measurement implementation.

The continuation `proton-single-probe-cycle-v1.md` reduces the probe resource:
one fixed coordinate plus all geometric orientations has rank 24, while a
source slot-cycle extension gives a complete 36-reading decoder. Its metric
audit proves that the latter action cannot be made unitary while keeping the
existing local projector orthogonal merely by changing the metric.

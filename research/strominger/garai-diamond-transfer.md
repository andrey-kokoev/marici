# Garai paired-layer construction on unchanged diamond: disposition

## Fixed experiment

The operator requests the transfer test without forces. Source geometry remains
A(n)=n1(0,2,2)+n2(2,0,2)+n3(2,2,0), B(n)=A(n)+(1,1,1). A centers carry the
proposed N role, B centers the proposed P role. Every coordination tetrahedron
retains all four corners; a finite occupied patch has exterior/halo ports, not
truncated tetrahedra. No FCC nearest-neighbor edges replace diamond edges.

Frozen constructor: for each n=1..6 take nonnegative primitive indices with
sum2n-2 on B, and sum2n-1 on A. These adjacent occupied(111) planes are triangular
patches of side lengths2n-1 and2n, exactly the paired triangular cardinalities
used in Garai Fig1. Source specification:
`inputs/garai-diamond-transfer-v1.json`.

## Result: geometric arithmetic survives, P/N identification does not

| n | desired half | actual P | actual N | total sites |
|---|---:|---:|---:|---:|
|1|2|1|3|4|
|2|8|6|10|16|
|3|18|15|21|36|
|4|32|28|36|64|
|5|50|45|55|100|
|6|72|66|78|144|

This follows generally, not by fitting:

    P=T_(2n-1)=2n^2-n,
    N=T_(2n)=2n^2+n,
    P+N=4n^2, N-P=2n.

The whole triangular plane belongs to ONE diamond family. One cannot assign
half its sites to the other species without changing the source role rule.
Swapping the orientation/family convention swaps the two counts; it does not
make them equal. Thus Garai's2n^2 half-count is their average, not the actual
number of P centers in this fixed transfer. This is an obstruction for this
constructor, not a theorem against every possible diamond patch with2n^2 P.

## A stronger universal obstruction to the regular2P2N core

Within either diamond family, squared distances are0 modulo8 in this chart.
Between families they are3 modulo8. Proof: same-family coordinate differences
are twice integers whose sum is even; opposite-family differences have three
odd components. Every mixed-family tetrahedron has both kinds of pair, so they
cannot all have equal length. Hence NO regular tetrahedron made of these center
sites can contain2P2N, even if non-nearest-neighbor pairs are allowed.

This does NOT say helium4 or any four-site balanced assembly is impossible.
A control2P2N nearest-neighbor path has coordinates

    (0,0,0), (1,1,1), (0,2,2), (-1,3,1),

squared pair distances3,3,3,8,8,11, and nonzero volume2/3. It is a distorted
geometric tetrahedron, not Garai's regular close-packed core. It is not assigned
stability by this experiment. Likewise each individual coordination tetrahedron
remains regular: its four opposite-family corners are monochromatic, as required.

## Information test: one additional component is necessary and sufficient

The actual internal diamond edges number E=3P. The patch is connected. For scalar
source states f at its V=4n^2 centers, read the mean(f_i+f_j)/2 on each internal
contact. The reader kernel is exactly span(tau), with tau=+1 on A,-1 on B:
edge equations x_i+x_j=0 propagate throughout the connected graph.

Therefore internal interface rank is V-1, NOT the displayed number E of edge
readings. The two opposite0/1 role patterns both read as1/2 on every edge.
Their indistinguishability is an exact source counterexample.

Two faithful repairs were verified on EVERY original scalar basis vector:

* Keep one independent staggered component alpha=sum(tau_i f_i)/V alongside
  all internal edge means. A tree traversal plus alpha reconstructs every f_i.
* Alternatively use one actual exterior-port mean with its outside endpoint
  value KNOWN/RETAINED; this fixes the otherwise free root amplitude and a
  traversal reconstructs the whole interior. Without that outside reference,
  the single port mean is not sufficient.

The packet has E+1 displayed coordinates but independent rank V. There are
E-V+1 internal edge consistency constraints. This restores information; it does
not create extra protons, electron states or a capacity2n^2. It is a snapshot
reconstruction result, not proof that the finite patch is dynamically closed
under the full infinite-network update. All other exterior ports remain explicit.

## Verification and next test

    python research/strominger/checkers/check_garai_diamond_transfer.py
    python research/aspect/scc/scc.py check garai-diamond-transfer-v1 --verbose

Receipt: `results/garai-diamond-transfer/verification.json`. Successful checks
include expected rejection witnesses; `hypothesis_status` is explicitly
`direct_faithful_transfer_rejected`, not physical validation.

No force, potential, energy, time law, charge assignment or spin factor was added.
Next nonredundant source test: grow graph-distance shells around ONE fixed A-B
bond, treating both endpoints symmetrically. The source exchange fixes that bond
as a set, supplying a definite A/B-balanced growth candidate. Measure its actual
counts, contact ranks and role-sensitive reconstruction across sizes; do not
assume2n^2. Raw count agreement alone is insufficient, and this new rule must not
be presented as Garai's constructor or fitted separately to each target nucleus.
This exploratory branch does not complete or rewrite the unfinished older
flag-family iteration/frontier.

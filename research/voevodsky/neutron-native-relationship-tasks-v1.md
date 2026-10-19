# Neutronlike 1,836 relationships: same aggregate spectrum, different tasks

## Result

The neutronlike intrinsic network has the same 1,836 transfers as the protonlike
network, but its stage-resolved information tasks differ sharply. A fresh
isolated producer replay reconstructs every native intrinsic coefficient. All
comparisons below preserve the neutron's metric and stage labels.

| Quantity | Protonlike | Neutronlike |
|---|---:|---:|
| L transfers / rank | 108 / 12 | 432 / 3 |
| G transfers / rank | 432 / 3 | 108 / 12 |
| N transfers / rank | 1296 / 1 | 1296 / 1 |
| Raw local-rejection dimension | 24 | 33 |
| Locally admitted collective-disagreement dimension | 11 | 2 |
| Collective dimension | 1 | 1 |
| Minimum stage-coordinate addresses for arbitrary raw reconstruction | 24 | 33 |
| Locally admitted amplitudes | 12 triangle amplitudes | 3 paired-face sector amplitudes |

An address is one intrinsic coordinate slot read at raw/local/aligned copies;
it is not a primitive arrow or physical detector. The coordinate systems and
geometries differ, so this table compares declared tasks, not particle masses.

The staged transfer ranks, recurrent sector and derived Hermitian spectrum
are nevertheless identical. Those aggregate invariants cannot distinguish
the organization that determines the different tasks.

## Native source and metric, not a relabelled proton

The source is the existing intrinsic three-by-twelve belt protocol. It has
eighteen actual geometric triangles, each supplying two real planar axes;
three rotating paired-face sectors each contain six triangles and twelve
complex coordinate slots. L selects a single sector-wide line in each sector.
G aligns corresponding intrinsic slots across the three placements.

This is **not** the old fifty-four-coordinate ambient belt realization. The
conversion interfaces to that older carrier have separately counted costs.
The eighteen original triangle modes remain geometry records, but this L does
not independently select eighteen local lines.

The store represents orthonormal physical entries as

    numerator_ij / sqrt(d_i d_j).

For exact rational/algebraic calculations we use the equivalent numerator
chart with

    M=diag(1/d_i),
    A_ij=numerator_ij/d_j,
    A_sharp=M^-1 A^dagger M.

The decoded L,G,N are orthogonal projectors for M. They are not ordinary
Euclidean orthogonal matrices in this numerator chart. The checker detects
the incorrect Euclidean adjoint as a negative control rather than silently
changing the inherited metric.

## Fresh reconstruction scope

`check_belt_three_by_twelve.py` is run with its output/input base redirected
inside an isolated temporary tree containing copies of its bound native
geometry and source store. It reconstructs the eighteen plane frames,
sector ordering, local numerators, alignment and return, and passes its own
checks. The generated intrinsic store equals every field and coefficient of
the established store. Shared outputs are not regenerated.

This is fresh replay of the intrinsic geometry-to-coefficient producer. It is
not a fresh execution of the entire raw real/complex-arrow frontend or its
upstream geometry providers. The existing bridge packet documents that
separate end-to-end connection.

## 1. Diagnose different formation questions

The actual schedule still yields

    x, Lx, GLx=Nx, NGLx=Nx.

No extra raw Gx probe is inserted. The three orthogonal readout components are

    (I-L)x       dimension 33,
    (L-N)x       dimension 2,
    Nx          dimension 1.

Thus the neutron sector-local selection discards more arbitrary input
directions than the proton's triangle-local selection. But once sector-local
selection is satisfied, only two independent inter-sector agreements remain.
This is an architectural distinction, not a claim of physical greater loss
or lower complexity across all possible interfaces.

A source-derived local encoder B and metric-aware decoder C satisfy

    CB=I3, BC=L,
    GB=BJ, NB=BJ, N=BJC,
    J=(1/3)1 1^T.

The three locally admitted sector amplitudes must agree for collective return.
They require two independent comparisons, rather than the proton's eleven.
The receipt retains every encoder/decoder coefficient.

The four joint L/G sectors have dimensions 1,2,11,22, compared with the
proton's 1,11,2,22. An isometry preserving both ordered stage maps cannot
identify these protocols: it would preserve rank L and rank G, which differ.

## 2. Exact reconstruction threshold: 33 addresses

For an address set S, let k_s be its number of coordinates in sector s. Read
those coordinates in raw, local and aligned stage copies. Then

    rank O_S=sum_s d(k_s)+indicator(0<number_empty_sectors<3),
    d(0)=0,
    d(k)=min(12,k+1) for k>0.

### Proof

Within a sector, the selected local mode has twelve nonzero coordinates.
Observed raw coordinate rows contribute k_s independent readings. Every
observed local-selection row is proportional to the one selected mode
covector, whose nonzero omitted entries make it independent until all twelve
raw coordinates are read. Different sectors have disjoint support. The global
row adds one further direction exactly when some but not all sectors are
unobserved. If every sector is touched, that row is already spanned by the
three local mode rows.

This proves the formula for every coordinate-address subset, not by
extrapolating the twenty-nine regression masks.

Full reconstruction holds **iff at least eleven addresses are read in every
sector**, hence a minimum of 33. The 33-dimensional ker L gives a second lower
bound: every downstream reading vanishes there, so at least 33 independent
raw coordinate readings are necessary.

An explicit decoder uses eleven raw coordinates and one local-stage output
per sector. For missing coordinate k and chosen local output j,

    x_k=[(Lx)_j-sum_(i!=k) L_ji x_i]/L_jk.

All native denominators are nonzero. The stored 36-by-36 inverse is checked
on every basis vector. Every one of the twelve possible omissions in each
sector is checked independently, proving all 12^3 combined layouts. Removing
any address from the displayed minimal layout leaves a stored nonzero
invisible direction.

The previous proton theorem cannot be copied unchanged: two coordinates per
three-coordinate triangle are sufficient there, but a twelve-coordinate
sector needs eleven in this neutron protocol.

## 3. The actual two rims see every locally admitted amplitude

Derive the observed triangles from the native geometry, not from convenient
store ordering. Select the three lower/lower rim-edge triangles and the three
upper/upper rim-edge triangles, reading both intrinsic axes of each. The six
triangle indices are

    1,4,7,10,13,16.

They give four coordinate addresses in each of the three sectors. Their
complete raw/local/aligned observation has

    rank 15 on arbitrary raw inputs,
    rank 3 on locally admitted inputs.

There are twenty-one hidden raw-input directions, but **every one lies in
ker L**. No locally admitted inter-sector disagreement is hidden by these
rim readings. The full twenty-one-vector observer kernel is stored and tested.

This is different from reading the proton's original two seed faces: that
observation leaves five locally admitted disagreement directions unresolved.
The two geometrical observation sets are explicitly named and are not assumed
to be the same physical probe. Within their declared access, the contrast is
exact and tells us which retained records would complete each interface.

## 4. A fixed probe under the existing C3 placement rotation

The native source rotation moves one paired-face sector to the next. Its
co-rotating intrinsic chart preserves the twelve within-sector labels. The
actual coefficient action is the corresponding three-sector permutation,
verified against the repeated source numerators and metrics.

One fixed coordinate probe, read through all three orientations and all
native prefix stages, has rank six on arbitrary raw input. It nevertheless
separates all three locally admitted amplitudes.

The geometric orbit covers three corresponding slots, not all thirty-six
coordinates. For full raw recovery using only this source action and the
native prefix probes, eleven distinct within-sector probe slots are needed.
The new minimum is not obtained by importing the proton's twelve-element
rotation orbit or its three-slot cycle controls.

## 5. The same staged aggregate spectrum hides the organizational difference

Use the actual metric-aware staged transfer

    W=[[0,0,N],[L,0,0],[0,G,0]].

With P=diag(N,N,N), it satisfies W^3=P, with ranks16,3,3 for W,W^2,W^3.
The transient part T=W-WP has orthogonal source and sink projectors and T^2=0.
The orthogonal stage-state dimensions are again

    3 recurrent +13 one-way sources +13 sinks +79 immediately zero.

But the thirteen source channels split as

- **2** raw-to-local sector-disagreement channels;
- **11** local-to-aligned frame-consistent channels outside local selection.

This reverses the proton's 11/2 split. The eleven local-stage channels are not
created by a strict raw -> L preparation; they are visible in the larger
stage-perturbation domain.

The derived metric-Hermitian part

    K=(W+W_sharp)/2

has exactly the same spectrum as the proton staged K:

    1 multiplicity1,
    1/2 multiplicity13,
    -1/2 multiplicity15,
    0 multiplicity79.

These exact invariant projectors are verified. K is metric-Hermitian as an
operator; its sesquilinear form matrix MK is ordinary Hermitian in the
numerator chart. Mistaking K for an ordinary Euclidean Hermitian matrix would
corrupt the comparison.

Same support count and same aggregate K spectrum therefore do **not** imply
same stage-resolved reconstruction or local visibility. The retained stage
labels and geometry carry information those scalars lose.

## 6. Repeat the finite RH packet attachment without copying proton coefficients

Take the same frozen Gaussian arithmetic packet's exact rational rounding
from `rh-gaussian-seed-packet-v1.json`. Construct a new attachment from the
neutron's own source/sink directions X,Y and metric Mstage:

    D=X^dagger Mstage X,
    B_G=X+Y D^-1 G.

The exact neutron identities yield

    B_G^dagger (Mstage K) B_G=G.

The three-dimensional packet has an injective attachment, independently
verified through rational realification. No proton attachment matrix is
copied. The analytic source positivity certificate remains the same independent
arithmetic result; changing the native carrier neither strengthens it to RH
nor supplies a geometric prime/zero operation assignment.

The reason both carriers admit this packet is their signed channel capacity,
not the integer1836 by itself. This is finite form expressibility, not a
particle-dependent arithmetic mechanism.

## Verification and limits

    python research/voevodsky/checkers/check_neutron_native_relationship_tasks.py

Seven check groups pass: isolated producer reproduction; native metric and
diagnostics; staged channels/spectrum; all-mask decoder and deletion hostiles;
source C3 probe; actual rim observer/kernel; and metric-correct finite arithmetic
attachment. Independent rational calculations verify the complete decoder,
full signed packet pullback and rim rank.

Prospective SCC fingerprint:
`b85a883aa7c20e7caf40e05ace10e2f1c42b3e43c91156bfbaef250ae1809ba1`.

Artifacts:

- `inputs/neutron-native-relationship-tasks-v1.json`.
- `results/neutron-native-relationship-tasks-v1.json`.
- `scc-models/neutron-native-relationship-tasks-v1.json`.

Shared stores and source files remain unchanged. This audit does not synthesize
a new neutron control, infer physical mass/time or transfer a proton physical
instrument into the neutron geometry. It supplies the requested native
relationship/task comparison and the same bounded signed arithmetic attachment.

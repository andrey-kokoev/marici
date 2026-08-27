# Reference capacity separates displacement detection from frame identification

## Bounded question

How much independently transported reference information is required to detect
a common-mode frame displacement, identify the displaced frame, or reconstruct
the state carried inside that frame?

## Frozen frame torsor

Let a finite group \(G\) act freely and transitively on a frame set \(X\). Thus
\(X\) is a \(G\)-torsor. Choosing one origin \(x_0\in X\) gives a bijection

\[
G\longrightarrow X,
\qquad
g\longmapsto gx_0.
\]

The torsor itself has no preferred origin. A source reference is extra data that
selects or distinguishes frames.

Let

\[
\rho:X\longrightarrow A
\]

be a finite reference readout. After displacement \(g\), the observed reference
value is \(\rho(gx_0)\).

## Three distinct tasks

The reference may be asked to solve three different problems.

### Departure detection

Relative to a trusted origin \(x_0\), detect whether the current frame is still
the origin:

\[
\rho(gx_0)=\rho(x_0)
\quad\Longrightarrow\quad
g=e.
\]

This requires the origin to have a reference value not shared by any displaced
frame. A binary reference can suffice:

\[
\rho(x)=
\begin{cases}
0,&x=x_0,\\
1,&x\neq x_0.
\end{cases}
\]

The bit detects departure but does not say where the frame went.

### Frame identification

Identify the exact displacement \(g\). This requires injectivity of the orbit
signature:

\[
g\longmapsto\rho(gx_0).
\]

Hence

\[
|A|\geq|G|.
\]

If the reference consists of \(k\) trusted binary coordinates, then

\[
2^k\geq|G|,
\qquad
k\geq\lceil\log_2|G|\rceil.
\]

### State reconstruction

Even exact knowledge of \(g\) reconstructs only the frame displacement. It does
not reconstruct arbitrary coordinates of a state carried in that frame. A
separate faithful observation map on the state fibre is required.

Thus state reconstruction implies frame identification, and frame identification
implies departure detection.

Neither reverse implication holds in general.

## Uniform transition detection

Departure detection from one frozen origin is weaker than detecting every
nontrivial transition from every possible starting frame.

Uniform transition detection requires

\[
\rho(gx)\neq\rho(x)
\]

for every \(x\in X\) and every nonidentity \(g\in G\). Because the action is
transitive, any two distinct frames are related by one such \(g\). Therefore
uniform transition detection forces \(\rho\) to be injective.

The one-bit origin flag works only while the origin remains trusted and known.
Once the starting frame is itself uncertain, full frame identification capacity
is required to detect arbitrary nontrivial motion in one step.

## Authorized residual subgroup

Sometimes the programme does not need the full frame. Suppose the reference
identifies only the coset in \(G/H\) for a subgroup \(H\leq G\). Then

\[
g\longmapsto gH
\]

leaves the residual ambiguity

\[
g\sim gh
\]

for \(h\in H\).

The number of distinguishable reference values is at least

\[
[G:H].
\]

Trusted binary capacity must satisfy

\[
k\geq\lceil\log_2[G:H]\rceil.
\]

This quotient is adequate only when every element of \(H\) acts identically on
all admitted future constructors and testers. Otherwise the reference erases a
control-relevant distinction.

For an arbitrary reference map, a fibre need not arise from a subgroup. The
subgroup language is authorized only when the reference is compatible with a
homogeneous quotient action.

## Composition cocycle

Let the absolute frame at stage \(i\) be represented by \(g_i\). The displacement
from stage \(i\) to stage \(j\) is

\[
a_{ji}=g_jg_i^{-1}.
\]

For three stages,

\[
a_{20}=a_{21}a_{10}.
\]

This is the displacement composition law. Any transported frame annotation
must respect it. A sequence of locally plausible labels that violates this law
is not a coherent frame history.

For a bundle of local frame choices, overlap displacements obey the analogous
cocycle condition on triple overlaps. A reference that fixes each local label
but violates composition does not define one global frame.

## Detection can miss return loops

An origin bit sampled only at the beginning and end cannot detect a sequence of
displacements whose product is the identity:

\[
a_{n,n-1}\cdots a_{21}a_{10}=e.
\]

The frame may leave the origin and later return. Detecting the excursion
requires intermediate records or a path-sensitive holonomy. Endpoint frame
identity is weaker than constructor-history identity.

This is where the coefficient lens matters. An additive scalar may cancel, a
determinant phase may retain an abelianized loop, and an ordered holonomy may
retain the full noncommutative history.

## Reference independence

A reference breaks a common-mode action only when it is not transformed by the
same hidden constructor. If both diagnostic code and reference are acted on by
the same \(g\), their relation may remain unchanged.

Independence here is causal and typed. It may mean:

- a separately prepared source origin;
- transport along a distinct fault domain;
- a fixed tensor unit preserved by authorized constructors;
- an external calibration with an audited crossing;
- or a second physical carrier whose common causes are explicitly bounded.

Calling a duplicated label independent does not make its frame independent.

## Two-sheet example

For \(G=C_2\), the frame torsor has two sheets. One trusted bit can identify the
sheet completely because

\[
\lceil\log_2|C_2|\rceil=1.
\]

That bit does not reconstruct a two-dimensional amplitude living on the sheet,
nor does it synthesize an operator acting within the amplitude fibre. It fixes
one torsor coordinate only.

This is the precise correction to the claim that one trusted bit can recover an
arbitrary missing linear coordinate.

## Nonabelian example

For an \(S_3\)-torsor, exact frame identification requires at least three binary
coordinates because

\[
2^2<6\leq2^3.
\]

A one-bit reference may separate the identity from all nonidentity frames, or
distinguish a chosen two-block quotient, but it cannot identify all six group
elements.

Even three bits identifying the group element do not reconstruct the full
operator algebra carried at a quantum-double endpoint. Frame capacity and
operator-control dimension are different invariants.

## Toric-code instance

Choosing signs and orientations for logical loop representatives fixes a frame
for the logical algebra. Syndrome bits do not determine that frame because
local stabilizer data are invariant under logical-sheet changes.

A trusted logical reference can distinguish selected homology classes. It does
not reconstruct an unknown encoded quantum state, and copying the reference
does not make conjugate logical observables jointly classical.

## Optical instance

A calibrated polarizer orientation supplies a frame reference for angle. A
binary mark can detect that a device left one certified orientation, but cannot
identify an arbitrary new angle. Multiple calibrated marks increase angular
identification capacity only if their physical alignment is independently
preserved.

Returning to the original endpoint orientation does not prove that the optical
path accumulated no phase or ordered polarization transformation.

## Software instance

A boolean health flag can report that configuration differs from a blessed
origin. It cannot identify which of many configurations is active. A version
identifier can identify a configuration class, while a content hash can provide
finer capacity.

None of these reconstructs runtime state. Moreover, beginning and ending on
the same version does not prove that no intervening migration occurred. An
append-only transition record or ordered provenance chain is a path-sensitive
constructor, not another endpoint label.

## DPC: reference claims must state their capacity

The conjecture is:

> Every proposed source reference should declare whether it detects departure
> from one trusted origin, identifies a quotient frame, identifies the full
> torsor element, or reconstructs state inside the frame. Its alphabet size,
> residual symmetry, composition law, and causal independence must match that
> claim.

This blocks the common explanatory slide from one trusted bit to complete state
reconstruction.

## Critics

### A continuous reference can encode unlimited information

Only under unbounded precision. A physical capacity claim needs a metric,
noise model, resolution, and stability theorem. The finite theorem is the exact
zero-error skeleton.

### One bit can detect every nonidentity group element

From one trusted origin, yes. It cannot identify which element occurred, and it
cannot uniformly detect every transition between uncertain frames.

### The subgroup quotient is always the right residual object

No. It is right only for a reference compatible with the group action. An
arbitrary labelling can have fibres with no homogeneous quotient structure.

### Returning to the origin means no lasting error

Only for endpoint-frame tests. Path-dependent phases, costs, state changes, and
ordered holonomies may remain.

### A canonical mathematical unit supplies the needed reference

It supplies a preferred abstract origin. A physical constructor must still
prepare, transport, and compare that origin without sharing the fault being
tested.

## Exact falsifiers

- One origin bit used to identify one of more than two displaced frames.
- Exact frame identification claimed with fewer than \(\lceil\log_2|G|\rceil\)
  trusted binary coordinates.
- A residual subgroup accepted although its elements change an admitted future
  constructor.
- Local displacement labels violating the composition cocycle.
- Equal initial and final frames used to infer an empty constructor history.
- A reference transformed by the same common-mode fault called independent.
- Torsor-frame identification used to infer arbitrary fibre-state
  reconstruction.

## Machine-readable reference certificate

```json
{
  "code": "torsor_reference_capacity",
  "frame_group": "G",
  "task": "departure_detection | quotient_identification | full_frame_identification | state_reconstruction",
  "reference_alphabet_size": "A",
  "binary_capacity": "k",
  "residual_subgroup": "H | null",
  "orbit_bound_satisfied": true,
  "composition_cocycle_verified": true,
  "independent_transport": "unproved",
  "state_fibre_faithful": false
}
```

## Deutschian explanation

A reference does not add generic information. It breaks a particular symmetry.
Its capacity is measured by how many formerly equivalent frames it can separate.
One bit can say that a trusted origin was lost; more information is needed to
say where the frame moved.

Even a perfect frame label does not describe the object carried in that frame.
The origin, the displacement, the path, and the fibre state are different
explanatory variables and require different constructors.

## Claim boundary

This packet proves finite capacity bounds for origin detection, quotient-frame
identification, and full torsor identification. It does not derive a physical
reference, continuous precision bound, or faithful observation of the state
fibre.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was to quantify what an independent reference
can and cannot recover.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Reference capacity now separates departure detection,
frame identification, history sensitivity, and fibre-state reconstruction.

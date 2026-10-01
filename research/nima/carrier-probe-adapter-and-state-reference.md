# Carrier probe adapter and the state-reference obstruction

## A concrete adapter from the existing probe construction

Label the twelve S12 fixed-label probes by the actual directed arrows
Omega={(i,j):i!=j} of the four-point carrier. S4 acts on Omega by permuting both
endpoints, giving a specific inclusion S4->S12. Restrict the probe functions
along that inclusion:

    f_(i,j)(g)=1 when g(i)=i and g(j)=j.

The checker verifies equivariance under every carrier relabelling. This is an
explicit primitive-feature adapter. Identifying it with the intended full rung9
transport still requires a record/presentation interpretation; matching a rank
to a rung number alone does not supply that identification.

## What restriction forgets, and what retention restores

Opposite directed arrows have identical restricted probes. Their span has rank6.
For source coefficients x_(i,j), the observed coefficients are

    z_{ij}=x_(i,j)+x_(j,i).

Keeping the six antisymmetric coefficient directions restores every source
coefficient exactly. These six probes fix both endpoints; they are not setwise
edge-stabilizer probes, which would also count endpoint swaps.

The four state probes p_i(g)=1[g(i)=i] are independent of that six-dimensional
span. A3-cycle fixes one state but no directed arrow, so no combination of the
restricted arrow probes can reconstruct the point probe on that permutation.
Together the arrow and state probes span ten dimensions. Thus this adapter
needs the state branch to reach a state-reference observation; arrow data alone
cannot generate it.

## The source metric does not transfer by a scalar normalization

The existing normalized S12 source Gram is10I12+J12. After splitting symmetric
and antisymmetric coefficients,

    ||x||^2_source = z^T(5I6+J6)z + 10||x_hidden||^2.

Uniform counting on the actual S4 carrier gives the restricted six-probe Gram
I6+J6 instead. The common-direction norm ratio is11/7 and the contrast ratio is5.
A single overall rescaling cannot make the two visible metrics agree.

For the state probes the same counting measure gives4I4+2J4, or2I4+J4 after a
single division by2. Cross inner products between an endpoint-fixing arrow probe
and a state probe are2 for an endpoint of the arrow and1 otherwise. All blocks
therefore belong to one explicitly computable common Gram; they cannot simply
be assigned independent orthogonal costs under this realization.

## Lift to the137 counted slots

On S4 x S4, use tensor products of the selected eleven arrow probes and tensor
products of the four state probes. There remain121+16 distinct record slots.
Their observed ranks are36 and16, with total52. Hence85 coefficient directions
are invisible to this particular slot observation. Removing the counted reference
arrow does not remove its reverse's identical endpoint-fixing probe.

The squared norms under unnormalized product counting are4 for each arrow slot
and36 for each state slot. Cross-block overlaps take values1,2,4. These are probe
counts, not gauge multiplicities or physical coupling predictions. Equal slot
weights are a separate normalization assumption if this is the chosen physical
observation model.

A second concrete probe choice, t_(i,j)(g)=1[g(i)=j], distinguishes direction.
It has primitive rank9, and the corresponding121+16 slot observation has rank88.
Thus the record count137 is stable while observable rank depends on the probe
construction. Neither probe choice is identified here with the existing finite
matrix assembly without an additional response adapter.

## Attempting to reconcile the metrics exposes a state-sector freedom

A conjugation-invariant nonuniform carrier measure can realize the transported
arrow metric5I6+J6: assign weight1 to the identity and5 to each transposition.
Arrow probes vanish on3-cycles, so their common weight gamma remains undetermined.
The resulting state Gram is

    (10+2 gamma)I4+6J4.

Two positive gamma values preserve the same transported arrow metric but give
different state metrics, even after a common-state reference is unit-normalized.
This measure is an added choice; literal uniform carrier counting gives the
previous raw Grams. The test does not alter counting measure silently to preserve
an assumed source normalization.

## Synthesis result

A natural restriction adapter has been constructed and its retained kernel is
explicit. It supplies neither an isometry for the existing S12 Gram nor a state
reference from arrow probes alone. The next adapter must include the state branch
and choose which carrier probes/readout actually represent the comparison maps.
The original S12 Gram, uniform S4 counting, and arbitrary physical normalization
cannot all be treated as the same metric without that construction.

The physical reference locus remains rung4. Its state-space/probe realization
and metric must be attached to the confirmed transport diagram explicitly. The
ranks6,9,10,52 and88 belong to the stated probe spaces; they are not inferred
identifications of tower roles or numbers of independent physical fields.

## Verification

    python research/nima/checkers/check_carrier_probe_adapter.py

All24 carrier permutations, exact probe ranks, reversal kernel and reconstruction,
a3-cycle obstruction for state reconstruction, source/target Grams and norm split,
the121+16 slot tensor models, cross-block overlaps, and two positive measures
with equal arrow Grams but different state Grams. Rational arithmetic throughout.

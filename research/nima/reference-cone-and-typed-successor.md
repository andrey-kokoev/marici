# Reference cone and the typed successor

## Fix the literal promoted object

The promoted object is a retained family, with one fresh label per incoming
family. The137-slot fixture therefore supplies32 promoted records. Each record
retains its member IDs, assembled response C_F, direct reference d and residual.
This follows the stated family-promotion signature without adding family pairs
as new promoted objects.

To test a higher-cell interpretation, regard C_F and d as parallel1-maps A->B.
The comparison boundary has the form

    sigma_F : C_F => d.

The checker retains that boundary specification with each family record. Naming
a formal comparison boundary is distinct from realizing a physical or algebraic
filler for it.

## Common target does not give parallel higher endpoints

Two2-cells can be endpoints of a3-cell only when their1-source and1-target agree.
Here sigma_F and sigma_G share target d, but generally have different sources
C_F and C_G. In the32-record generic fixture, all992 off-diagonal pairs fail
this parallelism condition. Only the32 diagonal pairs directly form admissible
higher endpoint types.

Grouping all these records by their common target remains a valid record-family
operation. It does not make their comparison boundaries parallel or change their
cell degree. Averaging the scalar residuals likewise stays in the original
linear response space.

## Explicit alignment

Supply a source connector

    a_FG : C_F => C_G.

Then a_FG followed by sigma_G and the direct sigma_F are parallel2-cells, giving
a well-formed prospective3-cell boundary:

    K_FG : sigma_F === (a_FG followed by sigma_G).

All1024 ordered family pairs become typeable after this alignment. The connector
and realization of K_FG are now explicit parts of the successor contract.

The existing residual values provide an additive realization of connector data:

    rho_F=C_F-d,
    a_FG=C_F-C_G=rho_F-rho_G.

Its composed response is a_FG+rho_G=rho_F. Every resulting scalar boundary
discrepancy is exactly zero. This verifies consistency of the alignment while
leaving the higher witness itself unspecified.

## Connector abundance is not operand independence

Include the32 assemblies and the reference as33 objects. There are1089 ordered
connector labels. Their additive values u-v depend on32 independent scalar
differences; a common translation of all33 potentials is invisible. Fixing the
reference removes that translation freedom. All triangle equations

    (u-v)+(v-w)=u-w

hold exactly. Thus reference-derived all-pairs connectors are determined by the
original spokes. They do not supply the independent product operation used in
the candidate1,2,4 homology recurrence.

If these connectors are normalized to one arrow per ordered endpoint pair, they
form a thin reference groupoid. Retaining distinct path histories or additional
filler states is another construction and needs its own equations.

## The next constructor is now localized

A type-ascending successor requires:

1. a connector/alignment law between assembled responses;
2. an actual filler type for the aligned comparison boundary;
3. a rule selecting or retaining its admissible witnesses and costs.

The additive difference connector is a concrete coherent option, but its
boundary discrepancy vanishes. A minimum-norm filler for zero boundary, starting
from zero, is zero under a positive cost. Nontrivial retained higher data would
come from specified history, kernel modes or other witness input. The dimension
of those choices must be computed from the filler operator, rather than assigned
by the number of endpoint slots.

This specifies the missing type-ascending step more tightly than an arbitrary
choice of next-level labels. Family retention, endpoint alignment and filler
realization are separate operations with different input/output types.

## Verification

    python research/nima/checkers/check_reference_cone_successor_typing.py

Checks32 retained families covering all137 slots, parallel-endpoint typing,
992 rejected raw higher comparisons,1024 aligned boundary specifications,
all33^3 additive connector triangle identities, and rank32 of the1089 connector
values. The test uses a rational scalar response channel and formal globular
boundary records. It does not instantiate a higher filler or assert a new gauge
identification.

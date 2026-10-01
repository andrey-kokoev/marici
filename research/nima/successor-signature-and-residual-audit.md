# Successor signature: retained families, comparisons and residuals

## Source contracts being tested

The architecture in docs/system-characteristics.md specifies

    groups = summarize(records, grouping_keys, retain_members=True)
    next_records = addcolumn(groups, label, unique_index).

It explicitly gives one fresh label per retained family. The earlier retained-
total fibration construction in label-from-to-fibration-tower.md preserves the
original record type up to reconstruction; the clarified grouped-record rule
adds family identities. Neither declaration supplies all next-level endpoint
fields.

The comparison specification in docs/theory-page.md states that the assembled
comparison is assessed against the direct relationship and its residual supplies
proposed next-level coherence data. The checked assembly makes this

    C,d in Hom(A,B),   rho=C-d in the same linear map space.

Its implementation keeps all137 comparison slots and the direct reference.

## Apply the residual-enriched rule twice

Attach to each promoted family its weighted assembly, retained direct reference,
residual, mass and complete member records. Use two endpoint policies:

1. Reference-target: its from-field identifies its assembly and its to-field
   identifies the common retained direct reference.
2. Inherited-key: its from-field identifies its assembly and its to-field
   injectively encodes the incoming grouping key.

Both satisfy one-label-per-family promotion, exact member reconstruction,
C=d+rho, transported member weights and the global reference/residual equation.
Repeated incoming promotion gives different next levels:

    reference-target: 137 ->32 ->1,
    inherited-key:    137 ->32 ->32.

These are concrete recursive record models satisfying the stated data-retention
and residual contracts. Their difference proves those contracts do not determine
a unique successor endpoint rule. The scalar aggregation in the checker is a
channel in a common linear map space; neither model claims to construct a new
higher-morphism type merely by wrapping that payload.

## Residual bookkeeping supplies no new free operand

For two independent2x2 matrices C,d, the decorated record(C,d,C-d) has eight
independent scalar parameters, the same as(C,d). Fixing d leaves four. Repeated
retention of the residual preserves that rank. Projection onto(C,d) is an inverse
to graph decoration, so the result holds beyond counting stored coordinates.

A genuine additional coherence witness can carry extra choices, but its type
and boundary equation must be supplied. For example, a filler K with
boundary(K)=C-d is different data from the already computed value C-d. Its
existence and ambiguity depend on that boundary map. They do not follow from
renaming the residual as a higher record.

## Independent comparison changes the constructor signature

There are32 incoming families in the137-slot fixture. Literal promotion creates
32 new records. Independently pairing those families creates32^2=1024 ordered
pair objects. The latter is a separate comparison operation after promotion.

The previously checked fibre law

    (q x q)^-1(v,w)=q^-1(v) x q^-1(w)

shows that this added operation is compatible with grouping. It does not identify
a family with a pair of families or derive the operation from fresh labelling.
The product-based b2=1,2,4 recurrence therefore remains a property of the added
independent comparison constructor.

Comparison also needs a type: comparing arbitrary records, composable arrows,
or parallel arrows gives different domains. In the endpoint-unique11-arrow
primitive relation, parallel-arrow pairs number11, while independent ordered
pairs number121. In the separate matrix assembly all output maps already have
the common type Hom(A,B); this distinction must be handled by its carrier adapter.

## Precise missing constructor

The next-level record must specify all of:

- whether its identity labels one retained family, a pair of families, or an
  additional comparison/filler witness;
- the type of each next-level endpoint and its construction from retained data;
- whether a residual is merely stored payload or a boundary requiring a witness;
- the admissible comparison domain at the next step.

Only after this signature is fixed can iteration test the tower's actual
successor. The audit excludes the inference that retention plus a computed
residual forces relational squaring. It leaves the verified product construction
available as an explicit architectural extension.

## Verification

    python research/nima/checkers/check_successor_semantics_audit.py

Both residual-enriched endpoint policies are applied twice. Checks cover all
original rows, member masses, weighted assemblies/residuals, one-label-per-family
cardinality, residual-graph parameter rank, and independent versus parallel
comparison domains. These are finite countermodels to uniqueness of the
successor under the stated contracts.

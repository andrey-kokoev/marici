# Repeating promotion: singleton obstruction and a next-level prediction

## Match the stated tower schedule

Each triple presents the same record table in three ways: individual labels,
source-indexed records, and target-indexed records. Both tower transitions
10->9 and7->6 promote the grouped records at the target-indexed presentation.
Therefore a candidate generator must apply the same incoming-family promotion
twice. The previous transaction fixture used source promotion followed by target
promotion; that fixture established update coherence for its schedule.

This test follows the tower schedule directly. Start with the137 retained slot
records, form every incoming family, give it a fresh ID, retain its full children,
and assign source/target endpoints by the same footprint policy at every level.

## General obstruction

Let t:E->V be the current target map. A nonempty incoming family is
F_v={e:t(e)=v}. Its child-target footprint is exactly the singleton {v}.
Under the footprint policy the promoted target is an injective encoding of {v}.
Different incoming families therefore have different promoted targets.

Consequently grouping the promoted records by target yields only singleton
families. The next promotion adds wrappers but does not change the partition
of original leaves. This argument repeats at every further level.

More generally, any promoted target that injectively encodes the incoming
family's grouping key has this property. Obtaining a genuine next-level incoming
family requires a target construction that can be shared by distinct current
families, or a different operation/schedule.

## Executable prediction

With the same footprint rule repeated, record counts are

    137 -> 32 -> 32 -> 32.

After the first promotion, every subsequent family has one child. Its original
leaf support, mean readout and minimum-change return remain those of the first
family. The per-triple readout count stays32. Record nesting depth grows by one;
there is no doubling of a structural quantity in this construction.

This is the next-level prediction of the current rule: singleton wrappers.
It rules out this rule as an explanation of a nontrivial family-of-family
progression with doubling degrees of freedom.

## Coherence alone does not select the missing rule

A control assigns one common target endpoint to every promoted record while
retaining all child records and their actual endpoint data. Repeating that
policy yields

    137 -> 32 -> 1 -> 1.

Both policies reconstruct every original leaf, transport member-count weights,
and give equal direct/staged mean returns. The coarser policy loses distinctions
in its endpoint interface but preserves them internally. The existing tests
admit it because they do not require a faithful semantic interpretation of the
promoted endpoint. Thus those tests alone cannot select the tower generator.

## Structural synthesis consequence

Fresh labelling and retained grouping suffice for coherent recursive storage.
They leave the relation BETWEEN promoted families unspecified. That relation
must supply shared next-level endpoints if successive incoming promotions are
to produce genuinely new families.

The next construction should start from source/target family incidence—what
relations connect one retained family to another—and define promoted endpoints
from that relation. Its first obligation is to produce non-singleton second-level
fibres without changing the rule between cycles. Then identify a structural
quantity and derive its recurrence. The proposed1,2,4 superscripts remain an
open target; leaf counts, mean counts and wrapper depth here do not supply it.

## Verification

    python research/nima/checkers/check_recursive_tower_generator.py

Checks three successive applications, both source/target view reconstructions,
complete descendant coverage, leaf-weighted mean composition, direct/staged
mean returns, singleton wrapping, and the coarser endpoint control. Exact
Fraction arithmetic. The general singleton obstruction has the proof above.

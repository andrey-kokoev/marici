# Re-rooting versus recovery of retained operands

## Result

For the existing candidate information operations, **every compatible full-state relation row uniquely determines any missing port**. This remains true after gluing a comparison into reconciliation, and local staged recovery agrees with whole-composite recovery.

However, reverse recovery uses operand histories already stored in the full output. Hiding those histories gives an explicit ambiguity. Also, interpreting the other ports as execution outputs requires reversed interfaces not present in the fixed incoming reading. No native inverse command is supplied.

Thus the result separates three claims:

1. Full retained data permit reconstruction: **yes**.
2. Record/attachment observations alone determine exact missing provenance: **no**.
3. Any boundary port can serve as an admitted native execution output: **not established**.

## One relation, not fitted inverse maps

Fix `reading:0:-1` and each of its four sign bindings. Select the P/P-at-E+ comparison C and the P/P-at-E- comparison B. The composite is

```
A1 ----\
        C ----\
A2 ----/       R ---- O
B ------------/
```

Here A1 and A2 are actual channel operand packets, C and B are actual comparison packets, R is the reconciliation operation and O its retained result.

Construct the local relations only by calling the existing constructors:

```
C_relation = {(A1,A2,C) : C = compareAt(A1,A2)}
R_relation = {(C,B,O) : O = reconcileAt(C,B)}.
```

All packets retain their occurrence, physical reference attachments, payloads and original constructor trees. The C input-slot order is fixed. At R's comparison ports, both orders of their retained channel children are represented, because the current comparison constructor admits both and preserves the distinction.

Per sign binding, Boolean enumeration yields:

- 8 distinct comparison rows;
- 64 distinct reconciliation rows;
- 32 composite rows after matching the **full** internal C packet.

The single composite relation is obtained by gluing these local relations. Each re-rooting test asks for one missing component of that same relation, not for a separately chosen inverse function.

## Recovery and gluing

Local tests choose each of the three ports as missing. For the composite, all four external ports are tried.

Examples:

- Missing O: recover C from A1,A2, then O from C,B.
- Missing B: recover C from A1,A2, then B from C,O.
- Missing A1: recover C from B,O, then A1 from A2,C.

Every staged result equals the result of a direct query to the composite relation, including its complete retained history and attachment fields.

Fresh checks:

- **864 local missing-port recoveries**;
- **512 composite missing-port recoveries**;
- **512 staged-versus-composite gluing squares**;
- **128 exact reconstructions through the previous rooted-gluing adapter**.

Uniqueness is asserted only on compatible inputs. The local-domain census also queries incompatible pairs: for example, at C there are 16 possible Boolean input pairs but only 8 admit an output. Changing the designated missing port does not make all supplied data admissible.

These are finite executable results. Structurally, the easy direction is explained by the original constructors: the full output explicitly retains its inputs. The experiment does not treat that explanation as independent evidence of physical reversibility.

## A genuine loss-of-provenance counterexample

Hold A1 and A2 fixed. Take two valid B comparison nodes that have identical records and reference attachments but reverse the order of their two retained channel children. The existing `compareAt` constructor produces both.

The corresponding full outputs O differ, because each retains its actual B child. But their record/attachment headers agree. Therefore

```
(A1, A2, header(O))
```

has two possible answers for the missing **full** B operand. The receipt exhibits both actual nodes, not just differently tagged copies.

There are 16 ambiguous such queries per binding. Every ambiguity disappears when the complete O tree is provided, since B is retained inside it.

This refutes exact provenance recovery from the reduced observations. It does not refute recovery of B's record dictionary, or a separately declared theory that intentionally quotients operand ordering. Our current task promises retention rather than such a quotient.

## Attachment is a separate gate

The source comparison-domain builder orients actual shared interfaces according to the fixed reading. All forward wires of the tested tree are present. Their oppositely directed wires are absent from that reading.

Choosing A1 or A2 as execution output would reverse two internal interfaces along the path from O; choosing B reverses one. Those reversed steps still connect geometrically adjacent cells, but the fixed directed domain supplies no such forward arrows. The original O-root requires no reversal.

This does not prove that the wider geometry cannot support a richer root-changing grammar. Nor does the presence of a forward incidence arrow itself provide a native comparison map: the underlying physical operation bindings remain open. The audit records the exact reversed interfaces and leaves `nativeRerootOperation` null for every root.

The opposite global reading is not automatically an answer: re-rooting at one chosen boundary reverses the path to that boundary while retaining other branches, rather than reversing every arrow of the whole carrier.

## Relation to cyclic operads

Unique deterministic recovery from the other ports is a stronger proposed interface property, not a defining axiom of every cyclic operad. These finite relation tests alone do not supply:

- an involution on port colors;
- coherent cyclic/symmetric actions on operation profiles;
- units or arbitrary composition closure;
- a native meaning for newly designated output ports.

Consequently, the result is not a cyclic-operad construction. It is a useful prerequisite audit: full retained states support algebraic recovery compatible with gluing, whereas native attachment and reduced-history sufficiency are separate questions.

## Reproduction

```
node research/strominger/checkers/check_su32_rerooting_and_gluing.mjs
```

Receipt: `results/su32-rerooting-and-gluing-v1/verification.json`, containing the domain censuses, exact ambiguity witness, per-root interface reversals and source hashes.

Fresh headless execution passed. Existing operation and geometry implementations were not modified. No circle action, native inverse, physical evolution or higher filler was introduced.

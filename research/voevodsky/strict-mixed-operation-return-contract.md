# Shared completion contract for strict mixed set operations

Status: original fixed-signature specification; now implemented in `checkers/strict_set_program.py`. See `strict-mixed-program-theorem.md` for the consolidated written theorem and its assurance limits.

## Common Hoare-style boundary

Each operation receives a fully materialized finite support word at a linear input and completed unary index/literal operand. Its result continuation and acknowledgment continuation are distinct external ports; a query additionally receives an OUT port. Neither continuation consumes a result before DONE. Prior Boolean snapshots are closed components. A successful operation returns a complete support word, its specified optional Boolean, exactly one DONE, and no owned control, budget or garbage. Unconsumed suffixes become part of the returned word rather than garbage. External dormant gate operands are not operation-owned work.

Completion is not defined as globally removing all agents: the result data and future operands remain. No host scan is an enabling condition. The contract assumes completed inputs; it does not apply to general prefix-demand pipeline streams.

## Return-bearing insertion

Use distinct annotated agent kinds ABc(p,a,r,c), ASc(p,a,r,c), ARc(p,r,c), avoiding a variable arity for existing AB/AS/AR. ABc--K/N and ASc--B/N have the previous insertion connections plus old c to successor c. ARc--B/N writes the final B1 and retained suffix as before, and attaches fresh DONE.p to the outside c peer. No successor control remains. Since saved support is a complete chain and all i budget units were consumed, immediate DONE is sound. There is exactly one c owner until the final step, then exactly one DONE. Count remains 2i+2; no extra reduction is needed to emit DONE.

## Return-bearing union

Use ULc/U0c/U1c(p,a,r,c). Nonterminal ULc--B and U_bc--B forward c to their successor controller. ULc--N performs the existing a-to-r outside splice and additionally emits DONE at c. U_bc--N emits the remembered bit with the saved left suffix and DONE at c. Both input tails are complete at entry; termination consumes one NIL and returns the other remaining suffix. Thus there is no pending producer behind the forwarded suffix and no garbage requiring EA. Counts remain 2n+1 for n<=m and 2m+2 otherwise.

For union, the two splice boundary peers are distinct and lie on independent linear result/input paths. Adding the passive c path may form a context cycle but does not identify the actual peer ports. The same cut-interface method, rather than whole-graph forest reasoning, applies.

## Gate variants

All gates await DONE at principal p. Every other port is auxiliary and therefore cannot independently enable the gate.

* GM(p,s,r,b,o,c): existing query gate. Release creates COPY and return-bearing query with s as support, b as budget, r as retained continuation, o as OUT and c as acknowledgment continuation.
* GA(p,s,r,b,c): release creates ABc, with p at budget b, a at support s, r at result continuation and c at acknowledgment continuation.
* GU(p,s,r,b,c): release creates ULc, with p at support s, a at literal b, r at result and c at acknowledgment continuation. The implementation uses b for both budget and literal operand ports.

Each gate consumes its preceding DONE; each external slot is used exactly once. The operation kinds and gate arities form a finite signature independent of program length. Empty strict programs can supply an initial DONE; placing every instruction behind a gate then costs one gate rewrite per instruction, unlike the earlier convention that starts the first query directly. The implementation must state which convention it adopts.

## Composition proof

Induct on the list of dormant gates. Before the first gate receives DONE, all later gate principals face auxiliary c ports, so no later instruction can start. Upon release the completed support and literal/budget meet the local operation's precondition. The operation-specific proof gives its postcondition: for membership the EA/NIL argument includes cleanup, while insertion/union retain complete suffixes and create no garbage. Their c paths forward linearly and end in one DONE. This restores the common precondition for the next gate. Earlier OUT snapshots remain untouched. Induction establishes strict order and sequential set semantics, assuming faithful implementation of the new return-bearing rules.

The immediate next task is implementation plus mixed-program tests against this specification, not further acknowledgment topology design. Include empty support, zero index, unequal union lengths, previous query snapshots, and no-overtaking checks under random individual scheduling. Specifically test that DONE is absent while any operation-owned controller remains. This is not a claim that arbitrary imported or concurrently used streams satisfy the completed-input precondition.

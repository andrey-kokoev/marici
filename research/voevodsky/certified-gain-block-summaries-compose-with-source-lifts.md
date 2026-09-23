# Certified gain-block summaries compose with source lifts

## Delivered composition gate

The balanced-gain controls now have an executable two-block decomposition, rather than only two elimination orders on one global graph. Each block computes its own exact difference-bound interface. The block interiors do not overlap; all shared nodes are explicitly retained in both interfaces, including the zero anchor. Both use the previously certified global coordinate chart.

Union the block interface rows, close that small relation, and project to the public endpoint nodes. For m=4,8,16, every resulting interface distance equals the corresponding globally eliminated distance. Independent replay certifies six blocks and three composed interfaces.

## Witness gluing

An admitted public endpoint assignment is first extended to the shared interface using the composed distance relation. Each block then extends that interface assignment independently by

    z_v=min_a (z_a+D_block(a,v)).

Both block extensions fix all shared nodes, so they glue to one source vector. Multiplying by the certified scales gives a raw atom assignment satisfying all original caps and gain constraints. Six such glued source lifts pass independent verification.

The general reason is exact relational projection with all shared variables retained. Source-relative block fillings can be chosen independently only after their common interface values have been fixed. Dropping a shared coordinate prematurely would remove the condition needed to glue the witnesses.

## Proof boundary

The verifier freshly replays the parent balanced-gain certificates. For each block it reconstructs the expected edge subset, checks original-row coverage, exact path witnesses and triangle closure. It checks that every node shared between blocks appears in both interfaces. It reconstructs the merged relation from the certified summaries, verifies its closure, compares with the independent global certificate and checks the assembled source witnesses directly.

This is not a test that two arbitrary selected section points agree. It constructs witnesses to a jointly fixed interface and verifies that their union is admitted. Different choices inside block fibers would also glue if they fixed the same shared interface and obeyed their block constraints.

## Cost and scope

The interfaces have three and four nodes, and the composed public relation has three. Thus these controls exercise small separators even as the source grows. The prototype still materializes dense block closures and migration proofs. It establishes compositional correctness, not optimal runtime, minimum proof storage or a general variable-audit optimizer.

The observer remains selected raw atoms; arbitrary moment evidence need not lie in the balanced-gain class. Re-exposing retired coordinates still requires retained fine information. No source authentication, upstream admission replay or owning API modification is claimed.

## Reproduction

    python research/voevodsky/checkers/check_composed_gain_blocks.py
    python research/voevodsky/checkers/verify_composed_gain_blocks.py

Requires `results/balanced-gain-elimination.json` from the preceding controls.

Artifacts:

- `results/composed-gain-blocks.json`
- `results/composed-gain-blocks-verification.json`

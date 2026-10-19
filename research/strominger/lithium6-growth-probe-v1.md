# Lithium-6: frozen-rule growth probe

Next element: lithium. The target here is its lightest stable isotope,
**Li-6: 3P/3N/3e**. This is an extension test from the retained He-4 core,
not a new layout or an admitted lithium viewer construction.

**Follow-up:** the [whole-assembly NN trial](lithium6-whole-assembly-v1.md)
relaxed these assumptions, but its claimed admission has since been withdrawn
for phase-discipline failures; see [the phase audit](phase-discipline-audit-v1.md).
The corrected [phase-first reference model](phase-first-assembly-v2.md) instead
searches the whole assembly with explicit phase-advance witnesses. This older
negative result remains scoped to its frozen retained-core grammar.

## Frozen assumptions

- Keep all six He-4 carriers, their geometry, and global C/M identities.
- Admit new nuclear attachments through the current PN interfaces: a full
  **MCM** face. A neutron's remaining **MCC** faces are the native NE interfaces.
- Allow both proton-reader alternatives at each proton: four combinations,
  with reference circuit orders 3, 2, 2, 3. Do not choose by desired outcome.
- Do not independently seed another packet and assert that it is glued in.
- Do not relabel C as M, change existing particle roles, or add an NN/PP law.

## Result: blocked before a new nuclear carrier

The retained cells are **0, 13, 16, 24, 14, 7**. Their nuclear incidence is

```
P1 — N1 — P2 — N2 — P1
```

Every nuclear carrier has exactly two MCM faces. All eight such face incidences
are occupied by the four existing PN interfaces. There is no free nuclear
port at which to add P3 or N3. This is a finite face audit, not a search that
merely timed out or missed a distant placement.

N1's two MCC ports already lead to E1/E2. N2's two free MCC ports lead to
additional electron cells **6 and 8**, obtained from the native window
constructor. Adding one could supply the third electron count, but cannot
supply the missing proton or neutron, or free a nuclear port. Electrons are
terminal under the frozen rules.

Both proton-reader choices use the same MCM face sets; changing their orders
or clock sheets does not free those faces. **All four alternatives are blocked.**
The ambiguity is therefore **not resolved** by this test. It exposes a missing
extension rule earlier than a new holonomy compatibility test can occur.

## Limits and next question

This does not show that lithium is impossible, or that a fresh Li-6 assembly
cannot exist. It only excludes monotone, face-connected nuclear growth from
this saturated retained core using the declared PN/NE rules. It also blocks
the first nuclear addition needed for retained-core Li-7 growth, although a
separate Li-7 construction was not attempted.

To continue, we must explicitly investigate a change of scope: a different
core assembly, rearrangement, or another admitted nuclear interface (for
example NN). Such an interface would need a geometry and full-carrier transport
rule justified independently of the desired lithium count. Adding a convenient
context map or an independent deuterium packet would not itself establish a
connected, compatible lithium construction.

This frozen-rule probe alone does not admit a lithium selector or geometry.
The separate whole-assembly trial explicitly changes the grammar. The He-4
reference trial remains unchanged for its default marking.

## Verification and corrected seed-marking coverage

While running this probe, the earlier He-4 marking sweep was found to be
ineffective: it supplied `bindings`, but `createHelium3Tunnel` ignored them.
That constructor now forwards `seed` and `bindings` to the native constructor;
tests assert the resulting initial binding dictionary before proceeding.

With the fixed octahedral subdivision, **8 of 24** seed markings admit the
retained second regular proton. The other **16** are rejected, rather than
silently replaced by the default marking. The earlier all-24 construction
claim is withdrawn. The default He-3/He-4 construction is unaffected.

For each of the eight admitted markings, the Li-6 audit checks nine character/
phase inputs with nonzero complementary coefficients and all four reader
alternatives: **288 variant cases**. It checks the 16 nuclear faces, four
occupied PN interfaces, two genuinely free NE continuations, retained geometry
and bindings, input immutability, and absence of any fabricated lithium commit.
The result is geometric; successful phase cases do not constitute an additional
physical admission argument.

- Model: `demos/particle-overlap-tetrahedron/lithium6-growth-probe.mjs`
- Check: `node research/strominger/checkers/check_lithium6_growth.mjs`
- Full suite: `node research/strominger/checkers/check_fiber_space.mjs`
- Evidence: `results/lithium6-growth/probe.json` and `verification.json`
- Corrected He-4 evidence: `results/helium4-window/verification.json`

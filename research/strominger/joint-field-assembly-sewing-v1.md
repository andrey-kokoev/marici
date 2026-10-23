# Sewing the existing joint field on a retained native assembly

## Prior research corrected the starting point

The prior [full-five joint-field candidate](full-five-channel-candidate-v1.md) already supplied:

- an explicit global36-component PN map, with the native five-slot permutation;
- a44-channel N/E exchange preserving the full reference, not only E's rank-two return;
- path-dependent coefficient bindings;
- a checked order-five comparison between two native histories.

The [extended field-frame audit](geometric-context-and-extended-coherence-v1.md) checked250,040 packet/frame states through depth28, but explicitly left simultaneous assemblies and their incidental contacts unresolved. The [full-field path result](full-field-path-coherence-v1.md) explains why freezing the coefficient bindings is wrong. The [face-extension obstruction](global-PN-NE-extension-v1.md) also rules out demanding that the chosen six-component face be an isolated preserved block of the full PN map.

Therefore the next test is not another invented field kernel or a new endpoint isometry. It is sewing this existing candidate over a genuinely retained native assembly. The full-five checker was freshly replayed; all directly pinned inputs of the imported candidate receipts were checked against live hashes. The old depth28 search was inspected, not rerun or enlarged here.

## The assembly

Take both histories of the existing order-five native coefficient comparison. Retain their complete union, then append the native PN,NE exit to each endpoint.

The unchanged native assembly validator certifies:

- two P bodies, two N bodies and one E body;
-14 retained packet presentations;
-18 actual retained operation interfaces;
- two terminal E packet histories;
- all contacts witnessed, no pending contact, and every retained packet able to reach an exit.

The checker uses **all18 interfaces**, not just the edges selected while generating the two paths. Histories remain ordered records; equal endpoint charts are not used to erase them. Retained packets are construction maps, not independently cloned physical particles.

## Constructed whole-field section

Use a single arbitrary44-coordinate root field z. Every retained packet h has an invertible metric-isometric frame U_h, constructed from the prior maps:

    P frame: geometric P-reader parity;
    N frame: global PN map after that P frame;
    E frame: joint N/E exchange after the N frame.

All36 baryon coordinates and all8 joint E coordinates are retained. In the ordered-corner convention, N-reader and NN transport are identity maps on co-moving field coordinates; their context and native coefficient actions are not discarded.

Set

    x_h = U_h z.

This is one compatible whole section, expressed in14 charts—not14 unrelated fields. Its metric is inherited from z rather than obtained by summing14 copies of its norm.

On every retained native edge e:s->t, the actual candidate map satisfies

    U_e U_s = U_t

on **all44 coordinates**. Thus the local transports sew. General comparison maps

    C_(s,t) = U_t U_s^-1

obey the cocycle law by cancellation. A mixed P/N/E comparison triangle is also checked directly using exact factor operations. Each chart reconstructs the same arbitrary root field.

## The required readout square now passes

Let B0 embed the five native root coefficients into the44-channel root, and let Pi_h be the actual retained five-slot permutation of packet h. Define

    B_h = U_h B0 Pi_h^-1,
    R_h = B_h^sharp.

The sharp is the metric adjoint. The candidate obeys both

    U_e B_s = B_t Pi_e,
    R_t U_e = Pi_e R_s.

The second identity holds on the **entire44-dimensional field**, not merely for one sample vector. It is the desired finite-assembly statement: transport first and then read the target window, or read the source window and apply its native operation—the answers agree.

These bindings are the prior frame-propagation construction, not independently derived geometric couplings. Their unrotated PN and NE restrictions are checked against the previously stored embeddings rather than refitted.

## Histories and E outputs survive

The two order-five histories yield the same candidate physical field map at their shared P chart but different native coefficient permutations and different B_h. Both remain present in the sewn assembly.

At each E exit, the prepared five-dimensional input splits into:

    two independent E directions + three retained baryon directions.

Exact complementary Gram projectors have ranks2 and3 and sum to the five-dimensional identity. All five coefficients are recovered; no attempt is made to squeeze them into E's rank-two return alone. The other39 dimensions of the full44-channel root are also transported invertibly, though they are absent in the chosen native five-dimensional preparation.

## Controls and computational method

Freezing the canonical, untransported binding fails at11 of the14 packet presentations. Replacing PN transport by identity also fails. These controls show why matching endpoints or using one fixed local binding is insufficient.

The PN matrix has entries with up to72 multiradical terms. A first dense-product implementation timed out. The completed check instead reuses its original12-by12 and3-by3 factorization, checks reconstruction of every stored PN entry, and proves full isometry from exact factor identities. The joint NE exchange similarly uses its orthonormal rank-two factors. No floating-point substitute was introduced.

## Result and boundary

**Positive result:** the previously declared joint-field candidate extends consistently over this certified five-body assembly, including both comparison histories and both E exits. The required local-to-whole readout squares hold exactly.

This is connection gluing over retained contextual charts. It is not a claim that raw coefficients on one fixed geometric face agree before and after PN; the prior face-block obstruction remains valid. It does not yet provide independent physical face readouts, every analytical esd7 witness, all possible assemblies, or an autonomous whole-state update and clock. Those obligations must not be silently folded into this positive bounded result.

This is a more source-faithful starting point for global evolution than the unrelated scalar Gaussian candidate: the native local maps are now actual restrictions of one compatible field description on a nontrivial retained assembly.

## Reproduction

```sh
node research/strominger/checkers/export_joint_field_sewing_fixture.mjs
python research/strominger/checkers/check_joint_field_assembly_sewing.py
```

**18 exact checks passed.** [Native fixture](results/joint-field-sewing-fixture.json); [field-sewing receipt](results/joint-field-assembly-sewing.json).

The receipt contains the exact generators, factored global frames and inverses, all14 bindings/readouts, all18 interface checks, retained histories, exit rank splits and live input hashes. Native constructors and prior field maps are unchanged.

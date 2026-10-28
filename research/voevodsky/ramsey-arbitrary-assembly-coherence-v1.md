# Arbitrary-assembly coherence for the declared joint44 field candidate

Node: `admitted-reversal-overlap-coherence`.

## Theorem and exact scope

**Theorem.** Fix the existing joint44 field generators, the five-column root coupling, the ordered-corner N/NN convention, and the checked N-port map. Interpret the native local geometry rules with exact integer coordinates. For every source-generated retained assembly from any of the24 marked tetrahedral seeds, with no bound on construction length, origin or number of packets:

1. the assigned native field transports admit compatible metric-isometric frames on every retained interface;
2. the history-dependent five-slot bindings and their full-field readouts intertwine on every interface;
3. all induced chart comparisons satisfy identity, inverse and cocycle laws;
4. for every **finite** such assembly with a complete entry/exit certificate, whole-reference reversal and the canonical dual-carrier comparison satisfy the same laws under the stated negative-direction pullback policy.

This proves coherence of the **declared candidate**, not unique selection of its field laws, a spatial-isometry identification of P/E, a new forward E operation, or physical dynamics. It does not turn the operator's Ramsey/native-forcing parent into a proved theorem.

The field-frame argument also applies on the entire infinite generated graph. A whole-boundary reversal of an infinite assembly with unbounded origins would require an additional indexing convention: there need not be a finite common reflection center K.

## 1. The source has a finite local quotient, not merely finite tested paths

For a chart h, retain:

- its species;
- primitive owner kind and inversion flag;
- owner origin and cell vertices;
- every reference alias, including E's extra M2.

Subtract the position of C0 from every coordinate. This defines its translation class t(h). Keep the discarded anchor a(h)=position(C0) separately. Owner information is retained, so a split cell is not confused with an unrelated tetrahedron or subdivision.

The checker starts from **all24** seed markings and repeatedly applies **every** actual outgoing local rule to one representative of each new class. The queue exhausts at

    96 classes = 32 P + 32 N + 32 E,
    160 transitions.

Their kinds are32 PN,32 inverse-PN,32 NE,48 reader advances and16 NN advances. Every target is already in the closed table. A safety cap is present but is not reached; reaching it would reject the closure claim.

### Why this finite closure covers arbitrary paths

This is the essential source-level lemma, not an extrapolation from enumeration depth.

**Translation naturality.** In `makeLatticeItem`, each coordinate is owner-origin plus a fixed primitive coordinate. Translating by an integer vector v with coordinate sum zero translates every vertex/component/face without changing its type. `acrossFace` tests translated equality and derives candidate origins by subtraction; hence it gives the translated unique neighbor. Face incidence, apex selection and geometry classes commute with translation. The local registry/cache only memoizes these geometric answers; it does not impose an occupancy-dependent outgoing rule.

The regular tetrahedron's kind/orientation and vertex set fix its owner. For a split primitive, the unique long diagonal fixes its octahedral center and hence owner origin. Thus the retained owner/cell descriptor supplies the same local neighbor problem, independently of registry IDs. Only equality of IDs is used geometrically, and translation preserves that equality.

**Origin naturality.** The chart constructor and outgoing geometric choices do not depend on packet origin. In phase frames, origin is added uniformly to the named indices. The witnesses test equal/consecutive occurrences; simultaneous origin translation preserves those tests. Reader/NN moves add one and PN/NE moves add zero.

**Coefficient naturality.** The outgoing constructor never branches on coefficient values or the current permutation. It composes a fixed operation permutation with the packet permutation. Packet interning distinguishes these data but does not change the available local geometric rules.

Consequently two packets with the same quotient descriptor have identical outgoing transition descriptors and anchor displacements, regardless of their translation, permitted origin or coefficient history. Every source path therefore projects to a path in the closed table. Induction on path length proves coverage for **all** source-generated packets and edges, without a depth bound.

The source is inspected for this structural argument. As independent regressions, the checker reconstructs every class at four translations, two origins and three coefficient frames:2304 representative cases and3840 edge comparisons pass. These samples check implementation consistency; they are not the all-parameter proof.

The theorem concerns exact-integer rules, or executions whose relevant arithmetic is exact. It is not a statement that overflowing JavaScript Number arithmetic preserves the mathematical geometry.

## 2. The missing global parity invariant

Let b(e)=1 for a P-reader advance and0 for every other native edge. The field model needs a potential p with

    p(target)=p(source)+b(e) mod2.

A potential depending only on translation class does **not** exist: the finite system is inconsistent. Ignoring anchor displacement would therefore produce a false universal argument.

For each quotient edge e:t->u, the closure table retains

    d(e)=a(target)-a(source).

The new exact certificate supplies96 bits c_t and the translation character

    k=(0,1,1,0)

such that **every one of the160 edges** satisfies

    c_u+c_t+k dot d(e)=b(e) mod2.                 (1)

The constants are stored explicitly as `chartConstants` in the verification receipt. They are found by finite GF(2) elimination and then checked independently edge by edge. Erasing k or mutating a chart constant fails. The linear system has rank88; no uniqueness of its solution is needed.

Define on an arbitrary actual chart

    p(h)=c_t(h)+a(h)_1+a(h)_2 mod2,

where coordinates are indexed0,1,2,3. Subtract its value at the chosen seed so that p(root)=0. Equation(1) and source naturality imply the required edge equation on the entire generated graph. In particular any closed actual-chart path has even P-reader parity: both chart type and anchor return, so the potential telescopes to zero.

A translated return can have odd parity. The lattice character accounts for it; it must not be mistaken for an actual closed-chart loop.

## 3. Construct all forward field frames

Let A be the full P-reader involution, P the metric-isometric PN map extended by I8, and W the full joint NE exchange. Put

    F_h = A^p(h)                    for species P,
    F_h = P A^p(h)                  for species N,
    F_h = W P A^p(h)                for species E.

Composition here acts on column vectors from right to left. These maps are invertible and metric-isometric.

For every native edge e:h->j, direct substitution gives

    U_e F_h = F_j.                               (2)

- PN and inverse-PN preserve p and cancel P or P^-1.
- NE preserves p and applies W.
- P-reader toggles p and uses A^2=I.
- N-reader and NN preserve p and use the declared identity co-moving transport.

Those are all source operation cases. The certificate checks both possible parity values on every quotient edge. No further path-length assumption enters.

Full-field isometry of P and W is not inferred from a few prepared vectors: the existing exact generator checker was freshly replayed into an owner-local receipt. It verifies PN's reconstructed factorization and full metric isometry, the geometric P involution, and the orthonormal factors proving the full NE exchange identities.

For any root field z, x_h=F_h z is now a compatible section on every retained interface by(2). Restriction to any retained subgraph, including incidental contacts witnessed by native edges, preserves this equation. If considering disconnected retained components without a shared preparation, one may choose separate root fields per component; the theorem does not manufacture extra equality constraints between independent preparations.

## 4. Bindings and readouts retain all coefficient histories

Let B0 be the unchanged isometric root five-column embedding and let Pi_h be the packet's actual full coefficient permutation. Set

    B_h=F_h B0 Pi_h^-1,
    R_h=B_h^sharp.

The native packet rule gives Pi_j=Pi_e Pi_h. Hence

    U_e B_h = B_j Pi_e.                          (3)

Since the field transport is metric-unitary, taking the appropriate adjoint of(3) gives

    R_j U_e = Pi_e R_h                           (4)

on **all44 input coordinates**. Also R_h B_h=I5.

This is a universal matrix argument, not a rank-only or sample-vector test. The checker additionally verifies coefficient rebasing for every one of120 possible five-permutations against all160 quotient transitions (19200 cases).

Different histories may have the same chart/frame and different Pi_h. Their bindings remain different as required; origin and history are not quotiented by the parity invariant.

## 5. Arbitrary overlap and path coherence

Define the comparison from h to j by

    C_(h,j)=F_j F_h^-1.

Then, identically on the full field,

    C_(h,h)=I,
    C_(j,h)=C_(h,j)^-1,
    C_(j,l) C_(h,j)=C_(h,l).

Every actual edge agrees with this comparison by(2). Consequently every composable path equals the endpoint comparison, and all loops and all higher associativity diagrams agree. This proves arbitrary-assembly connection coherence; enumerating increasingly many triangles is no longer necessary.

This is connection gluing over the declared contextual fields. It is not a theorem that raw pointwise face amplitudes agree under an independently fixed geometric face restriction.

## 6. Whole-reference reversal and canonical carrier identification

For any finite certificate choose K to be the maximum retained reference/phase index. Reflect all occurrences by

    J(role,i,vertex)=(opposite(role),K-i,vertex).

The dual packet origin is K-r-2; including each full five-reference list in the maximum makes these origins nonnegative. Swap P/E species, retain N, use the prior ordered-frame transformations, reverse edges and **all** entry/exit boundaries, and transform coefficients by Q. Edge maps become Q Pi_e^-1 Q. Applying the construction twice returns the original whole certificate.

This preserves phase templates symbolically at any origin. Geometry eligibility follows the explicitly negative-direction policy, not the forward regular-P guard. Global role consistency is preserved by flipping every role. On a shared triangular face the M count changes m->3-m, carrying PN/NE conditions into each other and the N/N condition into its stated negative-direction counterpart. Contact witnesses and reachability reverse with the complete boundary.

For the fields, use the already checked species maps

    D_P=W U_bar P,
    D_N=U_bar,
    D_E=P^-1 U_bar W,

where U_bar is the actual N-port map extended by I8. They are metric-unitary, have based inverses and implement the canonical Q binding on the chosen seed. Define

    F'_h=D_species(h) F_h,
    B'_h=D_species(h) B_h Q,
    R'_h=Q R_h D_species(h)^-1.

On a reversed edge j->h use

    U'_e=D_species(h) U_e^-1 D_species(j)^-1.

Substituting(2)-(4) proves its full binding/readout squares. Comparisons are F'_j (F'_h)^-1, so identity, inverse, all paths and all overlap cocycles follow by the same cancellation. The source-level potential proves the original frames exist globally; transporting them requires no new parity search.

An old P-reader becomes an explicit transported E-reader comparison. This is allowed by the experimental pullback policy and is not a silently installed primitive forward E move.

## 7. What is proved, and what is not

The arbitrary-size/path-length coherence obligation is proved **for this fixed joint44 candidate over the exact source-generated graph**, and therefore for every admitted retained subassembly in that class. It is no longer supported only by the14- or66-packet tests.

Still not proved:

- independent or unique physical/source selection of the chosen field generators and seed coupling;
- independent geometric-face readouts beyond the declared transported binding;
- admission as unchanged forward native rules;
- an infinite whole-boundary reflection with a finite K for unbounded origins;
- the broader Ramsey/native-forcing theorem, physical dynamics, isotope claims or arbitrary foreign input charts.

This is a written mathematical proof with an executable finite source certificate and exact algebra checks. It is **not** a new Agda/Rzk/Lean kernel certificate or graph admission.

## Reproduction and receipts

    node research/voevodsky/checkers/check_ramsey_native_chart_quotient.mjs
    python research/strominger/checkers/check_joint_field_assembly_sewing.py --fixture research/strominger/results/joint-field-sewing-fixture.json --output research/voevodsky/results/ramsey-forward-generators-replay-v1.json
    python research/voevodsky/checkers/check_ramsey_arbitrary_assembly_coherence.py

All fresh executions pass. The last receipt contains the complete96-bit potential, translation character, independently checked edge equations, source hashes and scope limits:

- `results/ramsey-native-chart-quotient-v1.json`
- `results/ramsey-forward-generators-replay-v1.json`
- `results/ramsey-arbitrary-assembly-coherence-v1.json`

No other-owner source or receipt, native generator rule, conjecture-net outcome or graph admission was changed.

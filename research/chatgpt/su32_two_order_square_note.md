# Su-32: two-order release test

Date: 2026-10-28.

## Evidence boundary

This calculation uses the pair/comparison table in the attached
`su32_packet_torus_audit.json` and its accompanying research note. The earlier
checker constructed a support-incidence model. It did not execute native Su-32
extension rules.

Fresh retrieval of these named files on the public repository's main branch
returned 404:

- `research/strominger/su32-fixed-reading-trace-v1.md`
- `research/strominger/sulfur-32-reversible-channel-specification.md`

Consequently, this is a new exact incidence calculation and a conditional
comparison construction, not verification against the actual native release
implementation. The statements below do not assert absence of a constructor
elsewhere in the full source or its 51-cell carrier.

The incoming records P+, P-, E+, E- are four directed labels. The four cross
pairs give two binary choices, not four independent binary coordinates. Their
identification with a two-coordinate face of the proposed four-polarity packet
space remains a separate obligation.

## 1. The recorded incidence is a square boundary

Let q_(p,e) denote the recorded cross-pair occurrence with P sign p and E sign e.
There are four such occurrences:

    q_++, q_-+, q_+-, q_--.

The four central comparisons contain the following pair occurrences:

    N1: q_++, q_-+       support {P+,P-,E+}
    N2: q_+-, q_--       support {P+,P-,E-}
    N3: q_++, q_+-       support {P+,E+,E-}
    N4: q_-+, q_--       support {P-,E+,E-}.

This is the vertex-edge incidence of a square. Its incidence graph, with both
pair records and comparison records as vertices, is an eight-cycle. The test
checks the actual recorded lists against these incidences.

Reading the comparisons as formal edges gives two routes from q_++ to q_--:

    q_++ --N1--> q_-+ --N4--> q_--
    q_++ --N3--> q_+- --N2--> q_--.

The directions in this display are selected for the calculation. Source-defined
transport maps along these edges have not been recovered.

## 2. Release and sign-flip are different operations

A sign-flip moves between two pair occurrences. Releasing a sign retains the
family of both possibilities. These operations must not be interchanged in the
interpretation of the test.

Define an auxiliary occurrence-family release by replacing one selected sign
with both choices while retaining the other sign. Starting at q_++ gives:

    release P first: {q_++,q_-+}, represented by N1's pair incidence;
    release E first: {q_++,q_+-}, represented by N3's pair incidence.

Releasing the remaining sign gives the same four-occurrence family in either
order:

    W = {q_++,q_-+,q_+-,q_--}.

This holds at all four starting corners. It is a theorem of the defined family
operation, not proof that native Su-32 release has this definition.

The input table contains all eight proper faces of this candidate square:
four pair records and four comparison records. It does not contain a supplied
object or operation for the all-free state. Taking their set union produces a
support label, not automatically a new native comparison witness.

In particular, the existence of the actual 51-cell carrier or of the union of
its records does not by itself make that carrier the requested local filler.

## 3. A canonical comparison at occurrence level

Group W using the two N comparisons that fix E, or those that fix P:

    A = (N1's pair occurrences) disjoint-union (N2's pair occurrences)
    B = (N3's pair occurrences) disjoint-union (N4's pair occurrences).

Both are presentations of the same four pair occurrences. The unique bijection
that preserves each original pair occurrence sends its copy in A to its copy in
B. Enumeration of all 24 bijections confirms that exactly one has this property.

The two presentation records and their grouping histories need not be equal.
A comparison record can retain A, B, the bijection, and its inverse. Nothing in
this construction licenses identifying the two generation histories.

There is a general, conditional version. Suppose the native operations actually
produce one common family of complete witnesses W_(p,e), with both the P and E
readings retained. Then their two regroupings are

    A = Sum_e Sum_p W_(p,e)
    B = Sum_p Sum_e W_(p,e).

The comparison and its inverse are explicit:

    alpha(e,(p,w)) = (p,(e,w))
    beta(p,(e,w))  = (e,(p,w)).

Both composites are identity on every coordinate, and w is preserved. Thus no
extra square-filler axiom is necessary for these two family presentations once
this common witness family and these release semantics have been established.

This does not establish uniqueness of higher equality proofs when W_(p,e) has
higher homotopy. The finite uniqueness check concerns only the four discrete
pair occurrences in the recorded table.

The source-level obligation is not merely that the two orders have the same
support. In general they could produce different families W^PE_(p,e) and
W^EP_(p,e). A source-admitted, reading-preserving equivalence between these
families must then be constructed. Replacing both by W without that comparison
would assume the conclusion.

## 4. Reversibility and matching endpoints do not determine transport

As an independent hostile test, augment each visible pair with a binary witness
h. This is a countermodel for an implication, not a claim about Su-32's actual
witness contents. Use 0 for + and 1 for -.

One explicit reversible model is

    P(p,e,h) = (1-p,e,h XOR e)
    E(p,e,h) = (p,1-e,h).

Both operators square to identity, and their visible effects are the independent
P and E sign changes. Nevertheless, from (0,0,0):

    P then E: (0,0,0) -> (1,0,0) -> (1,1,0)
    E then P: (0,0,0) -> (0,1,0) -> (1,1,1).

Thus the routes agree in their visible endpoint but differ on the retained
witness. Reversibility and equal squares have not selected identity transport
around the square.

More generally, place a bit t_i on each N_i edge, and transport h by XOR with
that edge bit. The route difference is

    omega = t_1 XOR t_2 XOR t_3 XOR t_4.

All 16 assignments satisfy reversibility and equal squares. Eight give omega=0;
eight give omega=1. Relabeling h independently at each visible vertex leaves
omega invariant. There are two gauge classes, each containing eight assignments.
The lifted graph is two disjoint four-cycles when omega=0 and one eight-cycle
when omega=1.

This does NOT mean that a nonidentity comparison is inadmissible. It may be the
comparison the source intends to retain. The result establishes that the
incidence and reversibility data do not determine its effect or establish its
source admission. Requiring raw route maps to be identical would be a stronger
condition than the user's conjecture.

Likewise, in the free groupoid on the comparison graph, the two paths differ by
the reduced loop

    N1, N4, inverse(N2), inverse(N3).

Its four letters do not cancel. Inversion alone supplies no relation comparing
these paths. The binary-witness model detects that missing relation.

## 5. Separate control for filler existence and multiplicity

The same four vertices and four edges admit three elementary cell-completion
controls:

    no square attached:      cell counts (4,4,0), Betti numbers (1,1,0);
    one square attached:     cell counts (4,4,1), Betti numbers (1,0,0);
    two squares attached:    cell counts (4,4,2), Betti numbers (1,0,1).

Each attached square uses the displayed boundary once. These spaces are,
respectively, a circle, a disk, and a sphere made from two disks. The checker
verifies the rational boundary ranks and Betti numbers, not a general homotopy
type-recognition algorithm. They demonstrate why boundary incidence alone does
not select filler existence or uniqueness. They are not alternative asserted
Su-32 models.

## 6. Result for conjecture C1

Established for the recorded data:

- the exact incidence of a two-sign square boundary;
- order-independent union of the pair-occurrence families under the explicitly
  defined auxiliary release;
- a unique pair-occurrence-preserving bijection between the two complete
  groupings;
- a conditional, witness-preserving comparison formula for native releases
  that genuinely implement those common-family regroupings;
- explicit reversible countermodels to inferring identity route transport from
  incidence and equal squares.

The next native proof has a precise target: identify the actual release outputs,
retain their complete witness families, and derive the comparison alpha between
the two orders with the required reader/continuation compatibility. Nontrivial
action on retained data must be recorded, not erased.

No cube coherence, 3-coskeletality, higher Segal property, four-coordinate
independence, or fibration follows from this test alone.

## Reproduction

The accompanying ZIP contains this note, the checker, its JSON output, and the
input JSON copied from the earlier attached audit. Run:

    python su32_two_order_square_check.py

The run on 2026-10-28 completed 712 assertions. The code uses only the Python
standard library. No Agda/Lean compilation, repository write, or native Su-32
release execution occurred.

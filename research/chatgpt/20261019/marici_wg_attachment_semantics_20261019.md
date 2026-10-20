# WG attachment semantics: existing proofs, new cells, and higher comparisons

Date: 2026-10-19.

## Disposition

This packet instantiates the existing Marici attachment definition on the retained two-attachment circle and derives the corresponding mapping-space tests. It does not replace T9 by a new physical law or claim that a particular T9 policy has been selected.

The main mathematical consequence is:

- An attachment X -> X[beta] admits a homotopy retraction exactly when beta was already fillable in X.
- If beta:S^(n-1)->X has an actual retained filler p:D^n->X, a *fresh independent* n-cell attached along beta gives X[beta] equivalent to X wedge S^n. The equivalence depends on the retained nullhomotopy p.
- Adjoining a further (n+1)-cell identifying the new filler with p removes that additional sphere summand.
- Storing a certified output as an evaluation-graph record is a different operation and does not automatically adjoin a cell.

These are consequences of the homotopy-pushout definition, not new axioms. They do not follow from a count of WG invocations. The new computation below checks the associated integral chain formulas and finite cyclic observation tests.

## Sources read in this continuation

Repository paths and blob SHAs returned by the connected GitHub reads:

1. `research/nima/marici-minimal-mathematical-formulation.md`
   - SHA: `22097430b821387eadc95a3c00beaec99fd7f3a7`.
   - Sections 2-4 define filler types, comparison of fixed-boundary fillers, attachment, and recursive objectification.
   - Section 9.2 defines the chain attachment d(e_delta)=delta and explicitly distinguishes a real linear filler from an admissible native filler.
2. `research/grothendieck/agda/ClosureGeneratedMapNecessity.agda`
   - SHA: `1332e7f686e0e85c73c08d6f98c430f6e58b863a`.
   - `generatedMapIso` is the full cocone/mapping-space isomorphism, including attachment paths.
3. `research/voevodsky/agda/ClosureGluingTreeRegression.agda`
   - SHA: `e3b059868de8aa2d3c6d0c795f15c879de9bf932`.
   - `circleEquiv`, `preservesLoop`, and `gluedLoopNotRefl` construct the circle and retain its nontrivial loop through presentation changes.

All paths are relative to https://github.com/andrey-kokoev/marici/blob/main/ . The cited reads are source inspection, not a fresh compilation or an audit of an uncommitted working tree.

Standard topology references used:

- Allen Hatcher, Algebraic Topology, Chapter 0 (homotopy invariance of attaching maps and mapping cones), Sections 1.2 and 2.2 (cellular presentations and homology), and Section 4.B (Hopf invariant).
  https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
- The Cubical library's pushout universal-property and wedge constructions:
  https://agda.github.io/cubical/Cubical.HITs.Pushout.Properties.html
  https://agda.github.io/cubical/Cubical.HITs.Wedge.Properties.html

## 1. The complete observation-extension test

Work in homotopy types or with CW attachments and their homotopy-invariant pushouts. Let i:A->D be an admitted boundary inclusion and beta:A->X an attaching map. Put

    X' = X pushout_A D,     j:X->X'.

For an old observation u:X->Y, define the full extension type

    Ext_beta(u) = sum(F:X'->Y). (F composed j = u).

The path in this dependent sum is retained. Applying the existing pushout universal property and taking the fiber over u gives

    Ext_beta(u) equivalent to
      sum(v:D->Y). (v composed i = u composed beta).

The right side is exactly the filler type in Y of the observed boundary. This is an equivalence of types, not just an iff between inhabitation statements. It retains comparisons between fillers and all their higher identity types.

Proof: `generatedMapIso` expresses a map X'->Y as its map on X, map on D, and the homotopy between their restrictions to A. Fixing the first map to u, with its equality witness, leaves precisely the displayed filler type. The elimination of the variable first map uses the contractible endpoint-and-path fiber, not a truncation of the remaining filler data.

The construction is natural under postcomposition Y->Z when the filler and boundary paths are transported. This does not assert that postcomposition preserves existence in both directions: a less discriminating observation can make an obstruction invisible.

## 2. Retraction criterion

Set Y=X and u=id_X. Then

    Retr(j) equivalent to Fill_X(beta),

where

    Retr(j) = sum(r:X'->X). (r composed j = id_X).

Thus a retained old filler is exactly the data needed for a retraction of the freely attached space back to its source. If the old filler does not exist, no such homotopy retraction exists. Storing a copy of the old syntax separately does not change this topological statement about j.

This is a sharper distinction than labeling all source-enlarging operations either lossless or lossy without specifying the realization map.

## 3. Fresh objectification of an already-existing spherical filler

Assume X is a pointed connected CW-type, n>=2, A=S^(n-1), D=D^n, and retain an actual filler p of beta in X. The same elementary construction also covers n=1 in the pointed component used below.

The filler p supplies a nullhomotopy of beta. Homotopy invariance of mapping cones gives, under X,

    X' = X union_beta D^n equivalent to X wedge S^n.

The equivalence is relative to the chosen p. It is not claimed to be canonical after p has been forgotten, and different fillers can give different splittings.

Let p_hat be the freshly attached disk. Glue p_hat to the oppositely oriented old p along their common boundary. This gives

    gamma_p : S^n -> X'.

Its projection to X'/X = D^n/S^(n-1) has degree one up to orientation. It is the primitive new sphere summand. The retraction r_p sends gamma_p to a nullhomotopic sphere because it sends both halves to p. Meanwhile r_p composed j is the identity, so the original homotopy information of X is retained by a split map.

If a further comparison cell is attached specifically along gamma_p, then

    (X union_beta D^n) union_gamma_p D^(n+1) equivalent to X.

In the wedge description this is X wedge (S^n filled by D^(n+1)). The attached pair cancels homotopically. This statement concerns the specified relative comparison sphere, not an arbitrary map with the same cellular boundary.

Consequently the following actions are distinct:

- return or reify the existing p;
- adjoin a fresh p_hat with the same boundary;
- adjoin a higher equality p_hat=p.

Only the second introduces the independent sphere in this construction; the third removes it. A literal repeated function call that returns the same package does neither.

Symmetry is handled by transporting the entire tuple (X,beta,p). It is not necessary, and may be impossible, to select a filler invariant under all symmetries while forgetting its transport data.

## 4. Exact integral chain counterpart

Suppose a realized old n-chain p has d(p)=delta. Adjoin a new n-generator e with d'(e)=delta. Then C'_n=C_n plus Z e, and define

    Phi(c,t) = (c+t*p,t),
    Phi_inverse(c,t) = (c-t*p,t).

The target complex is C plus an independent Z in degree n with zero differential. All other degrees use the identity maps. Because d(p)=delta,

    d_split Phi = Phi d',
    Phi_inverse Phi = identity,
    Phi Phi_inverse = identity.

The cycle e-p maps to the primitive independent generator. If a new (n+1)-generator h has d(h)=e-p, it pairs with that generator by an integral coefficient one and eliminates exactly that summand.

This chain theorem needs an actual integral p. Even then it is a chain theorem; the topological wedge theorem additionally needs an actual topological filler. A boundary solved only by a formal real linear combination is not automatically a native filler.

## 5. The retained-circle experiment

Use the source circle with vertices N,S and two distinct paths a,b:N->S. Its primitive cycle is z=a-b. The homotopy-level loop is a concatenated with the inverse of b.

For a disk attached along winding q, the cellular boundary is

    d(c)=q*(a-b).

The spanning-edge coordinates (b,z) cancel the contractible tree part of the graph. With m disks of windings q_1,...,q_m, the remaining integral boundary is the one-row matrix

    [q_1 ... q_m] : Z^m -> Z.

If g=gcd(q_1,...,q_m), the resulting H1 is Z/g (Z when g=0), and H2 is free of rank m-rank([q_i]). The fundamental group is the one-generator presentation with relations z^(q_i)=1, hence the same cyclic group. These conclusions follow from the actual attaching words and integral row reduction.

| Operation | Homotopy type in this specified example | Surviving class |
|---|---|---|
| Retain the unfilled source circle | S1 | z generates pi1=Z |
| Attach one disk along z | D2, contractible | z becomes fillable |
| Attach a second independent disk along the same old z | S2 | c_1-c_0 generates H2=Z |
| Attach a 3-cell comparing those disks | D3, contractible | the relative sphere is filled |
| Attach a disk along the constant loop | S1 wedge S2 | old z remains and a 2-sphere is added |
| Attach a disk only along z squared | RP2 | z has order two rather than becoming trivial |

These are the homotopy types of the specified cell attachments, not conclusions drawn from equality of Betti numbers. The first addition to the unfilled circle has no old filler and therefore no source retraction. The second addition does have an old filler c_0; it is exactly the witnessed sphere-splitting case above.

Exchanging the two independently labelled disks reverses the relative class. The checker verifies the relevant boundary and symmetry matrices. This is not a newly asserted A4 action on the example.

## 6. A native-to-real-linear filler mismatch

Attach only a disk c along z squared. The group presentation is

    pi1 = <z | z^2=1> = C2.

Therefore z has no topological disk filler. Over real or rational cellular chains, however,

    d(c/2)=z.

This is an exact mismatch, not a numerical error. The real linear obstruction test says that z is a boundary; the source topological loop is non-nullhomotopic.

A finite cyclic observer detects the distinction: the homomorphism pi1->C2 sending z to its nonidentity element respects z^2=1 but still detects z.

More generally, an observation into B(C_N) sending z to k extends over the q_i attachments exactly when q_i*k=0 mod N for all i. The checker verifies the exact count gcd(N,g) for every tested policy. This counts homotopy classes of cyclic characters; it is not a computation of the full mapping space.

The mismatch confirms why the source formulation's warning about linear fillers matters. The conditional stable/Hodge theorem is not refuted; its result must not be identified with the native filler space without an appropriate comparison theorem.

## 7. Relation to the Hopf question

For a fixed tetrahedral boundary beta:S2->X with an existing 3-ball filler, fresh objectification gives X wedge S3. This produces an actual higher homotopy class in the enlarged target. It does not choose a nonzero map from that new S3 back to an old S2. The retraction supplied by the old filler maps the relative sphere trivially.

CP2 instead attaches a 4-cell to S2 along the non-null Hopf map eta:S3->S2. Its integral cellular chain groups and differentials agree with those of S2 wedge S4, but their cohomology rings differ: the degree-two generator squares nontrivially in CP2 and trivially in the wedge.

Thus integral cellular data repairs the torsion loss above but still does not recover all higher attachment information. A proposed full source realization must retain the relevant nonlinear attaching maps and comparison types; chain boundaries and cell counts are not sufficient replacements.

## 8. Revised structural test for an actual WG successor

For each source-authorized step, export:

    prior structure X;
    boundary shape A->D;
    actual boundary map beta:A->X;
    whether an old filler p is supplied;
    whether a fresh cell is adjoined;
    whether a selected comparison to p is also adjoined;
    the inclusion j:X->X';
    retained source and symmetry transport data.

Test the full extension equivalence in Section 1. It identifies which old observations extend and what their complete choice spaces are. Test Section 2 to distinguish a split source-preserving enlargement from an imposed relation. Use the circle and torsion examples as rejection controls for an interpretation that forgets boundary winding.

This is not a claim that these examples are the physical T9 rule. It is a concrete test suite for whichever source rule is actually selected, using operations already present in the research formulation. No gauge target is imposed to choose the rule.

## Verification and artifacts

Run:

    python check_attachment_semantics.py --output wg_attachment_semantics_results.json

The standard-library checker executed successfully: 11,055 exact assertions, 400 circle-attachment policies, finite cyclic probes of orders 2 through 12, and witnessed chain splits through dimension 8. The homotopy-theoretic arguments are written proofs using the cited pushout and attaching-map theorems; the program does not compute arbitrary homotopy groups, construct the Hopf map, or certify source-law admission.

No Agda or Lean compilation was performed. The runtime has no Agda executable; a direct attempt to reach the official binary host could not resolve its hostname. No repository files were modified.

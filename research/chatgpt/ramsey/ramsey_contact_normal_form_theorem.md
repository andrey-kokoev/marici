# Normal forms for three births; no irreducible fourth-order obstruction

## Scope and statements

The carrier is the 64-vertex graph on F₂⁶ with A-steps
`1,2,4,8,16,32,63`; B denotes nonadjacency. Split it into lower vertices
0–31 and upper vertices 32–63. Lower square c is `{4c,4c+1,4c+2,4c+3}`.
An ordered birth `(a,b)` makes the previously declared half-square edits in
a and b and has ports `{4a+1,4a+2,4b,4b+3}`. All square cells used by births
are distinct. All old edits remain fixed when subsets of newborns are tested.
The permitted maximum B-group size is 22.

**Three-birth normal-form theorem.** If every pair of three births is admissible,
a forbidden B-group involving all three exists if and only if the contact-parity
equations are consistent. Whenever one exists, there is a witness consisting of
8 lower vertices, one per square and closed under v ↦ v xor 31, and 12 upper
vertices of one parity. Thus the earlier necessity result has a structural
proof; it need not be inferred from the list of 3,360 assemblies.

**Four-birth theorem.** For four disjoint births in the same half-carrier, let
β(1234) be the maximum old B-group avoiding all four port sets. Then

- consistent contact parity implies β(1234)=20;
- inconsistent contact parity implies β(1234)≤18.

In particular β(1234) is never 19. No assembly in this family has an obstruction
whose minimal newborn subset has size four. This is not a statement about
larger carriers, other birth operations, or unrestricted Ramsey numbers.

## 1. What remains after excluding newborn ports

For a full set of k births, k square cells are first contacts and k are second
contacts. In a first-contact square the allowed old vertices have low labels
0 and 3; the inserted A-diagonal connects them. In a second-contact square the
allowed labels are 1 and 2; the other inserted A-diagonal connects them.

Consequently an old B-group selects at most one vertex from each edited square.
An unedited square can contribute at most two vertices, and those two have the
same low-bit parity. More generally, every occupied square uses only one
low-bit parity.

There are 8−2k unedited squares, so a lower B-group I has

    s=|I| ≤ 16−2k.

Pair lower vertices by v ↦ v xor 31. Write D for the antipodal pairs touched
by I, t=|D|, and p=s−t. Thus p is the number of antipodal pairs for which both
representatives were selected.

Each touched lower pair blocks both corresponding upper vertices. The remaining
upper graph is the bipartite double cover of C[U], where C is the 16-vertex
Clebsch quotient and U=V(C)\D.

For S⊆U define N_U(S)=N_C(S)∩U. The largest upper B-group has size

    |U|+h(U),    h(U)=max_{S⊆U} (|S|−|N_U(S)|).

This formula follows directly by choosing S on one side of the double cover
and every vertex outside N_U(S) on the other side. Therefore

    |I| + maximum upper contribution = 16+p+h(U).       (1)

No maximum-independent-set algorithm is needed for this identity.

## 2. The small quotient bound

The Clebsch quotient C has degree 5, no A-triangles, and exactly two common
neighbors for each nonadjacent pair. Its independence number is 5.

For completeness, realize C as the even subsets of a five-element set, with
adjacency when symmetric difference has size four. Translate any independent
set to include the empty set. Its other members are pairwise-intersecting
2-subsets. Such a family has at most four members: either all share one element,
or they form a triangle of three 2-subsets. Thus α(C)≤5; a four-edge star plus
the empty set attains 5.

Every independent S in C with r=|S|≥2 satisfies

    |N_C(S)| ≥ r+6.                                    (2)

For r=2,3,4, let a_v count the neighbors of v in S. Degree and common-neighbor
counts give Σa_v=5r and Σa_v²=r(2r+3). Cauchy–Schwarz gives
|N_C(S)|≥25r/(2r+3), whose integer lower bounds are 8,9,10. For r=5, maximality
makes S dominate all eleven remaining vertices.

The maximum in h(U) may be taken over independent S. Indeed, for arbitrary X,
put S=X\N_C(X). This S is independent, N_U(S)⊆N_U(X)\X, and its deficiency is
at least that of X. Hence a positive Hall deficiency has one of two forms:

(a) It is witnessed by an isolated vertex of C[U], giving h=1.
(b) It is witnessed by an independent set of at least two vertices. By (2),
    h≤t−6, so (1) is at most s+10.                    (3)

The case h=0 is separate.

## 3. Isolated-vertex lemma

If C[U] has an isolated vertex, then p≤2 for k=3 and p≤1 for k=4.

To see this, let z be isolated and let π be its low-bit parity. The four
antipodal square classes each contain four quotient vertices. Two of z's five
neighbors lie in its own square class and have parity 1−π; one lies in each
of the other three classes and has parity π. All five must lie in D.

A complete selected antipodal pair in an outside class must have parity π.
Otherwise it occupies both square cells with parity 1−π and leaves nowhere
to touch that class's required parity-π neighbor. An outside class cannot
contain two complete pairs: this would double both of its unedited squares
with parity π, forcing every selection in all other square cells to have
parity 1−π, contrary to the required parity-π contacts in the other outside
classes.

Let r be the number of complete pairs in the three outside classes, and q
those in z's own class. The outside classes require at least 3+r occupied
parity-π square cells. Only k edited squares permit parity π. The home class
requires at least 2+q selected vertices across its two square cells, and
therefore at least q unedited squares there.

For k=3, the outside classes need at least r unedited squares and the home
class at least q. Only two unedited squares exist, so p=r+q≤2.
For k=4 there are no unedited squares: q=0 and 3+r≤4, so p≤1.

## 4. Proof of the three-birth normal form

Assume three births are pairwise admissible, and an old B-group of size at
least 20 avoids all their ports. Here s≤10.

If h>0 is witnessed by an isolated quotient vertex, Section 3 gives p≤2, and
(1) is at most 19. That case cannot supply the obstruction.

If h>0 is witnessed by at least two quotient vertices, (3) forces s=10.
Both unedited squares then contain their two opposite low-bit positions, and
each of the six edited squares contains one vertex. Classify the distance
between the two unedited cells in the three-dimensional cell cube:

**Distance two.** The free cells share two neighbors. Their selected low
parities must agree. Four edited neighbors are then forced to use the other
parity, although only three edited squares permit it. Impossible.

**Distance three.** The free cells are antipodal. Their parities must be
opposite to respect the three-first/three-second balance. No selected
antipodal pair remains. All four quotient vertices of the free square class
are removed, and each other class has two surviving quotient vertices of
opposite parity, joined by a C-edge. These three disjoint edges provide a
perfect matching of the surviving six quotient vertices, and a matching of
all twelve vertices in their double cover. The upper B-group has size six,
so the total is at most 10+6=16.

**Distance one.** Normalize the free cells to 3 and 7, using the carrier's
coordinate symmetries and simultaneous operation reversal. Their doubled
parities are opposite. Four edited-cell parities are forced. The two remaining
edited cells admit only two assignments, up to reversing everything:

  parallel: first cells {0,1,2}, second cells {4,5,6};
  crossed:  first cells {1,2,4}, second cells {0,5,6}.

In the crossed case there are no complete selected antipodal pairs. The
surviving quotient has six vertices; the square classes {1,6} and {2,5} each
supply a disjoint edge. Their double-cover edges give a matching of size four,
so the upper B-group has size at most 12−4=8. Total: at most 18.

In the parallel case the old graph is independent of the matching between
its first and second contact cells. The following 21-vertex B-group exists:

  {2,3,4,8,13,14,17,22,26,28,31,
   33,38,42,44,47,48,51,53,57,62}.

It meets ports only in first-contact cell 0, at vertex 2. Thus it avoids the
ports of the other two births, no matter how the contacts are paired. Adding
those two newborns gives B23. This contradicts pairwise admissibility. The
verifier checks this one explicit witness under all six contact matchings.

It follows that the only remaining case is h=0 and p≥4.

If the two free square cells are not antipodal, every antipodal square class
contains an edited square and contributes at most one complete pair. Thus
p=4 requires one pair in every class, forcing consistency of all contact
parities.

If the free cells are antipodal, p≥4 is impossible. One pair in that class
would require one in each of the other three classes, contradicting the odd
three/three parity counts. Two pairs in the free class would force all occupied
edited cells to the opposite low parity; two further complete pairs would
then require four edited squares of one parity, when only three exist.

We have proved necessity of the parity equations. For sufficiency, assign a
bit p_[c] to each antipodal square class and put

  e(c)=parity(c),
  low(c)=e(c)+2(e(c) xor p_[c]),
  I={4c+low(c):c=0,...,7}.

This is an antipodal lower B-group with one vertex in each square. Adjoin
upper vertices {32+v: parity(v)=0 and v∉I}. There are twelve. The twenty old
vertices avoid all ports; adding the three newborns gives B23. This is the
claimed normal form.

## 5. Four births: prediction and proof

Now every square is edited and s≤8. Let q be the number of antipodal square
classes whose two prescribed low parities agree. Because four squares permit
even parity and four permit odd parity, q is 0,2, or 4. Parity is consistent
exactly when q=4, and always p≤q.

If parity is inconsistent:

- h=0 gives 16+p≤18;
- a Hall witness of size at least two gives s+10≤18;
- an isolated-vertex witness gives p≤1 by Section 3, hence 16+p+1≤18.

Therefore β(1234)≤18. Four B-connected newborns add at most four vertices,
so their full common-link test is admissible at cap 22.

If parity is consistent, the canonical lower-eight/upper-twelve construction
still works, giving β(1234)≥20. The same upper bounds show β≤20: when h=0,
p≤4; when h>0 the bound is at most 18. Thus β(1234)=20. But those same twenty
old vertices together with any three newborns already give B23.

In neither case is the quartet a new minimal obstruction. Every failure of a
four-birth all-B completion is detectable on a subset of at most three births.
This does not mean every quartet is admissible: smaller subsets may fail.

## 6. Independent audit

The executable checks the quotient expansion, the isolated-vertex lemma, and
the exceptional-state classification on 120,047 local states covering 13
three-birth types and 6 four-birth types. These checks corroborate, rather than
replace, the proof above.

The optional audit fixes all four operations and checks all newborn subsets.
There are 105 pairings of the eight cells and 16 orientations, hence 1,680
assemblies. Under the declared carrier automorphisms these form 52 orbits.

| Full old common-link capacity | Oriented assemblies |
|---:|---:|
| 17 | 384 |
| 18 | 1,152 |
| 20 | 144 |

There are zero irreducible fourth-order obstructions. The exact distinction
between capacities 17 and 18 is supplied by the audit, not by the proof's
coarser inconsistent-parity bound β≤18.

Run `python ramsey_contact_normal_form_theorem.py --audit` to reproduce the
checks and write the full capacity spectra to JSON.

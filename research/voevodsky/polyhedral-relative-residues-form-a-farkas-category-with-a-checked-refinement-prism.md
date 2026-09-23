# Polyhedral relative residues form a Farkas category with a checked refinement prism

## From interval slack to a polyhedral relative residue

A fine fiber has a fixed affine coordinate chart and presentation

    K={x: A x<=b}.

Relative to a reference s, write x=s+v. Its exact residual presentation is

    J_s(K)=(A,r), r=b-A s,
    K=s+{v: A v<=r}.

Both A and r must be retained. Slack values without their normals do not determine the fiber. This is the affine defining system expressed at a reference; it resembles a value-plus-linear-part jet because the functions are affine, but is not an identification with the earlier analytic residue jet.

Changing reference by d gives r_new=r-A d. It preserves the physical relation even if the reference is not admitted. As in the scalar case, reference changes are not automatically homotopies through admitted witnesses.

## Certificate arrows, not merely semantic assertions

An object is (A,r,s). An arrow to (B,u,t) consists of

    M>=0, d=t-s, c>=0,
    B=M A,
    u=M r-B d+c.

M is an exact Farkas combination and c is its nonnegative bound surplus. If x belongs to the source relation, it belongs to the target relation. The arrow records proof of inclusion and a change of reference, not an unproved equality.

Two inclusions can establish equality of the physical relations. They need not be inverse matrices or isomorphisms of proof presentations: redundant rows carry extra proof structure. Normal forms, semantic equality and proof identity remain distinct.

Infeasibility is a different certified event: a nonnegative combination with zero normal and strictly negative bound. A negative individual residual only says the reference violates a row; it does not prove emptiness.

## Composition law

For consecutive arrows (M,d,c) and (N,e,k), define

    (N,e,k) o (M,d,c) = (N M, d+e, N c+k).

This follows by substituting the defining identities; all composed multipliers and surpluses remain nonnegative. The identity is (I,0,0). Matrix multiplication, vector addition and the action on c prove associativity exactly.

This is a concrete category of certified polyhedral presentations in a fixed ambient chart. Its arrows have verifier-checkable equations. It is not yet a category of authorized historical transitions: a valid weakening of constraints need not be an operation the retirement policy permits.

## Fine refinement is functorial

Append the SAME physical fine inequality a x<=b at every presentation. At reference s its new residual is b-a s. The induced arrow is

    M_new=diag(M,1), d_new=d, c_new=(c,0).

Using the same untranslated residual constant after moving s is incorrect. The checker rejects that error.

Dropping the newly appended row gives a certified inclusion from the refined relation to the original relation. These forgetful arrows form a natural transformation: refining an inclusion and then dropping the new row equals first dropping it and then applying the old inclusion, at the level of the actual Farkas matrices and base shifts.

This natural forgetful comparison does NOT authorize operational history erasure or restoration. It states a mathematical inclusion and its coherence.

## An actual four-simplex and a five-dimensional prism

Choose four composable presentation arrows. The nerve of this category supplies a four-simplex: five presentation objects, ten composite edges and ten triangular composition equalities. Its tetrahedral associativity laws follow from the same composition identity.

Apply the refinement functor to that chain. The natural forgetful transformation supplies a simplicial comparison on Delta^1 x Delta^4. Its standard staircase triangulation has five 5-simplices: travel along refined presentations to vertex k, drop the new row there, then travel along the original presentations.

This is not merely a suggestive dimension count. The executable example checks every composite edge, all ten triangle equalities, all ten naturality squares, five parenthesizations of the four-arrow chain, and fourteen parenthesizations for EACH of the five five-arrow staircase chains. All staircase routes have exactly the same composite certificate.

## Concrete example and what is independently constrained

The five presentations all describe the triangle

    h>=0, k>=0, h+k<=1.

They add the redundant bounds h<=1 and k<=1, remove those rows, permute the remaining rows, and change reference at each step before returning to the initial presentation. All constituent matrices are explicit nonnegative rational proofs. The refinement is h<=1/2. A separate nonzero-surplus example checks genuine weakening as well as equivalent presentations.

The carrier is a two-dimensional fine-coordinate polyhedron. The dimensions four and five above are SIMPLICIAL coherence dimensions, not dimensions of the source or fiber. No new original-source admission theorem is supplied by this checker.

## Relation to the earlier cone architecture

There is now a literal simplicial object in the new lane: a verified four-simplex of presentations and a verified five-dimensional refinement PRISM. However:

- its five vertices are a chosen chain of constraint presentations, not yet the earlier S,A,R,C,G roles;
- its residual package contains normals and slack values, not the established analytic residue jet;
- the prism is not automatically the earlier based cone B star (Delta^1 x Delta^3);
- no identification of a retained base edge or source-derived analytic filler has been proved;
- the source/history authority constraints must be added to admissible arrows separately.

Thus we have recovered the algebraic SHAPE in a controlled model without claiming the old analytic architecture has been reconstructed. Unlike an arbitrary formal cone, every edge here carries explicit Farkas/base-change data whose composition is checked. The next identification must preserve that data and the authority boundary, not only simplex dimensions.

## Reproduction

    python research/voevodsky/checkers/check_polyhedral_residue_coherence.py

Artifact: `results/polyhedral-residue-coherence.json`.

The direct exact checker establishes the displayed finite model and refuses negative certificate surplus and an incorrectly transported fine bound. It is not an independently implemented categorical proof assistant, general polyhedral equivalence solver or externally authenticated transition service.

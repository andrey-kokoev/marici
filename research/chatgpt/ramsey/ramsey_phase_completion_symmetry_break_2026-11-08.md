# Ramsey phase completion: a forced partial orbit and symmetry breaking

8 November 2026. Exact arithmetic with the existing 13-vertex and 17-vertex triangle-free constructions.

Companion: `check_ramsey_phase_completion_and_symmetry_break.py`. Execute with the Python standard library:

```sh
python check_ramsey_phase_completion_and_symmetry_break.py
```

## Scope

Question: can *minimal phase-incidence completion*, without a prescribed sector size, produce the 13→17 and 17→22 constructions? We tested minimum admissible symmetry-equivariant extensions, then independently extracted the phase pattern of the established valid five-vertex attachment.

The input is the graph `G13=C13(±1,±5)` and the order-four automorphism `σ(v)=5v (mod 13)`. This graph and automorphism are not derived from the symbolic `RGRG…00` row. The five-vertex successor audit initially selects the two opposite pairs of the existing red C4 and considers the 39 maximum independent four-sets of G13 as candidates for the other neighborhoods. Thus the full attachment family is **not** determined without assumptions.

## A. A direct failure of size-minimality

G13 is triangle-free with α(G13)=4. At the next Ramsey parameter, the admissibility bound is α≤5. A new vertex with any independent red neighborhood is admissible, so an admissible one-vertex extension always exists. Requiring a lift of σ does not fix this problem.

The independent red neighborhoods fixed by σ are exactly

```
∅, {0}, {1,5,8,12}.
```

All three yield valid equivariant single-vertex attachments. There are also eight valid two-vertex equivariant attachments (counting the orientation of the two-cycle seed and the choice of their mutual red/blue edge). The exhaustive four-phase orbit search over every one of the 183 independent seeds and all four cyclically invariant internal edge graphs finds exactly **four** valid four-vertex attachments, one orbit of four equivalent seeds. Their internal graph is forced to be a red C4.

Hence **minimum admissible sector size does not select four**. Additional selection data are necessary. Choosing the *largest possible* extension is a separate optimization that would need a theorem establishing global extremality; it is not a local symmetry operation.

## B. Exact 2+1+2 formation at 17→22

Take the 17-vertex witness produced by seed `S0={1,7,11}` and its σ-orbit of four independent three-sets, with new vertices 13,14,15,16 forming a red C4. The inherited automorphism σ17 advances this four-cycle.

The two opposite red-neighborhood pairs of its C4 are

```
L0={13,15},   L1={14,16}.
```

They form a two-cycle under σ17.

The old 13-vertex core has 39 maximum independent four-sets. Exactly one is fixed by σ:

```
A={1,5,8,12}.
```

Four other maximum independent sets form one σ-cycle:

```
B0={0,3,6,10}
B1={0,2,4,11}
B2={0,3,7,10}
B3={0,2,9,11}
```

A pair `Bi,Bj` is compatible as red neighborhoods of blue-adjacent new vertices exactly when

\[
\alpha(G_{17}-(B_i\cup B_j))\le4.
\]

The exact residual independence numbers are **4 for adjacent phases** and **5 for opposite phases**. Thus compatibility on these four B-states is precisely the cycle C4:

```
B0 — B1
|     |
B3 — B2
```

For instance, removing B0 and B2 leaves the independent five-set `{2,5,8,12,13}`. Two new blue-adjacent vertices with those red neighborhoods then form an independent seven-set together with these five old vertices, violating α≤6.

The 39-set exhaustive check yields exactly four compatible triples; they are

\[
\{A,B_i,B_{i+1}\},\qquad i\in\mathbb Z/4\mathbb Z.
\]

The five new neighborhoods therefore have the exact **2+1+2** decomposition:

- 2: the opposite C4 pairs L0,L1, permuted by σ;
- 1: the fixed independent four-set A;
- 2: an **adjacent pair** in the four-cycle B0,B1,B2,B3.

For any one of these four triples, all 1,024 possible internal red-edge graphs on the five new vertices were evaluated. **Exactly one** is admissible, namely K_{2,3}, with the two L-vertices in one side and the three A/B-vertices on the other. The resulting 22-vertex graph is triangle-free with α=6.

The five old-neighborhood indicator columns are linearly independent: their exact 5×5 Gram matrix has determinant **240**, so they span a five-dimensional incidence space.

## C. The next operation is a symmetry-breaking choice orbit

Under σ, the four compatible triples form one transitive four-element orbit. No individual triple is fixed by σ or by σ². The five neighborhood columns are not permuted into themselves by σ17; hence the inherited quarter-turn does **not** lift to an automorphism of any single resulting labeled 22-vertex extension in this family.

At the same time, all four extensions are isomorphic by transport through the original σ17 symmetry. The unlabelled result is one isomorphism class, even though the source retains four distinct phase-labelled continuation histories.

This yields the concrete candidate operation

\[
\text{source four-phase orbit}\longrightarrow
\text{maximum compatible adjacent pair}\longrightarrow
\text{four continuation choices}/C_4.
\]

The first arrow is derived in this selected source family, and the quotient by C4 identifies the four equivalent completed graphs. This is an exact instance of **partial-orbit selection, symmetry breaking, and quotienting**. It is not yet an arbitrary-k Ramsey generator.

## D. Does a new harmonic cause the five-vertex sector?

A four-column incidence orbit has rank 4 and requires trigonometric modes `1,cos θ,sin θ,cos 2θ` on four quarter-turn samples. The five new incidence columns have rank 5. If five *externally supplied* equally spaced phase points are used, they can be interpolated using `1,cos θ,sin θ,cos 2θ,sin 2θ`: still total polynomial degree **two**.

Thus the observed change from four to five columns does **not** force an increase of polynomial degree from two to three. The additional second-harmonic quadrature is available, but a fivefold cyclic phase action is **not** inherited from the order-four symmetry; assigning fifth-root phase points would be a new choice rather than an intrinsic derivation.

The simpler “next Ramsey sector appears whenever a higher polynomial degree is necessary” hypothesis is therefore **not supported** by this transition. A more precise hypothesis is that the new sector arises from an *incomplete orbit of existing comparison modes*, followed by quotienting the orbit of valid choices.

## E. What is proved, and what is still needed

Proved by exact finite enumeration within specified source families:

1. Size-minimal admissible completion selects neither 4 nor 5 in this sequence.
2. Four-phase equivariant attachment from G13 has one surviving four-seed orbit and a forced red C4.
3. Given the selected opposite-pair left attachments and core four-set right-neighborhood family at G17, the valid right triples are exactly the four adjacent-pair choices `A+Bi+Bi+1`.
4. Every valid triple forces the internal K_{2,3} edge assignment; nonadjacent B-pairs violate the exact independence constraint.
5. The four completions form one C4 orbit; no single completion retains the inherited order-four symmetry.
6. The five resulting incidence columns are linearly independent, but the minimum degree for *arbitrary cyclic interpolation* remains two.

Not established:

- A derivation of G13 and σ from the original short symbolic row.
- A source-only rule selecting the initial opposite-pair attachment among all other feasible first attachments.
- Completeness of the 2+1+2 family for all 17-vertex critical graphs or all 22-vertex witnesses (previously tested exceptions exist).
- A universal Ramsey threshold or closed-form formula for R(3,k).

**Next falsifiable target:** formulate a rule which, for *any* critical predecessor, selects a maximal compatible **partial orbit of incidence constraints**, carries all equivalent choices as one quotient rather than choosing a phase by hand, and reproduces both the surviving 2+1+2 branches and the known counterexamples to their universality. Test on the seven 17-vertex critical graphs without prescribing a five-vertex attachment shape.

# Audit elimination has certified savings and quadratic projection cost

## Result

One audit can be retired by an exact, proof-carrying elimination compiler.
The resulting public presentation preserves the complete public possibility
image, not merely a finite collection of optimum values. A rational interval
rule reconstructs an admissible fine witness whenever a public point is
admitted.

There is also a sharp representation obstruction INSIDE the owning source:
with m=4 fixed, 2n+8 fine evidence rows can require exactly n^2+5 public
facets after retiring one audit. Every one of these facets lies inside the
coarse source image, so retaining the coarse source generator does not make
these new evidence facets disappear.

Thus elimination is not uniformly a storage-reclamation operation. Its cost
is governed by compatibility between lower and upper envelopes of the retired
coordinate, and by the chosen representation language.

## 1. Frozen source and semantic statement

Use the owning box 0<=t_j<=100+2j with U=sum t_j and V=sum 128^-j t_j.
Fine audit schema B is fixed and its exact rational evidence tuple E retained.
Retire one atom audit h, leaving schema A. No new observed value is supplied.

The fine image is given exactly by the joint-audit dictionary from
`joint-audit-images-have-a-uniform-finite-separation-dictionary.md`, together
with E. Add valid coordinate bounds for convenience. Write these rows as

    a_i dot y + c_i h <= b_i,

where y contains the surviving joint coordinates.

The target is exactly the projection of this constrained fine image. A new
state using the coarse source generator and compiled frames denotes its
coarse saturation in source space. That source carrier can be LARGER than
the original fine carrier. It is their public images, not their fine witness
sets, that must agree.

The interface preserves public membership, public optimization, emptiness,
and possible/forced predicates determined by the public image. It does not
preserve predicates inspecting the retired atom or select the actual source.

## 2. Complete one-coordinate elimination and its converse certificate

Partition the fine rows by the sign of c_i. Let P, N, Z denote the positive,
negative and zero index sets. Source audit caps ensure both P and N exist.

Keep every zero row. For every i in P and j in N, form

    (a_i/c_i - a_j/c_j) dot y <= b_i/c_i - b_j/c_j.

Its certificate is the nonnegative combination of fine rows with weights
1/c_i and -1/c_j. The h coefficient cancels exactly. This proves the forward
inclusion into the projected system.

Conversely, for a public point satisfying these rows, define

    lower(y) = max_(j in N) (b_j-a_j dot y)/c_j,
    upper(y) = min_(i in P) (b_i-a_i dot y)/c_i.

Every pair inequality says one lower bound is at most one upper bound.
Therefore lower(y)<=upper(y). Any h in that closed interval, for example its
midpoint, satisfies EVERY original fine row. The exact joint-image theorem
then supplies a source lift. Empty and lower-dimensional states require no
special generic-position assumption.

This proves both inclusions for the entire continuum. It is the classical
Fourier--Motzkin argument applied to the source-bound audit presentation, not
a claim of a new general elimination algorithm.

## 3. Structural criterion: envelope interaction width

The uncompressed projected row count is exactly

    |Z| + |P|*|N|.

Consequently, if one sign family has bounded size, eliminating that coordinate
has linear row growth. This is a useful sufficient criterion, not a necessary
one: many pair inequalities can be redundant even when both families grow.
Proportional normalization and implication proofs can reduce the output.

The relevant structure is not merely how many audit coordinates disappear.
It is how many distinct lower and upper envelopes must be made compatible.
Iterating the theorem is semantically valid, but these sign counts can grow
at later stages; no inexpensive block-elimination theorem is claimed here.

The same description offers a non-flat alternative: retain the two envelope
families and the zero rows. Membership evaluates their extrema in linear
row work. If lower>upper, the maximizing lower and minimizing upper rows
supply a violated projected cut with a two-row certificate. This generates
the quadratic dictionary without storing all pairs. It retains envelope
information; it is not a claim that the evidence has vanished.

This envelope alternative is an analytical representation consequence here;
the executable compiler below materializes pairs before compaction.

## 4. Certified compaction, not heuristic row deletion

The compiler first merges proportional normals, retaining the tightest bound,
and drops true constant inequalities. It may then ask an exact LP backend
for redundancy proofs. Every final row retains a nonnegative combination of
expected fine rows proving its validity after elimination.

For the reverse direction, the final presentation supplies a checked bound
or contradiction certificate for EVERY raw pair/zero inequality. It is not
enough to verify each retained row independently: that would permit dropping
necessary constraints and enlarging the public image.

The LP helper uses nonnegative public variables. Explicit nonnegativity rows
remain in the intermediate final presentation, so its componentwise dual
normal inequalities have a valid interpretation.

The public runtime still has its coarse source generator. Any final row whose
bound already follows from that generator's exact support function need not
be retained as new evidence. The verifier checks that omission directly.
All remaining rows become the new public frame tuple.

A backend failure is not evidence of redundancy. Unsuccessful proposals leave
the row in place; if a final implication cannot be certified, its valid raw
row is restored. Thus a proposal failure can reduce compaction quality without
invalidating exact elimination. The returned certificates, not the solver's
reputation, are the acceptance boundary. This workload includes a pruning
proposal raising InfeasibleLPError; it was refused, not interpreted as a
mathematical inconsistency result. UnboundedLPError proposals were likewise
not used to delete rows.

## 5. Quadratic growth inside the owning m=4 source

Fix fine audits B={0,1} and retain only atom 1 publicly. The fine joint image
has dimension four: the two remaining slopes are distinct. At the source
center t_j=(100+2j)/2, let its joint image be c and set delta=128^-4. Define
normalized affine coordinates by

    (U,V,t_0,t_1) = c + delta*(x,y,H,z).

Here H is the coordinate being retired. The box

    -1<=x,y<=1,  -4<=H,z<=4

lies strictly inside the fine joint source image. The checker supplies strict
source-interior lifts for all 16 corners. Convexity proves inclusion of the
entire box. These local coordinates define rational linear evidence on the
original moments and audit values; they do not change the source or assert
an accuracy comparison in a rescaled norm.

For n>=2 let a_i=(2i+1-n)/n, i=0,...,n-1, and define

    f_n(x) = max_i (2a_i*x-a_i^2),
    g_n(y) = max_j (2a_j*y-a_j^2).

Add the 2n inequalities

    H >= 2a_i*x-a_i^2,
    H <= z-2a_j*y+a_j^2,

and the eight local-box rows. Since -1<=f_n,g_n<=1 on their intervals,
retiring H gives EXACTLY

    -1<=x,y<=1,
    f_n(x)+g_n(y) <= z <= 4.

For the converse, choose H=f_n(x). It obeys all lower bounds, all upper
bounds and its box caps. The lower z box bound is redundant.

The flat description has n^2 pair planes

    2a_i*x+2a_j*y-z <= a_i^2+a_j^2,

plus five box walls. All are facets. For each pair (i,j), the point
(a_i,a_j,a_i^2+a_j^2) lies on that plane and strictly inside all other pair
inequalities and box walls. Lowering z by 2/n^2 violates only that pair row.
The four x/y walls and z=4 likewise have points strict in every other row.
The point (0,0,3) proves full dimensionality.

Therefore the projected polytope has exactly n^2+5 facets. The witness points
are inside the coarse source image, so a source generator plus a flat tuple
of public linear evidence must still supply these facets.

At n=16: 40 fine evidence rows yield 261 public facets. This establishes
quadratic worst-case output growth for one-audit elimination in the declared
flat halfspace class. It is not merely a count of redundant generated pairs.

It is NOT an information-theoretic lower bound on every representation.
The envelope expression above has O(n) affine pieces, and a program can
encode regular knot families still more compactly. Nor should quadratic
facet growth be inferred for a two-dimensional public polygon from raw
pair counts alone: this construction has a three-dimensional public image.

## 6. Executable controls and actual resource ledger

Five proof packets cover forced-zero tails, one-sided audit evidence, coupling
to a surviving audit, an all-audits lower-dimensional image, and inconsistency.
For each, independent replay checks both projection inclusions. Additional
query certificates compare fine and compiled public optima, and admitted
public points receive fine witness extensions.

The size convention is compact JSON bytes for the specified state descriptor
including a fixed source binding, schema and frame tuple. It excludes the
shared source program and does not claim a canonical minimum encoding.

| Case | Old live state | New live state | Projection proof |
| --- | ---: | ---: | ---: |
| Forced-zero tail | 228 | 186 | 3,931 |
| One-sided evidence | 229 | 196 | 4,825 |
| Coupled surviving audit | 245 | 355 | 7,150 |
| Lower-dimensional all-audits case | 201 | 238 | 3,553 |
| Inconsistent history | 153 | 148 | 2,403 |

For the forced-zero control, the old evidence is U=t_0 and t_0<=1.
The compiled new evidence is U-V<=0 and -U+128V<=127. The coarse source
already implies V<=U, so these say U=V<=1. Two public frames replace three
fine frames, without retaining the retired coordinate in the live schema.

These are genuine reductions in the declared LIVE descriptor for three
controls, and increases for two. They are not total-system storage savings:
retaining the original context and projection proof costs more here. If the
application requires replayable provenance, its archive, transition proof and
verification context remain charged. This work authorizes no deletion of an
external evidence archive. A verified projection is a typed representation
transition, not silently dropping historical frames.

The quadratic controls check n=2,3,4,8,16, including strict facet and exclusive
violation witnesses. The all-n theorem follows from the formulas, not those
five instances.

## 7. Independent verification and scope

`verify_audit_elimination.py` imports neither the compiler, joint query engine
nor an LP solver. It reconstructs the fine source dictionary and every
expected evidence row; checks forward row combinations and reverse implication
certificates; checks source-support omissions; and verifies query certificates
and source witness extensions by exact rational arithmetic.

Five attacks are rejected: a negative forward multiplier, an omitted reverse
obligation, a dropped runtime frame, changed expected history and the wrong
public schema. Optimized Python execution is refused because the research
verifier uses assertions.

Files:

- `checkers/audit_elimination.py`
- `checkers/check_audit_elimination.py`
- `checkers/verify_audit_elimination.py`
- `results/audit-elimination-contract.json`
- `results/audit-elimination.json.gz`

Reproduce:

    uv run --with sympy python research/grothendieck/checkers/check_audit_elimination.py
    python research/grothendieck/checkers/verify_audit_elimination.py

The expected state is supplied by the frozen experimental contract, not the
answer packet. Hashes bind versions, not observation authenticity. The owning
analytical source is inherited; these runs do not freshly prove upstream
source admission, extend to prime-realizable sources, or modify Nima's API.
No noisy-audit inference, physical observation or witness interchange is
claimed.

## Synthesis

Exact audit retirement can replace fine evidence with a smaller public
presentation, with checkable proofs of ALL public-query preservation. But
flattening evidence into surviving-coordinate halfspaces can itself require
quadratic expansion, even in a fixed owning source.

The constructive design choice is therefore between a flat compiled summary
and a generated envelope-compatibility relation, with live state, proof,
archive and query work charged separately. The next structural question is
when block retirement admits a controlled envelope representation rather than
repeated uncontrolled pair expansion.

# Three-contact parity law

## Model and scope

The carrier is the Cayley graph on F₂⁶ with A-directions
`{1,2,4,8,16,32,63}`; B means nonadjacency. The B-group size limit is 22.
In the lower half `{0,…,31}`, square cell c is `{4c,4c+1,4c+2,4c+3}`.
Three births use three ordered pairs of cells `(a_i,b_i)`, with all six cells
distinct. At `x=4a`, delete A-edges `(x,x+1),(x+2,x+3)` and add `(x,x+3)`.
At `y=4b`, delete `(y,y+2),(y+1,y+3)` and add `(y+1,y+2)`.
The newborn's A-ports are `{x+1,x+2,y,y+3}`.

All edits are fixed before testing any subset of newborn vertices. This
prevents a change in the old carrier being misidentified as a higher-order
obstruction among a fixed set of births.

## Contact criterion

The directions connecting the two halves send a lower vertex v to upper
vertices `32+v` and `32+(v xor 31)`. Thus v and `v xor 31` have exactly the
same two upper contacts. On square cells this pairs `c` with `c xor 7`.
Write `[c]={c,c xor 7}`. There are four classes:
`{0,7},{1,6},{2,5},{3,4}`.

For an old B-witness to avoid a birth's ports, the first edited square must
use a low-bit position of even parity, and the second must use one of odd
parity. Introduce a bit p on each of the four antipodal classes. The equations
are

    p_[a_i] = 0,    p_[b_i] = 1   (i=0,1,2).

They have a solution exactly when

    { [a_0],[a_1],[a_2] } ∩ { [b_0],[b_1],[b_2] } = ∅.

This test uses only oriented contact incidence. No common-link capacity is
an input.

## Constructive proof of obstruction

Assume the equations have a solution. For c in F₂³, let e(c) be the parity
of its three bits. Choose the low-bit position

    t(c) = e(c) + 2(e(c) xor p_[c]),
    I = {4c+t(c): c=0,…,7}.

Exactly one vertex is selected per square. A cube edge between different
squares flips e(c), so its endpoints cannot both be selected at the same
low-bit position. Square edits cannot create an edge inside I, because I
contains only one vertex in each square. Thus I is an old B-group.

Since e(c xor 7)=e(c) xor 1 and p_[c xor 7]=p_[c],
`t(c xor 7)=t(c) xor 3`. Hence I is closed under v→v xor 31 and contains
four antipodal pairs. It avoids every birth port by the defining equations.

In the intact upper Q5 choose

    J = {32+v: 0≤v<32, parity(v)=0, v∉I}.

I contains four even and four odd vertices, so |J|=16−4=12. J is internally
B-connected by cube parity. Both possible lower contacts of an upper vertex
of J are excluded from I. Therefore I∪J is a B-group of size 8+12=20 that
avoids all newborn A-ports. Adding three mutually B-connected newborns gives
a forbidden B-group of 23.

This direction of the result is a direct proof, with no maximum-independent-
set or common-link computation.

## Original example

Take `(3,6),(7,5),(0,1)` and let ε_i reverse the ith ordered pair. The parity
equations become

    p_3 = ε_0,     p_1 = 1 xor ε_0,
    p_0 = ε_1,     p_2 = 1 xor ε_1,
    p_0 = ε_2,     p_1 = 1 xor ε_2.

They are consistent precisely when ε_0=ε_1=ε_2. The aligned orientations
000 and 111 therefore produce explicit B23 witnesses.

For 000, one such witness is

    {0,5,9,12,19,22,26,31,35,38,42,47,49,50,52,55,56,59,61,62,
     64,65,66}.

The first 20 entries are old vertices and the last three are newborns.

## Necessity in the finite family: exhaustive independent certification

There are choose(8,6)·15=420 unordered choices of three disjoint cell pairs,
and eight orientations per choice, for 3,360 oriented arrangements.
Permuting the three cell-index coordinates, translating them, and applying
the simultaneous low-coordinate reversal divides these into 56 symmetry
orbits. These transformations preserve the full old graph and all port maps.

The independent audit enumerates independent states on the lower half and
uses exact bipartite matching on the upper half. Every single birth has old
link capacity 21, every pair has capacity 20 or 21, and every triple has
capacity 19 or 20; the edited old carrier always has capacity 22.

Results over all 3,360 arrangements:

| Type | Count |
|---|---:|
| Some B-pair of newborns is already obstructed | 816 |
| Every B-pair is admissible, but the B-triple is obstructed | 576 |
| All newborn subsets are admissible as B-groups | 1,968 |

The parity equations are consistent in exactly the 576 genuinely ternary
cases, with no exceptions. In particular, among arrangements with all pairs
admissible, they are necessary and sufficient for triple obstruction.
Sufficiency is the constructive argument above. Necessity is presently
established by the exhaustive finite audit, not by a dimension-independent
structural proof.

For the original three-contact example, all pairs are admissible. Its link
deficit is therefore min(|T|,2) for aligned orientations and |T| for mixed
orientations. The compatibility complex is ∂Δ² in the first case and Δ² in
the second. This is a statement about a full triangle boundary, not a Kan
horn: a two-dimensional horn has only two of the three boundary edges.

## Contact-graph interpretation

Collapse the eight square cells to their four antipodal classes and retain
an arrow `[a_i]→[b_i]` for each birth. The parity equations require that each
class be only a source or only a target. The sources receive bit 0 and the
targets bit 1.

Since each cell is used at most once, each quotient vertex has degree at
most two. A consistent three-edge quotient can only be a four-vertex path
or a double edge plus a disjoint edge. These admit two and four consistent
orientations, respectively. A loop or an odd cycle admits none.

Among the 420 unordered arrangements, 192 have two obstruction-producing
orientations, 48 have four, and 180 have none. This explains the earlier
sample's 0/2/4 pattern without fitting an orientation truth table.

## Reproduction

Run:

    python ramsey_three_contact_parity_law.py
    python ramsey_three_contact_parity_law.py --audit

The first run constructs and verifies all 576 B23 witnesses. The second
independently validates necessity in all 56 symmetry orbits and writes the
complete link-capacity audit to JSON. Both use only the Python standard
library.

This result is confined to the declared folded-7-cube three-birth family.
It does not assert a universal simplex-coherence law or a general formula
for Ramsey numbers.

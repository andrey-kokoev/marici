# Double-Rees First-Flip Transfer and the Aligned-Corner Spatial Gate

## Record

Date: 2026-08-15

Status: theorem proved for the universal double-Rees first-flip coefficient
correspondence. Its saturated product resolution and complementary
Koszul--Cech residues are canonical, but the four formal corners do not by
themselves select the two physical occurrence-normal alignments. Spatial
descent, the generic \(Q\) attachment, the framed mapping fiber, and parity
remain unconstructed. No graph admission is claimed.

## Independent occurrence and normal Rees pairs

Work over the polynomial base

\[
A=\mathbb Z[x_5,X_{D03},u_5,u_{D03},\ldots]
\]

with all four displayed parameters independent and regular. The occurrence
pair has primitive relation

\[
\boxed{(X_{D03},-x_5),}
\]

while the normal pair has primitive relation

\[
\boxed{(u_{D03},-u_5).}
\]

Equivalently, these are the labelled resolutions

\[
0\longrightarrow A
\xrightarrow{(X_{D03},-x_5)}A^2
\longrightarrow(x_5,X_{D03})\longrightarrow0
\]

and

\[
0\longrightarrow A
\xrightarrow{(u_{D03},-u_5)}A^2
\longrightarrow(u_5,u_{D03})\longrightarrow0.
\]

Neither an occurrence parameter nor a normal parameter is inverted in
\(A\).

## Exact saturated product totalization

Tensor the two resolutions with the product orientation. In degree one use

\[
(h_{x_5},h_{X_D},v_{u_5},v_{u_D}),
\]

and in degree zero order the four formal corners as

\[
(x_5,u_5),
\quad(x_5,u_D),
\quad(X_D,u_5),
\quad(X_D,u_D).
\]

The total complex has ranks

\[
\boxed{1\longrightarrow4\longrightarrow4.}
\]

Its top column, in the chosen degree-one order, is

\[
(X_D,-x_5,-u_D,u_5)^T,
\]

and the lower matrix is the signed tensor-product incidence. Direct symbolic
calculation gives

\[
d_1d_2=0.
\]

Both input relations and the product incidence are primitive. Since the two
regular pairs use independent variables,

\[
\operatorname{Tor}^{A}_{k>0}
\bigl((x_5,X_D),(u_5,u_D)\bigr)=0,
\]

the two intermediate homology groups vanish, and \(H_0\) is their product
ideal. Hence the totalization is exact, saturated, and torsion-free.

This is a full coefficient correspondence, not merely its exceptional
associated grade.

## Complementary residues and the mixed boundary

Use the oriented two-normal Koszul--Cech duality convention. The two endpoint
normal generators have complementary images

\[
\boxed{
\frac1{u_D},
\qquad
-\frac1{u_5}.
}
\]

The occurrence relation then maps to the mixed endpoint boundary

\[
\boxed{
\frac{X_D}{u_D}m_+
-
\frac{x_5}{u_5}v_+.
}
\]

These fractions are Cech representatives in their named localized summands,
not elements obtained by inverting \(u_5\) or \(u_D\) in the base ring.
They are also line-valued evaluations: the numerator occurrence lines and
denominator normal duals retain distinct provenance.

The relation between the two arms uses the unique simultaneous inverse

\[
\boxed{
\frac1{u_5u_D}
}
\]

in the double chart-overlap Cech object. This is the only place where both
normal inverses occur together. The polynomial source remains unlocalized.

## The overlap is forced

The double-overlap term is not an optional refinement. If it is deleted, the
two complementary endpoint residues have a nonzero Cech boundary with
primitive coefficient \(\pm1\). Consequently

\[
d^2_{\rm without\ overlap}\ne0.
\]

No rescaling can remove this failure, because the surviving coefficient is a
unit. Thus the middle overlap is forced by the chain equation.

The result has no positive Tor and no integer torsion. The overlap is a Cech
localization term, not hidden derived torsion.

## Four formal corners versus two physical alignments

The canonical product has four corners:

\[
\begin{matrix}
(x_5,u_5)&(x_5,u_D)\\
(X_D,u_5)&(X_D,u_D).
\end{matrix}
\]

Only the diagonal pairings

\[
\boxed{(x_5,u_5),\qquad(X_D,u_D)}
\]

have the intended physical occurrence-normal labels: the short occurrence
\(x_5\) is aligned with its short normal \(u_5\), and the long occurrence
\(X_D\) is aligned with its long normal \(u_D\).

The crossed corners

\[
(x_5,u_D),
\qquad
(X_D,u_5)
\]

are indispensable algebraic terms of the universal tensor square, but there
are no established entry-143 face/circle support states carrying those
crossed occurrence-normal identifications. They may not be declared physical
charts merely because they occur in the free product resolution.

This is not a contradiction. The universal product records all independent
choices; the physical interval requires a separately constructed diagonal
selection or transport.

## The missing aligned/weighted graph

To obtain the physical first-flip interval from the four-corner coefficient
square, geometry must supply an occurrence-normal aligned graph, weighted
diagonal, or nearby-cycle correspondence

\[
\Gamma_{\rm align}
\subset
\operatorname{Rees}(x_5,X_D)
\times
\operatorname{Rees}(u_5,u_D)
\]

whose two endpoint charts are the aligned corners and whose middle
specialization explains the forced double-overlap class. Such a graph must
derive, rather than assign:

- the pairing \(x_5\leftrightarrow u_5\) and
  \(X_D\leftrightarrow u_D\);
- the disposition of the crossed corners;
- the orientation of the complementary residues;
- the legal landing of \(1/(u_5u_D)\) in a support-graded overlap; and
- the first-flip line-valued counit of entry 167.

No such graph, weighted diagonal, or nearby-cycle comparison is constructed
by the checker. Therefore no graph admission is claimed.

## Entry-143 support boundary

The coefficient overlap is not automatically an existing costalk of entry
143. Its target states are indexed by actual noncrossing face labels and
circle sets \(H\subseteq S\). The two crossed corners lack those supports,
and no current descent morphism places the double-overlap term into the
facewise filtration while preserving all lower Cech boundaries.

The coefficient theorem therefore does not construct

\[
\alpha_{03},
\qquad
\operatorname{BC}^{\log}_{+;03},
\]

or any equivalent spatial extraordinary map. It proves the coefficient
shape and a necessary overlap that such a map must realize.

## Generic-Q and global boundary

The first-flip interval and its short endpoint lie in the peripheral
short-boundary support. The double-Rees transfer does not attach the
primitive \(p_{03}\), retain the pre-quotient \(q_J\), or map nontrivially to
the fixed entry-143 \(Q03\) leg.

The following remain unconstructed:

1. spatial descent of the double overlap to the varying-\(H\) entry-143
   support complex;
2. the aligned nearby-cycle graph and extraordinary endpoint counits;
3. compatibility with the full \(F03\) product-Rees square of entry 170;
4. the second central flip and generic \(Q\) attachment;
5. three-road normalization-sheet gluing and Beck--Chevalley cells; and
6. the endpoint-pointed mapping fiber.

Consequently reflection parity is undefined.

## Anti-circularity controls

- Do not delete the double-overlap term; this breaks \(d^2=0\) primitively.
- Do not treat Cech denominators as inversions in the polynomial base.
- Do not identify the two crossed corners with entry-143 support states.
- Do not select the aligned corners by asserting the desired physical
  interval; derive them from an independent graph or specialization.
- Do not infer a spatial costalk, \(p_{03}\), \(q_J\), generic \(Q\) leg,
  mapping fiber, parity, or graph admission from the coefficient
  totalization.
- Do not contract or quotient a lower overlap before checking its boundary.

## Falsifiers and scope

The coefficient theorem would be falsified by a nonprimitive occurrence or
normal syzygy, nonzero intermediate homology, positive Tor, integer torsion,
failure of \(d^2=0\), a different forced complementary residue, or a closed
complex after deleting the overlap.

The spatial boundary would be crossed by an independently constructed
aligned/weighted diagonal or nearby-cycle graph whose proper extraordinary
push--pull lands the overlap in legal entry-143 states, handles both crossed
corners, and glues to the full \(F03\) collar and nonzero generic \(Q\) leg.

No no-go is asserted for such an enlarged spatial correspondence. The
theorem is scoped to the universal double-Rees coefficient transfer.

## Provenance and exact certificate

The exact checker is

- `research/voevodsky/check_d03_double_rees_first_flip_transfer.rs`.

Its SHA-256 hash is

`d57bd6fc69a94d4b3869b5046fe8bc52e001dc8c9c1622eab1a32812a09dc64e`.

It verifies both primitive syzygies, the saturated exact
\(1\to4\to4\) product totalization, symbolic \(d^2=0\), vanishing positive
Tor and intermediate homology, absence of torsion, both complementary
residues, the mixed boundary, legal use of the double overlap, absence of
base inversion, and primitive failure after overlap deletion.

The four-corner physical-label audit uses entry 143's fixed face/circle
supports and entries 167--170's independently typed occurrence, normal, and
collar data. It is a boundary statement, not an extra checker claim.

## Next experiment

Construct an occurrence-normal aligned weighted diagonal or nearby-cycle
graph inside the double-Rees product. Require its endpoints to be
\((x_5,u_5)\) and \((X_D,u_D)\), and derive the crossed-corner transport and
the forced \(1/(u_5u_D)\) overlap without base inversion. Then build its
support-typed extraordinary push--pull to the full entry-143 \(F03\) collar,
attach \(p_{03}\), and test retention of \(q_J\) in the generic \(Q03\) leg.
Only afterward assemble the mapping fiber or evaluate parity.

## Outcome contract

~~~json
{
  "claim": "The independent occurrence and normal Rees syzygies have an exact saturated 1-to-4-to-4 product totalization; complementary Koszul-Cech duality produces residues 1/u_D and -1/u5, the mixed boundary (X_D/u_D)m-(x5/u5)v, and a forced legal double-overlap 1/(u5*u_D), while deleting that overlap breaks d squared primitively.",
  "status": "proved",
  "scope": "universal double-Rees first-flip coefficient correspondence only; no graph admission, spatial entry143 descent, generic Q attachment, mapping fiber, or parity",
  "assumptions": [
    "x5, X_D03, u5, and u_D03 are independent regular polynomial parameters.",
    "The ordered occurrence and normal pairs fix one global product orientation.",
    "Simultaneous inverse powers occur only in the named double-overlap Cech summand.",
    "Entry-143 support states retain their actual face and circle labels."
  ],
  "factorization": {
    "occurrence_syzygy": "(X_D03,-x5), primitive",
    "normal_syzygy": "(u_D03,-u5), primitive",
    "total_ranks": [1, 4, 4],
    "d_squared": "zero symbolically",
    "positive_Tor": "zero",
    "intermediate_homology": [0, 0],
    "torsion": "none",
    "complementary_residues": ["1/u_D03", "-1/u5"],
    "double_overlap": "1/(u5*u_D03), legal only in correspondence middle",
    "mixed_boundary": "(X_D03/u_D03)*m_plus-(x5/u5)*v_plus",
    "base_inversion": "none",
    "delete_overlap": "falsified: primitive nonzero d squared",
    "formal_corners": [["x5", "u5"], ["x5", "u_D03"], ["X_D03", "u5"], ["X_D03", "u_D03"]],
    "physical_aligned_corners": [["x5", "u5"], ["X_D03", "u_D03"]],
    "crossed_corner_entry143_supports": "absent",
    "aligned_weighted_nearby_cycle_graph": "unconstructed",
    "spatial_descent": "unconstructed",
    "generic_Q": "unconstructed",
    "mapping_fiber": "uninstantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_double_rees_first_flip_transfer.rs",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-167 First Central-Flip Line-Valued Counit and the Next-Flip Generic Gate.md",
    "src/ledger/20260815-168 Full Rees First-Flip Occurrence Kernel and the External Normal Gate.md",
    "src/ledger/20260815-170 Product-Rees F03 Square and the Forced Long-Normal Completion.md"
  ],
  "checker_sha256": "d57bd6fc69a94d4b3869b5046fe8bc52e001dc8c9c1622eab1a32812a09dc64e",
  "counterevidence": [
    "Deleting the double-overlap leaves a primitive nonzero Cech boundary.",
    "Only two of the four formal product corners have aligned physical occurrence-normal labels.",
    "The crossed corners have no established entry-143 face/circle support states.",
    "No spatial aligned graph or generic-Q attachment is constructed by the coefficient totalization."
  ],
  "next_experiment": "Construct an aligned weighted diagonal or nearby-cycle graph inside the double-Rees product, derive its crossed-corner transport and forced overlap, then push it extraordinarily to the full F03 collar and test p03/q_J generic-Q attachment before forming the mapping fiber or parity."
}
~~~

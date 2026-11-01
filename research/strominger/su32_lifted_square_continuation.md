# Su-32: lifted square tests and coherence of complete wire regroupings

Date: 2026-10-28.

## Evidence and result

The input is the user-supplied `su32-native-window-operation-v1.md`. It defines
an integer-labelled port graph and a complete, label-preserving operation on
420 wire values. It does not include the individual edge registry or a list of
native two-order release routes.

The following are mathematical deductions from that specification, with
bounded exact regression checks. They are not a replay of the native geometry.
The named repository checker and its receipt both returned HTTP 404 on the
accessible default branch. No inference of mathematical failure follows from
that retrieval result.

The new results are:

1. An exact, reference-independent criterion for equality of lifted route
   endpoints. It checks the whole terminal port, not only a cell or deck sum.
2. An all-finite-length composition theorem for complete, wire-preserving
   regroupings. This is equality of value maps, not identification of histories.
3. Proof that the earlier 4-by-4 ambient residue quotient loses every period
   displacement. Testing all 31 index-five covers still loses 5 Z^3.

Actual native square records evaluated: **0**. Native higher fillers verified:
**0**. The executable controls are explicitly synthetic.

## 1. Exact lifted endpoint test

The source generators and coordinate maps are

\[
g_i=\mathbf1-4e_i,\quad
\Lambda=\sum_{i=0}^{2}\mathbb Zg_i,\quad
a_i(t)=\frac{t_3-t_i}{4},\quad
L(b)=\sum_{i=0}^{2}b_i g_i.
\]

In these coordinates,

\[
a(g_0)=(1,0,0),\quad a(g_1)=(0,1,0),\quad
a(g_2)=(0,0,1),\quad a(g_3)=(-1,-1,-1).
\]

For an oriented source path gamma with edge translations t_e and traversal
signs epsilon_e, define

\[
\nu(\gamma)=\sum_{e\in\gamma}\epsilon_e a(t_e).
\]

If gamma begins at base port p and ends at base port q, its lift beginning at
(p,b) ends at

\[
(q,b+\nu(\gamma)).
\]

**Proof.** Each source edge adds its declared integer translation. Induct on
path length. Reversing an edge negates the translation. Since a and L are
inverse additive maps on Lambda, their use introduces no rounding or modulus.

For two routes gamma_1 and gamma_2 with the same initial port, let

\[
\Delta=\nu(\gamma_1)-\nu(\gamma_2).
\]

Their lifted endpoints are identical, at every initial lift b, precisely when

\[
q_1=q_2,\qquad \Delta=0.
\]

Here q includes the full face/axis/occurrence identity supplied by the source.
Two slots on one cell are not the same port. Coincident physical faces do not
by themselves identify distinct occurrence records.

For a common final port q, the source geometry convention F_q-L(b) gives the
physical translation difference -L(Delta). When the final ports differ, that
formula alone is not their physical difference; the difference of their face
representatives also matters.

For a two-edge square, the numerical part reduces to

\[
\Delta=a(t_1)+a(t_2)-a(t_3)-a(t_4).
\]

This verifies equality of lifted endpoints, not that the source admits a 2-cell
between the paths. This separation agrees with the standard voltage-graph
construction; see Hubard, Mochan and Montero, *Voltage Operations on Maniplexes,
Polytopes and Maps*, Combinatorica 43 (2023), Section 2.1, DOI
10.1007/s00493-023-00018-7.

### Independence of representative choice

Change lifted coordinates by b'=b+s(p), and change representative geometry by
F'_p=F_p+L(s(p)). The same physical occurrence is preserved. An edge p to q then
has new deck label

\[
\tau'_e=\tau_e+s(q)-s(p).
\]

The additional terms telescope along a route. For parallel routes, both receive
the same s(q)-s(p), so Delta is unchanged. A nonzero discrepancy cannot be
removed by changing representatives.

### Why testing only constant translations is insufficient

The constant deck shifts commute because Z^3 is abelian. All 24 signed
pairs drawn from distinct g_i therefore pass the additive square test. This
does not test actual release operations: their target ports or translations
may depend on the current port.

For operations of the form

\[
U(p,b)=(u(p),b+\tau_U(p)),\qquad
V(p,b)=(v(p),b+\tau_V(p)),
\]

both orders must be defined, their port maps must agree, and the deck condition
is

\[
\tau_U(p)+\tau_V(u(p))=
\tau_V(p)+\tau_U(v(p)).
\]

Commutativity of Z^3 does not remove this dependence on p.

## 2. Complete regroupings have derived composition coherence

Let W be the exact set of 420 complete lifted-wire identities asserted by the
source note. For a permitted complete presentation A, let S_A be its slots and
lambda_A:S_A to W its bijection identifying the wire at each slot. Let X be any
set of opaque wire values. Reading a wire assignment in presentation A is

\[
R_A:X^W\longrightarrow X^{S_A},\qquad
R_A(f)=f\circ\lambda_A.
\]

Because lambda_A is a bijection, R_A is invertible. The source specification of
reconstructing the wire assignment and presenting it at other endpoints is
exactly the value-level map

\[
C_{AB}=R_B\circ R_A^{-1}.
\]

For three complete presentations,

\[
C_{BC}\circ C_{AB}
=R_C\circ R_B^{-1}\circ R_B\circ R_A^{-1}
=R_C\circ R_A^{-1}
=C_{AC}.
\]

Also C_AA is the identity and C_BA is inverse to C_AB. Repeated cancellation
proves, for every finite sequence of permitted complete presentations,

\[
C_{A_{n-1}A_n}\circ\cdots\circ C_{A_0A_1}
=C_{A_0A_n}.
\]

No extra numerical mixing law or value-level square/pentagon equation is
needed. The equations follow from the shared exact wire assignment and the
specified regrouping constructor.

**Scope.** The source explicitly supplies the P-plus-boundary and
E-plus-boundary presentations and the intermediate wire assignment. The proof
applies to any further presentation only once its complete bijection to the
same W is established. It does not prove that a proposed release operation is
admitted, or that an extension changing W belongs to this class.

The two construction histories remain different records. The proof establishes
equality of the functions they induce on wire values, not equality or
contractibility of the types of retained histories. A native constructor for a
comparison between the histories remains a separate operation. Nor does a
commutative diagram of presentations constitute a geometric square cell by
itself.

### Exact test with opaque values

For label-only copy maps, assign each input slot its distinct exact lifted-wire
ID. Two output tables agree for all possible opaque values if and only if they
agree on these identity tags. The forward implication follows by choosing that
tag set as X; the reverse follows by substituting any value for each tag.

This is stronger than testing several numerical payloads. It is valid only
when the operations really are label-only copying, as asserted in the note.
It must use full lifted-wire identity, not a repeated base-wire ID.

### Boundary and state-domain condition

Completeness is essential. The native P and E presentations each have
320 internal slots plus 100 boundary slots. Removing the boundary slots
invalidates R_A inverse on unrestricted lifted states. The source's 100
independent omitted inputs give direct counterexamples to reconstruction.

On the restricted periodic image, an analogous argument uses the 64 base-wire
values and the consistency constraints stated in the source. That is a
different state domain, not a proof of independence for all 320 internal slots.

## 3. The 4-by-4 quotient cannot detect native deck discrepancies

The previous audit introduced the ambient root lattice

\[
A_3=\{t\in\mathbb Z^4:\sum_i t_i=0\}
\]

and computed A_3/Lambda isomorphic to (Z/4)^2. An explicit quotient map is

\[
\phi(t)=((t_0-t_3)\bmod4,(t_1-t_3)\bmod4).
\]

For every deck vector Delta, L(Delta) belongs to Lambda, hence

\[
\phi(L(\Delta))=(0,0).
\]

For example, Delta=(1,0,0) is a genuine nonzero lift displacement, while
L(Delta)=g_0 has zero image under phi. Thus even an arbitrarily large native
period displacement is invisible in this residue quotient. This is not merely
a possibility of four-step aliasing.

**Correction of interpretation.** The 16-class ambient quotient is an algebraic
construction from the supplied period vectors. The uploaded note does not give
the map identifying those classes with its sixteen physical residue types, or
identify two quotient generators with native P/E release operations. The earlier
chat's claim that this independently explains the physical residue inventory
was too strong. The algebraic quotient result remains valid.

The proposed 4-by-4 chart may still be useful as an explicitly chosen encoding.
Its agreement cannot establish equality of native lifted occurrences.

## 4. Even all index-five covers leave an exact blind subgroup

For a nonzero covector ell over F_5, the index-five cover detects Delta only
through ell(Delta mod 5). There are (5^3-1)/(5-1)=31 kernels.

For a nonzero vector v in F_5^3, its annihilator has dimension two and therefore
contains six projective covectors. Consequently a nonzero residue is hidden by
exactly six of the 31 covers and detected by 25. The zero residue is hidden by
all 31. Equivalently,

\[
\bigcap_{[\ell]\in\mathbb P^2(\mathbb F_5)}
\ker(\ell:\mathbb Z^3\to\mathbb F_5)=5\mathbb Z^3.
\]

Delta=(5,0,0) is a nonzero integer displacement which passes the endpoint-deck
part of every index-five cover test. This does not dispute the uploaded note's
reported physical-cell collisions. It identifies a different limitation of
finite-cover checks as certificates of integer-lift closure.

## 5. Endpoint closure does not supply a geometric filler

The synthetic positive control has routes a;b and c;d around a four-edge cycle.
They end at the same lifted port with Delta=0. The closed word

\[
a\,b\,d^{-1}\,c^{-1}
\]

has no cancellable inverse edge pair. In the graph with no attached 2-cells, it
is a nontrivial reduced loop. Adding a disk along it changes the complex; that
disk is not supplied by the fact that the deck sum is zero.

Thus three separate questions remain visible: lifted endpoint equality,
equality of opaque-value maps, and a retained native comparison/filler.
The calculations here solve the arithmetic criterion and the complete
regrouping value theorem, not the final constructor question.

## 6. Execution record

`audit.py` completed 16,547 assertions with the Python standard library. They
include 729 bounded lattice round trips, 24 signed translation squares, all
125 F_5^3 visibility cases, all 24^3 triples of four-wire presentation
permutations, inverse checks, representative-change controls and malformed
route rejections. These are supporting finite checks; the all-integer and
all-finite-length statements above use the written proofs.

Four synthetic route controls give:

| Control | Terminal ports equal | Delta | Verdict |
|---|---|---|---|
| commuting translations | yes | (0,0,0) | same lifted endpoint |
| wrong deck translation | yes | (0,0,-1) | different lifted occurrences |
| wrong axis port | no | (0,0,0) | not parallel |
| hidden in every index-five cover | yes | (-5,0,0) | different lifted occurrences |

Both route words remain in each result. No control is labelled native. The
actual checker and receipt were not available, so no list of actual Su-32
square discrepancies has been calculated.

Native repository requests attempted:

- `research/strominger/checkers/check_su32_native_window_operation.mjs`: 404.
- `research/strominger/results/su32-native-window-operation-v1/verification.json`: 404.

Library retrieval returned the supplied specification and prior analysis notes,
not the native edge and release-route tables. The input contract in this package
accepts those tables without choosing a finite sheet reduction or deleting
histories. Source selection and higher-witness verification remain explicitly
outside that arithmetic checker.

No native repository files were changed. No proof assistant was run. No
n-Segal, coskeletality or Hopf-fibration claim is established by this audit.

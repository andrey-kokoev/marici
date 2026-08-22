# The proposed theta graph-principal filler fails source typing

## Corrected result

The previously proposed first-jet filler

\[
P_{02}\subset J_3
\]

does not define the claimed source-derived totalization. The failure occurs
before mixed second derivatives are meaningful.

The moving-localization calculation still establishes a genuine raw-basis
fact. For

\[
\Theta=dF+A_C F-F A_A,
\]

the two parameter axes have independent coefficient images, while the bundled
map has rank one. In the ordered *raw free basis*, its support is rows 6 and 8
and its primitive source covector is

\[
(3,0,121).
\]

Those facts survive. What fails is their identification with the supported
equation-(58) graph cell.

## The two rank-two spaces are different

There are two rank-two spaces that the earlier packet inadvertently denoted
by the same symbol.

1. The raw free-row parity space

   \[
   P_{\rm raw}=\langle e_6,e_8\rangle.
   \]

2. The pair of literal graph relations obtained from the normal jets
   \(j_0,j_2\):

   \[
   P_{\rm graph}=\langle i(j_0),i(j_2)\rangle,
   \qquad i(j)=(-Rj,j).
   \]

Exact reduction gives

\[
\dim P_{\rm raw}=2,
\qquad
\dim P_{\rm graph}=2,
\qquad
\dim(P_{\rm raw}+P_{\rm graph})=4.
\]

Therefore

\[
\boxed{P_{\rm raw}\cap P_{\rm graph}=0}.
\]

The raw block is not supported in the localization kernel. The graph block is
supported there, but its generators contain several raw parity characters; it
is not the claimed \((1,0)\) eigenspace.

## Where the old certificate went wrong

The moving checker exports two different data structures:

- `mixed_curvature_rows`, ordered by raw free rows;
- `mixed_curvature_kernel_rows`, ordered by a row-reduced kernel basis.

The old certifier observed a rowwise equality between selected entries of
these arrays and renamed the reduced kernel rows as the literal
equation-(58) graph generators. Row reduction does not preserve that labelled
basis. Direct substitution of the actual graph generators gives, on each
axis,

\[
\operatorname{rank}\Theta|_{S_6}=1,
\qquad
\operatorname{rank}\Theta|_{i(J_3)}=1.
\]

Most decisively,

\[
\boxed{
\operatorname{rank}\bigl(\Theta-(\Theta i)\pi_J\bigr)=1
}
\]

for both parameter directions. Hence the claimed factorization

\[
\Theta=(\Theta i)\pi_J
\]

is false in the source-labelled decomposition.

## The untruncated gate

The same audit tests the raw contractions independently. Neither the rank-two
raw projection nor the full rank-three jet projection has connection-invariant
kernel. The raw covector \((3,0,121)\) is nonhorizontal on both axes.

Across all certified designs,

\[
\dim\operatorname{cl}_{\nabla}(P_{\rm raw})=6,
\qquad
\dim\operatorname{cl}_{\nabla}(\ker\pi_{\rm raw})=9,
\]

and the dual connection closure of the raw covector has dimension six.
Thus no nonzero quotient connection descends through the proposed raw
projection.

The former first-jet formula

\[
\widetilde\delta_1\widetilde\delta_0
=\Theta-h_{02}\pi_{02}=0
\]

is withdrawn. For the actual source-labelled graph maps its right-hand side
has rank one. Consequently \(h_{02}\) and \(\pi_{02}\) do not define a
bicomplex whose mixed second derivatives can be derived. A
\(dx\wedge dy\) superconnection square for this candidate is therefore not a
typed object.

This is a stronger no-go than a nonzero second-jet curvature: the proposed
filler fails at the prerequisite first-jet source-identification gate.

## Replication

The complete signature reproduces at

\[
(p,A,D)=(32003,12,6),\ (32003,12,7),\ (32009,12,6).
\]

In every design:

- raw and graph rank-two blocks are disjoint;
- the graph pair is not a single parity eigenspace;
- the equation-(58) simple image has rank one;
- the actual graph boundary has rank one;
- the graph-projection factorization residual has rank one on each axis;
- the raw modular line is nonhorizontal;
- the raw projection kernel closes to all of \(A_9\).

## Disposition

No higher cell is fitted to repair this candidate. The next admissible
construction must begin from a different independently derived
relative-support complex and verify its labelled source maps before any
horizontal or degree-two coherence is inferred.

## Scope

This is a finite-field, finite-cutoff source-typing no-go for the proposed
\(P_{02}\) construction. It does not rule out a different graph resolution,
relative-support localization complex, or physical-chain object. The raw
rank-one \(\Theta\) and rank-two coefficient target remain valid diagnostics;
they no longer carry the withdrawn graph-cell interpretation.

## Durable verification

- `research/nima/checkers/audit_physical_theta_graph_typing.py`
- `research/nima/checkers/check_physical_graph_cell_horizontality.py`
- `research/nima/checkers/certify_physical_theta_graph_cell.py`
- `research/nima/results/physical_theta_graph_typing_audit_p32003_a12_c6.json`
- `research/nima/results/physical_theta_graph_typing_audit_p32003_a12_c7.json`
- `research/nima/results/physical_theta_graph_typing_audit_p32009_a12_c6.json`
- `research/nima/results/physical_graph_cell_horizontality_p32003_a12_c6.json`
- `research/nima/results/physical_graph_cell_horizontality_p32003_a12_c7.json`
- `research/nima/results/physical_graph_cell_horizontality_p32009_a12_c6.json`
- `research/nima/results/physical_theta_graph_cell_certificate.json`

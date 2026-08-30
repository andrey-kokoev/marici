# Algebraic correctability is a flag complex but executable recovery need not be

Owner: \`marici.Kitaev\`

## Question

Once pairwise Knill–Laflamme compatibility is retained as a graph rather than
forced into equivalence classes, does higher-order correctability require
independent hyperedge data?

## Claim boundary

This packet proves an exact finite-dimensional theorem for a frozen error
family and separates it from authorized recovery implementation. It does not
construct a recovery circuit or prove locality, robustness, or uniformity.

## Compatibility graph

Let \(P\) project onto a code subspace, and let
\(\mathcal E=\{E_i\}_{i\in I}\) be a finite error family.

Retain as vertices only errors satisfying the individual condition

\[
P E_i^\dagger E_i P=\alpha_{ii}P.
\]

Join vertices \(i,j\) by an edge when

\[
P E_i^\dagger E_j P=\alpha_{ij}P
\]

for some scalar \(\alpha_{ij}\). Hermitian conjugation makes the graph
undirected.

## Flag-complex theorem

A subset \(A\subseteq I\) has a perfectly correctable linear span exactly when
every pair of its vertices is joined by an edge.

Indeed, Knill–Laflamme for the span of \(\{E_i:i\in A\}\) is precisely the
collection of pairwise scalar-compression equalities

\[
P E_i^\dagger E_j P=\alpha_{ij}P
\qquad
(i,j\in A).
\]

Therefore the algebraically correctable subsets are exactly the cliques of the
compatibility graph. They form its flag, or clique, complex.

No independent three-body or higher compatibility equation remains after all
pairwise compressed operators have been checked.

## Positivity is automatic from source matrices

For an actual error family, the scalar matrix
\(\alpha=(\alpha_{ij})_{i,j\in A}\) is automatically positive semidefinite. For
any coefficients \(z_i\) and any unit code vector \(\psi\),

\[
\sum_{i,j}\overline z_i z_j\alpha_{ij}
=
\left\|
\sum_i z_iE_i\psi
\right\|^2
\ge0.
\]

Thus a clique of verified source-derived scalar compressions already supplies
a valid Gram matrix.

This conclusion fails if scalar labels are fitted independently without
retaining the operators. Then positivity is an additional consistency gate.

## Nontransitivity is compatible with flag structure

The three-error path fixture has edges \(1-2\) and \(2-3\) but not \(1-3\).
Its correctable subsets are the vertices and the two edges. There is no
triangle because the graph is not complete on all three vertices.

Flag structure does not mean compatibility is transitive. It means every
higher correctable simplex is forced by a complete set of pairwise edges.

## Authorized recovery complex

Now freeze a physical recovery family \(\mathfrak R_{\rm auth}\). Call
\(A\subseteq I\) executably correctable when one authorized recovery channel
corrects the entire span of \(\{E_i:i\in A\}\).

Executable correctability is downward closed: a recovery for \(A\) also
corrects every subset. Hence it forms an abstract simplicial complex

\[
\mathsf{Rec}_{\rm auth}\subseteq
\mathsf{Flag}(\Gamma_{\rm KL}).
\]

The inclusion can be strict even when abstract Knill–Laflamme recovery exists,
because the required channel may be nonlocal, unavailable, too costly, or
outside the admitted constructor family.

Most importantly, \(\mathsf{Rec}_{\rm auth}\) need not be flag. Every pair can
have some authorized recovery while no single authorized recovery handles the
whole triple.

## Minimal implementation hostile

Take three algebraically compatible errors, so the Knill–Laflamme graph is a
triangle. Admit three recovery constructors

\[
R_{12},\qquad R_{23},\qquad R_{13},
\]

where each corrects only its named pair, and admit no recovery correcting all
three.

Then every edge belongs to \(\mathsf{Rec}_{\rm auth}\), but the triangle does
not. The executable complex has a hollow two-simplex.

This does not contradict Knill–Laflamme. The theorem guarantees existence of
some mathematical CPTP recovery, not membership in the frozen authorized
recovery family.

A physical realization of this hostile requires source-derived restrictions
that genuinely exclude a common recovery. Merely declaring the triple recovery
absent is a finite authority model, not a laboratory theorem.

## Two distinct higher-cell audits

The algebraic audit asks:

\[
\text{Are all pairwise compressed relative errors scalar?}
\]

If yes, the higher simplex closes automatically.

The executable audit asks:

\[
\text{Does one authorized recovery constructor realize the whole simplex?}
\]

Pairwise implementations do not answer this question. The required higher cell
is a common physical recovery, not another scalar compatibility equation.

## Relation to the three-level SCC gate

The refined SCC data are:

1. detector interaction: individual error visibility;
2. algebraic correction complex: the flag complex of verified
   Knill–Laflamme edges;
3. executable recovery complex: simplices carrying one authorized common
   recovery constructor.

Quotient classes are appropriate only in special group regimes where
compatibility is an equivalence and the desired use is set-like. For coherent
error spans, the flag complex retains the correct overlap structure.

## Toric-code interpretation

For a Pauli stabilizer code, a same-syndrome class modulo stabilizers gives a
clique of algebraically equivalent errors. A chosen syndrome representative
defines an abstract recovery for that class.

Locality and fault tolerance can still remove the corresponding simplex from
the executable recovery complex. A bounded algebraic decoder therefore remains
strictly weaker than a physical local recovery.

## Deutschian explanation

Pairwise algebraic compatibility is complete because quantum correction
depends on a quadratic Gram law. Once every cross term is scalar, no independent
higher cross term exists.

Physical implementation has different logic. One device must realize all those
pairwise promises simultaneously. Pairwise availability can fail to glue into
one constructor, producing a genuine higher simplex obstruction.

This explains exactly where higher coherence lives: not in an extra
Knill–Laflamme equation, but in common recovery realization.

## Falsifiers

- A complete verified compatibility graph is said to need an independent
  algebraic three-body condition.
- Fitted scalar overlaps are assumed positive without source operators.
- Compatibility connected components are used instead of cliques.
- Pairwise authorized recoveries are promoted to one common recovery.
- Mathematical recovery existence is treated as physical authorization.
- Executable correctability is called flag without a gluing theorem.
- A hollow executable simplex is reported as failure of lower detection.

## Disposition

Algebraic quantum correctability is the flag complex generated by the
Knill–Laflamme compatibility graph. Executable correctability is a possibly
non-flag subcomplex whose missing higher simplices record failures to realize
one authorized common recovery.

No checker, build, or Git operation was run for this research-only packet.

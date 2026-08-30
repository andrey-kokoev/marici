# Source-selector audit on the faithful flavor quotient (WP52)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Bounded question

Does a source-derived flavor operation select a proper subspace or distinguished
point of the admissible `physical16` lens family, rather than merely reading the
quotient or rigidifying a sparse presentation?

## Domain, quotient, and projection

The admitted state domain is the generic nondegenerate quark-Yukawa domain
((Y_u,Y_d)), modulo the full weak-basis group
(U(3)_Q\times U(3)_u\times U(3)_d). The faithful coordinate used here is

\[
\mathrm{physical16}=(m_u,\ldots,m_b; |V_{ij}|_{i,j=1}^3; J_{\rm signed}).
\]

The measured ten-coordinate projection retains the six masses,
(|V_{us}|,|V_{ub}|,|V_{cb}|), and signed (J). It is finite-to-one but not
injective.

## Largest presently authorized probe family

Two families must remain typed separately.

1. Weak-basis-invariant mass and CKM probes factor through the physical
   quotient. `physical16` is a faithful generic coordinate for the present
   tests. These probes are readouts, not selectors: evaluating them does not
   reduce the admissible state family without an independently declared
   dynamical condition.
2. On the 72 certified generation-exchange doublets, the independently
   derived involution (T) supplies the even/odd nerve

   \[
   \begin{pmatrix}1&1\\1&-1\end{pmatrix}.
   \]
   It separates the two sparse presentations. Since both presentations have
   the same `physical16`, this is a rigidifier of the lens fiber, not a
   selector of physical points.

Their contextual partitions are therefore different: quotient readouts
identify ({s,T(s)}), while the deck nerve splits it into singletons. The
union is not a physical probe family because the odd row does not descend.

## Exact hostile pair

Take exact PDG mixing parameters

\[
s_{12}=1/5,\quad s_{13}=1/20,\quad s_{23}=1/4,\quad
\sin\delta=3/5,
\]

with the two branches (cos\delta=\pm4/5), and hold the six masses fixed.
The measured ten coordinates agree exactly, including signed (J). The full
CKM modulus matrices do not: a single additional modulus, for example
(|V_{td}|^2), separates the branches exactly. This is the smallest hostile
falsifier of any uniqueness inference from measured ten.

## Descent and instrument gates

The quotient probes descend under the full weak-basis group. The sparse probe
does not: the exact (3/5,4/5) left-handed weak-basis rotation preserves all
audited invariant words while changing the nine-link support from (4+5) to
(5+7) nonzeros and changing the chart loop phase. Consequently the deck-odd
probe is undefined on another representative of the same physical orbit.

Masses and CKM amplitudes/CP violation have an experimental readout typing.
No admitted physical instrument implements the deck-odd chart probe. A
reference port could make a relative sheet label observable only by defining
a new relational experiment. Its objects would be pairs `(flavor state,
reference)` and its equivalences the stabilizer of that reference. It would
not reveal an absolute phase of the original flavor experiment.

## Disposition

No currently authorized operation is both a source-generated selector and a
map on `physical16`:

- `physical16` probes separate physical points but do not select them;
- measured ten creates a false uniqueness risk;
- the generation-exchange nerve rigidifies presentations but does not descend;
- purity stationarity is not promoted: it fails on the complete fitted
  ensemble and is not derived from a source action;
- no source action, RG normalization, positive conditional expectation, or
  instrumented relational probe has yet supplied a proper physical subfamily.

Thus the present classification is **rigidifier only, not selector**. The
remaining gate is a typed physical instrument for an independently derived
weak-basis-invariant operation whose fixed locus or image is a proper subset
of the admissible `physical16` family and whose prediction survives the full
fitted ensemble.

## Assumptions and falsifiers

Assumptions: nondegenerate ordered masses; unitary three-generation CKM
kinematics; `physical16` used only as a generic faithful coordinate; the
generation-exchange claims restricted to their certified 72-doublet domain.

Smallest exact falsifier: the two (cos\delta) branches above refute measured-ten
injectivity. A progressive falsifier of this packet would be an independently
derived operation that (i) descends under full weak-basis equivalence, (ii)
has a declared instrument, and (iii) removes at least one `physical16` class
before fitting its numerical value.

Verification: `uv run --with sympy python research/flavor/checkers/wp52_source_selector_audit.py`.
Generated result: `research/flavor/results/wp52_source_selector_audit.json`.

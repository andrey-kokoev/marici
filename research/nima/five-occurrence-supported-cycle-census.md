# Five-Occurrence Supported Cycles Have Exactly Two Primitive Shapes

The amplitude support calculation extends exactly to five labelled
occurrences.  For every one of the \(2^{10}=1024\) simple support graphs
\(G\), compute

\[
H_1(\operatorname{Cl}G)
=\ker\partial_1/\operatorname{im}\partial_2.
\]

The census gives

\[
\begin{array}{c|ccc}
\dim H_1&0&1&2\\
\hline
\#\text{ supports}&837&177&10.
\end{array}
\]

Exactly 27 supports are minimal under edge deletion while retaining nonzero
\(H_1\):

- 15 labelled chordless four-cycles with the fifth vertex isolated;
- 12 labelled chordless five-cycles.

Every minimal support carries one cycle.  More elaborate supports may carry
two independent directions, but the complete graph \(K_5\) again has
vanishing \(H_1\): its triangle cells fill every graph cycle.

Thus the primitive Carrier births at five occurrences have exactly two
shapes,

\[
\boxed{C_4\sqcup\{v\}\quad\text{and}\quad C_5.}
\]

The phase-valued coefficient records are characters in
\(H^1(\operatorname{Cl}G;U(1))\).  Whether a sector lens retains them as new
information remains a separate question, as the four-mode Gaussian
counterexample already demonstrates.

The census also shows that port availability is not monotone in the number of
relations.  Adding an edge may create a triangle two-cell that fills and
therefore destroys a previously supported cycle.  The relevant datum is the
typed incidence complex, not graph density.

The exact checker passes 7/7 gates.

Artifacts:

- `research/nima/five-occurrence-supported-cycle-census.md`
- `research/nima/checkers/check_five_occurrence_clique_homology.py`
- `research/nima/results/five-occurrence-clique-homology.json`

Sequence claim: `seqclaim-5931a0152bae3e6c0c89e153`.

# A cyclic physical source does not determine the terminal readout quotient

> **Rank correction.** The earlier rank-21 language was a cutoff-five
> plateau. The stabilized geometric marked-relative object has rank 26. The
> variance no-go below is unchanged and is now stated for that object.

The stabilized marked-relative packet establishes a rank-26 vector space
\(V\), a connection, and a literal source vector \(s\in V\) whose horizontal
orbit spans the full packet:

\[
\dim\langle s,\nabla s,\nabla^2s,\ldots\rangle=26.
\]

This is a controllability or cyclic-generation statement.  The dynamic
terminal readout problem has the opposite variance.  It requires a
source-derived physical covector

\[
R:V\longrightarrow W
\]

and the common kernel of its dual horizontal orbit.  Source cyclicity cannot
be converted into observability without a canonical nondegenerate pairing
identifying \(V\) with \(V^\vee\).

## Exact counterexample

Take

\[
A=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\qquad s=\binom10.
\]

Then \((s,As)\) has rank two, so \(s\) is cyclic.  Keeping the same \((A,s)\),
the three readouts

\[
0,\qquad (1,0),\qquad(0,1)
\]

have observability ranks \(0,1,2\), respectively.  Therefore even full source
cyclicity determines no terminal readout dimension.

## Cosmological consequence

The stabilized rank-26 source-orbit computation cannot establish either a
proper dynamic terminal quotient or full physical observability.  It proves
only that any connection-stable **subobject containing the source vector** is
the full calibrated packet.

The next admissible datum is not another orbit computation.  It is the
literal relative-chain pairing, descended as a covector on the same labelled
rank-26 quotient and checked for horizontal compatibility.  Until that exists,

\[
\boxed{\text{dynamic terminal physical readout: uncomputed}.}
\]

No basis pairing, coordinate dot product, or fitted dual vector may replace
that source-derived chain map.

## Reproducibility

- `research/nima/checkers/check_cyclic_source_readout_variance_gate.py`
- `research/nima/results/cyclic_source_readout_variance_gate.json`
- stabilized geometry and cyclicity: `research/nima/checkers/check_physical_marked_rank26_geometry.py`

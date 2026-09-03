# Singleton occurrence identity is not universally required for coherence

## Question

Must every coherent network retain every typed source occurrence as a singleton identity object?

## Symmetric countermodel

Let the source occurrence space be \(V=\mathbb Q^2\) with occurrences \(a,b\). Let

\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

exchange them. This transport is strictly unitary. Let every admitted downstream constructor and readout factor through the symmetric quotient

\[
q=\begin{pmatrix}1&1\end{pmatrix}:V\to\mathbb Q.
\]

Then

\[
qS=q.
\]

The kernel \(\langle(1,-1)\rangle\) is preserved and the entire admitted network descends coherently to the one-dimensional quotient. The individual occurrence selector

\[
E_a=\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

does not descend: \(qE_a=(1,0)\) is neither \(q\) nor zero. Thus the quotient network is coherent even though singleton occurrence identity has been forgotten.

## Distinguishing hostile

Add the asymmetric readout

\[
r=\begin{pmatrix}1&0\end{pmatrix}.
\]

Then \(rS\ne r\). The symmetric quotient no longer supports the declared readout, and occurrence forgetting becomes invalid.

## Exact criterion

Singleton occurrence selectors are necessary only relative to a family of constructors or readouts that jointly distinguishes those occurrences. If every admitted map coequalizes \(a\) and \(b\), their lawful identity object is the quotient class \([a]=[b]\), not either singleton.

The primitive identity anchor is therefore the minimal quotient on which all admitted constructors, transports, and readouts descend. Singleton occurrences survive precisely when the admitted family is jointly faithful on them.

## Consequence for the conjecture

The universal singleton formulation is false. The corrected conjecture is:

> The coherence network is fibred over its source-derived observational quotient. Occurrence selectors are retained exactly to the resolution jointly distinguished by admitted constructors and readouts; equivalence classes, not raw occurrences, are the identity objects below that resolution.

This does not license arbitrary occurrence forgetting. The six-to-three arithmetic example remains invalid because its incidence and torsion readout detect the forgotten directions.

## Verification

`research/aspect/checkers/check_occurrence_forgetting_coherent_quotient.py` checks the coherent symmetric quotient, failure of singleton-selector descent, and an asymmetric readout that detects forgetting using exact rational matrices.

## Disposition

The strongest conjecture is falsified. Retain identity at the jointly faithful quotient resolution, not automatically at singleton occurrence resolution.

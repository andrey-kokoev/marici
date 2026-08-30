# Gauge forgetting cannot be repaired downstream

## Question

Can additional outputs, downstream processing, or spectator ports recover a
distinction already erased by a gauge-invariant observation?

## Claim boundary

No. This packet proves the categorical and finite-linear obstruction. It does
not identify which additional source reference is physically available in any
particular sector.

## Coequalizer theorem

Let a group \(G\) act on a state object \(X\), and let

\[
q:X\longrightarrow Q
\]

be the quotient or coequalizer. Every gauge-invariant observation
\(h:X\to Y\) factors as \(h=\bar hq\). Consequently every downstream map
\(d:Y\to Z\) satisfies

\[
dh=d\bar hq.
\]

If \(q\) identifies two distinct states, no postcomposition of \(h\) can
separate them. Enlarging the output space, changing coordinates, adding
derived statistics, or duplicating measurements remains downstream of the
same quotient.

## Spectator-port obstruction

Appending a port that is independent of the unresolved gauge coordinate also
factors through \(q\). Calling it an input or reference port does not change
the theorem. Its source incidence must be nontrivial on the erased orbit.

A genuine repair is an additional source-derived map

\[
r:X\longrightarrow R
\]

such that the combined map

\[
(q,r):X\longrightarrow Q\times R
\]

is monic on the intended state class. Equivalently, \(r\) must separate every
nontrivial pair lying in one \(q\)-fiber. This is a jointly faithful reference
port, not output dilation.

## Exact linear model

Take \(X=\mathbb Q^2\), with the second coordinate representing the forgotten
gauge direction, and

\[
q=\begin{pmatrix}1&0\end{pmatrix}.
\]

For every downstream matrix \(D\), the composite \(Dq\) annihilates
\(e_2\). Any number of spectator rows proportional to \(q\), or zero on
\(e_2\), leaves rank one. The source-sensitive row

\[
r=\begin{pmatrix}0&1\end{pmatrix}
\]

makes \((q,r)\) full rank.

## Cross-sector interpretation

- In flavor, normalized rates quotient common gain. More normalized outputs
  cannot recover it; an independently calibrated luminosity or absolute source
  reference must couple to that direction.
- In reciprocal boundary characters, the scalar product quotients
  anti-diagonal rescaling. More scalar determinant readouts cannot select the
  frame; exchange and augmentation must be source-derived and gauge-sensitive.
- In Aspect’s colligation audit, appending spectator columns cannot repair the
  overdrive inequality. A repair must change the generator, source balance,
  metric, physical-input splitting, or signature.

The shared statement is not “add another port.” It is “add a source incidence
that does not descend through the defective quotient.”

## DPC

Given a proposed repair port \(r\):

1. identify the equivalence relation or gauge action erased by the current
   readout;
2. prove that the current readout factors through its coequalizer;
3. test whether \(r\) also factors through that coequalizer;
4. reject the repair if it does;
5. if it does not, test joint monicity of \((q,r)\) on the declared state
   class;
6. require independent source authority for \(r\).

## Disposition

The downstream-repair class is closed. Only a source-sensitive extension can
restore the missing distinction, and joint faithfulness—not the number or
placement of ports—is the operative gate.

## Verification

`check_gauge_forgetting_downstream_no_go.py` verifies the universal kernel of
downstream composites, hostile spectator enlargements, and the minimal
source-sensitive rank repair using exact rational matrices.

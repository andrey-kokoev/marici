# 2734 — Single-Occurrence Defect Absorption Is Noncanonical

## Question

Entry 2728 showed that the full moving marked-pole relation span absorbs the differentiated Euler defect. Test whether one labelled occurrence is canonically selected by the three external derivative directions.

## First occurrence test

The (q_{\mathcal G_1})-multiplication family alone absorbs all three defects at the reference point:

\[
\begin{array}{c|c|c}
\text{direction}&\text{processed generators}&\text{derived span rank}\\
\hline
x&891&823\\
y&891&824\\
z&891&828
\end{array}
\]

Every residual support is zero.

## Hostile second occurrence

The distinct (q_{\mathcal G_{23}})-multiplication family also absorbs all three defects:

\[
\begin{array}{c|c|c}
\text{direction}&\text{processed generators}&\text{derived span rank}\\
\hline
x&668&629\\
y&690&650\\
z&690&654
\end{array}
\]

Again every residual support is zero.

## Conclusion

Existence of a single-occurrence absorbing span does not select a unique occurrence or coherence cell. At least two inequivalent labelled pole families independently contain the same defect.

Therefore Entry 2728 must not be implemented by choosing a convenient occurrence projector. The canonical missing object, if it exists, is the derivative of the complete labelled marked-pole relation map together with its chart-transition naturality—not any one absorbing subspace.

## Artifacts

- `research/benincasa/check_rank26_single_occurrence_coherence.py`
- `research/benincasa/rank26-single-occurrence-coherence.json`
- `research/benincasa/rank26-single-occurrence-coherence-g23.json`

## Next falsifier

Construct the full relation-map derivative as a map of labelled presentations and transport it through the independently derived residue-chart transition. Test the naturality square before passing to spans. If the square commutes, the adapter cell is canonical despite nonunique span witnesses. If it fails, the present chartwise repair is nonphysical.

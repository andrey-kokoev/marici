# Semantic pullback makes one prospective observability prediction

## Question

Can the bidirectional calculus predict a missing state direction and its
minimal repair from a constructor's forward semantics before the forward
hostile is computed?

## Preregistration

The frozen fixture is
`research/nima/fixtures/semantic-pullback-prospective-observability.json`.
Its SHA-256 digest is
`862e4e3486009184cbc4828eed4031573b259ce8e86340b69ee03f94a7c946f7`.
It was admitted before checker construction as graph event
`ev-000000006383-53b6e708-5423-4bd5-81f8-d18873d082a4`.

The source is a four-dimensional rational state with transport

\[
T=
\begin{pmatrix}
1&1&0&0\\
0&1&1&0\\
0&0&1&1\\
0&0&0&1
\end{pmatrix}
\]

and scalar observer

\[
C=\begin{pmatrix}1&0&0&0\end{pmatrix}.
\]

Records at times zero, one, and two were admitted. Time three was frozen as
the candidate extension. Before checker construction, the prediction was:

- admitted observability rank three;
- residual state exactly the fourth basis direction;
- one additional scalar record is necessary and sufficient;
- the residual state has trace `0,0,0,1` at times zero through three.

Any mismatch was a preregistered failure.

## Semantic backward transformer

The observer effect is pulled backward through transport rather than replaced
by declared requirement labels:

\[
C\longmapsto CT^k.
\]

At admitted times this gives

\[
C=egin{pmatrix}1&0&0&0\end{pmatrix},
\]

\[
CT=egin{pmatrix}1&1&0&0\end{pmatrix},
\]

\[
CT^2=egin{pmatrix}1&2&1&0\end{pmatrix}.
\]

Their row reduction has rank three and common kernel

\[
\operatorname{span}
\left\{
\begin{pmatrix}0\\0\\0\\1\end{pmatrix}
\right\}.
\]

The backward computation therefore predicts the hidden state direction
without choosing a source preimage from an observed record.

## Independent forward hostile

The forward audit applies the actual transport repeatedly to the frozen
hostile state. Its record trace is exactly

\[
(0,0,0,1).
\]

Thus the state is invisible under every admitted record and becomes visible
at the preregistered extension time.

The candidate effect is

\[
CT^3=egin{pmatrix}1&3&3&1\end{pmatrix}.
\]

Adding it raises the observability rank from three to four. An independent
search of the complete nonzero cube with coordinates in
`{-1,0,1}` finds only the two signed fourth-basis states in the admitted
kernel, and the candidate effect separates both.

## Result

All four preregistered predictions pass:

- exact rank;
- exact residual direction;
- exact minimal extension count;
- exact hostile trace.

This is stronger than the atomic-label pilot because the residual is derived
from the forward matrix by effect pullback and exact kernel computation.

## Claim boundary

This is one finite rational observability constructor. It does not establish
that every Marici arrow has a computable weakest precondition, that nonlinear
or unbounded residuals admit finite bases, or that the resulting extension is
physically source-authorized. The example is deliberately small enough to
make post-hoc flexibility visible.

## Disposition

The prospective Deutschean gate passes at the first finite semantic level.
The calculus predicted a counterfactual incapacity and the minimal additional
effect before the forward hostile was run.

The next progressive test must leave finite linear observability. A suitable
target is an operator whose backward pullback produces a domain, boundary, or
completion residual rather than a finite kernel direction.

## Verification

- Checker:
  `research/nima/checkers/check_semantic_pullback_prospective_observability.py`
- Result:
  `research/nima/results/semantic-pullback-prospective-observability.json`
- Preregistration event:
  `ev-000000006383-53b6e708-5423-4bd5-81f8-d18873d082a4`

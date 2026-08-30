# 1718 — Incomparable Simplex-Face Blowups Commute on the Complete Joint Tensor

## Transverse-corner falsifier

Chain-nested faces cannot detect an interchange obstruction.  Freeze instead
the smallest labelled transverse corner

\[
\Pi(\delta,\theta)=
\begin{pmatrix}
\delta\theta a&\delta b\\
\theta c&d
\end{pmatrix}.
\]

The four entries are occurrences in the complete joint mixture table; none is
reconstructed from marginals.

## Blowup square

Resolving the \(\delta\)-face and then the \(\theta\)-face transports the
mixed entry as

\[
\delta(\theta a).
\]

The reverse order transports it as

\[
\theta(\delta a).
\]

Because the normal parameters are scalar Cartier coordinates,

\[
\boxed{\delta(\theta a)=\theta(\delta a)}.
\]

The two side directions remain the distinct labelled occurrences \(b\) and
\(c\).  Thus commutation is not obtained by forgetting occurrence data.

## Narrow result

The incomparable simplex-face square commutes strictly on the complete joint
coefficient tensor.  No interchange class and no new Cut carrier stratum are
present in the tested finite corner.

## Durable artifacts

- `research/benincasa/checkers/incomparable_simplex_face_interchange.rs`
- `research/benincasa/results/incomparable-simplex-face-interchange.json`
- `research/benincasa/incomparable-simplex-face-interchange.md`

## Next falsifier

Replace the classical nonnegative joint table by a matrix-valued or
noncommutative mixture coefficient.  The same square then tests whether the
normal transports commute or produce a genuine coefficient-level braiding.

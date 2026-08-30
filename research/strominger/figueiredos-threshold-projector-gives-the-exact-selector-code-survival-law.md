# Figueiredo's Threshold Projector Gives the Exact Selector-Code Survival Law

## Transferred theorem

Let \(P\) project onto the selector code and let \(W\) be an intervening unitary
on the full endpoint space. Relative to code and spectator sectors, write

\[
W=\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
\]

Unitarity gives

\[
A^\dagger A=I-C^\dagger C.
\]

Thus the compressed code operation is isometric only when the leakage block
\(C\) vanishes. Exact reversible survival of preparation, controlled phase, and
complementary readout requires both off-diagonal blocks to vanish, equivalently

\[
[W,P]=0.
\]

This is the endpoint transfer of Figueiredo WP860's threshold-superselection
criterion.

## Hostile global unitary

A three-four-five rotation mixing one code direction with one spectator is a
perfectly valid global unitary. Its code compression has Gram matrix

\[
\begin{pmatrix}9/25&0\\0&1\end{pmatrix}.
\]

The missing norm \(16/25\) is exactly the leakage probability. Hence global
unitarity, matching spectra, or preservation of the terminal sign on selected
states does not establish transport of the full instrument.

## Consequence for the endpoint programme

Entry 3727 showed that quadratic grade mixing cannot preserve a finite selector
code. The present theorem gives the invariant form of that failure. The
code-relative instrument can pass through a family of endpoint operations only
if the source supplies a superselection projector \(P\) commuting with the
complete interaction algebra.

This strengthens the support contract from a state-level promise to an
algebra-level law:

```text
weak claim
  prepared states begin inside the selector code

required claim
  every admitted intervening operation commutes with the selector projector
```

No such projector law has been derived for the magnetic source.

## Other transfers found in the same scan

Aspect's three-channel analyzer is full rank over characteristic zero but has
determinant six and loses rank modulo two and three. This adds an integral Smith
gate to any linear ubermonitor: field-level faithfulness does not imply
integral route reconstruction.

Figueiredo WP859 supplies a constructive pattern in which a source-derived
common junction and lossless completion jointly generate a dark port and its
complementary reference output. It is the closest cross-sector model for our
four-capability instrument, but there is no source-derived comparison map to
the endpoint oscillator and no identification is made.

Aspect's reciprocal log-Gaussian result supplies a further warning: a
functional-calculus repair is canonical only after the source fixes the
coordinate unit. In our endpoint case the source commutator fixes the integer
number grading mathematically; physical spectral-projector execution remains
unproved.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/selector_projector_intertwining_checks.py
```

The exact checker contrasts a block-preserving unitary with the rational
three-four-five hostile rotation.

# Coherent Ports Must Remain Nonrepresentable in the Protected Core

## Double-category falsifier

Separating protected operations from coherent ports into vertical and
horizontal arrows is stable only if no automatic constructor collapses the
horizontal arrows into vertical endomorphisms.

For the coherent port (i=(1,1)^T), its horizontal round trip retains the
relative-coherence matrix

\[
R=ii^\dagger=
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

If a representability, companion, or conjoint constructor identifies (R)
with a vertical selector endomorphism, then ([R,P]\ne0), and protection is
lost.

## The only elementary safe projection loses the signal

The block conditional expectation

\[
\mathbb E_P(R)=PRP+(I-P)R(I-P)
\]

does land in the protected commutant. In the two-sector model it gives the
identity matrix. But it does so by deleting both off-diagonal entries, exactly
the relative coherence carried by the port.

Hence the same collapse cannot be both protection-preserving and faithful to
the coherence datum in this model.

## Structural theorem

The role split requires a nonrepresentability invariant:

```text
coherent horizontal ports do not canonically represent protected vertical maps
```

A companion, conjoint, shadow, trace, or conditional expectation crossing
this boundary is an authority-bearing constructor. Endpoint compatibility does
not generate it.

The minimal consistent structure is therefore a partial double category:

- vertical composition closes the protected algebra;
- horizontal composition retains coherent route data;
- selected squares compare the two sorts;
- no general horizontal-to-vertical collapse exists;
- any supplied collapse declares whether it preserves protection or coherence.

## Prediction

Any proposed source completion of the four-capability magnetic instrument must
fail one of three tests:

1. no collapse is supplied, so the coherent port cannot act as internal
   control;
2. a faithful collapse is supplied, so the protected projector is violated;
3. a protected conditional expectation is supplied, so relative coherence is
   erased.

Escaping the trilemma requires a genuinely new object carrying coherence in a
separate factor while the protected algebra acts trivially on that factor.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/horizontal_port_vertical_collapse_no_go_checks.py
```

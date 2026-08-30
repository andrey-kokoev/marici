# 2871 — The Soft Torsor Is Pointed Only after Moving-Fiber Pushforward

## Corrected source object

Let \(\Gamma_a(t)\) be the physical Cayley–Menger fiber cycle. It moves with
the base coordinate \(t=q_{g1}/X_1\) and collapses at \(t=2\). The correctly
typed base one-form is therefore the Gauss–Manin pushforward

\[
I(t)\,dt
=
\left(\int_{\Gamma_a(t)}\Omega\right)dt.
\]

The soft endpoint has the source-derived asymptotic form

\[
I(t)=\frac{L}{t}+O(1),
\qquad t\to0,
\]

where \(L\) is the \(q_{g1}\)-residue vanishing period. At \(t=2\), the
positive physical Cayley–Menger cycle collapses and \(I(t)\) is finite.

## Pointed logarithmic torsor

Only after pushforward is there a canonically typed endpoint pointing:

\[
P(t)=\int_2^t I(s)\,ds,
\qquad P(2)=0.
\]

Its soft finite part is

\[
\operatorname{FP}_{t=0}P
=
\lim_{t\to0}
\left[
P(t)-L\log\!\left(\frac{t}{2}\right)
\right].
\]

The subtraction uses the same source-normalized coordinate and the same
opposite endpoint that point the torsor. No fixed-\(a\) primitive is used.

## Result

The full moving-fiber compatibility gate passes in the following narrow form:

\[
\text{moving-fiber pushforward}
\longrightarrow
\text{base one-form}
\longrightarrow
\text{endpoint pointing}
\longrightarrow
\text{soft finite part}.
\]

Entry 2870's objection to pointwise pre-pushforward pointing remains valid.
The present result supplies the corrected constructor rather than restoring
the retracted fixed-fiber construction.

## Remaining gates

The finite part must still be tested under admissible regulator changes, and
its logarithmic monodromy must still be compared with the source-oriented
Leray tube around \(q_{g1}=0\).

## Durable artifacts

- `research/benincasa/check_soft_endpoint_pushed_forward_pointing.py`
- `research/benincasa/soft-endpoint-pushed-forward-pointing.json`


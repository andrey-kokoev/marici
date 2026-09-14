# The first forward–reverse positive filler gate is a sharp interval

## The 2-to-3 incidence packet

Normalize the translation-invariant kernel by \(K(0)>0\), and write

\[
a=\frac{K(h)}{K(0)},
\qquad
b=\frac{K(2h)}{K(0)}.
\]

The first forward–reverse packet is

\[
G_3=
\begin{pmatrix}
1&a&b\\
a&1&a\\
b&a&1
\end{pmatrix}.
\]

Reversal exchanges the first and third coordinates. Thus the incidence square splits canonically into reversal-odd and reversal-even channels.

## Odd channel

The odd vector \((1,0,-1)\) gives the condition

\[
1-b\geq0.
\]

## Even channel

On the span of \((1,0,1)\) and \((0,1,0)\), positivity gives

\[
1+b-2a^2\geq0.
\]

Hence a positive incidence-compatible third-rung filler exists exactly when

\[
\boxed{2a^2-1\leq b\leq1}.
\]

In source-kernel form, the two inequalities are

\[
K(0)-K(2h)\geq0
\]

and

\[
\boxed{
K(0)\bigl(K(0)+K(2h)\bigr)-2K(h)^2\geq0.
}
\]

The boxed inequality is the first coupled forward–reverse extension gate.

## Exact obstruction

Take

\[
a=\frac9{10},
\qquad
b=-\frac9{10}.
\]

Every two-point face is positive and reversal incidence is exact. But positive extension requires

\[
b\geq2a^2-1=\frac{31}{50},
\]

which the prescribed reading violates. The even-channel margin is \(-38/25\), so no rank-three positive filler exists.

Therefore forward/reverse incidence and positivity of all lower faces do not by themselves prove extension.

## Tightening programme

The mechanism is nevertheless now exact. At each successor stage:

1. forward positivity gives a Schur-admissible region;
2. reverse positivity gives its dual region;
3. incidence intersects them;
4. the source formula prescribes one new reading;
5. RH requires that prescribed reading to remain in every intersection.

At the first nontrivial stage, the unresolved source theorem is precisely

\[
K(0)(K(0)+K(2h))\geq2K(h)^2
\]

for every Gaussian width and spacing.

Higher rungs replace this interval by intersections of Schur-complement ellipsoids. A proof that the coupled endpoint–gamma–prime source reading always belongs to those nested regions would establish the desired positive extension induction.

## Verification

```text
python research/voevodsky/checkers/check_first_forward_reverse_positive_filler_gate.py
```

Artifacts:

- `research/voevodsky/checkers/check_first_forward_reverse_positive_filler_gate.py`
- `research/voevodsky/results/first_forward_reverse_positive_filler_gate.json`

# Hardware–bracketing confounder

## Question

Can native three-body process calibration distinguish a logical associator from
a stable phase attached to one physical bracketing circuit?

## Exact identifiability failure

If logical left is always implemented by hardware `H1` and logical right by
hardware `H2`, the observed difference is only

\[
R=A+D,
\]

where `A` is the logical associator and `D` is the hardware phase difference.
No amount of repetition separates them.

With true associator zero and hardware phase `3/5`, the fixed experiment
reports residual `3/5`. This is observationally identical to a true associator
`3/5` with matched hardware.

## Crossed repair

Require both physical circuits to implement both logical bracketings. Measure

```text
logical L on H1 versus logical R on H2
logical L on H2 versus logical R on H1
```

The two differences are

\[
R_{12}=A+D,
\qquad
R_{21}=A-D.
\]

Therefore

\[
A=\frac{R_{12}+R_{21}}2,
\qquad
D=\frac{R_{12}-R_{21}}2.
\]

For a mixed fixture `A=1/5`, `D=3/5`, the raw differences are `4/5` and
`-2/5`; the crossed estimator recovers both quantities exactly.

## Apparatus requirement

Logical bracketing and physical circuit identity must be independently
randomized within the same calibration epoch. Each hardware path must expose
the same open three-body ports and support both logical control sequences.
Route labels remain sealed until all four crossed cells are immutable.

## Disposition

The native three-body calibration gate was necessary but not sufficient. A
crossed hardware design is required for associator identifiability.

## Verification

Run:

```text
python research/aspect/checkers/check_hardware_bracketing_confounder.py
```

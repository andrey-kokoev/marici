# The universal Schwarz spectral cover solves label exchange but not positivity

For a real symmetric primitive/prime-prime observation square

\[
S=
\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]

set

\[
C_{13}=a+c,
\qquad
D=ac-b^2.
\]

Define the oriented spectral double cover

\[
\boxed{
y^2=C_{13}^2-4D=(a-c)^2+4b^2.
}
\]

On this cover, define

\[
X_{13}=\frac{C_{13}+y}{2},
\qquad
X_{24}=\frac{C_{13}-y}{2}.
\]

Then the deck transformation \(y\mapsto-y\) exchanges the labeled channels exactly, while

\[
X_{13}+X_{24}=C_{13}
\]

and

\[
X_{13}X_{24}=D.
\]

Thus the oriented-cover construction resolves the earlier label-equivariance problem.

It does not force positivity. Assuming \(C_{13}\geq0\), both channels are positive exactly when

\[
C_{13}\geq|y|,
\]

which is equivalent to

\[
D\geq0.
\]

So an indefinite square still has a valid oriented spectral cover; one sheet simply carries a negative channel.

## No identified source cover

The similarly named conductor `C13` candidate is unrelated: there `C13` is a conjecture identifier, not the kinematic coordinate \(C_{13}\). Its elliptic cover cannot be imported here without a new cross-program source map. See `research/voevodsky/erratum-the-conductor-C13-candidate-is-not-the-kinematic-C13-coordinate.md`.

Thus the universal spectral cover is currently an abstract construction only. It solves orientation and exchange algebraically, while the positive-chamber bound

\[
C_{13}\geq|y|
\]

remains the RH-bearing condition.

## Verification

```text
python research/voevodsky/checkers/check_universal_Schwarz_spectral_cover.py
```

Artifacts:

- `research/voevodsky/checkers/check_universal_Schwarz_spectral_cover.py`
- `research/voevodsky/results/universal_Schwarz_spectral_cover.json`

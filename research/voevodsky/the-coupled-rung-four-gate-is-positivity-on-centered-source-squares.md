# The coupled rung-four gate is positivity on centered source squares

## Centering identity

Let \(L\) be the complete endpoint–gamma–prime observer and assume

\[
m=L(1)>0.
\]

For an arbitrary composite primitive \(p\), define its coupled centered form

\[
p^\circ
=
p-\frac{L(p)}{m}\,1.
\]

Then

\[
L(p^\circ)=0
\]

and direct expansion gives

\[
\boxed{
mL(p^*p)-|L(p)|^2
=
mL((p^\circ)^*p^\circ).
}
\]

Thus the rung-four Schwarz determinant is one centered-square source observation.

## Cancellation-preserving source expression

Write only after centering

\[
L=L_E+L_\Gamma+L_P.
\]

Then

\[
\det S_L(p)
=
m\left[
L_E((p^\circ)^*p^\circ)
+L_\Gamma((p^\circ)^*p^\circ)
+L_P((p^\circ)^*p^\circ)
\right].
\]

Both the centering coefficient

\[
\frac{L(p)}{L(1)}
\]

and the final square evaluation use the fully coupled observer. No endpoint, gamma, or prime sector is required to be positive or relatively bounded separately.

## Exact reduced gate

Because \(m>0\), universal rung-four positivity is equivalent to

\[
\boxed{
L(q^*q)\geq0
\quad
\text{for every composite }q\text{ satisfying }L(q)=0.
}
\]

This removes the constant observation direction. In matrix language it is the Schur complement of the base observation \(L(1)\).

Hence all possible negativity lies in the codimension-one centered source fiber

\[
\ker L.
\]

## Significance

This is the requested coupled source formulation. It preserves endpoint–gamma–prime cancellation and avoids the false sectorwise domination route.

It also sharpens the coherence interpretation:

- rung three supplies \(L(p)\) and \(L(p^*p)\);
- centering removes the already observed base component;
- rung four tests the residual square in the observation-null fiber;
- higher rungs certify closure and completion of that fiber.

Under the source identity and Gaussian density, RH is equivalent to nonnegativity of the complete source observer on every centered Gaussian square.

## Remaining arithmetic inequality

No positivity proof follows merely from centering. The unresolved statement is now exactly

\[
L_E(q^*q)+L_\Gamma(q^*q)+L_P(q^*q)\geq0,
\qquad L(q)=0.
\]

This is narrower than arbitrary source positivity but remains RH-strength.

## Verification

```text
python research/voevodsky/checkers/check_coupled_centered_schwarz_identity.py
```

Artifacts:

- `research/voevodsky/checkers/check_coupled_centered_schwarz_identity.py`
- `research/voevodsky/results/coupled_centered_schwarz_identity.json`

# A diagonal contour form does not determine the off-diagonal augmented Green coupling

## Correction

The reflected contour identity identifies the sum of the spectral current and
endpoint residue forms after both are pulled back to the same source core. It
does not by itself construct an operator

\[
B_S:\mathscr E_S\to\mathscr H_{end,S}
\]

occupying the off-diagonal block of an augmented Green operator.

The previous claim that equality of the two source pullbacks uniquely extends
to such a \(B_S\) was too strong.

## Diagonal versus mixed data

The contour identity has the form

\[
q_S(g,h)
=
q_{bulk,S}(g,h)+q_{end,S}(g,h).
\]

This determines a sesquilinear form on the diagonal source embedding

\[
g\longmapsto(i_{bulk}g,i_{end}g).
\]

An off-diagonal coupling would instead require a separately defined mixed form

\[
b_S(x,y),
\qquad
x\in\mathscr E_S,
\quad
y\in\mathscr H_{end,S},
\]

with a bound

\[
|b_S(x,y)|
\le C\|x\|_{\mathscr E_S}\|y\|_{\mathscr H_{end,S}}.
\]

Values only on pairs arising from the same source embedding do not determine
this mixed form on the completed product. Distinct off-diagonal operators can
have the same pullback, and a pullback may fail to descend if either embedding
has a kernel not respected by the proposed pairing.

## Exact missing descent conditions

To obtain \(B_S\), one must prove:

1. **kernel compatibility**
   \[
   i_{bulk}g=0
   \Longrightarrow
   b_{src}(g,h)=0
   \quad\text{for every }h,
   \]
   and the analogous endpoint condition;

2. **product-norm boundedness**
   \[
   |b_{src}(g,h)|
   \le C
   \|i_{bulk}g\|_{\mathscr E_S}
   \|i_{end}h\|_{\mathscr H_{end,S}};
   \]

3. **density of both source ranges** in the declared source-generated
   completions.

Only then does Riesz representation supply a unique bounded operator \(B_S\).

## Status

The contour identity supplies the candidate source pairing and fixes its
normalization, including endpoint parity. Construction of the off-diagonal
augmented coupling still requires the kernel and product-bound descent theorem.
Consequently the signed mixed Green map is not yet closed at operator level.

The subsequent Schur positivity problem cannot be attempted honestly until
this descent is proved.

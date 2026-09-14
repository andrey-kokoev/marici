# The v_alg logarithmic representative is available on the central sheet

## Recovery

Ledger entry `20260816-296 Universal One-Wall Cleared Extension Certificate` gives the literal central-sheet realization that the previous audit missed. Put

\[
s=x+y,
\qquad
R=xa^2+yb^2-xys,
\qquad
K_0=R^2.
\]

On the fixed sheet \(\sqrt{K_0}=R\), suppressing the common volume form \(da\wedge db\),

\[
e_7=\frac1R,
\qquad
e_8=\frac{a^2}{R},
\qquad
e_9=\frac{b^2}{R}.
\]

Therefore the specialized algebraic class has the explicit representative

\[
\boxed{
\varphi_{v_{\rm alg}}
=
\frac{x^2y^2\bigl(x^2-y^2+2a^2-2b^2\bigr)}
{xa^2+yb^2-xy(x+y)}\,da\wedge db.
}
\]

The opposite sheet changes \(R\mapsto-R\), hence reverses this representative.

## Immediate residue consequence

For any candidate route wall \(L(a,b)=0\) not dividing \(R\), this displayed representative has no logarithmic pole along the generic point of \(L\). Consequently

\[
\operatorname{Res}_L\varphi_{v_{\rm alg}}=0
\]

away from \(L\cap\{R=0\}\). By the relative intersection formula found in `Cosmology meets cohomology`, a dual boundary class supported generically on such an \(L\) has zero pairing with \(v_{\rm alg}\); any nonzero pairing must be concentrated at the finite intersections with the ramification divisor \(R=0\) or at infinity.

## Remaining coordinate gate

The four pyramid fibers are written globally as

\[
b/h=\pm(y+z),\qquad b/h=\pm(2x+y+z),
\]

whereas the central-sheet representative uses the affine source coordinates \((a,b;x,y)\). The repository does not yet serialize the substitution identifying these two coordinate conventions at the physical anchor. Until that dictionary is fixed, it is unsafe to substitute a guessed linear equation such as \(b=-(x+y)\).

## Reduction

The missing route period is no longer blocked by absent forms. It is reduced to:

1. recover the global-to-central coordinate dictionary at \(d_1\);
2. transport the reflected route wall into \((a,b)\);
3. solve its intersections with \(R=0\), including infinity;
4. sum the two sheet-oriented local residues.

Thus only a coordinate-marking gate remains before the residue calculation.
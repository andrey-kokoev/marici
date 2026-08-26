# Constrained-auxiliary authority audit (WP381)

## Bounded question

Can a constrained auxiliary or contour-rotated Gaussian evade WP380 and
derive the positive penalty for the invariant flavor residual (F)?

## Complex-contour representation

For positive (lambda), exact square completion gives

\[
-\frac{A^2}{4\lambda}+iAF
=-\frac{(A-2i\lambda F)^2}{4\lambda}-\lambda F^2.
\]

After an admitted complex contour shift, the auxiliary integral represents
the desired Euclidean factor with positive potential (+\lambda F^2\).
This escapes the real stationary-minimization assumptions of WP380, but its
integrand is complex for real nonzero (A) and (F). The integration cycle,
convergence domain, and reflection-positivity or unitarity recovery are new
source data. This is a changed contour experiment, not a healthy real
mediator completion.

With a real coupling instead,

\[
-\frac{A^2}{4\lambda}+AF
=-\frac{(A-2\lambda F)^2}{4\lambda}+\lambda F^2,
\]

which gives the opposite potential sign found in WP379.

## Real constrained representation

Consider

\[
V(B,\eta,F)=\frac{\mu}{2}B^2+\eta(B-F),
\qquad \mu>0.
\]

The multiplier equation imposes (B=F), and elimination yields

\[
V_{\mathrm{eff}}(F)=\frac{\mu}{2}F^2.
\]

The positive sign is exact, but the constraint already contains the complete
flavor residual (B-F). It therefore transports the desired shell into the
source grammar rather than deriving it. Moreover, the auxiliary Hessian is

\[
\begin{pmatrix}\mu&1\\1&0\end{pmatrix},
\qquad \det=-1,
\]

so this is a saddle constraint, not minimization over a positive mediator
sector.

## Authority disposition

Both constructions are mathematically valid representations. Neither supplies
independent selector authority:

- the complex Gaussian requires a declared contour and physical recovery map;
- the real constraint inserts (F) in the constraint itself;
- neither fixes (lambda), (mu), or the numerical source ratio defining
  (F).

The constrained construction descends under the full weak-basis groupoid only
because (F) was already chosen as the invariant WP378 residual. Replacing it
with texture-chart data would fail descent. No reference port is repaired or
required here; the complex contour instead changes the admitted source
integration structure.

The smallest falsifier is twofold: the complex exponent has a nonzero
imaginary part at (A=F=\lambda=1), while the real multiplier Hessian has
determinant (-1). The remaining gate is a source derivation of the contour or
constraint, its physical instrument, and its coefficient before flavor
readout.

Run `uv run --with sympy python
research/flavor/checkers/wp381_constrained_auxiliary_authority.py` to
regenerate the result.

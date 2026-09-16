# Prior research points to an infinite-tail boundary quotient, not a missing finite coherence

## Search conclusion

The prior Marici packets contain a coherent answer to the constructive question.

The missing object is not another formal symmetry or a finite higher-homotopy repair. The surviving constructive route is an infinite-dimensional theta-tail carrier equipped with a source-derived boundary quotient or contraction.

## Positive pieces already constructed

### Exact positive-mode Gram identity

For a genuinely positive exponential packet, endpoint-minus-pair orientation has an exact rank-two Gram factorization. The vectors are

\[
v_n=(\alpha_n^2-|z|^2,2\operatorname{Im}(z)\alpha_n).
\]

This proves the desired orientation on that cone without estimates.

Reference:

`research/grothendieck/the-positive-mode-endpoint-dominance-is-an-exact-rank-two-gram-factorization.md`

### Positive mixed-sector Green kernel

Opposite Mellin sectors produce

\[
K(x,y)=e^{-|x-y|/2}-e^{-(x+y)/2},
\]

the Dirichlet Green kernel of

\[
-d^2/dx^2+1/4
\]

on the half-line. It has the explicit Gram realization

\[
K(\log p,\log q)
=\langle \mathbf1_{[1,p]}/\sqrt p,
\mathbf1_{[1,q]}/\sqrt q\rangle.
\]

Reference:

`research/grothendieck/the-mixed-cauchy-defect-is-a-dirichlet-green-kernel.md`

### Source-derived contraction principle

A signed completed source form

\[
Q(f)=\|Af\|^2-\|Bf\|^2
\]

is positive exactly when the source-defined map

\[
C(Af)=Bf
\]

is well-defined and contractive. Then

\[
Q(f)=\|(1-C^*C)^{1/2}Af\|^2.
\]

This is the noncircular meta-constructor if \(A,B,C\) are derived before positivity is assumed.

Reference:

`research/grothendieck/the-positive-meta-constructor-is-a-source-derived-contraction.md`

## Exact obstructions to naive construction

### The actual theta source is not locally pairwise positive

The completed theta density enters the two-point Krein negative cone on arbitrarily narrow packets near the modular seam. Thus global positivity cannot be assembled from independently positive adjacent source pairs.

Reference:

`research/grothendieck/actual-theta-source-enters-the-local-two-point-krein-negative-cone.md`

### Sectorwise endpoint positivity is false

The endpoint translate kernel has a negative rank-two determinant at every nonzero separation. Endpoint, gamma, and prime/source channels must be coupled before positivity is taken.

Reference:

`research/grothendieck/the-endpoint-source-translate-kernel-fails-rank-two-at-every-separation.md`

### Finite theta-tail repairs collapse at the terminal boundary

The minimal transport--accumulator system has a rank-four Green defect. Two crossed repair pairs produce a positive candidate Hamiltonian, but the repair-frame connection has an unavoidable logarithmic terminal singularity. The same pole occurs for every finite family of tail-scaled repair channels.

Reference:

`research/grothendieck/theta-canonical-system-typed-defect-gate.md`

This is a direct no-go for the obvious strategy of adding finitely many moment states or coherence cells.

## Surviving carrier

The faithful source object is the moving Hilbert fiber

\[
\mathcal H_r=L^2([r,L],\Phi(t)dt).
\]

Restriction has the exact positive shell identity

\[
\|f\|_{\mathcal H_r}^2-
\|f\|_{\mathcal H_s}^2
=
\int_r^s|f(t)|^2\Phi(t)dt
\ge0.
\]

Unlike finite tail moments, this carrier does not collapse by division through a vanishing tail mass.

The theta accumulators are boundary readouts of the coherent sections

\[
\cos(zt),
\qquad
-t\sin(zt).
\]

The remaining construction is a relative boundary quotient whose determinant is \(X(z)\) and whose Weyl function is

\[
-X'(z)/X(z).
\]

## Correct constructive target

The denominator-free Loewner kernel is

\[
L_C(x,y)
=
\frac{(x-1/4)C'(x)C(y)-(y-1/4)C'(y)C(x)}{x-y}.
\]

A source proof should construct a map \(R_x\) from the infinite tail carrier such that

\[
\boxed{
L_C(x,y)=R_x^*R_y.
}
\]

Equivalently, it may construct a boundary contraction whose defect Gram kernel is \(L_C\).

This cannot be obtained by defining \(R_x\) from a Cholesky factor of the target kernel; the map must descend from restriction, boundary trace, and theta readout operations.

## Interpretation

The prior research supports the following diagnosis:

1. the scalar model and its symmetries are correctly typed;
2. local and sectorwise positivity are provably false;
3. finite moment/coherence repairs are terminal-singular;
4. exact positive bulk structures exist;
5. the missing operation is the relative boundary quotient that couples the positive bulk to the Xi accumulator.

Thus the likely missing datum is not a finite coherence but an infinite-dimensional boundary map.

## Next exact computation

On the restriction system \(\mathcal H_r\), define the two theta trace functionals

\[
T_0(z)f=\int_r^L f(t)\cos(zt)\Phi(t)dt,
\]

\[
T_1(z)f=-\int_r^L tf(t)\sin(zt)\Phi(t)dt.
\]

The next constructive test is to compute the Schur complement/Green quotient of the joint trace operator \((T_0,T_1)\), retaining the endpoint \((\partial_t^2-1/4)\) contribution, and compare its polarized kernel exactly with \(L_C\).

If the equality holds and the quotient is a contraction, Pick positivity follows by construction. If the Schur complement differs from \(L_C\), the mismatch identifies the missing modular boundary current explicitly.

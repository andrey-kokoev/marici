# The doubled theta-tail flow isolates one modular forcing current

**Scope correction:** packet 146 supersedes the claim that every
non-derivative bulk component falsifies the route. The previously proved
two-variable reflection coboundary authorizes a source-derived component
proportional to `2 Re(z)`; that component renormalizes the bulk energy. The
exact doubled identity in this packet remains valid.

## Domain correction

The homogeneous rank-two system must retain a free constant channel:

\[
 \mathcal D_z
 \binom{G}{c}=0,
 \qquad
 \mathcal D_z=
 \begin{pmatrix}
 \partial_q+z&f(q)\\
 0&\partial_q
 \end{pmatrix}.
\]

For `c` nonzero, `G` is a scalar multiple of the source tail. A transform zero
is not existence of this solution; it is membership in the two-endpoint
domain

\[
 \mathsf{Dom}_{0,\infty}
 =\{(G,c):G(0)=G(\infty)=0\}.
\]

Thus

\[
 \text{transform}(z)=0
 \quad\Longleftrightarrow\quad
 \ker(\mathcal D_z|_{\mathsf{Dom}_{0,\infty}})\ne0
\]

within the convergence domain and subject to the later completed-source audit.

## Fourier--Tate doubled flow

Use the centered spectral coordinate `z=s-1/2`. Let the direct and dual tails
satisfy

\[
 \begin{aligned}
 (G_+)'&=-zG_+-f_+c_+,\\
 (G_-)'&=\bar zG_--f_-c_-.
 \end{aligned}
\]

The second equation is the tail flow at the reciprocal-conjugate parameter
`-conjugate(z)`. It is the parameter paired with `z` by the real
Fourier--Tate symmetry. The precise relation between `f_+` and `f_-` remains
to be derived from the completed source.

Put

\[
 a=\Re z,
 \qquad
 \mathcal N=|G_+|^2+|G_-|^2,
 \qquad
 J=|G_+|^2-|G_-|^2.
\]

Direct differentiation gives

\[
 \begin{aligned}
 \partial_q|G_+|^2
 &=-2a|G_+|^2-2\Re(f_+c_+\overline{G_+}),\\
 \partial_q|G_-|^2
 &=+2a|G_-|^2-2\Re(f_-c_-\overline{G_-}).
 \end{aligned}
\]

Hence the exact doubled identity is

\[
 \boxed{
 2a\mathcal N
 =-\partial_qJ-2\mathcal F,}
\]

where the entire unresolved bulk term is

\[
 \boxed{
 \mathcal F
 =\Re\left(
 f_+c_+\overline{G_+}
 -f_-c_-\overline{G_-}
 \right).}
\]

No local positivity or acute-cone assumption enters this identity.

## Conditional seam conclusion

Suppose reciprocal sewing supplies a source-derived boundary current
`J_boundary` satisfying

\[
 2\mathcal F=\partial_qJ_{\rm boundary}
\]

after the primitive, square, trace-class, and archimedean channels are all
retained. Then

\[
 2a\mathcal N
 =-\partial_q(J+J_{\rm boundary}).
\]

For a nonzero doubled state in the complete two-endpoint domain, vanishing of
the total boundary flux would give

\[
 2a\int_0^\infty\mathcal N\,dq=0.
\]

Since the integral is positive for a nonzero Hilbert-level tail state, this
forces `a=0`, equivalently `Re(s)=1/2`.

This is a conditional algebraic implication, not an RH proof. The missing
statement is exactly the boundary-current identity for `F`.

## What the completion must explain

The doubled calculation compresses the open problem to one source equality:

\[
 \boxed{
 \text{Fourier--Tate sewing turns the forcing difference }\mathcal F
 \text{ into a complete boundary derivative}.}
\]

The previously found current levels predict the terms:

\[
 J_{\rm boundary}
 =J_{k=1}+J_{k=2}+J_{\ge3}+J_\infty.
\]

Prime two's negative local scalar phase must occur inside this exact current;
it may not be bounded away or removed.

## Falsifiers

The route fails if any of the following survives after exact bilateral sewing:

1. a non-derivative bulk polarization in `F`;
2. a boundary term depending on a noncanonical prime cutoff path;
3. a distributional `k=1` term on which the pairing is undefined;
4. a completed zero state with vanishing Hilbert tail norm but nonzero data
   only in an uncontrolled quotient;
5. a hostile symmetric multiplier that preserves the same doubled operator,
   domain, forcing, and boundary current.

## Next finite calculation

Insert the exact theta modular reflection into `f_-` and expand `F` before
prime aggregation. Separate the reflected diagonal, prime-square, connected
tail, and moving-seam terms. The first uncancelled non-derivative term is the
smallest decisive obstruction; no numerical zero search is required.

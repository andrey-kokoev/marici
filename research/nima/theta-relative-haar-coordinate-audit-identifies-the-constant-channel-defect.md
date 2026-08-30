# The relative Haar coordinate audit identifies the constant-channel defect

## Status

Correction of the direct Dirichlet interpretation. The relative Haar form is
an exact source explanation of the already known positive tail bulk, not a new
closure of its forcing current. Its real gain is to type the unresolved
forcing as interaction with the non-normalizable constant source channel.

## Tail coordinate and multiplicative coordinate

The source tail uses

\[
q\in[0,\infty).
\]

There are two reciprocal multiplicative charts.

For the exterior chart,

\[
x=e^q,
\qquad
x\in[1,\infty),
\qquad
\frac{dx}{x}=dq.
\]

For the interior chart,

\[
x=e^{-q},
\qquad
x\in(0,1],
\qquad
\frac{dx}{x}=-dq.
\]

In both charts, the tail seam \(q=0\) is

\[
x=1.
\]

It is not the singular Haar endpoint \(x=0\).

## Correction to the Dirichlet claim

The scalar zero-state condition is

\[
G_s(0)=0.
\]

In multiplicative coordinates this is a Dirichlet condition at \(x=1\), the
sewing interface. It does not directly remove the singularity of \(dx/x\) at
\(x=0\).

The other tail condition is

\[
G_s(\infty)=0.
\]

In the interior chart this approaches \(x=0\). But this condition belongs to
every convergent tail, not specifically to scalar zeros. Relative-energy
admission near \(x=0\) therefore follows from tail decay and regularity, not
from the scalar-null boundary condition at \(q=0\).

The previous suggestion that scalar nullity itself solves the relative Haar
domain problem is rejected.

## Relative Haar energy is the known tail norm

Under either logarithmic chart,

\[
\int |G(x)|^2\frac{dx}{x}
=
\int_0^\infty|G(q)|^2\,dq.
\]

Thus the relative Haar energy is exactly the positive tail bulk already
present in the doubled Green identity:

\[
\mathcal N
=
|G_+|^2+|G_-|^2.
\]

The modular cocycle explains why this bulk has its critical spectral
coefficient. It does not remove the forcing polarization.

## The augmented source channel

The forward-derived homogeneous system is

\[
\mathcal D_z
\binom{G}{c}=0,
\qquad
\mathcal D_z
=
\begin{pmatrix}
\partial_q+z&f(q)\\
0&\partial_q
\end{pmatrix}.
\]

For a physical source state,

\[
c=1.
\]

The tail component \(G\) may lie in \(L^2(dq)\). The constant component does
not:

\[
\int_0^\infty|c|^2\,dq=\infty.
\]

Therefore the complete rank-two state is not an ordinary vector in the
relative Haar Hilbert space. It is a finite-energy response driven by a
non-normalizable source channel.

## Exact origin of the forcing term

The tail equation gives

\[
G'=-zG-fc.
\]

Differentiating the tail energy yields

\[
\partial_q|G|^2
=
-2\operatorname{Re}z\,|G|^2
-
2\operatorname{Re}(fc\overline G).
\]

The indefinite forcing term is precisely the off-diagonal interaction between
the finite-energy tail state and the non-normalizable constant source
channel.

In the doubled system, the unresolved polarization

\[
\mathcal F
=
\operatorname{Re}
\left(
f_+c_+\overline{G_+}
-
f_-c_-\overline{G_-}
\right)
\]

is therefore a relative-Haar domain defect. It is not a failure of positivity
of the tail bulk.

## Physical interpretation

The system resembles a passive transmission line driven by an idealized
source held at fixed amplitude for infinite scale time. The propagating field
has finite energy, while the drive is not a state in the same Hilbert space.
Power balance necessarily contains a supply term.

Trying to prove positivity of the tail norm again cannot eliminate that
supply. One must either:

1. realize the constant source as a boundary-control input rather than a state;
2. dilate it into a larger conservative reservoir;
3. show reciprocal sewing converts its total work into endpoint flux.

These are equivalent architectural forms only after their source maps and
domains are constructed.

## Boundary currents acquire a precise role

The endpoint, primitive, prime-square, trace-class, and archimedean channels
must jointly account for work done by the constant source channel. Their target
identity is not positivity of \(\mathcal N\), which is already positive. It is

\[
2\mathcal F
=
\partial_qJ_{\mathrm{boundary}}
+
2\operatorname{Re}z\,\mathcal M,
\]

where the completed bulk

\[
\mathcal N+\mathcal M
\]

must remain positive.

The relative Haar theorem supplies provenance for \(\mathcal N\). The
boundary-reservoir theorem must supply \(J_{\mathrm{boundary}}\) and
\(\mathcal M\).

## Revised source-level target

Construct a conservative dilation

\[
\widetilde{\mathcal H}
=
\mathcal H_{\mathrm{tail}}
\oplus
\mathcal H_{\mathrm{reservoir}}
\]

and a finite-energy state \((G,r)\) such that eliminating \(r\) reproduces the
forced tail equation. The full energy must obey

\[
2\operatorname{Re}z\,
\widetilde{\mathcal E}(G,r)
=
-\partial_q\widetilde J(G,r).
\]

The scalar zero must select a nonzero two-ended state in this conservative
dilation. If the reservoir is reconstructed backward from the scalar kernel,
the construction is circular.

## Finite falsifiers

The reservoir route fails if:

1. elimination does not recover the exact source forcing \(fc\);
2. the reservoir energy is indefinite;
3. an undeclared bulk residual remains;
4. the constant channel still has infinite norm after the declared dilation;
5. the construction changes under a hostile source with the same scalar
   functional equation only after inspecting its zeros;
6. completion allows the reservoir partner to escape.

## Verdict

The relative Haar operator explains the positive bulk and critical scaling,
but does not itself solve RH. The unresolved RH-bearing object is now typed
more sharply: it is the conservative reservoir or boundary supply associated
with the non-normalizable constant source channel in the forward-derived tail
system.

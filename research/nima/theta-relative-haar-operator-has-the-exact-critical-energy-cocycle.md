# The relative Haar operator has the exact critical energy cocycle

## Status

Exact operator theorem. It constructs a positive, faithful, source-natural
energy with the multiplier \(p^{1-2\operatorname{Re}s}\). The unresolved gate
is whether the completed theta/Tate source and all boundary currents belong to
its closed domain or to an authorized renormalized extension.

## Two independently normalized sectors

Let

\[
\mathcal H_a=L^2(\mathbb R_+,dx)
\]

and

\[
\mathcal H_m=L^2(\mathbb R_+,d^\times x),
\qquad
d^\times x=\frac{dx}{x}.
\]

Their source-normalized unitary dilation representations are

\[
(U_a(p)f)(x)=p^{1/2}f(px)
\]

and

\[
(U_m(p)g)(x)=g(px).
\]

Both are unitary in their own Haar Hilbert spaces.

## The relative trace operator

On the dense intersection define

\[
J:\mathcal H_a\supset\operatorname{Dom}J\longrightarrow\mathcal H_m,
\qquad
Jf=f,
\]

with

\[
\operatorname{Dom}J
=
L^2(dx)\cap L^2(dx/x).
\]

This inclusion is closed. If \(f_n\to f\) in \(L^2(dx)\) and \(Jf_n\to g\) in
\(L^2(dx/x)\), subsequences converge almost everywhere in both measures, so
\(f=g\) almost everywhere and \(f\in\operatorname{Dom}J\).

The relative positive operator is

\[
\Delta_{a|m}=J^*J=M_{1/x}.
\]

Its quadratic form is

\[
\mathcal E_{a|m}(f)
=
\|Jf\|_{\mathcal H_m}^2
=
\int_0^\infty|f(x)|^2\frac{dx}{x}.
\]

It is strictly positive on every nonzero state in its form domain.

## Exact modular cocycle

The relative inclusion intertwines the two unitary dilation representations
with a half-character:

\[
JU_a(p)=p^{1/2}U_m(p)J.
\]

Indeed, both sides evaluate to \(p^{1/2}f(px)\). Taking adjoints gives the
quadratic covariance

\[
U_a(p)^*\Delta_{a|m}U_a(p)
=
p\Delta_{a|m}.
\]

Equivalently,

\[
\mathcal E_{a|m}(U_a(p)f)
=
p\mathcal E_{a|m}(f).
\]

This factor is not a label-frame artifact. It compares two independently
unitary representations fixed by two different Haar measures.

## Mellin transport

Attach the source Mellin character to additive unitary dilation:

\[
V_s(p)=p^{-s}U_a(p).
\]

Then

\[
\mathcal E_{a|m}(V_s(p)f)
=
p^{1-2\operatorname{Re}s}
\mathcal E_{a|m}(f).
\]

Thus:

- the energy contracts for \(\operatorname{Re}s>1/2\);
- it is invariant for \(\operatorname{Re}s=1/2\);
- it expands for \(\operatorname{Re}s<1/2\).

The critical seam is the unit-energy locus of a positive faithful relative
Haar form.

## Infinitesimal generator

Writing \(p=e^L\), the covariance is

\[
U_a(e^L)^*\Delta_{a|m}U_a(e^L)
=
e^L\Delta_{a|m}.
\]

Differentiation at \(L=0\) gives

\[
\mathcal L_A(\Delta_{a|m})=\Delta_{a|m},
\]

where \(A\) is the additive dilation generator. Along a discrete prime step,
the logarithmic increment is \(\log p\). This identifies the primitive
von Mangoldt weight as the infinitesimal modular-energy current and \(p\) as
its integrated transport.

## Why the gauge objection no longer applies

In a single coefficient space, replacing \(A\) by \(AD\) and coefficients by
\(D^{-1}c\) cancels a diagonal weight. Here the two norms and two unitary
representations are independently fixed:

\[
\|U_a(p)f\|_{\mathcal H_a}=\|f\|_{\mathcal H_a}
\]

and

\[
\|U_m(p)g\|_{\mathcal H_m}=\|g\|_{\mathcal H_m}.
\]

The factor \(p^{1/2}\) is the defect of equivariance of the fixed relative
operator \(J\). Removing it would change one Haar normalization rather than
change a common basis.

## The domain is now the decisive RH gate

The operator \(J\) is unbounded. Near \(x=0\), a function with nonzero limit
fails the relative-energy condition because

\[
\int_0^1|f(x)|^2\frac{dx}{x}=\infty.
\]

Hence a raw theta source with an uncancelled endpoint constant is not in the
form domain. This is not a technical nuisance: endpoint, primitive,
prime-square, and archimedean currents may be the exact boundary data required
to renormalize the relative form.

The next theorem must establish one of the following directly from the
completed source:

1. the boundary-corrected zero-state belongs to \(\operatorname{Dom}J\);
2. the coupled endpoint packet defines a closed renormalized form extending
   \(\mathcal E_{a|m}\);
3. the source fails the domain gate, closing this route.

## Reciprocal sector

The inverse comparison uses the reciprocal density \(x\). Formally, the two
relative modular operators are

\[
\Delta_{a|m}=M_{1/x},
\qquad
\Delta_{m|a}=M_x.
\]

Reflection \(x\mapsto1/x\) exchanges them. The critical seam is where the
Mellin character balances these reciprocal metric transports.

This supplies a concrete two-sector Ubersector:

\[
(\mathcal H_a,\mathcal H_m,J,J^*,\Delta_{a|m},\Delta_{m|a}).
\]

## Zero-to-state bridge still required

The positive relative energy does not by itself connect to a scalar zero. One
must still derive an operator pencil and a nonzero state \(f_s\) satisfying

\[
\Xi(s)=0
\quad\Longrightarrow\quad
L(s)f_s=0.
\]

Then the Green identity must use the same relative form:

\[
2\operatorname{Re}(s-1/2)\,
\mathcal E_{a|m}(f_s)
=
\mathcal B(f_s).
\]

If the completed boundary supply vanishes and \(f_s\ne0\) lies in the form
domain, positivity forces \(\operatorname{Re}s=1/2\).

## Finite falsifiers

The route fails upon the first occurrence of any of the following:

1. a source zero-state outside the relative form domain after all authorized
   endpoint corrections;
2. failure of a primitive, square, seam, or archimedean current to extend to
   the graph topology of \(J\);
3. a nonzero state in the kernel of the renormalized relative form;
4. a Green residual not accounted for by the declared boundary packet;
5. a scalar zero that produces no operator state;
6. a common gauge that trivializes the relative cocycle while preserving both
   source Haar normalizations.

## Verdict

The additive-to-multiplicative comparison supplies an exact positive faithful
energy and the exact critical multiplier. The previous diagonal weighted Gram
was only its coordinate shadow. The RH-bearing frontier has moved to the
domain and boundary-renormalization theorem for the relative Haar operator,
followed by the independent zero-to-state bridge.

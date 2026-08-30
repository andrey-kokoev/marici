# Two-ray restriction gives an exact oriented bridge from translated fronts to theta fibers

## Unitary two-ray decomposition

Define
\[
\mathcal R_2:
L^2(\mathbb R,dq)
\longrightarrow
L^2(\mathbb R_+,dx)\oplus L^2(\mathbb R_+,dx)
\]
by
\[
(\mathcal R_2f)(x)
=
\bigl(f(x),f(-x)\bigr),
\qquad x>0.
\]

Then
\[
\|\mathcal R_2f\|^2
=
\int_0^\infty\bigl(|f(x)|^2+|f(-x)|^2\bigr)\,dx
=
\|f\|_{L^2(\mathbb R)}^2.
\]

Thus \(\mathcal R_2\) is unitary onto the two-ray direct sum. No support assumption or fitted continuation is used.

## Reciprocal character

Reflection
\[
(Rf)(q)=f(-q)
\]
becomes the ray swap
\[
\mathcal R_2R
=
\Sigma\mathcal R_2,
\qquad
\Sigma(a,b)=(b,a).
\]

Hence:

- even functions map to diagonal pairs \((h,h)\);
- odd functions map to anti-diagonal pairs \((h,-h)\).

The reciprocal character is therefore retained exactly before theta transport.

## Translated Gaussian fronts

Let
\[
g_t^+(q)=e^{-\pi(q+t)^2},
\qquad
g_t^-(q)=e^{-\pi(q-t)^2}.
\]

On the positive ray,
\[
\mathcal R_2g_t^+
=
\left(
e^{-\pi(x+t)^2},
e^{-\pi(x-t)^2}
\right),
\]
while
\[
\mathcal R_2g_t^-
=
\left(
e^{-\pi(x-t)^2},
e^{-\pi(x+t)^2}
\right).
\]

Thus reflection exchanges the two translated fronts by swapping ray coordinates.

Their sum is diagonal:
\[
\mathcal R_2(g_t^++g_t^-)
=
(h_t,h_t),
\]
where
\[
h_t(x)=e^{-\pi(x+t)^2}+e^{-\pi(x-t)^2}.
\]

Their difference is anti-diagonal:
\[
\mathcal R_2(g_t^+-g_t^-)
=
(k_t,-k_t),
\]
where
\[
k_t(x)=e^{-\pi(x+t)^2}-e^{-\pi(x-t)^2}.
\]

## Window history

The scale derivative of the comoving window is
\[
\partial_tW_t
=
-(g_t^++g_t^-).
\]
Therefore
\[
\mathcal R_2(\partial_tW_t)
=
-(h_t,h_t).
\]

The spatial derivative \(DW_t\) is odd, so
\[
\mathcal R_2(DW_t)
=
(r_t,-r_t)
\]
for its positive-ray restriction \(r_t\).

Thus the even history channel and odd incidence channel become the diagonal and anti-diagonal subspaces of one typed ray bundle.

## Componentwise theta transport

Apply the half-density maps
\[
\mathcal M_n f(u)
=
\sqrt n\,e^{u/2}f(ne^u)
\]
to each ray coordinate:
\[
\mathcal T_n
=
(\mathcal M_n\oplus\mathcal M_n)\mathcal R_2.
\]

Since both factors are unitary,
\[
\mathcal T_n
\]
is an isometry from the full-line front space to the doubled label-\(n\) theta fiber.

It intertwines reflection with coordinate swap:
\[
\mathcal T_nR
=
\Sigma\mathcal T_n.
\]

Hence the source reciprocal grading survives the nonlinear exponential transport exactly.

## Chain-homotopy compatibility

Because \(\mathcal R_2\) and \(\mathcal M_n\) are independent of the path parameter \(t\),
\[
\mathcal T_n\partial_tW_t
=
\partial_t\mathcal T_nW_t.
\]

Therefore
\[
\mathcal T_n(W_{2L}-W_L)
=
\int_L^{2L}\partial_t(\mathcal T_nW_t)\,dt.
\]

The oriented adjacent-cell boundary is preserved before completion.

## What this closes

The previously missing arrow
\[
\text{translated two-front full-line history}
\longrightarrow
\text{positive/negative ray half-density fibers}
\]
now exists as the exact isometry \(\mathcal T_n\).

It preserves:

- both translated fronts;
- reciprocal reflection;
- diagonal versus anti-diagonal character;
- scale-path differentiation;
- endpoint orientation;
- Hilbert norm.

## Remaining theorem

Theta completion acts exactly after \(\mathcal M_n\), but the transported translated profile is
\[
e^{-\pi(ne^u\pm t)^2},
\]
not the centered theta Gaussian
\[
e^{-\pi n^2e^{2u}}.
\]

The translation parameter \(t\) remains inside the nonlinear argument. The next source calculation must determine how the adjacent \(t\)-history is integrated, evaluated, or contracted so that the centered three-grade theta packet emerges without discarding the ray orientation.

## Hostile

Replacing both ray coordinates by their sum before transport erases the anti-diagonal odd incidence. Applying \(\mathcal M_n\) only to the centered Gaussian similarly forgets the translated cell. The exact doubled transport must precede either compression.

## Frontier

The analytic bridge has contracted to one explicit operation:
\[
e^{-\pi(ne^u\pm t)^2}
\longrightarrow
e^{-\pi n^2e^{2u}}
\]
through a source-authorized treatment of the oriented \(t\)-history.

# Prime idempotents commute with the odd Jacobi contraction, but raw-prime frame coercivity is false

## Scope

The local identity

\[
\Phi'(u)=-\langle\Delta',J_{\mathrm{odd}}(u)\rangle
\]

is independent of the arithmetic label. This note performs the prime-labelled direct-sum audit.

The conclusion has two parts:

1. prime diagonality and cutoff naturality are exact once the Jacobi packet is tensored with the source prime-label carrier;
2. a prime-uniform lower bound is false in the unweighted counting norm because the Euler half-density tends to zero.

The correct lower frame statement must be made in the source half-density metric.

## Labelled packet

Let \(\mathcal L\) be the algebraic prime-label space with basis \(e_p\) and idempotents

\[
P_p e_q=\delta_{pq}e_q.
\]

Let \(J_r\) be the local first or fifth Jacobi jet space, as appropriate, and let

\[
\mathcal J_{\mathrm{alg}}
=
\mathcal L\odot J_r.
\]

The odd contraction acts fiberwise:

\[
\mathfrak O_r(e_p\otimes F)
=
e_p\otimes\langle\Delta',F\rangle.
\]

Therefore

\[
P_p\mathfrak O_r
=
\mathfrak O_rP_p
\]

on the algebraic packet. In block form,

\[
P_q\mathfrak O_rP_p=0
\qquad(p\ne q).
\]

This is exact prime diagonality. It does not depend on scalar orthogonality, invariant means, or a posteriori cancellation. It follows from the tensor identity of the source-labelled construction.

## Cutoff naturality

For a finite prime set \(F\), put

\[
P_F=\sum_{p\in F}P_p.
\]

Then

\[
P_F\mathfrak O_r
=
\mathfrak O_rP_F.
\]

For nested cutoffs \(F\subseteq G\),

\[
\mathfrak O_r^{(G)}|_{\mathcal J_F}
=
\mathfrak O_r^{(F)}.
\]

Thus every finite odd Jacobi packet is the literal restriction of every larger packet. No cross-prime Schur estimate is needed for this constructor.

Reciprocal sewing acts in the Jacobi factor, while \(P_p\) acts in the label factor. Hence they commute on the algebraic tensor domain. The same is true for wall projection provided the wall remains a separate coefficient summand rather than being absorbed into a prime fiber.

## Euler loading

Let \(a_p(s)\) be the frozen arithmetic loading attached to the odd port. In the primitive off-seam channel its characteristic size is

\[
|a_p(s)|=p^{-1/2-\sigma}
\]

up to the separately typed logarithmic or grade coefficient.

The loaded observer is

\[
\mathfrak O_{r,a}(e_p\otimes F)
=
a_p(s)e_p\otimes\langle\Delta',F\rangle.
\]

On a compact Jacobi scale interval \(C\), the local odd observer has bounds

\[
m_C\|F_{\mathrm{odd}}\|
\le
|\langle\Delta',F_{\mathrm{odd}}\rangle|
\le
M_C\|F_{\mathrm{odd}}\|
\]

on the declared one-dimensional source-generated odd-jet line, with \(m_C>0\).

## Raw-prime lower bound fails

In the unweighted counting metric on labels,

\[
\|e_p\|=1.
\]

For normalized local odd vectors \(F_p\),

\[
\|\mathfrak O_{r,a}(e_p\otimes F_p)\|
\le
M_C|a_p(s)|.
\]

Since

\[
p^{-1/2-\sigma}\longrightarrow0,
\]

we have

\[
\inf_p
\|\mathfrak O_{r,a}(e_p\otimes F_p)\|
=
0.
\]

Consequently no cutoff-uniform lower frame bound exists in the raw \(\ell^2\) prime metric. This is not loss of odd orientation. It is the intended Euler half-density.

Any theorem demanding a positive lower bound there would falsely reject the source arithmetic loading.

## Source half-density metric

Define the labelled source norm by transporting the Euler loading:

\[
\left\|
\sum_p e_p\otimes F_p
\right\|_{a,C}^2
=
\sum_p |a_p(s)|^2\|F_p\|^2.
\]

Then prime diagonality gives

\[
\|\mathfrak O_{r,a}F\|^2
=
\sum_p|a_p(s)|^2
|\langle\Delta',F_p\rangle|^2.
\]

Hence, on the source-generated odd-jet subbundle,

\[
m_C^2\|F\|_{a,C}^2
\le
\|\mathfrak O_{r,a}F\|^2
\le
M_C^2\|F\|_{a,C}^2.
\]

The frame constants are independent of the prime cutoff. The arithmetic decay is part of the domain metric rather than a defect of the observer.

If logarithmic or grade factors are present, they must appear on both sides through the source-fixed loading. They cannot be removed merely to improve the estimate.

## Completion typing

The established projective exponential Köthe packet already gives equicontinuous prime truncations and strong convergence for the source currents in fixed finite-order dual rungs. Because \(\mathfrak O_r\) is prime diagonal and locally uniformly continuous on compact \(r\)-regions, it passes through those truncations at the same topology level:

- test vectors converge in the projective test topology;
- Hilbert square packets converge in their weighted Hilbert norm;
- seam currents converge in the declared fixed strong-dual rung;
- weak dual boundary values remain weak where that was the original promise.

This conclusion is conditional only on using the same source weight in the labelled Jacobi packet. It does not authorize a stronger common Hilbert topology at the seam.

## Remaining Green quotient gate

Prime labels, cutoffs, and reciprocal sewing now commute with the odd Jacobi contraction before Green reduction. What remains is not prime diagonality. It is descent through the relative Green/Stokes radical.

The next theorem must prove

\[
\ker G_{\mathrm{Jacobi}}
\subseteq
\ker\mathfrak O_{r,a}
\]

for every radical direction intended to be quotiented, while retaining the separately typed wall connecting morphism. Since \(\Delta'\) annihilates constants, the Jacobi heat-energy wall is a promising candidate, but the complete adjacent-window radical may contain additional directions and must be audited rather than inferred.

## Conclusion

The odd Jacobi constructor is exactly prime diagonal and cutoff natural. Its completed lower frame is uniform only relative to the Euler half-density metric. Raw-prime coercivity is mathematically false and should not be included among the global margins.

# Sparse Mellin grades have no special parity defect

Author: marici.Grothendieck

Date: 2026-08-28

## Question

Strominger's magnetic current tower collapses when omitted odd depths are
restored. Test whether primitive and square Mellin grades exhibit the same
phenomenon on a finite prime-valuation fiber.

Let

\[
0<\lambda_1<\cdots<\lambda_m
\]

be distinct logarithmic scales. For distinct nonnegative grades
\(k_1<\cdots<k_r\), form

\[
V_{ij}=\lambda_i^{k_j}.
\]

## Generalized Vandermonde theorem

The functions \(x^{k_1},\ldots,x^{k_r}\) form a Chebyshev system on the
positive real axis. Consequently every \(r\) by \(r\) minor obtained from
distinct positive \(\lambda_i\) is nonzero and has the common orientation.
Therefore

\[
\operatorname{rank}V=\min(m,r).
\]

The conclusion depends only on the number of distinct retained grades, not
on whether they are consecutive, even, odd, primitive, or square.

## Effect of restoring a grade

If \(r<m\), adjoining any omitted grade raises the rank by exactly one and
lowers the blind dimension by exactly one:

\[
\dim\ker V^*=m-r.
\]

There is no distinguished local repair by the first missing odd grade. Full
faithfulness occurs only after retaining at least \(m\) distinct grades.

For a prime-power orbit \(\lambda_j=j\log p\), consecutive grades admit a
simple finite-difference description: the first local blind relation for
grades \(0,\ldots,r-1\) is the order-\(r\) finite difference on \(r+1\)
adjacent labels. Sparse grades also have local generalized-Vandermonde
relations, but no parity-specific collapse.

## Consequence for the RH boundary packet

The primitive and square ports are two independent Mellin grades. On a fiber
with more than two labels they necessarily leave a complement whose
dimension grows with the fiber. Restoring one intermediate grade removes one
dimension only. Hence the magnetic omitted-mediator explanation does not
transfer literally.

Any finite collection of primitive, square, and archimedean jets remains a
finite-rank observation of an arbitrarily large valuation fiber. A faithful
boundary anomaly must use the complete grade tower, a source-derived
recurrence quotient, or a nonlocal operator that couples all labels.


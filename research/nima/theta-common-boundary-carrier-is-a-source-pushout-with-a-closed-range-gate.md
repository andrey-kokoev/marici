# The common RH boundary carrier is a source pushout with a closed-range gate

## Canonical finite construction

At finite cutoff \(X\), let \(S_X\) be the labelled theta/Tate source packet. Its two presentations give maps

\[
b_{\mathrm{an},X}:S_X\to B_{\mathrm{an},X},
\qquad
b_{\mathrm{arith},X}:S_X\to B_{\mathrm{arith},X}.
\]

The common carrier should not be chosen by embedding both targets into an arbitrary large space. It is the pushout of these two source maps:

\[
B_X
=
B_{\mathrm{an},X}
\amalg_{S_X}
B_{\mathrm{arith},X}.
\]

For linear carriers this is the quotient

\[
B_X
=
\frac{
B_{\mathrm{an},X}\oplus B_{\mathrm{arith},X}
}{
\operatorname{im}(b_{\mathrm{an},X},-b_{\mathrm{arith},X})
}.
\]

The minus sign is the oriented comparison relation. It identifies boundary values only when the same labelled source produces them.

This construction supplies the common codomain required by the boundary-comparison cone without fitting an ambient coordinate system.

## Finite universal property

Suppose maps

\[
u:B_{\mathrm{an},X}\to Z,
\qquad
v:B_{\mathrm{arith},X}\to Z
\]

agree on the source:

\[
u\,b_{\mathrm{an},X}
=
v\,b_{\mathrm{arith},X}.
\]

Then there is a unique map \(B_X\to Z\) induced from \(u\oplus v\). This is the precise meaning of reconciling the two presentations.

A direct product lacks this property because it retains both coordinates without imposing their source equality. A scalar quotient imposed after determinant formation is too late because it has already erased the typed relation.

## Completion does not automatically preserve the pushout

Every finite-dimensional relation image is closed. After restricted-product or graph completion, the comparison relation can acquire dense nonclosed range.

Let

\[
R:
\widehat S
\to
\widehat B_{\mathrm{an}}\oplus\widehat B_{\mathrm{arith}}
\]

be the completed oriented source relation. The Hausdorff topological pushout uses

\[
\overline{\operatorname{im}R}
\]

rather than merely \(\operatorname{im}R\).

If the image is not closed, completing the algebraic pushout and taking the pushout of completed carriers need not agree. The difference is precisely a completion defect of the comparison cone.

Thus the required Beck–Chevalley or exactness cell is

\[
\widehat{
B_{\mathrm{an}}\amalg_S B_{\mathrm{arith}}
}
\longrightarrow
\widehat B_{\mathrm{an}}
\amalg_{\widehat S}
\widehat B_{\mathrm{arith}},
\]

and it must be an isomorphism in the declared typed category.

## Exact hostile

On \(\ell^2\), define

\[
T(x_1,x_2,\ldots)
=
\left(
x_1,\frac{x_2}{2},\frac{x_3}{3},\ldots
\right).
\]

Every finite compression

\[
T_N=\operatorname{diag}(1,1/2,\ldots,1/N)
\]

is invertible. But

\[
\|T_N e_N\|=\frac1N\to0,
\]

so no cutoff-independent lower bound exists.

The completed operator is injective and has dense nonclosed range. The vector

\[
y=(1,1/2,1/3,\ldots)
\]

lies in \(\ell^2\) and is the limit of finite-range vectors, but its formal preimage is \((1,1,1,\ldots)\), which is not in \(\ell^2\).

Therefore every finite pushout may be exact while the completed comparison cone acquires a genuine defect.

## Relation to the seam obstruction

The same structure appears in the tail–seam graph problem. There, closability and closed-range questions compare a Hankel tail map with a Volterra seam map. Here, the comparison relation includes those analytic maps together with cyclic arithmetic incidence.

The common-carrier theorem cannot be proved by finite determinant equality. It requires the completed relation to be closed, or a stronger source-derived contracting homotopy that supplies a continuous inverse on its image.

## Typed version

The relation is not one Hilbert operator. It lives in a Fourier-saturated multigraph category whose coordinates retain:

- primitive exponential-current topology;
- square tempered/Hilbert topology;
- connected trace-class topology;
- independent seam graph topology;
- endpoint finite-dimensional topology;
- archimedean reservoir topology;
- right, left, and seam support.

Closed range must be tested in that declared product topology. A lower bound in a scalar projection does not suffice.

## DPC

A proposed common boundary carrier passes only if:

1. both legs originate from the same labelled finite source;
2. the carrier satisfies the pushout universal property;
3. the oriented source relation is retained before scalar projection;
4. cutoff inclusions form natural pushout squares;
5. completion commutes with the pushout in the typed topology;
6. the completed relation has closed range or an explicit continuous contraction;
7. support and cyclic arity are preserved;
8. finite invertibility is not used as evidence for completed exactness.

## Outcome

The common boundary carrier is categorically determined at every finite cutoff. The remaining analytic theorem is exact: prove that the source pushout survives completion, equivalently that the completed analytic–arithmetic comparison relation is closed in the Fourier-saturated typed topology. Failure of this property is the precise mechanism by which comparison cohomology can appear at infinity.

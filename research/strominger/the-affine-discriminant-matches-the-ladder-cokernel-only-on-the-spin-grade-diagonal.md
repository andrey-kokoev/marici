# The Affine Discriminant Matches the Ladder Cokernel Only on the Spin-Grade Diagonal

## Exact comparison

The general-spin affine frame has discriminant

\[
d_{\mathrm{aff}}(s)=4s-1.
\]

Independently, the spherical ladder operator

\[
\mathcal A_{s,r}=\bar\eth\,\eth^r
\]

has cokernel equal to the missing lowest target representation of degree

\[
l_{\mathrm{coker}}=s+r-1.
\]

Its dimension is therefore

\[
d_{\mathrm{coker}}(s,r)=2s+2r-1.
\]

Their difference factorizes as

\[
d_{\mathrm{coker}}-d_{\mathrm{aff}}=2(r-s).
\]

Consequently

\[
d_{\mathrm{coker}}(s,r)=d_{\mathrm{aff}}(s)
\quad\Longleftrightarrow\quad
r=s.
\]

On this diagonal, the cokernel degree is (l=2s-1), and its representation dimension is (4s-1). This supplies a source-derived reason for the previously inserted harmonic degree—but only on the spin-grade diagonal.

## Spin-two correction

For (s=2), the affine discriminant is seven. The grade-two ladder operator has

\[
\dim\operatorname{coker}\mathcal A_{2,2}=7,
\]

with missing target representation (mathcal H_3).

The live grade-three magnetic operator instead has

\[
\dim\operatorname{coker}\mathcal A_{2,3}=9,
\]

with missing target representation (mathcal H_4). Therefore the affine seven is not the cokernel dimension of the grade-three operator.

## Disposition of the earlier explanation

The claim that one representation constructor explains (4s-1) uniformly across grade is too strong. The affine discriminant is independent of grade, whereas the ladder cokernel grows by two whenever the grade increases by one.

The corrected statement is:

> The affine discriminant and the covariant ladder cokernel have the same numerical invariant on the diagonal subtheory (r=s). Away from that diagonal, their dimensions differ by (2(r-s)).

This is a genuine common-target relation in the natural numbers:

```text
affine frame at spin s  -> determinant order 4s-1

ladder word at (s,r)    -> cokernel dimension 2s+2r-1
                                      |
                                      +-- equal only when r=s
```

It still does not identify the torsion cokernel with the complex harmonic representation. The no-go for a direct additive intertwiner remains intact.

## What is now explained

The number seven has two distinct statuses:

1. For every affine grade at spin two, it is the order of the affine discriminant group.
2. At ladder grade two specifically, it is also the dimension of the missing target endpoint (mathcal H_3).

The shared value is source-derived on that diagonal slice. Using it at grade three requires an additional cross-grade theorem, and the exact dimension nine is a counterexample to any claim that the ordinary ladder cokernel supplies such a theorem.

## Next constructor question

If the affine frame at grade (g) is meant to correspond to a ladder endpoint at some different grade, a source map must explicitly state the grade transformation. No numerical equality authorizes that transport. The smallest candidate would be a grade-lowering correspondence from the affine grade-three boundary block to the grade-two ladder cokernel, preserving spin, reflection, and boundary support. No such constructor is presently derived.

## Evidence replay

The checker verifies the diagonal law for (1\leq s,r\leq20), the exact factorization, and the spin-two grade-two/grade-three contrast.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/affine_discriminant_ladder_cokernel_diagonal_checks.py
```

Machine-readable results are written to `research/strominger/results/affine_discriminant_ladder_cokernel_diagonal_checks.json`.

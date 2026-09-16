# The finite-stage determinant compiler is canonical and completion reduces to holomorphic ideal convergence

## Question

Can the primitive, square, connected, and archimedean attachments be joined into one determinant-line object without choosing an external G4 loading?

## Claim boundary

Yes at every finite prime-and-grade stage. The compiler is forced by the regularized-determinant identity. Passage to the completed tower requires compact-local holomorphic convergence in the declared ideal and normalization of the first two cumulants; those estimates are not proved here. No external G4 loading is selected.

## Finite-stage compiler

Let \(K_N(z)\) be a finite-stage return operator, with first and second cumulants retained as the already constructed scalar functionals

$$
L_{1,N}(z)=\operatorname{Tr}K_N(z),
\qquad
L_{2,N}(z)=\operatorname{Tr}K_N(z)^2,
$$

in the source-selected primitive and square conventions. Let \(A_{\infty,N}(z)\) be the Gaussian Mellin-line factor. Define

$$
\mathfrak D_N(z)
=
A_{\infty,N}(z)
\exp\left(L_{1,N}(z)-\frac12L_{2,N}(z)\right)
\det_3(I+K_N(z)).
$$

The finite-dimensional regularized determinant identity gives

$$
\det(I+K_N)
=
\exp\left(\operatorname{Tr}K_N-rac12\operatorname{Tr}K_N^2\right)
\det_3(I+K_N).
$$

Hence \(\mathfrak D_N=A_{\infty,N}\det(I+K_N)\). The primitive and square rows are exactly the two removed cumulants, while the connected grades compile into \(\det_3\). There is no additional coefficient choice at finite stage once the source convention for \(L_2\) is fixed.

## Logarithmic connection

Away from the zero divisor,

$$
\partial_z\log\mathfrak D_N
=
\partial_z\log A_{\infty,N}
+
\partial_zL_{1,N}
-
\frac12\partial_zL_{2,N}
+
\partial_z\log\det_3(I+K_N).
$$

This is the determinant-line form of the previously constructed reflected logarithmic contour differential: archimedean, primitive, square, connected, and endpoint/residue terms are components of one connection rather than unrelated scalar appendages.

## Completion criterion

A completed compiler follows if, on every compact parameter set:

1. \(K_N(z)\to K(z)\) holomorphically in a Schatten topology supporting \(\det_3\);
2. \(L_{1,N}\to L_1\) and \(L_{2,N}\to L_2\) locally uniformly in their source-normalized conventions;
3. \(A_{\infty,N}\to A_\infty\) locally uniformly;
4. cutoff transition maps preserve these three factors.

Continuity of regularized determinants in Schatten norm then gives

$$
\mathfrak D_N\longrightarrow
\mathfrak D
=
A_\infty
\exp\left(L_1-\frac12L_2\right)
\det_3(I+K)
$$

locally uniformly. The resulting holomorphic section carries its zero multiplicities intrinsically. An inverse-gap estimate is needed only for a globally bounded logarithmic derivative away from the divisor, not for existence of the determinant section itself.

## Loading boundary

This compiler starts from a named return operator \(K_N\). It does not decide whether an external G4 packet should use the mixed primitive-square loading or the forward theta-shell loading. That source-arrow ambiguity precedes the compiler and cannot be resolved by determinant algebra.

## Disposition

The determinant-line compiler is exact and canonical at finite stage. A subsequent Weierstrass-majorant calculation closes the connected-tail holomorphic trace-norm condition on \(\operatorname{Re}z>-1/6\), provided the declared local return blocks carry the stated holomorphic half-density parameter bound. The remaining completion problem is compatible convergence and normalization of the first two cumulants and Mellin line. External G4 loading and sewing identification remain separate.
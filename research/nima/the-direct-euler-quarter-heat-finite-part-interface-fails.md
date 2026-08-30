# The simplest Euler–quarter-heat finite-part interface fails

## Result

Let

[
C_E
=
4gamma+
sum_{nge1}
left[
rac{2H_n^{(1/2)}-n^{-1/2}}{n^{3/2}}-rac4n
ight].
]

The direct interface derived in the preceding packet would require

[
C_E-4rac{zeta'(3/2)}{zeta(3/2)}=-rac{pi}{3}.
]

A controlled numerical evaluation gives

[
C_Eapprox-5.4170760062,
qquad
C_E-4rac{zeta'(3/2)}{zeta(3/2)}+rac{pi}{3}
approx1.6510629682.
]

Hence the proposed identity fails by a large nonzero amount. In the normalized Gram frame, the missing finite return is

[
Delta_{mathrm{fin}}
=
rac{
C_E-4zeta'(3/2)/zeta(3/2)+pi/3
}{
zeta(3/2)^2
}
approx0.2419315360.
]

## Error control

Euler–Maclaurin gives

[
H_n^{(1/2)}
=
2sqrt n+zeta(1/2)+rac1{2sqrt n}
+rac1{24n^{3/2}}+O(n^{-7/2}).
]

Therefore the summand after subtracting (4/n) is

[
2zeta(1/2)n^{-3/2}+rac1{12}n^{-3}+O(n^{-5}),
]

so the tail after (N) is corrected by

[
4zeta(1/2)N^{-1/2}+O(N^{-2}).
]

The displayed value used (N=3{,}000{,}000), with the leading tail correction. The residual (1.65) is far beyond the remaining truncation error.

## Constructor consequence

Quarter-density matching remains forced by the pole coefficients, but pole matching does not determine the finite part. The direct identification

[
	ext{Euler regular part}
=
	ext{quarter-heat regular part}
]

is false.

The interface must contain an additional finite source-authorized return whose normalized scalar shadow is (Delta_{mathrm{fin}}). The next source audit should test the smallest already-declared candidates:

1. Todd correction of the discrete max kernel;
2. endpoint half-density attachment;
3. archimedean gamma return;
4. a combination fixed by the Beck–Chevalley comparison cell.

This is a useful falsification: it rules out the zero-correction interface while preserving the singular quarter-density theorem.

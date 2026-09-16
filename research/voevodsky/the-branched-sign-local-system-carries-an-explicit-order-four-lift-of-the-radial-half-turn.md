# The branched sign local system carries an explicit order-four lift of the radial half-turn

## Question

Once the determinant transition defines a branched metaplectic double cover, can the radial reciprocal involution be lifted explicitly to an order-four operator carrying all four Fourier characters?

## Claim boundary

Yes algebraically on the radial carrier tensored with the cover's rank-two sign fiber, after choosing the Fourier orientation \(i\) rather than \(-i\). The lift squares to the radial half-turn and has spectrum \(\{1,-1,i,-i\}\). Analytic identification with the external G4 Fourier--Poisson operator still requires the source comparison arrow.

## Branched cover

For the meromorphic determinant transition \(\mathcal S=D_+/D_-\), let

$$
\widetilde X
=
\operatorname{Norm}
\{(z,\eta):\eta^2=\mathcal S(z)\}.
$$

This is the canonical double cover branched at the odd part of \(\operatorname{div}\mathcal S\). Its deck involution acts by \(\eta\mapsto-\eta\). Let \(L_{\rm sign}\cong\mathbb C^2\) denote the regular sign fiber with involution

$$
\tau=\operatorname{diag}(1,-1).
$$

## Square root of the radial involution

Let \(W_u\) be the radial reciprocal swap, with \(W_u^2=I\), and define its spectral projectors

$$
P_+=\frac{I+W_u}{2},
\qquad
P_-=\frac{I-W_u}{2}.
$$

The polynomial operator

$$
R_u=P_++iP_-
$$

satisfies

$$
R_u^2=P_+-P_-=W_u,
\qquad
R_u^4=I.
$$

On the lifted carrier

$$
\widetilde H_{\rm rad}=H_{\rm rad}\otimes L_{\rm sign},
$$

define

$$
\widetilde W_u=R_u\otimes\tau.
$$

Then

$$
\widetilde W_u^2=W_u\otimes I,
\qquad
\widetilde W_u^4=I.
$$

Its eigenvalues are

$$
\{1,-1,i,-i\},
$$

because \(R_u\) has eigenvalues \(1,i\) and \(\tau\) has eigenvalues \(1,-1\). Thus no Fourier character sector is forced into the kernel by spectral mismatch.

## Reflection and branching

Away from the determinant divisor, the two sign sheets are locally trivial and the lift is an ordinary order-four operator. Around an odd divisor point, deck monodromy exchanges the sign sheets. The lifted operator remains globally defined on \(\widetilde X\), even though no single-valued scalar square root exists downstairs.

## Remaining comparison

This construction solves the representation-theoretic obstruction between an involutive radial swap and a four-character Fourier action. It does not prove an intertwiner

$$
C W_{\rm FP}=\widetilde W_u C.
$$

That map must still identify local vacua, valuation lengths, prime/grade labels, four traces, and response cocycles. Equality cannot be inferred from matching spectra alone.

## Disposition

A canonical branched metaplectic carrier and, after Fourier-orientation choice, an explicit order-four lift are constructed from the radial involution and determinant sign local system. The missing external G4 sewing cell is reduced from an impossible spectral comparison to a source-identification intertwiner between two order-four representations.
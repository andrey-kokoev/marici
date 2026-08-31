# The free radial wall crossing has exact inverse-distance blowup and cannot supply seam-uniform G4 bounds

## Question

Can the off-seam free radial resolvent provide cutoff- and parameter-uniform bounds through the critical seam?

## Claim boundary

No. The sewn doubled derivative is skew-adjoint, so its resolvent norm is exactly the inverse distance to the imaginary axis. Its rank-one wall-crossing component already has norm \(1/(2|\operatorname{Re}z|)\). Parameter derivatives diverge at higher inverse powers. Therefore seam-uniform G4 bounds cannot come from the Hilbert resolvent; they require the declared rapid/Laplace rigging and a separate boundary-value comparison.

## Exact full resolvent norm

For unitary sewing, the reciprocal double \(\mathbb D_u\) is skew-adjoint. Its spectrum is the imaginary axis. Hence for \(\operatorname{Re}z\ne0\), normal-operator functional calculus gives

\[
\|(\mathbb D_u-z)^{-1}\|
=\frac{1}{\operatorname{dist}(z,i\mathbb R)}
=\frac{1}{|\operatorname{Re}z|}.
\]

This bound is exact, not only asymptotic.

## Exact wall-crossing norm

For \(a=\operatorname{Re}z>0\), the right-half-plane crossing is

\[
C_z^+=-u\,k_z^-\otimes\ell_z^+,
\]

where

\[
k_z^-(t)=e^{-zt},
\qquad
\ell_z^+(g)=\int_0^\infty e^{-zs}g(s)\,ds.
\]

Both factors have norm

\[
\|k_z^-\|_2=\|\ell_z^+\|
=(2a)^{-1/2}.
\]

Therefore

\[
\|C_z^+\|=\frac{1}{2a}.
\]

For \(a<0\), the reciprocal crossing satisfies

\[
\|C_z^-\|=\frac{1}{2|a|}.
\]

Thus half of the full inverse-distance scale is already carried by the one-dimensional wall channel. No cutoff or arithmetic summability estimate can remove this free seam singularity.

## Parameter derivatives

For \(j\ge0\),

\[
\partial_z^j e^{-zt}=(-t)^j e^{-zt},
\]

and

\[
\|t^j e^{-zt}\|_2^2
=\frac{(2j)!}{(2a)^{2j+1}}
\qquad(a>0).
\]

Hence each differentiated kernel vector has norm proportional to

\[
a^{-j-1/2}.
\]

Leibniz differentiation of the rank-one tensor yields wall-response jets with inverse powers at least of order \(a^{-j-1}\). The complete resolvent identity gives the corresponding operator estimate

\[
\partial_z^j(\mathbb D_u-z)^{-1}
=j!(\mathbb D_u-z)^{-j-1},
\]

so

\[
\|\partial_z^j(\mathbb D_u-z)^{-1}\|
=\frac{j!}{|\operatorname{Re}z|^{j+1}}.
\]
Every fixed jet exists off the seam, but no nontrivial jet family is Hilbert-uniform as the seam is approached.

## Consequence for the radial Laplace rigging

The shell densities and Wronskian currents are rapidly decaying, so their Laplace transforms and all parameter jets remain entire as source probes. This does not contradict Hilbert-resolvent blowup: the source rigging selects vectors whose pairings continue beyond the bounded-resolvent domain.

The continuation must therefore be stated as a rigged pairing

\[
\mathcal S_{\rm rad}
\longrightarrow
\mathcal S_{\rm rad}'
\]

or as an entire source-response section. It cannot be called a bounded Hilbert resolvent on the seam.

## G4 completion consequence

A compact-local bound for the conservative complex must distinguish two parameter regions:

1. compact sets with positive distance from the seam, where the Hilbert resolvent is uniformly bounded;
2. seam-crossing compact sets, where only the source-rigged response may be continued.

Any proof of cutoff-uniform invertibility for the arithmetic Schur complement must show cancellation or renormalization at the level of the full source-derived response. Estimating the free resolvent norm separately gives a divergent bound and cannot close the seam gate.

A scalar cancellation observed after codiagonalization is insufficient; the vector-valued singular wall channel and all jets must cancel in the declared feature topology.

## Hostiles

A checker must reject:

1. a seam-uniform Hilbert resolvent bound;
2. omission of the exact factor \(1/2\) in the wall-crossing norm;
3. bounded zeroth-order pairing used to infer bounded parameter jets;
4. an entire source pairing renamed as a bounded seam resolvent;
5. scalar Schur cancellation used without vector-valued feature cancellation;
6. cutoff convergence proved only on compact sets separated from the seam and then promoted across it.

## Disposition

The free radial resolvent has a quantified seam obstruction. Its full norm is \(|\operatorname{Re}z|^{-1}\), its wall crossing has norm \((2|\operatorname{Re}z|)^{-1}\), and its jets diverge at increasing inverse powers. The remaining G4 seam theorem must be a rigged source-response continuation with vector-valued jet control, not a uniform Hilbert-resolvent estimate. No RH conclusion is authorized.

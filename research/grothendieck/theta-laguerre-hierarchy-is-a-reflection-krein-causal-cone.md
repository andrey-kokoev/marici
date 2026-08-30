# The Laguerre hierarchy is a reflection-Krein causal cone

## Bounded question

Does the completed source supply a canonical polarization for the bilinear
transvectants of packet 122, and what would their positivity mean dynamically?

## Source reflection

On the two-copy Hilbert space, let

\[
 (Rf)(u,v)=f(-u,-v).
\]

The completed vacuum `Omega tensor Omega` is reflection-fixed.  With

\[
 \Psi_x=e^{ix\Sigma/2}\Omega^{\otimes2},
\]

complex conjugation satisfies

\[
 C\Psi_x=R\Psi_x.
\]

Also

\[
 R\Sigma R=-\Sigma,
 \qquad
 R\Delta R=-\Delta.
\]

## Exact Krein norm

Packet 122 gives

\[
 (2n)!\mathcal L_n[X](x)
 =\langle R\Psi_x,\Delta^{2n}\Psi_x\rangle.
\]

Move one factor `Delta^n` across the Hilbert pairing.  Since
`Delta^n R=(-1)^n R Delta^n`, one obtains

\[
 \boxed{
 (2n)!\mathcal L_n[X](x)
 =\langle J_n\Delta^n\Psi_x,\Delta^n\Psi_x\rangle,
 \qquad J_n=(-1)^nR.}
\]

Thus every generalized Laguerre form is the norm of the transported source
jet in a canonical parity-adjusted Krein metric.  No polarization has been
fitted from zero locations: `R` is reciprocal reflection and the factor
`(-1)^n` is forced by the parity of the separation operator.

## Positive and negative channels

Let `P_plus=(I+R)/2` and `P_minus=(I-R)/2`.  Expanding the spectral transport,

\[
 \Psi_x
 =\cos(x\Sigma/2)\Omega^{\otimes2}
 +i\sin(x\Sigma/2)\Omega^{\otimes2}.
\]

After applying `Delta^n`, the parity adjustment always designates the cosine
channel positive and the sine channel negative. Consequently

\[
 \boxed{
 (2n)!\mathcal L_n[X](x)
 =\|\Delta^n\cos(x\Sigma/2)\Omega^{\otimes2}\|^2
 -\|\Delta^n\sin(x\Sigma/2)\Omega^{\otimes2}\|^2.}
\]

This is the exact destructive-interference formula between the two reciprocal
phase sectors.

## Causal-cone interpretation

Define the order-`n` source orbit

\[
 F_{n,x}=\Delta^n\Psi_x.
\]

Then

\[
 \mathcal L_n[X](x)\ge0
 \quad\Longleftrightarrow\quad
 F_{n,x}\text{ lies in the }J_n\text{-nonnegative cone}.
\]

Equality is the Krein light cone, where the cosine and sine channel norms are
equal.  Negativity means that the transported orbit has crossed into the
opposite parity sector.

At `x=0`, the sine channel vanishes, so every order starts strictly inside its
positive cone.  The global problem is whether source transport can ever drive
one of these infinitely many jets through its light cone.

This realizes the operator's phase-space intuition precisely:

\[
 \boxed{
 \text{RH-relevant positivity}
 =\text{prohibition of parity-cone crossing under spectral transport}.}
\]

## Relation to scalar zeros

The null cone of `L_n` is not the scalar zero set of `X`.  At a simple real
zero, `L_1=(X')^2>0`.  Scalar zeros are coordinate crossings of the phase
orbit; Krein-null events are losses of higher-order orientation.  Keeping
these types separate prevents another false identification of “zero.”

## Remaining theorem and falsifier

The polarization problem is solved; its **definiteness on the theta orbit** is
not.  The sharp Deutsch--Popperian conjecture is now:

> Integral winding separation and modular sewing keep every orbit `F_(n,x)`
> in its parity-adjusted nonnegative Krein cone for all real `x` and all `n`.

The smallest falsifier is an exact pair `(n,x)` with the sine-channel norm
larger than the cosine-channel norm.  A proof must derive cone invariance from
the labelled source dynamics; calling the displayed difference a norm without
its `J_n` signature would be circular.

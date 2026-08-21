# Cosmology Deck-Transfer Admission Gate

## Question

The finite-set calculation supplies, for every homomorphism of finite deck
groups \(\phi:G\to H\), the unnormalized fiber sum

\[
(\phi_!f)(h)=\sum_{\phi(g)=h}f(g).
\]

It preserves the frozen identity selection,
\(\phi_!\delta_{0,G}=\delta_{0,H}\), composes strictly, and satisfies
Frobenius reciprocity.  Does the five-site cosmological source already supply
this operation physically?

## Source audit

Entries 1223--1225 establish a rank-32 coefficient local system, a rank-32
regular Betti orbit, and their diagonal invariant pairing for
\(G=(\mathbb Z_2)^5\).  They do not specify a quotient cover
\(G\to H\), a forgetting map between physical relative pairs, or a
pushforward of chains along such a map.

Entry 1224 does contain the full orbit trace

\[
\operatorname{Tr}(\Gamma_+)=\sum_{g\in G}g\Gamma_+,
\]

but explicitly distinguishes it from the source-selected chamber cycle
\(\Gamma_+\): replacing chamber evaluation by this invariant trace changes
the observable.  Entry 1225 instead obtains physical continuation covariance
by transporting coefficient and Betti factors together and pairing them:

\[
\langle T c,T\Gamma\rangle=\langle c,\Gamma\rangle.
\]

That diagonal pairing is not a pushforward along a deck quotient.

## Verdict

\[
\boxed{
\text{finite deck transfer is algebraically canonical but is not presently
source-admitted as a cosmological physical operation.}
}
\]

The existing source chooses equivariant chamber transport plus an invariant
coefficient--Betti pairing.  It does not choose orbit summation or quotient
forgetting.  The transfer may become physical only after a source-derived
map of relative pairs supplies:

1. a genuine quotient/forgetting map of covers;
2. its oriented chain pushforward or Gysin morphism;
3. boundary compatibility;
4. the normalization fixing the identity chamber.

Until then, transfer repairs the variance problem in the algebraic deck
readout system but not in the frozen cosmological readout.

## Consequence

This sharpens the sector-indexed picture.  Even a canonical operation on the
coefficient/readout algebra need not be an admissible physical constructor.
Physical admission is extra structure supplied by source geometry, not by
finite-group functoriality alone.

## Sources

- Entry 1223, *The Intrinsic Five-Site Kummer Connection Descends Strictly*.
- Entry 1224, *The Five-Site Physical Sheet Is Equivariant but Does Not
  Descend*.
- Entry 1225, *The Five-Site Coefficient--Betti Pairing Is Deck Invariant*.
- `research/nima/finite-deck-transfer.md`.

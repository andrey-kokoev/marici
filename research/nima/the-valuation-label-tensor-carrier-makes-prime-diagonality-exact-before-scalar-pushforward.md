# The valuation-label tensor carrier makes prime diagonality exact before scalar pushforward

## Correct represented space

Representing every prime history directly on one common analytic Hilbert space forgets the source label. The source carrier already has orthogonal valuation/Fock idempotents, so the faithful analytic representation must retain them.

Let

\[
\mathcal L
=
\ell^2\{(p,k)\}
\]

be the label space with basis \(e_{p,k}\), and let \(\mathcal H\) be the analytic history space. The represented carrier is

\[
\mathcal K
=
\mathcal L\widehat\otimes\mathcal H.
\]

Define

\[
P_{p,k}
=
|e_{p,k}\rangle\langle e_{p,k}|
\otimes I_{\mathcal H}.
\]

These are source idempotents, not Fourier–Bohr projections inferred from scalar orthogonality.

## Labelled history representation

For each label, define the window-history block

\[
\Pi_{p,k}
=
P_{p,k}
\bigl(
I_{\mathcal L}\otimes M_{W_{k\log p}}
\bigr)
P_{p,k}.
\]

The assembled history is the diagonal operator

\[
\Pi
=
\bigoplus_{p,k}\Pi_{p,k}.
\]

Therefore

\[
P_{q,\ell}\Pi P_{p,k}=0
\]

whenever

\[
(q,\ell)\ne(p,k).
\]

Prime and grade diagonality are exact by carrier construction.

## Fourier orbit

Fourier acts only on the analytic factor:

\[
\widetilde{\mathcal F}
=
I_{\mathcal L}\otimes\mathcal F.
\]

Hence

\[
[\widetilde{\mathcal F},P_{p,k}]=0.
\]

All four multiplication/convolution presentations remain label diagonal. Fourier saturation therefore preserves prime labels automatically.

## Adams transport

The grade-doubling Adams edge acts on labels by

\[
A_2e_{p,k}=e_{p,2k}
\]

together with the typed analytic history map. It preserves the prime idempotent and changes only grade:

\[
A_2P_{p,k}
=
P_{p,2k}A_2.
\]

No \(q\ne p\) block can appear.

This is the exact prime-label intertwining law required by the previous audits.

## Scalar pushforward is downstream

The arithmetic scalar observer eventually applies a summation or augmentation on \(\mathcal L\). That map intentionally forgets labels and can create cancellations between primes.

It must occur after:

- mixed Green formation;
- Fourier orbit completion;
- label-diagonal closure;
- endpoint and wall attachment.

Using scalar pushforward first recreates the nonfaithful \(B\) versus \(B^{*}\) hostiles.

## Completion

The orthogonal direct sum completes naturally in the weighted arithmetic norm carrying

\[
a_{p,k}=\frac1k p^{-k/2}.
\]

The diagonal operator norm is the supremum of local norms. Euler supercontraction controls the Adams rays.

The remaining completion check is that any source-authorized cross-prime assembly constructor is represented explicitly rather than hidden inside the scalar augmentation.

## Scope

This theorem does not claim that all Green interactions between different primes vanish. It claims that the local Adams history and its Fourier orbit do not manufacture cross-prime incidence.

Authorized global Green kernels may couple distinct label fibers through separate assembly arrows. Those couplings must be typed as such and audited by Schur or frame estimates.

## Frontier

Prime-label preservation for the first Adams edge is closed by the valuation-label tensor representation. The next unresolved gate is compositional:

> Classify the source-authorized cross-prime assembly arrows and prove that scalar augmentation occurs only after their complete typed Green blocks are formed.

This returns the programme to the two-atom constructor-coherence test rather than local analytic diagonality.

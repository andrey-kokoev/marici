# The optical null channel decodes but does not determine the cusp extension

## Question

Does the constructed optical channel compute the unknown ambient cusp parity, or does it only read a class already supplied to its encoder?

## Claim boundary

This audits the logical dependency of the proposed channel. It does not retract the encoder, detector, calibration, or classification theorems.

## Two quotient spaces

The cusp problem supplies an unresolved torsor of ambient lifts with parity coordinate space

\[
K_{\rm cusp}\cong(\mathbb Z/2)^2.
\]

The conductor problem supplies

\[
Q_{\rm cond}=\operatorname{coker}J
\cong(\mathbb Z/2)^2.
\]

Equal abstract group structure does not identify these spaces. A comparison requires a source-derived map

\[
\phi:K_{\rm cusp}\longrightarrow Q_{\rm cond}.
\]

Site exchange restricts an invertible \(\phi\) to two matrices, identity and swap, but does not select between them.

## Dependency of the optical construction

The single-rail and dual-rail encoders have domain \(Q_{\rm cond}\). Their complete channel is

\[
Q_{\rm cond}
\overset{\mathcal E}{\longrightarrow}
\mathcal H_{m optical}
\overset{\mathcal M}{\longrightarrow}
\{0,1\}^2.
\]

On prepared codewords, the decoder verifies

\[
\mathcal M\mathcal E=\operatorname{id}_{Q_{\rm cond}}.
\]

For an unknown cusp lift \(m\), the desired experiment instead needs

\[
K_{\rm cusp}
\overset{\phi}{\longrightarrow}
Q_{\rm cond}
\overset{\mathcal E}{\longrightarrow}
\mathcal H_{m optical}.
\]

No constructed apparatus supplies \(\phi\). Preparing \(\mathcal E(a,b)\) presupposes the input bits; successfully reading them back validates the communication channel but does not determine which bits belong to \(m\).

## Relabelling obstruction

If \(S\) swaps the two bits, both

\[
\phi
\quad\text{and}\quad
S\phi
\]

are exchange-compatible after the corresponding detector-wall relabelling. All encoder and readout tests commute with that relabelling. Therefore those tests cannot choose the global thimble ordering.

## Required physical coupling

A noncircular experiment needs a source interaction

\[
U:
\mathcal T_m\otimes|\mathrm{ready}\rangle
\longrightarrow
\mathcal T'_m\otimes|\mathcal E(\phi[m])\rangle
\]

or an equivalent measurement whose response is derived from the cusp thimble itself. Its two syndrome responses must equal integral pairings with duals of \(e_6\) and \(v_{\rm alg}\), up to a declared ordered comparison.

The known Cut functional is zero on the relevant coinvariant and cannot serve as this coupling.

## Disposition

The optical work constructs and validates a decoder architecture for any supplied conductor class. It does not compute the cusp extension parity. The original global Picard-marking or source-coupling blocker remains, now isolated as the missing comparison \(\phi\).

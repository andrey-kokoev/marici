# Minimal faithful polarizer-probe coordinates

## Question

What is the smallest finite probe family that separates the quotient states of a finite polarization net, and what multiplicity remains below that threshold?

## Claim boundary

This packet treats four ideal normalized linear-polarization states modulo \(180^\circ\) and four ideal polarizer intensity probes. It proves a finite coordinate statement only. It does not establish tomography for arbitrary density matrices, noisy instruments, or SCC state spaces.

## State quotient and probes

Let

\[
Q=\{0^\circ,45^\circ,90^\circ,135^\circ\}
\]

represent normalized linear-polarization states, already quotiented by \(\phi\sim\phi+180^\circ\). A probe at angle \(\theta\) records

\[
m_\theta(\phi)=\cos^2(\theta-\phi).
\]

For a probe family \(S\), define the coordinate map

\[
c_S:Q\to\prod_{\theta\in S}\{0,1/2,1\},
\qquad
c_S(\phi)=(m_\theta(\phi))_{\theta\in S}.
\]

The family is jointly faithful exactly when \(c_S\) is injective.

## One probe is insufficient

At \(\theta=0^\circ\), the records are

\[
1,\ 1/2,\ 0,\ 1/2
\]

for states \(0^\circ,45^\circ,90^\circ,135^\circ\). The fiber over \(1/2\) has multiplicity two. Every single probe in the candidate family has the same reflected-pair ambiguity. A scalar record therefore cannot identify the quotient state.

## Two probes suffice when nonopposite

The family \(S=\{0^\circ,45^\circ\}\) gives

\[
0^\circ\mapsto(1,1/2),
\quad
45^\circ\mapsto(1/2,1),
\quad
90^\circ\mapsto(0,1/2),
\quad
135^\circ\mapsto(1/2,0).
\]

All four coordinates are distinct. Hence two probes suffice, and the one-probe ambiguity proves minimality.

Not every pair suffices. Opposite settings, such as \(0^\circ\) and \(90^\circ\), retain the \(45^\circ/135^\circ\) ambiguity because the second record is determined by the first. The exact criterion in this finite candidate set is that the two probe axes are not opposite modulo \(180^\circ\).

## Relation to the probe programme

This example separates three objects:

1. the full quotient state \(Q\);
2. a compressed measured map \(m_\theta\), which is not monic;
3. a jointly faithful coordinate \(c_S\), which is monic for a minimal two-probe family.

Interaction and reconstruction claims must be made against \(c_S\), not against a single scalar projection. The two-probe family does not create the state; it separates states that the one-probe record identifies.

## Hostile fixtures

- Every singleton family must retain a nontrivial fiber.
- Opposite two-probe families must remain nonfaithful.
- Nonopposite two-probe families must separate all four states.
- Removing either probe from a minimal family must restore ambiguity.
- Equal cardinality of record space and state space does not replace the injectivity check.

## Disposition

Within the finite quotient, the minimal faithful probe depth is two. One probe leaves an exact multiplicity-two fiber, while adjacent probe axes separate all states. This is a constructive instance of faithful quotient coordinates and supplies a finite operational meaning for the user's two-instrument intuition.

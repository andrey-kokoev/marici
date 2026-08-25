# The completed source carries a Klein-four parity-helicity representation

## Representation

Let

\[
 \mathcal H_P^J=\mathcal H_P^{J,+}\oplus\mathcal H_P^{J,-}.
\]

On the antipodally closed label packet `P union p(P)`, define:

- `P`: simultaneous observation-chart and source-label transport, preserving
  helicity;
- `sigma`: complex/helicity conjugation, exchanging `+` and `-`;
- `Q=P sigma`: physical reflection-helicity involution.

Exact tensor gluing and conjugation imply

\[
 P^2=\sigma^2=1,\qquad P\sigma=\sigma P,
\]

so the packet is a representation of `Z2 x Z2`.  This statement is compatible
with every finite jet stage and therefore with the strict LF union.

## Electric and magnetic ports

Define

\[
 \Pi_E=\frac{1+Q}{2},\qquad
 \Pi_M=\frac{1-Q}{2}.
\]

Then

\[
 \Pi_E^2=\Pi_E,\quad \Pi_M^2=\Pi_M,\quad
 \Pi_E\Pi_M=0,\quad \Pi_E+\Pi_M=1.
\]

Consequently

\[
 \ker\Pi_E=\mathcal H_{Q=-1},\qquad
 \ker\Pi_M=\mathcal H_{Q=+1}.
\]

These are parity-projection aliases, not failures of source construction or
transport.  The joint port

\[
 \mathcal J:h\longmapsto(\Pi_Eh,\Pi_Mh)
\]

is faithful, with inverse `(e,m) -> e+m` on its image.  Thus every distinction
forgotten by one parity port is retained by the complementary port.

## Orbitwise normal form

On a two-point label orbit `{xi,p(xi)}`, choose one source-jet coordinate and
its transported partner.  After the invertible Lah change of jet frame, `Q`
has the exchange form

\[
 Q=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

for each helicity-paired coordinate.  Its `+1` and `-1` vectors are the
symmetric and antisymmetric combinations.  Each orbit contributes equal
electric and magnetic dimensions.

At a geometrically fixed label, the same conclusion holds in the fiber after
including helicity: `Q` exchanges the two helicity components.  There is no
zero column.  A tower-like vanishing can appear only after selecting one
projector and discarding its complement.

## First nonfaithful arrow

The completed pipeline so far is

\[
 \mathcal S_P^J\hookrightarrow\mathcal H_P^J
 \xrightarrow[\simeq]{P,\sigma}\mathcal H_{p(P)}^J
 \xrightarrow{\Pi_E\ \mathrm{or}\ \Pi_M}\mathcal H_{Q=\pm1}^J.
\]

The first two arrows are faithful.  Either individual projector is the first
nonfaithful arrow; their joint refinement is faithful.  This locates the
universal parity kernel before any grade-three, contour, or conservation
specialization.

## Evidence

`checkers/completed_parity_helicity_representation_checks.py` verifies the
group relations, projector algebra, orbitwise ranks, individual kernels, and
joint faithfulness for hostile multiplicities and jet-stage dimensions.

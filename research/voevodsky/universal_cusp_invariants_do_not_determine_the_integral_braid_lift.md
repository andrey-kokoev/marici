# Universal cusp invariants do not determine the integral braid lift

## Question

Can the already proved primitive, norm-minus-six, canonical-parity, single-Weyl-orbit properties determine the Picard–Lefschetz image of a chamber braid word?

## Claim boundary

This packet gives an integral Picard-lattice counterexample. It does not identify either counterexample class with a particular physical braid.

## Two indistinguishable candidates

Write

\[
\operatorname{Pic}(S)=\mathbb Z\langle H,E_1,\ldots,E_7\rangle,
\]

with \(H^2=1\), \(E_i^2=-1\), and

\[
K_S=-3H+E_1+\\cdots+E_7.
\]

For exceptional curves \(C=E_1\) and \(C=E_2\), form their Geiser component differences

\[
d_i=-K_S-2E_i.
\]

Then both satisfy

\[
d_i^2=-6,
\qquad
K_S\cdot d_i=0,
\qquad
d_i\equiv-K_S\pmod2,
\]

and both are primitive. They are distinct and related by the Weyl reflection exchanging \(E_1,E_2\).

The integral functional

\[
\ell(v)=(E_1-E_2)\cdot v
\]

distinguishes them:

\[
\ell(d_1)=2,
\qquad
\ell(d_2)=-2.
\]

Thus every universal invariant already established at all four cusps is compatible with at least two different labelled integral outputs carrying opposite detector values.

## Role of the missing object

The braid-to-Picard lift is not needed merely to prove that some primitive class exists. That is already known. Its role is to select the labelled representative \(d_C\) inside the 56-element oriented Weyl orbit and fix its sign relative to the physical path.

Accordingly, information must flow as

\[
\text{kinematic chamber}
\longrightarrow
\text{ordered lower-half-plane braid word}
\longrightarrow
\text{oriented vanishing cycle}
\longrightarrow
\text{labelled }d_C\in\operatorname{Pic}(S)
\longrightarrow
\text{primitive detector pairing}.
\]

Skipping the braid and vanishing-cycle stages leaves only Weyl-invariant data, which cannot determine the detector value.

## Disposition

The known universal cusp parity cannot substitute for the missing lift. A conforming lift must output an explicit Picard column, not only its norm, divisibility, mod-two class, or Weyl orbit. The two dominant-chamber braid words become discriminating only after their labelled columns and orientations are computed.

Verification:

- `research/voevodsky/checkers/check_universal_cusp_invariant_nonuniqueness.py`
- `research/voevodsky/results/universal_cusp_invariant_nonuniqueness.json`

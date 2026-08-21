# Finite-time one-loop reconstruction contract

## Scope

This packet freezes the source data needed to reconstruct the terms of orders
\(\eta _0^1\) and \(\eta _0^0\) omitted from Sec. 5.2 of Collins--Holman--
Vardanyan, arXiv:1408.4801.  It does not claim that the reconstruction has
already been performed.

The source calculation is an abbreviated toy truncation.  It retains only

\[
S^{(3)}=M_{\rm pl}^2\int d^4x\,
\epsilon(3\epsilon+2\delta)e^\rho
\zeta\,\partial_k\zeta\,\partial^k\zeta,
\]

from the full cubic inflationary action.  The source explicitly states that
finite-time renormalization of the full single-field theory requires all cubic
operators.  Consequently every result from this packet is scoped to the toy
truncation.

## Immutable source conventions

- External momentum: \(\vec p\).
- Loop momentum: \(\vec q\).
- Second internal momentum: \(k=|\vec p-\vec q|\).
- The four Schwinger--Keldysh propagators are built from the Bunch--Davies
  Wightman functions in Eq. (9), with the source-internally forced correction
  \[
  G_k^<(\eta,\eta')\propto
  (1-ik\eta)(1+ik\eta')e^{+ik(\eta-\eta')}.
  \]
  The TeX source prints a negative exponential for both \(G^>\) and \(G^<\).
  This cannot be used literally: the paper's own definitions for a real field
  require \(G^<(\eta,\eta')=G^>(\eta,\eta')^*\).  Every computational packet
  must report that correction explicitly.
- The bulk cubic interaction is the source interaction used in Eqs. (8), (13),
  and (14).  Its contracted bulk--bulk graph is Eq. (13), with vertex factor
  \((p^2+q^2+k^2)^2\).
- The source-derived cubic boundary kernel is
  \[
  C(k_1,k_2,k_3)=\frac1K\left(\frac1{K\eta _0}-i\right),
  \qquad K=k_1+k_2+k_3,
  \]
  from Eq. (12).
- The boundary vertex is inserted as
  \[
  H_0^{(3)}(t)=-\frac12\delta(t-t_0)S_0^{(3)},
  \]
  in Eq. (18).  Equation (17) fixes the authoritative integrated insertion as
  \[
  \int_{t_0}^{t}H_0^{(3)}(t')dt'=-S_0^{(3)}.
  \]
  Consequently the displayed local delta notation corresponds formally to
  endpoint mass \(2\).  It must not be combined with an unrecorded full- or
  half-weight endpoint convention.
- Bulk counterterms are included through
  \(\bar H_I=H_I+H_{ct}\), as in Eqs. (16)--(18), before the initial-state
  matching is extracted.
- In the displayed solution for the bulk counterterms, the third coefficient
  is \(c_1\), not the repeated \(c_3\) printed in the TeX source:
  \[
  c_1=\frac{H^2}{M^2}\frac{(3\epsilon+2\delta)^2}{128}
  \operatorname{Inf}(3I_2-5I_4-I_0).
  \]
  This label is uniquely forced by cancellation of the three independent
  late-time powers.

The complete source expression is therefore the four-sector expansion of

\[
-\frac12\int_{t_0}^{t}dt'\int_{t_0}^{t}dt''\,
\langle T\,\zeta^+\zeta^+
[\bar H_I^+-\bar H_I^-+H_0^{(3)}]_{t'}
[H_I^+-H_I^-+H_0^{(3)}]_{t''}\rangle .
\]

The four labelled sectors must remain separate until after contraction:

1. bulk--bulk;
2. bulk--boundary;
3. boundary--bulk;
4. boundary--boundary.

## Reconstruction procedure

1. Wick-contract each labelled Schwinger--Keldysh sector using Eq. (9), without
   first combining the two mixed sectors.
2. Convert both bulk times to conformal time and apply the endpoint delta only
   after the contour labels and time ordering are fixed.
3. Add the dynamical counterterm graph before sorting by powers of \(\eta _0\).
4. Reduce the answer in the independent late-time structures
   \[
   1+p^2\eta^2,
   \quad
   (1-p^2\eta^2)\cos 2p(\eta-\eta_0)
      +2p\eta\sin 2p(\eta-\eta_0),
   \]
   \[
   (1-p^2\eta^2)\sin 2p(\eta-\eta_0)
      -2p\eta\cos 2p(\eta-\eta_0).
   \]
5. Sort coefficients at orders \(\eta _0^2\), \(\eta _0^1\), and
   \(\eta _0^0\).  Keep loop integrals unevaluated and source-labelled.

The endpoint reduction must preserve the full frequency label

\[
\omega=\alpha p+\beta q+\gamma k
\]

until equal labels are combined.  A polynomial fit along a sequence holding
only the external \(2p\) phase fixed is invalid because unresolved internal
frequencies alias into its fitted powers.  Nonzero-frequency Laurent monomials
are reduced by the asymptotic primitive recurrence; zero-frequency
\(t^{-1}\) terms are retained explicitly as logarithms.

## Corrected mandatory acceptance gate

The original version of this packet required literal reproduction of Eq. (19).
Entries 1558--1562 have since falsified that gate: the printed doubling of both
boundary-containing sectors is incompatible with the source exponent,
endpoint multiplicativity, the complete labelled Wick census, and the
three-point sewing discriminant.

The authoritative cubic-loop regression gate is now

\[
\boxed{
\mathcal C^{(2)}_{\rm cubic,osc}=J_1-2J_2-J_0,
\qquad
\mathcal C^{(2)}_{\rm cubic,zero}=0.
}
\]

This gate must be passed before bulk counterterms are added. Counterterm
contributions are then inserted with the corrected \(c_1,c_2,c_3\) labels and
must themselves be reduced into the same quadratic response basis. The full
renormalized result must reproduce Eq. (21)'s response types; Eq. (19)'s
boundary-sector coefficients are no longer an admissible normalization
target.

The bounded provenance and limitations of this correction are recorded in
`research/benincasa/finite-time-eq19-erratum-packet.md`.

## Hadamard test after reconstruction

Only the sum of the renormalized loop and all three matched initial-state
orders defines the candidate \(\Delta G_{\rm ren}\).  Its large-\(p\) equal-time
asymptotics must then be tested directly.  The displayed \(p^3\) behavior of
\(\operatorname{Im}A_p\) is a statement about the boundary action kernel; by
itself it neither proves nor disproves the Hadamard property of the corrected
two-point function.

Even a passing test proves only one-loop preservation within the abbreviated
single-vertex model.  It cannot be promoted to the complete single-field
inflationary state without repeating the construction for the full cubic
interaction basis and its counterterm mixing.

## Narrow status

The reconstruction is source-determined in principle: the interaction,
propagators, contour expression, boundary kernel, delta insertion, and bulk
counterterms are all printed.  The paper does not print the contracted
\(\eta_0^1\) and \(\eta_0^0\) integrands.  They must be derived; no published
formula may be silently inferred from Eq. (19).

The arXiv source payload was also audited.  It contains a single `paper.tex`
file and no ancillary notebook or supplementary derivation, so there is no
primary-source computational packet beyond the printed formulas.

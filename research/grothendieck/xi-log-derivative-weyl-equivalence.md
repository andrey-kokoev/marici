# The theta logarithmic derivative is the exact Weyl gate

Epistemic-graph event: 1418.

Correction (Ledger 1401, event 1447): the scalar minimal Herglotz
realization has one dimension per distinct atom; an atom of mass \`m_gamma\`
does not itself create an eigenspace of dimension \`m_gamma\`. The determinant
statement below therefore uses the multiplicity amplification recovered from
the integer pole residues of \`M_Xi\`, not the scalar minimal realization alone.

## A source-defined candidate

Let

\`Xi(z)=xi(1/2+i z)\`

be defined by the theta/Poisson integral of Ledger 1377, without factoring or
querying its zeros. Define the meromorphic function

\`M_Xi(z)=-Xi'(z)/Xi(z)\`.

This is the canonical amplitude-retaining successor to the scalar phase ratio
of Ledger 1380. It keeps the vanishing order as a pole residue instead of
cancelling it against the conjugate factor.

## Exact positivity equivalence

The following are equivalent:

1. every zero of \`Xi\` is real;
2. \`M_Xi\` is a meromorphic Nevanlinna function:
   \`M_Xi(conj z)=conj(M_Xi(z))\` and \`Im M_Xi(z)>=0\` for \`Im z>0\`.

For the forward implication, the even order-one canonical product is

\`Xi(z)/Xi(0)=prod_(gamma>0)(1-z^2/gamma^2)^(m_gamma)\`.

Therefore

\`M_Xi(z)=sum_(gamma>0) m_gamma
[1/(gamma-z)+1/(-gamma-z)]\`,

with the symmetric convergence dictated by the canonical product. Each term
\`1/(lambda-z)\` has positive imaginary part in the upper half-plane.

For the reverse implication, a Nevanlinna function is holomorphic off the real
axis and its meromorphic poles are real with nonpositive residues. Every zero
of \`Xi\` is a pole of \`-Xi'/Xi\`, with residue minus its positive integer
multiplicity. A nonreal zero would therefore contradict the Nevanlinna
property. Because zeros of \`Xi(z)\` are critical-line parameters for zeros of
\`xi(s)\`, condition 1 is the Riemann hypothesis.

Thus the missing positivity theorem has been localized exactly:

\`RH iff M_Xi is Nevanlinna\`.

## Conditional self-adjoint realization

Under this positivity condition, the meromorphic Herglotz realization theorem
produces a boundary triple with Weyl function \`M_Xi\`. More concretely, its
representing measure is the positive atomic measure

\`mu=sum_gamma m_gamma delta_gamma\`.

The scalar minimal Herglotz model has one dimension per distinct atom and a
boundary vector whose squared component is \`m_gamma\`. To recover zero
multiplicity in a determinant, amplify the fiber at \`+/- gamma\` to
\`C^(m_gamma)\`, with \`A\` acting as the corresponding scalar on that fiber.
The positive integers \`m_gamma\` are recovered nonnumerically as minus the pole
residues of \`M_Xi\`. This amplified operator has compact resolvent and
\`A^{-1}\` Hilbert--Schmidt. Its symmetric second regularized determinant is

\`det_2(I-z A^{-1})
=prod_(gamma>0)(1-z^2/gamma^2)^(m_gamma)
=Xi(z)/Xi(0)\`.

The exponential factors in \`det_2\` cancel between \`+gamma\` and
\`-gamma\`. Multiplication by the source-known constant \`Xi(0)\` recovers the
completed determinant exactly.

This construction need not be fed a numerical zero list: \`M_Xi\` is defined
directly from the theta kernel, its distinct real support and integer residues
are recovered from that function, and the multiplicity amplification is
canonical up to unitary equivalence. It is not the minimal scalar Herglotz
realization when a zero is multiple. Proving that the representing measure is
positive is exactly RH, so the construction is conditional rather than a
solution.

## Remaining source-derivation gate

Even if Nevanlinna positivity is proved analytically, one further provenance
condition remains. A general Herglotz realization is an abstract inverse
spectral construction. The requested Mellin boundary requires the same
\`M_Xi\` to arise from a declared boundary trace/defect map of the
Mellin-dilation and paired coefficient--Betti system. No such relative-chain
or operator-domain map is currently available.

The exact two-part target is therefore:

1. derive Nevanlinna positivity of \`-Xi'/Xi\` from a positive source object,
   proving RH; and
2. identify that positive realization with a source boundary quotient rather
   than an abstract spectral model.

## Scope

This is an unconditional equivalence and a conditional determinant
realization. It is not a proof of positivity/RH and not yet a physical or
Carrier-level Mellin boundary.

Boundary-triple reference: Behrndt, Hassi, and de Snoo,
[Generalized boundary triples, Weyl functions and inverse problems](https://arxiv.org/abs/1706.07948).

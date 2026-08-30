# The Weil explicit formula is the global prime--gamma boundary morphism

Epistemic-graph event: 1439.

## Logarithmic test algebra

Let \`g\` be a smooth compactly supported function on the additive logarithmic
line. Define

\`g^*(u)=conj(g(-u))\`

and let \`h=g*g^*\). Its Fourier transform satisfies

\`H(t)=|G(t)|^2>=0\` for real \`t\`.

The centered Weil explicit-formula distribution \`W\` pairs such test
functions with the completed zeta data. In standard normalization its
arithmetic side has the schematic exact form

\`W(h)=W_infinity(h)+W_endpoint(h)
-sum_(n>=2)Lambda(n)n^(-1/2)
[h(log n)+h(-log n)]\`.

The first two terms are the gamma and completed endpoint distributions. The
last term is precisely the paired intrinsic-prime-power distribution found in
Ledgers 1388--1392. All divergent pieces are combined in the single
explicit-formula functional; no finite Euler cutoff is promoted separately.

## Spectral side and positivity

Contour shifting gives the equal spectral expression

\`W(h)=sum_rho H((rho-1/2)/i)\`,

with the standard symmetric regularization and multiplicities. This identity
derives the completed zero divisor as residues; it does not require a supplied
numerical zero list.

If RH holds, every parameter \`gamma=(rho-1/2)/i\` is real, and therefore

\`W(g*g^*)=sum_gamma |G(gamma)|^2>=0\`.

Weil's positivity criterion proves the converse: positivity on all admissible
convolution squares forces the completed zero divisor onto the critical line.
Thus

\`RH iff W(g*g^*)>=0 for every admissible g\`.

This is the global version of the Pick and Stieltjes positivity equivalences
in Ledgers 1382--1385.

## Canonical quotient

Define on the test algebra the Hermitian form

\`<g_1,g_2>_W=W(g_1*g_2^*)\`.

Its radical quotient is unconditional and source-derived from the
gamma-plus-prime explicit formula. Under RH it is positive and its Hilbert
completion is the Weil space. Without RH it is an indefinite quotient.

This supplies the previously missing global renormalization morphism:

\`paired prime--gamma test algebra -> radical quotient of W\`.

It is cutoff-independent and retains the exact negative prime directions;
positivity is imposed nowhere.

## Comparison with the xi Pick preshape

On the spectral side, the formal Cauchy feature at \`z\` is

\`c_z(gamma)=1/(gamma-z)\`.

Its Gram kernel against \`c_w\` is the pole expansion of

\`K_Xi(z,w)
=[-Xi'(z)/Xi(z)-conj(-Xi'(w)/Xi(w))]
/(z-conj(w))\`.

Therefore the Weil quotient and the Pick preshape have the same formal
completed spectral Gram law. Establishing an actual isometry requires
extending \`W\` from compactly supported smooth tests to the Cauchy-resolvent
vectors and proving density/closability. Those analytic domain statements are
not automatic from the explicit formula and remain a separate gate.

## What this does and does not solve

The global comparison morphism is now derived noncircularly. Its positive
descent is exactly Weil's RH criterion, so the explicit formula does not prove
positivity. Nor does it by itself construct a fixed self-adjoint operator:
after positivity one still needs the closable multiplication relation,
compact-resolvent proof, and determinant normalization of Ledger 1382.

The gain is structural: no unknown counterterm remains to be invented.
Theta/Poisson completion and the Weil formula already supply the unique
global prime--gamma renormalization. The sole mathematical obstruction is the
positivity/closure of its quotient.

## Scope

This identifies the canonical global source morphism and its radical quotient.
It does not prove Weil positivity/RH or the Cauchy-domain isometry to the Pick
space.

Primary references:

- André Weil's explicit-formula positivity criterion, as reviewed in
  [Pérez Marco, Notes on the Riemann Hypothesis](https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/riemann.pdf).
- The centered explicit formula and positivity applications in
  [Stephen D. Miller, The Highest-Lowest Zero and
  other Applications of Positivity](https://arxiv.org/abs/math/0112196).

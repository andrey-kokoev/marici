# Higher-coherence topology iteration 08: compact-open holomorphic totalization preserves Xi divisibility but cannot see Haar positivity

## Candidate topology

Place parameter-dependent cone packets in the nuclear Fréchet space

\[
\mathcal O(D;B)
\]

of `B`-valued holomorphic sections with compact-open seminorms

\[
p_{K,j}(F)=\sup_{z\in K}\|\partial_z^jF(z)\|_B.
\]

For scalar or nuclear Fréchet `B`, bounded families are normal and all finite
spectral jets pass continuously through locally uniform limits. This is the
natural topology for the complete Evans jet tower.

## Xi ideal

The independent bordered defect already satisfies

\[
\Delta(z)=\tau(z)H(z),
\qquad H\not\equiv0.
\]

In compact-open topology, the closed condition of vanishing through the full
multiplicity of every zero of `tau` is exactly membership in the principal
holomorphic ideal

\[
\tau\mathcal O(D;B).
\]

Therefore repeated holomorphic cones can totalize all Xi-divisible defects
without losing multiplicity. This is a genuine successful topology for the
analytic chain comparison.

## Why it does not encode the energy residual

The relative-Haar residual is

\[
r_p(z,\bar z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z).
\]

It is Hermitian/real-analytic rather than holomorphic in `z`. It is not an
object of `O(D;B)`. Holomorphic totalization can prove that a complex-linear
boundary defect lies in the Xi ideal, but cannot turn that statement into the
vanishing of a positive function depending on `bar z`.

## Real-analytic enlargement

Enlarge to holomorphic sections on the complexification

\[
\mathcal O(D\times\overline D;B)
\]

and restrict to the real diagonal `w=bar z`. Then the Haar multiplier becomes

\[
1-p^{-(z+w)}.
\]

Point evaluation and all mixed jets remain continuous. Hence a persistent
residual still vanishes in the completed topology only if

\[
1-p^{-(z+\bar z)}=0
\]

or the state energy vanishes. The enlargement types the residual but does not
absorb it.

## Normal-family rigidity

Locally uniform completion cannot erase bounded zero incidence or a fixed
nonzero evaluation. If finite higher fillers converge normally and their
completed readout is zero, then every compatible finite readout converges to
zero. A stage-independent value `r_p(z)` therefore must already be zero.

Conversely, allowing convergence that is not locally uniform can create or
remove zeros and destroy jet continuity. Such a topology cannot preserve the
multiplicity theorem that motivated the holomorphic completion.

## Verdict for topology 8

Compact-open/Montel topology is optimal for:

- all Evans parameter jets;
- closed Xi-ideal divisibility;
- normal-family cutoff limits;
- preservation of zero multiplicities.

It sharply separates the analytic success from the Hermitian obstruction. The
Haar residual either lies outside the holomorphic category or remains visible
in the real-analytic complexification.

The next nonredundant topology to test is a sheaf/hypercohomological topology,
where local higher fillers may glue only up to Cech cocycles and the residual
could survive or vanish as a global obstruction class.
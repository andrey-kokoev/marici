# Carrier incidence gives reachability, not yet causality

## Candidate bridge

The shared Carrier repeatedly supplies finite incidence cells and their
transport. The smallest nontrivial test is the pentagonal rank-two
associahedral cell. Declare two vertices adjacent when they share an edge and
let

\[
F_d(i)=\{j:\operatorname{dist}_{\rm inc}(i,j)\le d\}.
\]

This is a support filtration indexed by composition depth.

The exact checker verifies two structural properties:

1. every dihedral automorphism transports \(F_d(i)\) to \(F_d(g i)\);
2. relational composition is subadditive:
   \[
   F_m\circ F_n\subseteq F_{m+n}.
   \]

Therefore Carrier incidence already contains a canonical combinatorial
precursor of finite propagation:

\[
\boxed{
\text{incidence generators}
\Longrightarrow
\text{automorphism-natural bounded support growth}.
}
\]

No background spatial coordinate is needed for this statement.

## Decisive obstruction

The same pentagon has a reflection fixing one vertex while exchanging its two
neighbors. That reflection preserves every unoriented support ball. Hence the
filtration cannot distinguish the two local directions and supplies neither
future nor past:

\[
\boxed{
\text{Carrier reachability filtration}
\not\Rightarrow
\text{causal orientation}.
}
\]

This is the exact analogue of the distinction between a metric neighborhood
and a light cone. Incidence depth says how many local compositions are needed
to connect two sites; causal polarity says which composites are physically
future-directed.

The Carrier has other objects called polarity or orientation lines, but no
established comparison identifies those algebraic signs with spacetime time
orientation. Making that identification by terminology would be mistyped.

## Updated bridge contract

A Carrier-to-causal comparison now has two stages:

\[
\mathfrak C_{\rm Carrier}
\xrightarrow{\;\text{incidence depth}\;}
(\text{support filtration},d)
\xrightarrow{\;\tau\;}
(\text{future-directed probe cone},J^+).
\]

The first arrow has a finite exact model and is natural under the pentagon's
full automorphism group. The second arrow requires a source-derived causal
polarity \(\tau\) that:

1. selects future-directed generators;
2. is preserved by admissible orientation-preserving transport;
3. transforms correctly under time reversal;
4. composes without directed cycles;
5. agrees across scattering, radiative gravity, and cosmology.

If such a \(\tau\) exists and retains the finite support bound, the earlier
frame-naturality theorem selects the Lorentz-like branch. Without it, the
Carrier supplies a finite interaction distance but not a speed of
information.

## Interpretation

The progress is real but narrower than deriving spacetime:

\[
\boxed{
\text{Carrier may already explain locality as finite compositional depth;}
\quad
\text{time orientation remains coefficient/readout data}.
}
\]

The sharp next test is not another graph census. It is a comparison between
the Carrier polarity line and a physically admitted time-orientation line,
including a hostile reflection that reverses one while preserving or
reversing the other.

Exact artifacts:

- \`research/nima/checkers/check_carrier_incidence_support_filtration.py\`
- \`research/nima/results/carrier_incidence_support_filtration.json\`

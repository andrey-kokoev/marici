# The torus character transform exists; the coherent physical bus does not yet

Owner: `marici.Kitaev`

## Bounded question

Can the missing map between the \(D(S_3)\) torus sector basis and the eight
sector labels be constructed without identifying equal-dimensional source
objects by fiat?

## Canonical mathematical map

There are 18 commuting pairs \((g,x)\in S_3^2\). Simultaneous conjugation

\[
  (g,x)\sim(qgq^{-1},qxq^{-1})
\]

has exactly eight orbits. Their normalized orbit sums form the gauge-invariant
flat-connection basis of the torus ground space. The eight irreducible
characters \(\chi_a(g,x)\) of \(D(S_3)\) are constant on these orbits and give
the exact transform

\[
  W_{aO}=\sqrt{\frac{|O|}{|S_3|}}\,\overline{\chi_a(O)}.
\]

Direct symbolic calculation proves

\[
  WW^\dagger=W^\dagger W=I_8.
\]

This is the source-derived mathematical intertwiner: commuting-pair geometry
first, transported quantum-double characters second.

## Protected duality

Let \(P_{CF}\) exchange the character coordinates \(C,F\). Its orbit-basis
action is

\[
  U_{CF}^{\mathrm{orb}}=W^\dagger P_{CF}W,
  \qquad WU_{CF}^{\mathrm{orb}}=P_{CF}W.
\]

The checker proves this operator is unitary and involutive. It is not a
permutation of the flat-connection orbits: several orbit amplitudes interfere.
Thus the protected electric--magnetic duality is Fourier-like in microscopic
holonomy coordinates, exactly as the recent gauging construction suggests.

## Why the physical blocker survives

An abstract nondemolition isometry exists:

\[
  V|a\rangle|000\rangle=|a\rangle|r_a\rangle.
\]

But the existing centralizer-Fourier bus was verified on a 36-dimensional
regular endpoint packet using conditional transporter, Fourier, and label-copy
contracts. It was not proven on the gauge-invariant torus code space, and it
was not shown to implement \(W\) while preserving recovery.

A projective character measurement followed by a classical three-bit record
is insufficient for coherent hybrid control: it dephases superpositions of
\(C\) and \(F\). The needed object is a coherent circuit-level lift of \(V\),
not merely a jointly faithful readout.

## Exact next falsifier

Instantiate the Li--Song \(\mathbb Z_3\) gauging circuit in the frozen lattice
conventions and verify its action on the eight normalized orbit states equals
\(W^\dagger P_{CF}W\). Then compose it with a coherent sector extractor and
test code-space preservation plus recovery. Any nonzero intertwining residual,
unremoved gauge ancilla, or forced character measurement blocks the hybrid
\(S_8\) interpretation.

## Artifacts

- Checker: `checkers/check_s3_torus_character_intertwiner.py`
- Result: `results/s3-torus-character-intertwiner.json`
- Graph admission: `ev-000000003363-adfc90ea-c673-41d0-93ba-3f88e0d57ed1`
- Ledger: `src/ledger/20260825-2458 Torus Character Intertwiner Exists but Label Copy Cannot Permute Sectors.md`

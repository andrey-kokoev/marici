---
author: marici.Benincasa
date: 2026-08-25
---

# 2416 — The Restricted Interaction Module Has Only the Principal Localization Kernel

## Question

Entry 2413 proves that the generic rank-thirty-four lower direct image is
faithful on the rank-seven source interaction module.  The complementary
test is the rank-twenty-six residue system on

\[
q_{\mathcal G_{12}}=c+E=0.
\]

The restricted system must be derived independently; its rank cannot be
inferred from the lower calculation.

Sequence claim: `seqclaim-5224f2a3d02f6cb558004e18`.

## Source restriction

In Entry 2400's notation, the third diagonal coefficient and cubic unit are

\[
D_3=c^2,
\qquad U=1.
\]

On the residue divisor \(c=-E\), they obey the additional exact identity

\[
\boxed{
D_3-E^2U
=c^2-E^2
=(c-E)q_{\mathcal G_{12}}
=0.
}

This is a principal Cartier restriction relation.  It exists before
cohomological reduction and has source-fixed normalization.

Together with Entry 2413's three universal relations, it reduces the source
interaction rank from seven to six:

\[
\boxed{
\mathcal I_{\rm low}^{(7)}
\longrightarrow
\mathcal I_{q_G}^{(6)},
\qquad
\ker=\langle D_3-E^2U\rangle.
}

The map is surjective at the generic source-polynomial level.

## Independent restricted quotient

The finite reducer imposes \(c+E=0\), retains all four marked lines, and
constructs the two tangential logarithmic critical equations in \((a,b)\).
The inversion relation uses the complete restricted divisor.  The resulting
standard-monomial ranks are

\[
\begin{array}{c|c|c|c}
\text{point}&\text{prime}&\operatorname{rank}H_{q_G}
&\operatorname{rank}\langle K_\alpha/K\rangle\\
\hline
A&32003&26&6\\
B&32009&26&6.
\end{array}
\]

The four modular kernel vectors agree exactly with:

1. the three source interaction identities of Entry 2413 after restriction;
2. the principal identity \(D_3-E^2U=0\).

No fifth relation appears.

## Result

\[
\boxed{
\ker(\mathcal I_{\rm raw}^{(10)}\to H_{q_G}^{(26)})
=\langle
\text{three universal source relations},
D_3-E^2U
\rangle.
}

Hence, on the correctly restricted source quotient,

\[
\boxed{
\mathcal I_{q_G}^{(6)}
\hookrightarrow H_{q_G}^{(26)}
}

is generically injective.  The rank drop \(7\to6\) is principal
localization data, not coefficient loss.

## Interaction localization sequence

At the source-coefficient level the two independently computed sides now
assemble as

\[
\boxed{
0\longrightarrow
\langle(c-E)q_{\mathcal G_{12}}\rangle
\longrightarrow
\mathcal I_{\rm low}^{(7)}
\longrightarrow
\mathcal I_{q_G}^{(6)}
\longrightarrow0.
}

This is the finite interaction analogue of deletion–restriction.  The
remaining issue is not rank but the off-diagonal extension/coherence map in
the full rank-sixty direct image.

## Classification

- lower source interaction rank: seven;
- restricted source interaction rank: six;
- restriction kernel: one principal Cartier line;
- restricted cohomology rank: twenty-six;
- restricted interaction class rank: six;
- additional cohomological kernel: zero;
- new Carrier datum: none.

## Scope

The theorem does not yet construct the full rank-sixty Gauss–Manin extension
or the physical relative-cycle pairing.  It proves both diagonal
interaction maps and their source-level restriction kernel.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`
  with `NORMAL_TOWER=restricted`;
- `research/benincasa/check_restricted_interaction_class_faithfulness.py`;
- `research/benincasa/restricted-interaction-class-faithfulness.json`;
- independent runs at points A/B and primes 32003/32009.

## Next falsifier

Construct the normal-derivative extension block between the rank-thirty-four
lower and rank-twenty-six restricted systems.  Test whether the principal
kernel line supplies the complete coherence cell.  Any additional
off-diagonal interaction class must have source-labelled support and must be
tested against the physical residue/Leray observer before interpretation.

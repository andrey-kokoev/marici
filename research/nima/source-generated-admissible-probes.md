# Source-Generated Admissible Probes

For a source diagram \(D\), define \(\mathcal P(D)\) as the smallest typed
family containing its primitive probes and closed under every operation the
source and coefficient object actually supply: composition, declared
transport, legal restriction, additive structure, and required coherences.

The hostile model is \(V=\mathbf F_2^2\). The primitive probe
\(p_0(x,y)=x\) alone sees two profiles. A declared coordinate swap generates
\(p_1(x,y)=y\), and the pair distinguishes all four states.

The first account incorrectly called \(p_0+p_1\) fitted. Because the
coefficient object is linear, addition is already legal, so this probe is
source-generated. Transport-orbit closure is not the full typed closure.

Faithfulness remains an outcome rather than an admission rule. With addition
but without swap, the closure stays nonfaithful. With both, it becomes the
complete linear dual and is faithful.

Software translation: an API may derive fields using every operation promised
by its service contract. It may not add an unsupported computation merely
because that computation distinguishes two backend states.

The dependency-free checker passes 8/8 gates.

Sequence claim: seqclaim-aad28a0570e894a773fb9aba.

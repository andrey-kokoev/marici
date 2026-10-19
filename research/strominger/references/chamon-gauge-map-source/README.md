# Pinned Chamon gauge-map source

Authors: Wilbur Shirley, Xu Liu and Arpit Dua, *Emergent fermionic gauge theory and foliated fracton order in the Chamon model*, arXiv:2206.12791v1; published as Phys. Rev. B 107, 035136.

Downloaded `https://arxiv.org/src/2206.12791v1`. Archive SHA-256:
`aa8a1f862185e94005540599367b409c47a3372a8da8759c697c03408a1b1e6a`.

Unmodified members retained:

| Local file | Archive member | SHA-256 |
|---|---|---|
| `main.tex` | `main.tex` | `b2a0aaa58d8e9a67c5fefa03245adb14d1c796691cd54b3bc3856365c70dc793` |
| `supplementary.nb` | `anc/supplementary.nb` | `7b6a7c19767d1402effd295f5e8bda542b6d4bedb07aabc4aa10645be55a0c02` |

These are upstream reference artifacts, not our code. No license change or authorship claim is made. The local checker reads the numerical TeX matrices and the first notebook reduction sequence without executing Mathematica. It independently implements Laurent arithmetic and the declared elementary gates. Other notebook calculations, including entanglement renormalization, have not been imported.

Important retained distinctions: the printed ancillary shear blocks are identity, whereas the notebook uses zero; the reduction includes a `rowMul` translation of wire 7 by `y`. Neither difference is silently discarded. See `../../chamon-gauge-map-v1.md`.

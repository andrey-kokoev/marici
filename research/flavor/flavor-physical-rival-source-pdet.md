# Physical rival-source detector map (WP244)

## Result

WP242 and WP243 physically realize the threshold ports that were only formal
in WP129. On WP129's frozen rival family, restricted to accessible distinct
poles with compulsory nonzero residues, the two calibrated pole-yield ports
give signatures

\[
\begin{array}{c|cc}
\text{constructor} & A\text{ pole} & D\text{ pole}\\\hline
\text{WP128 two adjoints} & 1&1\\
\text{WP127 one auxiliary} & 1&0\\
\text{direct EFT contact} & 0&0.
\end{array}
\]

The contextual partition is discrete at the response-law level. The composed
operation is therefore an asymptotic source-grammar partition on this admitted
domain. The two ports have independently simulated CMS responses, certified
collision readout, and source-to-rate normalization, but WP245 shows that 2016
exposure is insufficient for operational identification.

## Domain-relative faithfulness

Identification is not uniform on the closure of the domain. At
`kappa_D=0`, the two-adjoint signature becomes `(1,0)` and is observationally
identical to the one-auxiliary rival. This is the smallest exact falsifier and
the first nonfaithful arrow:

\[
\text{source grammar}\longrightarrow\text{nonzero pole support}.
\]

The source action must therefore exclude zero portal residues and place both
poles in accessible, resolvable support before the discrete constructor claim
applies. Detector reach cannot impose that condition retrospectively.

The operation inherits full weak-basis descent from WP237/WP243. It adds no
reference port and does not select a `physical16` point. Rival scalar theories
outside WP129's frozen family may share `(1,1)` and are not identified by this
bounded classification.

## Reproduction

Run `uv run --with numpy python
research/flavor/checkers/wp244_physical_rival_source_pdet.py`. The checker
regenerates `results/wp244_physical_rival_source_pdet.json` and requires the
three-way interior partition plus the exact zero-residue collision.

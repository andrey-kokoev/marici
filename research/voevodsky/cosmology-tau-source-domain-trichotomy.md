# Source-domain trichotomy for the universal p-normal lift

## Question

Do any current source-domain candidates satisfy the \(\tau_p\) contract after the residue functor nonfaithfulness gate?

## Claim boundary

This packet re-reads current Voevodsky artifacts and Nima's prior-art gates. It does not construct a new source cover, relative base--fiber comparison, Cayley--Menger face cone, Bockstein class, global contour, or physical period.

## Disposition

The contract remains a unit column

\[
(1,1)
\]

in rows

\[
(\Xi_{\log},-\sigma_{123}).
\]

Nima's prior-art audit identifies one existing internal candidate: the physical normal-adapter gradient-pivot Čech class. It has pairwise Cartan exactness and a second-Čech triple homotopy. Nima's gradient-pivot type gate blocks its direct use here: the candidate uses pivots \((a,b,c)\), but the target fixed fiber has only \((a,b)\); the pivot \(c\) is base-dependent. Restricting to the fixed fiber leaves two charts, one overlap, and no triple face mapping to \(\sigma_{123}\).

The current route table is therefore:

- gradient-pivot normal adapter: available prior art, but fails fixed-fiber cover typing;
- native three-chart marked-fiber cover: not constructed;
- relative base--fiber comparison retaining the \(c\) direction: not constructed;
- Cayley--Menger face cone with compensating residue: not constructed.

The checker verifies that no current route supplies the \(\tau_p\) unit column. The relative p-normal Bockstein and physical period remain unconstructed.

Further repetition of the residue classifier is exhausted. The next admissible nonrepeat task is to construct either a native three-chart marked-fiber cover or a relative base--fiber comparison retaining the \(c\) direction, then test whether its first differential column is \((1,1)\) up to sign.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_tau_source_domain_trichotomy.py`

Result:

- `research/voevodsky/results/cosmology_tau_source_domain_trichotomy.json`

Command:

- `python research/voevodsky/check_cosmology_tau_source_domain_trichotomy.py`

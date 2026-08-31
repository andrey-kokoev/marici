# Typed descriptor interface for exact boundary words

## Result

Every source row in each finite ambient presentation has a unique typed descriptor in one of `T`, `S_K`, or `Q`. Vertical exponent shift by the ambient-degree difference defines an injective admitted map for A12-to-A14, A14-to-A16, and A12-to-A16.

The checked descriptor counts are:

| ambient degree | T | S_K | Q | boundary targets |
|---:|---:|---:|---:|---:|
| 12 | 21,964 | 2,880 | 18,720 | 48 |
| 14 | 29,904 | 4,224 | 25,200 | 60 |
| 16 | 39,076 | 5,824 | 32,640 | 72 |

For every family and inclusion, all shifted source descriptors occur in the target presentation and no two source descriptors collide.

## Disposition

N5b3a is completed. Ambient-local row indices can be replaced by descriptors before exact-word comparison.

This interface result does not show that independently selected exact words transport literally, reconstruct after transport, or compose. The exact boundary solver must next retain every rational coefficient keyed by its typed descriptor. N5b3b then tests literal exact-word transport; failure activates comparison modulo exact source syzygies.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_exact_boundary_descriptor_interface.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_exact_boundary_descriptor_interface.json`

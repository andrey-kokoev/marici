# October 19 research imports

Groups below follow local filesystem creation times on 2026-10-19, not a newly established authorship chronology. These are imported notes and receipts; renaming does not reverify their scientific claims.

| Created | Topic | Note | Checker | Imported receipt |
|---|---|---|---|---|
| 13:37 | FCC tetrahedral–octahedral Gaussian boundary recursion | [Note](fcc_gaussian_boundary_recursion.md) | Original note names `fcc_boundary.py`, `additional_checks.py`, and `exact_recursion_check.py`; not included here | [Results](fcc_gaussian_boundary_recursion_results.json) |
| 13:46 | FCC stable boundary singlet/triplet sectors | Follow-up to the FCC recursion | [Checker](check_fcc_stable_boundary_sectors.py) | [Results](fcc_stable_boundary_sectors_results.json) |
| 14:08 | FCC blocking phases versus Marici coherence | [Note](fcc_blocking_phase_transport_vs_marici_coherence.md) | [Checker](check_fcc_blocking_phase_transport.py) | [Results](fcc_blocking_phase_transport_results.json) |
| 16:05 | WG circle torsor and BU(1) | [Note](wg_circle_torsor_to_BU1.md) | [Checker](check_wg_circle_torsor.py) | [Results](wg_circle_torsor_results.json) |
| 16:48 | Rung successors, joins and cofibers | [Note](marici_rung_join_cofiber_bridge_20261019.md) | [Checker](check_rung_join_bridge.py) | [Results](rung_join_cofiber_bridge_results.json) |
| 17:15 | Audit of prior WG proofs | [Audit](wg_prior_proofs_audit_20261019.md) | — | — |
| 17:34 | Source-level circle/join integration | [Note](marici_source_join_integration_20261019.md) | — | — |
| 18:36 | Witnessed attachment semantics | [Note](marici_wg_attachment_semantics_20261019.md) | [Checker](check_attachment_semantics.py) | Not included |
| 19:02 | Actual source attachment and cut-descent defect | [Note](actual_source_attachment_synthesis_20261019.md) | [Checker](check_actual_attachment.py) | Not included |
| 19:37 | Source-closed homotopy synthesis | [Note](source_closed_homotopy_synthesis.md) | [Checker](check_simplicial_source.py) | Not included |
| 20:09 | Native comparison relations and rung transport | [Note](native_relation_certificate.md) | [Checker](check_native_relations.py) | Not included |

## Renamed imports

| Original download name | Topic-specific name |
|---|---|
| `RESEARCH_NOTE.md` | `fcc_gaussian_boundary_recursion.md` |
| `all_results.json` | `fcc_gaussian_boundary_recursion_results.json` |
| `stable_sector_test.py` | `check_fcc_stable_boundary_sectors.py` |
| `stable_sector_test.json` | `fcc_stable_boundary_sectors_results.json` |
| `RESEARCH_NOTE(1).md` | `fcc_blocking_phase_transport_vs_marici_coherence.md` |
| `check.py` | `check_fcc_blocking_phase_transport.py` |
| `results.json` | `fcc_blocking_phase_transport_results.json` |
| `results(1).json` | `wg_circle_torsor_results.json` |
| `results(2).json` | `rung_join_cofiber_bridge_results.json` |

## Output names and missing dependencies

Calculation receipts are ignored local artifacts, not committed files; receipt links above resolve only when those imports or regenerated outputs are present locally.

Checker output names and reproduction commands distinguish each topic rather than sharing `results.json`. The WG circle checker writes a receipt only when `--output` is supplied. Other unique output names are `wg_attachment_semantics_results.json`, `actual_source_attachment_results.json`, `source_closed_homotopy_results.json`, and `native_relation_certificate_results.json`.

The stable-sector checker still needs the original generated `results/T_side*.npz` kernels. The actual-attachment checker needs its retrieved upstream source files. Those inputs are not supplied by this naming cleanup. Original environment/provenance statements in the notes remain historical claims.

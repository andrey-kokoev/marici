# A shared reservoir permits isolated-versus-pair comparison

## Question and construction

Complete the singular incidence response of the 1836-arrow structure without deleting its constant mode or changing the surrounding system between cases. Add one reservoir node and equal-strength links k to each of the 108 original ports. The original internal graph is unchanged; the completion adds 108 links, giving 109 nodes and 1944 links in total. This is a declared symmetric boundary model, not a WG-selected construction or a reinterpretation of the internal 1836 count.

Grounding the reservoir is a gauge choice on this connected Laplacian system. The original-port equation becomes

    (D + k I) x = J.

The reservoir equation supplies the compensating source -sum(J). Use a uniform +1/36 source at the raw ports and a uniform -1/36 source at the aligned ports. These are signed source fixtures, not a derived electric-charge operator or the fine-coordinate eigenmode intensities.

The same graph and k serve all cases:

| Configuration | Original-port total source | Reservoir source |
|---|---:|---:|
| Proton-like source alone | +1 | -1 |
| Witness-like source alone | -1 | +1 |
| Pair | 0 | 0 |

The pair still has nonzero local response even though its net reservoir source vanishes.

## Exact source reduction

On stage-constant potentials, the original graph supplies

    D_stage = [[1404,-108,-1296],
               [-108,540,-432],
               [-1296,-432,1728]].

Reservoir links add 36 k to each diagonal. Rational elimination solves this three-variable system, and the checker independently verifies every original-port equation plus the reservoir equation, so the reduction is not merely a guessed aggregate fit.

## Two energy functionals give opposite cross-term signs

Stored-field energy is W=J^T(D+kI)^-1 J/2. For the opposite signed sources, its pair-minus-isolated cross-term is negative:

| Reservoir link strength k | Stored-field cross-term |
|---|---:|
| 1/4 | -1040/28057, approximately -0.0370674 |
| 1 | -17/1831, approximately -0.00928454 |
| 4 | -5/2152, approximately -0.00232342 |

These are unit-metric response energies, with no conversion to electron-mass units.

The previous shared-environment model minimized W-J^T x, whose value is -W. Its cross-term therefore has the opposite sign: positive for this opposite-sign pair. The two functionals represent different source-work accounting and cannot be exchanged silently to obtain binding. Same-sign controls reverse both cross-terms. No distance-dependent force has been computed.

Consequently the response equation alone does not select the physical energy readout. This is the principal new distinction: a neutral composite lowers stored-field energy relative to its isolated sources, but does not lower the earlier minimized scalar-relaxation functional.

## Weak reservoir limit

Each isolated unit source has a constant-mode field energy 1/(216 k). The neutral pair has no constant-mode source and its field energy tends to 5/13824 as k tends to zero, agreeing with the previous closed neutral solution. The isolated comparison therefore depends essentially on the reservoir; the isolated divergences do not cancel in the pair-minus-isolated cross-term. No reservoir-independent binding value follows from this limit.

## Verification and disposition

`python research/nima/checkers/check_wg_reservoir_completion.py` passed via structured-command execution `structured_command_execution:e_32876_1791216971288010700_10`.

Exact checks cover all 109 source equations, superposition, stored-field energy against source work, sign reversal, sensitivity to k, and the neutral zero-mode limit. Results: `results/wg-reservoir-completion.json`, including the source-arrow digest. The coupling scale and physical source-work readout remain unspecified by WG; no mass target was fitted. No publication or commit is claimed.

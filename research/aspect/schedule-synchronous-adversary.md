# Cyclic position balance can resonate with schedule-synchronous dynamics

In a cyclic rotation, cell `c` occupies position `p=c+b` in block `b`. A disturbance depending on synchronous phase `p-b` therefore sees the constant label `c`, even though every cell occupies every position and every block is complete.

For each period `2`, `4`, `8`, `16`, and `32`, the exact hostile assigns response one to synchronous phase zero and zero otherwise. One rotation family gives false cell spread one at every period while passing cell and position marginals.

The repair introduces 32 independently sealed permutation-family offsets. With offset `s`, the synchronous phase is `c+s`. Across all offsets, every cell samples every residue equally for all five periods. The false cell spread becomes zero. The raw analysis must also report residual Fourier power at those periods; balance is a design certificate, while the spectrum checks realized execution.

The required carrier is therefore `cell × position × block phase × permutation family`, not separate marginals of those labels.

Executable witness: `checkers/check_schedule_synchronous_adversary.py`.

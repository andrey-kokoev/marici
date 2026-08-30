# One passing reset depth does not certify the recovery law

The ready/dead model predicts predecessor spread

\[
\Delta_k=\frac9{25}\left(\frac{16}{25}\right)^k
\]

for every reset depth from zero through ten. Consecutive nonzero spreads therefore have exact ratio `16/25`.

The hostile adds a second memory mode with retention `1/2`. Its spread is the equal mixture of the two exponentials. A single depth can remain below the qualification tolerance, but the ten consecutive ratios are not constant and the recurrence residuals are nonzero.

The reset run must sweep depths `0…10` and test the frozen geometric recurrence simultaneously. Failure identifies additional state—afterpulse, thermal relaxation, recovery age, or modulator hysteresis—and invalidates the two-state basis for selecting five bins.

Executable witness: `checkers/check_reset_depth_law_falsifier.py`.

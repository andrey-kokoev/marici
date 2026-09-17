# qRB microstep 61: common-baseline correction

Prior research indicates that prime and prime′ channels should not be modeled as two independent copies with separately canceling common modes. They act in one common translation/scaling representation.

The correct decomposition is

$$
\text{prime phase current}
=
\text{positive summed density}
-
\text{one common Plancherel baseline}.
$$

Thus the relative subtraction is a single common-mode removal in the shared carrier, followed by the polarity-sensitive boundary readout. Prime labels remain source-diagonal before codiagonalization, but common-history overlap can create cross-prime blocks afterward.

This replaces the earlier naive pairwise cancellation ansatz. The next estimate must control the codiagonal cross-prime block, not cancel each prime against an independently copied prime′ mode.

Status: pairing model corrected; common-baseline codiagonal estimate remains open.

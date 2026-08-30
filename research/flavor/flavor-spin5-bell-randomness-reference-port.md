# Spin(5) Bell-randomness reference port (WP913)

## Question

Can a physically typed added reference experiment supply the independent
event-key constructor missing from WP910 through WP912?

## Reference-port construction

Adjoin a device-independent randomness-expansion experiment based on a
loophole-free Bell test, an entropy-accumulation analysis, and a declared
extractor. This changes the experiment and its physical groupoid. It does not
reveal randomness or independence already present in the unaugmented flavor
simulation.

The port emits one extracted bit string (R) together with:

- Bell-trial inputs, outputs, timing, and spacelike-separation record;
- detector-efficiency and no-signalling support assumptions;
- entropy-accumulation transcript and soundness parameter;
- extractor family, seed provenance, and output length;
- immutable allocation of disjoint output blocks to event-key identifiers.

The primary experimental precedent is the loophole-free
[device-independent randomness experiment](https://www.nature.com/articles/s41586-018-0559-3),
which reported (6.2469\times10^7) extracted bits with total failure below
(10^{-5}). A later
[device-independent randomness-expansion experiment](https://www.nature.com/articles/s41567-020-01147-2)
reported (2.57\times10^8) net certified bits with soundness error
(3.09\times10^{-12}). These are precedents for the port type, not acquired
flavor-run records. Quantum-proof extraction is supported by the
[leftover-hashing theorem with quantum side information](https://arxiv.org/abs/1002.2436).

## Product-law transport

Suppose the certified extracted string is within distance
(epsilon_{\rm rng}) of a uniform string independent of admitted side
information. Partition it deterministically into disjoint 256-bit event keys.
Uniform bits factor exactly across those blocks. Marginalization, deterministic
partitioning, and the WP910 event-local transform cannot increase total
variation or trace distance. Therefore the complete paired output record is
within (epsilon_{\rm rng}) of the ideal product-key experiment.

This is the explanatory constructor WP912 lacked: the product structure comes
from a certified global string, not from passing a tower of marginal tests.

## Error-budget repair

WP911 spent the full (1/20) budget statistically. Reserve instead

\[
\epsilon_{\rm rng}=10^{-10}
\]

and allocate the remaining

\[
\alpha_{\rm stat}=\frac1{20}-10^{-10}
\]

equally across two strata, two poles, and four looks. The checker recomputes
all look sizes by exact integer binomial tails. The sum of statistical and
randomness soundness errors is then at most (1/20).

The cited (2.57\times10^8)-bit precedent is large enough for 350,276 disjoint
256-bit keys, which require 89,670,656 bits. This is only a capacity comparison;
the published bits are not reused and do not instantiate the proposed run.

## Changed groupoid and remaining gates

The Bell apparatus, setting-seed preparation, extractor, transcript verifier,
and bit-to-event allocation form a new relational reference port. Its admitted
groupoid is the stabilizer of the complete certified transcript and allocation
map. Relabellings that preserve only aggregate bit counts are not admitted.

The construction remains conditional until a fresh port run is executed. The
initial private setting seed, device isolation, loophole closure, entropy
analysis, extractor implementation, and integration with the CMS event-local
adapter must all be realized. A public randomness beacon may timestamp or
commit the protocol, but public pulses alone do not supply the private seed or
the Bell certificate.

This port repairs acquisition for a detector-response experiment. It does not
select a flavor point or rigidify texture charts.

Run:

~~~text
uv run python research/flavor/checkers/wp913_spin5_bell_randomness_reference_port.py
~~~

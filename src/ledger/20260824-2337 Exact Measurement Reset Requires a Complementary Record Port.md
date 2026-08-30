# Entry 2337: Exact measurement reset requires a complementary record port

The return-arrow obstruction of Entry 2336 has an exact information-flow
form.  The binary nonselective Lüders channel

\[
\mathcal D(\rho)=\Pi_+\rho\Pi_++\Pi_-\rho\Pi_-
\]

has Choi rank two.  A unitary dilation that returns the complete apparatus and
environment to one fixed pure state induces a rank-one channel.  It therefore
cannot realize \(\mathcal D\).

The working pointer can be reset reversibly by transferring its bit to a
record:

\[
(s,s)\longmapsto(0,s).
\]

Thus reset is record transport, not record destruction.  A reusable exact
measurement constructor needs both:

\[
\text{working-apparatus return}
\quad+\quad
\text{complementary record/waste port}.
\]

If the finite record memory is itself restored, its information must be
transported into another declared resource or the measurement must be undone.
Landauer heat is a later reservoir-dependent consequence; the present result
is the temperature-independent channel-rank theorem beneath it.

This refines the five-face constructor criterion into a six-face diagram:
task, interaction, displayed record, conditional successor, working return,
and complementary record transport, coherent under repetition.

Evidence:

- `research/nima/toric-reset-waste-port-conjecture.md`
- `research/nima/toric-reset-is-record-transport.md`
- `research/nima/checkers/check_toric_reset_waste_port.py`
- `research/nima/results/toric_reset_waste_port.json`
- sequence claim `seqclaim-2552b0da5b3ad717b18ff60b`

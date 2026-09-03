# Bounded Rees prefix instrumentation

Problem: measure provenance growth on an actual Rees prefix without launching a
full computation.

Bold conjecture: bounded-prefix counts suffice to establish direct full-scale
feasibility.

Rivals: direct provenance vectors, checkpointed replay, and target-only
extraction.

Risky consequence: provenance and operation growth must remain controlled, but
a prefix must also sample the dependent-row regime before it predicts the full
presentation.

Strongest falsification attempt: at ambient degree four and prime 101, the first
512 of 4,320-column relation rows were instrumented. All 512 were independent.
Reduction operations rose from 22 at row 64 to 55 at row 512; mean provenance
support fell from 1.34 to 1.17, the maximum rose from 3 to 11, and 600 retained
entries were 0.229 percent of the dense prefix bound.

Disposition: falsified as a full-feasibility claim, retained as an
instrumentation proof. The prefix lies before substantial dependencies and
cannot predict the 9,780-row ambient-eight system. No full run was launched.
The next leaf constructs checkpointed replay whose retained state is bounded
independently of expanded source combinations.

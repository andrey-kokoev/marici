# Spin(5) response-branch disposition (WP916)

## Objective audit

The flavor objective asks whether a source-derived operation selects a proper
subspace or distinguished point of the admissible `physical16` lens family.
WP893 through WP915 instead developed a conditional detector-response
experiment around the Spin(5) two-pole source card.

The completed typing is

\[
\begin{aligned}
&\text{free source card }(q_u,q_v)\\
&\longrightarrow\text{chosen two-pole event generators}\\
&\longrightarrow\text{paired detector-response comparison}\\
&\longrightarrow\text{null-completed discordance certificate}.
\end{aligned}
\]

The Bell and multi-source ports, if physically executed, would justify the
randomization law used by the comparison. They are external reference
constructors and explicitly change the experimental groupoid.

## Missing selector arrow

WP897 leaves two independent nonnegative mixing coordinates (q_u,q_v).
Production rates scale with them, while universal branching fractions cancel
them. None of WP898 through WP915 supplies a source action, variational law,
fixed point, threshold boundary condition, or geometric constraint that maps
the admissible source family into a proper `physical16` image.

The zero-drift predicate asks whether changing the declared width changes the
detector record by more than a tolerance. It does not ask which value of
((q_u,q_v)) nature prepares. Passing it for several source cards preserves
those cards; it does not select among them.

In the exact finite audit, take the four-point source grid

\[
Q=\{(1,1),(1,4),(4,1),(4,4)\}.
\]

The response-validation operation maps every card to `admissible_for_response`
under the zero-drift hypothesis. Its image contains all four cards, so the
selection reduction is zero. A faithful downstream readout could distinguish
the cards by rate, but WP299 already proves that faithful readout is not
selection.

## Architectural classification

- **Carrier:** conditional Spin(5) two-pole source card and fixed nuisance
  strata.
- **Admissible lenses:** free (q_u,q_v) family plus declared pole data.
- **Source selector:** absent.
- **Presentation rigidifier:** absent in this branch.
- **Physical readout:** prospective null-completed width-response instrument.
- **Reference port:** prospective Bell/multi-source event-key acquisition,
  defining a new relational experiment.

The first missing arrow is before detector simulation: no independently
derived map sends the Spin(5) source card to a proper `physical16` family. No
amount of randomization, replay, locality testing, or discordance precision can
repair that absent source map.

## Decisive disposition

Close the zero-drift branch as a conditional instrument-design programme. It
is neither selector nor rigidifier. Its smallest exact selector falsifier is
two distinct admitted source cards receiving the same response-admissibility
record.

The progressive successor must return upstream. The nearest explicit
conditional selector is WP360's invariant portal

\[
V_{\rm int}=\lambda(J^2-cQ)^2,
\]

which would select a codimension-one `physical16` shell if derived from an
admitted flavor action. Its coefficient and common-frame instrument remain
unauthorized. The next bounded source question is therefore whether an
independent Spin(5), RG, threshold, or geometric construction derives such an
invariant portal without using the desired low-energy answer.

Run:

~~~text
uv run python research/flavor/checkers/wp916_spin5_response_branch_disposition.py
~~~

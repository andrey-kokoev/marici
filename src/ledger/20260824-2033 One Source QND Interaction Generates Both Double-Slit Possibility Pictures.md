# One Source QND Interaction Generates Both Double-Slit Possibility Pictures

The existing source-motivated controlled-pointer instrument supplies the
missing same-object structure from Entry 2032.

With path-controlled pointer records

\[
e_L=\binom10,
\qquad
e_R=\binom cs,
\qquad
c^2+s^2=1,
\]

forgetting the pointer gives interference visibility

\[
V=|\langle e_L,e_R\rangle|=|c|,
\]

while optimally separating the same pointer records gives

\[
D=|s|.
\]

At the existing exact source point \((c,s)=(3/5,4/5)\),

\[
\boxed{V^2+D^2=1.}
\]

The normalized sum/difference pointer basis produces two conditioned
full-visibility subensembles with opposite phase.  Forgetting that eraser
outcome recombines them to the original unconditioned coherence.  Hence
which-path measurement and quantum erasure are different readout and
conditioning operations on one joint source state, not retroactive changes of
history.

The exact Symbolic checker passes 8/8 gates using the repository-prescribed
invocation:

```text
uv run --with sympy python research/nima/checkers/check_double_slit_qnd_source_instrument.py
```

Boundary: this proves a bounded two-path/two-level source realization.  It
does not show that the common Carrier generates the QND interaction, nor does
it derive continuum propagation or Born frequencies.

Artifacts:

- `research/nima/double-slit-qnd-source-instrument.md`
- `research/nima/checkers/check_double_slit_qnd_source_instrument.py`
- `research/nima/results/double-slit-qnd-source-instrument.json`

Sequence claim: `seqclaim-1906bcf4b8a5480766ec90c6`.


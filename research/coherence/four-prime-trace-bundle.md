# The varying graph carries an exact finite Green trace bundle

For a finite breakpoint set \(B\), define the trace fiber

\[
\mathcal T_B
=
\mathbb C_{0+}
\oplus
\bigoplus_{b\in B}(\mathbb C_{b-}\oplus\mathbb C_{b+})
\]

with Green metric

\[
J_B=-1_{0+}\oplus\bigoplus_{b\in B}(1_{b-}\oplus-1_{b+}).
\]

This is the boundary form obtained by integration by parts on the broken intervals.

For right zero-extension, trace transport is forced:

\[
(S_af)(a-)=0,
\qquad
(S_af)(a+)=f(0+),
\]

and

\[
(S_af)((a+b)\pm)=f(b\pm).
\]

The resulting trace map \(\Sigma_a:\mathcal T_B\to\mathcal T_{S_aB}\) satisfies exactly

\[
\Sigma_a^*J_{S_aB}\Sigma_a=J_B.
\]

Thus right shift is a Green isometry between different fibers. The new seam at \(a\) carries the old endpoint flux; no boundary datum is discarded.

For left shift,

\[
(R_af)(0+)=f(a+),
\qquad
(R_af)((b-a)\pm)=f(b\pm),\quad b>a.
\]

This map intentionally forgets the interval and seams below \(a\). Accordingly,

\[
\mathcal R_a^*J_{R_aB}\mathcal R_a-J_B
\]

is a nonzero diagonal relative boundary form supported exactly on the discarded traces. It is not an unexplained failure of naturality: it is the declared relative defect of compression.

For the four-prime subset-sum fiber, \(|B|=15\) and

\[
\dim\mathcal T_B=31.
\]

The checker verifies all four right-shift Green isometries. The left-shift relative residual ranks are respectively

\[
2,4,6,10
\]

for shifts by \(\log2,\log3,\log5,\log7\). Their growth records how many lower seam coordinates each compression removes.

Hence the completed boundary object is an indefinite varying-fiber system

\[
(\mathcal D_B,\mathcal T_B,J_B)
\]

whose arrows are either Green isometries or explicitly bordered compressions. This supplies the trace-level target in which the operator-valued two-cochain and four-cup must be read.

Verification:

```text
python research/coherence/check_four_prime_trace_bundle.py
```

Artifacts:

- `check_four_prime_trace_bundle.py`
- `four-prime-trace-bundle.v1.json`

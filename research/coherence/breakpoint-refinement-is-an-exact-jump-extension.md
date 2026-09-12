# Breakpoint refinement is an exact jump extension, not an equivalence

## One new breakpoint

Let \(B\) be a finite breakpoint set and let \(c\notin B\). The refined broken graph \(\mathcal D_{B\cup\{c\}}\) permits independent traces at \(c-\) and \(c+\). The old graph embeds as the continuity locus

\[
\iota:\mathcal D_B\hookrightarrow\mathcal D_{B\cup\{c\}}.
\]

Define the jump map

\[
J_c(f)=f(c+)-f(c-).
\]

It is continuous and surjective, with kernel exactly \(\iota(\mathcal D_B)\). Hence

\[
\boxed{
0\longrightarrow\mathcal D_B
\longrightarrow\mathcal D_{B\cup\{c\}}
\xrightarrow{J_c}\mathbb C_c
\longrightarrow0.
}
\]

Adding a seam is therefore a cofiber extension by one boundary-defect line.

## Several breakpoints

For \(B\subset C\), the combined jump map gives

\[
0\longrightarrow\mathcal D_B
\longrightarrow\mathcal D_C
\longrightarrow
\bigoplus_{c\in C\setminus B}\mathbb C_c
\longrightarrow0.
\]

The kernel and total cofiber are independent of the order in which points of \(C\setminus B\) are introduced. The checker verifies all 24 orders for four new breaks. Every order has cofiber rank four and the same final continuity kernel.

## What is and is not canonical

The inclusion, jump quotient, and exact sequence are canonical. A splitting

\[
\mathbb C_c\to\mathcal D_{B\cup\{c\}}
\]

is not: it requires choosing a function realizing a unit jump, including its support and metric profile.

Consequently graph refinement is not an equivalence with a contractible choice of inverse. It is a filtered extension carrying genuine residual data.

## Higher formulation

In the derived target, refinement should be represented by the exact triangle

\[
\mathcal D_B
\longrightarrow
\mathcal D_C
\longrightarrow
\bigoplus_{c\in C\setminus B}\mathbb C_c
\xrightarrow{+1}.
\]

Different refinement orders form a commuting cubical filtration. Its associated graded object is the direct sum of jump lines. No higher anomaly appears at the finite incidence level, but no jump line may be discarded as a mere subdivision artifact.

This clarifies the role of the varying graph bundle:

\[
\boxed{
\text{refinement creates typed boundary residuals; it does not merely change coordinates.}
}
\]

The next compatibility test is whether prime-shift sewing maps these exact triangles to exact triangles and transports each jump line to the declared shifted seam line.

## Verification

Run:

```text
python research/coherence/check_breakpoint_refinement_cofibers.py
```

Artifacts:

- `check_breakpoint_refinement_cofibers.py`
- `breakpoint-refinement-cofibers.v1.json`

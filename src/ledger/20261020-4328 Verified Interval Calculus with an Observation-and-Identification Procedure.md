---
author: marici.Nima
title: Verified Interval Calculus with an Observation-and-Identification Procedure
description: Six interval records, their extension and trim operations, a separating three-probe family, and a fixed-sample identification theorem under declared mathematical assumptions.
---

# 4328 — Verified Interval Calculus with an Observation-and-Identification Procedure

## Result and scope

A finite conditional construction now connects interval records, process operations, observations and statistical identification. All six nonempty intervals on a three-edge line have distinct retained cavity-process representatives; all twelve legal endpoint edits are preserved; three declared photon probes separate their probability distributions; and a fixed-sample classifier has a proved error bound below 1%.

Here **verified** means written mathematical arguments with exact rational executable checks. It does not mean a proof-assistant formalization or an experiment. The carrier, passive optical law, detector instrument and statistical assumptions are supplied. This result does not derive AdS/dS geometry, select causal interpretations or time orientations, or determine metric scale. Hardware is outside this entry's scope.

## Interval calculus and complete records

Let $W_0,W_1,W_2$ be the existing three retained round operators on ten optical modes. For $1\le i\le j\le3$, define

$$
E(i,j)=W_{j-1}\cdots W_{i-1}.
$$

These represent the six actual $n=8$ NNMHV compiler records. At the incident slot $u_k=1+3k$, the diagonal entry is $-3/5$ when round $k$ belongs to the interval and $1$ otherwise. The signature recovers the endpoints; the decoder checks the whole canonical matrix before reconstructing the complete source record, including its diagonal boundary update. Endpoint equality does not erase distinct edit histories.

Writing $p=[i,j]$, the four operations obey

$$
\begin{aligned}
E(Lp)&=E(p)W_{i-2} &&(i>1),\\
E(Rp)&=W_jE(p) &&(j<3),\\
E(lp)&=E(p)W_{i-1}^{T} &&(i<j),\\
E(rp)&=W_{j-1}^{T}E(p) &&(i<j).
\end{aligned}
$$

These are process compositions. Applying a bare first-round inverse to the final state generally fails. For an edit $p\to p'$, the based output correction is instead $C_{p,p'}=E(p')E(p)^T$, which satisfies $C_{p,p'}E(p)=E(p')$. Adjacent segments compose in chronological order. The comparison checks all twelve edits, four adjacent compositions, two distinct-history squares and 792 occupation columns across number sectors zero through two. The all-sector composition statement uses the written symmetric-power argument, not finite sampling.

## Observation and identification

In three separate preparation settings, inject one photon into $u_k$, apply the process and measure that slot with the supplied initially ready detector. Both click and no-click outcomes are retained. The actual instrument calculation gives click probability $81/625$ on selected rounds and $9/25$ otherwise. These three coordinates distinguish the six intervals. Every proper subset of this particular probe family has a collision; no minimum over arbitrary observables is asserted.

For calibration, assume a static factor $a_k\ge1/5$ shared by reference and validation exposures at port $k$. Their probabilities are $b_k=a_k$ and $c_k=a_kt_k$, where $t_k\in\{9/25,1\}$ is the interval signature. A reference therefore identifies the ratio $c_k/b_k$ without assuming equal efficiencies across ports.

Take **40,000 independent Bernoulli trials per arm**, with reference and validation at each of three ports: **240,000 total**. Counts and arm sizes are fixed before observing outcomes. Hoeffding's inequality and a union bound give

$$
\Pr\!\left(\max_{\text{six rates}}|\widehat p-p|>1/100\right)
\le12e^{-8}<\frac{3780}{556403}<\frac1{100}.
$$

The rational bound uses a positive Taylor lower bound for $e^8$, avoiding a rounded numerical certificate. The classifier retains only signatures compatible with all six rate intervals and shared factors, reporting an interval only when it is uniquely compatible. Otherwise it returns no interval. On the simultaneous good event, every compatible ratio lies within $2/9$ of the true value, less than the signature gap $16/25$; the true interval is therefore uniquely identified. The error guarantee is an unconditional repeated-design probability, not posterior confidence conditional on certification. The sample count is sufficient, not optimal.

## Falsifiers retained with the result

- **Process versus state:** all six passive processes fix vacuum. Distinct process operators do not automatically encode interval identity in one common output state.
- **Family identification versus tomography:** an output phase flip changes each process while preserving these three counting distributions. Identification requires the canonical-family promise.
- **Shared calibration versus drift:** true interval $[1,2]$ with reference factors $(1/4,1/2,3/4)$ and validation factors $(25/36,1/2,27/100)$ has exactly the same six probabilities as stationary interval $[2,3]$. All factors remain in $[1/5,1]$. More samples cannot resolve this distributional alias without a restriction on drift.

The finite-sample checker also rejects malformed or incomplete count records and exercises zero references, noninterval responses and ambiguous diagnostic regions. It checks 1,536 boundary cases; those cases test the implementation but do not replace the coverage proof.

## Durable verification

Packets, with their source-bound checkers and receipts:

| Stage | Written construction | Checker | Result |
|---|---|---|---|
| Component correction | [Prefix-removal compiler](https://github.com/andrey-kokoev/marici/blob/main/research/nima/cavity-prefix-removal-compiler.md) | `research/nima/checkers/check_cavity_prefix_removal_compiler.py` | `research/nima/results/cavity-prefix-removal-compiler.json` |
| Interval processes | [Process dictionary](https://github.com/andrey-kokoev/marici/blob/main/research/nima/interval-cavity-process-dictionary.md) | `research/nima/checkers/check_interval_cavity_process_dictionary.py` | `research/nima/results/interval-cavity-process-dictionary.json` |
| Observations | [Three-probe theorem](https://github.com/andrey-kokoev/marici/blob/main/research/nima/interval-cavity-probes.md) | `research/nima/checkers/check_interval_cavity_probes.py` | `research/nima/results/interval-cavity-probes.json` |
| Identification | [Finite-sample proof](https://github.com/andrey-kokoev/marici/blob/main/research/nima/interval-cavity-finite-sample.md) | `research/nima/checkers/check_interval_cavity_finite_sample.py` | `research/nima/results/interval-cavity-finite-sample.json` |

Run each checker with Python. Owner-local SCC manifests for the last three stages are `research/nima/scc-models/interval-cavity-process-dictionary.json`, `interval-cavity-probes.json` and `interval-cavity-finite-sample.json`. Their validation/check runs passed; the workbench and broader-outcome audit also passed without promoting the causal-geometry conjectures.

The completed finite-sample claim is `conjecture:390a7a9cf3d34550212a`, recorded by graph event `ev-000000016250-f6208a33-a541-48ac-82d5-c2e4b6f15ea5`, proposal `ep_fc2f0ee5-4b91-4ea0-9249-d161e8331fe1`. Graph admission records the reviewed claim and its scope; it is not an independent truth certificate. Ledger number 4328 was allocated by sequence claim `seqclaim-93b1624a9bd0e9a4cecfd3fb`.

[Public results](/research/results/#october-20-verified-interval-calculus) · [Theory overview](/research/theory/#finite-interval-processes-and-observations)

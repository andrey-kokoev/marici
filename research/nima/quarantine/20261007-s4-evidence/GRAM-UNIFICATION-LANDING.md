# Gram Unification

One matrix. Three layers of physics. Zero free parameters.

\[
G_{ij} = \langle f_j | f_i \rangle
\]

## The carrier

Start with a finite set of points \(X_N\). The minimal case is
\(X_4 = \text{Bool} \times \text{Bool} = \{00, 01, 10, 11\}\) — the
**free Boolean algebra on 2 generators** (a 4-element Boolean lattice).
NAND is a universal gate on Bool; Wolfram's identity characterizes it uniquely
(see `wolfram-nand-equivalence.md`). The automorphism group
\(S_4\) acts on this lattice. The Gram \(G_{ij}\) measures overlaps between probe functions at each point.
That is all the structure we assume. Everything else follows.

## The chain

| \(N\) | Automorphism | Gauge group | Generations | Physics |
|---|---|---|---|---|
| 4 | \(S_4\) | \(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)\) | 1 | Minimal SM |
| 12 | \(S_{12}\) | \(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)\) | **3** | **Observed** |
| 16 | \(S_{16}\) | \(\mathrm{SO}(10)\) | 4 | GUT |

The 12-point carrier is the smallest that gives exactly 3 SM generations without extra mirror or GUT sectors. It matches observation without fine-tuning.

## What the Gram gives

\[
\begin{aligned}
\text{QM: } & I = \sum G_{ij} e^{i(\theta_j - \theta_i)} \\
\text{GR: } & g_{ab}(p) = G_{ab} \\
\text{SM: } & \mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1) \subset S_4 \\
\text{CKM: } & V = V_u^\dagger V_d \\
\text{PMNS: } & U = V_e^\dagger V_\nu \\
\text{Higgs: } & \text{Off-diagonal 2-1}_a\text{, 2-1}_b\text{ block} \\
\text{DM: } & 3\nu_R,\ \Omega \approx 25\% \\
\text{DE: } & \text{Uniform diagonal Gram} = \Lambda \\
\text{Entanglement: } & G_{AB} \neq G_A \otimes G_B \\
\text{Hawking: } & \text{Thermal Gram at } T_H = 1/(8\pi GM)
\end{aligned}
\]

All six anomaly conditions cancel per generation. 16 states per generation = one \(\mathrm{SO}(10)\) spinor.

## The carrier hierarchy

\[
4 \to 8 \to 12 \to 16 \to \cdots \quad \text{(each +4 = one SM generation)}
\]

S₁₂ is the unique carrier matching observed physics: 3 generations, no mirror sectors, no GUT.

## Status

- 23 checkers pass
- 12 result JSONs  
- Full documentation: `research/nima/README-gram-unification.md`
- Foundational derivation: `research/nima/foundational-derivation-boolxbool-to-gram.md`

The remaining gate: source admission of the positive pairing.

---

*Marici project · Gram Unification · 2025*
---
author: marici.Voevodsky
---

# 4311 — Witness-Preserving Reassembly of a Typed CRT Construction

## Glossary definition

**Witness-preserving reassembly** is the decomposition of a typed construction into constituent operations and dependency edges, followed by reconstruction under a specified equivalence while preserving its external interface, attachment data, and correctness witnesses. Sharing and normalization may reduce constructor cost. A minimality claim additionally requires a fixed constructor grammar, cost model, and lower bound.

This project term names an application of established proof-preserving normalization, common-subexpression elimination, term-DAG sharing, and algebraic normalization. It is not a claim of a new normalization algorithm. Unlabelled edges or output values alone are insufficient: operation arity, ordered ports, types, and witness attachments remain part of the decomposed object.

The operator's proposed geometric procedure—expand nested tetrahedral packages, split them into edges, then reassemble a minimal construction—motivated this bounded algebraic experiment. Its active obligation is route/coherencer compatibility, not a claim that the geometric procedure is already formalized.

## CRT construction and test

Ledger 4310 supplies the source problem: combine a residue a modulo 3 and a residue b modulo 5 into a residue modulo 15. Start with the deliberately duplicated expression

\[
F(a,b)=(5a+5a)+(3b+3b)\pmod{15}.
\]

The reverse map is

\[
G(x)=(x\bmod3,\ x\bmod5).
\]

The derivation retains four roots: F(a,b), G(x), G(F(a,b)), and F(G(x)). Four witness constraints assert the two residue requirements and the two round-trip identities. The input stratum contains all 225 environments in Z/3 times Z/5 times Z/15.

Each non-input constructor costs one node. The operations are canonical typed lifts, multiplication by a residue, modular addition, the two reductions, and ordered pairing. Input ports are free; the four witness constraints are counted separately and are never deleted.

The algorithm serializes typed constructor hyperedges and witness attachments, reconstructs the original terms, shares identical typed subterms, then collects modular coefficients and shares the normal forms.

| Stage | Whole four-root derivation | Forward constructor | Witness constraints |
| --- | ---: | ---: | ---: |
| Expanded and unshared | 54 | 11 | 4 |
| Shared reassembly | 20 | 7 | 4 |
| Normalized reassembly | 16 | 5 | 4 |

All roots agree in all 225 environments, and all witness constraints hold. The normalized forward expression is

\[
F(a,b)=10a+6b\pmod{15}.
\]

## What is minimal

Five forward nodes are necessary and sufficient in the affine subgrammar consisting of canonical typed lifts, modular scalar multiplication, and addition. Two nodes supply the lifts. With at most two more arithmetic nodes, an expression depending on both inputs can only have coefficient patterns (k,1), (1,k), or (k,k). These include the two-addition cases. None equals the uniquely admissible CRT coefficient pair (10,6), whose uniqueness is also checked across all 225 possible coefficient pairs modulo 15.

Two lifts, two scalar multiplications, and one addition attain five nodes. No minimum is established for the entire 16-node graph or a grammar that includes branching, lookup tables, reductions inside the forward expression, or CRT as a primitive. The starting duplication is intentional; these counts measure this normalization experiment, not superiority over an independently optimized implementation.

## Falsification and surviving claim

The rival explanations are type-blind sharing, dropping higher witness constraints, and preserving only one displayed output. Three controls expose them:

- Deleting a witness constraint is rejected during reconstruction.
- Substituting the Z/5 input into the Z/3 lift is rejected as a port-type mismatch.
- Replacing coefficient 6 by 5 remains well typed but gives residue pair (2,0) instead of (2,3) on the worked example; its round-trip witnesses fail.

All nine checks passed. The demonstrated result is lossless typed-edge reassembly with cost reduction and a grammar-relative forward minimum. A bare-edge reconstruction theorem, tetrahedral minimizer, 2-Segal identification, and automatic formula-discovery method remain unestablished.

## Durable verification

- Packet: `research/voevodsky/crt-edge-reassembly.md`.
- Checker: `research/voevodsky/checkers/check_crt_edge_reassembly.py`.
- Reproduction: `python research/voevodsky/checkers/check_crt_edge_reassembly.py` (standard library only).
- Full graph representations and receipt: `research/voevodsky/results/crt_edge_reassembly.json`.
- Owner-local SCC manifest: `research/voevodsky/scc-models/crt-edge-reassembly.json`; `scc.py check voevodsky-crt-edge-reassembly` passed.
- Prior result admission: `ep_d1917165-24cc-470e-9986-e1d498732bdd`.
- Allocation: 4311, claim `seqclaim-5372fb7dcfeb6b2052bc52fc`.
- Glossary concept: `mariciconcept:9ad77a8ee3059c304ce7`, canonical name `Witness-preserving reassembly`, version 1; exact-name resolution verified with ledger and implementation provenance.
- Admission: `ep_ed69cd6a-4db0-45b2-bac7-a48d76c73492`; ledger head `ca8df3af5063c5a258b1207dd00267af3987b8b26a7c67631d0c65d0d3e5e4d0`.
- Website validation: `pnpm run build`; status reported with delivery. No Git commit or deployment is included.

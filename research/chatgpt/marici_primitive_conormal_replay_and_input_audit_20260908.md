# Primitive conormal-column test: reproducibility and instantiation status

Date: 2026-09-08

## 1. Recovered executable

The existing uploaded archive `marici_primitive_conormal_column_bundle_20260908.zip` contains the script under `check_primitive_conormal_column.py`. The script was recovered without modifying its bytes and is supplied under the exact repository filename requested by the task:

`research/chatgpt/check_marici_primitive_conormal_column_20260908.py`.

The filename in the preceding proof and the filename inside its bundle differed. The standalone file is now provided; no repository write or commit was performed.

The isolated replay starts in a newly created temporary directory containing only this standalone script. It invokes Python with `-I`, which excludes caller-local imports and user site packages. The script needs no third-party packages.

Result:

- Process exit code: 0.
- Exact assertion count: 80,087.
- Sum of the individual check-category counts: 80,087.
- Recomputed JSON: identical to the retained certificate.
- Recomputed file bytes: identical to the retained certificate.

Certificate SHA-256:

```text
a3cf610aab53828a5ac4a028b0d29719dbae3d6a48a2e55fc0571dde71105e37
```

Run from `research/chatgpt` in the supplied repository-layout bundle:

```sh
python reproduce_marici_primitive_conormal_column_20260908.py --output replay_receipt.json
```

Or run only the recovered checker:

```sh
python check_marici_primitive_conormal_column_20260908.py --output replay.json
```

The unchanged certificate explicitly reports that the complete physical endpoint source was not imported and that its covectors and control cohomology are unset. Reproducing it does not convert those fields into physical results. Its all-degree assertions still rely on the preceding mathematical proofs; the finite replay is not proof-assistant certification.

## 2. Physical-source retrieval

The accessible default branch was reported at commit `bea7339e69931b479e395d147c5f5a7fcb0dce8b`, dated 2026-09-08 13:44:46 UTC. Direct reads of each of these task-specified paths returned `404 Not Found`:

```text
research/chatgpt/marici_physical_endpoint_pullback.md
research/chatgpt/check_marici_physical_endpoint_pullback.py
research/chatgpt/marici_comparison_fibre_adjunction_bar.md
research/chatgpt/marici_physical_change_of_rings.md
```

Exact-name and content searches of the accessible repository and File Library recovered task briefs and related earlier calculations, but not the requested physical source matrices. This does not establish that the files are absent from a local working tree, another commit, or another branch. It establishes that they were not available for this computation.

The current upload is the task specification. It lists the source files but does not contain their ordered bases, differential matrices, primitive representatives, or frame maps. The 128/1024 state counts are not enough to reconstruct them.

## 3. Status of the first-jet test

Once a correctly typed free native-B source model and its frame identification are supplied, the existing compiler accepts

\[
D_0=\epsilon(D),\qquad D_{35}=\epsilon(\partial_{X_{35}}D),
\qquad \nu_0=\epsilon(\nu),\qquad\nu_{35}=\epsilon(\partial_{X_{35}}\nu).
\]

In words: take the occurrence constant and the first 35 coefficient while preserving every spectator coefficient. This extraction is not permitted on a summand whose coefficient ring inverts a short occurrence that the conductor map sends to zero. Such a summand requires its actual support functor.

The target action is

\[
[f]_{(u,v)}=
\begin{pmatrix}f_0&0\\ \beta f_{35}&f_0\end{pmatrix}.
\]

In words: the conormal module retains the full spectator coefficient and the labelled first occurrence term. This formula is exact in that module, not an approximation to its action.

For the source degree that receives the target line, the required system is

\[
\begin{pmatrix}
D_0^\top&0\\
\beta D_{35}^\top&D_0^\top\\
\nu_0^\top&0\\
\beta\nu_{35}^\top&\nu_0^\top
\end{pmatrix}
\binom{A^\top}{B^\top}
=
\begin{pmatrix}0\\0\\0\\1\end{pmatrix}.
\]

In words: the map kills incoming boundaries and sends the specified primitive to the conormal generator. The kernel-valued specialization is separately

\[
BD_0=0,\qquad B\nu_0=1.
\]

Neither physical system has been instantiated. None of the four input arrays has been inferred from the conductor resolution or from source ranks. Missing arrays are recorded as null, not zero.

No solution and no inconsistency detector are exported for the physical problem. An integral inconsistency detector requires the actual matrix. Retrieval failure is not algebraic inconsistency.

The first missing mathematical input is the supported native-linear source model and its degree/line dictionary. Once it is fixed, the first missing numerical block is the incoming differential into the degree mapped to `E_beta,35 Pi-dual[3]`, together with the primitive cocycle in the same ordered basis. If the physical primitive is itself a derived morphism, its complete Hom-complex representative and composition are needed before treating it as a column.

## 4. Variance and preserved scope

The target-side statements retained from the preceding note are:

1. The column `j35(v)=(0,v,0)` is closed and lies in the fibre of the declared projection from D35 to the complete dualizing object.
2. Right precomposition on the native conductor-domain derived Hom retains the relative-operation orbit of that column.
3. A map from the complete physical endpoint source has not been constructed by either statement.

The new task expressly prohibits turning the native-linear problem into an operation-preserving forward comparison into literal ambient `RHom_A`. That prohibition is retained as a task input. The referenced Branch C change-of-rings proof was not independently replayed here because its file and dependencies were not recovered.

An endpoint comparison into `RHom_B(B_sigma,Y_sigma)` must retain its declared adjunction and the full B-action. It cannot be replaced by direct coefficient Hom into C or by an ambient coinduced target without the comparison specified in the task. Native precomposition is not identified with contravariant postcomposition without an explicit mate.

The target conormal line, Pi-dual, regulator beta, and independent row parameter lambda retain the preceding conventions. The physical endpoint determinant, six occurrence lines, product-Cartier determinant, repeated-normal excess, long-normal frame, and polarity/orientation still require the actual source frame dictionary. No physical shift is inferred from a scalar primitive coefficient.

## 5. Deliverables

The bundle supplies the recovered standalone checker, the byte-identical retained certificate, the original target-side proof, a clean-directory replay script, the actual replay receipt, and an input-status manifest. It contains no invented endpoint basis or placeholder zero maps.

The remaining computation requires the four listed Branch C files and all imports of their endpoint checker at an accessible revision or as uploaded files. Once those are available, the task is to extract the actual four coefficient arrays and solve both systems in the declared native-linear category, then test the physical operation orbits and reflection transport.

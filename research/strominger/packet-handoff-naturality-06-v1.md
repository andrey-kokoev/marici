# Packet handoff ground naturality — iteration 6/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [contract](contracts/packet-handoff-naturality-06.v1.json) · [checker](checkers/check_packet_handoff_naturality_06.py) · [receipt](results/packet-handoff-naturality-06-v1.json).

## Question and governing test

Does the native minimum-cover atlas supply the coherence operator and the missing indexed handoff, rather than another fitted role label?

Rivals separate metric-weighted gluing from equal port-count averaging, coordinate transitions from native spin operations, and active-code equivalence from full preparation/history equivalence. The risky predictions were frozen before execution. The disposition is a **common source-bound reconstruction rule and an exact electron opposite-edge coordinate involution**, with explicit native-lift, preparation and phase obstructions. This is not a physical particle assignment.

## 1. A common source-metric gluing rule reconstructs every native return

The encoders are constructed independently of N:

* proton: actual supplied body frames and the supplied local cyclic mode;
* neutron: selected geometric numerator modes and the actual intrinsic-plane embedding;
* electron: the supplied negative Pauli normal lines, `P_f=(I-n_f.sigma)/2`.

The local mode, spin representation and sign choice remain source inputs; geometry alone is not claimed to select them. N is used only for the subsequent comparison. Choosing a basis of the resulting return module is a coordinate choice, not a preferred physical port.

Let K encode that source return module in its geometric coefficient fibers. For each minimum faithful cover p, define

    E_p = R_p K,
    S_p = E_p* E_p,
    D_p = S_p^(-1) E_p*.

Here R_p retains its actual geometric ports and `D_p E_p=I`. Set

    S_total = sum_p S_p,
    W_p = S_total^(-1) S_p,
    D_glue = sum_p W_p D_p R_p.

Every primitive face occurs with the same multiplicity m in its cover family, so

    S_total = m K* K,
    D_glue = (K* K)^(-1) K*.

Transport this decoder back through the exact native coefficient embedding. **K D_glue equals the native N on all raw inputs for all three sources.** The same formula is used without a particle-dependent rule; the supplied encoders, metrics and primitive ports differ.

Uniform singleton averaging also reproduces the proton return. It **fails for neutron**, with an exact nonzero matrix residual: the source metric gives unequal geometric mode weights. This rules out replacing the native metric by a port count. Active-return ranks remain 1/1/2; this construction does not identify either baryon's full rank-three capacity-M space with its active line.

## 2. Six actual electron edge-associated charts

Use precise types:

* logical M is the native complex doublet;
* `C_full = direct_sum_f Image(P_f)` has complex dimension 4 inside the eight raw coordinates;
* for a face pair p={f,g}, `C_p=Image(P_f) direct_sum Image(P_g)` has complex dimension 2 inside four pair coordinates.

The two faces share an actual tetrahedral edge. E_p is an isomorphism onto C_p, not onto unrestricted complex four-space. For every pair,

    S_p = P_f + P_g,
    tr(S_p)=2,       det(S_p)=2/3,
    S_p^(-1) = (3/2)(2I-S_p).

The six inverses recover the entire coherent doublet, including phase/sign. Their transported logical metrics are

    H_p = D_p* D_p,
    E_p* H_p E_p = I.

H_p is positive on C_p, not positive definite on the unused ambient complement. The original complete face field has norm squared `2 z*z`; multiply H_p by 2 when comparing that native field norm. Raw Euclidean pair restrictions are **not** isometries.

The coordinate changes

    T_(q,p) = E_q D_p

satisfy all 216 cocycles, with `T_(p,p)=identity_on_C_p`, and preserve the transported H metrics. All 216 cocycles also pass after independent nonmonomial chart-frame changes. Every one of the 144 native spin/face action squares and all 576 group multiplication/base-action comparisons pass. Central `-I` fixes every geometric pair mark but negates every chart field: the chart atlas does not erase spin sign.

## 3. Native electron coherence is the symmetric average of the six local inverses

A stronger all-input identity holds at the tetrahedral source:

    (1/6) sum_p D_p R_p = (1/2) K*,
    G = N = K ((1/6) sum_p D_p R_p).

Thus the actual four-face coherence map is recovered by **averaging the six faithful pair reconstructions**, not by selecting a preferred pair. Moreover, the exact equivariant Hom space from the full native C_full representation to the logical doublet has dimension 1 under all 24 supplied operations. Normalizing it as a left inverse to the native code fixes the scalar. This uniqueness is for this full native module and operation set, not for enlarged sources or indexed handoff laws.

A single pair inverse does not replace G on the full preparation task. For each pair, a nonzero allowed face input supported on an omitted face has zero pair restriction but nonzero native decoded/global field. The difference between pair and global decoders has rank 2 on C_full. All six explicit witnesses are retained.

## 4. A natural opposite-edge involution—and its exact limitation

The actual geometric group acts transitively on the six pair charts. Its only equivariant self-maps are:

1. identity;
2. complement p -> p-complement, the opposite edge.

Hence **requiring a nonidentity chart successor** would select the complement uniquely. With a marked incoming chart this gives a conditional realization

    M -> C_p -> C_(p-complement),

which retains the entire active doublet and has coordinate period 2. No preferred incoming chart is chosen. C_p is the derived edge chart, not the full native four-channel C preparation space. Neither the requirement to change charts nor this index is selected by the native stage commands or given physical-time meaning.

For comparison, the actual baryon singleton-chart source actions admit 12 proton and 524880 neutron equivariant bijective successors. Those counts follow from the actual regular-orbit decompositions, not enumeration of fitted labels. Symmetry alone does not select their next ports.

The electron complement also cannot be lifted to a **conjugation-equivariantly chosen native spin operation**. At a marked edge the native stabilizer is order 4. Its noncentral generator squares to `-I`, despite fixing the unordered pair mark. There are four native spin operations moving that edge to its opposite; the stabilizer conjugates every one to its negative. None is a stabilizer-fixed choice. A flat code-coordinate transition can therefore exist where a canonical native spin-word selection cannot.

Even a phase-blind state-dependent edge selector fails at the face-polarized density matrices: an actual order-three face stabilizer fixes the density but fixes no pair chart. Additional selection data would have to be stated, not inferred from the density.

## 5. Chart data still do not select the primitive indexed event

All L/G/N operations fix the active code and therefore every chart value, for all three sources. The same complete chart family can belong to distinct valid marked primitive phases 0 and 2, with different enabled commands L and N. Keeping all six charts does not recover this missing phase/history mark. The iteration3 three-phase schedule obstruction is not removed by a coordinate period-two complement.

**Iteration7 executable frontier:** `source-native-line-transport-versus-flat-code-atlas`. Compute actual face-line projection transports and exact loop phases; compare the proton local cyclic-polarization lines with the electron symmetric-square bridge and the neutron selected mode lines. Test supplied body transport, projection-induced line transport and flat faithful code-coordinate transitions separately. The needed source projectors, native words, metrics and geometric incidences exist. A derived projection transport must not be promoted to a primitive operation, and a coordinate cocycle must not be used to cancel a native coherent spin sign.

## Verification

**25 exact check groups pass**, including retained nonzero/failure witnesses. The same-checker frozen challenge passes at `8326d3748541104bbc785f5824dbe44ae79237b552886dabafdcb8ac6f987d51`. This is bounded executable validation, not independent review or proof-assistant certification.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-06-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

No native producer entrypoint, other-owner fixture edit, proof-assistant run, commit, push, publication or deployment is performed. The common physical M/C grading and source-selected indexed handoff remain open.

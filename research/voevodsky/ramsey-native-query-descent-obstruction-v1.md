# A fixed-length native cache collision prevents color-query descent

## Frozen proposition and result

For the declared native word compiler, consider the candidate claim that the required lattice color query can be recovered from its complete endpoint and cached model, plus fixed task data and total event count, without the ordered trace.

That specific claim is false. Two length-two words give the same projected native state and the same seven-event count but require different colors. This strengthens the earlier syntax-only erasure examples into an obstruction for the actual word-to-lattice query used in the Ramsey reduction.

Verification level: a written finite factorization argument, fresh actual native packet replay, and independent Python decoding and arithmetic. No proof-assistant theorem or blanket native-forcing no-go is claimed.

## Fixed task and candidate histories

Keep the same codebook and task throughout:

- Alphabet: s0,s1,s2.
- Pattern: s0=(0,0,0), s1=(1,1,0), s2=(1,0,1), a triangular subset of the original tetrahedral template.
- Colored region: the complete even-sum lattice box L_2.
- Colors: kappa(v)=v_y mod 2.
- Word length: two.

The native code uses zero-bit PN/inverse-PN loops and one-bit P reader advances. Compare

$$
w_A=(0,2)\quad\text{with bits }0010,
\qquad
w_B=(1,0)\quad\text{with bits }0100.
$$

Both have one reader advance and three zero loops: seven selected native events. In the first history, the phase-zero loop is repeated before advancing; in the second, the phase-one loop is repeated after advancing. First visits to the relevant contexts agree. Repeated cached zero loops return the entire packet without changing the source cache. The two histories therefore have equal complete native endpoints and cached model data. The checker compares the actual canonical data, not only a hash or geometric position.

Nevertheless the required word-sum queries are

$$
\Phi(w_A)=s_0+s_2=(1,0,1),\qquad\kappa(\Phi(w_A))=0,
$$

$$
\Phi(w_B)=s_1+s_0=(1,1,0),\qquad\kappa(\Phi(w_B))=1.
$$

Both points lie in the same completely supplied region. The codebook, pattern, coloring, word length and total selected event count agree. Those fields cannot explain away the collision.

## Why no readout can descend through this projection

Let P forget the ordered history while retaining the stated native state and task data, and let Q be the required color query. The two checked histories satisfy P(hA)=P(hB) but Q(hA)!=Q(hB). If a function f with Q=f after P existed, their query values would have to agree. Contradiction.

Thus this particular forgetting projection cannot implement the color query, regardless of how clever the downstream algorithm is. Full trace decoding recovers the different words and gives the correct queries, but that decoder/readout remains an explicit host-side adapter in the current implementation.

This does **not** prove that full word history is the minimal necessary addition: a suitable retained task-specific selection mark might suffice. It also does not exclude a different native word code, a native history-bearing package or an independently admitted comparison/control operation. The original native-forcing proposition already asks to retain the needed histories and is not refuted by failure of this coarser rival.

## Evidence

- Scope and fixed test: `research/voevodsky/contracts/ramsey-native-query-descent-attempt.v1.json`.
- Checker: `research/voevodsky/checkers/check_ramsey_native_query_descent.py`.
- Receipt: `research/voevodsky/results/ramsey-native-query-descent-v1.json`.
- Reused actual-native encoder and replayer: `research/voevodsky/ramsey-native-word-trace.mjs`.
- Independent decoder: the separate Python decoder in `check_ramsey_native_word_trace.py`.

The actual traces are freshly generated and checked by the source's packet/phase rules. Reused source hashes are integrity/provenance inputs, not an imported scientific proof outcome. All production source files remain unchanged.

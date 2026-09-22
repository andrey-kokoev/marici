# History and possibility swap under coherent cut reversal

## Contract

A finite language L of equal-length words declares complete admitted source developments. A cut at position k has the joint relation

    R_k(L) = {(w[:k], w[k:]) : w in L}.

Its history and continuation projections retain their joint compatibility relation. Every word is one possible complete development; no independent sampling of the two projections is allowed.

## Cut transport and reversal

Moving a cut from k to j transports (h,ef) to (he,f), with |e|=j-k. This is a bijection of joint cut relations: concatenation reconstructs the original word and splitting at k gives the inverse. Successive transports compose strictly.

Define the opposite language by reversing every word. The map

    D(h,f) = (reverse(f),reverse(h))

is an involution from R_k(L) to R_(n-k)(reverse(L)). It exchanges history and continuation. If M_(k,j) moves the original cut forward, then

    M_(n-j,n-k) D M_(k,j) = D.

Thus logical reversal reverses the direction of cut transport. The equality is a strict coherence witness; a nontrivial homotopy theory is not constructed here.

For a fixed history h and next symbol e, removing e from its compatible continuation sector gives exactly the continuation fiber at he. This verifies the proposed sector transport T(h)_e -> T(he). The full T(h) can branch; selecting e restricts to its sector.

## Exhaustive test and adversaries

The checker exhausts all 255 nonempty binary languages of length three and checks 20,480 cut-composition instances, reconstruction, involution, transport reversal and sector correspondence.

For L={000,011,101}, the cut at one has three joint pairs. Its Cartesian marginals give six pairs, including (1,11), whose reconstructed word 111 is absent from L. Marginal retention loses source compatibility.

The opposite language is {000,110,101}. Word reversal therefore supplies a dual description but is not a symmetry preserving this original language. The tested self-duality is specifically literal word reversal with fixed symbols; other possible equivalences are not excluded.

At the terminal cut all remaining continuations are empty, while the joint relation still contains three histories. Forgetting history loses the invertibility available on joint pairs.

## Interpretation and boundary

The tests support a precise finite construction: history and possibility exchange under logical orientation reversal, and their joint source relation is preserved through coherent cut movement. These identities also follow directly from word splitting and concatenation; exhaustive tests are regression evidence.

Invertibility here concerns factorizations of complete words. It supplies no physical inverse operation and no algorithm that knows an unobserved next event. A live history extension selects a compatible sector, which must be justified by the model's admission mechanism.

The owning assembled observer has not yet been equipped with these word-language cuts. Its noncommutative source products, retained marks, calibration and quotient relations would need explicit reversal maps before transferring this result. No minimum tact or physical time scale is inferred.

## Reproduction

    python research/voevodsky/checkers/check_history_possibility_cut_duality.py

Artifact: `results/history-possibility-cut-duality.json`.

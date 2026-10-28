# Falsification: a fixed four-record relabelling codec cannot realize the five-slot grammar

## Freeze the tested claim

The earlier existential conjecture did not specify an encoding or the type of wire contents. It cannot honestly be reported falsified merely because one guessed encoding fails.

This test freezes a concrete strengthening **before testing**:

1. The four signed records carry four independent complex values.
2. Native wire operations relabel those records without mixing their values, so their coefficient actions are four-by-four permutation matrices.
3. Each geometric endpoint has one injective complex-linear encoding into the five-slot packet, independent of the path taken. Histories may remain separate records but do not change this amplitude encoding.
4. Both native paths below are required to intertwine through that encoding.

**This strengthening is falsified.** The broader history-dependent conjecture is not.

## Fresh native counterexample

Starting from the same live `GenerativeAssemblyRules` seed, replay:

```
A: reader advance, reader advance, reader advance
B: PN, N reader advance, inverse-PN, P reader advance,
   PN, N reader advance, inverse-PN
```

Every operation is obtained from the current native outgoing-operation list and validated with its actual geometric/occurrence witness. No inverse NE or invented comparison move is used.

Both paths end at the same primitive, aliases, species, absolute origin 3 and occurrence frame. Their full coefficient permutations are

```
A = [2,3,0,1,4]
B = [3,4,2,0,1].
```

Their relative row permutation is

```
H = B A^-1 = [1,4,0,2,3],
```

a five-cycle. The histories are different and are retained in the receipt. Sharing this endpoint does not prove equality of the full assemblies built along the paths.

## Exact rejection of every fixed linear encoding in the tested class

If E is the endpoint encoding and S the relative permutation of the four source records, intertwining both paths requires

```
H E = E S.
```

Every four-record permutation has order m in `{1,2,3,4}`. Therefore `H^m E=E`. Since m is coprime to five, `H^m` is still a five-cycle, whose fixed vectors in C^5 are precisely the constant vectors.

Hence every column of E must be constant:

```
rank(E) <= 1,
```

contradicting the required rank four. This rejects **all** encodings in this class, not just the current contrast basis.

The executable check exhausts all 24 choices of S. The equations are entry equalities `E[H[i],j]=E[i,S[j]]`. An exact union-find calculation solves those constraints and verifies that every row of E must equal its first row. There is no floating rank tolerance and no assumption that arbitrary words in the five-slot permutations are native operations.

## Controls: what the counterexample does not prove

### Four-dimensional admissible subspaces can exist

The subspace `sum(v_i)=0` is invariant under every five-slot permutation. Encoding

```
E0(x)=(x0,x1,x2,x3,-x0-x1-x2-x3)
```

is injective and preserves four independent complex parameters. Its induced action for the displayed H is

```
(x0,x1,x2,x3) -> (x1,-x0-x1-x2-x3,x0,x2).
```

This has order five but mixes values instead of permuting four records. The checker verifies the exact intertwiner and order. Thus a bare five-versus-four dimension argument would be wrong once admissible states are restricted.

### A history-dependent encoding evades the obstruction

Choose any rank-four initial encoding, for example `(x0,x1,x2,x3,0)`, and define `E_h=Pi_h E0` using the retained path permutation. It absorbs the coefficient transport while leaving decoded source contents unchanged. The two endpoint encodings differ despite equal geometric endpoints. The checker verifies this escape explicitly.

This is not a source-derived signed-pair binding or a proposed routing law. It shows why our earlier replay results cannot falsify the broad claim: a freely adjustable history-dependent chart can satisfy such transport equations by construction.

## Consequence

The fixed, endpoint-only interpretation is dead under the stated four-record relabelling assumptions. A surviving proposal must explicitly choose at least one of:

- source-justified history/assembly-dependent encoding;
- a source content type other than four independent complex records;
- a source operation richer than relabelling, without inventing a forbidden content transformation;
- a justified global domain that excludes one tested path.

The operator's specification currently supplies none of these as a complete codec. It also does not assert that the four signed labels are four independent complex amplitudes. Therefore the stronger conclusion “the intended wire cannot be represented by any five-slot packet” is **not established**.

To make the original conjecture falsifiable, fix the admissible wire states, their native updates and a source-supported dependence of the encoding on retained context/history. Do not choose that dependence after seeing a failed comparison.

## Replay

```sh
node research/strominger/checkers/falsify_fixed_signed_pair_codec.mjs --record
```

Receipt: `results/fixed-signed-pair-codec-falsification-v1/verification.json`. It retains both live native histories, all 24 exact solution classifications, the two escape controls, source hashes and `broadExistentialConjectureFalsified: false`.

No packet model, native rule, global routing or viewer was changed by this test.

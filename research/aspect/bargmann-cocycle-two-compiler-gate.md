# Two compilers for the Bargmann orientation cocycle

The oriented triple witness has two exact finite realizations.

For three pure probe projectors P_i, P_j, P_k, the one-copy ordered projector
loop gives

    trace(P_i P_j P_k)
      = inner(i,j) inner(j,k) inner(k,i).

The signal branch of a phase-referenced interferometer may implement this
ordered nonunitary filter chain while a calibrated reference branch supplies
the comparison amplitude. Every rejected component and loss port must be
retained in the enlarged instrument record. Postselection alone does not
preserve the complex amplitude.

The three-copy realization prepares

    P_i tensor P_j tensor P_k

and coherently compares the identity with the left cyclic permutation V_3.
The cyclic-shift identity gives

    trace(V_3 (P_i tensor P_j tensor P_k))
      = trace(P_i P_j P_k).

In a whole-copy swap library, V_3 needs exactly two transpositions. This count
does not imply physical depth two or authorize controlled swaps.

The two compilers have different failure modes:

- the projector loop is sensitive to unmatched branch attenuation,
  environmental omission, and filter-order errors;
- the cyclic shift is sensitive to copy distinguishability, shared-control
  faults, and unauthorized controlled permutations.

Their agreement is therefore a useful cross-compiler gate. Reversing the
projector order or cyclic direction must conjugate the result. Dephasing the
control or destroying reference coherence must erase both quadratures.

Three pairwise overlap measurements cannot substitute for either compiler.
Their product is the squared magnitude of the Bargmann invariant and discards
its orientation phase.

The existing Aspect triad-phase associator packet already requires a
three-photon cyclic-permutation scan for exactly this arity reason. The present
packet specializes that constructor target to probe-frame orientation. It does
not claim that either compiler has been physically executed.

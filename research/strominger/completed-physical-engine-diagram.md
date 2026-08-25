# Exact source-derived completed physical engine diagram

## Typed pipeline

```text
labelled hard records and finite source jets
                 S_P^fin
                    |
          conservation restriction
                    v
               ker(C_P)  <---- antipodal matching Graph(A)
                    |
          invariant Green constructor (injective locally)
                    v
       H_P^fin,+  (+)  H_P^fin,-
          |                    |
          +---- joint (E,M) ---+          joint rank: full
                    |
             magnetic Pi_M                  kernel: Q=+1
                    v
          finite magnetic point jets
                    |
        grade-three symbol p^4-q^4          kernel: 0
                    v
   Y_local = principal parts + delta jets + background
             |                         |
       local coefficient ports         | Green/curl reconstruction
       (support-faithful)               v
                                  A_P / exact gauge
                                         |
                                  complete periods
                                         v
                                  H^1(S^2-P)
                               dimension |P|-1
```

Collision specialization is an additional source-side arrow:

```text
labelled cluster packets --moment map V_L--> collision jet packet
          kernel = null(V_L)                 |
                                                +--> grade-three (injective)
```

## Exactness and losses

The faithful arrows are:

- invariant Green construction on the admitted finite labelled packet;
- spin-two chart gluing;
- triangular Lah source-jet transport;
- joint electric-magnetic readout;
- grade-three transport on the magnetic finite-jet sector;
- direct sum over distinct puncture supports;
- either boundary projection after restriction to the antipodal graph;
- the complete period basis on `H1`.

The nonfaithful arrows are:

- `Pi_M`, with kernel the electric eigenspace;
- exact collision or insufficient moment resolution, with kernel `null(V_L)`;
- quotient by exact one-forms;
- local-to-period projection, which forgets higher principal parts and delta
  derivatives;
- selection of fewer than `|P|-1` independent periods;
- Green/spin reconstruction before declaring constant and `l<=1` zero modes.

Conservation is a restriction, not an alias. Antipodal matching is the graph
of an invertible adapter, not a sum projection. Chart boundaries are repaired
by the atlas and are not invariant rank loss.

## Commuting squares

Source differentiation commutes with the observation readout:

\[
\begin{CD}
 \mathcal H_P^J @>{\mathfrak M_3}>> \mathcal Y_P^{J+4}\\
 @V{\partial_\xi^r\partial_{\bar\xi}^s}VV
 @VV{\partial_\xi^r\partial_{\bar\xi}^s}V\\
 \mathcal H_P^{J+r+s} @>>{\mathfrak M_3}>
 \mathcal Y_P^{J+r+s+4}.
\end{CD}
\]

Parity transport commutes with the magnetic projector and grade-three density
up to the magnetic sign character. Partial Laurent charts commute with the
readout only after the coherent remainder port is included.

## Kernel formula

Before collision and target quotient,

\[
 \ker\mathfrak M_3=\mathcal H_{Q=+1}.
\]

For collision clusters `alpha` with moment matrices `V_alpha`, followed by a
period-only instrument `I`, the total loss is layered rather than one direct
sum in arbitrary coordinates:

\[
 \text{electric projection aliases}
 \;\leadsto\;
 \bigoplus_\alpha\ker V_\alpha
 \;\leadsto\;
 \text{exact/higher-jet quotient}
 \;\leadsto\;
 \ker I|_{H^1}.
\]

Each witness is attached to its first nonfaithful arrow.

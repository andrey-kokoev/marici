# Source-dynamics channel-selection no-go: WP1180

## Question

Can source dynamics select one channel from the conditional dilation fiber?

## DPC resolution

- **Conjecture:** WP857 source dynamics selects one portal-to-sector channel.
- **Rivals:** stationary semigroup composition; transient portal interface;
  sector jump operators; threshold intertwiner.
- **Risky consequences:** the stationary map is
  \(E_\infty(X)=\operatorname{Tr}(X)P_{\rm dark}\), so every dark-fixing
  channel composes to \(\operatorname{Tr}(X)\rho_{\rm dim}\), independent of
  the channel parameter.
- **Falsification attempt:** WP1179's epsilon-zero and \(1/100\) channels
  coincide after stationary source dynamics; no sector output operators or
  intertwiner are sourced.
- **Residual:** a finite-time portal-to-sector interface could still select a
  channel.
- **Disposition:** reject stationary source-dynamics channel selection.

Checker:
`research/flavor/checkers/wp1180_source_dynamics_channel_selection_no_go.py`

Result:
`results/wp1180_source_dynamics_channel_selection_no_go.json`

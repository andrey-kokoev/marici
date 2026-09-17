# qRB microstep 73: uniform Douglas-margin gate

For the spectrally adapted packets `P_n`, define the common-edge margin

$$
\eta_n
=
\min\left\{
\lambda_{\min}(P_nG^TP_n-D_{n,+}),
\lambda_{\min}(P_nG^0P_n-D_{n,-})
\right\}.
$$

Finite Douglas domination holds when `eta_n` is nonnegative. A packet-independent coercive common edge would require

$$
\inf_n\eta_n>0.
$$

The finite fixture has `eta=1`. No inference about the global infimum is valid from that one value. If the infimum is zero, a closed positive common edge may still exist, but coercivity is lost and the completion must use a form topology.

Status: uniform margin criterion isolated; global margin behavior is untested.

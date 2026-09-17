# qRB microstep 31: finite-span diagonal extension

The diagonal construction is stated on enumerated pairs, but it automatically extends to the finite complex-linear span of the countable observer core.

For

$$
 u=\sum_{i=1}^m a_i g_i,
 \qquad
 v=\sum_{j=1}^n b_j g_j,
$$

sesquilinearity gives

$$
T_k(u,v)=\sum_{i,j}a_i\overline{b_j}T_k(g_i,g_j).
$$

Since every finite set of pairs is eventually included in the diagonal schedule,

$$
T_k(u,v)\to
\sum_{i,j}a_i\overline{b_j}W_S(g_i*g_j^*).
$$

Thus the limiting signed observer is well-defined on `E_count`, independent of how a vector is represented, provided the source form is sesquilinear.

This is stronger than pairwise notation but still weaker than continuity on a completed graph domain. The next gate is a common seminorm bound or closability estimate.

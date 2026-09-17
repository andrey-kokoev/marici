# The spectral gap encloses the dangerous eigenvector

Let `F` be the certified rank-1000 finite matrix and `F0` its midpoint. If
`||F-F0||<=epsilon` and the first midpoint eigenvalue is separated from the
rest by `gap`, Davis--Kahan gives

\[
\sin\angle(v_1,v_{1,0})\le\frac{\epsilon}{gap-\epsilon}.
\]

The modified-gamma Bernstein entry budget is `3.22544e-13`. At rank 1000 it
gives the conservative matrix norm error `epsilon<=3.22544e-10`; Arb node and
prime/endpoint radii are negligible. The first gap is approximately
`6.97886e-6`, so the angular error is below `4.63e-5`.

For the finite cross block from modes below 1000 to modes 1000--1999, whose
scouted norm is at most the full `0.27086` cross norm, replacing the exact
first eigenvector by its midpoint representative changes the residual by at
most about `1.26e-5`. This remains below the first residual reserve after the
observed finite residual is included.

Thus an interval certificate need not enclose 1000 eigenvector coordinates
independently. It suffices to certify the finite matrix norm error, the first
spectral gap, and the cross-block norm.

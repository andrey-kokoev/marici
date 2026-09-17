# qRB microstep 35: finite versus completed bounds

On every finite observer packet, the relative readout is automatically bounded: if `G` is the finite Gram matrix of the chosen comparison norm, then

$$
|T(u,v)|
\le
\|G^{-1/2}TG^{-1/2}\|\,\|u\|_G\,\|v\|_G.
$$

This proves only a finite-stage estimate. The completion question requires a bound whose constant remains controlled as the packet and regulators grow.

Therefore finite positive certificates cannot be promoted to a completed relative observer without a uniform or closability argument.

Status: finite-stage boundedness discharged as linear algebra; uniform completed bound remains open.

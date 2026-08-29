# Physical-promotion and spacelike-evidence gate

The digest-bound receipt proves identity of a packet and its compiled views. It does not prove that the packet came from hardware or that relevant operations were spacelike separated. This gate keeps those authorities distinct.

Promotion to physical evidence requires all of the following:

- packet status is `physical_raw`;
- acquisition-service identity and signed run manifest are present;
- detector calibration and clock-synchronization authorities are independently identified;
- coincidence policy was fixed before Bell analysis;
- the digest-bound pushforward receipt passes;
- each preregistered cross-wing interval has positive spacelike margin after worst-case timing and position uncertainty;
- the packet contains no synthetic or ideal-mean fields.

For spatial separation `d`, coordinate-time difference `dt`, aggregate timing uncertainty `u_t`, aggregate position uncertainty `u_x`, and light speed `c`, the conservative margin is

`d - u_x - c (abs(dt) + u_t)`.

Every required interval must exceed the preregistered margin. These calculations are necessary but do not create calibration authority; the authority fields must refer to independent durable records.

The present synthetic packet is supposed to fail promotion. The checker also exercises a geometry-only calculation fixture to verify the interval arithmetic, while refusing to treat it as physical evidence.

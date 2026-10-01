"""Conditional driven emission into the normalized broadband photon packet.

Interaction picture: V_I(t)=g(t)(zeta*sigma_- A_psi^dagger+h.c.). Its exact
single-excitation rotation is used. Schrödinger coupling must include
exp[-i(omega-Omega)t]; this is supplied mode-matched drive, not an autonomous
single-frequency source or a derived local electromagnetic interaction.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import count

from photon_maxwell_adapter import Q, ZERO, ONE, I, mv, transpose
from photon_momentum_wavepacket import MomentumPacketLedger, MomentumPacket


def dagger(matrix):
    return tuple(tuple(x.conjugate() for x in row) for row in transpose(matrix))


def norm(vector):
    return sum((x.conjugate() * x for x in vector), ZERO)


def expectation(vector, matrix):
    return sum((a.conjugate() * b for a, b in zip(vector, mv(matrix, vector))), ZERO)


@dataclass(frozen=True)
class AffineFrequencyPhase:
    # Represents exp(i*(omega_coefficient*omega+constant)), not a rounded value.
    omega_coefficient: F
    constant: F

    def __post_init__(self):
        for name in ('omega_coefficient', 'constant'):
            value = getattr(self, name)
            if not isinstance(value, (int, F)):
                raise ValueError('Exact rational phase data required')
            object.__setattr__(self, name, F(value))

    def times(self, other):
        return AffineFrequencyPhase(self.omega_coefficient + other.omega_coefficient,
                                    self.constant + other.constant)

    def conjugate(self):
        return AffineFrequencyPhase(-self.omega_coefficient, -self.constant)


def free_operator_phase(time, gap):
    # e^{i H0 t} sigma_- a^dagger(k) e^{-i H0 t}
    return AffineFrequencyPhase(time, -gap * time)


def matching_drive_phase(time, gap):
    return free_operator_phase(time, gap).conjugate()


@dataclass(frozen=True)
class MatchedPulse:
    cosine: Q
    sine: Q
    coupling_phase: Q = ONE

    def __post_init__(self):
        c, s, z = (Q.coerce(x) for x in (self.cosine, self.sine, self.coupling_phase))
        if c.conjugate() != c or s.conjugate() != s or c * c + s * s != ONE:
            raise ValueError('Real cos(theta),sin(theta) with unit norm required')
        if z.conjugate() * z != ONE:
            raise ValueError('Constant interaction phase must have unit modulus')
        object.__setattr__(self, 'cosine', c)
        object.__setattr__(self, 'sine', s)
        object.__setattr__(self, 'coupling_phase', z)

    def unitary(self):
        # Ordered basis |g,0>, |e,0>, |g,psi>; this is an exact interaction-
        # picture invariant sector for the supplied matched control, not H0.
        c, s, z = self.cosine, self.sine, self.coupling_phase
        return ((ONE, ZERO, ZERO), (ZERO, c, -I * z.conjugate() * s),
                (ZERO, -I * z * s, c))

    def kraus(self):
        # Source basis (g,e), conditioned on field vacuum / one packet.
        c, s, z = self.cosine, self.sine, self.coupling_phase
        return (((ONE, ZERO), (ZERO, c)), ((ZERO, -I * z * s), (ZERO, ZERO)))


@dataclass(frozen=True)
class EmissionRecord:
    label: str
    packet: MomentumPacket
    gap: F
    duration: F
    pulse: MatchedPulse
    source_input: tuple
    joint_output: tuple


@dataclass(frozen=True)
class HeraldedPacket:
    emission: EmissionRecord
    profile_parent: MomentumPacket
    schrodinger_free_phase: AffineFrequencyPhase


class PhotonEmissionLedger:
    def __init__(self, packets):
        if not isinstance(packets, MomentumPacketLedger):
            raise ValueError('A retained normalized continuum packet ledger is required')
        self.packets = packets
        self._serial = count()
        self._records = {}

    def emit(self, packet, pulse, gap=F(1), duration=F(1), source_input=(ZERO, ONE)):
        packet = self.packets.resolve(packet)
        if not isinstance(pulse, MatchedPulse):
            raise ValueError('An explicit matched pulse is required')
        if (not isinstance(gap, (int, F)) or not isinstance(duration, (int, F))
                or gap <= 0 or duration <= 0):
            raise ValueError('Positive exact source gap and control duration required')
        source_input = tuple(Q.coerce(x) for x in source_input)
        if len(source_input) != 2 or norm(source_input) != ONE:
            raise ValueError('Normalized two-level source input required')
        if self.packets.norm_squared(packet) != ONE:
            raise ValueError('The continuum field mode is not normalized')
        initial = source_input + (ZERO,)
        joint = mv(pulse.unitary(), initial)
        if norm(joint) != ONE:
            raise ValueError('Joint source-field normalization failed')
        out = EmissionRecord(f'emission:{next(self._serial)}', packet, F(gap), F(duration),
                             pulse, source_input, joint)
        self._records[out.label] = out
        return out

    def resolve(self, record):
        if not isinstance(record, EmissionRecord) or self._records.get(record.label) is not record:
            raise ValueError('Unknown, foreign or substituted emission record')
        self.packets.resolve(record.packet)
        return record

    def probabilities(self, record):
        record = self.resolve(record)
        g0, e0, g1 = record.joint_output
        return (g0.conjugate() * g0 + e0.conjugate() * e0, g1.conjugate() * g1)

    def field_density(self, record):
        record = self.resolve(record)
        a, b, d = record.joint_output
        return ((a.conjugate() * a + b.conjugate() * b, a * d.conjugate()),
                (d * a.conjugate(), d.conjugate() * d))

    def source_density(self, record):
        """Source density in the interaction picture (retain its free phase separately)."""
        record = self.resolve(record)
        a, b, d = record.joint_output
        return ((a.conjugate() * a + d.conjugate() * d, a * b.conjugate()),
                (b * a.conjugate(), b.conjugate() * b))

    def herald_packet(self, record):
        record = self.resolve(record)
        if self.probabilities(record)[1] == ZERO:
            raise ValueError('Zero-probability branch cannot define a normalized heralded packet')
        # The Schrödinger-picture outgoing amplitude at time T is
        # exp(-i*omega*T) psi(k). Never silently omit this continuum phase.
        return HeraldedPacket(record, record.packet, AffineFrequencyPhase(-record.duration, 0))

    def energy_audit(self, record):
        record = self.resolve(record)
        mean = record.packet.profile.mean_momentum()[0]
        second = record.packet.profile.diagonal_second_moments()[0]
        variance = second - mean * mean
        gap = record.gap
        excited = record.source_input[1].conjugate() * record.source_input[1]
        p = self.probabilities(record)[1]
        delta = Q(mean - gap)
        second_detuning = Q(second - 2 * gap * mean + gap * gap)
        return {'initial_free_energy': excited * gap,
                'final_free_energy': (excited - p) * gap + p * mean,
                'mean_external_work': p * delta,
                'TPM_work_second_moment': p * second_detuning,
                'TPM_work_variance': p * Q(variance) + p * (ONE - p) * delta * delta,
                'free_commutator_on_excited_vacuum_norm_squared': second_detuning,
                'packet_energy_variance': Q(variance)}

    def instantaneous_power(self, record, rate, rate_derivative=ZERO):
        # Exact expectation of the full derivative of V_S in the matched
        # interaction-picture state. Its projection suffices for expectation,
        # NOT for replacing the broadband H0 by a 3x3 Hamiltonian.
        record = self.resolve(record)
        rate, rate_derivative = Q.coerce(rate), Q.coerce(rate_derivative)
        if rate.conjugate() != rate or rate_derivative.conjugate() != rate_derivative:
            raise ValueError('Real instantaneous pulse rates required')
        z = record.pulse.coupling_phase
        delta = Q(record.packet.profile.mean_momentum()[0] - record.gap)
        off_ge = z * (rate_derivative - I * rate * delta)
        power = ((ZERO, ZERO, ZERO), (ZERO, ZERO, off_ge.conjugate()), (ZERO, off_ge, ZERO))
        return expectation(record.joint_output, power)

    def deconstruct(self, record):
        record = self.resolve(record)
        return record.packet, record.source_input, record.pulse, record.gap, record.duration

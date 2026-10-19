import numpy as np


# create the stabilizers
def create_chamon_stabs(px, py, pz):
    # the code in not css so stabilizers include both x and z...
    # note that this is for the case where the first element is a qubit
    dpy = 2 * py
    dpz = 2 * pz
    numstab = 4 * px * py * pz
    numqubits = 4 * px * py * pz
    stabs = np.zeros([numstab, 2 * numqubits])
    index = 0
    for k in range(2 * pz):
        for j in range(2 * py):
            for i in range(px):
                # adding where stabilizer applies x:
                stabs[index, index] = 1
                if ((j % 2) + ((k + 1) % 2)) % 2 == 1:  # if on row starting with qubit
                    if (i % px) == px - 1:  # if on right boundary
                        stabs[index, index - px + 1] = 1
                    else:
                        stabs[index, index + 1] = 1
                else:  # if on row starting with stabilizer
                    if i % px == 0:  # if on x left boundary
                        stabs[index, index + px - 1] = 1  # x stabilzer to x part
                    else:
                        stabs[index, index - 1] = 1  # x stabilzer to x part

                # adding where stabilizer applies y:
                if j % dpy == 0:  # if on y front boundary
                    stabs[index, index + px * dpy - px] = 1  # y stabilizer to x part
                    stabs[index, numqubits + index + px * dpy - px] = 1  # y stabilizer to z part
                else:
                    stabs[index, index - px] = 1  # y stabilizer to x part
                    stabs[index, numqubits + index - px] = 1  # y stabilizer to z part

                if j % dpy == (dpy - 1):  # if on y back boundary
                    stabs[index, index - px * dpy + px] = 1  # y stabilizer to x part
                    stabs[index, numqubits + index - px * dpy + px] = 1  # y stabilizer to z part
                else:
                    stabs[index, index + px] = 1  # y stabilizer to x part
                    stabs[index, numqubits + index + px] = 1  # y stabilizer to z part

                # adding where stabilizer applies z:
                if k % dpz == 0:  # if on z bottom boundary:
                    stabs[index, numqubits + index + px * dpy * dpz - px * dpy] = 1  # z stab to z part
                else:
                    stabs[index, numqubits + index - px * dpy] = 1  # z stab to z part
                if k % dpz == (dpz - 1):
                    stabs[index, numqubits + index - px * dpy * dpz + px * dpy] = 1  # z stab to z part
                else:
                    stabs[index, numqubits + index + px * dpy] = 1  # z stab to z part
                index += 1
    return stabs


def find_total_syndrome(noisy_qubits, numqubits, stabs):
    # just for the purpose of visualization, find all stabilizers that light up due to this noise
    total_noise = np.zeros(2 * numqubits)
    for i in range(len(noisy_qubits)):
        noisy_qubit_index = noisy_qubits[i]
        total_noise[noisy_qubit_index] = 1
    total_syndrome = np.matmul(stabs, total_noise) % 2
    return total_syndrome


def find_syndrome_from_noise_nums(noisy_qubits, numqubits, stabs):
    # just for the purpose of visualization, find all stabilizers that light up due to this noise
    total_noise = np.zeros(2 * numqubits)
    for i in range(len(noisy_qubits)):
        noisy_qubit_index = noisy_qubits[i]
        total_noise[noisy_qubit_index] = 1
    total_syndrome = np.matmul(stabs, total_noise) % 2
    return total_noise, total_syndrome
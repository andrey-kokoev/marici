def stab_2_location(stab_index, px):
    # gives the x-y-z location of a stabilizer from its index
    # note that this assumes that the bottom layer starts with a qubit..
    num_stlayer = 2 * px * px
    z = stab_index // num_stlayer
    y = (stab_index // px) % (2 * px)
    x = (stab_index % px)
    if (z % 2 == 0 and y % 2 == 0) or (z % 2 == 1 and y % 2 == 1):
        x = 2 * x + 1
    else:
        x = 2 * x
    return (x, y, z)


def qubit_2_location(qubit_index, px):
    # gives the x-y-z location of a qubit from its index
    # note that this assumes that the bottom layer starts with a qubit..

    numqubits = 4 * px * px * px
    if qubit_index >= numqubits:
        # if x error then the index will be numqubits+index, so fix that
        qubit_index -= numqubits
    num_qulayer = 2 * px * px
    z = qubit_index // num_qulayer
    y = (qubit_index // px) % (2 * px)
    x = (qubit_index % px)
    if (z % 2 == 0 and y % 2 == 0) or (z % 2 == 1 and y % 2 == 1):
        x = 2 * x
    else:
        x = 2 * x + 1
    return (x, y, z)


def list_qubits_to_loc(qubit_list, px, type, num_qubits):
    if type == 0 or type == "x":
        ql = qubit_list
    elif type == 2 or type == "z":
        ql = [x+num_qubits for x in qubit_list]
    else:
        raise Exception("type should be 0, 2, x or z")
    loc_qubits = [qubit_2_location(x, px) for x in ql]
    return loc_qubits


def neighbor_single_direction(x, px):
    x_left = x - 1
    x_right = x + 1
    if x == 2*px-1:
        x_right = 0
    if x == 0:
        x_left = 2*px-1
    return x_left, x_right


def position_2_neighbors(stab_position, px=3, py=None, pz=None):
    if py is None:
        py = px
    if pz is None:
        pz = px
    x_stab = stab_position[0]
    y_stab = stab_position[1]
    z_stab = stab_position[2]

    (x_left, x_right) = neighbor_single_direction(x_stab, px)
    (y_down, y_up) = neighbor_single_direction(y_stab, py)
    (z_down, z_up) = neighbor_single_direction(z_stab, pz)

    return (x_left, y_stab, z_stab), (x_right, y_stab, z_stab), (x_stab, y_down, z_stab), (x_stab, y_up, z_stab), (x_stab, y_stab, z_down), (x_stab, y_stab, z_up)


def loc_2_number(location, px, py=None):
    if py is None:
        py = px
    x = location[0]
    y = location[1]
    z = location[2]
    number = 2 * px * py * z + py * y + x//2
    return number

def index_2_neighbor(index, px, type):
    if type == "qubit":
        loc = qubit_2_location(index, px)
    elif type == "stab":
        loc = stab_2_location(index, px)
    else:
        raise Exception("type should be either qubit or stab")
    neighbors_loc = position_2_neighbors(loc, px)
    neighbors = list()
    for n in neighbors_loc:
        neighbors.append(loc_2_number(n, px))
    return neighbors

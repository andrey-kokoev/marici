#[derive(Clone, Copy)]
struct Master {
    name: &'static str,
    wall_a: i32,
    wall_b: i32,
    k_power_twice: i32,
    numerator_degree: i32,
}

impl Master {
    fn radial_weight(self) -> i32 {
        // da ^ db has radial degree two, each wall has degree one, and
        // K^(h/2) has degree 3h because K has degree six.
        self.numerator_degree + 2 - self.wall_a - self.wall_b - 3 * self.k_power_twice
    }
}

fn main() {
    // The normalized reducer sets X1=1 and uses
    // X2=(u+v)/2-1, X3=(u-v)/2.
    // Verify the inverse homogeneous coordinates symbolically by comparing
    // integer coefficients after clearing the common X1 denominator.
    let x1 = 7_i64;
    let x2 = 11_i64;
    let x3 = 13_i64;
    let e = x1 + x2 + x3;
    let u_num = e;
    let v_num = x1 + x2 - x3;
    assert_eq!(u_num + v_num - 2 * x1, 2 * x2);
    assert_eq!(u_num - v_num, 2 * x3);

    let masters = [
        Master { name: "Omega111", wall_a: 1, wall_b: 1, k_power_twice: 1, numerator_degree: 0 },
        Master { name: "Omega101", wall_a: 1, wall_b: 0, k_power_twice: 1, numerator_degree: 0 },
        Master { name: "Omega110", wall_a: 0, wall_b: 1, k_power_twice: 1, numerator_degree: 0 },
        Master { name: "e1", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 2 },
        Master { name: "e2", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 1 },
        Master { name: "e3", wall_a: 0, wall_b: 0, k_power_twice: 3, numerator_degree: 6 },
        Master { name: "e4", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 1 },
        Master { name: "e5", wall_a: 0, wall_b: 0, k_power_twice: 3, numerator_degree: 6 },
        Master { name: "e6", wall_a: 0, wall_b: 0, k_power_twice: 3, numerator_degree: 5 },
        Master { name: "e7", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 0 },
        Master { name: "e8", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 2 },
        Master { name: "e9", wall_a: 0, wall_b: 0, k_power_twice: 1, numerator_degree: 2 },
    ];
    let weights: Vec<_> = masters.iter().copied().map(Master::radial_weight).collect();
    assert_eq!(weights, vec![-3, -2, -2, 1, 0, -1, 0, -1, -2, -1, 1, 1]);
    for (master, weight) in masters.iter().zip(weights) {
        println!("{}: {}", master.name, weight);
    }
}

use serde_json::{json, Value};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};
use symbolica::prelude::*;

const N: usize = 7;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}

impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 {
            n = -n;
            d = -d;
        }
        let mut a = n.unsigned_abs();
        let mut b = d as u128;
        while b != 0 {
            let r = a % b;
            a = b;
            b = r;
        }
        let g = a as i128;
        Self { n: n / g, d: d / g }
    }
    fn zero() -> Self {
        Self { n: 0, d: 1 }
    }
    fn one() -> Self {
        Self { n: 1, d: 1 }
    }
    fn add(self, o: Self) -> Self {
        Self::new(self.n * o.d + o.n * self.d, self.d * o.d)
    }
    fn neg(self) -> Self {
        Self {
            n: -self.n,
            d: self.d,
        }
    }
    fn sub(self, o: Self) -> Self {
        self.add(o.neg())
    }
    fn mul(self, o: Self) -> Self {
        Self::new(self.n * o.n, self.d * o.d)
    }
    fn div(self, o: Self) -> Self {
        Self::new(self.n * o.d, self.d * o.n)
    }
    fn atom(self) -> Atom {
        a(&format!("{}/{}", self.n, self.d))
    }
}

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn replace(expression: Atom, variable: &Atom, value: &Atom) -> Atom {
    expression
        .replace(variable.to_pattern())
        .with(value.to_pattern())
        .expand()
}

fn parse_region(name: &str) -> Option<BTreeSet<usize>> {
    name.strip_prefix("g_").map(|digits| {
        digits
            .chars()
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}

fn wall_coefficients(name: &str) -> (Vec<Rat>, Vec<Rat>) {
    let mut x = vec![Rat::zero(); N];
    let mut y = vec![Rat::zero(); N];
    if let Some(region) = parse_region(name) {
        for site in &region {
            x[*site] = Rat::one();
        }
        for edge in 0..N {
            if region.contains(&edge) != region.contains(&((edge + 1) % N)) {
                y[edge] = Rat::one();
            }
        }
    } else {
        x.fill(Rat::one());
        let edge = name
            .strip_prefix("G_minus_e")
            .unwrap()
            .chars()
            .next()
            .unwrap()
            .to_digit(10)
            .unwrap() as usize
            - 1;
        y[edge] = Rat::new(2, 1);
    }
    (y, x)
}

fn region_label(region: &BTreeSet<usize>) -> String {
    format!(
        "g_{}",
        region
            .iter()
            .map(|site| (site + 1).to_string())
            .collect::<String>()
    )
}

fn frozen_support_labels() -> Vec<String> {
    let mut labels = BTreeSet::new();
    for length in 1..N {
        for start in 0..N {
            labels.insert(region_label(
                &(0..length).map(|offset| (start + offset) % N).collect(),
            ));
        }
    }
    for edge in 0..N {
        labels.insert(format!("G_minus_e{}{}", edge + 1, (edge + 1) % N + 1));
    }
    labels.into_iter().collect()
}

fn pulled_wall(name: &str, solution: &WallSolution) -> Atom {
    let (y, x) = wall_coefficients(name);
    let from_y = y
        .iter()
        .zip(solution.y.iter())
        .fold(a("0"), |sum, (coefficient, value)| {
            sum + coefficient.atom() * value.clone()
        });
    (0..N)
        .fold(from_y, |sum, site| {
            sum + x[site].atom() * a(&format!("X{}", site + 1))
        })
        .expand()
}

struct WallSolution {
    y: Vec<Atom>,
    free: Vec<usize>,
    base_relations: Vec<Atom>,
}

fn solve_walls(labels: &[String]) -> WallSolution {
    let mut matrix = labels
        .iter()
        .map(|label| {
            let (mut y, x) = wall_coefficients(label);
            y.extend(x);
            y
        })
        .collect::<Vec<_>>();
    let mut row = 0usize;
    let mut pivots = Vec::new();
    for col in 0..N {
        let Some(pivot) = (row..matrix.len()).find(|r| matrix[*r][col].n != 0) else {
            continue;
        };
        matrix.swap(row, pivot);
        let p = matrix[row][col];
        for c in col..2 * N {
            matrix[row][c] = matrix[row][c].div(p);
        }
        for target in 0..matrix.len() {
            if target == row || matrix[target][col].n == 0 {
                continue;
            }
            let scale = matrix[target][col];
            for c in col..2 * N {
                matrix[target][c] = matrix[target][c].sub(scale.mul(matrix[row][c]));
            }
        }
        pivots.push(col);
        row += 1;
    }
    let free = (0..N).filter(|c| !pivots.contains(c)).collect::<Vec<_>>();
    let mut y = (0..N).map(|i| a(&format!("t{i}"))).collect::<Vec<_>>();
    for (r, &pivot) in pivots.iter().enumerate() {
        let mut expression = a("0");
        for &f in &free {
            expression = expression - matrix[r][f].atom() * a(&format!("t{f}"));
        }
        for j in 0..N {
            expression = expression - matrix[r][N + j].atom() * a(&format!("X{}", j + 1));
        }
        y[pivot] = expression.expand();
    }
    let base_relations = (row..matrix.len())
        .filter_map(|r| {
            let expression = (0..N)
                .fold(a("0"), |sum, j| {
                    sum + matrix[r][N + j].atom() * a(&format!("X{}", j + 1))
                })
                .expand();
            (expression != a("0")).then_some(expression)
        })
        .collect();
    WallSolution {
        y,
        free,
        base_relations,
    }
}

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 {
        return matrix[0][0].clone();
    }
    (0..matrix.len())
        .fold(a("0"), |total, column| {
            let minor = matrix[1..]
                .iter()
                .map(|row| {
                    row.iter()
                        .enumerate()
                        .filter(|(i, _)| *i != column)
                        .map(|(_, v)| v.clone())
                        .collect()
                })
                .collect::<Vec<Vec<_>>>();
            let term = matrix[0][column].clone() * determinant(&minor);
            if column % 2 == 0 {
                total + term
            } else {
                total - term
            }
        })
        .expand()
}

fn adjugate(matrix: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let n = matrix.len();
    let mut result = vec![vec![a("0"); n]; n];
    for row in 0..n {
        for column in 0..n {
            let minor = matrix
                .iter()
                .enumerate()
                .filter(|(i, _)| *i != column)
                .map(|(_, source)| {
                    source
                        .iter()
                        .enumerate()
                        .filter(|(i, _)| *i != row)
                        .map(|(_, v)| v.clone())
                        .collect()
                })
                .collect::<Vec<Vec<_>>>();
            result[row][column] = if (row + column) % 2 == 0 {
                determinant(&minor)
            } else {
                -determinant(&minor)
            };
        }
    }
    result
}

fn dot_k(left: &[i32], right: &[i32], k: &Atom) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, l)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, r)| {
                let separation = i.max(j) - i.min(j);
                let distance = separation.min(7 - separation);
                let pairing = match distance {
                    0 => a("2"),
                    1 => a("3/2"),
                    2 => a("1/2"),
                    3 => k.clone(),
                    _ => unreachable!(),
                };
                inner + a(&l.to_string()) * a(&r.to_string()) * pairing
            })
        })
        .expand()
}

fn quadratic(vector: &[Atom], matrix: &[Vec<Atom>]) -> Atom {
    vector
        .iter()
        .enumerate()
        .fold(a("0"), |sum, (i, l)| {
            sum + vector.iter().enumerate().fold(a("0"), |inner, (j, r)| {
                inner + l.clone() * matrix[i][j].clone() * r.clone()
            })
        })
        .expand()
}

fn universal_cover(squares: &[Atom]) -> (Atom, Atom, Atom, Atom) {
    let k = a("k");
    let routing = [
        vec![1, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0, 0],
    ];
    let q5 = vec![1, 1, 1, 1, 1, 0, 0];
    let q6 = vec![1, 1, 1, 1, 1, 1, 0];
    let gram = routing
        .iter()
        .map(|l| routing.iter().map(|r| dot_k(l, r, &k)).collect())
        .collect::<Vec<Vec<_>>>();
    let det = determinant(&gram).factor();
    let adj = adjugate(&gram);
    let u = (0..4)
        .map(|i| {
            ((squares[0].clone() + gram[i][i].clone() - squares[i + 1].clone()) / a("2")).expand()
        })
        .collect::<Vec<_>>();
    let first = (det.clone() * squares[0].clone() - quadratic(&u, &adj)).expand();
    let extension = |q: &Vec<i32>, square: &Atom| {
        let b = routing
            .iter()
            .map(|route| dot_k(route, q, &k))
            .collect::<Vec<_>>();
        let linear = (0..4).fold(a("0"), |sum, i| {
            sum + (0..4).fold(a("0"), |inner, j| inner + adj[i][j].clone() * b[j].clone())
                * u[i].clone()
        });
        (det.clone() * (square.clone() - squares[0].clone() - dot_k(q, q, &k)) + a("2") * linear)
            .expand()
    };
    (
        first,
        extension(&q5, &squares[5]),
        extension(&q6, &squares[6]),
        det,
    )
}

fn main() {
    let partition: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-inventory-partition.json").unwrap(),
    )
    .unwrap();
    let limit = std::env::var("CLASS_LIMIT")
        .ok()
        .map(|x| x.parse::<usize>().unwrap())
        .unwrap_or(1);
    let rank = std::env::var("WALL_RANK")
        .ok()
        .map(|x| x.parse::<u64>().unwrap())
        .unwrap_or(4);
    let scope = std::env::var("SCOPE").unwrap_or_else(|_| "classes".into());
    let inventory: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-full-source-inventory.json").unwrap(),
    )
    .unwrap();
    let inventory_index = inventory["all_orbits"]
        .as_array()
        .unwrap()
        .iter()
        .map(|orbit| (orbit["canonical_key"].as_str().unwrap(), orbit))
        .collect::<BTreeMap<_, _>>();
    let mut selected = Vec::<(String, Value)>::new();
    for class in partition["classes"]
        .as_array()
        .unwrap()
        .iter()
        .filter(|c| c["wall_rank"].as_u64() == Some(rank))
    {
        if scope == "classes" {
            selected.push((
                class["class_key"].as_str().unwrap().to_string(),
                class["neutral_representative"].clone(),
            ));
        } else {
            for key in class["member_keys"].as_array().unwrap() {
                selected.push((
                    class["class_key"].as_str().unwrap().to_string(),
                    (*inventory_index[key.as_str().unwrap()]).clone(),
                ));
            }
        }
    }
    selected.sort_by(|left, right| {
        left.1["canonical_key"]
            .as_str()
            .unwrap()
            .cmp(right.1["canonical_key"].as_str().unwrap())
    });
    selected.truncate(limit);
    let mut outputs = Vec::new();
    for (class_key, orbit) in selected {
        let labels = orbit["representative"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_str().unwrap().to_string())
            .collect::<Vec<_>>();
        let solution = solve_walls(&labels);
        assert_eq!(solution.free.len(), N - rank as usize);
        let squares = solution
            .y
            .iter()
            .map(|v| (v.clone() * v.clone()).expand())
            .collect::<Vec<_>>();
        let (f, g, h, gram) = universal_cover(&squares);
        let equations = [f, g, h];
        let variables = solution
            .free
            .iter()
            .map(|i| Symbol::parse(format!("t{i}"), "marici").unwrap())
            .collect::<Vec<_>>();
        let jacobian = equations
            .iter()
            .map(|eq| {
                variables
                    .iter()
                    .map(|v| eq.derivative(*v).expand())
                    .collect()
            })
            .collect::<Vec<Vec<_>>>();
        let maximal_minors = match variables.len() {
            3 => vec![determinant(&jacobian).factor()],
            2 => vec![
                determinant(&[jacobian[0].clone(), jacobian[1].clone()]).factor(),
                determinant(&[jacobian[0].clone(), jacobian[2].clone()]).factor(),
                determinant(&[jacobian[1].clone(), jacobian[2].clone()]).factor(),
            ],
            1 => jacobian.iter().map(|row| row[0].clone().factor()).collect(),
            _ => unreachable!(),
        };
        let projective_multiplier = if variables.len() == 3 {
            adjugate(&jacobian)
                .into_iter()
                .enumerate()
                .find(|(_, row)| row.iter().any(|entry| entry != &a("0")))
                .map(|(source_row, row)| {
                    json!({
                        "source_row":source_row,
                        "ordered_cover_rows":["F1","F6","F7"],
                        "left_multiplier":row.iter().map(|entry|entry.factor().to_string()).collect::<Vec<_>>(),
                        "identity":format!("lambda*J=det(J)*e_{}",source_row+1),
                        "discriminant_restriction":"lambda*J=0"
                    })
                })
        } else {
            None
        };
        let polynomial_variables = (1..=N)
            .map(|i| Symbol::parse(format!("X{i}"), "marici").unwrap())
            .chain(std::iter::once(Symbol::parse("k", "marici").unwrap()))
            .chain((0..N).map(|i| Symbol::parse(format!("t{i}"), "marici").unwrap()))
            .collect::<Vec<_>>();
        let mut common = maximal_minors
            .iter()
            .filter(|minor| *minor != &a("0"))
            .map(|minor| minor.to_polynomial::<_, u16>(&Q, polynomial_variables.clone()))
            .reduce(|left, right| left.gcd(&right))
            .unwrap();
        let common_expression = common.to_expression().factor();
        let gram_soft_factors = solution
            .free
            .iter()
            .map(|i| a(&format!("t{i}")))
            .chain([a("k"), a("6+7*k")])
            .collect::<Vec<_>>();
        for factor in &gram_soft_factors {
            let polynomial = factor.to_polynomial::<_, u16>(&Q, polynomial_variables.clone());
            loop {
                let (quotient, remainder) = common.quot_rem(&polynomial, false);
                if !remainder.is_zero() {
                    break;
                }
                common = quotient;
            }
        }
        let residual_common = common.to_expression().factor();
        let mut fully_saturated = common.clone();
        let declared_support_factors = solution
            .y
            .iter()
            .cloned()
            .chain(
                frozen_support_labels()
                    .iter()
                    .map(|label| pulled_wall(label, &solution)),
            )
            .filter(|factor| factor != &a("0"))
            .collect::<Vec<_>>();
        let mut removed_support_factors = Vec::new();
        for factor in declared_support_factors {
            let polynomial = factor.to_polynomial::<_, u16>(&Q, polynomial_variables.clone());
            if polynomial.is_constant() {
                continue;
            }
            let mut multiplicity = 0usize;
            loop {
                let (quotient, remainder) = fully_saturated.quot_rem(&polynomial, false);
                if !remainder.is_zero() {
                    break;
                }
                fully_saturated = quotient;
                multiplicity += 1;
            }
            if multiplicity > 0 {
                removed_support_factors.push(json!({
                    "factor":factor.factor().to_string(),
                    "multiplicity":multiplicity
                }));
            }
        }
        let fully_saturated_expression = fully_saturated.to_expression().factor();
        let gram_specializations = [a("0"), a("-6/7")]
            .iter()
            .map(|value| {
                let specialized = equations
                    .iter()
                    .map(|equation| replace(equation.clone(), &a("k"), value))
                    .filter(|equation| equation != &a("0"))
                    .map(|equation| {
                        equation.to_polynomial::<_, u16>(&Q, polynomial_variables.clone())
                    })
                    .collect::<Vec<_>>();
                let ideal_gcd = specialized
                    .iter()
                    .cloned()
                    .reduce(|left, right| left.gcd(&right))
                    .unwrap();
                let principal = specialized.iter().any(|polynomial| {
                    let (quotient, remainder) = polynomial.quot_rem(&ideal_gcd, false);
                    remainder.is_zero() && quotient.is_constant()
                });
                let singular_gcd = (0..polynomial_variables.len())
                    .map(|variable| ideal_gcd.derivative(variable))
                    .filter(|derivative| !derivative.is_zero())
                    .fold(ideal_gcd.clone(), |current, derivative| {
                        current.gcd(&derivative)
                    });
                json!({
                    "k":value.to_string(),
                    "ideal_gcd":ideal_gcd.to_expression().factor().to_string(),
                    "principal_ideal":principal,
                    "reduced_cartier":principal && singular_gcd.is_constant(),
                    "cartier_length":if principal && singular_gcd.is_constant(){1}else{0}
                })
            })
            .collect::<Vec<_>>();
        outputs.push(json!({
            "class_key":class_key,"canonical_key":orbit["canonical_key"],"labels":labels,
            "free_signed_energy_indices":solution.free.iter().map(|i|i+1).collect::<Vec<_>>(),
            "base_relations":solution.base_relations.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "wall_solution":solution.y.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "routing_gram":gram.to_string(),
            "jacobian_shape":[3,variables.len()],
            "maximal_minors":maximal_minors.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "source_normalized_projective_multiplier":projective_multiplier,
            "all_maximal_minors_zero":maximal_minors.iter().all(|minor|minor==&a("0")),
            "common_gcd":common_expression.to_string(),
            "residual_common_gcd_after_Gram_soft_removal":residual_common.to_string(),
            "residual_common_gcd_is_constant":common.is_constant(),
            "removed_frozen_soft_lower_support_factors":removed_support_factors,
            "residual_common_gcd_after_Gram_soft_lower_saturation":fully_saturated_expression.to_string(),
            "fully_saturated_common_gcd_is_constant":fully_saturated.is_constant(),
            "Gram_specializations":gram_specializations,
            "classification":if common.is_constant(){"no_common_codimension_one_Jacobian_factor_after_Gram_soft_saturation"}else{"candidate_common_horizontal_factor_pending_projection"}
        }));
    }
    let packet = json!({"schema":"marici.seven_site_universal_jacobian.v1","wall_rank":rank,"scope":scope,"item_limit":limit,"classes":outputs});
    let output = std::env::var("OUTPUT")
        .unwrap_or_else(|_| "../results/seven-site-universal-jacobian.json".into());
    fs::write(
        output,
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"wall_rank":rank,"processed":packet["classes"].as_array().unwrap().len(),"all_first_minors_zero":packet["classes"][0]["all_maximal_minors_zero"]})
    );
}

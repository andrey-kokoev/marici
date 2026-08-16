use std::{env, fs};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Q { n: i128, d: i128 }

impl Q {
    const Z: Self = Self { n: 0, d: 1 };
    const O: Self = Self { n: 1, d: 1 };

    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 { n = -n; d = -d; }
        let g = gcd(n.abs(), d);
        Self { n: n / g, d: d / g }
    }
    fn add(self, r: Self) -> Self {
        let g = gcd(self.d, r.d);
        let a = self.d / g;
        let b = r.d / g;
        Self::new(self.n * b + r.n * a, a * r.d)
    }
    fn neg(self) -> Self { Self::new(-self.n, self.d) }
    fn sub(self, r: Self) -> Self { self.add(r.neg()) }
    fn mul(self, r: Self) -> Self {
        let g1 = gcd(self.n.abs(), r.d);
        let g2 = gcd(r.n.abs(), self.d);
        Self::new((self.n / g1) * (r.n / g2), (self.d / g2) * (r.d / g1))
    }
    fn div(self, r: Self) -> Self { self.mul(Self::new(r.d, r.n)) }
    fn pow(self, mut k: usize) -> Self {
        let mut a = self;
        let mut z = Self::O;
        while k > 0 {
            if k & 1 == 1 { z = z.mul(a); }
            k >>= 1;
            if k > 0 { a = a.mul(a); }
        }
        z
    }
    fn json(self) -> String { format!("\"{}/{}\"", self.n, self.d) }
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 { (a, b) = (b, a % b); }
    a.max(1)
}

#[derive(Clone, Copy, Debug)]
struct D { v: Q, dx: Q, dy: Q }

impl D {
    fn c(n: i128, d: i128) -> Self {
        Self { v: Q::new(n, d), dx: Q::Z, dy: Q::Z }
    }
    fn x(x: i128) -> Self { Self { v: Q::new(x, 1), dx: Q::O, dy: Q::Z } }
    fn y(y: i128) -> Self { Self { v: Q::new(y, 1), dx: Q::Z, dy: Q::O } }
    fn add(self, r: Self) -> Self {
        Self { v: self.v.add(r.v), dx: self.dx.add(r.dx), dy: self.dy.add(r.dy) }
    }
    fn neg(self) -> Self { Self { v: self.v.neg(), dx: self.dx.neg(), dy: self.dy.neg() } }
    fn mul(self, r: Self) -> Self {
        Self {
            v: self.v.mul(r.v),
            dx: self.dx.mul(r.v).add(self.v.mul(r.dx)),
            dy: self.dy.mul(r.v).add(self.v.mul(r.dy)),
        }
    }
    fn div(self, r: Self) -> Self {
        let inv = Self {
            v: Q::O.div(r.v),
            dx: r.dx.neg().div(r.v.pow(2)),
            dy: r.dy.neg().div(r.v.pow(2)),
        };
        self.mul(inv)
    }
    fn pow(self, mut k: usize) -> Self {
        let mut a = self;
        let mut z = Self::c(1, 1);
        while k > 0 {
            if k & 1 == 1 { z = z.mul(a); }
            k >>= 1;
            if k > 0 { a = a.mul(a); }
        }
        z
    }
}

fn polynomial(x: D, y: D, terms: &[(i128, usize, usize)]) -> D {
    terms.iter().fold(D::c(0, 1), |z, &(c, px, py)| {
        z.add(D::c(c, 1).mul(x.pow(px)).mul(y.pow(py)))
    })
}

fn h31(x: D, y: D) -> [D; 6] {
    let h1 = polynomial(x, y, &[
        (1727,0,6),(9026,1,5),(19841,2,4),(23548,3,3),
        (16001,4,2),(5954,5,1),(959,6,0),
    ]).div(D::c(32,1).mul(x.pow(2)).mul(y.pow(2)));
    let h3 = polynomial(x, y, &[
        (1667,0,5),(6901,1,4),(11640,2,3),(10136,3,2),(4645,4,1),(915,5,0),
    ]).neg().div(D::c(16,1).mul(x).mul(y));
    let h5 = polynomial(x, y, &[
        (661,0,4),(2113,1,3),(2643,2,2),(1585,3,1),(397,4,0),
    ]).div(D::c(8,1));
    let h7 = x.mul(y).mul(polynomial(x, y, &[
        (259,0,3),(613,1,2),(535,2,1),(181,3,0),
    ])).neg().div(D::c(8,1));
    let h9 = x.pow(2).mul(y.pow(2)).mul(polynomial(x, y, &[
        (25,0,2),(41,1,1),(21,2,0),
    ])).div(D::c(4,1));
    let h11 = x.pow(3).mul(y.pow(3)).mul(x.add(y)).neg().div(D::c(2,1));
    [h1,h3,h5,h7,h9,h11]
}

fn binomial_half(j: usize, k: usize) -> Q {
    let mut z = Q::O;
    for m in 0..k {
        z = z.mul(Q::new(2 * j as i128 + 1 - 2 * m as i128, 2 * (m as i128 + 1)));
    }
    z
}

fn jets(xv: i128, yv: i128, occurrence_31: bool) -> [D; 5] {
    let x = D::x(xv);
    let y = D::y(yv);
    let s = x.add(y);
    let a = x.mul(y);
    let hs = if occurrence_31 {
        h31(x, y)
    } else {
        let swapped = h31(y, x);
        [swapped[0].neg(), swapped[1].neg(), swapped[2].neg(), swapped[3].neg(), swapped[4].neg(), swapped[5].neg()]
    };
    let n2 = D::c(2,1).mul(s).div(a);
    std::array::from_fn(|k| {
        let mut z = D::c(0,1);
        for j in 0..6 {
            z = z.add(hs[j].mul(n2.pow(j)).mul(D::c(binomial_half(j,k).n, binomial_half(j,k).d)));
        }
        z.div(D::c(2,1).mul(s).pow(k))
    })
}

fn derivative_column(j: &[D;5], xv: i128, yv: i128, x_direction: bool) -> [Q;5] {
    // Common prefactor C=N/(8a^(3/2)): d log C = 1/2 d log(x+y)-2 d log(xy).
    let lambda = if x_direction {
        Q::new(1, 2*(xv+yv)).add(Q::new(-2, xv))
    } else {
        Q::new(1, 2*(xv+yv)).add(Q::new(-2, yv))
    };
    std::array::from_fn(|k| {
        let dq = if x_direction { j[k].dx } else { j[k].dy };
        dq.add(lambda.mul(j[k].v))
    })
}

fn span_coordinates(c1: &[D;5], c2: &[D;5], target: &[Q;5]) -> Option<(Q,Q,usize,Q)> {
    for r0 in 0..5 {
        for r1 in r0+1..5 {
            let det = c1[r0].v.mul(c2[r1].v).sub(c1[r1].v.mul(c2[r0].v));
            if det == Q::Z { continue; }
            let alpha = target[r0].mul(c2[r1].v).sub(target[r1].mul(c2[r0].v)).div(det);
            let beta = c1[r0].v.mul(target[r1]).sub(c1[r1].v.mul(target[r0])).div(det);
            for row in 0..5 {
                let residual = target[row].sub(alpha.mul(c1[row].v)).sub(beta.mul(c2[row].v));
                if residual != Q::Z { return Some((alpha,beta,row,residual)); }
            }
            return None;
        }
    }
    panic!("rank below two");
}

fn matrix_rank(columns: &[[Q;5]]) -> usize {
    let mut a = vec![vec![Q::Z; columns.len()]; 5];
    for (c,column) in columns.iter().enumerate() {
        for r in 0..5 { a[r][c] = column[r]; }
    }
    let mut rank = 0;
    for col in 0..columns.len() {
        let Some(pivot) = (rank..5).find(|&r| a[r][col] != Q::Z) else { continue };
        a.swap(rank,pivot);
        let p = a[rank][col];
        for j in col..columns.len() { a[rank][j] = a[rank][j].div(p); }
        for r in 0..5 {
            if r == rank { continue; }
            let f = a[r][col];
            if f == Q::Z { continue; }
            for j in col..columns.len() { a[r][j] = a[r][j].sub(f.mul(a[rank][j])); }
        }
        rank += 1;
        if rank == 5 { break; }
    }
    rank
}

fn line_closure(column: &[D;5], target: &[Q;5]) -> Option<(Q,usize,Q)> {
    let pivot = (0..5).find(|&row| column[row].v != Q::Z).expect("nonzero line");
    let alpha = target[pivot].div(column[pivot].v);
    for row in 0..5 {
        let residual = target[row].sub(alpha.mul(column[row].v));
        if residual != Q::Z { return Some((alpha,row,residual)); }
    }
    None
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let points = [(1_i128,2_i128),(1,3),(2,3),(2,5),(3,4),(3,5)];
    let mut tests = 0_u64;
    let mut failures = Vec::new();
    let mut sewn_line_tests = 0_u64;
    let mut sewn_line_failures = Vec::new();
    let mut sewn_escape_formula_checks = 0_u64;
    let mut first_saturation_ranks = Vec::new();
    for &(x,y) in &points {
        let c31 = jets(x,y,true);
        let c23 = jets(x,y,false);
        let dx31 = derivative_column(&c31,x,y,true);
        let dy31 = derivative_column(&c31,x,y,false);
        let dx23 = derivative_column(&c23,x,y,true);
        let dy23 = derivative_column(&c23,x,y,false);
        let base31: [Q;5] = std::array::from_fn(|k| c31[k].v);
        let base23: [Q;5] = std::array::from_fn(|k| c23[k].v);
        let saturation_rank = matrix_rank(&[base31,base23,dx31,dy31,dx23,dy23]);
        first_saturation_ranks.push((x,y,saturation_rank));
        for (label, target) in [
            ("dx31", dx31), ("dy31", dy31), ("dx23", dx23), ("dy23", dy23),
        ] {
            tests += 1;
            if let Some((alpha,beta,row,residual)) = span_coordinates(&c31,&c23,&target) {
                failures.push(format!(
                    "    {{\"x\":{},\"y\":{},\"derivative\":\"{}\",\"first_escaping_jet_row\":{},\"alpha\":{},\"beta\":{},\"residual\":{}}}",
                    x,y,label,row,alpha.json(),beta.json(),residual.json()
                ));
            }
        }
        let sewn: [D;5] = std::array::from_fn(|k| c31[k].add(c23[k]));
        for (label,left,right) in [("dx",dx31,dx23),("dy",dy31,dy23)] {
            sewn_line_tests += 1;
            let target: [Q;5] = std::array::from_fn(|k| left[k].add(right[k]));
            if let Some((alpha,row,residual)) = line_closure(&sewn,&target) {
                let expected = Q::new(17 * (y*y - x*x), 8 * x*x * y*y);
                assert_eq!(row, 3);
                assert_eq!(residual, expected);
                sewn_escape_formula_checks += 1;
                sewn_line_failures.push(format!(
                    "    {{\"x\":{},\"y\":{},\"derivative\":\"{}\",\"first_escaping_jet_row\":{},\"alpha\":{},\"residual\":{}}}",
                    x,y,label,row,alpha.json(),residual.json()
                ));
            }
        }
    }
    let min_rank = first_saturation_ranks.iter().map(|z| z.2).min().unwrap();
    let max_rank = first_saturation_ranks.iter().map(|z| z.2).max().unwrap();
    let rank_json = first_saturation_ranks.iter()
        .map(|&(x,y,rank)| format!("{{\"x\":{},\"y\":{},\"rank\":{}}}",x,y,rank))
        .collect::<Vec<_>>().join(",");
    let json = format!(
        "{{\n  \"schema\": \"marici.occurrence-jet-closure.v2\",\n  \"normal_coordinate\": \"w^2=x*y*n^2-2*(x+y)\",\n  \"moving_endpoint_included\": true,\n  \"highest_odd_primitive_degree\": 11,\n  \"degree_eleven_term_included\": true,\n  \"source_section_span_tests\": {},\n  \"closure_failures\": {},\n  \"rank_two_source_section_span_closed\": {},\n  \"sewn_jet_line_tests\": {},\n  \"sewn_jet_line_failures\": {},\n  \"sewn_jet_line_closed\": {},\n  \"sewn_first_escape_order\": \"w^-3\",\n  \"sewn_escape_formula\": \"17*(y^2-x^2)/(8*x^2*y^2)\",\n  \"sewn_escape_formula_checks\": {},\n  \"first_connection_saturation_min_rank\": {},\n  \"first_connection_saturation_max_rank\": {},\n  \"first_connection_saturation_ranks\": [{}],\n  \"failures\": [\n{}\n  ],\n  \"sewn_line_failure_details\": [\n{}\n  ],\n  \"new_carrier_incidence\": false\n}}\n",
        tests, failures.len(), failures.is_empty(),
        sewn_line_tests, sewn_line_failures.len(), sewn_line_failures.is_empty(),
        sewn_escape_formula_checks,
        min_rank, max_rank, rank_json,
        failures.join(",\n"), sewn_line_failures.join(",\n")
    );
    fs::write(output,json).expect("write certificate");
}

#!/usr/bin/env node
"use strict";

const fs = require("fs");

function gcd(a, b) {
  a = a < 0n ? -a : a; b = b < 0n ? -b : b;
  while (b) [a, b] = [b, a % b];
  return a;
}
function egcd(a, b) {
  let oldR = a, r = b, oldS = 1n, s = 0n;
  while (r) {
    const q = oldR / r;
    [oldR, r] = [r, oldR - q * r];
    [oldS, s] = [s, oldS - q * s];
  }
  return [oldR, oldS];
}
function invMod(a, m) {
  const [g, x] = egcd((a % m + m) % m, m);
  if (g !== 1n) throw new Error("noninvertible CRT modulus");
  return (x % m + m) % m;
}
function crt(residues, moduli) {
  let x = 0n, modulus = 1n;
  for (let i = 0; i < residues.length; i++) {
    const p = moduli[i];
    const delta = ((residues[i] - x) % p + p) % p;
    const step = delta * invMod(modulus % p, p) % p;
    x += modulus * step;
    modulus *= p;
  }
  return [x, modulus];
}
function isqrt(n) {
  if (n < 0n) throw new Error("negative sqrt");
  if (n < 2n) return n;
  let x = 1n << (BigInt(n.toString(2).length) + 1n >> 1n);
  while (true) {
    const y = (x + n / x) >> 1n;
    if (y >= x) return x;
    x = y;
  }
}
function rationalReconstruct(x, m) {
  const bound = isqrt(m / 2n);
  let r0 = m, r1 = x, t0 = 0n, t1 = 1n;
  while (r1 > bound) {
    const q = r0 / r1;
    [r0, r1] = [r1, r0 - q * r1];
    [t0, t1] = [t1, t0 - q * t1];
  }
  let num = r1, den = t1;
  if (den < 0n) { num = -num; den = -den; }
  const d = gcd(num, den);
  num /= d; den /= d;
  if (den === 0n || (num < 0n ? -num : num) > bound || den > bound) return null;
  if (((num - x * den) % m + m) % m !== 0n) return null;
  return [num, den];
}
function sparseMap(vector) {
  return new Map(vector.entries.map(([column, value]) => [column, BigInt(value)]));
}

if (process.argv.length < 7) {
  throw new Error("usage: node reconstruct_interaction_net_residual_nullspace.cjs MATRIX NS1 NS2 NS3 [NS...] OUTPUT");
}
const [matrixPath, ...rest] = process.argv.slice(2);
const outputPath = rest.pop();
const packets = rest.map(path => JSON.parse(fs.readFileSync(path, "utf8")));
const primes = packets.map(packet => BigInt(packet.prime));
const pivotHash = packets[0].pivot_sha256;
for (const packet of packets) {
  if (packet.pivot_sha256 !== pivotHash) throw new Error("pivot mismatch");
  if (JSON.stringify(packet.free_columns) !== JSON.stringify(packets[0].free_columns)) throw new Error("free-column mismatch");
}
const maps = packets.map(packet => packet.basis.map(sparseMap));
const columns = packets[0].matrix_header.columns;
const reconstructed = [];
let failed = 0;
let maxNumerator = 0n, maxDenominator = 0n;
for (let basisIndex = 0; basisIndex < packets[0].basis.length; basisIndex++) {
  const entries = [];
  for (let column = 0; column < columns; column++) {
    const residues = maps.map(mapBasis => mapBasis[basisIndex].get(column) || 0n);
    const [value, modulus] = crt(residues, primes);
    const fraction = rationalReconstruct(value, modulus);
    if (!fraction) { failed++; continue; }
    const [num, den] = fraction;
    if (num) entries.push([column, num.toString(), den.toString()]);
    const absNum = num < 0n ? -num : num;
    if (absNum > maxNumerator) maxNumerator = absNum;
    if (den > maxDenominator) maxDenominator = den;
  }
  reconstructed.push({free_column: packets[0].free_columns[basisIndex], entries});
}
const result = {
  schema: "marici.rational-residual-nullspace.v1",
  status: failed === 0 ? "candidate" : "incomplete",
  primes: packets.map(packet => packet.prime),
  modulus: primes.reduce((a, b) => a * b, 1n).toString(),
  pivot_sha256: pivotHash,
  vector_count: reconstructed.length,
  column_count: columns,
  failed_reconstructions: failed,
  maximum_absolute_numerator: maxNumerator.toString(),
  maximum_denominator: maxDenominator.toString(),
  basis: reconstructed
};
fs.writeFileSync(outputPath, JSON.stringify(result) + "\n");
process.stdout.write(JSON.stringify({...result, basis: undefined}, null, 2) + "\n");

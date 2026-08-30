#!/usr/bin/env node
"use strict";

const fs = require("fs");
const crypto = require("crypto");

function modBigInt(text, prime) {
  const p = BigInt(prime);
  let value = BigInt(text) % p;
  if (value < 0n) value += p;
  return Number(value);
}

function inverse(value, prime) {
  let a = value, b = prime, x0 = 1, x1 = 0;
  while (b !== 0) {
    const q = Math.floor(a / b);
    [a, b] = [b, a - q * b];
    [x0, x1] = [x1, x0 - q * x1];
  }
  return ((x0 % prime) + prime) % prime;
}

function leading(row) {
  let pivot = Infinity;
  for (const column of row.keys()) if (column < pivot) pivot = column;
  return pivot;
}

function sparseRank(lines, prime) {
  const pivots = new Map();
  let sourceRows = 0;
  for (let lineIndex = 1; lineIndex < lines.length; lineIndex++) {
    const line = lines[lineIndex];
    if (!line) continue;
    sourceRows++;
    const row = new Map();
    for (const entry of line.split(",")) {
      const split = entry.indexOf(":");
      const column = Number(entry.slice(0, split));
      const value = modBigInt(entry.slice(split + 1), prime);
      if (value) row.set(column, value);
    }
    while (row.size) {
      const pivot = leading(row);
      const basis = pivots.get(pivot);
      if (!basis) {
        const scale = inverse(row.get(pivot), prime);
        for (const [column, value] of row) {
          const normalized = (value * scale) % prime;
          if (normalized) row.set(column, normalized);
          else row.delete(column);
        }
        pivots.set(pivot, row);
        break;
      }
      const factor = row.get(pivot);
      for (const [column, value] of basis) {
        let reduced = (row.get(column) || 0) - factor * value;
        reduced %= prime;
        if (reduced < 0) reduced += prime;
        if (reduced) row.set(column, reduced);
        else row.delete(column);
      }
    }
  }
  return {rank: pivots.size, source_rows: sourceRows, pivots};
}

function nullspaceBasis(pivots, columns, prime) {
  const pivotColumns = [...pivots.keys()].sort((a, b) => a - b);
  const pivotSet = new Set(pivotColumns);
  const freeColumns = [];
  for (let column = 0; column < columns; column++) {
    if (!pivotSet.has(column)) freeColumns.push(column);
  }
  const descendingPivots = [...pivotColumns].reverse();
  const basis = [];
  for (const freeColumn of freeColumns) {
    const vector = new Int32Array(columns);
    vector[freeColumn] = 1;
    for (const pivot of descendingPivots) {
      let sum = 0;
      for (const [column, coefficient] of pivots.get(pivot)) {
        if (column !== pivot && vector[column]) {
          sum = (sum + coefficient * vector[column]) % prime;
        }
      }
      vector[pivot] = sum ? prime - sum : 0;
    }
    const sparse = [];
    for (let column = 0; column < columns; column++) {
      if (vector[column]) sparse.push([column, vector[column]]);
    }
    basis.push({free_column: freeColumn, entries: sparse});
  }
  return {pivot_columns: pivotColumns, free_columns: freeColumns, basis};
}

if (process.argv.length < 4) {
  throw new Error("usage: node rank_interaction_net_residual.cjs MATRIX PRIME [PRIME...] [--nullspace-prefix=PATH]");
}
const matrixPath = process.argv[2];
const nullspacePrefixArgument = process.argv.slice(3).find(arg => arg.startsWith("--nullspace-prefix="));
const nullspacePrefix = nullspacePrefixArgument ? nullspacePrefixArgument.split("=", 2)[1] : null;
const primes = process.argv.slice(3).filter(arg => !arg.startsWith("--")).map(Number);
const data = fs.readFileSync(matrixPath, "utf8");
const lines = data.split(/\r?\n/);
const header = JSON.parse(lines[0]);
const results = {};
for (const prime of primes) {
  const started = Date.now();
  const result = sparseRank(lines, prime);
  const pivotColumns = [...result.pivots.keys()].sort((a, b) => a - b);
  const pivotHash = crypto.createHash("sha256").update(JSON.stringify(pivotColumns)).digest("hex");
  if (nullspacePrefix) {
    const nullspace = nullspaceBasis(result.pivots, header.columns, prime);
    fs.writeFileSync(
      `${nullspacePrefix}-${prime}.json`,
      JSON.stringify({
        schema: "marici.sparse-residual-nullspace.v1",
        prime,
        matrix_header: header,
        pivot_sha256: pivotHash,
        ...nullspace
      }) + "\n"
    );
  }
  results[String(prime)] = {
    rank: result.rank,
    source_rows: result.source_rows,
    pivot_sha256: pivotHash,
    nullspace_dimension: header.columns - result.rank,
    milliseconds: Date.now() - started
  };
}
process.stdout.write(JSON.stringify({
  schema: "marici.sparse-residual-rank.v1",
  matrix: matrixPath,
  header,
  results,
  quotient_dimensions: Object.fromEntries(
    Object.entries(results).map(([prime, result]) => [prime, header.columns - result.rank])
  )
}, null, 2) + "\n");

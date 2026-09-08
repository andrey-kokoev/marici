param(
  [ValidateSet('11-boundary-framed-comparison', '12-relative-cochain-secondary', '13-split-support-fibre', '14-hom-complex-window', '15-integer-hom-indexing', '16-integer-coefficient-complex', '17-integer-hom-square', '18-finite-coefficient-presentations', '19-loaded-polynomial-cech-modules', '20-loaded-coefficient-square')]
  [string] $Module = '11-boundary-framed-comparison',
  [ValidateRange(1,300)] [int] $TimeoutSeconds = 30
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'bounded-process.ps1')
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$results = Join-Path $repo 'research/nima/results'
New-Item -ItemType Directory -Force -Path $results | Out-Null
$relativeTarget = "research/nima/rzk/$Module.rzk.md"
$target = [IO.Path]::GetFullPath((Join-Path $repo $relativeTarget))
$closure = @('research/nima/rzk/11-boundary-framed-comparison.rzk.md')
if ($Module -ne '11-boundary-framed-comparison') {
  $closure += 'research/nima/rzk/12-relative-cochain-secondary.rzk.md'
}
if ($Module -in @('13-split-support-fibre', '14-hom-complex-window')) {
  $closure += 'research/nima/rzk/13-split-support-fibre.rzk.md'
}
if ($Module -eq '14-hom-complex-window') {
  $closure += 'research/nima/rzk/14-hom-complex-window.rzk.md'
}
$manifest = $null
if ($Module -in @('15-integer-hom-indexing', '16-integer-coefficient-complex', '17-integer-hom-square', '18-finite-coefficient-presentations', '19-loaded-polynomial-cech-modules', '20-loaded-coefficient-square')) {
  $manifest = Get-Content (Join-Path $results "$Module.closure.json") -Raw | ConvertFrom-Json
  if ($manifest.target -ne $relativeTarget) { throw 'Closure manifest targets a different module' }
  $closure = @($manifest.files | ForEach-Object { $_.path })
  if ($closure.Count -eq 0 -or $closure[-1] -ne $relativeTarget) { throw 'Closure must end with the requested target' }
}
$absoluteClosure = @($closure | ForEach-Object {
  $full = [IO.Path]::GetFullPath((Join-Path $repo $_))
  if (-not $full.StartsWith($repo + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Dependency outside repository: $_"
  }
  $full
})
if (@($absoluteClosure | Select-Object -Unique).Count -ne $absoluteClosure.Count) { throw 'Duplicate dependency path' }
$cmd = Get-Command rzk -ErrorAction SilentlyContinue
$exe = if ($null -ne $cmd) { $cmd.Source } else { Join-Path $HOME '.local/bin/rzk.exe' }
if (-not (Test-Path -LiteralPath $exe -PathType Leaf)) { throw "Rzk not found: $exe" }
$inputs = Get-NimaInputSnapshot -Paths ($absoluteClosure + @($exe))
if ($null -ne $manifest) {
  for ($i = 0; $i -lt $absoluteClosure.Count; $i++) {
    if ($inputs[$i].sha256 -ne $manifest.files[$i].sha256) {
      throw "Stale dependency manifest: $($closure[$i]). Rebuild the closure first."
    }
  }
}
$started = [DateTimeOffset]::UtcNow.ToString('o')
$run = Invoke-NimaBoundedProcess -Executable $exe -WorkingDirectory $repo `
  -Arguments (@('typecheck') + $absoluteClosure) -TimeoutMilliseconds ($TimeoutSeconds * 1000)
$stable = Test-NimaInputSnapshot -Snapshot $inputs
$exitCode = if (-not $stable) { 125 } else { $run.exit_code }
$status = if (-not $stable) { 'input_changed' } elseif ($run.timed_out) { 'timed_out' } elseif ($exitCode -eq 0) { 'passed' } else { 'failed' }
$dependencyEvidence = @(for ($i = 0; $i -lt $closure.Count; $i++) {
  @{ path = $closure[$i]; sha256 = $inputs[$i].sha256 }
})
$record = [ordered]@{
  started_at = $started
  checked_at = [DateTimeOffset]::UtcNow.ToString('o')
  status = $status
  target = $relativeTarget
  target_sha256 = ($inputs | Where-Object { $_.path -eq $target }).sha256
  executable_sha256 = $inputs[-1].sha256
  exit_code = $exitCode
  process_exit_code = $run.process_exit_code
  timed_out = $run.timed_out
  timeout_seconds = $TimeoutSeconds
  duration_ms = $run.duration_ms
  input_hashes_match_before_after = $stable
  stdout = $run.stdout
  stderr = $run.stderr
  dependency_closure = $dependencyEvidence
}
$record | ConvertTo-Json -Depth 5 | Set-Content (Join-Path $results "$Module.typecheck.json")
[Console]::Out.Write($run.stdout)
[Console]::Error.Write($run.stderr)
if (-not $stable) { [Console]::Error.WriteLine('Input changed during verification; result not accepted.') }
if ($run.timed_out) { [Console]::Error.WriteLine('Rzk timeout; partial diagnostics retained.') }
exit $exitCode

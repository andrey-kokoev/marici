# Used only after a goal certificate has been emitted; never emits a theorem itself.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/milestones/double-negation/agda'
$Results = Join-Path $Root 'research/nima/results'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Compiler = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Run = Join-Path $Root '.ai/tmp/scc-state/nima-double-negation-kernel-run.json'
$Receipt = Join-Path $Results 'double-negation-kernel.json'
if (!(Test-Path (Join-Path $Sources 'DoubleNegation.agda'))) { throw 'No goal theorem emitted: kernel gate unavailable.' }
function Inventory {
  $Out = [ordered]@{}
  foreach ($Dir in @($Sources,$Library)) {
    foreach ($File in (Get-ChildItem $Dir -File -Recurse -Filter '*.agda' | Sort-Object FullName)) {
      $Out[$File.FullName] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash
    }
  }
  return ,$Out
}
$Before = Inventory
$CompilerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash
$CheckerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash
if (Test-Path $Receipt) { Remove-Item $Receipt }
$Manifest = [ordered]@{
  schema='marici.double-negation.kernel-run.v1'; compiler=$Compiler; compiler_sha256=$CompilerHash;
  build='existing Agda 2.8.0 executable'; source_sha256=$Before; checker_sha256=$CheckerHash;
  parent_pid=$PID; children=@(); status='running'; started_at=[DateTime]::UtcNow.ToString('o');
  expected_schema='marici.double-negation.kernel-audit.v1'; receipt=$Receipt
}
$Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
function Compile([string]$Module) {
  $Log = Join-Path $Results "agda-$Module.log"
  $Err = Join-Path $Results "agda-$Module.stderr.log"
  $Args = @('--transliterate','--ignore-interfaces','-i',$Sources,'-i',$Library,(Join-Path $Sources "$Module.agda"))
  $Process = Start-Process -FilePath $Compiler -ArgumentList $Args -NoNewWindow -PassThru -RedirectStandardOutput $Log -RedirectStandardError $Err -WorkingDirectory $Root
  $Manifest.children += @{pid=$Process.Id; start_ticks=$Process.StartTime.ToUniversalTime().Ticks; args=$Args; stdout=$Log; stderr=$Err}
  $Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
  try {
    if (!$Process.WaitForExit(120000)) { throw "Compiler timeout: $Module" }
    return @{code=$Process.ExitCode; text=((Get-Content $Log -Raw)+(Get-Content $Err -Raw))}
  } finally {
    # Only this exact child object is eligible for cleanup, never a discovered process.
    if (!$Process.HasExited) { $Process.Kill(); $Process.WaitForExit() }
  }
}
try {
  $Positive = Compile 'DoubleNegation'
  if ($Positive.code -ne 0) { throw $Positive.text }
  $Negative = Compile 'DoubleNegationWrongConclusion'
  $Rejected = $Negative.code -ne 0 -and $Negative.text.Contains('[UnequalTerms]')
  if (!$Rejected) { throw 'Wrong-conclusion negative control failed.' }
  $After = Inventory
  $Stable = (($Before | ConvertTo-Json -Compress) -ceq ($After | ConvertTo-Json -Compress)) -and ($CompilerHash -ceq (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash) -and ($CheckerHash -ceq (Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash)
  if (!$Stable) { throw 'Compiler inputs changed.' }
  [ordered]@{
    schema='marici.double-negation.kernel-audit.v1'; passed=$true; fresh=$true; inputs_stable=$true;
    negative_rejected=$true; negative_diagnostic='[UnequalTerms]'; source_sha256=$After;
    compiler=$Compiler; compiler_sha256=$CompilerHash; checker_sha256=$CheckerHash; run_manifest=$Run
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
  $Manifest.status = 'passed'
  Write-Output 'PASS: fresh double-negation kernel check and altered-conclusion control'
} catch {
  $Manifest.status = 'failed'
  throw
} finally {
  $Manifest['finished_at'] = [DateTime]::UtcNow.ToString('o')
  $Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
}

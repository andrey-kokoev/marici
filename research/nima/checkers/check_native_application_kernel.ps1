param([switch]$Incremental)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/adapters/native-application'
$Core = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Compiler = Join-Path $env:USERPROFILE 'tools/cubical-agda/agda-2.8.0/agda.exe'
$Library = Join-Path $env:USERPROFILE 'tools/cubical-agda/cubical-0.9'
$Run = Join-Path $Root '.ai/tmp/scc-state/nima-native-application-run.json'
$Stem = if ($Incremental) { 'native-application-incremental' } else { 'native-application' }
$Receipt = Join-Path $Results "$Stem-kernel.json"
function Inventory {
  $Out = [ordered]@{}
  foreach ($Dir in @($Sources,$Core,$Library)) {
    foreach ($File in (Get-ChildItem $Dir -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
      $Out[$File.FullName] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash
    }
  }
  return ,$Out
}
if (Test-Path $Run) {
  $Old = Get-Content $Run -Raw | ConvertFrom-Json
  if ($Old.status -eq 'running') { throw 'Previous run needs reconciliation.' }
}
$Before = Inventory
$CompilerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash
$CheckerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash
if (Test-Path $Receipt) { Remove-Item $Receipt }
$Manifest = [ordered]@{
  schema='marici.native-application.kernel-run.v1'; compiler=$Compiler; compiler_sha256=$CompilerHash;
  build='existing Agda 2.8.0 executable'; source_sha256=$Before; checker_sha256=$CheckerHash;
  parent_pid=$PID; children=@(); status='running'; started_at=[DateTime]::UtcNow.ToString('o');
  expected_schema='marici.native-application.kernel-audit.v1'; receipt=$Receipt
}
$Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
function Compile([string]$Name, [bool]$Fresh) {
  $Log = Join-Path $Results "agda-$Name.log"
  $Err = Join-Path $Results "agda-$Name.stderr.log"
  $Args = @('--transliterate','-i',$Sources,'-i',$Core,'-i',$Library)
  if ($Fresh) { $Args += '--ignore-interfaces' }
  $Args += Join-Path $Sources "$Name.agda"
  $Process = Start-Process -FilePath $Compiler -ArgumentList $Args -NoNewWindow -PassThru -RedirectStandardOutput $Log -RedirectStandardError $Err -WorkingDirectory $Root
  $Manifest.children += @{pid=$Process.Id; start_ticks=$Process.StartTime.ToUniversalTime().Ticks; args=$Args; stdout=$Log; stderr=$Err}
  $Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
  try {
    if (!$Process.WaitForExit(300000)) { throw "Compiler timeout: $Name" }
    return @{code=$Process.ExitCode; text=((Get-Content $Log -Raw)+(Get-Content $Err -Raw)); args=$Args}
  } finally {
    if (!$Process.HasExited) { $Process.Kill(); $Process.WaitForExit() }
  }
}
try {
  $Positive = Compile 'NativeApplicationGate' (!$Incremental)
  if ($Positive.code -ne 0) { throw $Positive.text }
  $Negative = Compile 'NativeApplicationBadReadout' $false
  if ($Negative.code -eq 0 -or !$Negative.text.Contains('[UnequalTerms]')) { throw "Wrong rejection: $($Negative.text)" }
  $After = Inventory
  $Stable = (($Before | ConvertTo-Json -Compress) -ceq ($After | ConvertTo-Json -Compress)) -and ($CompilerHash -ceq (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash) -and ($CheckerHash -ceq (Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash)
  if (!$Stable) { throw 'Compiler inputs changed.' }
  [ordered]@{
    schema='marici.native-application.kernel-audit.v1'; passed=$true; fresh=(!$Incremental); inputs_stable=$true;
    module='NativeApplicationGate'; positive_exit_code=0; args=$Positive.args;
    negative_exit_code=$Negative.code; negative_diagnostic='[UnequalTerms]'; source_sha256=$After;
    compiler=$Compiler; compiler_sha256=$CompilerHash; checker_sha256=$CheckerHash; run_manifest=$Run
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
  $Manifest.status = 'passed'
  Write-Output "PASS: native application endpoint obstruction and retained-operand/readout control; fresh=$(!$Incremental)"
} catch {
  $Manifest.status = 'failed'
  throw
} finally {
  $Manifest['finished_at'] = [DateTime]::UtcNow.ToString('o')
  $Manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Run
}

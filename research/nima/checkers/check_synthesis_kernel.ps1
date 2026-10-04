param(
  [ValidateSet('SynthesisCertifiedMinimum','FreshEquationalConsequences')][string]$Module = 'SynthesisCertifiedMinimum',
  [switch]$CleanupOnly,
  [switch]$Incremental
)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/agda'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Compiler = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Results = Join-Path $Root 'research/nima/results'
# Existing ignored SCC state directory; no shared checkpoint is overwritten.
$Run = Join-Path $Root '.ai/tmp/scc-state/nima-synthesis-kernel-run.json'
$Stem = if ($Module -eq 'SynthesisCertifiedMinimum') { 'synthesis-kernel' } else { 'fresh-equations-kernel' }
if ($Incremental) { $Stem += '-incremental' }
$Schema = 'marici.synthesis.kernel-audit.v1'
$Receipt = Join-Path $Results "$Stem-formal-audit.json"
if (Test-Path $Run) {
  $Previous = Get-Content $Run -Raw | ConvertFrom-Json
  if ($Previous.status -eq 'running') {
    $Owned = Get-Process -Id $Previous.child_pid -ErrorAction SilentlyContinue
    if ($Owned) {
      $Delta = ($Owned.StartTime.ToUniversalTime() - [DateTime]::Parse($Previous.started_at).ToUniversalTime()).TotalSeconds
      if ($Owned.Path -ne $Previous.command -or $Delta -lt -1 -or $Delta -gt 30) {
        throw 'Stale PID does not match the recorded compiler child; refusing cleanup.'
      }
      $Owned.Kill()
      $Owned.WaitForExit()
    }
    $Previous.status = 'interrupted-and-owned-child-reconciled'
    $Previous | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 ($Run + '.previous.json')
    $Previous | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Run
  }
}
if ($CleanupOnly) { Write-Output 'Owned compiler child reconciled'; return }
if (Test-Path $Receipt) { Remove-Item $Receipt }
function Inventory([string]$Dir) {
  $Out = [ordered]@{}
  foreach ($File in (Get-ChildItem $Dir -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
    $Out[[IO.Path]::GetRelativePath($Dir,$File.FullName).Replace('\','/')] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash
  }
  return ,$Out
}
$Owner = Inventory $Sources
$Lib = Inventory $Library
$CompilerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash
$Log = Join-Path $Results "agda-$Module.log"
$Err = Join-Path $Results "agda-$Module.stderr.log"
$Args = @('--transliterate','-i',$Sources,'-i',$Library)
if (!$Incremental) { $Args += '--ignore-interfaces' }
$Args += Join-Path $Sources "$Module.agda"
$Manifest = [ordered]@{
  schema='marici.synthesis.kernel-run.v1'; command=$Compiler; args=$Args;
  build='existing Agda 2.8.0 executable'; compiler_sha256=$CompilerHash;
  source_sha256=$Owner; library_sha256=$Lib; parent_pid=$PID; child_pid=$null;
  started_at=[DateTime]::UtcNow.ToString('o'); status='starting'; stdout=$Log; stderr=$Err;
  expected_schema='marici.synthesis.kernel-audit.v1'
}
$Manifest | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Run
$Process = Start-Process -FilePath $Compiler -ArgumentList $Args -WorkingDirectory $Root -NoNewWindow -RedirectStandardOutput $Log -RedirectStandardError $Err -PassThru
$Manifest.child_pid = $Process.Id
$Manifest.status = 'running'
$Manifest | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Run
if (!$Process.WaitForExit(600000)) {
  $Process.Kill()
  $Process.WaitForExit()
  $Code = 124
} else { $Code = $Process.ExitCode }
$Controls = @()
if ($Code -eq 0) {
  $Cases = if ($Module -eq 'SynthesisCertifiedMinimum') {
    @(@{name='SynthesisMinimumMissingCase'; diagnostic='[CoverageIssue]'}, @{name='SynthesisMinimumBadRejection'; diagnostic='[UnequalTerms]'})
  } else { @{name='FreshWrongConclusion'; diagnostic='[UnequalTerms]'} }
  foreach ($Case in $Cases) {
    $Name = $Case.name; $Expected = $Case.diagnostic
    $NLog = Join-Path $Results "agda-$Name.log"
    $NErr = Join-Path $Results "agda-$Name.stderr.log"
    $NArgs = @('--transliterate','-i',$Sources,'-i',(Join-Path $Sources 'negative'),'-i',$Library,(Join-Path $Sources "negative/$Name.agda"))
    $NProcess = Start-Process -FilePath $Compiler -ArgumentList $NArgs -WorkingDirectory $Root -NoNewWindow -RedirectStandardOutput $NLog -RedirectStandardError $NErr -Wait -PassThru
    $Text = (Get-Content $NLog -Raw) + (Get-Content $NErr -Raw)
    $Rejected = $NProcess.ExitCode -ne 0 -and $Text.Contains($Expected)
    $Controls += @{module=$Name; exit_code=$NProcess.ExitCode; expected_diagnostic=$Expected; correctly_rejected=$Rejected; args=$NArgs}
    if (!$Rejected) { $Code = 44; Write-Output $Text }
  }
}
$OwnerAfter = Inventory $Sources
$LibAfter = Inventory $Library
$Stable = (($Owner | ConvertTo-Json -Compress) -ceq ($OwnerAfter | ConvertTo-Json -Compress)) -and (($Lib | ConvertTo-Json -Compress) -ceq ($LibAfter | ConvertTo-Json -Compress)) -and ($CompilerHash -ceq (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash)
$Manifest.status = if ($Code -eq 0 -and $Stable) { 'passed' } else { 'failed' }
$Manifest['exit_code'] = $Code
$Manifest['finished_at'] = [DateTime]::UtcNow.ToString('o')
$Manifest | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Run
[ordered]@{
 schema=$Schema; module=$Module; passed=($Code -eq 0 -and $Stable); controls=$Controls;
 exit_code=$Code; inputs_stable=$Stable; ignore_interfaces=(!$Incremental); no_new_window=$true;
 command=$Compiler; args=$Args; compiler_sha256=$CompilerHash;
 owner_source_inventory_sha256=$OwnerAfter; library=$Library; library_source_inventory_sha256=$LibAfter;
 checker_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash;
 run_manifest=$Run; stdout=$Log; stderr=$Err; finished_at=$Manifest.finished_at
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
if ($Code -ne 0 -or !$Stable) {
  Write-Output ((Get-Content $Log -Raw) + (Get-Content $Err -Raw))
  throw "Kernel compilation failed: $Code; stable=$Stable"
}
Write-Output "PASS: kernel check of $Module; fresh=$(!$Incremental)"

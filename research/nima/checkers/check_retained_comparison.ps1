param(
  [ValidateSet('RetainedComparisonStructure','RetainedComparisonReduction')][string]$Module = 'RetainedComparisonStructure',
  [switch]$VersionOnly
)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Results = Join-Path $Root 'research/nima/results'
$Sources = Join-Path $Root 'research/nima/agda'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Compiler = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
if ($VersionOnly) {
  $VersionLog = Join-Path $Results 'agda-headless-version.log'
  $VersionErr = Join-Path $Results 'agda-headless-version.stderr.log'
  $Process = Start-Process -FilePath $Compiler -ArgumentList @('--version') -NoNewWindow -RedirectStandardOutput $VersionLog -RedirectStandardError $VersionErr -Wait -PassThru
  Get-Content $VersionLog
  Get-Content $VersionErr
  exit $Process.ExitCode
}
$ReceiptName = if ($Module -eq 'RetainedComparisonStructure') { 'retained-comparison-formal-audit.json' } else { 'retained-comparison-reduction-formal-audit.json' }
$Receipt = Join-Path $Results $ReceiptName
if (Test-Path $Receipt) { Remove-Item $Receipt }
function Inventory([string]$Dir) {
  $Out = [ordered]@{}
  foreach ($File in (Get-ChildItem $Dir -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
    $Out[[IO.Path]::GetRelativePath($Dir,$File.FullName).Replace('\','/')] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash
  }
  return ,$Out
}
function Compile([string]$Module, [bool]$Fresh) {
  $Source = Join-Path $Sources "$Module.agda"
  $Name = [IO.Path]::GetFileName($Module)
  $Log = Join-Path $Results "agda-$Name.log"
  $Err = Join-Path $Results "agda-$Name.stderr.log"
  $Args = @('--transliterate','-i',$Sources,'-i',(Join-Path $Sources 'negative'),'-i',$Library)
  if ($Fresh) { $Args += '--ignore-interfaces' }
  $Args += $Source
  # NoNewWindow prevents Windows Terminal activation. Explicit application
  # launch avoids document classification in the sanitized execution environment.
  $Process = Start-Process -FilePath $Compiler -ArgumentList $Args -WorkingDirectory $Root -NoNewWindow -RedirectStandardOutput $Log -RedirectStandardError $Err -Wait -PassThru
  $Text = (Get-Content $Log -Raw) + (Get-Content $Err -Raw)
  Write-Output $Text
  return @{ code=$Process.ExitCode; text=$Text; args=$Args }
}
$Started = [DateTime]::UtcNow.ToString('o')
$OwnerBefore = Inventory $Sources
$LibraryBefore = Inventory $Library
$CompilerBefore = (Get-FileHash -Algorithm SHA256 $Compiler).Hash
$Output = @(Compile $Module $true)
$Positive = $Output[-1]
$Output[0..($Output.Count-2)] | Write-Output
if ($Positive.code -ne 0) { throw "Existence proof compilation failed: $($Positive.code)" }
$Output = @(Compile 'negative/RetainedComparisonBadErasure' $false)
$Negative = $Output[-1]
if ($Negative.code -eq 0 -or !$Negative.text.Contains('[UnequalTerms]') -or !$Negative.text.Contains('false') -or !$Negative.text.Contains('true')) {
  throw "Wrong erasure-control result: $($Negative.code)`n$($Negative.text)"
}
$OwnerAfter = Inventory $Sources
$LibraryAfter = Inventory $Library
$CompilerAfter = (Get-FileHash -Algorithm SHA256 $Compiler).Hash
$Stable = (($OwnerBefore | ConvertTo-Json -Compress) -ceq ($OwnerAfter | ConvertTo-Json -Compress)) -and (($LibraryBefore | ConvertTo-Json -Compress) -ceq ($LibraryAfter | ConvertTo-Json -Compress)) -and ($CompilerBefore -ceq $CompilerAfter)
if (!$Stable) { throw 'Inputs changed during compilation' }
[ordered]@{
  schema='marici.nima.retained-comparison-formal-audit.v1'
  passed=$true
  module=$Module
  started_at=$Started
  finished_at=[DateTime]::UtcNow.ToString('o')
  command=$Compiler
  args=$Positive.args
  ignore_interfaces=$true
  compiler_sha256=$CompilerAfter
  owner_source_inventory_sha256=$OwnerAfter
  library_source_inventory_sha256=$LibraryAfter
  inputs_stable_during_check=$Stable
  checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash
  positive_exit_code=$Positive.code
  erasure_control_exit_code=$Negative.code
  erasure_control_correctly_rejected=$true
  scope=if ($Module -eq 'RetainedComparisonStructure') { 'Inhabitant of the candidate comparison/change/realization record; distinct changes with equal realization; no left inverse of realization; derived transport.' } else { 'Right-unit and right-inverse laws derived from left-unit, associativity and left-inverse laws; recovery of the original chosen witnesses for set-valued change homs. Original record unchanged.' }
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
Write-Output 'PASS: inhabited candidate record, retained-change distinction, and expected erasure rejection.'

param(
  [ValidatePattern('^[A-Za-z][A-Za-z0-9]*$')][string]$Module = 'GradedBoundaryCoherence',
  [ValidatePattern('^[a-z][a-z0-9-]*$')][string]$ReceiptStem = 'graded-boundary-coherence',
  [ValidatePattern('^[A-Za-z][A-Za-z0-9]*(,[A-Za-z][A-Za-z0-9]*)*$')][string]$NegativeModules = 'GradedBoundaryBadFiller,GradedBoundaryBadErasure'
)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Compiler = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Receipt = Join-Path $Results "$ReceiptStem-formal-audit.json"
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
  # Required: do not open a console or steal operator focus.
  $Process = Start-Process -FilePath $Compiler -ArgumentList $Args -WorkingDirectory $Root -NoNewWindow -RedirectStandardOutput $Log -RedirectStandardError $Err -Wait -PassThru
  $Text = (Get-Content $Log -Raw) + (Get-Content $Err -Raw)
  return @{ module=$Module; code=$Process.ExitCode; text=$Text; args=$Args }
}
$Started = [DateTime]::UtcNow.ToString('o')
$OwnerBefore = Inventory $Sources
$LibraryBefore = Inventory $Library
$CompilerBefore = (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash
$Positive = Compile $Module $true
if ($Positive.code -ne 0) { throw "Positive compilation failed: $($Positive.code)`n$($Positive.text)" }
$Controls = @()
foreach ($Name in $NegativeModules.Split(',')) {
  $Negative = Compile "negative/$Name" $false
  if ($Negative.code -eq 0 -or !$Negative.text.Contains('[UnequalTerms]') -or !$Negative.text.Contains('false') -or !$Negative.text.Contains('true')) {
    throw "Wrong rejection for $Name`: $($Negative.code)`n$($Negative.text)"
  }
  $Controls += @{ module=$Name; exit_code=$Negative.code; expected_diagnostic='[UnequalTerms]'; correctly_rejected=$true }
}
$OwnerAfter = Inventory $Sources
$LibraryAfter = Inventory $Library
$CompilerAfter = (Get-FileHash -Algorithm SHA256 -LiteralPath $Compiler).Hash
$Stable = (($OwnerBefore | ConvertTo-Json -Compress) -ceq ($OwnerAfter | ConvertTo-Json -Compress)) -and (($LibraryBefore | ConvertTo-Json -Compress) -ceq ($LibraryAfter | ConvertTo-Json -Compress)) -and ($CompilerBefore -ceq $CompilerAfter)
if (!$Stable) { throw 'Inputs changed during compilation' }
[ordered]@{
  schema=if ($Module -eq 'GradedBoundaryCoherence') { 'marici.nima.graded-boundary-coherence-formal-audit.v1' } else { 'marici.nima.agda-proof-packet.v1' }
  passed=$true
  module=$Module
  started_at=$Started
  finished_at=[DateTime]::UtcNow.ToString('o')
  command=$Compiler
  args=$Positive.args
  library=$Library
  no_new_window=$true
  ignore_interfaces=$true
  compiler_sha256=$CompilerAfter
  owner_source_inventory_sha256=$OwnerAfter
  library_source_inventory_sha256=$LibraryAfter
  inputs_stable_during_check=$Stable
  checker_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash
  positive_exit_code=$Positive.code
  controls=$Controls
  scope="Fresh safe Cubical Agda check of $Module and its declared rejection controls; theorem statements are in the source module."
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
Write-Output "PASS: fresh $Module compilation and $($Controls.Count) expected compiler rejections."

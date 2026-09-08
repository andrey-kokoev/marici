param(
    [Parameter(Mandatory = $true)] [string] $Executable,
    [Parameter(Mandatory = $true)] [string] $WorkingDirectory,
    [Parameter(Mandatory = $true)] [string[]] $ChildArgument,
    [Parameter(Mandatory = $true)] [string] $StdoutPath,
    [Parameter(Mandatory = $true)] [string] $StderrPath,
    [ValidateRange(1, 86400)] [int] $TimeoutSeconds = 6000
)

$ErrorActionPreference = 'Stop'

Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;

public static class MariciJobObject {
    [StructLayout(LayoutKind.Sequential)]
    public struct IO_COUNTERS {
        public UInt64 ReadOperationCount, WriteOperationCount, OtherOperationCount;
        public UInt64 ReadTransferCount, WriteTransferCount, OtherTransferCount;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct BASIC_LIMIT_INFORMATION {
        public Int64 PerProcessUserTimeLimit, PerJobUserTimeLimit;
        public UInt32 LimitFlags;
        public UIntPtr MinimumWorkingSetSize, MaximumWorkingSetSize;
        public UInt32 ActiveProcessLimit;
        public UIntPtr Affinity;
        public UInt32 PriorityClass, SchedulingClass;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct EXTENDED_LIMIT_INFORMATION {
        public BASIC_LIMIT_INFORMATION BasicLimitInformation;
        public IO_COUNTERS IoInfo;
        public UIntPtr ProcessMemoryLimit, JobMemoryLimit, PeakProcessMemoryUsed, PeakJobMemoryUsed;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode)]
    public static extern IntPtr CreateJobObject(IntPtr attributes, string name);

    [DllImport("kernel32.dll")]
    public static extern bool SetInformationJobObject(
        IntPtr job, int informationClass, IntPtr information, UInt32 informationLength);

    [DllImport("kernel32.dll")]
    public static extern bool AssignProcessToJobObject(IntPtr job, IntPtr process);

    [DllImport("kernel32.dll")]
    public static extern bool CloseHandle(IntPtr handle);
}
'@

$job = [MariciJobObject]::CreateJobObject([IntPtr]::Zero, $null)
if ($job -eq [IntPtr]::Zero) { throw 'CreateJobObject failed' }

$process = $null
$stdoutStream = $null
$stderrStream = $null
$stdoutTask = $null
$stderrTask = $null
try {
    $limits = [MariciJobObject+EXTENDED_LIMIT_INFORMATION]::new()
    # PowerShell returns nested value-type fields by value. Mutate a local copy,
    # then assign it back; direct chained assignment silently leaves flags zero.
    $basicLimits = $limits.BasicLimitInformation
    $basicLimits.LimitFlags = 0x00002000 # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    $limits.BasicLimitInformation = $basicLimits
    $size = [Runtime.InteropServices.Marshal]::SizeOf($limits)
    $buffer = [Runtime.InteropServices.Marshal]::AllocHGlobal($size)
    try {
        [Runtime.InteropServices.Marshal]::StructureToPtr($limits, $buffer, $false)
        if (-not [MariciJobObject]::SetInformationJobObject($job, 9, $buffer, $size)) {
            throw 'SetInformationJobObject failed'
        }
    }
    finally {
        [Runtime.InteropServices.Marshal]::FreeHGlobal($buffer)
    }

    $start = [Diagnostics.ProcessStartInfo]::new()
    $start.FileName = $Executable
    $start.WorkingDirectory = $WorkingDirectory
    $start.UseShellExecute = $false
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    foreach ($argument in $ChildArgument) { [void] $start.ArgumentList.Add($argument) }

    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $start
    if (-not $process.Start()) { throw 'failed to start child process' }
    if (-not [MariciJobObject]::AssignProcessToJobObject($job, $process.Handle)) {
        throw 'AssignProcessToJobObject failed'
    }

    $stdoutStream = [IO.File]::Create($StdoutPath)
    $stderrStream = [IO.File]::Create($StderrPath)
    $stdoutTask = $process.StandardOutput.BaseStream.CopyToAsync($stdoutStream)
    $stderrTask = $process.StandardError.BaseStream.CopyToAsync($stderrStream)
    if (-not $process.WaitForExit($TimeoutSeconds * 1000)) {
        throw "child timeout after $TimeoutSeconds seconds"
    }
    $stdoutTask.GetAwaiter().GetResult()
    $stderrTask.GetAwaiter().GetResult()
    exit $process.ExitCode
}
finally {
    # Closing the job terminates an unfinished child before output-copy tasks
    # and streams are drained and disposed.
    [void] [MariciJobObject]::CloseHandle($job)
    if ($null -ne $stdoutTask) { $stdoutTask.GetAwaiter().GetResult() }
    if ($null -ne $stderrTask) { $stderrTask.GetAwaiter().GetResult() }
    if ($null -ne $stdoutStream) { $stdoutStream.Dispose() }
    if ($null -ne $stderrStream) { $stderrStream.Dispose() }
    if ($null -ne $process) { $process.Dispose() }
}

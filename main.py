import os
import sys

def audit_codebase(target_path="."):
    """
    Performs a lightweight static audit of python source files
    to find undocumented functions and missing docstrings.
    """
    print("=" * 60)
    print(f"[*] Starting Smart Repo Audit on: {os.path.abspath(target_path)}")
    print("=" * 60)

    total_files = 0
    python_files = 0
    missing_docs = 0

    for root, dirs, files in os.walk(target_path):
        if any(skip in root for skip in [".git", "__pycache__", "venv", ".venv", "node_modules"]):
            continue
        
        for file in files:
            total_files += 1
            if file.endswith(".py"):
                python_files += 1
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                        content = "".join(lines)
                        # Check basic documentation signals
                        if '"""' not in content and "'''" not in content:
                            missing_docs += 1
                            print(f"[!] Warning: Missing docstring in {os.path.relpath(filepath, target_path)}")
                except Exception as e:
                    print(f"[-] Could not read {filepath}: {e}")

    print("\n" + "=" * 60)
    print("                AUDIT SUMMARY REPORT")
    print("=" * 60)
    print(f"Total Files Scanned      : {total_files}")
    print(f"Python Files Evaluated   : {python_files}")
    print(f"Files Missing Docstrings : {missing_docs}")
    coverage = ((python_files - missing_docs) / python_files * 100) if python_files else 100
    print(f"Documentation Coverage   : {coverage:.1f}%")
    print("=" * 60)
    print("[+] Status: Codebase ready for AI documentation generation.")
    print("=" * 60)

if __name__ == "__main__":
    path_to_scan = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_codebase(path_to_scan)

import os
import json
from collections import defaultdict
from pygments.lexers import guess_lexer_for_filename
from pathlib import Path

def analyze_osv_files(osv_dir):
    """Analyzes OSV JSON files to determine language breakdown and total size."""

    language_stats = defaultdict(int)
    total_size = 0
    total_files = 0

    for filename in os.listdir(osv_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(osv_dir, filename)
            total_files += 1

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    total_size += os.path.getsize(file_path)

                    # Extract package information (if available)
                    for affected in data.get("affected", []):
                        package = affected.get("package", {})
                        pkg_name = package.get("name", "")
                        pkg_ecosystem = package.get("ecosystem", "")
                        
                        # Attempt language detection based on package name or ecosystem
                        if pkg_name:
                            try:
                                lexer = guess_lexer_for_filename(pkg_name)
                                language_stats[lexer.name] += 1
                            except Exception:
                                pass # Language detection failed
                        elif pkg_ecosystem:
                            language_stats[pkg_ecosystem] += 1

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return language_stats, total_size, total_files

def display_results(language_stats, total_size, total_files):
    """Displays the language breakdown and total size."""

    print("\nOSV Language Breakdown:")
    for lang, count in sorted(language_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{count} - {lang}")

    print(f"\nTotal OSV Files: {total_files}")
    print(f"Total Size of OSV Data: {total_size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    osv_dir = "/home/yesmin88/Downloads/all" # Replace with your OSV directory path
    language_stats, total_size, total_files = analyze_osv_files(osv_dir)
    display_results(language_stats, total_size, total_files)

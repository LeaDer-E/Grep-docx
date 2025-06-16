import os
import re
from docx import Document
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

IGNORED_FILES = {'Search.py', 'requirements.txt'}
IGNORED_DIRS = {'myenv'}


def search_in_docx(file_path: str, pattern: re.Pattern):
    results = []
    try:
        doc = Document(file_path)
    except Exception:
        return results

    for i, para in enumerate(doc.paragraphs, start=1):
        text = para.text
        if pattern.search(text):
            highlighted = pattern.sub(lambda m: f"{Fore.RED}{m.group(0)}{Style.RESET_ALL}", text)
            results.append((i, highlighted))
    return results


def format_result(file_path, hits, cwd):
    relative_path = os.path.relpath(file_path, cwd)
    filename = os.path.basename(file_path)

    print(Fore.BLUE + "\n" + "=" * 100)
    print(Fore.YELLOW + f"🔍  FILE: {Fore.CYAN}{filename}")
    print(Fore.YELLOW + f"📁  FULL PATH: {Fore.WHITE}{file_path}")
    print(Fore.YELLOW + f"📂  RELATIVE PATH: {Fore.WHITE}{relative_path}")
    print(Fore.BLUE + "=" * 100 + Style.RESET_ALL)

    for lineno, line in hits:
        print(f"  {Fore.GREEN}• Line {lineno:>3}:{Style.RESET_ALL} {line}")

    print(Fore.MAGENTA + "-" * 100 + Style.RESET_ALL)


def run_search():
    term = input(Fore.GREEN + '\n🔎 Enter search term (or \\Exit to quit): ' + Style.RESET_ALL).strip()
    if term == '\\Exit':
        return False
    if term == '\\exit':
        return False

    pattern = re.compile(re.escape(term), re.IGNORECASE)
    found = False
    cwd = os.getcwd()

    for root, dirs, files in os.walk(cwd):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for fname in files:
            if fname in IGNORED_FILES or not fname.lower().endswith('.docx'):
                continue

            path = os.path.join(root, fname)
            hits = search_in_docx(path, pattern)
            if hits:
                found = True
                format_result(path, hits, cwd)

    if not found:
        print(Fore.RED + '\n❗ No matches found.' + Style.RESET_ALL)
    return True


def main():
    print(Fore.MAGENTA + '\n📄 DOCX GREP-LIKE SEARCH TOOL' + Style.RESET_ALL)
    print(Fore.CYAN + 'Type \\Exit to quit at any time.' + Style.RESET_ALL)
    while True:
        if not run_search():
            break
    print(Fore.CYAN + '\nGoodbye. 👋' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
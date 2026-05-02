import os
import subprocess

def create_ai_project_structure():
    print("--- Initializing Universal AI Project Structure ---")
    
    # 1. Define Directories
    dirs = [
        ".antigravity/memory",
        ".antigravity/logs",
        ".cursor/rules",
        ".gemini",
        "ai_brain",
        "graphify-out"
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"[+] Created directory: {d}")

    # 2. Define Templates
    templates = {
        "AI_CONTEXT.md": "# Project Context\n\n## Master Entry Point\nThis project is managed by a multi-agent AI system.\n\n**Read `ai_brain/` before starting any work.**",
        "ai_brain/current_task.md": "# Current Task\n\n**Status**: Initializing Project\n**Assignee**: AI Initializer\n\n## Goal\nSet up the project environment and prepare for the first feature.",
        "ai_brain/features_log.md": "# Feature Log\n\n- Project initialized using the Universal AI Structure.",
        "ai_brain/architecture.md": "# System Architecture\n\n```mermaid\ngraph TD\n    A[Start] --> B[Implementation]\n```",
        "ai_brain/constraints.md": "# Project Constraints\n\n1. Do not delete the `.antigravity` or `ai_brain` folders.\n2. Always update the log after every task.",
        ".cursor/rules/project_rules.mdc": "Rule: Always check ai_brain/current_task.md before writing code.",
    }


    for path, content in templates.items():
        with open(path, "w") as f:
            f.write(content)
        print(f"[+] Created template: {path}")

    # 3. Smart Git Protection (Safe Append)
    ignore_list = [
        "\n# AI-Driven Development Folders",
        ".antigravity/",
        "graphify-out/",
        ".gemini/",
        "ai_brain/",
        "init_ai_project.py",
        "structureForNewProject.md",
        "AI_CONTEXT.md",
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".agents/",
        ".claude/",
        ".codex/",
        ".cursor/"
    ]
    
    gitignore_path = ".gitignore"
    existing_content = ""
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            existing_content = f.read()

    with open(gitignore_path, "a") as f:
        for item in ignore_list:
            if item.strip() and item.strip() not in existing_content:
                f.write(item + "\n")
        print(f"[+] Safely updated {gitignore_path} with AI protection rules.")

    # 4. Run Graphify Installations
    print("\n--- Running Universal Graphify Bridge Installation ---")
    platforms = ["antigravity", "gemini", "codex", "cursor", "claude"]
    
    for p in platforms:
        try:
            print(f"[*] Installing Graphify bridge for {p}...")
            # We use 'python -m graphify' to ensure it finds the pip-installed version
            subprocess.run(["python", "-m", "graphify", p, "install"], check=False)
        except Exception as e:
            print(f"[!] Failed to install for {p}: {e}")

    print("\n--- DONE! Project is now AI-Ready ---")
    print("Next step: Run 'python -m graphify update .' to build your knowledge graph.")

if __name__ == "__main__":
    create_ai_project_structure()

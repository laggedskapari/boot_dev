def categorize_file(filename):
    def get_category(extention): return {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Python",
    }.get(extention, "Unknown")

    return get_category(filename[filename.rfind("."):])

def remove_invalid_line(document):
    return "\n".join(filter(lambda: line: not line.startswith('-'), document.split("\n"))

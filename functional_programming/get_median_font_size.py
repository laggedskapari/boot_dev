def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    sorted_sizes = sorted(font_sizes)
    n = len(sorted_sizes)
    if n % 2 == 0:
        return sorted_sizes[n // 2 - 1]
    else:
        return sorted_sizes[n // 2]

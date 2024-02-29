def add_format(default_formats, new_format):
    users_copy = default_formats.copy()
    users_copy[new_format] = True
    return users_copy


def remove_format(default_formats, old_format):
    users_copy = default_formats.copy()
    users_copy[old_format] = False
    return users_copy

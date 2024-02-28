def add_doc(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_docments = documents + (new_doc,)
    return new_docments

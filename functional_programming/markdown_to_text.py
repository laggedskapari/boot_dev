def markdown_to_text(doc_content):
    result = []
    lineList = doc_content.split("\n")
    for word in lineList:
        if word.startswith('#'):
            word = remove_hash_from_word(word)
            result.append(word)
        else:
            word = remove_astrick_from_word(word)
            result.append(word)
    return "\n".join(result)


def remove_hash_from_word(word):
    return word.lstrip('# ')


def remove_astrick_from_word(word):
    return word.strip('*')


cont = '# This is the \n **content**'
print(markdown_to_text(cont))


run_cases = [
    (
        """
# Header 1
This is a **bold statement**
I am #1
This is just plain text. No special markdown.

* This is a list
* lists don't need to change

Well sh*t.
""",
        """
Header 1
This is a bold statement
I am #1
This is just plain text. No special markdown.

* This is a list
* lists don't need to change

Well sh*t.
""",
    )
]

submit_cases = run_cases + [
    (
        """
# Todo List
*Wish* *Boots* *a* *Happy* *Birthday*
Buy a #21 Jersey
* Do my best
""",
        """
Todo List
Wish Boots a Happy Birthday
Buy a #21 Jersey
* Do my best
""",
    ),
    (
        """
# Hash header #

*Italics line*
**Bold line**

## Subheader

* List item
* *Italics list item*
* **Bold list item**
""",
        """
Hash header #

Italics line
Bold line

Subheader

* List item
* Italics list item
* Bold list item
""",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:")
    print(f'"{input1}"')
    print(f"Expecting:")
    print(f'"{expected_output}"')
    result = markdown_to_text(input1)
    print(f"Actual:")
    print(f'"{result}"')
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

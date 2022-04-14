from array_stack import ArrayStack


def is_matched_html(raw):
    Stack = ArrayStack()

    tag_start_pointer = raw.find('<')

    while tag_start_pointer != -1:
        tag_end_pointer = raw.find('>', tag_start_pointer + 1)
        if tag_end_pointer == -1:
            return False
        tag = raw[tag_start_pointer + 1:tag_end_pointer]
        if not tag.startswith('/'):
            Stack.push(tag)
        else:
            if Stack.is_empty():
                return False
            if tag[1:] != Stack.pop():
                return False
        tag_start_pointer = raw.find('<', tag_end_pointer + 1)

    return Stack.is_empty()


raw_html = """
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
"""

raw_html_1 = """
<ol>
<li> Will the salesman die? </li>
What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
"""

print(is_matched_html(raw_html))
print(is_matched_html(raw_html_1))

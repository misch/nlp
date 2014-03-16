import re

def all_tags_closed():

    # regular expressions for start and end tags
    start_tag_expression = re.compile("<([^/?].*?)[ .*?>|>]")
    end_tag_expression =  re.compile("</(.*?)>")

    f = open('input_ex2_1.txt','r')

    # grab all the start and end tags
    start_tags = []
    end_tags = []
    for line in f:
        start_match = start_tag_expression.findall(line)
        end_match = end_tag_expression.findall(line)
        if start_match:
            start_tags.append(start_match)
        if end_match:
            end_tags.append(end_match)
    f.close()

    # flatten lists of lists
    end_tags = [value for sub_list in end_tags for value in sub_list]
    start_tags = [value for sub_list in start_tags for value in sub_list]

    end_tags.sort()
    start_tags.sort()

    if len(start_tags) != len(end_tags):
        return False

    tags_closed = True
    for i in range(1,len(start_tags)+1):
        current = start_tags.pop()
        if current != end_tags.pop():
            tags_closed = False

    return tags_closed

def tags_correctly_nested():
    #TODO
    return 0

def has_root():
    #TODO
    return 0

def attribute_value_is_quoted():
    #TODO
    return 0

def elements_correctly_named():
    #TODO
    return 0


# --- Script --- #

if all_tags_closed():
    print("All tags are closed!")
else:
    print("Not all tags are closed...")
#!/usr/bin/python
import re

def all_tags_closed(filename):

    # regular expressions for start and end tags
    start_tag_expression = re.compile("<([^/?].*?)[ .*?>|>]")
    end_tag_expression =  re.compile("</(.*?)>")

    f = open(filename,'r')

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

def tags_correctly_nested(filename):
     # regular expressions for start and end tags
    start_tag_expression = re.compile("<([^/?].*?)[ .*?>|>]")
    end_tag_expression =  re.compile("</(.*?)>")

    f = open(filename,'r')

    expected_end_tags = []
    correctly_nested = True
    for line in f:
        start_match = start_tag_expression.findall(line)
        end_match = end_tag_expression.findall(line)
        if start_match:
            for start_tag in start_match:
                expected_end_tags.append(start_tag)
        if end_match:
            if not expected_end_tags:
                return False
            end_match.reverse() # if multiple tags are opened and closed on one line, then
                                # the start tags are all added to the "stack" before they
                                # get compared to the end tags. Therefore, the end tags of one line
                                # have to be considered in reverse order.
            for end_tag in end_match:
                if end_tag != expected_end_tags.pop():
                    correctly_nested = False
    f.close()

    return correctly_nested

def has_root(filename):
        # regular expressions for start and end tags
    start_tag_expression = re.compile("<([^/?].*?)[ .*?>|>]")
    end_tag_expression =  re.compile("</(.*?)>")

    f = open(filename,'r')

    root_open = 0
    # Get <root>
    for line in f:
        start_match = start_tag_expression.findall(line)

        if start_match:
            if root_open == 0:
                root_open = start_match[0]
            elif root_open == start_match[0]: # The root element cannot occur more than once in the tree
                return False

    # Get </root>
    # Assumes that there are no empty newlines at the end of the file
    for line in f:
        pass
    last = line
    f.close()
    end_match = end_tag_expression.findall(last)
    if end_match:
        root_close = end_match.pop()
        return root_open == root_close
    else:
        return False

def attribute_value_is_quoted(filename):

    # Regular expression to match tags with attributes.
    # Match-group 1: tag name
    # Match-group 2: attribute name
    # Match-group 3: attribute value
    tags_with_attributes_expression = re.compile("<([^/?][^>]*?) (.*?)=(.*?)>")

    value_quoted = True
    f = open(filename,'r')

    for line in f:
        match = tags_with_attributes_expression.findall(line) # a list of 3-tuples (tag,attribute,value)
        if match:
            for element in match:
                attr_value = element[2]
                if attr_value[0] != '"' or attr_value[-1] != '"':
                    value_quoted = False
    f.close()
    return value_quoted

def elements_correctly_named(filename):
    # Regular expression to match tags with attributes.
    tags_with_attributes_expression = re.compile("<([^/?][^>]*?) (.*?)=(.*?)>")
    tag_expression = re.compile("</?(.+?)[ .*?>|>]")

    correct_name_expression = re.compile("^^([0-9]|,|.|:|;|xml)[-_.:0-9a-z]+$",re.IGNORECASE)

    correct_names = True
    f = open(filename,'r')

    for line in f:
        match = tag_expression.findall(line)
        if match:
            for element in match:
                correct = correct_name_expression.match(element)
                if not correct:
                    correct_names = False
    f.close()
    return correct_names

def check_xml_file(filename):
    invalid_xml= False
    error_message = ''
    if not all_tags_closed(filename):
        error_message += "\tNot all tags are closed!\n"
        invalid_xml = True

    if not tags_correctly_nested(filename):
        error_message += "\tThe tags are not correctly nested!\n"
        invalid_xml = True

    if not has_root(filename):
        error_message += "\tNo root element!\n"
        invalid_xml = True

    if not attribute_value_is_quoted(filename):
        error_message += "\tQuotes missing in attribute value!\n"
        invalid_xml = True

    if not elements_correctly_named(filename):
        error_message += "\tElements are not correctly named.\n"
        invalid_xml = True

    if invalid_xml:
        print("File "+ filename + ": NO. Errors: \n" + error_message)
    else:
        print("File " + filename + ": YES.")


# --- Script --- #

check_xml_file('input_ex2_1.txt')
check_xml_file('input_ex2_2.txt')
check_xml_file('input_ex2_3.txt')
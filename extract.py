import re


def clean_text(input_text):
    input_text = input_text.replace("|", "")
    photo_regex = re.compile(re.escape('photo'), re.IGNORECASE)
    is_regex = re.compile(re.escape('is'), re.IGNORECASE)
    available_regex = re.compile(re.escape('available'), re.IGNORECASE)
    input_text = photo_regex.sub("", input_text)
    input_text = is_regex.sub("", input_text)
    input_text = available_regex.sub("", input_text)

    return input_text


def filter_field(field):
    field = field.replace("\r", "").replace("\n", "")
    index = field.find(":")

    if index == -1:
        return field

    return field[index + 1:]


def extract(input_text):
    input_text = clean_text(input_text)

    index_box_id = input_text.find("\n")
    index_voter_id = input_text.find("\n", index_box_id + 1)
    index_name = input_text.find("नाव", 0)

    index_fathers_name = input_text.find("वडीलांचे नाव", index_name + 1)
    index_husband_name = input_text.find("पतीचे नाव", index_name + 1)
    index_mothers_name = input_text.find("आईचे नाव", index_name + 1)
    index_parent_name = min(
        index_fathers_name if index_fathers_name != -1 else 99999999999999,
        index_husband_name if index_husband_name != -1 else 99999999999999,
        index_mothers_name if index_mothers_name != -1 else 99999999999999)

    house_number_index = input_text.find("घर क्रमांक", index_parent_name + 1)
    age_index = input_text.find("वय", house_number_index + 1)
    sex_index = input_text.find("लिंग", index_parent_name + 1)

    box_id_field = filter_field(input_text[0:index_box_id])
    voter_id_field = filter_field(input_text[index_box_id:index_voter_id])
    name_field = filter_field(input_text[index_name:index_parent_name])
    parent_name_field = filter_field(input_text[index_parent_name:house_number_index])
    house_number_field = filter_field(input_text[house_number_index:age_index])
    age_field = filter_field(input_text[age_index:sex_index])
    sex_field = filter_field(input_text[sex_index:])

    print(
        box_id_field + "," + voter_id_field + "," + name_field + "," + parent_name_field + "," + house_number_field + "," + age_field + "," + sex_field)
    return box_id_field + "," + voter_id_field + "," + name_field + "," + parent_name_field + "," + house_number_field + "," + age_field + "," + sex_field + "\n"

import re


from bs4 import BeautifulSoup
from flask.helpers import get_debug_flag


def apply_processors_chain(to_string):
    for process in (
                  rem_extra_whitespaces,
                  rem_extra_spaces_before_punctuation,
                  make_angle_quote_marks,
                  change_hyphens_by_sh_dashes_in_phones,
                  change_hyphens_by_sintac_dashes,
                  bind_number_with_follower,
                  bind_short_with_follower,
                  # here is a place for extra processors
                  ):
        to_string = process(to_string)
    return to_string


def bind_number_with_follower(in_str):
    return re.sub(r'(\d+)( )([^0-9]+)', r'\1{}\3'.format(get_nbsp()), in_str)


def bind_short_with_follower(in_str):
    return re.sub(r'(\b\w{1,3})( )(\b)', r'\1{}\3'.format(get_nbsp()), in_str)


def make_angle_quote_marks(in_str):
    in_str = re.sub(r'([\'\"])(\b)', r'«\2', in_str)
    return re.sub(r'(\b)([\'\"])', r'\1»', in_str)


def change_hyphens_by_sh_dashes_in_phones(in_str):
    ndash = '–'
    return re.sub(r'(\d)(-)', r'\1{}'.format(ndash), in_str)


def change_hyphens_by_sintac_dashes(in_str):
    mdash = '—'
    return re.sub(r'( )(-)', r'\1{}'.format(mdash), in_str)


def get_nbsp():
    if get_debug_flag():
        return '+'
    return '\u00A0'


def prepare_text(in_html):
    soup = BeautifulSoup(in_html, 'html.parser')
    for to_string in soup.find_all(string=True):
        new_string = apply_processors_chain(to_string)
        to_string.replace_with(new_string)
    return soup


def rem_extra_whitespaces(in_str):
    return re.sub(r'\s+', ' ', in_str).strip()


def rem_extra_spaces_before_punctuation(in_str):
    return re.sub(r'([\w\'\"])(\s)([\.,;:!?]{1,3})', r'\1\3', in_str)

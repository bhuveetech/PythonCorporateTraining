""" This module is used to practice comments """
import argparse


# ====================== Block comment Example =====================
# The main function will parse arguments via the parser variable.  These
# arguments will be defined by the user on the console.  This will pass
# the word argument the user wants to parse along with the filename the
# user wants to use, and also provide help text if the user does not
# correctly pass the arguments.
#
# Add extra comment
def main():
    parser = argparse.ArgumentParser()      # Inline comment Create argparser Object
    parser.add_argument(
      "word",
      help="the word to be searched for in the text file."
    )
    parser.add_argument(
      "filename",
      help="the path to the text file to be searched through"
    )


# ================== Documentation string Example=================== #
def get_db_conn(host_name, db, user, db_pass):
    """
    Get a db connection with given host.
    if no connection exist, thrown an exception
    :param host_name: hostname
    :param db: database name
    :param user: database user
    :param db_pass: database password
    :return:
    """
    pass

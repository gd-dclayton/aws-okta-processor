from __future__ import print_function

from .base import Base


class Delete(Base):
    """
    Usage:
      delete --organization=<okta_organization> --user=<user_name> [--key=<key>]

    Options:
      -u <user_name> --user=<user_name>                          Okta user name.
      -o <okta_organization> --organization=<okta_organization>  Okta organization domain.
      -k <key> --key=<key>                                       Key used for generating and accessing cache.
    """  # noqa

    def execute(self):
        pass

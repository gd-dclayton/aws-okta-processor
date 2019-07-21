from __future__ import print_function

from .base import Base


class Delete(Base):
    """
    Usage:
      delete --name=<profile_name>

    Options:
      -n <profile_name> --name=<profile_name>    Name to store profile under.
    """  # noqa

    def execute(self):
        pass

"""The token_operations command."""

from __future__ import print_function

from .base import Base


class Create(Base):
    """
    Usage:
      create --organization=<okta_organization> --user=<user_name> --name=<profile_name>
             [--duration=<duration_seconds>]
             [--silent]

    Options:
      -u <user_name> --user=<user_name>                          Okta user name.
      -o <okta_organization> --organization=<okta_organization>  Okta organization domain.
      -d <duration_seconds> --duration=<duration_seconds>        Duration of role session [default: 3600].
      -n <profile_name> --name=<profile_name>                    Name to store profile under.
      -s --silent                                                Run silently.
    """  # noqa

    def execute(self):
        pass

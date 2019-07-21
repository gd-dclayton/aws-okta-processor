from docopt import docopt

from ..base import get_configuration


class Base:
    def __init__(self, command_options):
        self.options = docopt(
            self.__doc__,
            argv=command_options
        )

        self.configuration = get_configuration(
            options=self.options
        )

    def execute(self):
        raise NotImplementedError(
            'You must implement the execute() method yourself!'
        )

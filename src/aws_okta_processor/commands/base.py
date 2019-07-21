import os

from docopt import docopt


CONFIG_MAP = {
            "--environment": "AWS_OKTA_ENVIRONMENT",
            "--user": "AWS_OKTA_USER",
            "--pass": "AWS_OKTA_PASS",
            "--organization": "AWS_OKTA_ORGANIZATION",
            "--application": "AWS_OKTA_APPLICATION",
            "--role": "AWS_OKTA_ROLE",
            "--duration": "AWS_OKTA_DURATION",
            "--key": "AWS_OKTA_KEY",
            "--factor": "AWS_OKTA_FACTOR",
            "--silent": "AWS_OKTA_SILENT"
        }


class Base:
    def __init__(self, command_options):
        self.options = docopt(
            self.__doc__,
            argv=command_options,
            options_first=True
        )

    def execute(self):
        raise NotImplementedError(
            'You must implement the execute() method yourself!'
        )


def get_configuration(options=None):
    configuration = {}

    for param, var in CONFIG_MAP.items():
        if param not in options:
            configuration[var] = None
            continue

        if options[param]:
            configuration[var] = options[param]

        if var not in configuration.keys():
            if var in os.environ:
                configuration[var] = os.environ[var]
            else:
                configuration[var] = None

    return configuration

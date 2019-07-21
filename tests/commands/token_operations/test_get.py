from test_base import TestBase


from aws_okta_processor.commands.token_operations import Get


class TestGet(TestBase):
    def test_get_pass_config(self):
        self.OPTIONS.extend(["-p", "user_pass_two"])
        authenticate = Get(self.OPTIONS)
        assert authenticate.get_pass() == "user_pass_two"

    def test_get_key_dict(self):
        authenticate = Get(self.OPTIONS)
        key_dict = authenticate.get_key_dict()

        self.assertEqual(
            key_dict,
            {
                "Organization": self.OPTIONS[3],
                "User": self.OPTIONS[1],
                "Key": self.OPTIONS[5],
            }
        )

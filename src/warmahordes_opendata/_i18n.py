from importlib import resources
import os

import oslo_i18n

DOMAIN = "warmahordes_opendata"

oslo_i18n.enable_lazy()

os.environ[
    oslo_i18n._locale.get_locale_dir_variable_name(__package__)
] = str(os.path.join(resources.files(__package__), "locale"))

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

_ = _translators.primary

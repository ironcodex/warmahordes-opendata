from importlib import resources
import os

import oslo_i18n

oslo_i18n.enable_lazy()

os.environ[
    oslo_i18n._locale.get_locale_dir_variable_name(__package__)
] = str(os.path.join(resources.files(__package__), "locale"))

_translators = oslo_i18n.TranslatorFactory(domain=__package__)

_ = _translators.primary


def get_available_languages():
    return oslo_i18n.get_available_languages(__package__)


def translate(message, locale):
    if type(message) == str:
        message = _(message)

    return oslo_i18n.translate(message, locale)

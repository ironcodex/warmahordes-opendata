#    Copyright 2021 IronCodex
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from importlib import resources
import os

import oslo_i18n

oslo_i18n.enable_lazy()

os.environ[oslo_i18n._locale.get_locale_dir_variable_name(__package__)] = str(
    os.path.join(resources.files(__package__), "locale")
)

_translators = oslo_i18n.TranslatorFactory(domain=__package__)

_ = _translators.primary


def get_available_languages():
    return oslo_i18n.get_available_languages(__package__)


def translate(message, locale):
    if type(message) == str:
        message = _(message)

    return oslo_i18n.translate(message, locale)

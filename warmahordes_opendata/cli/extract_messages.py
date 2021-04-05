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

import textwrap

from warmahordes_opendata import base
from warmahordes_opendata.rules import Rule  # noqa


header = """# Translations template for warmahordes_opendata.
# Copyright (C) 2021 Iron Codex
# This file is distributed under the same license as the
# warmahordes_opendata project.
#
#, fuzzy
msgid ""
msgstr ""
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"""

rules = base.load_dir("data/rules")


def print_group(group, order=None):
    if order is None:
        order = rules[group].keys()
    else:
        order += [rule for rule in rules[group].keys() if rule not in order]

    print(f"# Rules - {group}\n")

    for rule in order:
        print_rule(rules[group][rule])


def print_rule(rule):
    title = rule.title.replace("\\'", "'")
    desc = rule.description.replace('"', '\\"').replace("\\'", "'")

    print(f'msgid "{title}"')
    print('msgstr ""\n')

    if len(desc) < 74:
        print(f'msgid "{repr(desc)[1:-1]}"')
    else:
        print('msgid ""')
        desc = desc.replace("\n", "\\n@@")
        parts = desc.split("@@")
        for part in parts:
            lines = textwrap.wrap(
                part, 73, break_long_words=False, drop_whitespace=False
            )
            for line in lines:
                print(f'"{line}"')

    print('msgstr ""\n')


def main():
    print(header)

    for group in rules.keys():
        print_group(group)


if __name__ == "__main__":
    main()

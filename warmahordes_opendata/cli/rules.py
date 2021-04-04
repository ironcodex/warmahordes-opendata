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

import sys

from warmahordes_opendata.rules import Rule


def main():
    query = " ".join(sys.argv[1:])
    rules = Rule.find(query)

    if len(rules) == 0:
        print("No rules found where the name includes '{query}'")
    elif len(rules) == 1:
        print(f"\n{rules[0].title}\n")
        print(rules[0].description)
    else:
        for rule in rules:
            print(rule.title)


if __name__ == "__main__":
    main()

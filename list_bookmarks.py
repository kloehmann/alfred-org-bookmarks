#!/usr/bin/env python3
import json
import re
import os
from lib import orgparse as org


BOOKMARKS_FILE = os.getenv("bookmarksfile")
LINK_PATTERN = re.compile("\\[\\[(.*)\\]\\[(.*)\\]\\]")


if __name__ == "__main__":
    json_data = {"items": []}
    base = org.load(BOOKMARKS_FILE)

    get_path = (
        lambda node: node.get_heading()
        if node.get_parent() == base
        else get_path(node.get_parent()) + "/" + node.get_heading()
    )

    for node in base[1:]:
        raw_node = node.get_heading(format="raw")
        pattern_match = LINK_PATTERN.match(raw_node)
        if pattern_match:
            link_target = pattern_match.group(1)
            json_data["items"].append({"title": get_path(node), "arg": link_target})

    print(json.dumps(json_data))

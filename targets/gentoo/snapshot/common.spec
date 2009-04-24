[section metro]

# This defines what internal Metro class is used to build this target
class: snapshot

[section target]

type: repository-image
name: $[portage/name]-$[target/version]

[section path/mirror]

snapshot: $[:snapshot/subpath]/$[portage/name]-$[target/version].tar.bz2
# "current" symlink:
link: $[:snapshot/subpath]/$[portage/name]-current.tar.bz2
link/dest: $[portage/name]-$[target/version].tar.bz2

[section trigger]

ok/run: [
#!/bin/bash
# CREATE current symlink for the snapshot
rm -f $[path/mirror/link]
ln -s $[path/mirror/link/dest] $[path/mirror/link] || exit 3
]



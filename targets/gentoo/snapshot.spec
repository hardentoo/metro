[collect ./snapshot/common.spec]

run: [
#!/bin/bash
	rsync -a --delete --exclude /packages/ --exclude /distfiles/ --exclude /local/ --exclude CVS/ --exclude /.git/ $[rsync/path]/ $[path/work]/portage/ || exit 1
	tar -cjf $[path/mirror/snapshot] -C $[path/work] portage
	if [ $? -ne 0 ]
	then
		rm -f $[path/mirror/snapshot]
		exit 1
	fi
]

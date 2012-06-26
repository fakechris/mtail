mtail
=====

tail multiple files from local and remote ssh servers

#### Dependencies:

* python-gflags
* ssh
* tailer

#### Installation:

	easy_install python-gflags ssh tailer
    python setup.py install

#### usage:

	mtail --files file:///var/log/syslog,ssh://user:pass@host:port/var/log/syslog,ssh://user1@host1/var/log/syslog
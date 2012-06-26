#!/usr/bin/env python

from distutils.core import setup

def main():
    setup(
        name = 'mtail',
        packages=['mtail'],
        version = open('VERSION.txt').read().strip(),
        author='Chris Song',
        author_email='fakechris@gmail.com',
        url='http://github.com/fakechris/mtail',
        download_url='http://github.com/fakechris/mtail',
        license='MIT',
        keywords=['tail', 'ssh', 'multiple'],
        description='Tail multiple files from local and remote ssh hosts.',
        long_description=open('README.md').read(),
        scripts = ['mtail/mtail'],
        install_requires = ["tailer", "ssh", "python-gflags"],
        classifiers = [
            "Programming Language :: Python",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Operating System :: POSIX",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            'Topic :: System :: Logging',
            'Topic :: Text Processing',
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: System Shells",
            "Topic :: System :: Systems Administration",
        ],
    )

if __name__ == '__main__':
    main()

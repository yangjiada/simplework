#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
from setuptools import setup, find_packages
from datetime import date
import os

# 定义项目因变量
NAME = "simplework"
GITHUB_USERNAME = "yangjiada"

# 自动生成设置参数
try:
    SHORT_DESCRIPTION = __import__(NAME).__short_description__ # GitHub Short Description
except:
    print("'__short_description__' not found in '%s.__init__.py'!" % NAME)
    SHORT_DESCRIPTION = "No short description!"


try:
    LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
except:
    LONG_DESCRIPTION = "No long description!"


VERSION = __import__(NAME).__version__
AUTHOR = "Jan Yang"
AUTHOR_EMAIL = "yang.jiada@foxmail.com"
MAINTAINER = "Jan Yang"
MAINTAINER_EMAIL = "yang.jiada@foxmail.com"

# Include all sub packages in package directory
# 包括在包目录下的所有包
PACKAGES = [NAME] + ["%s.%s" % (NAME, i) for i in find_packages(NAME)]
# Include everything in package directory
# 包括在包目录里的一切
INCLUDE_PACKAGE_DATA = True
PACKAGE_DATA = {
    "": ["*.*"],
}


# The project directory name is the GitHub repository name
# 项目目录名称是GitHub库名称
repository_name = os.path.basename(os.getcwd())

# Project Url
# 项目URL
URL = "https://github.com/{0}/{1}".format(GITHUB_USERNAME, repository_name)
# Use todays date as GitHub release tag
# 使用今天的日期作为GitHub版本标记
github_release_tag = str(date.today())
# Source code download url
# 源码下载地址
DOWNLOAD_URL = "https://github.com/{0}/{1}".format(
    GITHUB_USERNAME, repository_name)

try:
    LICENSE = __import__(NAME).__license__
except:
    print("'__license__' not found in '%s.__init__.py'!" % NAME)
    LICENSE = ""

PLATFORMS = ["Windows", "MacOS", "Unix"]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
]

try:
    f = open("requirements.txt", "rb")
    REQUIRES = [i.strip() for i in f.read().decode("utf-8").split("\n")]
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    packages=PACKAGES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    package_data=PACKAGE_DATA,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    platforms=PLATFORMS,
    license=LICENSE,
    install_requires=REQUIRES,
)

"""
Appendix
--------
::
Frequent used classifiers List = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Development Status :: 6 - Mature",
    "Development Status :: 7 - Inactive",
    "Intended Audience :: Customer Service",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Healthcare Industry",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Legal Industry",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Religion",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",
    "License :: OSI Approved :: BSD License",
    "License :: OSI Approved :: MIT License",
    "License :: OSI Approved :: Apache Software License",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Natural Language :: English",
    "Natural Language :: Chinese (Simplified)",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",

    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3 :: Only",
]
"""

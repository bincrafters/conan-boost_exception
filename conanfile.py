#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostExceptionConan(base.BoostBaseConan):
    name = "boost_exception"
    url = "https://github.com/bincrafters/conan-boost_exception"
    lib_short_names = ["exception"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits"
    ]

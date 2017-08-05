from conans import ConanFile, tools, os

class BoostExceptionConan(ConanFile):
    name = "Boost.Exception"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/exception"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "exception"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing",\
                      "Boost.Tuple/1.64.0@bincrafters/testing",\
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      #assert1 config0 core2 smart_ptr4 throw_exception2 tuple4 type_traits3

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()
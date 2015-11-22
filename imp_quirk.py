
import imp

#
# If you set a breakpoint at find_module in import.c, you see that the
# sys.meta_path is completely skipped, thus it won't find testpkg.foo
#
#

print '= testpkg import'
import testpkg
print '= testpkg is', testpkg
foo = imp.find_module('foo', testpkg.__path__)
print '= foo is', foo

# Include these so pyinstaller grabs them
print '======================='
import testpkg
import testpkg.foo

import pkgutil
import os
os.environ['FOO'] = 'hm'

loader = pkgutil.get_loader('testpkg.foo')
print 'loader for foo:', loader


# Include these so pyinstaller grabs them
print '======================='
import testpkg
import testpkg.foo

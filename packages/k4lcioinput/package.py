
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class K4lcioinput(CMakePackage, Key4hepPackage):
    """LCIO reader based on PODIO and EDM4hep"""
    homepage = "https://github.com/mirguest/LCIOInput"
    url      = "https://github.com/mirguest/LCIOInput/archive/v0.1.0.tar.gz"
    git      = "https://github.com/mirguest/LCIOInput.git"

    maintainers = ['mirguest']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')


    depends_on('k4lcioreader')
    depends_on('k4fwcore@0.2.0')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
            args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

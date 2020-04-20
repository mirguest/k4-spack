from spack import *
from spack.package import PackageBase

class Key4hepStack(PackageBase):
    """Dummy package to install the Key4hep software development environment."""

    phases = ['build', 'install']
    build_system_class = 'BundlePackage'

    homepage = 'https://cern.ch/key4hep'

    version('0.1')
    version('nightly')

    depends_on('podio@master', when="@nightly")
    depends_on('edm4hep@master', when="@nightly")
    depends_on('K4fwcore@master', when="@nightly")
    depends_on('guinea-pig@master', when="@nightly")
    depends_on('dd4hep@master', when="@nightly")

    depends_on("podio@v00-10", when="@0.1")
    depends_on("edm4hep@v00-01", when="@0.1")
    depends_on("K4fwcore@v00-01", when="@0.1")
    depends_on('guinea-pig@v1.2.2rc', when="@0.1")
    depends_on("dd4hepv01-11-02", when"@0.1")


    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        pass

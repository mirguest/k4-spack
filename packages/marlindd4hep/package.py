# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Marlindd4hep(CMakePackage):
    """Provides one processor to initialize a DD4hep detector geometry from a compact file for a Marlin job."""

    url      = "https://github.com/iLCSoft/MarlinDD4hep/archive/v00-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.6', sha256='1cf8eb03bbdf6da8fbf277d8168d97f77e1675850a7e66d0e9f90684e3a2f077')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('dd4hep')

    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define('INSTALL_DOC', False))
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinDD4hep.so.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
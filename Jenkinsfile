// Obtain files from source control system.
if (utils.scm_checkout()) return

matrix_os = ["linux"]
matrix_python = ["3.5"]
matrix = []

  for (os in matrix_os) {
    for (python_ver in matrix_python) {
      // Define each build configuration, copying and overriding values as necessary.
      env_py = "_python_${python_ver}".replace(".", "_")
      bc = new BuildConfig()
      bc.nodetype = os
      bc.name = "debug-${os}-${env_py}"
      bc.build_cmds = ["ls"]
      bc.test_cmds = ["ls", "sed -i 's/file=\".*\"//g;' results.xml"]
      matrix += bc
    }
  }
  utils.run(matrix)

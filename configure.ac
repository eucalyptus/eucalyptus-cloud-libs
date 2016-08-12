m4_define([base_version], [4.4])
m4_define([git_revision],
          m4_esyscmd([git rev-parse HEAD | cut -c-7 | tr -d '\n']))
m4_define([git_commit_count],
          m4_esyscmd([git log --pretty=format: HEAD | wc -l | tr -d '\n']))
m4_define([date], m4_esyscmd([date +%Y%m%d | tr -d '\n']))
m4_define([fullversion], [base_version-git_commit_count-date[git]git_revision])

AC_INIT([eucalyptus-java-deps], [fullversion])

AC_CONFIG_FILES([
    Makefile
])
AC_OUTPUT

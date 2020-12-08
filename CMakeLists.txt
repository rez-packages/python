include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(PROJECT_VERSION $ENV{REZ_BUILD_PROJECT_VERSION})

file(MAKE_DIRECTORY ${CMAKE_INSTALL_PREFIX})

set(URL https://www.python.org/ftp/python/${PROJECT_VERSION}/Python-${PROJECT_VERSION}.tgz)
set(ARCHIVE_REL libs/python-${PROJECT_VERSION}.tar.gz)

set(CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-optimizations --enable-unicode=ucs4 LDFLAGS=-Wl,-rpath,'$$ORIGIN/../lib/')
message(STATUS "Configure Command: ${CONFIGURE_COMMAND}")

if(NOT EXISTS $ENV{REZ_REPO_PAYLOAD_DIR}/${ARCHIVE_REL})
    file(DOWNLOAD ${URL} $ENV{REZ_REPO_PAYLOAD_DIR}/${ARCHIVE_REL})
endif()

if(${REZ_BUILD_INSTALL})
	set(INSTALL_COMMAND make -j${REZ_BUILD_THREAD_COUNT} install)
else()
	set(INSTALL_COMMAND ${CMAKE_COMMAND} -E echo "install skipped")
endif()

rez_set_archive(
	ARCHIVE
	${ARCHIVE_REL}
	${URL}
)

ExternalProject_Add(
	${PROJECT_NAME}
	URL ${ARCHIVE}
	UPDATE_COMMAND ""
	CONFIGURE_COMMAND ${CONFIGURE_COMMAND}
	BUILD_IN_SOURCE 1
	BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
	INSTALL_COMMAND ${INSTALL_COMMAND}
)


install(CODE "message(STATUS \"Python-${PROJECT_VERSION} installed.\")")

ROOT_PATH=../src
RPM_ROOT_DIR=$(ROOT_PATH)/../rpm
RPM_MACRO=--macros=/usr/lib/rpm/macros:/usr/lib/rpm/suse_macros:$(RPM_ROOT_DIR)/rpmmacros.spec

SPEC_TEMPLATE_BIN=$(RPM_ROOT_DIR)/SPECS/hello-template-bin.spec

all: rpm

rpm:
	rpmbuild --bb $(RPM_MACRO) --rcfile /usr/lib/rpm/rpmrc:$(RPM_RC) \
	  $(SPEC_TEMPLATE_BIN)

clean:
	find RPMS -name '*.rpm' -exec rm -f {} ';'

clobber: clean
	rm -rf BUILD/*
	rm -rf tmp/*

# hello-world-rpm
A starting point to build RPMs from source code using make and rpmbuild.

Simply run `cd ./rpm && make rpm`. The RPMs can be found in the new `./rpm/RPMS` folder:

```bash
:~/hello-world-rpm/rpm> find RPMS
RPMS
RPMS/x86_64
RPMS/x86_64/hello-0.1-1.x86_64.rpm
RPMS/x86_64/hello-test-0.1-1.x86_64.rpm
```

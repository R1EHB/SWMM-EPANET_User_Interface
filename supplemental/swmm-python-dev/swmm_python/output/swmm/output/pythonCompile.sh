#!/bin/bash

# this shouldn't be used; use setup.py instead.


gcc -shared -o output.so    -I/usr/include/python3.8  -Wno-unused-result -Wsign-compare  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches   -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -D_GNU_SOURCE -fPIC -fwrapv  -DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches   -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -D_GNU_SOURCE -fPIC -fwrapv -L/usr/lib64 -lpython3.8 -lcrypt -lpthread -ldl  -lutil -lm output_wrap.c




	      

#!/usr/bin/env bash

MB_JAVA_BIN=${MB_JAVA_BIN:-/usr/bin/java}
MB_JAVA_OPTS=${MB_JAVA_OPTS:-}

${MB_JAVA_BIN} ${MB_JAVA_OPTS} -jar /var/lib/metabase/metabase.jar $@


# FROM rhscl/python-34-rhel7:latest
# FROM centos/python-34-centos7
MAINTAINER johnedstone <johnedstone@gmail.com>
USER root
ADD oracle*.rpm /tmp/
RUN  yum --nogpgcheck localinstall -y \
    /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm  \
    /tmp/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm \
    /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm \
    &&  yum --enablerepo=\* clean all
RUN /bin/rm /tmp/oracle* && \
    echo "/usr/lib/oracle/12.1/client64/lib/" > /etc/ld.so.conf.d/oracle.conf \
    && ldconfig \
    && ln -s /usr/bin/sqlplus64 /usr/bin/sqlplus
USER 1001

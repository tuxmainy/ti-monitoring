FROM python:3

# set default environments
ENV DATA_FILE=/data/data.hdf5
ENV BASE_URL=http://example.org
ENV NOTIFY=false
ENV NOTIFY_CONF=/data/notifications.json
ENV SMTP_HOST=example.org
ENV SMTP_PORT=587
ENV SMTP_USER=example
ENV SMTP_PASS=secret
ENV SMTP_FROM=foo@example.org

# install python packages
RUN pip3 install pandas h5py requests tzlocal dash uwsgi

# create data dir
RUN mkdir /data

# copy git clone into container
WORKDIR /ti-monitoring
COPY . .

# switch to non priv user
RUN chown -R www-data /ti-monitoring /data
USER www-data

# run webapp on startup
CMD ["uwsgi", "--socket=[::]:8000", "--protocol=http", "--wsgi=wsgi"]

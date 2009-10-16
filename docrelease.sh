#!/bin/bash
make html && rm -rf /opt/trackers/evasionproject/apidocs/* && \
  cp -R build/html/* /opt/trackers/evasionproject/apidocs && \
  cp -R images /opt/trackers/evasionproject/apidocs && \
  cp /opt/trackers/evasionproject/apidocs/evasionproject.html /opt/trackers/evasionproject/apidocs/index.html 

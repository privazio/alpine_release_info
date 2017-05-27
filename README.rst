Alpine Linux Release Info
=========================

Command line utility to query Alpine Linux's distribution tree.

The targeted use case is the continuous delivery of products based on Alpine Linux such as Docker Images.

This script will deliver the latest release given branch, architecture, flavor, etc. There are many other parameters
that can be queried such as: url to download, sha512, gpg signature, etc.

Demo
====

.. image:: https://raw.githubusercontent.com/privazio/alpine_release_info/master/doc/demo.gif


Usage
=====

To install the latest release of this utility:

.. code::

  pip install alpine_release_info


For help on the available parameters:

.. code::

  alpine_release_info -h

To query the download url for the latest release on the v3.5 branch for armhf architecture and minirootfs flavor:

.. code::

  alpine_release_info -a armhf -b v3.5 -f alpine-minirootfs -q url

# Heimdallr
A utility which creates administrative bridges between physical/virtual systems, utilities and services to bring them together.

## Goal

A typical domain will have multiple servers (both physical and
virtual), running some set of software servers and utilities, which we
will refer to collectively as "services".  Often, these services
depend on each other, and information needs to be transferred between
them, but either the systems do not incorporate the ability to query
another because of multiple implementation options, or the information
is stored statically to reduce issues with service outages. In
addition, sometimes none of these systems stores the information for
which the there is a desire to keep on record. Then, there is the
added burden of having to do what is referred to as "swivel-chair"
administration.  This is where Heimdallr enters the picture.  Like the
Norse god of the same name, it will be a system which looks into other
worlds and builds bridges between them.

While some systems like Ansible are great for performing some of this,
it still does not completely cover the problem fully. It is great for
connecting to systems to which SSH connectivity exists, but then there
is the issue of connecting to other systems, such as those which use
REST, SOAP, SNMP or other network protocols, and have their own APIs.
The vision for this utility is one which allows it to be the source of
truth for certain information about an administrative domain, while
delegating that authority to certain other utilities as the source of
truth for certain other information. In doing so, it will bridge
together these utilities where those utilities do not already
communicate, helping to maintain a consistent view.

Some of the few utilities and services which are intended to be
brought under the umbrella of this utility include:

- [Ansible](https://www.ansible.com) --- Information gathering and task/command execution
- [Cobbler](https://cobbler.github.io/) --- Initial system provisioning, and maintaining DHCP
- [phpIPAM](https://phpipam.net/) --- Network/IP Address Management
- [FreeNAS](https://freenas.org/) --- File Storage

In addition, there is the intent that Heimdallr will perform certain
tasks which are complex enough that they are not readily done with
Ansible. A primary example of this is migrating directories/partitions
from one system to another, more securely than a simple
[rsync](https://rsync.samba.org/) would do on its own.

For some of this, the intent is to provide the functionality via a web
interface, replacing the web interfaces of services like Cobbler with
a web interface with Heimdallr's own rainbow hues. And for others, the
interface will initially be a command line which will perform the
task, though those too are ultimately intended to be run through the
web interface.

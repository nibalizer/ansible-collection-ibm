
ibm_is_security_group_network_interface_attachment -- Configure IBM Cloud 'ibm_is_security_group_network_interface_attachment' resource
=======================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_security_group_network_interface_attachment' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  security_group (False, str, None)
    (Required for new resource) NA


  name (False, str, None)
    NA


  instance_network_interface (False, str, None)
    NA


  port_speed (False, int, None)
    NA


  primary_ipv4_address (False, str, None)
    NA


  network_interface (False, str, None)
    (Required for new resource) NA


  secondary_address (False, list, None)
    NA


  status (False, str, None)
    NA


  subnet (False, str, None)
    NA


  type (False, str, None)
    NA


  floating_ips (False, list, None)
    NA


  security_groups (False, list, None)
    NA


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)


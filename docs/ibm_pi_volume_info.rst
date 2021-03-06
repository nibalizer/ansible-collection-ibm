
ibm_pi_volume_info -- Retrieve IBM Cloud 'ibm_pi_volume' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_volume' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  shareable (False, bool, None)
    NA


  disk_type (False, str, None)
    NA


  pi_volume_name (True, str, None)
    Volume Name to be used for pvminstances


  pi_cloud_instance_id (True, str, None)
    NA


  state (False, str, None)
    NA


  size (False, int, None)
    NA


  name (False, str, None)
    NA


  bootable (False, bool, None)
    NA


  creation_date (False, str, None)
    NA


  zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)


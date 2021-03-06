
ibm_resource_key -- Configure IBM Cloud 'ibm_resource_key' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_resource_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  role (False, str, None)
    (Required for new resource) Name of the user role.Valid roles are Writer, Reader, Manager, Administrator, Operator, Viewer, Editor.


  resource_alias_id (False, str, None)
    The id of the resource alias for which to create resource key


  tags (False, list, None)
    NA


  crn (False, str, None)
    crn of resource key


  name (False, str, None)
    (Required for new resource) The name of the resource key


  parameters (False, dict, None)
    Arbitrary parameters to pass. Must be a JSON object


  credentials (False, dict, None)
    Credentials asociated with the key


  status (False, str, None)
    Status of resource key


  resource_instance_id (False, str, None)
    The id of the resource instance for which to create resource key


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)



ibm_service_instance -- Configure IBM Cloud 'ibm_service_instance' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_service_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) A name for the service instance


  space_guid (False, str, None)
    (Required for new resource) The guid of the space in which the instance will be created


  credentials (False, dict, None)
    The service broker-provided credentials to use this service.


  service_plan_guid (False, str, None)
    The uniquie identifier of the service offering plan type


  tags (False, list, None)
    NA


  wait_time_minutes (False, int, 10)
    Define timeout to wait for the service instances to succeeded/deleted etc.


  service (False, str, None)
    (Required for new resource) The name of the service offering like speech_to_text, text_to_speech etc


  service_keys (False, list, None)
    The service keys asociated with the service instance


  parameters (False, dict, None)
    Arbitrary parameters to pass along to the service broker. Must be a JSON object


  plan (False, str, None)
    (Required for new resource) The plan type of the service


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


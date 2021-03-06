#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_database_info
short_description: Retrieve IBM Cloud 'ibm_database' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_database' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    adminpassword:
        description:
            - The admin user id for the instance
        required: False
        type: str
    version:
        description:
            - The database version to provision if specified
        required: False
        type: str
    name:
        description:
            - Resource instance name for example, my Database instance
        required: True
        type: str
    resource_group_id:
        description:
            - The id of the resource group in which the Database instance is present
        required: False
        type: str
    location:
        description:
            - The location or the region in which the Database instance exists
        required: False
        type: str
    groups:
        description:
            - NA
        required: False
        type: list
        elements: dict
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    service:
        description:
            - The name of the Cloud Internet database service
        required: False
        type: str
    plan:
        description:
            - The plan type of the Database instance
        required: False
        type: str
    status:
        description:
            - The resource instance status
        required: False
        type: str
    tags:
        description:
            - NA
        required: False
        type: list
        elements: str
    users:
        description:
            - NA
        required: False
        type: list
        elements: dict
    whitelist:
        description:
            - NA
        required: False
        type: list
        elements: dict
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource
        required: False
        type: str
    guid:
        description:
            - Unique identifier of resource instance
        required: False
        type: str
    adminuser:
        description:
            - The admin user id for the instance
        required: False
        type: str
    members_memory_allocation_mb:
        description:
            - Memory allocation required for cluster
        required: False
        type: int
    members_disk_allocation_mb:
        description:
            - Disk allocation required for cluster
        required: False
        type: int
    connectionstrings:
        description:
            - NA
        required: False
        type: list
        elements: dict
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'adminpassword',
    'version',
    'name',
    'resource_group_id',
    'location',
    'groups',
    'resource_name',
    'resource_group_name',
    'service',
    'plan',
    'status',
    'tags',
    'users',
    'whitelist',
    'resource_crn',
    'resource_controller_url',
    'guid',
    'adminuser',
    'members_memory_allocation_mb',
    'members_disk_allocation_mb',
    'connectionstrings',
    'resource_status',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    adminpassword=dict(
        required=False,
        type='str'),
    version=dict(
        required=False,
        type='str'),
    name=dict(
        required=True,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    location=dict(
        required=False,
        type='str'),
    groups=dict(
        required=False,
        elements='',
        type='list'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    service=dict(
        required=False,
        type='str'),
    plan=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    users=dict(
        required=False,
        elements='',
        type='list'),
    whitelist=dict(
        required=False,
        elements='',
        type='list'),
    resource_crn=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    guid=dict(
        required=False,
        type='str'),
    adminuser=dict(
        required=False,
        type='str'),
    members_memory_allocation_mb=dict(
        required=False,
        type='int'),
    members_disk_allocation_mb=dict(
        required=False,
        type='int'),
    connectionstrings=dict(
        required=False,
        elements='',
        type='list'),
    resource_status=dict(
        required=False,
        type='str'),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_database',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.4.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

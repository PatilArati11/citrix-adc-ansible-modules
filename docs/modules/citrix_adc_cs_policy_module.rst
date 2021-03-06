:orphan:

.. _citrix_adc_cs_policy_module:

citrix_adc_cs_policy - Manage content switching policy
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage content switching policy.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - action
      -
      - Content switching action that names the target load balancing virtual server to which the traffic is switched.
    * - domain
      -
      - The domain name. The string value can range to 63 characters.

        Minimum length = 1
    * - instance_ip

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - nitro_auth_token

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol
      - Choices:

          - http (*default*)
          - https
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - policyname
      -
      - Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore, hash ``#``, period ``.``, space `` ``, colon ``:``, at sign ``@``, equal sign ``=``, and hyphen ``-`` characters. Cannot be changed after a policy is created.

        The following requirement applies only to the NetScaler CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my policy or my policy).

        Minimum length = 1
    * - rule
      -
      - Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.

        Note:

        Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - state
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - url
      -
      - URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: ``[[prefix] [*]] [.suffix]``.

        Minimum length = 1

        Maximum length = 208
    * - validate_certs
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Create url cs policy
      delegate_to: localhost
      citrix_adc_cs_policy:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
        state: present
    
        policyname: policy_1
        url: /example/


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'url': 'difference. ours: (str) example1 other: (str) /example1'}
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Could not load nitro python sdk

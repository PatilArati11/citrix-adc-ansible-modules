import os
import copy
import json
import yaml
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader

from helpers import calculate_transforms_for_attribute, calculate_doc_list, calculate_attributes_config_dict


HERE = os.path.abspath(os.path.dirname(__file__))

def populate_template(template_dir, **kwargs):
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(template_dir),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template('citrix_adm_mpsgroup.template')
    stream = template.stream(**kwargs)

    #output_file = 'netscaler_appfw_profile.py'
    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adm_mpsgroup.py')
    stream.dump(
        output_file,
        encoding='utf-8'
    )

def main():

    # Find template dir
    template_dir = os.path.join(HERE, '..', 'templates', 'citrix_adm')
    if not os.path.exists(template_dir):
        raise Exception('Cannot find template dir')

    # Find nscli json data dir
    json_dir = os.path.join(HERE, '..', 'nitro_api_defines/kamet/appfw')
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')


    yaml_dir = os.path.join(HERE, '..', 'citrix_adm_api_defines', 'kamet')
    if not os.path.exists(yaml_dir):
        raise Exception('Cannot find json dir')

    main_yaml_file = os.path.join(yaml_dir, 'mpsgroup.yaml')
    with open(main_yaml_file, 'r') as fh:
        main_object_attributes = yaml.load(fh)

    main_object_doc_list = calculate_doc_list(main_object_attributes)
    print('main_object_doc_list %s' % json.dumps(main_object_doc_list, indent=4))

    attributes_config_list = []

    main_data = calculate_attributes_config_dict('mpsgroup', main_object_attributes)

    main_data['transforms'] = OrderedDict([
        ('enable_session_timeout', 'lambda v: "true" if v else "false"'),
        ('allow_application_only', 'lambda v: "true" if v else "false"'),
        ('assign_all_apps', 'lambda v: "true" if v else "false"'),
        ('assign_all_devices', 'lambda v: "true" if v else "false"'),
    ])

    attributes_config_list.append(main_data)

    print('attributes_config_list: %s' % json.dumps(attributes_config_list, indent=4))


    # Populate the template
    populate_template(
        template_dir,
        main_object_doc_list=main_object_doc_list,
        main_nitro_class='mpsgroup',
        main_object_put_id='id',
        attributes_config_list=attributes_config_list,
    )



if __name__ == '__main__':
    main()

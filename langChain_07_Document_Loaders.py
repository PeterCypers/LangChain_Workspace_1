'''
Document loaders ingest raw data from sources into LangChain Document objects.

python -m pip install -qU langchain-community beautifulsoup4
'''
# webpage to load:
# https://swagger.io/specification/

testwebsite = "https://petercypers.github.io/html_keyword_list/"
OAS = "https://swagger.io/specification/"

######### Set-API-Env-Variable ##############
from keys.anthropic_key import get_claude_key
ANTHROPIC_KEY = get_claude_key()

import os
os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_KEY
os.environ["USER_AGENT"] = "MyLangChainApp/1.0"
#############################################

####################################################################################
##                             Web-Base Loader                                    ##
##  https://docs.langchain.com/oss/python/integrations/document_loaders/web_base  ##
####################################################################################

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(OAS)

# bypass SSL
loader.requests_kwargs = {'verify':False}

''' multiple pages:
loader_multiple_pages = WebBaseLoader(
    ["https://www.example.com/", "https://google.com"]
)
'''
docs = loader.load()

print(docs[0].metadata)
# InsecureRequestWarning: USER_AGENT environment variable not set, consider setting it to identify your requests. -> resolved
# InsecureRequestWarning: Unverified HTTPS request is being made to host 'petercypers.github.io'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings -> not yet resolved
print(docs[0].page_content[:100])
''' print(dir(docs[0])) output:
['__abstractmethods__', '__annotations__', '__class__', '__class_getitem__', '__class_vars__', '__copy__',
 '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__fields__', '__fields_set__',
 '__format__', '__ge__', '__get_pydantic_core_schema__', '__get_pydantic_json_schema__', '__getattr__',
 '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__pretty__', '__private_attributes__',
 '__pydantic_complete__', '__pydantic_computed_fields__', '__pydantic_core_schema__',
 '__pydantic_custom_init__', '__pydantic_decorators__', '__pydantic_extra__', '__pydantic_fields__',
 '__pydantic_fields_set__', '__pydantic_generic_metadata__', '__pydantic_init_subclass__',
 '__pydantic_on_complete__', '__pydantic_parent_namespace__', '__pydantic_post_init__',
 '__pydantic_private__', '__pydantic_root_model__', '__pydantic_serializer__',
 '__pydantic_setattr_handlers__', '__pydantic_validator__', '__reduce__', '__reduce_ex__', '__replace__',
 '__repr__', '__repr_args__', '__repr_name__', '__repr_recursion__', '__repr_str__', '__rich_repr__',
 '__setattr__', '__setstate__', '__signature__', '__sizeof__', '__slots__', '__str__',
 '__subclasshook__', '__weakref__', '_abc_impl', '_calculate_keys', '_copy_and_set_values', '_get_value',
 '_iter', '_setattr_handler', 'construct', 'copy', 'dict', 'from_orm', 'get_lc_namespace', 'id',
 'is_lc_serializable', 'json', 'lc_attributes', 'lc_id', 'lc_secrets', 'metadata',
 'model_computed_fields', 'model_config', 'model_construct', 'model_copy', 'model_dump',
 'model_dump_json', 'model_extra', 'model_fields', 'model_fields_set', 'model_json_schema',
 'model_parametrized_name', 'model_post_init', 'model_rebuild', 'model_validate',
 'model_validate_json', 'model_validate_strings', 'page_content', 'parse_file', 'parse_obj',
 'parse_raw', 'schema', 'schema_json', 'to_json', 'to_json_not_implemented', 'type',
 'update_forward_refs', 'validate']
 '''
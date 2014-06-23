import pkg_resources

from django.template import Context, Template

def load_resource(resource_path):
    resource_content = resource_content = pkg_resources.resource_string(__name__, resource_path)
    return unicode(resource_content)

def render_template(template_path, context={}):
    template_str = load_resource(template_path)
    template = Template(template_str)
    return template.render(Context(context))

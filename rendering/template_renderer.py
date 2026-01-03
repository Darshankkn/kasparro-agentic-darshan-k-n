def render(template, content):
    for k, v in content.items():
        template[k] = v
    return template

from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template-ospf.j2")

with open("ospf.yml") as f:
    data = yaml.safe_load(f)

print(template.render(routers=data["routers"]))

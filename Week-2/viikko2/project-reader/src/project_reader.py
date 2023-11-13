from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        toml_data = toml.loads(content)

        name = toml_data.get('tool', {}).get('poetry', {}).get('name', '')
        description = toml_data.get('tool', {}).get('poetry', {}).get('description', '')
        license = toml_data.get('tool', {}).get('poetry', {}).get('license', '')
        authors = toml_data.get('tool', {}).get('poetry', {}).get('authors', [])
        dependencies = toml_data.get('tool', {}).get('poetry', {}).get('dependencies', {})
        dev_dependencies = toml_data.get('tool', {}).get('poetry', {}).get('group', {}).get('dev', {}).get('dependencies', {})

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        print('Name:', name)
        print('Description:', description)
        print('License:', license)
        print('Authors:')
        for author in authors:
            print('- ', author)
        print('Dependencies:')
        for d in dependencies:
            print('- ', d)
        print('Development Dependencies:')
        for d in dev_dependencies:
            print('- ', d)
        
        return None

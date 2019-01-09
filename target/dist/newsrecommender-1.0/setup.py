#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'newsrecommender',
        version = '1.0',
        description = 'News recommender',
        long_description = 'An example PyBuilder / Git project for project management\nand file version control. See blog post at http://bit.ly/2QY65wO for a\nmore through explanation.',
        author = 'Zia Muhammad',
        author_email = 'zia-muhammad@outlook.com',
        license = 'None',
        url = 'https://github.com/Ziasafi/newsrecommender.git',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = [
            'article_to_json',
            'demo',
            'recommender_server',
            'news_articles_processor'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )

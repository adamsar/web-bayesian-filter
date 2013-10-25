try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Web Bayes',
    version='0.1',
    description="""Quick project for learning how to implement
    a bayesian filter for test data""",
    author='Andrew Adams',
    author_email='adamsar@gmail.com',
    url='http://www.andrew-adams.net',
    install_requires=[
        'celery',
        'httplib2',
        'feedparser',
        'numpy',
        'scipy',
        'scikit-learn'
    ],
    setup_requires=[],
    packages=['web_bayes'],
    include_package_data=True,
    zip_safe=False
)

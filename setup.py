from setuptools import setup

setup(
    name='jenkins-jobs-mattermost',
    version='0.1.0',
    description='Jenkins Job Builder Mattermost Notifier',
    url='https://github.com/jovandeginste/jenkins-jobs-mattermost',
    author='Jo Vandeginste',
    author_email='jo.vandeginste@kuleuven.be',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.publishers': [
            'mattermost = jenkins_jobs_mattermost.mattermost:mattermost_publisher']},
    packages=['jenkins_jobs_mattermost'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
